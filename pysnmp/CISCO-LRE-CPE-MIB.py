# SNMP MIB module (CISCO-LRE-CPE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LRE-CPE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:09 2024
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

(dot1dTpFdbAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dTpFdbAddress")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLreCpeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 340)
)
ciscoLreCpeMIB.setRevisions(
        ("2003-03-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ClreCpeMIBNotifications_ObjectIdentity = ObjectIdentity
clreCpeMIBNotifications = _ClreCpeMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 340, 0)
)
_ClreCpeMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
clreCpeMIBNotificationsPrefix = _ClreCpeMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 340, 0, 0)
)
_CiscoLreCpeMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLreCpeMIBObjects = _CiscoLreCpeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 340, 1)
)
_ClreCpeDot1dTp_ObjectIdentity = ObjectIdentity
clreCpeDot1dTp = _ClreCpeDot1dTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 1)
)
_ClreCpeDot1dTpFdbTable_Object = MibTable
clreCpeDot1dTpFdbTable = _ClreCpeDot1dTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 1, 1)
)
if mibBuilder.loadTexts:
    clreCpeDot1dTpFdbTable.setStatus("current")
_ClreCpeDot1dTpFdbEntry_Object = MibTableRow
clreCpeDot1dTpFdbEntry = _ClreCpeDot1dTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 1, 1, 1)
)
clreCpeDot1dTpFdbEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dTpFdbAddress"),
)
if mibBuilder.loadTexts:
    clreCpeDot1dTpFdbEntry.setStatus("current")
_ClreCpeDot1dBasePortIfIndex_Type = InterfaceIndex
_ClreCpeDot1dBasePortIfIndex_Object = MibTableColumn
clreCpeDot1dBasePortIfIndex = _ClreCpeDot1dBasePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 1, 1, 1, 1),
    _ClreCpeDot1dBasePortIfIndex_Type()
)
clreCpeDot1dBasePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clreCpeDot1dBasePortIfIndex.setStatus("current")
_ClreCpePort_ObjectIdentity = ObjectIdentity
clreCpePort = _ClreCpePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 2)
)
_ClreCpePortTable_Object = MibTable
clreCpePortTable = _ClreCpePortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 2, 1)
)
if mibBuilder.loadTexts:
    clreCpePortTable.setStatus("current")
_ClreCpePortEntry_Object = MibTableRow
clreCpePortEntry = _ClreCpePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 2, 1, 1)
)
clreCpePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    clreCpePortEntry.setStatus("current")


class _ClreCpePortAdminStatus_Type(Integer32):
    """Custom type clreCpePortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_ClreCpePortAdminStatus_Type.__name__ = "Integer32"
_ClreCpePortAdminStatus_Object = MibTableColumn
clreCpePortAdminStatus = _ClreCpePortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 2, 1, 1, 1),
    _ClreCpePortAdminStatus_Type()
)
clreCpePortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clreCpePortAdminStatus.setStatus("current")


class _ClreCpePortAdminSpeed_Type(Integer32):
    """Custom type clreCpePortAdminSpeed based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10000000,
              100000000)
        )
    )
    namedValues = NamedValues(
        *(("autoDetect", 1),
          ("s10000000", 10000000),
          ("s100000000", 100000000))
    )


_ClreCpePortAdminSpeed_Type.__name__ = "Integer32"
_ClreCpePortAdminSpeed_Object = MibTableColumn
clreCpePortAdminSpeed = _ClreCpePortAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 2, 1, 1, 2),
    _ClreCpePortAdminSpeed_Type()
)
clreCpePortAdminSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clreCpePortAdminSpeed.setStatus("current")


class _ClreCpePortAdminDuplex_Type(Integer32):
    """Custom type clreCpePortAdminDuplex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoDetect", 1),
          ("fullDuplex", 2),
          ("halfDuplex", 3))
    )


_ClreCpePortAdminDuplex_Type.__name__ = "Integer32"
_ClreCpePortAdminDuplex_Object = MibTableColumn
clreCpePortAdminDuplex = _ClreCpePortAdminDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 2, 1, 1, 3),
    _ClreCpePortAdminDuplex_Type()
)
clreCpePortAdminDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clreCpePortAdminDuplex.setStatus("current")


class _ClreCpePortAdminProtected_Type(TruthValue):
    """Custom type clreCpePortAdminProtected based on TruthValue"""


_ClreCpePortAdminProtected_Object = MibTableColumn
clreCpePortAdminProtected = _ClreCpePortAdminProtected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 2, 1, 1, 4),
    _ClreCpePortAdminProtected_Type()
)
clreCpePortAdminProtected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clreCpePortAdminProtected.setStatus("current")
_ClreCpePortOperProtected_Type = TruthValue
_ClreCpePortOperProtected_Object = MibTableColumn
clreCpePortOperProtected = _ClreCpePortOperProtected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 340, 1, 2, 1, 1, 5),
    _ClreCpePortOperProtected_Type()
)
clreCpePortOperProtected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clreCpePortOperProtected.setStatus("current")
_ClreCpeMIBConformance_ObjectIdentity = ObjectIdentity
clreCpeMIBConformance = _ClreCpeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 340, 2)
)
_ClreCpeMIBCompliances_ObjectIdentity = ObjectIdentity
clreCpeMIBCompliances = _ClreCpeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 340, 2, 1)
)
_ClreCpeMIBGroups_ObjectIdentity = ObjectIdentity
clreCpeMIBGroups = _ClreCpeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 340, 2, 2)
)

# Managed Objects groups

clreCpeDot1dTpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 340, 2, 2, 1)
)
clreCpeDot1dTpGroup.setObjects(
    ("CISCO-LRE-CPE-MIB", "clreCpeDot1dBasePortIfIndex")
)
if mibBuilder.loadTexts:
    clreCpeDot1dTpGroup.setStatus("current")

clreCpePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 340, 2, 2, 2)
)
clreCpePortGroup.setObjects(
      *(("CISCO-LRE-CPE-MIB", "clreCpePortAdminStatus"),
        ("CISCO-LRE-CPE-MIB", "clreCpePortAdminSpeed"),
        ("CISCO-LRE-CPE-MIB", "clreCpePortAdminDuplex"),
        ("CISCO-LRE-CPE-MIB", "clreCpePortAdminProtected"),
        ("CISCO-LRE-CPE-MIB", "clreCpePortOperProtected"))
)
if mibBuilder.loadTexts:
    clreCpePortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

clreCpeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 340, 2, 1, 1)
)
if mibBuilder.loadTexts:
    clreCpeMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LRE-CPE-MIB",
    **{"ciscoLreCpeMIB": ciscoLreCpeMIB,
       "clreCpeMIBNotifications": clreCpeMIBNotifications,
       "clreCpeMIBNotificationsPrefix": clreCpeMIBNotificationsPrefix,
       "ciscoLreCpeMIBObjects": ciscoLreCpeMIBObjects,
       "clreCpeDot1dTp": clreCpeDot1dTp,
       "clreCpeDot1dTpFdbTable": clreCpeDot1dTpFdbTable,
       "clreCpeDot1dTpFdbEntry": clreCpeDot1dTpFdbEntry,
       "clreCpeDot1dBasePortIfIndex": clreCpeDot1dBasePortIfIndex,
       "clreCpePort": clreCpePort,
       "clreCpePortTable": clreCpePortTable,
       "clreCpePortEntry": clreCpePortEntry,
       "clreCpePortAdminStatus": clreCpePortAdminStatus,
       "clreCpePortAdminSpeed": clreCpePortAdminSpeed,
       "clreCpePortAdminDuplex": clreCpePortAdminDuplex,
       "clreCpePortAdminProtected": clreCpePortAdminProtected,
       "clreCpePortOperProtected": clreCpePortOperProtected,
       "clreCpeMIBConformance": clreCpeMIBConformance,
       "clreCpeMIBCompliances": clreCpeMIBCompliances,
       "clreCpeMIBCompliance": clreCpeMIBCompliance,
       "clreCpeMIBGroups": clreCpeMIBGroups,
       "clreCpeDot1dTpGroup": clreCpeDot1dTpGroup,
       "clreCpePortGroup": clreCpePortGroup}
)
