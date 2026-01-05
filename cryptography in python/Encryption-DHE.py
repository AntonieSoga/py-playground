from cryptography.hazmat.primitives.asymmetric import dh

parameters = dh.generate_parameters(generator=2,key_size=2048)

private_key = parameters.generate_private_key()
peer_private_key = parameters.generate_private_key()


shared_key = private_key.exchange(peer_private_key.public_key())

print ("Shared secret established! ✅")