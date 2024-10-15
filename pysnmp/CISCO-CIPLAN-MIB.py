# SNMP MIB module (CISCO-CIPLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CIPLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:28 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoCipLanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 34)
)
ciscoCipLanMIB.setRevisions(
        ("1998-01-06 00:00",
         "1995-04-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CipLanObjects_ObjectIdentity = ObjectIdentity
cipLanObjects = _CipLanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 1)
)
_CipLan_ObjectIdentity = ObjectIdentity
cipLan = _CipLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1)
)
_CipCardLanAdminTable_Object = MibTable
cipCardLanAdminTable = _CipCardLanAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cipCardLanAdminTable.setStatus("current")
_CipCardLanAdminEntry_Object = MibTableRow
cipCardLanAdminEntry = _CipCardLanAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1)
)
cipCardLanAdminEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CIPLAN-MIB", "cipCardLanAdminLanType"),
    (0, "CISCO-CIPLAN-MIB", "cipCardLanAdminLanId"),
)
if mibBuilder.loadTexts:
    cipCardLanAdminEntry.setStatus("current")


class _CipCardLanAdminLanType_Type(Integer32):
    """Custom type cipCardLanAdminLanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fddi", 3),
          ("iso88023csmacd", 1),
          ("iso88025tokenRing", 2))
    )


_CipCardLanAdminLanType_Type.__name__ = "Integer32"
_CipCardLanAdminLanType_Object = MibTableColumn
cipCardLanAdminLanType = _CipCardLanAdminLanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 1),
    _CipCardLanAdminLanType_Type()
)
cipCardLanAdminLanType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipCardLanAdminLanType.setStatus("current")


class _CipCardLanAdminLanId_Type(Integer32):
    """Custom type cipCardLanAdminLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_CipCardLanAdminLanId_Type.__name__ = "Integer32"
_CipCardLanAdminLanId_Object = MibTableColumn
cipCardLanAdminLanId = _CipCardLanAdminLanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 2),
    _CipCardLanAdminLanId_Type()
)
cipCardLanAdminLanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipCardLanAdminLanId.setStatus("current")


class _CipCardLanAdminBridgeType_Type(Integer32):
    """Custom type cipCardLanAdminBridgeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sourcerouteOnly", 2),
          ("transpAndSourceRoute", 3),
          ("transparentOnly", 1))
    )


_CipCardLanAdminBridgeType_Type.__name__ = "Integer32"
_CipCardLanAdminBridgeType_Object = MibTableColumn
cipCardLanAdminBridgeType = _CipCardLanAdminBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 3),
    _CipCardLanAdminBridgeType_Type()
)
cipCardLanAdminBridgeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardLanAdminBridgeType.setStatus("current")


class _CipCardLanAdminSrbLocalRing_Type(Integer32):
    """Custom type cipCardLanAdminSrbLocalRing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CipCardLanAdminSrbLocalRing_Type.__name__ = "Integer32"
_CipCardLanAdminSrbLocalRing_Object = MibTableColumn
cipCardLanAdminSrbLocalRing = _CipCardLanAdminSrbLocalRing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 4),
    _CipCardLanAdminSrbLocalRing_Type()
)
cipCardLanAdminSrbLocalRing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardLanAdminSrbLocalRing.setStatus("current")


class _CipCardLanAdminSrbBridgeNum_Type(Integer32):
    """Custom type cipCardLanAdminSrbBridgeNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CipCardLanAdminSrbBridgeNum_Type.__name__ = "Integer32"
_CipCardLanAdminSrbBridgeNum_Object = MibTableColumn
cipCardLanAdminSrbBridgeNum = _CipCardLanAdminSrbBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 5),
    _CipCardLanAdminSrbBridgeNum_Type()
)
cipCardLanAdminSrbBridgeNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardLanAdminSrbBridgeNum.setStatus("current")


class _CipCardLanAdminSrbTargetRing_Type(Integer32):
    """Custom type cipCardLanAdminSrbTargetRing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CipCardLanAdminSrbTargetRing_Type.__name__ = "Integer32"
_CipCardLanAdminSrbTargetRing_Object = MibTableColumn
cipCardLanAdminSrbTargetRing = _CipCardLanAdminSrbTargetRing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 6),
    _CipCardLanAdminSrbTargetRing_Type()
)
cipCardLanAdminSrbTargetRing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardLanAdminSrbTargetRing.setStatus("current")


class _CipCardLanAdminTbBridgeGrp_Type(Integer32):
    """Custom type cipCardLanAdminTbBridgeGrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_CipCardLanAdminTbBridgeGrp_Type.__name__ = "Integer32"
_CipCardLanAdminTbBridgeGrp_Object = MibTableColumn
cipCardLanAdminTbBridgeGrp = _CipCardLanAdminTbBridgeGrp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 7),
    _CipCardLanAdminTbBridgeGrp_Type()
)
cipCardLanAdminTbBridgeGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardLanAdminTbBridgeGrp.setStatus("current")
_CipCardLanAdminRowStatus_Type = RowStatus
_CipCardLanAdminRowStatus_Object = MibTableColumn
cipCardLanAdminRowStatus = _CipCardLanAdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 8),
    _CipCardLanAdminRowStatus_Type()
)
cipCardLanAdminRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardLanAdminRowStatus.setStatus("current")
_CipCardLanAdaptAdminTable_Object = MibTable
cipCardLanAdaptAdminTable = _CipCardLanAdaptAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cipCardLanAdaptAdminTable.setStatus("current")
_CipCardLanAdaptAdminEntry_Object = MibTableRow
cipCardLanAdaptAdminEntry = _CipCardLanAdaptAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 2, 1)
)
cipCardLanAdaptAdminEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CIPLAN-MIB", "cipCardLanAdminLanType"),
    (0, "CISCO-CIPLAN-MIB", "cipCardLanAdminLanId"),
    (0, "CISCO-CIPLAN-MIB", "cipCardLanAdaptAdminAdaptNo"),
)
if mibBuilder.loadTexts:
    cipCardLanAdaptAdminEntry.setStatus("current")


class _CipCardLanAdaptAdminAdaptNo_Type(Integer32):
    """Custom type cipCardLanAdaptAdminAdaptNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_CipCardLanAdaptAdminAdaptNo_Type.__name__ = "Integer32"
_CipCardLanAdaptAdminAdaptNo_Object = MibTableColumn
cipCardLanAdaptAdminAdaptNo = _CipCardLanAdaptAdminAdaptNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 2, 1, 1),
    _CipCardLanAdaptAdminAdaptNo_Type()
)
cipCardLanAdaptAdminAdaptNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipCardLanAdaptAdminAdaptNo.setStatus("current")
_CipCardLanAdaptAdminMacAddress_Type = MacAddress
_CipCardLanAdaptAdminMacAddress_Object = MibTableColumn
cipCardLanAdaptAdminMacAddress = _CipCardLanAdaptAdminMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 2, 1, 2),
    _CipCardLanAdaptAdminMacAddress_Type()
)
cipCardLanAdaptAdminMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardLanAdaptAdminMacAddress.setStatus("current")


class _CipCardLanAdaptAdminAdaptName_Type(DisplayString):
    """Custom type cipCardLanAdaptAdminAdaptName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_CipCardLanAdaptAdminAdaptName_Type.__name__ = "DisplayString"
_CipCardLanAdaptAdminAdaptName_Object = MibTableColumn
cipCardLanAdaptAdminAdaptName = _CipCardLanAdaptAdminAdaptName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 2, 1, 3),
    _CipCardLanAdaptAdminAdaptName_Type()
)
cipCardLanAdaptAdminAdaptName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardLanAdaptAdminAdaptName.setStatus("current")
_CipCardLanAdaptAdminRowStatus_Type = RowStatus
_CipCardLanAdaptAdminRowStatus_Object = MibTableColumn
cipCardLanAdaptAdminRowStatus = _CipCardLanAdaptAdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 2, 1, 4),
    _CipCardLanAdaptAdminRowStatus_Type()
)
cipCardLanAdaptAdminRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardLanAdaptAdminRowStatus.setStatus("current")
_CiscoCipLanMibConformance_ObjectIdentity = ObjectIdentity
ciscoCipLanMibConformance = _CiscoCipLanMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 2)
)
_CiscoCipLanMibCompliances_ObjectIdentity = ObjectIdentity
ciscoCipLanMibCompliances = _CiscoCipLanMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 2, 1)
)
_CiscoCipLanMibGroups_ObjectIdentity = ObjectIdentity
ciscoCipLanMibGroups = _CiscoCipLanMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 2, 2)
)

# Managed Objects groups

ciscoLanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 2, 2, 1)
)
ciscoLanGroup.setObjects(
      *(("CISCO-CIPLAN-MIB", "cipCardLanAdminBridgeType"),
        ("CISCO-CIPLAN-MIB", "cipCardLanAdminSrbLocalRing"),
        ("CISCO-CIPLAN-MIB", "cipCardLanAdminSrbBridgeNum"),
        ("CISCO-CIPLAN-MIB", "cipCardLanAdminSrbTargetRing"),
        ("CISCO-CIPLAN-MIB", "cipCardLanAdminTbBridgeGrp"),
        ("CISCO-CIPLAN-MIB", "cipCardLanAdminRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLanGroup.setStatus("current")

ciscoLanAdaptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 2, 2, 2)
)
ciscoLanAdaptGroup.setObjects(
      *(("CISCO-CIPLAN-MIB", "cipCardLanAdaptAdminMacAddress"),
        ("CISCO-CIPLAN-MIB", "cipCardLanAdaptAdminAdaptName"),
        ("CISCO-CIPLAN-MIB", "cipCardLanAdaptAdminRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLanAdaptGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCipLanMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 34, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCipLanMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CIPLAN-MIB",
    **{"ciscoCipLanMIB": ciscoCipLanMIB,
       "cipLanObjects": cipLanObjects,
       "cipLan": cipLan,
       "cipCardLanAdminTable": cipCardLanAdminTable,
       "cipCardLanAdminEntry": cipCardLanAdminEntry,
       "cipCardLanAdminLanType": cipCardLanAdminLanType,
       "cipCardLanAdminLanId": cipCardLanAdminLanId,
       "cipCardLanAdminBridgeType": cipCardLanAdminBridgeType,
       "cipCardLanAdminSrbLocalRing": cipCardLanAdminSrbLocalRing,
       "cipCardLanAdminSrbBridgeNum": cipCardLanAdminSrbBridgeNum,
       "cipCardLanAdminSrbTargetRing": cipCardLanAdminSrbTargetRing,
       "cipCardLanAdminTbBridgeGrp": cipCardLanAdminTbBridgeGrp,
       "cipCardLanAdminRowStatus": cipCardLanAdminRowStatus,
       "cipCardLanAdaptAdminTable": cipCardLanAdaptAdminTable,
       "cipCardLanAdaptAdminEntry": cipCardLanAdaptAdminEntry,
       "cipCardLanAdaptAdminAdaptNo": cipCardLanAdaptAdminAdaptNo,
       "cipCardLanAdaptAdminMacAddress": cipCardLanAdaptAdminMacAddress,
       "cipCardLanAdaptAdminAdaptName": cipCardLanAdaptAdminAdaptName,
       "cipCardLanAdaptAdminRowStatus": cipCardLanAdaptAdminRowStatus,
       "ciscoCipLanMibConformance": ciscoCipLanMibConformance,
       "ciscoCipLanMibCompliances": ciscoCipLanMibCompliances,
       "ciscoCipLanMibCompliance": ciscoCipLanMibCompliance,
       "ciscoCipLanMibGroups": ciscoCipLanMibGroups,
       "ciscoLanGroup": ciscoLanGroup,
       "ciscoLanAdaptGroup": ciscoLanAdaptGroup}
)
