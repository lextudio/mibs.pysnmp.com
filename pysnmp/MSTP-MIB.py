# SNMP MIB module (MSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MSTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:03 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

swMSTPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 15)
)


# Types definitions



class BridgeId(OctetString):
    """Custom type BridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwMSTPGblMgmt_ObjectIdentity = ObjectIdentity
swMSTPGblMgmt = _SwMSTPGblMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 1)
)


class _SwMSTPStpAdminState_Type(Integer32):
    """Custom type swMSTPStpAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwMSTPStpAdminState_Type.__name__ = "Integer32"
_SwMSTPStpAdminState_Object = MibScalar
swMSTPStpAdminState = _SwMSTPStpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 1, 1),
    _SwMSTPStpAdminState_Type()
)
swMSTPStpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPStpAdminState.setStatus("current")


class _SwMSTPStpVersion_Type(Integer32):
    """Custom type swMSTPStpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 2),
          ("rstp", 1),
          ("stp", 0))
    )


_SwMSTPStpVersion_Type.__name__ = "Integer32"
_SwMSTPStpVersion_Object = MibScalar
swMSTPStpVersion = _SwMSTPStpVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 1, 2),
    _SwMSTPStpVersion_Type()
)
swMSTPStpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPStpVersion.setStatus("current")


class _SwMSTPStpMaxAge_Type(Integer32):
    """Custom type swMSTPStpMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_SwMSTPStpMaxAge_Type.__name__ = "Integer32"
_SwMSTPStpMaxAge_Object = MibScalar
swMSTPStpMaxAge = _SwMSTPStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 1, 3),
    _SwMSTPStpMaxAge_Type()
)
swMSTPStpMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPStpMaxAge.setStatus("current")


class _SwMSTPStpHelloTime_Type(Integer32):
    """Custom type swMSTPStpHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_SwMSTPStpHelloTime_Type.__name__ = "Integer32"
_SwMSTPStpHelloTime_Object = MibScalar
swMSTPStpHelloTime = _SwMSTPStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 1, 4),
    _SwMSTPStpHelloTime_Type()
)
swMSTPStpHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPStpHelloTime.setStatus("current")


class _SwMSTPStpForwardDelay_Type(Integer32):
    """Custom type swMSTPStpForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_SwMSTPStpForwardDelay_Type.__name__ = "Integer32"
_SwMSTPStpForwardDelay_Object = MibScalar
swMSTPStpForwardDelay = _SwMSTPStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 1, 5),
    _SwMSTPStpForwardDelay_Type()
)
swMSTPStpForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPStpForwardDelay.setStatus("current")


class _SwMSTPStpMaxHops_Type(Integer32):
    """Custom type swMSTPStpMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SwMSTPStpMaxHops_Type.__name__ = "Integer32"
_SwMSTPStpMaxHops_Object = MibScalar
swMSTPStpMaxHops = _SwMSTPStpMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 1, 6),
    _SwMSTPStpMaxHops_Type()
)
swMSTPStpMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPStpMaxHops.setStatus("current")


class _SwMSTPStpTxHoldCount_Type(Integer32):
    """Custom type swMSTPStpTxHoldCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SwMSTPStpTxHoldCount_Type.__name__ = "Integer32"
_SwMSTPStpTxHoldCount_Object = MibScalar
swMSTPStpTxHoldCount = _SwMSTPStpTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 1, 7),
    _SwMSTPStpTxHoldCount_Type()
)
swMSTPStpTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPStpTxHoldCount.setStatus("current")


class _SwMSTPStpForwardBPDU_Type(Integer32):
    """Custom type swMSTPStpForwardBPDU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwMSTPStpForwardBPDU_Type.__name__ = "Integer32"
_SwMSTPStpForwardBPDU_Object = MibScalar
swMSTPStpForwardBPDU = _SwMSTPStpForwardBPDU_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 1, 8),
    _SwMSTPStpForwardBPDU_Type()
)
swMSTPStpForwardBPDU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPStpForwardBPDU.setStatus("current")


class _SwMSTPStpLBD_Type(Integer32):
    """Custom type swMSTPStpLBD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwMSTPStpLBD_Type.__name__ = "Integer32"
_SwMSTPStpLBD_Object = MibScalar
swMSTPStpLBD = _SwMSTPStpLBD_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 1, 9),
    _SwMSTPStpLBD_Type()
)
swMSTPStpLBD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPStpLBD.setStatus("current")


class _SwMSTPStpLBDRecoverTime_Type(Integer32):
    """Custom type swMSTPStpLBDRecoverTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_SwMSTPStpLBDRecoverTime_Type.__name__ = "Integer32"
_SwMSTPStpLBDRecoverTime_Object = MibScalar
swMSTPStpLBDRecoverTime = _SwMSTPStpLBDRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 1, 10),
    _SwMSTPStpLBDRecoverTime_Type()
)
swMSTPStpLBDRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPStpLBDRecoverTime.setStatus("current")
_SwMSTPCtrl_ObjectIdentity = ObjectIdentity
swMSTPCtrl = _SwMSTPCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2)
)


class _SwMSTPName_Type(OctetString):
    """Custom type swMSTPName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwMSTPName_Type.__name__ = "OctetString"
_SwMSTPName_Object = MibScalar
swMSTPName = _SwMSTPName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 1),
    _SwMSTPName_Type()
)
swMSTPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPName.setStatus("current")


class _SwMSTPRevisionLevel_Type(Integer32):
    """Custom type swMSTPRevisionLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwMSTPRevisionLevel_Type.__name__ = "Integer32"
_SwMSTPRevisionLevel_Object = MibScalar
swMSTPRevisionLevel = _SwMSTPRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 2),
    _SwMSTPRevisionLevel_Type()
)
swMSTPRevisionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPRevisionLevel.setStatus("current")
_SwMSTPInstanceCtrlTable_Object = MibTable
swMSTPInstanceCtrlTable = _SwMSTPInstanceCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3)
)
if mibBuilder.loadTexts:
    swMSTPInstanceCtrlTable.setStatus("current")
_SwMSTPInstanceCtrlEntry_Object = MibTableRow
swMSTPInstanceCtrlEntry = _SwMSTPInstanceCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1)
)
swMSTPInstanceCtrlEntry.setIndexNames(
    (0, "MSTP-MIB", "swMSTPInstId"),
)
if mibBuilder.loadTexts:
    swMSTPInstanceCtrlEntry.setStatus("current")


class _SwMSTPInstId_Type(Integer32):
    """Custom type swMSTPInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SwMSTPInstId_Type.__name__ = "Integer32"
_SwMSTPInstId_Object = MibTableColumn
swMSTPInstId = _SwMSTPInstId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 1),
    _SwMSTPInstId_Type()
)
swMSTPInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPInstId.setStatus("current")


class _SwMSTPInstVlanRangeList1to64_Type(OctetString):
    """Custom type swMSTPInstVlanRangeList1to64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwMSTPInstVlanRangeList1to64_Type.__name__ = "OctetString"
_SwMSTPInstVlanRangeList1to64_Object = MibTableColumn
swMSTPInstVlanRangeList1to64 = _SwMSTPInstVlanRangeList1to64_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 2),
    _SwMSTPInstVlanRangeList1to64_Type()
)
swMSTPInstVlanRangeList1to64.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMSTPInstVlanRangeList1to64.setStatus("current")


class _SwMSTPInstVlanRangeList65to128_Type(OctetString):
    """Custom type swMSTPInstVlanRangeList65to128 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwMSTPInstVlanRangeList65to128_Type.__name__ = "OctetString"
_SwMSTPInstVlanRangeList65to128_Object = MibTableColumn
swMSTPInstVlanRangeList65to128 = _SwMSTPInstVlanRangeList65to128_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 3),
    _SwMSTPInstVlanRangeList65to128_Type()
)
swMSTPInstVlanRangeList65to128.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMSTPInstVlanRangeList65to128.setStatus("current")


class _SwMSTPInstVlanRangeList129to192_Type(OctetString):
    """Custom type swMSTPInstVlanRangeList129to192 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwMSTPInstVlanRangeList129to192_Type.__name__ = "OctetString"
_SwMSTPInstVlanRangeList129to192_Object = MibTableColumn
swMSTPInstVlanRangeList129to192 = _SwMSTPInstVlanRangeList129to192_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 4),
    _SwMSTPInstVlanRangeList129to192_Type()
)
swMSTPInstVlanRangeList129to192.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMSTPInstVlanRangeList129to192.setStatus("current")


class _SwMSTPInstVlanRangeList193to256_Type(OctetString):
    """Custom type swMSTPInstVlanRangeList193to256 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwMSTPInstVlanRangeList193to256_Type.__name__ = "OctetString"
_SwMSTPInstVlanRangeList193to256_Object = MibTableColumn
swMSTPInstVlanRangeList193to256 = _SwMSTPInstVlanRangeList193to256_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 5),
    _SwMSTPInstVlanRangeList193to256_Type()
)
swMSTPInstVlanRangeList193to256.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMSTPInstVlanRangeList193to256.setStatus("current")


class _SwMSTPInstVlanRangeList257to320_Type(OctetString):
    """Custom type swMSTPInstVlanRangeList257to320 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwMSTPInstVlanRangeList257to320_Type.__name__ = "OctetString"
_SwMSTPInstVlanRangeList257to320_Object = MibTableColumn
swMSTPInstVlanRangeList257to320 = _SwMSTPInstVlanRangeList257to320_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 6),
    _SwMSTPInstVlanRangeList257to320_Type()
)
swMSTPInstVlanRangeList257to320.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMSTPInstVlanRangeList257to320.setStatus("current")


class _SwMSTPInstVlanRangeList321to384_Type(OctetString):
    """Custom type swMSTPInstVlanRangeList321to384 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwMSTPInstVlanRangeList321to384_Type.__name__ = "OctetString"
_SwMSTPInstVlanRangeList321to384_Object = MibTableColumn
swMSTPInstVlanRangeList321to384 = _SwMSTPInstVlanRangeList321to384_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 7),
    _SwMSTPInstVlanRangeList321to384_Type()
)
swMSTPInstVlanRangeList321to384.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMSTPInstVlanRangeList321to384.setStatus("current")


class _SwMSTPInstVlanRangeList385to448_Type(OctetString):
    """Custom type swMSTPInstVlanRangeList385to448 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwMSTPInstVlanRangeList385to448_Type.__name__ = "OctetString"
_SwMSTPInstVlanRangeList385to448_Object = MibTableColumn
swMSTPInstVlanRangeList385to448 = _SwMSTPInstVlanRangeList385to448_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 8),
    _SwMSTPInstVlanRangeList385to448_Type()
)
swMSTPInstVlanRangeList385to448.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMSTPInstVlanRangeList385to448.setStatus("current")


class _SwMSTPInstVlanRangeList449to512_Type(OctetString):
    """Custom type swMSTPInstVlanRangeList449to512 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwMSTPInstVlanRangeList449to512_Type.__name__ = "OctetString"
_SwMSTPInstVlanRangeList449to512_Object = MibTableColumn
swMSTPInstVlanRangeList449to512 = _SwMSTPInstVlanRangeList449to512_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 9),
    _SwMSTPInstVlanRangeList449to512_Type()
)
swMSTPInstVlanRangeList449to512.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMSTPInstVlanRangeList449to512.setStatus("current")


class _SwMSTPInstType_Type(Integer32):
    """Custom type swMSTPInstType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cist", 0),
          ("msti", 1))
    )


_SwMSTPInstType_Type.__name__ = "Integer32"
_SwMSTPInstType_Object = MibTableColumn
swMSTPInstType = _SwMSTPInstType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 10),
    _SwMSTPInstType_Type()
)
swMSTPInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPInstType.setStatus("current")


class _SwMSTPInstStatus_Type(Integer32):
    """Custom type swMSTPInstStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwMSTPInstStatus_Type.__name__ = "Integer32"
_SwMSTPInstStatus_Object = MibTableColumn
swMSTPInstStatus = _SwMSTPInstStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 11),
    _SwMSTPInstStatus_Type()
)
swMSTPInstStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPInstStatus.setStatus("current")


class _SwMSTPInstPriority_Type(Integer32):
    """Custom type swMSTPInstPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_SwMSTPInstPriority_Type.__name__ = "Integer32"
_SwMSTPInstPriority_Object = MibTableColumn
swMSTPInstPriority = _SwMSTPInstPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 12),
    _SwMSTPInstPriority_Type()
)
swMSTPInstPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMSTPInstPriority.setStatus("current")
_SwMSTPInstDesignatedRootBridge_Type = BridgeId
_SwMSTPInstDesignatedRootBridge_Object = MibTableColumn
swMSTPInstDesignatedRootBridge = _SwMSTPInstDesignatedRootBridge_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 13),
    _SwMSTPInstDesignatedRootBridge_Type()
)
swMSTPInstDesignatedRootBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPInstDesignatedRootBridge.setStatus("current")
_SwMSTPInstExternalRootCost_Type = Integer32
_SwMSTPInstExternalRootCost_Object = MibTableColumn
swMSTPInstExternalRootCost = _SwMSTPInstExternalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 14),
    _SwMSTPInstExternalRootCost_Type()
)
swMSTPInstExternalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPInstExternalRootCost.setStatus("current")
_SwMSTPInstRegionalRootBridge_Type = BridgeId
_SwMSTPInstRegionalRootBridge_Object = MibTableColumn
swMSTPInstRegionalRootBridge = _SwMSTPInstRegionalRootBridge_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 15),
    _SwMSTPInstRegionalRootBridge_Type()
)
swMSTPInstRegionalRootBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPInstRegionalRootBridge.setStatus("current")
_SwMSTPInstInternalRootCost_Type = Integer32
_SwMSTPInstInternalRootCost_Object = MibTableColumn
swMSTPInstInternalRootCost = _SwMSTPInstInternalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 16),
    _SwMSTPInstInternalRootCost_Type()
)
swMSTPInstInternalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPInstInternalRootCost.setStatus("current")
_SwMSTPInstDesignatedBridge_Type = BridgeId
_SwMSTPInstDesignatedBridge_Object = MibTableColumn
swMSTPInstDesignatedBridge = _SwMSTPInstDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 17),
    _SwMSTPInstDesignatedBridge_Type()
)
swMSTPInstDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPInstDesignatedBridge.setStatus("current")
_SwMSTPInstRootPort_Type = Integer32
_SwMSTPInstRootPort_Object = MibTableColumn
swMSTPInstRootPort = _SwMSTPInstRootPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 18),
    _SwMSTPInstRootPort_Type()
)
swMSTPInstRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPInstRootPort.setStatus("current")
_SwMSTPInstMaxAge_Type = Integer32
_SwMSTPInstMaxAge_Object = MibTableColumn
swMSTPInstMaxAge = _SwMSTPInstMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 19),
    _SwMSTPInstMaxAge_Type()
)
swMSTPInstMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPInstMaxAge.setStatus("current")
_SwMSTPInstForwardDelay_Type = Integer32
_SwMSTPInstForwardDelay_Object = MibTableColumn
swMSTPInstForwardDelay = _SwMSTPInstForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 20),
    _SwMSTPInstForwardDelay_Type()
)
swMSTPInstForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPInstForwardDelay.setStatus("current")
_SwMSTPInstLastTopologyChange_Type = TimeTicks
_SwMSTPInstLastTopologyChange_Object = MibTableColumn
swMSTPInstLastTopologyChange = _SwMSTPInstLastTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 21),
    _SwMSTPInstLastTopologyChange_Type()
)
swMSTPInstLastTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPInstLastTopologyChange.setStatus("current")
_SwMSTPInstTopChangesCount_Type = Counter32
_SwMSTPInstTopChangesCount_Object = MibTableColumn
swMSTPInstTopChangesCount = _SwMSTPInstTopChangesCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 22),
    _SwMSTPInstTopChangesCount_Type()
)
swMSTPInstTopChangesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPInstTopChangesCount.setStatus("current")
_SwMSTPInstRemainHops_Type = Integer32
_SwMSTPInstRemainHops_Object = MibTableColumn
swMSTPInstRemainHops = _SwMSTPInstRemainHops_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 23),
    _SwMSTPInstRemainHops_Type()
)
swMSTPInstRemainHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPInstRemainHops.setStatus("current")
_SwMSTPInstRowStatus_Type = RowStatus
_SwMSTPInstRowStatus_Object = MibTableColumn
swMSTPInstRowStatus = _SwMSTPInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 3, 1, 24),
    _SwMSTPInstRowStatus_Type()
)
swMSTPInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMSTPInstRowStatus.setStatus("current")
_SwMSTPPortTable_Object = MibTable
swMSTPPortTable = _SwMSTPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4)
)
if mibBuilder.loadTexts:
    swMSTPPortTable.setStatus("current")
_SwMSTPPortEntry_Object = MibTableRow
swMSTPPortEntry = _SwMSTPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1)
)
swMSTPPortEntry.setIndexNames(
    (0, "MSTP-MIB", "swMSTPPort"),
)
if mibBuilder.loadTexts:
    swMSTPPortEntry.setStatus("current")


class _SwMSTPPort_Type(Integer32):
    """Custom type swMSTPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMSTPPort_Type.__name__ = "Integer32"
_SwMSTPPort_Object = MibTableColumn
swMSTPPort = _SwMSTPPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 1),
    _SwMSTPPort_Type()
)
swMSTPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPPort.setStatus("current")


class _SwMSTPPortOperHelloTime_Type(Integer32):
    """Custom type swMSTPPortOperHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_SwMSTPPortOperHelloTime_Type.__name__ = "Integer32"
_SwMSTPPortOperHelloTime_Object = MibTableColumn
swMSTPPortOperHelloTime = _SwMSTPPortOperHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 2),
    _SwMSTPPortOperHelloTime_Type()
)
swMSTPPortOperHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPPortOperHelloTime.setStatus("current")


class _SwMSTPPortAdminHelloTime_Type(Integer32):
    """Custom type swMSTPPortAdminHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_SwMSTPPortAdminHelloTime_Type.__name__ = "Integer32"
_SwMSTPPortAdminHelloTime_Object = MibTableColumn
swMSTPPortAdminHelloTime = _SwMSTPPortAdminHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 3),
    _SwMSTPPortAdminHelloTime_Type()
)
swMSTPPortAdminHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPPortAdminHelloTime.setStatus("current")


class _SwMSTPSTPPortEnable_Type(Integer32):
    """Custom type swMSTPSTPPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwMSTPSTPPortEnable_Type.__name__ = "Integer32"
_SwMSTPSTPPortEnable_Object = MibTableColumn
swMSTPSTPPortEnable = _SwMSTPSTPPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 4),
    _SwMSTPSTPPortEnable_Type()
)
swMSTPSTPPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPSTPPortEnable.setStatus("current")


class _SwMSTPPortExternalPathCost_Type(Integer32):
    """Custom type swMSTPPortExternalPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_SwMSTPPortExternalPathCost_Type.__name__ = "Integer32"
_SwMSTPPortExternalPathCost_Object = MibTableColumn
swMSTPPortExternalPathCost = _SwMSTPPortExternalPathCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 5),
    _SwMSTPPortExternalPathCost_Type()
)
swMSTPPortExternalPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPPortExternalPathCost.setStatus("current")
_SwMSTPPortMigration_Type = TruthValue
_SwMSTPPortMigration_Object = MibTableColumn
swMSTPPortMigration = _SwMSTPPortMigration_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 6),
    _SwMSTPPortMigration_Type()
)
swMSTPPortMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPPortMigration.setStatus("current")


class _SwMSTPPortAdminEdgePort_Type(Integer32):
    """Custom type swMSTPPortAdminEdgePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("false", 2),
          ("true", 1))
    )


_SwMSTPPortAdminEdgePort_Type.__name__ = "Integer32"
_SwMSTPPortAdminEdgePort_Object = MibTableColumn
swMSTPPortAdminEdgePort = _SwMSTPPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 7),
    _SwMSTPPortAdminEdgePort_Type()
)
swMSTPPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPPortAdminEdgePort.setStatus("current")


class _SwMSTPPortOperEdgePort_Type(Integer32):
    """Custom type swMSTPPortOperEdgePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("false", 2),
          ("true", 1))
    )


_SwMSTPPortOperEdgePort_Type.__name__ = "Integer32"
_SwMSTPPortOperEdgePort_Object = MibTableColumn
swMSTPPortOperEdgePort = _SwMSTPPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 8),
    _SwMSTPPortOperEdgePort_Type()
)
swMSTPPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPPortOperEdgePort.setStatus("current")


class _SwMSTPPortAdminP2P_Type(Integer32):
    """Custom type swMSTPPortAdminP2P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("false", 1),
          ("true", 0))
    )


_SwMSTPPortAdminP2P_Type.__name__ = "Integer32"
_SwMSTPPortAdminP2P_Object = MibTableColumn
swMSTPPortAdminP2P = _SwMSTPPortAdminP2P_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 9),
    _SwMSTPPortAdminP2P_Type()
)
swMSTPPortAdminP2P.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPPortAdminP2P.setStatus("current")


class _SwMSTPPortOperP2P_Type(Integer32):
    """Custom type swMSTPPortOperP2P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("false", 1),
          ("true", 0))
    )


_SwMSTPPortOperP2P_Type.__name__ = "Integer32"
_SwMSTPPortOperP2P_Object = MibTableColumn
swMSTPPortOperP2P = _SwMSTPPortOperP2P_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 10),
    _SwMSTPPortOperP2P_Type()
)
swMSTPPortOperP2P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPPortOperP2P.setStatus("current")


class _SwMSTPPortLBD_Type(Integer32):
    """Custom type swMSTPPortLBD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwMSTPPortLBD_Type.__name__ = "Integer32"
_SwMSTPPortLBD_Object = MibTableColumn
swMSTPPortLBD = _SwMSTPPortLBD_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 11),
    _SwMSTPPortLBD_Type()
)
swMSTPPortLBD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPPortLBD.setStatus("current")


class _SwMSTPPortBPDUFiltering_Type(Integer32):
    """Custom type swMSTPPortBPDUFiltering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwMSTPPortBPDUFiltering_Type.__name__ = "Integer32"
_SwMSTPPortBPDUFiltering_Object = MibTableColumn
swMSTPPortBPDUFiltering = _SwMSTPPortBPDUFiltering_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 12),
    _SwMSTPPortBPDUFiltering_Type()
)
swMSTPPortBPDUFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPPortBPDUFiltering.setStatus("current")
_SwMSTPPortRestrictedRole_Type = TruthValue
_SwMSTPPortRestrictedRole_Object = MibTableColumn
swMSTPPortRestrictedRole = _SwMSTPPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 13),
    _SwMSTPPortRestrictedRole_Type()
)
swMSTPPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPPortRestrictedRole.setStatus("current")
_SwMSTPPortRestrictedTCN_Type = TruthValue
_SwMSTPPortRestrictedTCN_Object = MibTableColumn
swMSTPPortRestrictedTCN = _SwMSTPPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 4, 1, 14),
    _SwMSTPPortRestrictedTCN_Type()
)
swMSTPPortRestrictedTCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPPortRestrictedTCN.setStatus("current")
_SwMSTPMstPortTable_Object = MibTable
swMSTPMstPortTable = _SwMSTPMstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 5)
)
if mibBuilder.loadTexts:
    swMSTPMstPortTable.setStatus("current")
_SwMSTPMstPortEntry_Object = MibTableRow
swMSTPMstPortEntry = _SwMSTPMstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 5, 1)
)
swMSTPMstPortEntry.setIndexNames(
    (0, "MSTP-MIB", "swMSTPMstPort"),
    (0, "MSTP-MIB", "swMSTPMstPortInsID"),
)
if mibBuilder.loadTexts:
    swMSTPMstPortEntry.setStatus("current")


class _SwMSTPMstPort_Type(Integer32):
    """Custom type swMSTPMstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMSTPMstPort_Type.__name__ = "Integer32"
_SwMSTPMstPort_Object = MibTableColumn
swMSTPMstPort = _SwMSTPMstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 5, 1, 1),
    _SwMSTPMstPort_Type()
)
swMSTPMstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPMstPort.setStatus("current")


class _SwMSTPMstPortInsID_Type(Integer32):
    """Custom type swMSTPMstPortInsID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SwMSTPMstPortInsID_Type.__name__ = "Integer32"
_SwMSTPMstPortInsID_Object = MibTableColumn
swMSTPMstPortInsID = _SwMSTPMstPortInsID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 5, 1, 2),
    _SwMSTPMstPortInsID_Type()
)
swMSTPMstPortInsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPMstPortInsID.setStatus("current")
_SwMSTPMstPortDesignatedBridge_Type = BridgeId
_SwMSTPMstPortDesignatedBridge_Object = MibTableColumn
swMSTPMstPortDesignatedBridge = _SwMSTPMstPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 5, 1, 3),
    _SwMSTPMstPortDesignatedBridge_Type()
)
swMSTPMstPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPMstPortDesignatedBridge.setStatus("current")


class _SwMSTPMstPortInternalPathCost_Type(Integer32):
    """Custom type swMSTPMstPortInternalPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_SwMSTPMstPortInternalPathCost_Type.__name__ = "Integer32"
_SwMSTPMstPortInternalPathCost_Object = MibTableColumn
swMSTPMstPortInternalPathCost = _SwMSTPMstPortInternalPathCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 5, 1, 4),
    _SwMSTPMstPortInternalPathCost_Type()
)
swMSTPMstPortInternalPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPMstPortInternalPathCost.setStatus("current")


class _SwMSTPMstPortPriority_Type(Integer32):
    """Custom type swMSTPMstPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_SwMSTPMstPortPriority_Type.__name__ = "Integer32"
_SwMSTPMstPortPriority_Object = MibTableColumn
swMSTPMstPortPriority = _SwMSTPMstPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 5, 1, 5),
    _SwMSTPMstPortPriority_Type()
)
swMSTPMstPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMSTPMstPortPriority.setStatus("current")


class _SwMSTPMstPortStatus_Type(Integer32):
    """Custom type swMSTPMstPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("broken", 6),
          ("disabled", 2),
          ("discarding", 3),
          ("err-disabled", 8),
          ("forwarding", 5),
          ("learning", 4),
          ("no-stp-enabled", 7),
          ("other", 1))
    )


_SwMSTPMstPortStatus_Type.__name__ = "Integer32"
_SwMSTPMstPortStatus_Object = MibTableColumn
swMSTPMstPortStatus = _SwMSTPMstPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 5, 1, 6),
    _SwMSTPMstPortStatus_Type()
)
swMSTPMstPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPMstPortStatus.setStatus("current")


class _SwMSTPMstPortRole_Type(Integer32):
    """Custom type swMSTPMstPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 1),
          ("backup", 2),
          ("designated", 4),
          ("disable", 0),
          ("loopback", 7),
          ("master", 5),
          ("nonstp", 6),
          ("root", 3))
    )


_SwMSTPMstPortRole_Type.__name__ = "Integer32"
_SwMSTPMstPortRole_Object = MibTableColumn
swMSTPMstPortRole = _SwMSTPMstPortRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 15, 2, 5, 1, 7),
    _SwMSTPMstPortRole_Type()
)
swMSTPMstPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMSTPMstPortRole.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MSTP-MIB",
    **{"BridgeId": BridgeId,
       "swMSTPMIB": swMSTPMIB,
       "swMSTPGblMgmt": swMSTPGblMgmt,
       "swMSTPStpAdminState": swMSTPStpAdminState,
       "swMSTPStpVersion": swMSTPStpVersion,
       "swMSTPStpMaxAge": swMSTPStpMaxAge,
       "swMSTPStpHelloTime": swMSTPStpHelloTime,
       "swMSTPStpForwardDelay": swMSTPStpForwardDelay,
       "swMSTPStpMaxHops": swMSTPStpMaxHops,
       "swMSTPStpTxHoldCount": swMSTPStpTxHoldCount,
       "swMSTPStpForwardBPDU": swMSTPStpForwardBPDU,
       "swMSTPStpLBD": swMSTPStpLBD,
       "swMSTPStpLBDRecoverTime": swMSTPStpLBDRecoverTime,
       "swMSTPCtrl": swMSTPCtrl,
       "swMSTPName": swMSTPName,
       "swMSTPRevisionLevel": swMSTPRevisionLevel,
       "swMSTPInstanceCtrlTable": swMSTPInstanceCtrlTable,
       "swMSTPInstanceCtrlEntry": swMSTPInstanceCtrlEntry,
       "swMSTPInstId": swMSTPInstId,
       "swMSTPInstVlanRangeList1to64": swMSTPInstVlanRangeList1to64,
       "swMSTPInstVlanRangeList65to128": swMSTPInstVlanRangeList65to128,
       "swMSTPInstVlanRangeList129to192": swMSTPInstVlanRangeList129to192,
       "swMSTPInstVlanRangeList193to256": swMSTPInstVlanRangeList193to256,
       "swMSTPInstVlanRangeList257to320": swMSTPInstVlanRangeList257to320,
       "swMSTPInstVlanRangeList321to384": swMSTPInstVlanRangeList321to384,
       "swMSTPInstVlanRangeList385to448": swMSTPInstVlanRangeList385to448,
       "swMSTPInstVlanRangeList449to512": swMSTPInstVlanRangeList449to512,
       "swMSTPInstType": swMSTPInstType,
       "swMSTPInstStatus": swMSTPInstStatus,
       "swMSTPInstPriority": swMSTPInstPriority,
       "swMSTPInstDesignatedRootBridge": swMSTPInstDesignatedRootBridge,
       "swMSTPInstExternalRootCost": swMSTPInstExternalRootCost,
       "swMSTPInstRegionalRootBridge": swMSTPInstRegionalRootBridge,
       "swMSTPInstInternalRootCost": swMSTPInstInternalRootCost,
       "swMSTPInstDesignatedBridge": swMSTPInstDesignatedBridge,
       "swMSTPInstRootPort": swMSTPInstRootPort,
       "swMSTPInstMaxAge": swMSTPInstMaxAge,
       "swMSTPInstForwardDelay": swMSTPInstForwardDelay,
       "swMSTPInstLastTopologyChange": swMSTPInstLastTopologyChange,
       "swMSTPInstTopChangesCount": swMSTPInstTopChangesCount,
       "swMSTPInstRemainHops": swMSTPInstRemainHops,
       "swMSTPInstRowStatus": swMSTPInstRowStatus,
       "swMSTPPortTable": swMSTPPortTable,
       "swMSTPPortEntry": swMSTPPortEntry,
       "swMSTPPort": swMSTPPort,
       "swMSTPPortOperHelloTime": swMSTPPortOperHelloTime,
       "swMSTPPortAdminHelloTime": swMSTPPortAdminHelloTime,
       "swMSTPSTPPortEnable": swMSTPSTPPortEnable,
       "swMSTPPortExternalPathCost": swMSTPPortExternalPathCost,
       "swMSTPPortMigration": swMSTPPortMigration,
       "swMSTPPortAdminEdgePort": swMSTPPortAdminEdgePort,
       "swMSTPPortOperEdgePort": swMSTPPortOperEdgePort,
       "swMSTPPortAdminP2P": swMSTPPortAdminP2P,
       "swMSTPPortOperP2P": swMSTPPortOperP2P,
       "swMSTPPortLBD": swMSTPPortLBD,
       "swMSTPPortBPDUFiltering": swMSTPPortBPDUFiltering,
       "swMSTPPortRestrictedRole": swMSTPPortRestrictedRole,
       "swMSTPPortRestrictedTCN": swMSTPPortRestrictedTCN,
       "swMSTPMstPortTable": swMSTPMstPortTable,
       "swMSTPMstPortEntry": swMSTPMstPortEntry,
       "swMSTPMstPort": swMSTPMstPort,
       "swMSTPMstPortInsID": swMSTPMstPortInsID,
       "swMSTPMstPortDesignatedBridge": swMSTPMstPortDesignatedBridge,
       "swMSTPMstPortInternalPathCost": swMSTPMstPortInternalPathCost,
       "swMSTPMstPortPriority": swMSTPMstPortPriority,
       "swMSTPMstPortStatus": swMSTPMstPortStatus,
       "swMSTPMstPortRole": swMSTPMstPortRole}
)
