# SNMP MIB module (ELTEX-MES-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-CFM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:32 2024
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

(eltMesMng,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMesMng")

(Dot1agCfmMpDirection,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMpDirection")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrNone")

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
 RowStatus,
 TAddress,
 TDomain,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

eltMesCfmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 774)
)
eltMesCfmMIB.setRevisions(
        ("2013-03-19 00:00",
         "2015-11-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesCfmNotifications_ObjectIdentity = ObjectIdentity
eltMesCfmNotifications = _EltMesCfmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 774, 0)
)
_EltMesCfmMIBObjects_ObjectIdentity = ObjectIdentity
eltMesCfmMIBObjects = _EltMesCfmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 774, 1)
)
_EltMesCfmMd_ObjectIdentity = ObjectIdentity
eltMesCfmMd = _EltMesCfmMd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 774, 1, 1)
)
_EltCfmMdTable_Object = MibTable
eltCfmMdTable = _EltCfmMdTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 774, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltCfmMdTable.setStatus("deprecated")
_EltCfmMdEntry_Object = MibTableRow
eltCfmMdEntry = _EltCfmMdEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 774, 1, 1, 1, 1)
)
eltCfmMdEntry.setIndexNames(
    (0, "ELTEX-MES-CFM-MIB", "eltCfmMdName"),
)
if mibBuilder.loadTexts:
    eltCfmMdEntry.setStatus("deprecated")


class _EltCfmMdName_Type(OctetString):
    """Custom type eltCfmMdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EltCfmMdName_Type.__name__ = "OctetString"
_EltCfmMdName_Object = MibTableColumn
eltCfmMdName = _EltCfmMdName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 774, 1, 1, 1, 1, 1),
    _EltCfmMdName_Type()
)
eltCfmMdName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltCfmMdName.setStatus("deprecated")


class _EltCfmMdIndex_Type(Unsigned32):
    """Custom type eltCfmMdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EltCfmMdIndex_Type.__name__ = "Unsigned32"
_EltCfmMdIndex_Object = MibTableColumn
eltCfmMdIndex = _EltCfmMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 774, 1, 1, 1, 1, 2),
    _EltCfmMdIndex_Type()
)
eltCfmMdIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltCfmMdIndex.setStatus("deprecated")
_EltCfmMdRowStatus_Type = RowStatus
_EltCfmMdRowStatus_Object = MibTableColumn
eltCfmMdRowStatus = _EltCfmMdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 774, 1, 1, 1, 1, 3),
    _EltCfmMdRowStatus_Type()
)
eltCfmMdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltCfmMdRowStatus.setStatus("deprecated")
_EltMesCfmMa_ObjectIdentity = ObjectIdentity
eltMesCfmMa = _EltMesCfmMa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 774, 1, 2)
)
_EltCfmMaTable_Object = MibTable
eltCfmMaTable = _EltCfmMaTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 774, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltCfmMaTable.setStatus("deprecated")
_EltCfmMaEntry_Object = MibTableRow
eltCfmMaEntry = _EltCfmMaEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 774, 1, 2, 1, 1)
)
eltCfmMaEntry.setIndexNames(
    (0, "ELTEX-MES-CFM-MIB", "eltCfmMdIndex"),
    (0, "ELTEX-MES-CFM-MIB", "eltCfmMaIndex"),
)
if mibBuilder.loadTexts:
    eltCfmMaEntry.setStatus("deprecated")


class _EltCfmMaIndex_Type(Unsigned32):
    """Custom type eltCfmMaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EltCfmMaIndex_Type.__name__ = "Unsigned32"
_EltCfmMaIndex_Object = MibTableColumn
eltCfmMaIndex = _EltCfmMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 774, 1, 2, 1, 1, 1),
    _EltCfmMaIndex_Type()
)
eltCfmMaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltCfmMaIndex.setStatus("deprecated")
_EltCfmMaDirection_Type = Dot1agCfmMpDirection
_EltCfmMaDirection_Object = MibTableColumn
eltCfmMaDirection = _EltCfmMaDirection_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 774, 1, 2, 1, 1, 2),
    _EltCfmMaDirection_Type()
)
eltCfmMaDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltCfmMaDirection.setStatus("deprecated")
_EltCfmMaRowStatus_Type = RowStatus
_EltCfmMaRowStatus_Object = MibTableColumn
eltCfmMaRowStatus = _EltCfmMaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 774, 1, 2, 1, 1, 3),
    _EltCfmMaRowStatus_Type()
)
eltCfmMaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltCfmMaRowStatus.setStatus("deprecated")
_EltMesCfmConformance_ObjectIdentity = ObjectIdentity
eltMesCfmConformance = _EltMesCfmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 774, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-CFM-MIB",
    **{"eltMesCfmMIB": eltMesCfmMIB,
       "eltMesCfmNotifications": eltMesCfmNotifications,
       "eltMesCfmMIBObjects": eltMesCfmMIBObjects,
       "eltMesCfmMd": eltMesCfmMd,
       "eltCfmMdTable": eltCfmMdTable,
       "eltCfmMdEntry": eltCfmMdEntry,
       "eltCfmMdName": eltCfmMdName,
       "eltCfmMdIndex": eltCfmMdIndex,
       "eltCfmMdRowStatus": eltCfmMdRowStatus,
       "eltMesCfmMa": eltMesCfmMa,
       "eltCfmMaTable": eltCfmMaTable,
       "eltCfmMaEntry": eltCfmMaEntry,
       "eltCfmMaIndex": eltCfmMaIndex,
       "eltCfmMaDirection": eltCfmMaDirection,
       "eltCfmMaRowStatus": eltCfmMaRowStatus,
       "eltMesCfmConformance": eltMesCfmConformance}
)
