# SNMP MIB module (PGP-UNIVERSAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PGP-UNIVERSAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:37 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(products,) = mibBuilder.importSymbols(
    "PGP-SMI",
    "products")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

pgpuniversal = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17766, 1, 1)
)
pgpuniversal.setRevisions(
        ("2004-12-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Messaging_ObjectIdentity = ObjectIdentity
messaging = _Messaging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17766, 1, 1, 1)
)
if mibBuilder.loadTexts:
    messaging.setStatus("current")
_MessagesProcessedToday_Type = Integer32
_MessagesProcessedToday_Object = MibScalar
messagesProcessedToday = _MessagesProcessedToday_Object(
    (1, 3, 6, 1, 4, 1, 17766, 1, 1, 1, 1),
    _MessagesProcessedToday_Type()
)
messagesProcessedToday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messagesProcessedToday.setStatus("current")
_MessagesEncryptedToday_Type = Integer32
_MessagesEncryptedToday_Object = MibScalar
messagesEncryptedToday = _MessagesEncryptedToday_Object(
    (1, 3, 6, 1, 4, 1, 17766, 1, 1, 1, 2),
    _MessagesEncryptedToday_Type()
)
messagesEncryptedToday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messagesEncryptedToday.setStatus("current")
_MessagesDecryptedToday_Type = Integer32
_MessagesDecryptedToday_Object = MibScalar
messagesDecryptedToday = _MessagesDecryptedToday_Object(
    (1, 3, 6, 1, 4, 1, 17766, 1, 1, 1, 3),
    _MessagesDecryptedToday_Type()
)
messagesDecryptedToday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messagesDecryptedToday.setStatus("current")
_MessagesProcessedTotal_Type = Integer32
_MessagesProcessedTotal_Object = MibScalar
messagesProcessedTotal = _MessagesProcessedTotal_Object(
    (1, 3, 6, 1, 4, 1, 17766, 1, 1, 1, 4),
    _MessagesProcessedTotal_Type()
)
messagesProcessedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messagesProcessedTotal.setStatus("current")
_MessagesEncryptedTotal_Type = Integer32
_MessagesEncryptedTotal_Object = MibScalar
messagesEncryptedTotal = _MessagesEncryptedTotal_Object(
    (1, 3, 6, 1, 4, 1, 17766, 1, 1, 1, 5),
    _MessagesEncryptedTotal_Type()
)
messagesEncryptedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messagesEncryptedTotal.setStatus("current")
_MessagesDecryptedTotal_Type = Integer32
_MessagesDecryptedTotal_Object = MibScalar
messagesDecryptedTotal = _MessagesDecryptedTotal_Object(
    (1, 3, 6, 1, 4, 1, 17766, 1, 1, 1, 6),
    _MessagesDecryptedTotal_Type()
)
messagesDecryptedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messagesDecryptedTotal.setStatus("current")
_VirusesFoundToday_Type = Integer32
_VirusesFoundToday_Object = MibScalar
virusesFoundToday = _VirusesFoundToday_Object(
    (1, 3, 6, 1, 4, 1, 17766, 1, 1, 1, 7),
    _VirusesFoundToday_Type()
)
virusesFoundToday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virusesFoundToday.setStatus("current")
_MessagesInQueue_Type = Integer32
_MessagesInQueue_Object = MibScalar
messagesInQueue = _MessagesInQueue_Object(
    (1, 3, 6, 1, 4, 1, 17766, 1, 1, 1, 8),
    _MessagesInQueue_Type()
)
messagesInQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messagesInQueue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PGP-UNIVERSAL-MIB",
    **{"pgpuniversal": pgpuniversal,
       "messaging": messaging,
       "messagesProcessedToday": messagesProcessedToday,
       "messagesEncryptedToday": messagesEncryptedToday,
       "messagesDecryptedToday": messagesDecryptedToday,
       "messagesProcessedTotal": messagesProcessedTotal,
       "messagesEncryptedTotal": messagesEncryptedTotal,
       "messagesDecryptedTotal": messagesDecryptedTotal,
       "virusesFoundToday": virusesFoundToday,
       "messagesInQueue": messagesInQueue}
)
