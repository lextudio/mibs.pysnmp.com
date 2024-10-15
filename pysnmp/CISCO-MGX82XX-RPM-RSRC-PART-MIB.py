# SNMP MIB module (CISCO-MGX82XX-RPM-RSRC-PART-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MGX82XX-RPM-RSRC-PART-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:36 2024
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

(rpmInterface,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "rpmInterface")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoMgx82xxRpmRsrcPartMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 61)
)
ciscoMgx82xxRpmRsrcPartMIB.setRevisions(
        ("2002-09-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RpmIfCnfResPart_ObjectIdentity = ObjectIdentity
rpmIfCnfResPart = _RpmIfCnfResPart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 2)
)
_RpmIfCnfRscPartTable_Object = MibTable
rpmIfCnfRscPartTable = _RpmIfCnfRscPartTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 2, 1)
)
if mibBuilder.loadTexts:
    rpmIfCnfRscPartTable.setStatus("current")
_RpmIfCnfRscPartEntry_Object = MibTableRow
rpmIfCnfRscPartEntry = _RpmIfCnfRscPartEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 2, 1, 1)
)
rpmIfCnfRscPartEntry.setIndexNames(
    (0, "CISCO-MGX82XX-RPM-RSRC-PART-MIB", "rpmIfRscSlotNum"),
    (0, "CISCO-MGX82XX-RPM-RSRC-PART-MIB", "rpmIfRscPartIfNum"),
    (0, "CISCO-MGX82XX-RPM-RSRC-PART-MIB", "rpmIfRscPartCtrlrNum"),
)
if mibBuilder.loadTexts:
    rpmIfCnfRscPartEntry.setStatus("current")


class _RpmIfRscSlotNum_Type(Integer32):
    """Custom type rpmIfRscSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RpmIfRscSlotNum_Type.__name__ = "Integer32"
_RpmIfRscSlotNum_Object = MibTableColumn
rpmIfRscSlotNum = _RpmIfRscSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 2, 1, 1, 1),
    _RpmIfRscSlotNum_Type()
)
rpmIfRscSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmIfRscSlotNum.setStatus("current")


class _RpmIfRscPartIfNum_Type(Integer32):
    """Custom type rpmIfRscPartIfNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RpmIfRscPartIfNum_Type.__name__ = "Integer32"
_RpmIfRscPartIfNum_Object = MibTableColumn
rpmIfRscPartIfNum = _RpmIfRscPartIfNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 2, 1, 1, 2),
    _RpmIfRscPartIfNum_Type()
)
rpmIfRscPartIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmIfRscPartIfNum.setStatus("current")


class _RpmIfRscPartCtrlrNum_Type(Integer32):
    """Custom type rpmIfRscPartCtrlrNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("par", 1),
          ("pnni", 2),
          ("tag", 3))
    )


_RpmIfRscPartCtrlrNum_Type.__name__ = "Integer32"
_RpmIfRscPartCtrlrNum_Object = MibTableColumn
rpmIfRscPartCtrlrNum = _RpmIfRscPartCtrlrNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 2, 1, 1, 3),
    _RpmIfRscPartCtrlrNum_Type()
)
rpmIfRscPartCtrlrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmIfRscPartCtrlrNum.setStatus("current")


class _RpmIfRscPrtRowStatus_Type(Integer32):
    """Custom type rpmIfRscPrtRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("del", 2),
          ("mod", 3))
    )


_RpmIfRscPrtRowStatus_Type.__name__ = "Integer32"
_RpmIfRscPrtRowStatus_Object = MibTableColumn
rpmIfRscPrtRowStatus = _RpmIfRscPrtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 2, 1, 1, 4),
    _RpmIfRscPrtRowStatus_Type()
)
rpmIfRscPrtRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmIfRscPrtRowStatus.setStatus("current")


class _RpmIfRscPrtIngrPctBandwidth_Type(Integer32):
    """Custom type rpmIfRscPrtIngrPctBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RpmIfRscPrtIngrPctBandwidth_Type.__name__ = "Integer32"
_RpmIfRscPrtIngrPctBandwidth_Object = MibTableColumn
rpmIfRscPrtIngrPctBandwidth = _RpmIfRscPrtIngrPctBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 2, 1, 1, 5),
    _RpmIfRscPrtIngrPctBandwidth_Type()
)
rpmIfRscPrtIngrPctBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmIfRscPrtIngrPctBandwidth.setStatus("current")


class _RpmIfRscPrtEgrPctBandwidth_Type(Integer32):
    """Custom type rpmIfRscPrtEgrPctBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RpmIfRscPrtEgrPctBandwidth_Type.__name__ = "Integer32"
_RpmIfRscPrtEgrPctBandwidth_Object = MibTableColumn
rpmIfRscPrtEgrPctBandwidth = _RpmIfRscPrtEgrPctBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 2, 1, 1, 6),
    _RpmIfRscPrtEgrPctBandwidth_Type()
)
rpmIfRscPrtEgrPctBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmIfRscPrtEgrPctBandwidth.setStatus("current")


class _RpmIfRscPrtVpiLow_Type(Integer32):
    """Custom type rpmIfRscPrtVpiLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RpmIfRscPrtVpiLow_Type.__name__ = "Integer32"
_RpmIfRscPrtVpiLow_Object = MibTableColumn
rpmIfRscPrtVpiLow = _RpmIfRscPrtVpiLow_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 2, 1, 1, 7),
    _RpmIfRscPrtVpiLow_Type()
)
rpmIfRscPrtVpiLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmIfRscPrtVpiLow.setStatus("current")


class _RpmIfRscPrtVpiHigh_Type(Integer32):
    """Custom type rpmIfRscPrtVpiHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RpmIfRscPrtVpiHigh_Type.__name__ = "Integer32"
_RpmIfRscPrtVpiHigh_Object = MibTableColumn
rpmIfRscPrtVpiHigh = _RpmIfRscPrtVpiHigh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 2, 1, 1, 8),
    _RpmIfRscPrtVpiHigh_Type()
)
rpmIfRscPrtVpiHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmIfRscPrtVpiHigh.setStatus("current")


class _RpmIfRscPrtVciLow_Type(Integer32):
    """Custom type rpmIfRscPrtVciLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RpmIfRscPrtVciLow_Type.__name__ = "Integer32"
_RpmIfRscPrtVciLow_Object = MibTableColumn
rpmIfRscPrtVciLow = _RpmIfRscPrtVciLow_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 2, 1, 1, 9),
    _RpmIfRscPrtVciLow_Type()
)
rpmIfRscPrtVciLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmIfRscPrtVciLow.setStatus("current")


class _RpmIfRscPrtVciHigh_Type(Integer32):
    """Custom type rpmIfRscPrtVciHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RpmIfRscPrtVciHigh_Type.__name__ = "Integer32"
_RpmIfRscPrtVciHigh_Object = MibTableColumn
rpmIfRscPrtVciHigh = _RpmIfRscPrtVciHigh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 2, 1, 1, 10),
    _RpmIfRscPrtVciHigh_Type()
)
rpmIfRscPrtVciHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmIfRscPrtVciHigh.setStatus("current")


class _RpmIfRscPrtMaxChans_Type(Integer32):
    """Custom type rpmIfRscPrtMaxChans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4047),
    )


_RpmIfRscPrtMaxChans_Type.__name__ = "Integer32"
_RpmIfRscPrtMaxChans_Object = MibTableColumn
rpmIfRscPrtMaxChans = _RpmIfRscPrtMaxChans_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 2, 1, 1, 11),
    _RpmIfRscPrtMaxChans_Type()
)
rpmIfRscPrtMaxChans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmIfRscPrtMaxChans.setStatus("current")
_CmrRsrcPartMIBConformance_ObjectIdentity = ObjectIdentity
cmrRsrcPartMIBConformance = _CmrRsrcPartMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 61, 3)
)
_CmrRsrcPartMIBCompliances_ObjectIdentity = ObjectIdentity
cmrRsrcPartMIBCompliances = _CmrRsrcPartMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 61, 3, 1)
)
_CmrRsrcPartMIBGroups_ObjectIdentity = ObjectIdentity
cmrRsrcPartMIBGroups = _CmrRsrcPartMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 61, 3, 2)
)

# Managed Objects groups

cmrRsrcPartMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 61, 3, 2, 1)
)
cmrRsrcPartMIBGroup.setObjects(
      *(("CISCO-MGX82XX-RPM-RSRC-PART-MIB", "rpmIfRscSlotNum"),
        ("CISCO-MGX82XX-RPM-RSRC-PART-MIB", "rpmIfRscPartIfNum"),
        ("CISCO-MGX82XX-RPM-RSRC-PART-MIB", "rpmIfRscPartCtrlrNum"),
        ("CISCO-MGX82XX-RPM-RSRC-PART-MIB", "rpmIfRscPrtRowStatus"),
        ("CISCO-MGX82XX-RPM-RSRC-PART-MIB", "rpmIfRscPrtIngrPctBandwidth"),
        ("CISCO-MGX82XX-RPM-RSRC-PART-MIB", "rpmIfRscPrtEgrPctBandwidth"),
        ("CISCO-MGX82XX-RPM-RSRC-PART-MIB", "rpmIfRscPrtVpiLow"),
        ("CISCO-MGX82XX-RPM-RSRC-PART-MIB", "rpmIfRscPrtVpiHigh"),
        ("CISCO-MGX82XX-RPM-RSRC-PART-MIB", "rpmIfRscPrtVciLow"),
        ("CISCO-MGX82XX-RPM-RSRC-PART-MIB", "rpmIfRscPrtVciHigh"),
        ("CISCO-MGX82XX-RPM-RSRC-PART-MIB", "rpmIfRscPrtMaxChans"))
)
if mibBuilder.loadTexts:
    cmrRsrcPartMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmrRsrcPartMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 61, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cmrRsrcPartMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MGX82XX-RPM-RSRC-PART-MIB",
    **{"rpmIfCnfResPart": rpmIfCnfResPart,
       "rpmIfCnfRscPartTable": rpmIfCnfRscPartTable,
       "rpmIfCnfRscPartEntry": rpmIfCnfRscPartEntry,
       "rpmIfRscSlotNum": rpmIfRscSlotNum,
       "rpmIfRscPartIfNum": rpmIfRscPartIfNum,
       "rpmIfRscPartCtrlrNum": rpmIfRscPartCtrlrNum,
       "rpmIfRscPrtRowStatus": rpmIfRscPrtRowStatus,
       "rpmIfRscPrtIngrPctBandwidth": rpmIfRscPrtIngrPctBandwidth,
       "rpmIfRscPrtEgrPctBandwidth": rpmIfRscPrtEgrPctBandwidth,
       "rpmIfRscPrtVpiLow": rpmIfRscPrtVpiLow,
       "rpmIfRscPrtVpiHigh": rpmIfRscPrtVpiHigh,
       "rpmIfRscPrtVciLow": rpmIfRscPrtVciLow,
       "rpmIfRscPrtVciHigh": rpmIfRscPrtVciHigh,
       "rpmIfRscPrtMaxChans": rpmIfRscPrtMaxChans,
       "ciscoMgx82xxRpmRsrcPartMIB": ciscoMgx82xxRpmRsrcPartMIB,
       "cmrRsrcPartMIBConformance": cmrRsrcPartMIBConformance,
       "cmrRsrcPartMIBCompliances": cmrRsrcPartMIBCompliances,
       "cmrRsrcPartMIBCompliance": cmrRsrcPartMIBCompliance,
       "cmrRsrcPartMIBGroups": cmrRsrcPartMIBGroups,
       "cmrRsrcPartMIBGroup": cmrRsrcPartMIBGroup}
)
