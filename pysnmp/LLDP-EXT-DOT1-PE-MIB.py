# SNMP MIB module (LLDP-EXT-DOT1-PE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LLDP-EXT-DOT1-PE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:03 2024
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

(ifGeneralInformationGroup,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifGeneralInformationGroup")

(lldpXdot1StandAloneExtensions,) = mibBuilder.importSymbols(
    "LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB",
    "lldpXdot1StandAloneExtensions")

(lldpV2Extensions,
 lldpV2LocPortIfIndex,
 lldpV2PortConfigEntry,
 lldpV2RemIndex,
 lldpV2RemLocalDestMACAddress,
 lldpV2RemLocalIfIndex,
 lldpV2RemTimeMark) = mibBuilder.importSymbols(
    "LLDP-V2-MIB",
    "lldpV2Extensions",
    "lldpV2LocPortIfIndex",
    "lldpV2PortConfigEntry",
    "lldpV2RemIndex",
    "lldpV2RemLocalDestMACAddress",
    "lldpV2RemLocalIfIndex",
    "lldpV2RemTimeMark")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lldpXDot1PEExtensions = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2)
)
lldpXDot1PEExtensions.setRevisions(
        ("2012-01-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LldpXdot1PeMIB_ObjectIdentity = ObjectIdentity
lldpXdot1PeMIB = _LldpXdot1PeMIB_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1)
)
_LldpXdot1PeObjects_ObjectIdentity = ObjectIdentity
lldpXdot1PeObjects = _LldpXdot1PeObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1)
)
_LldpXdot1PeConfig_ObjectIdentity = ObjectIdentity
lldpXdot1PeConfig = _LldpXdot1PeConfig_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 1)
)
_LldpXdot1PeConfigPortExtensionTable_Object = MibTable
lldpXdot1PeConfigPortExtensionTable = _LldpXdot1PeConfigPortExtensionTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1PeConfigPortExtensionTable.setStatus("current")
_LldpXdot1PeConfigPortExtensionEntry_Object = MibTableRow
lldpXdot1PeConfigPortExtensionEntry = _LldpXdot1PeConfigPortExtensionEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1PeConfigPortExtensionEntry.setStatus("current")


class _LldpXdot1PeConfigPortExtensionTxEnable_Type(TruthValue):
    """Custom type lldpXdot1PeConfigPortExtensionTxEnable based on TruthValue"""


_LldpXdot1PeConfigPortExtensionTxEnable_Object = MibTableColumn
lldpXdot1PeConfigPortExtensionTxEnable = _LldpXdot1PeConfigPortExtensionTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 1, 1, 1, 1),
    _LldpXdot1PeConfigPortExtensionTxEnable_Type()
)
lldpXdot1PeConfigPortExtensionTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1PeConfigPortExtensionTxEnable.setStatus("current")
_LldpXdot1PeLocalData_ObjectIdentity = ObjectIdentity
lldpXdot1PeLocalData = _LldpXdot1PeLocalData_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 2)
)
_LldpXdot1PeLocPortExtensionTable_Object = MibTable
lldpXdot1PeLocPortExtensionTable = _LldpXdot1PeLocPortExtensionTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1PeLocPortExtensionTable.setStatus("current")
_LldpXdot1PeLocPortExtensionEntry_Object = MibTableRow
lldpXdot1PeLocPortExtensionEntry = _LldpXdot1PeLocPortExtensionEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 2, 1, 1)
)
lldpXdot1PeLocPortExtensionEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1PeLocPortExtensionEntry.setStatus("current")


class _LldpXdot1PeLocPECascadePortPriority_Type(Unsigned32):
    """Custom type lldpXdot1PeLocPECascadePortPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LldpXdot1PeLocPECascadePortPriority_Type.__name__ = "Unsigned32"
_LldpXdot1PeLocPECascadePortPriority_Object = MibTableColumn
lldpXdot1PeLocPECascadePortPriority = _LldpXdot1PeLocPECascadePortPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 2, 1, 1, 1),
    _LldpXdot1PeLocPECascadePortPriority_Type()
)
lldpXdot1PeLocPECascadePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1PeLocPECascadePortPriority.setStatus("current")
_LldpXdot1PeLocPEAddress_Type = MacAddress
_LldpXdot1PeLocPEAddress_Object = MibTableColumn
lldpXdot1PeLocPEAddress = _LldpXdot1PeLocPEAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 2, 1, 1, 2),
    _LldpXdot1PeLocPEAddress_Type()
)
lldpXdot1PeLocPEAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1PeLocPEAddress.setStatus("current")
_LldpXdot1PeLocPECSPAddress_Type = MacAddress
_LldpXdot1PeLocPECSPAddress_Object = MibTableColumn
lldpXdot1PeLocPECSPAddress = _LldpXdot1PeLocPECSPAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 2, 1, 1, 3),
    _LldpXdot1PeLocPECSPAddress_Type()
)
lldpXdot1PeLocPECSPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1PeLocPECSPAddress.setStatus("current")
_LldpXdot1PeRemoteData_ObjectIdentity = ObjectIdentity
lldpXdot1PeRemoteData = _LldpXdot1PeRemoteData_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 3)
)
_LldpXdot1PeRemPortExtensionTable_Object = MibTable
lldpXdot1PeRemPortExtensionTable = _LldpXdot1PeRemPortExtensionTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1PeRemPortExtensionTable.setStatus("current")
_LldpXdot1PeRemPortExtensionEntry_Object = MibTableRow
lldpXdot1PeRemPortExtensionEntry = _LldpXdot1PeRemPortExtensionEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 3, 1, 1)
)
lldpXdot1PeRemPortExtensionEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1PeRemPortExtensionEntry.setStatus("current")


class _LldpXdot1PeRemPECascadePortPriority_Type(Unsigned32):
    """Custom type lldpXdot1PeRemPECascadePortPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LldpXdot1PeRemPECascadePortPriority_Type.__name__ = "Unsigned32"
_LldpXdot1PeRemPECascadePortPriority_Object = MibTableColumn
lldpXdot1PeRemPECascadePortPriority = _LldpXdot1PeRemPECascadePortPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 3, 1, 1, 1),
    _LldpXdot1PeRemPECascadePortPriority_Type()
)
lldpXdot1PeRemPECascadePortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1PeRemPECascadePortPriority.setStatus("current")
_LldpXdot1PeRemPEAddress_Type = MacAddress
_LldpXdot1PeRemPEAddress_Object = MibTableColumn
lldpXdot1PeRemPEAddress = _LldpXdot1PeRemPEAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 3, 1, 1, 2),
    _LldpXdot1PeRemPEAddress_Type()
)
lldpXdot1PeRemPEAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1PeRemPEAddress.setStatus("current")
_LldpXdot1PeRemPECSPAddress_Type = MacAddress
_LldpXdot1PeRemPECSPAddress_Object = MibTableColumn
lldpXdot1PeRemPECSPAddress = _LldpXdot1PeRemPECSPAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 1, 1, 3, 1, 1, 3),
    _LldpXdot1PeRemPECSPAddress_Type()
)
lldpXdot1PeRemPECSPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1PeRemPECSPAddress.setStatus("current")
_LldpXdot1PeConformance_ObjectIdentity = ObjectIdentity
lldpXdot1PeConformance = _LldpXdot1PeConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 2)
)
_LldpXdot1PeCompliances_ObjectIdentity = ObjectIdentity
lldpXdot1PeCompliances = _LldpXdot1PeCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 2, 1)
)
_LldpXdot1PeGroups_ObjectIdentity = ObjectIdentity
lldpXdot1PeGroups = _LldpXdot1PeGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 2, 2)
)
lldpV2PortConfigEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-PE-MIB",
     "lldpXdot1PeConfigPortExtensionEntry")
)
lldpXdot1PeConfigPortExtensionEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())

# Managed Objects groups

lldpXdot1PeGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 2, 2, 1)
)
lldpXdot1PeGroup.setObjects(
      *(("LLDP-EXT-DOT1-PE-MIB", "lldpXdot1PeConfigPortExtensionTxEnable"),
        ("LLDP-EXT-DOT1-PE-MIB", "lldpXdot1PeLocPECascadePortPriority"),
        ("LLDP-EXT-DOT1-PE-MIB", "lldpXdot1PeLocPEAddress"),
        ("LLDP-EXT-DOT1-PE-MIB", "lldpXdot1PeLocPECSPAddress"),
        ("LLDP-EXT-DOT1-PE-MIB", "lldpXdot1PeRemPECascadePortPriority"),
        ("LLDP-EXT-DOT1-PE-MIB", "lldpXdot1PeRemPEAddress"),
        ("LLDP-EXT-DOT1-PE-MIB", "lldpXdot1PeRemPECSPAddress"))
)
if mibBuilder.loadTexts:
    lldpXdot1PeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lldpXdot1PeCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1PeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LLDP-EXT-DOT1-PE-MIB",
    **{"lldpXDot1PEExtensions": lldpXDot1PEExtensions,
       "lldpXdot1PeMIB": lldpXdot1PeMIB,
       "lldpXdot1PeObjects": lldpXdot1PeObjects,
       "lldpXdot1PeConfig": lldpXdot1PeConfig,
       "lldpXdot1PeConfigPortExtensionTable": lldpXdot1PeConfigPortExtensionTable,
       "lldpXdot1PeConfigPortExtensionEntry": lldpXdot1PeConfigPortExtensionEntry,
       "lldpXdot1PeConfigPortExtensionTxEnable": lldpXdot1PeConfigPortExtensionTxEnable,
       "lldpXdot1PeLocalData": lldpXdot1PeLocalData,
       "lldpXdot1PeLocPortExtensionTable": lldpXdot1PeLocPortExtensionTable,
       "lldpXdot1PeLocPortExtensionEntry": lldpXdot1PeLocPortExtensionEntry,
       "lldpXdot1PeLocPECascadePortPriority": lldpXdot1PeLocPECascadePortPriority,
       "lldpXdot1PeLocPEAddress": lldpXdot1PeLocPEAddress,
       "lldpXdot1PeLocPECSPAddress": lldpXdot1PeLocPECSPAddress,
       "lldpXdot1PeRemoteData": lldpXdot1PeRemoteData,
       "lldpXdot1PeRemPortExtensionTable": lldpXdot1PeRemPortExtensionTable,
       "lldpXdot1PeRemPortExtensionEntry": lldpXdot1PeRemPortExtensionEntry,
       "lldpXdot1PeRemPECascadePortPriority": lldpXdot1PeRemPECascadePortPriority,
       "lldpXdot1PeRemPEAddress": lldpXdot1PeRemPEAddress,
       "lldpXdot1PeRemPECSPAddress": lldpXdot1PeRemPECSPAddress,
       "lldpXdot1PeConformance": lldpXdot1PeConformance,
       "lldpXdot1PeCompliances": lldpXdot1PeCompliances,
       "lldpXdot1PeCompliance": lldpXdot1PeCompliance,
       "lldpXdot1PeGroups": lldpXdot1PeGroups,
       "lldpXdot1PeGroup": lldpXdot1PeGroup}
)
