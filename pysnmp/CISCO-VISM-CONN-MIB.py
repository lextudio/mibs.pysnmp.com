# SNMP MIB module (CISCO-VISM-CONN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VISM-CONN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:49 2024
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

(vismChanCnfGrp,
 vismChanGrp) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "vismChanCnfGrp",
    "vismChanGrp")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoVismConnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 86)
)
ciscoVismConnMIB.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-09 00:00",
         "2004-02-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VismChanCnfGrpTable_Object = MibTable
vismChanCnfGrpTable = _VismChanCnfGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1)
)
if mibBuilder.loadTexts:
    vismChanCnfGrpTable.setStatus("current")
_VismChanCnfGrpEntry_Object = MibTableRow
vismChanCnfGrpEntry = _VismChanCnfGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1)
)
vismChanCnfGrpEntry.setIndexNames(
    (0, "CISCO-VISM-CONN-MIB", "vismCnfChanNum"),
)
if mibBuilder.loadTexts:
    vismChanCnfGrpEntry.setStatus("current")


class _VismCnfChanNum_Type(Integer32):
    """Custom type vismCnfChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(131, 510),
    )


_VismCnfChanNum_Type.__name__ = "Integer32"
_VismCnfChanNum_Object = MibTableColumn
vismCnfChanNum = _VismCnfChanNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 1),
    _VismCnfChanNum_Type()
)
vismCnfChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismCnfChanNum.setStatus("current")


class _VismChanRowStatus_Type(Integer32):
    """Custom type vismChanRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("del", 2),
          ("mod", 3),
          ("outOfService", 4))
    )


_VismChanRowStatus_Type.__name__ = "Integer32"
_VismChanRowStatus_Object = MibTableColumn
vismChanRowStatus = _VismChanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 2),
    _VismChanRowStatus_Type()
)
vismChanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanRowStatus.setStatus("current")


class _VismChanPortNum_Type(Integer32):
    """Custom type vismChanPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VismChanPortNum_Type.__name__ = "Integer32"
_VismChanPortNum_Object = MibTableColumn
vismChanPortNum = _VismChanPortNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 3),
    _VismChanPortNum_Type()
)
vismChanPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanPortNum.setStatus("current")


class _VismChanLocRmtLpbkState_Type(Integer32):
    """Custom type vismChanLocRmtLpbkState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VismChanLocRmtLpbkState_Type.__name__ = "Integer32"
_VismChanLocRmtLpbkState_Object = MibTableColumn
vismChanLocRmtLpbkState = _VismChanLocRmtLpbkState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 4),
    _VismChanLocRmtLpbkState_Type()
)
vismChanLocRmtLpbkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanLocRmtLpbkState.setStatus("current")


class _VismChanTestType_Type(Integer32):
    """Custom type vismChanTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notest", 3),
          ("testcon", 1),
          ("testdelay", 2))
    )


_VismChanTestType_Type.__name__ = "Integer32"
_VismChanTestType_Object = MibTableColumn
vismChanTestType = _VismChanTestType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 5),
    _VismChanTestType_Type()
)
vismChanTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanTestType.setStatus("current")


class _VismChanTestState_Type(Integer32):
    """Custom type vismChanTestState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("inprogress", 3),
          ("notinprogress", 4),
          ("passed", 1))
    )


_VismChanTestState_Type.__name__ = "Integer32"
_VismChanTestState_Object = MibTableColumn
vismChanTestState = _VismChanTestState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 6),
    _VismChanTestState_Type()
)
vismChanTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanTestState.setStatus("current")


class _VismChanRTDResult_Type(Integer32):
    """Custom type vismChanRTDResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VismChanRTDResult_Type.__name__ = "Integer32"
_VismChanRTDResult_Object = MibTableColumn
vismChanRTDResult = _VismChanRTDResult_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 7),
    _VismChanRTDResult_Type()
)
vismChanRTDResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanRTDResult.setStatus("current")
if mibBuilder.loadTexts:
    vismChanRTDResult.setUnits("microseconds")


class _VismChanPvcType_Type(Integer32):
    """Custom type vismChanPvcType based on Integer32"""
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
        *(("aal-1", 3),
          ("aal-2", 2),
          ("aal-5", 1))
    )


_VismChanPvcType_Type.__name__ = "Integer32"
_VismChanPvcType_Object = MibTableColumn
vismChanPvcType = _VismChanPvcType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 8),
    _VismChanPvcType_Type()
)
vismChanPvcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanPvcType.setStatus("current")


class _VismChanConnType_Type(Integer32):
    """Custom type vismChanConnType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("pvc", 1)
    )


_VismChanConnType_Type.__name__ = "Integer32"
_VismChanConnType_Object = MibTableColumn
vismChanConnType = _VismChanConnType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 9),
    _VismChanConnType_Type()
)
vismChanConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanConnType.setStatus("current")


class _VismLocalVpi_Type(Integer32):
    """Custom type vismLocalVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VismLocalVpi_Type.__name__ = "Integer32"
_VismLocalVpi_Object = MibTableColumn
vismLocalVpi = _VismLocalVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 10),
    _VismLocalVpi_Type()
)
vismLocalVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLocalVpi.setStatus("current")


class _VismLocalVci_Type(Integer32):
    """Custom type vismLocalVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VismLocalVci_Type.__name__ = "Integer32"
_VismLocalVci_Object = MibTableColumn
vismLocalVci = _VismLocalVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 11),
    _VismLocalVci_Type()
)
vismLocalVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLocalVci.setStatus("current")


class _VismLocalNSAP_Type(OctetString):
    """Custom type vismLocalNSAP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_VismLocalNSAP_Type.__name__ = "OctetString"
_VismLocalNSAP_Object = MibTableColumn
vismLocalNSAP = _VismLocalNSAP_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 12),
    _VismLocalNSAP_Type()
)
vismLocalNSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismLocalNSAP.setStatus("current")


class _VismRemoteVpi_Type(Integer32):
    """Custom type vismRemoteVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VismRemoteVpi_Type.__name__ = "Integer32"
_VismRemoteVpi_Object = MibTableColumn
vismRemoteVpi = _VismRemoteVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 13),
    _VismRemoteVpi_Type()
)
vismRemoteVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRemoteVpi.setStatus("current")


class _VismRemoteVci_Type(Integer32):
    """Custom type vismRemoteVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VismRemoteVci_Type.__name__ = "Integer32"
_VismRemoteVci_Object = MibTableColumn
vismRemoteVci = _VismRemoteVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 14),
    _VismRemoteVci_Type()
)
vismRemoteVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRemoteVci.setStatus("current")


class _VismRemoteNSAP_Type(OctetString):
    """Custom type vismRemoteNSAP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_VismRemoteNSAP_Type.__name__ = "OctetString"
_VismRemoteNSAP_Object = MibTableColumn
vismRemoteNSAP = _VismRemoteNSAP_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 15),
    _VismRemoteNSAP_Type()
)
vismRemoteNSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRemoteNSAP.setStatus("current")


class _VismMastership_Type(Integer32):
    """Custom type vismMastership based on Integer32"""
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
        *(("master", 1),
          ("slave", 2),
          ("unknown", 3))
    )


_VismMastership_Type.__name__ = "Integer32"
_VismMastership_Object = MibTableColumn
vismMastership = _VismMastership_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 16),
    _VismMastership_Type()
)
vismMastership.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismMastership.setStatus("current")


class _VismVpcFlag_Type(Integer32):
    """Custom type vismVpcFlag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("vcc", 2)
    )


_VismVpcFlag_Type.__name__ = "Integer32"
_VismVpcFlag_Object = MibTableColumn
vismVpcFlag = _VismVpcFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 17),
    _VismVpcFlag_Type()
)
vismVpcFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismVpcFlag.setStatus("current")


class _VismConnServiceType_Type(Integer32):
    """Custom type vismConnServiceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("vbr-nrt", 3),
          ("vbr-rt", 2),
          ("vbr2-nrt", 6),
          ("vbr2-rt", 5),
          ("vbr3-nrt", 7),
          ("vbr3-rt", 4))
    )


_VismConnServiceType_Type.__name__ = "Integer32"
_VismConnServiceType_Object = MibTableColumn
vismConnServiceType = _VismConnServiceType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 18),
    _VismConnServiceType_Type()
)
vismConnServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismConnServiceType.setStatus("current")


class _VismRoutingPriority_Type(Integer32):
    """Custom type vismRoutingPriority based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_VismRoutingPriority_Type.__name__ = "Integer32"
_VismRoutingPriority_Object = MibTableColumn
vismRoutingPriority = _VismRoutingPriority_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 19),
    _VismRoutingPriority_Type()
)
vismRoutingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRoutingPriority.setStatus("current")


class _VismMaxCost_Type(Integer32):
    """Custom type vismMaxCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VismMaxCost_Type.__name__ = "Integer32"
_VismMaxCost_Object = MibTableColumn
vismMaxCost = _VismMaxCost_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 20),
    _VismMaxCost_Type()
)
vismMaxCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismMaxCost.setStatus("current")


class _VismRestrictTrunkType_Type(Integer32):
    """Custom type vismRestrictTrunkType based on Integer32"""
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
        *(("noresriction", 1),
          ("sateliteTrunk", 3),
          ("terrestrialTrunk", 2))
    )


_VismRestrictTrunkType_Type.__name__ = "Integer32"
_VismRestrictTrunkType_Object = MibTableColumn
vismRestrictTrunkType = _VismRestrictTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 21),
    _VismRestrictTrunkType_Type()
)
vismRestrictTrunkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRestrictTrunkType.setStatus("current")


class _VismConnPCR_Type(Integer32):
    """Custom type vismConnPCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_VismConnPCR_Type.__name__ = "Integer32"
_VismConnPCR_Object = MibTableColumn
vismConnPCR = _VismConnPCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 22),
    _VismConnPCR_Type()
)
vismConnPCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismConnPCR.setStatus("current")
if mibBuilder.loadTexts:
    vismConnPCR.setUnits("cells-per-second")


class _VismConnPercentUtil_Type(Integer32):
    """Custom type vismConnPercentUtil based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VismConnPercentUtil_Type.__name__ = "Integer32"
_VismConnPercentUtil_Object = MibTableColumn
vismConnPercentUtil = _VismConnPercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 23),
    _VismConnPercentUtil_Type()
)
vismConnPercentUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismConnPercentUtil.setStatus("current")
if mibBuilder.loadTexts:
    vismConnPercentUtil.setUnits("percentage")


class _VismConnRemotePCR_Type(Integer32):
    """Custom type vismConnRemotePCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_VismConnRemotePCR_Type.__name__ = "Integer32"
_VismConnRemotePCR_Object = MibTableColumn
vismConnRemotePCR = _VismConnRemotePCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 24),
    _VismConnRemotePCR_Type()
)
vismConnRemotePCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismConnRemotePCR.setStatus("current")
if mibBuilder.loadTexts:
    vismConnRemotePCR.setUnits("cells-per-second")


class _VismConnRemotePercentUtil_Type(Integer32):
    """Custom type vismConnRemotePercentUtil based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VismConnRemotePercentUtil_Type.__name__ = "Integer32"
_VismConnRemotePercentUtil_Object = MibTableColumn
vismConnRemotePercentUtil = _VismConnRemotePercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 25),
    _VismConnRemotePercentUtil_Type()
)
vismConnRemotePercentUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismConnRemotePercentUtil.setStatus("current")
if mibBuilder.loadTexts:
    vismConnRemotePercentUtil.setUnits("percentage")


class _VismChanProtection_Type(Integer32):
    """Custom type vismChanProtection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protected", 1),
          ("unprotected", 2))
    )


_VismChanProtection_Type.__name__ = "Integer32"
_VismChanProtection_Object = MibTableColumn
vismChanProtection = _VismChanProtection_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 26),
    _VismChanProtection_Type()
)
vismChanProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanProtection.setStatus("current")


class _VismChanPreference_Type(Integer32):
    """Custom type vismChanPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_VismChanPreference_Type.__name__ = "Integer32"
_VismChanPreference_Object = MibTableColumn
vismChanPreference = _VismChanPreference_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 27),
    _VismChanPreference_Type()
)
vismChanPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanPreference.setStatus("current")


class _VismChanActivityState_Type(Integer32):
    """Custom type vismChanActivityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("failed", 3),
          ("standby", 2),
          ("unknown", 4))
    )


_VismChanActivityState_Type.__name__ = "Integer32"
_VismChanActivityState_Object = MibTableColumn
vismChanActivityState = _VismChanActivityState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 28),
    _VismChanActivityState_Type()
)
vismChanActivityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanActivityState.setStatus("current")


class _VismChanLockingState_Type(Integer32):
    """Custom type vismChanLockingState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 2),
          ("unlock", 1))
    )


_VismChanLockingState_Type.__name__ = "Integer32"
_VismChanLockingState_Object = MibTableColumn
vismChanLockingState = _VismChanLockingState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 29),
    _VismChanLockingState_Type()
)
vismChanLockingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanLockingState.setStatus("current")


class _VismChanScrIngress_Type(Integer32):
    """Custom type vismChanScrIngress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_VismChanScrIngress_Type.__name__ = "Integer32"
_VismChanScrIngress_Object = MibTableColumn
vismChanScrIngress = _VismChanScrIngress_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 30),
    _VismChanScrIngress_Type()
)
vismChanScrIngress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanScrIngress.setStatus("current")
if mibBuilder.loadTexts:
    vismChanScrIngress.setUnits("cells-per-second")


class _VismChanMbsIngress_Type(Integer32):
    """Custom type vismChanMbsIngress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VismChanMbsIngress_Type.__name__ = "Integer32"
_VismChanMbsIngress_Object = MibTableColumn
vismChanMbsIngress = _VismChanMbsIngress_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 31),
    _VismChanMbsIngress_Type()
)
vismChanMbsIngress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanMbsIngress.setStatus("current")
if mibBuilder.loadTexts:
    vismChanMbsIngress.setUnits("cells-per-second")


class _VismChanClrIngress_Type(Integer32):
    """Custom type vismChanClrIngress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VismChanClrIngress_Type.__name__ = "Integer32"
_VismChanClrIngress_Object = MibTableColumn
vismChanClrIngress = _VismChanClrIngress_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 32),
    _VismChanClrIngress_Type()
)
vismChanClrIngress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanClrIngress.setStatus("current")


class _VismChanCdvt_Type(Integer32):
    """Custom type vismChanCdvt based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_VismChanCdvt_Type.__name__ = "Integer32"
_VismChanCdvt_Object = MibTableColumn
vismChanCdvt = _VismChanCdvt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 33),
    _VismChanCdvt_Type()
)
vismChanCdvt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanCdvt.setStatus("current")


class _VismConnPCREgress_Type(Integer32):
    """Custom type vismConnPCREgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_VismConnPCREgress_Type.__name__ = "Integer32"
_VismConnPCREgress_Object = MibTableColumn
vismConnPCREgress = _VismConnPCREgress_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 34),
    _VismConnPCREgress_Type()
)
vismConnPCREgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismConnPCREgress.setStatus("current")
if mibBuilder.loadTexts:
    vismConnPCREgress.setUnits("cells-per-second")


class _VismChanScrEgress_Type(Integer32):
    """Custom type vismChanScrEgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_VismChanScrEgress_Type.__name__ = "Integer32"
_VismChanScrEgress_Object = MibTableColumn
vismChanScrEgress = _VismChanScrEgress_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 35),
    _VismChanScrEgress_Type()
)
vismChanScrEgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanScrEgress.setStatus("current")
if mibBuilder.loadTexts:
    vismChanScrEgress.setUnits("cells-per-second")


class _VismChanMbsEgress_Type(Integer32):
    """Custom type vismChanMbsEgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VismChanMbsEgress_Type.__name__ = "Integer32"
_VismChanMbsEgress_Object = MibTableColumn
vismChanMbsEgress = _VismChanMbsEgress_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 36),
    _VismChanMbsEgress_Type()
)
vismChanMbsEgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanMbsEgress.setStatus("current")
if mibBuilder.loadTexts:
    vismChanMbsEgress.setUnits("cells-per-second")


class _VismChanClrEgress_Type(Integer32):
    """Custom type vismChanClrEgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VismChanClrEgress_Type.__name__ = "Integer32"
_VismChanClrEgress_Object = MibTableColumn
vismChanClrEgress = _VismChanClrEgress_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 37),
    _VismChanClrEgress_Type()
)
vismChanClrEgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanClrEgress.setStatus("current")


class _VismChanApplication_Type(Integer32):
    """Custom type vismChanApplication based on Integer32"""
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
        *(("bearer", 2),
          ("control", 1),
          ("signaling", 3))
    )


_VismChanApplication_Type.__name__ = "Integer32"
_VismChanApplication_Object = MibTableColumn
vismChanApplication = _VismChanApplication_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 38),
    _VismChanApplication_Type()
)
vismChanApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanApplication.setStatus("current")


class _VismChanFallbackLcn_Type(Integer32):
    """Custom type vismChanFallbackLcn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(131, 510),
    )


_VismChanFallbackLcn_Type.__name__ = "Integer32"
_VismChanFallbackLcn_Object = MibTableColumn
vismChanFallbackLcn = _VismChanFallbackLcn_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 39),
    _VismChanFallbackLcn_Type()
)
vismChanFallbackLcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanFallbackLcn.setStatus("current")


class _VismChanReroute_Type(TruthValue):
    """Custom type vismChanReroute based on TruthValue"""


_VismChanReroute_Object = MibTableColumn
vismChanReroute = _VismChanReroute_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 40),
    _VismChanReroute_Type()
)
vismChanReroute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanReroute.setStatus("current")


class _VismFarEndAddressType_Type(Integer32):
    """Custom type vismFarEndAddressType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("e164", 3),
          ("gwid", 4),
          ("notapplicable", 1),
          ("nsap", 2),
          ("unspecified", 5))
    )


_VismFarEndAddressType_Type.__name__ = "Integer32"
_VismFarEndAddressType_Object = MibTableColumn
vismFarEndAddressType = _VismFarEndAddressType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 41),
    _VismFarEndAddressType_Type()
)
vismFarEndAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismFarEndAddressType.setStatus("current")


class _VismFarEndE164Address_Type(DisplayString):
    """Custom type vismFarEndE164Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_VismFarEndE164Address_Type.__name__ = "DisplayString"
_VismFarEndE164Address_Object = MibTableColumn
vismFarEndE164Address = _VismFarEndE164Address_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 42),
    _VismFarEndE164Address_Type()
)
vismFarEndE164Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismFarEndE164Address.setStatus("current")


class _VismFarEndGWIDAddress_Type(DisplayString):
    """Custom type vismFarEndGWIDAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_VismFarEndGWIDAddress_Type.__name__ = "DisplayString"
_VismFarEndGWIDAddress_Object = MibTableColumn
vismFarEndGWIDAddress = _VismFarEndGWIDAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 43),
    _VismFarEndGWIDAddress_Type()
)
vismFarEndGWIDAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismFarEndGWIDAddress.setStatus("current")


class _VismFarEndNSAPAddress_Type(OctetString):
    """Custom type vismFarEndNSAPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_VismFarEndNSAPAddress_Type.__name__ = "OctetString"
_VismFarEndNSAPAddress_Object = MibTableColumn
vismFarEndNSAPAddress = _VismFarEndNSAPAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 44),
    _VismFarEndNSAPAddress_Type()
)
vismFarEndNSAPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismFarEndNSAPAddress.setStatus("current")


class _VismVCCI_Type(Integer32):
    """Custom type vismVCCI based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VismVCCI_Type.__name__ = "Integer32"
_VismVCCI_Object = MibTableColumn
vismVCCI = _VismVCCI_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 45),
    _VismVCCI_Type()
)
vismVCCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismVCCI.setStatus("current")


class _VismConnAdminStatus_Type(Integer32):
    """Custom type vismConnAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VismConnAdminStatus_Type.__name__ = "Integer32"
_VismConnAdminStatus_Object = MibTableColumn
vismConnAdminStatus = _VismConnAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 46),
    _VismConnAdminStatus_Type()
)
vismConnAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismConnAdminStatus.setStatus("current")


class _VismChanPrefRouteId_Type(Unsigned32):
    """Custom type vismChanPrefRouteId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VismChanPrefRouteId_Type.__name__ = "Unsigned32"
_VismChanPrefRouteId_Object = MibTableColumn
vismChanPrefRouteId = _VismChanPrefRouteId_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 47),
    _VismChanPrefRouteId_Type()
)
vismChanPrefRouteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanPrefRouteId.setStatus("current")


class _VismChanDirectRoute_Type(TruthValue):
    """Custom type vismChanDirectRoute based on TruthValue"""


_VismChanDirectRoute_Object = MibTableColumn
vismChanDirectRoute = _VismChanDirectRoute_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 48),
    _VismChanDirectRoute_Type()
)
vismChanDirectRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanDirectRoute.setStatus("current")


class _VismChanAisSuppression_Type(TruthValue):
    """Custom type vismChanAisSuppression based on TruthValue"""


_VismChanAisSuppression_Object = MibTableColumn
vismChanAisSuppression = _VismChanAisSuppression_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 49),
    _VismChanAisSuppression_Type()
)
vismChanAisSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanAisSuppression.setStatus("current")


class _VismChanAisDelayTime_Type(Unsigned32):
    """Custom type vismChanAisDelayTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VismChanAisDelayTime_Type.__name__ = "Unsigned32"
_VismChanAisDelayTime_Object = MibTableColumn
vismChanAisDelayTime = _VismChanAisDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 50),
    _VismChanAisDelayTime_Type()
)
vismChanAisDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanAisDelayTime.setStatus("current")


class _VismChanUserMaxPCRBandwidth_Type(Unsigned32):
    """Custom type vismChanUserMaxPCRBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_VismChanUserMaxPCRBandwidth_Type.__name__ = "Unsigned32"
_VismChanUserMaxPCRBandwidth_Object = MibTableColumn
vismChanUserMaxPCRBandwidth = _VismChanUserMaxPCRBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 51),
    _VismChanUserMaxPCRBandwidth_Type()
)
vismChanUserMaxPCRBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanUserMaxPCRBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vismChanUserMaxPCRBandwidth.setUnits("cells-per-second")


class _VismChanUserMaxScrIngress_Type(Unsigned32):
    """Custom type vismChanUserMaxScrIngress based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_VismChanUserMaxScrIngress_Type.__name__ = "Unsigned32"
_VismChanUserMaxScrIngress_Object = MibTableColumn
vismChanUserMaxScrIngress = _VismChanUserMaxScrIngress_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 52),
    _VismChanUserMaxScrIngress_Type()
)
vismChanUserMaxScrIngress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanUserMaxScrIngress.setStatus("current")
if mibBuilder.loadTexts:
    vismChanUserMaxScrIngress.setUnits("cells-per-second")


class _VismChanUserMaxMbsIngress_Type(Unsigned32):
    """Custom type vismChanUserMaxMbsIngress based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VismChanUserMaxMbsIngress_Type.__name__ = "Unsigned32"
_VismChanUserMaxMbsIngress_Object = MibTableColumn
vismChanUserMaxMbsIngress = _VismChanUserMaxMbsIngress_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 53),
    _VismChanUserMaxMbsIngress_Type()
)
vismChanUserMaxMbsIngress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanUserMaxMbsIngress.setStatus("current")
if mibBuilder.loadTexts:
    vismChanUserMaxMbsIngress.setUnits("cells-per-second")


class _VismChanUserMinPCRBandwidth_Type(Unsigned32):
    """Custom type vismChanUserMinPCRBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_VismChanUserMinPCRBandwidth_Type.__name__ = "Unsigned32"
_VismChanUserMinPCRBandwidth_Object = MibTableColumn
vismChanUserMinPCRBandwidth = _VismChanUserMinPCRBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 54),
    _VismChanUserMinPCRBandwidth_Type()
)
vismChanUserMinPCRBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanUserMinPCRBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vismChanUserMinPCRBandwidth.setUnits("cells-per-second")


class _VismChanUserPcrNumber_Type(Integer32):
    """Custom type vismChanUserPcrNumber based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("userConfiguredMaxBandwidth", 1),
          ("userConfiguredMinBandwidth", 2))
    )


_VismChanUserPcrNumber_Type.__name__ = "Integer32"
_VismChanUserPcrNumber_Object = MibTableColumn
vismChanUserPcrNumber = _VismChanUserPcrNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 1, 1, 55),
    _VismChanUserPcrNumber_Type()
)
vismChanUserPcrNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismChanUserPcrNumber.setStatus("current")


class _VismChanNumNextAvailable_Type(Integer32):
    """Custom type vismChanNumNextAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 510),
    )


_VismChanNumNextAvailable_Type.__name__ = "Integer32"
_VismChanNumNextAvailable_Object = MibScalar
vismChanNumNextAvailable = _VismChanNumNextAvailable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 1, 2),
    _VismChanNumNextAvailable_Type()
)
vismChanNumNextAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanNumNextAvailable.setStatus("current")
_VismChanStateGrp_ObjectIdentity = ObjectIdentity
vismChanStateGrp = _VismChanStateGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 2)
)
_VismChanStateGrpTable_Object = MibTable
vismChanStateGrpTable = _VismChanStateGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vismChanStateGrpTable.setStatus("current")
_VismChanStateGrpEntry_Object = MibTableRow
vismChanStateGrpEntry = _VismChanStateGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 2, 1, 1)
)
vismChanStateGrpEntry.setIndexNames(
    (0, "CISCO-VISM-CONN-MIB", "vismStateChanNum"),
)
if mibBuilder.loadTexts:
    vismChanStateGrpEntry.setStatus("current")


class _VismStateChanNum_Type(Integer32):
    """Custom type vismStateChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(131, 510),
    )


_VismStateChanNum_Type.__name__ = "Integer32"
_VismStateChanNum_Object = MibTableColumn
vismStateChanNum = _VismStateChanNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 2, 1, 1, 1),
    _VismStateChanNum_Type()
)
vismStateChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismStateChanNum.setStatus("current")


class _VismChanState_Type(Integer32):
    """Custom type vismChanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 3),
          ("notConfigured", 1),
          ("okay", 2))
    )


_VismChanState_Type.__name__ = "Integer32"
_VismChanState_Object = MibTableColumn
vismChanState = _VismChanState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 2, 1, 1, 2),
    _VismChanState_Type()
)
vismChanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanState.setStatus("current")


class _VismChanXmtATMState_Type(Integer32):
    """Custom type vismChanXmtATMState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("other", 1),
          ("sendingAIS", 3),
          ("sendingFERF", 4))
    )


_VismChanXmtATMState_Type.__name__ = "Integer32"
_VismChanXmtATMState_Object = MibTableColumn
vismChanXmtATMState = _VismChanXmtATMState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 2, 1, 1, 3),
    _VismChanXmtATMState_Type()
)
vismChanXmtATMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanXmtATMState.setStatus("current")


class _VismChanRcvATMState_Type(Integer32):
    """Custom type vismChanRcvATMState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("oamFailure", 5),
          ("other", 1),
          ("receivingAIS", 3),
          ("receivingFERF", 4))
    )


_VismChanRcvATMState_Type.__name__ = "Integer32"
_VismChanRcvATMState_Object = MibTableColumn
vismChanRcvATMState = _VismChanRcvATMState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 2, 1, 1, 4),
    _VismChanRcvATMState_Type()
)
vismChanRcvATMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanRcvATMState.setStatus("current")


class _VismChanStatusBitMap_Type(Integer32):
    """Custom type vismChanStatusBitMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VismChanStatusBitMap_Type.__name__ = "Integer32"
_VismChanStatusBitMap_Object = MibTableColumn
vismChanStatusBitMap = _VismChanStatusBitMap_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 2, 1, 1, 5),
    _VismChanStatusBitMap_Type()
)
vismChanStatusBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismChanStatusBitMap.setStatus("current")
_CiscoVismConnMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVismConnMIBConformance = _CiscoVismConnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 86, 2)
)
_CiscoVismConnMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVismConnMIBGroups = _CiscoVismConnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 86, 2, 1)
)
_CiscoVismConnMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVismConnMIBCompliances = _CiscoVismConnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 86, 2, 2)
)

# Managed Objects groups

ciscoVismConnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 86, 2, 1, 1)
)
ciscoVismConnGroup.setObjects(
      *(("CISCO-VISM-CONN-MIB", "vismChanNumNextAvailable"),
        ("CISCO-VISM-CONN-MIB", "vismCnfChanNum"),
        ("CISCO-VISM-CONN-MIB", "vismChanRowStatus"),
        ("CISCO-VISM-CONN-MIB", "vismChanPortNum"),
        ("CISCO-VISM-CONN-MIB", "vismChanLocRmtLpbkState"),
        ("CISCO-VISM-CONN-MIB", "vismChanTestType"),
        ("CISCO-VISM-CONN-MIB", "vismChanTestState"),
        ("CISCO-VISM-CONN-MIB", "vismChanRTDResult"),
        ("CISCO-VISM-CONN-MIB", "vismChanPvcType"),
        ("CISCO-VISM-CONN-MIB", "vismChanConnType"),
        ("CISCO-VISM-CONN-MIB", "vismLocalVpi"),
        ("CISCO-VISM-CONN-MIB", "vismLocalVci"),
        ("CISCO-VISM-CONN-MIB", "vismLocalNSAP"),
        ("CISCO-VISM-CONN-MIB", "vismRemoteVpi"),
        ("CISCO-VISM-CONN-MIB", "vismRemoteVci"),
        ("CISCO-VISM-CONN-MIB", "vismRemoteNSAP"),
        ("CISCO-VISM-CONN-MIB", "vismMastership"),
        ("CISCO-VISM-CONN-MIB", "vismVpcFlag"),
        ("CISCO-VISM-CONN-MIB", "vismConnServiceType"),
        ("CISCO-VISM-CONN-MIB", "vismRoutingPriority"),
        ("CISCO-VISM-CONN-MIB", "vismMaxCost"),
        ("CISCO-VISM-CONN-MIB", "vismRestrictTrunkType"),
        ("CISCO-VISM-CONN-MIB", "vismConnPCR"),
        ("CISCO-VISM-CONN-MIB", "vismConnPercentUtil"),
        ("CISCO-VISM-CONN-MIB", "vismConnRemotePCR"),
        ("CISCO-VISM-CONN-MIB", "vismConnRemotePercentUtil"),
        ("CISCO-VISM-CONN-MIB", "vismChanProtection"),
        ("CISCO-VISM-CONN-MIB", "vismChanPreference"),
        ("CISCO-VISM-CONN-MIB", "vismChanActivityState"),
        ("CISCO-VISM-CONN-MIB", "vismChanLockingState"),
        ("CISCO-VISM-CONN-MIB", "vismChanScrIngress"),
        ("CISCO-VISM-CONN-MIB", "vismChanMbsIngress"),
        ("CISCO-VISM-CONN-MIB", "vismChanCdvt"),
        ("CISCO-VISM-CONN-MIB", "vismChanClrIngress"),
        ("CISCO-VISM-CONN-MIB", "vismConnPCREgress"),
        ("CISCO-VISM-CONN-MIB", "vismChanScrEgress"),
        ("CISCO-VISM-CONN-MIB", "vismChanMbsEgress"),
        ("CISCO-VISM-CONN-MIB", "vismChanClrEgress"),
        ("CISCO-VISM-CONN-MIB", "vismChanApplication"),
        ("CISCO-VISM-CONN-MIB", "vismChanFallbackLcn"),
        ("CISCO-VISM-CONN-MIB", "vismChanReroute"),
        ("CISCO-VISM-CONN-MIB", "vismFarEndAddressType"),
        ("CISCO-VISM-CONN-MIB", "vismFarEndE164Address"),
        ("CISCO-VISM-CONN-MIB", "vismFarEndGWIDAddress"),
        ("CISCO-VISM-CONN-MIB", "vismFarEndNSAPAddress"),
        ("CISCO-VISM-CONN-MIB", "vismVCCI"),
        ("CISCO-VISM-CONN-MIB", "vismConnAdminStatus"))
)
if mibBuilder.loadTexts:
    ciscoVismConnGroup.setStatus("deprecated")

ciscoVismConnStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 86, 2, 1, 2)
)
ciscoVismConnStateGroup.setObjects(
      *(("CISCO-VISM-CONN-MIB", "vismStateChanNum"),
        ("CISCO-VISM-CONN-MIB", "vismChanState"),
        ("CISCO-VISM-CONN-MIB", "vismChanXmtATMState"),
        ("CISCO-VISM-CONN-MIB", "vismChanRcvATMState"),
        ("CISCO-VISM-CONN-MIB", "vismChanStatusBitMap"))
)
if mibBuilder.loadTexts:
    ciscoVismConnStateGroup.setStatus("current")

ciscoVismConnGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 86, 2, 1, 3)
)
ciscoVismConnGroupRev1.setObjects(
      *(("CISCO-VISM-CONN-MIB", "vismChanNumNextAvailable"),
        ("CISCO-VISM-CONN-MIB", "vismCnfChanNum"),
        ("CISCO-VISM-CONN-MIB", "vismChanRowStatus"),
        ("CISCO-VISM-CONN-MIB", "vismChanPortNum"),
        ("CISCO-VISM-CONN-MIB", "vismChanLocRmtLpbkState"),
        ("CISCO-VISM-CONN-MIB", "vismChanTestType"),
        ("CISCO-VISM-CONN-MIB", "vismChanTestState"),
        ("CISCO-VISM-CONN-MIB", "vismChanRTDResult"),
        ("CISCO-VISM-CONN-MIB", "vismChanPvcType"),
        ("CISCO-VISM-CONN-MIB", "vismChanConnType"),
        ("CISCO-VISM-CONN-MIB", "vismLocalVpi"),
        ("CISCO-VISM-CONN-MIB", "vismLocalVci"),
        ("CISCO-VISM-CONN-MIB", "vismLocalNSAP"),
        ("CISCO-VISM-CONN-MIB", "vismRemoteVpi"),
        ("CISCO-VISM-CONN-MIB", "vismRemoteVci"),
        ("CISCO-VISM-CONN-MIB", "vismRemoteNSAP"),
        ("CISCO-VISM-CONN-MIB", "vismMastership"),
        ("CISCO-VISM-CONN-MIB", "vismVpcFlag"),
        ("CISCO-VISM-CONN-MIB", "vismConnServiceType"),
        ("CISCO-VISM-CONN-MIB", "vismRoutingPriority"),
        ("CISCO-VISM-CONN-MIB", "vismMaxCost"),
        ("CISCO-VISM-CONN-MIB", "vismRestrictTrunkType"),
        ("CISCO-VISM-CONN-MIB", "vismConnPCR"),
        ("CISCO-VISM-CONN-MIB", "vismConnPercentUtil"),
        ("CISCO-VISM-CONN-MIB", "vismConnRemotePCR"),
        ("CISCO-VISM-CONN-MIB", "vismConnRemotePercentUtil"),
        ("CISCO-VISM-CONN-MIB", "vismChanProtection"),
        ("CISCO-VISM-CONN-MIB", "vismChanPreference"),
        ("CISCO-VISM-CONN-MIB", "vismChanActivityState"),
        ("CISCO-VISM-CONN-MIB", "vismChanLockingState"),
        ("CISCO-VISM-CONN-MIB", "vismChanScrIngress"),
        ("CISCO-VISM-CONN-MIB", "vismChanMbsIngress"),
        ("CISCO-VISM-CONN-MIB", "vismChanCdvt"),
        ("CISCO-VISM-CONN-MIB", "vismChanClrIngress"),
        ("CISCO-VISM-CONN-MIB", "vismConnPCREgress"),
        ("CISCO-VISM-CONN-MIB", "vismChanScrEgress"),
        ("CISCO-VISM-CONN-MIB", "vismChanMbsEgress"),
        ("CISCO-VISM-CONN-MIB", "vismChanClrEgress"),
        ("CISCO-VISM-CONN-MIB", "vismChanApplication"),
        ("CISCO-VISM-CONN-MIB", "vismChanFallbackLcn"),
        ("CISCO-VISM-CONN-MIB", "vismChanReroute"),
        ("CISCO-VISM-CONN-MIB", "vismFarEndAddressType"),
        ("CISCO-VISM-CONN-MIB", "vismFarEndE164Address"),
        ("CISCO-VISM-CONN-MIB", "vismFarEndGWIDAddress"),
        ("CISCO-VISM-CONN-MIB", "vismFarEndNSAPAddress"),
        ("CISCO-VISM-CONN-MIB", "vismVCCI"),
        ("CISCO-VISM-CONN-MIB", "vismConnAdminStatus"),
        ("CISCO-VISM-CONN-MIB", "vismChanPrefRouteId"),
        ("CISCO-VISM-CONN-MIB", "vismChanDirectRoute"),
        ("CISCO-VISM-CONN-MIB", "vismChanAisSuppression"),
        ("CISCO-VISM-CONN-MIB", "vismChanAisDelayTime"),
        ("CISCO-VISM-CONN-MIB", "vismChanUserMaxPCRBandwidth"),
        ("CISCO-VISM-CONN-MIB", "vismChanUserMaxScrIngress"),
        ("CISCO-VISM-CONN-MIB", "vismChanUserMaxMbsIngress"),
        ("CISCO-VISM-CONN-MIB", "vismChanUserMinPCRBandwidth"),
        ("CISCO-VISM-CONN-MIB", "vismChanUserPcrNumber"))
)
if mibBuilder.loadTexts:
    ciscoVismConnGroupRev1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVismConnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 86, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoVismConnCompliance.setStatus(
        "deprecated"
    )

ciscoVismConnComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 86, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ciscoVismConnComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VISM-CONN-MIB",
    **{"vismChanCnfGrpTable": vismChanCnfGrpTable,
       "vismChanCnfGrpEntry": vismChanCnfGrpEntry,
       "vismCnfChanNum": vismCnfChanNum,
       "vismChanRowStatus": vismChanRowStatus,
       "vismChanPortNum": vismChanPortNum,
       "vismChanLocRmtLpbkState": vismChanLocRmtLpbkState,
       "vismChanTestType": vismChanTestType,
       "vismChanTestState": vismChanTestState,
       "vismChanRTDResult": vismChanRTDResult,
       "vismChanPvcType": vismChanPvcType,
       "vismChanConnType": vismChanConnType,
       "vismLocalVpi": vismLocalVpi,
       "vismLocalVci": vismLocalVci,
       "vismLocalNSAP": vismLocalNSAP,
       "vismRemoteVpi": vismRemoteVpi,
       "vismRemoteVci": vismRemoteVci,
       "vismRemoteNSAP": vismRemoteNSAP,
       "vismMastership": vismMastership,
       "vismVpcFlag": vismVpcFlag,
       "vismConnServiceType": vismConnServiceType,
       "vismRoutingPriority": vismRoutingPriority,
       "vismMaxCost": vismMaxCost,
       "vismRestrictTrunkType": vismRestrictTrunkType,
       "vismConnPCR": vismConnPCR,
       "vismConnPercentUtil": vismConnPercentUtil,
       "vismConnRemotePCR": vismConnRemotePCR,
       "vismConnRemotePercentUtil": vismConnRemotePercentUtil,
       "vismChanProtection": vismChanProtection,
       "vismChanPreference": vismChanPreference,
       "vismChanActivityState": vismChanActivityState,
       "vismChanLockingState": vismChanLockingState,
       "vismChanScrIngress": vismChanScrIngress,
       "vismChanMbsIngress": vismChanMbsIngress,
       "vismChanClrIngress": vismChanClrIngress,
       "vismChanCdvt": vismChanCdvt,
       "vismConnPCREgress": vismConnPCREgress,
       "vismChanScrEgress": vismChanScrEgress,
       "vismChanMbsEgress": vismChanMbsEgress,
       "vismChanClrEgress": vismChanClrEgress,
       "vismChanApplication": vismChanApplication,
       "vismChanFallbackLcn": vismChanFallbackLcn,
       "vismChanReroute": vismChanReroute,
       "vismFarEndAddressType": vismFarEndAddressType,
       "vismFarEndE164Address": vismFarEndE164Address,
       "vismFarEndGWIDAddress": vismFarEndGWIDAddress,
       "vismFarEndNSAPAddress": vismFarEndNSAPAddress,
       "vismVCCI": vismVCCI,
       "vismConnAdminStatus": vismConnAdminStatus,
       "vismChanPrefRouteId": vismChanPrefRouteId,
       "vismChanDirectRoute": vismChanDirectRoute,
       "vismChanAisSuppression": vismChanAisSuppression,
       "vismChanAisDelayTime": vismChanAisDelayTime,
       "vismChanUserMaxPCRBandwidth": vismChanUserMaxPCRBandwidth,
       "vismChanUserMaxScrIngress": vismChanUserMaxScrIngress,
       "vismChanUserMaxMbsIngress": vismChanUserMaxMbsIngress,
       "vismChanUserMinPCRBandwidth": vismChanUserMinPCRBandwidth,
       "vismChanUserPcrNumber": vismChanUserPcrNumber,
       "vismChanNumNextAvailable": vismChanNumNextAvailable,
       "vismChanStateGrp": vismChanStateGrp,
       "vismChanStateGrpTable": vismChanStateGrpTable,
       "vismChanStateGrpEntry": vismChanStateGrpEntry,
       "vismStateChanNum": vismStateChanNum,
       "vismChanState": vismChanState,
       "vismChanXmtATMState": vismChanXmtATMState,
       "vismChanRcvATMState": vismChanRcvATMState,
       "vismChanStatusBitMap": vismChanStatusBitMap,
       "ciscoVismConnMIB": ciscoVismConnMIB,
       "ciscoVismConnMIBConformance": ciscoVismConnMIBConformance,
       "ciscoVismConnMIBGroups": ciscoVismConnMIBGroups,
       "ciscoVismConnGroup": ciscoVismConnGroup,
       "ciscoVismConnStateGroup": ciscoVismConnStateGroup,
       "ciscoVismConnGroupRev1": ciscoVismConnGroupRev1,
       "ciscoVismConnMIBCompliances": ciscoVismConnMIBCompliances,
       "ciscoVismConnCompliance": ciscoVismConnCompliance,
       "ciscoVismConnComplianceRev1": ciscoVismConnComplianceRev1}
)
