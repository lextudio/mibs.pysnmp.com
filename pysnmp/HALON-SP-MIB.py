# SNMP MIB module (HALON-SP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HALON-SP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:00 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

halonSecuritySP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33234, 1, 1)
)
halonSecuritySP.setRevisions(
        ("2013-02-07 11:32",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HalonSecurity_ObjectIdentity = ObjectIdentity
halonSecurity = _HalonSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33234)
)
_HalonSecurityProducts_ObjectIdentity = ObjectIdentity
halonSecurityProducts = _HalonSecurityProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33234, 1)
)
_HalonSecuritySPObjects_ObjectIdentity = ObjectIdentity
halonSecuritySPObjects = _HalonSecuritySPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33234, 1, 1, 1)
)
_SerialNumber_Type = OctetString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 1),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_ConfigurationRevision_Type = Integer32
_ConfigurationRevision_Object = MibScalar
configurationRevision = _ConfigurationRevision_Object(
    (1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 2),
    _ConfigurationRevision_Type()
)
configurationRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationRevision.setStatus("current")
_MailQueueLength_Type = Counter64
_MailQueueLength_Object = MibScalar
mailQueueLength = _MailQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 3),
    _MailQueueLength_Type()
)
mailQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mailQueueLength.setStatus("current")
_QuarantinedMessages_Type = Counter64
_QuarantinedMessages_Object = MibScalar
quarantinedMessages = _QuarantinedMessages_Object(
    (1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 4),
    _QuarantinedMessages_Type()
)
quarantinedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quarantinedMessages.setStatus("current")
_StatTable_Object = MibTable
statTable = _StatTable_Object(
    (1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    statTable.setStatus("current")
_StatEntry_Object = MibTableRow
statEntry = _StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1)
)
statEntry.setIndexNames(
    (0, "HALON-SP-MIB", "statKey1Index"),
    (0, "HALON-SP-MIB", "statKey2Index"),
    (0, "HALON-SP-MIB", "statKey3Index"),
)
if mibBuilder.loadTexts:
    statEntry.setStatus("current")
_StatKey1Index_Type = OctetString
_StatKey1Index_Object = MibTableColumn
statKey1Index = _StatKey1Index_Object(
    (1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 1),
    _StatKey1Index_Type()
)
statKey1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statKey1Index.setStatus("current")
_StatKey2Index_Type = OctetString
_StatKey2Index_Object = MibTableColumn
statKey2Index = _StatKey2Index_Object(
    (1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 2),
    _StatKey2Index_Type()
)
statKey2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statKey2Index.setStatus("current")
_StatKey3Index_Type = OctetString
_StatKey3Index_Object = MibTableColumn
statKey3Index = _StatKey3Index_Object(
    (1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 3),
    _StatKey3Index_Type()
)
statKey3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statKey3Index.setStatus("current")
_StatCount_Type = Counter64
_StatCount_Object = MibTableColumn
statCount = _StatCount_Object(
    (1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 4),
    _StatCount_Type()
)
statCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCount.setStatus("current")
_StatCreated_Type = Integer32
_StatCreated_Object = MibTableColumn
statCreated = _StatCreated_Object(
    (1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 5),
    _StatCreated_Type()
)
statCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCreated.setStatus("current")
_StatUpdated_Type = Integer32
_StatUpdated_Object = MibTableColumn
statUpdated = _StatUpdated_Object(
    (1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 6),
    _StatUpdated_Type()
)
statUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statUpdated.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HALON-SP-MIB",
    **{"halonSecurity": halonSecurity,
       "halonSecurityProducts": halonSecurityProducts,
       "halonSecuritySP": halonSecuritySP,
       "halonSecuritySPObjects": halonSecuritySPObjects,
       "serialNumber": serialNumber,
       "configurationRevision": configurationRevision,
       "mailQueueLength": mailQueueLength,
       "quarantinedMessages": quarantinedMessages,
       "statTable": statTable,
       "statEntry": statEntry,
       "statKey1Index": statKey1Index,
       "statKey2Index": statKey2Index,
       "statKey3Index": statKey3Index,
       "statCount": statCount,
       "statCreated": statCreated,
       "statUpdated": statUpdated}
)
