# SNMP MIB module (CHECKPOINT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CHECKPOINT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:38 2024
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

checkpoint = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2620)
)
checkpoint.setRevisions(
        ("2013-12-26 13:09",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1)
)
_Fw_ObjectIdentity = ObjectIdentity
fw = _Fw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1)
)
_FwTrapPrefix_ObjectIdentity = ObjectIdentity
fwTrapPrefix = _FwTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 0)
)


class _FwModuleState_Type(DisplayString):
    """Custom type fwModuleState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwModuleState_Type.__name__ = "DisplayString"
_FwModuleState_Object = MibScalar
fwModuleState = _FwModuleState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 1),
    _FwModuleState_Type()
)
fwModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwModuleState.setStatus("current")


class _FwFilterName_Type(DisplayString):
    """Custom type fwFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwFilterName_Type.__name__ = "DisplayString"
_FwFilterName_Object = MibScalar
fwFilterName = _FwFilterName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 2),
    _FwFilterName_Type()
)
fwFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwFilterName.setStatus("current")


class _FwFilterDate_Type(DisplayString):
    """Custom type fwFilterDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwFilterDate_Type.__name__ = "DisplayString"
_FwFilterDate_Object = MibScalar
fwFilterDate = _FwFilterDate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 3),
    _FwFilterDate_Type()
)
fwFilterDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwFilterDate.setStatus("current")
_FwAccepted_Type = Integer32
_FwAccepted_Object = MibScalar
fwAccepted = _FwAccepted_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 4),
    _FwAccepted_Type()
)
fwAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwAccepted.setStatus("current")
_FwRejected_Type = Integer32
_FwRejected_Object = MibScalar
fwRejected = _FwRejected_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 5),
    _FwRejected_Type()
)
fwRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwRejected.setStatus("current")
_FwDropped_Type = Integer32
_FwDropped_Object = MibScalar
fwDropped = _FwDropped_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 6),
    _FwDropped_Type()
)
fwDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDropped.setStatus("current")
_FwLogged_Type = Integer32
_FwLogged_Object = MibScalar
fwLogged = _FwLogged_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 7),
    _FwLogged_Type()
)
fwLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwLogged.setStatus("current")
_FwMajor_Type = Integer32
_FwMajor_Object = MibScalar
fwMajor = _FwMajor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 8),
    _FwMajor_Type()
)
fwMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMajor.setStatus("current")
_FwMinor_Type = Integer32
_FwMinor_Object = MibScalar
fwMinor = _FwMinor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 9),
    _FwMinor_Type()
)
fwMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMinor.setStatus("current")


class _FwProduct_Type(DisplayString):
    """Custom type fwProduct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwProduct_Type.__name__ = "DisplayString"
_FwProduct_Object = MibScalar
fwProduct = _FwProduct_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 10),
    _FwProduct_Type()
)
fwProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwProduct.setStatus("current")


class _FwEvent_Type(DisplayString):
    """Custom type fwEvent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwEvent_Type.__name__ = "DisplayString"
_FwEvent_Object = MibScalar
fwEvent = _FwEvent_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 11),
    _FwEvent_Type()
)
fwEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwEvent.setStatus("current")


class _FwSICTrustState_Type(DisplayString):
    """Custom type fwSICTrustState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwSICTrustState_Type.__name__ = "DisplayString"
_FwSICTrustState_Object = MibScalar
fwSICTrustState = _FwSICTrustState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 12),
    _FwSICTrustState_Type()
)
fwSICTrustState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSICTrustState.setStatus("current")


class _FwProdName_Type(DisplayString):
    """Custom type fwProdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwProdName_Type.__name__ = "DisplayString"
_FwProdName_Object = MibScalar
fwProdName = _FwProdName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 21),
    _FwProdName_Type()
)
fwProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwProdName.setStatus("current")
_FwVerMajor_Type = Integer32
_FwVerMajor_Object = MibScalar
fwVerMajor = _FwVerMajor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 22),
    _FwVerMajor_Type()
)
fwVerMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVerMajor.setStatus("current")
_FwVerMinor_Type = Integer32
_FwVerMinor_Object = MibScalar
fwVerMinor = _FwVerMinor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 23),
    _FwVerMinor_Type()
)
fwVerMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVerMinor.setStatus("current")
_FwKernelBuild_Type = Integer32
_FwKernelBuild_Object = MibScalar
fwKernelBuild = _FwKernelBuild_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 24),
    _FwKernelBuild_Type()
)
fwKernelBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwKernelBuild.setStatus("current")
_FwPolicyStat_ObjectIdentity = ObjectIdentity
fwPolicyStat = _FwPolicyStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25)
)


class _FwPolicyName_Type(DisplayString):
    """Custom type fwPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwPolicyName_Type.__name__ = "DisplayString"
_FwPolicyName_Object = MibScalar
fwPolicyName = _FwPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 1),
    _FwPolicyName_Type()
)
fwPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPolicyName.setStatus("current")


class _FwInstallTime_Type(DisplayString):
    """Custom type fwInstallTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwInstallTime_Type.__name__ = "DisplayString"
_FwInstallTime_Object = MibScalar
fwInstallTime = _FwInstallTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 2),
    _FwInstallTime_Type()
)
fwInstallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwInstallTime.setStatus("current")
_FwNumConn_Type = Integer32
_FwNumConn_Object = MibScalar
fwNumConn = _FwNumConn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 3),
    _FwNumConn_Type()
)
fwNumConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwNumConn.setStatus("current")
_FwPeakNumConn_Type = Integer32
_FwPeakNumConn_Object = MibScalar
fwPeakNumConn = _FwPeakNumConn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 4),
    _FwPeakNumConn_Type()
)
fwPeakNumConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPeakNumConn.setStatus("current")
_FwIfTable_Object = MibTable
fwIfTable = _FwIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 5)
)
if mibBuilder.loadTexts:
    fwIfTable.setStatus("current")
_FwIfEntry_Object = MibTableRow
fwIfEntry = _FwIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 5, 1)
)
fwIfEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "fwIfIndex"),
)
if mibBuilder.loadTexts:
    fwIfEntry.setStatus("current")
_FwIfIndex_Type = Unsigned32
_FwIfIndex_Object = MibTableColumn
fwIfIndex = _FwIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 5, 1, 1),
    _FwIfIndex_Type()
)
fwIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfIndex.setStatus("current")
_FwIfName_Type = DisplayString
_FwIfName_Object = MibTableColumn
fwIfName = _FwIfName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 5, 1, 2),
    _FwIfName_Type()
)
fwIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwIfName.setStatus("current")
_FwAcceptPcktsIn_Type = Integer32
_FwAcceptPcktsIn_Object = MibTableColumn
fwAcceptPcktsIn = _FwAcceptPcktsIn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 5, 1, 5),
    _FwAcceptPcktsIn_Type()
)
fwAcceptPcktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwAcceptPcktsIn.setStatus("current")
_FwAcceptPcktsOut_Type = Integer32
_FwAcceptPcktsOut_Object = MibTableColumn
fwAcceptPcktsOut = _FwAcceptPcktsOut_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 5, 1, 6),
    _FwAcceptPcktsOut_Type()
)
fwAcceptPcktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwAcceptPcktsOut.setStatus("current")
_FwAcceptBytesIn_Type = Integer32
_FwAcceptBytesIn_Object = MibTableColumn
fwAcceptBytesIn = _FwAcceptBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 5, 1, 7),
    _FwAcceptBytesIn_Type()
)
fwAcceptBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwAcceptBytesIn.setStatus("current")
_FwAcceptBytesOut_Type = Integer32
_FwAcceptBytesOut_Object = MibTableColumn
fwAcceptBytesOut = _FwAcceptBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 5, 1, 8),
    _FwAcceptBytesOut_Type()
)
fwAcceptBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwAcceptBytesOut.setStatus("current")
_FwDropPcktsIn_Type = Integer32
_FwDropPcktsIn_Object = MibTableColumn
fwDropPcktsIn = _FwDropPcktsIn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 5, 1, 9),
    _FwDropPcktsIn_Type()
)
fwDropPcktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDropPcktsIn.setStatus("current")
_FwDropPcktsOut_Type = Integer32
_FwDropPcktsOut_Object = MibTableColumn
fwDropPcktsOut = _FwDropPcktsOut_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 5, 1, 10),
    _FwDropPcktsOut_Type()
)
fwDropPcktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDropPcktsOut.setStatus("current")
_FwRejectPcktsIn_Type = Integer32
_FwRejectPcktsIn_Object = MibTableColumn
fwRejectPcktsIn = _FwRejectPcktsIn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 5, 1, 11),
    _FwRejectPcktsIn_Type()
)
fwRejectPcktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwRejectPcktsIn.setStatus("current")
_FwRejectPcktsOut_Type = Integer32
_FwRejectPcktsOut_Object = MibTableColumn
fwRejectPcktsOut = _FwRejectPcktsOut_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 5, 1, 12),
    _FwRejectPcktsOut_Type()
)
fwRejectPcktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwRejectPcktsOut.setStatus("current")
_FwLogIn_Type = Integer32
_FwLogIn_Object = MibTableColumn
fwLogIn = _FwLogIn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 5, 1, 13),
    _FwLogIn_Type()
)
fwLogIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwLogIn.setStatus("current")
_FwLogOut_Type = Integer32
_FwLogOut_Object = MibTableColumn
fwLogOut = _FwLogOut_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 5, 1, 14),
    _FwLogOut_Type()
)
fwLogOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwLogOut.setStatus("current")


class _FwPacketsRate_Type(DisplayString):
    """Custom type fwPacketsRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwPacketsRate_Type.__name__ = "DisplayString"
_FwPacketsRate_Object = MibScalar
fwPacketsRate = _FwPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 6),
    _FwPacketsRate_Type()
)
fwPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwPacketsRate.setStatus("current")


class _FwAcceptedBytesTotalRate_Type(DisplayString):
    """Custom type fwAcceptedBytesTotalRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwAcceptedBytesTotalRate_Type.__name__ = "DisplayString"
_FwAcceptedBytesTotalRate_Object = MibScalar
fwAcceptedBytesTotalRate = _FwAcceptedBytesTotalRate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 8),
    _FwAcceptedBytesTotalRate_Type()
)
fwAcceptedBytesTotalRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwAcceptedBytesTotalRate.setStatus("current")


class _FwDroppedBytesTotalRate_Type(DisplayString):
    """Custom type fwDroppedBytesTotalRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwDroppedBytesTotalRate_Type.__name__ = "DisplayString"
_FwDroppedBytesTotalRate_Object = MibScalar
fwDroppedBytesTotalRate = _FwDroppedBytesTotalRate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 9),
    _FwDroppedBytesTotalRate_Type()
)
fwDroppedBytesTotalRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDroppedBytesTotalRate.setStatus("current")
_FwConnTableLimit_Type = Integer32
_FwConnTableLimit_Object = MibScalar
fwConnTableLimit = _FwConnTableLimit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 10),
    _FwConnTableLimit_Type()
)
fwConnTableLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwConnTableLimit.setStatus("current")


class _FwDroppedTotalRate_Type(DisplayString):
    """Custom type fwDroppedTotalRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwDroppedTotalRate_Type.__name__ = "DisplayString"
_FwDroppedTotalRate_Object = MibScalar
fwDroppedTotalRate = _FwDroppedTotalRate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 25, 16),
    _FwDroppedTotalRate_Type()
)
fwDroppedTotalRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDroppedTotalRate.setStatus("current")
_FwPerfStat_ObjectIdentity = ObjectIdentity
fwPerfStat = _FwPerfStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26)
)
_FwHmem_ObjectIdentity = ObjectIdentity
fwHmem = _FwHmem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1)
)
_FwHmem_block_size_Type = Integer32
_FwHmem_block_size_Object = MibScalar
fwHmem_block_size = _FwHmem_block_size_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1, 1),
    _FwHmem_block_size_Type()
)
fwHmem_block_size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem_block_size.setStatus("current")
_FwHmem_requested_bytes_Type = Integer32
_FwHmem_requested_bytes_Object = MibScalar
fwHmem_requested_bytes = _FwHmem_requested_bytes_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1, 2),
    _FwHmem_requested_bytes_Type()
)
fwHmem_requested_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem_requested_bytes.setStatus("current")
_FwHmem_initial_allocated_bytes_Type = Integer32
_FwHmem_initial_allocated_bytes_Object = MibScalar
fwHmem_initial_allocated_bytes = _FwHmem_initial_allocated_bytes_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1, 3),
    _FwHmem_initial_allocated_bytes_Type()
)
fwHmem_initial_allocated_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem_initial_allocated_bytes.setStatus("current")
_FwHmem_initial_allocated_blocks_Type = Integer32
_FwHmem_initial_allocated_blocks_Object = MibScalar
fwHmem_initial_allocated_blocks = _FwHmem_initial_allocated_blocks_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1, 4),
    _FwHmem_initial_allocated_blocks_Type()
)
fwHmem_initial_allocated_blocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem_initial_allocated_blocks.setStatus("current")
_FwHmem_initial_allocated_pools_Type = Integer32
_FwHmem_initial_allocated_pools_Object = MibScalar
fwHmem_initial_allocated_pools = _FwHmem_initial_allocated_pools_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1, 5),
    _FwHmem_initial_allocated_pools_Type()
)
fwHmem_initial_allocated_pools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem_initial_allocated_pools.setStatus("current")
_FwHmem_current_allocated_bytes_Type = Integer32
_FwHmem_current_allocated_bytes_Object = MibScalar
fwHmem_current_allocated_bytes = _FwHmem_current_allocated_bytes_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1, 6),
    _FwHmem_current_allocated_bytes_Type()
)
fwHmem_current_allocated_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem_current_allocated_bytes.setStatus("current")
_FwHmem_current_allocated_blocks_Type = Integer32
_FwHmem_current_allocated_blocks_Object = MibScalar
fwHmem_current_allocated_blocks = _FwHmem_current_allocated_blocks_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1, 7),
    _FwHmem_current_allocated_blocks_Type()
)
fwHmem_current_allocated_blocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem_current_allocated_blocks.setStatus("current")
_FwHmem_current_allocated_pools_Type = Integer32
_FwHmem_current_allocated_pools_Object = MibScalar
fwHmem_current_allocated_pools = _FwHmem_current_allocated_pools_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1, 8),
    _FwHmem_current_allocated_pools_Type()
)
fwHmem_current_allocated_pools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem_current_allocated_pools.setStatus("current")
_FwHmem_maximum_bytes_Type = Integer32
_FwHmem_maximum_bytes_Object = MibScalar
fwHmem_maximum_bytes = _FwHmem_maximum_bytes_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1, 9),
    _FwHmem_maximum_bytes_Type()
)
fwHmem_maximum_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem_maximum_bytes.setStatus("current")
_FwHmem_maximum_pools_Type = Integer32
_FwHmem_maximum_pools_Object = MibScalar
fwHmem_maximum_pools = _FwHmem_maximum_pools_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1, 10),
    _FwHmem_maximum_pools_Type()
)
fwHmem_maximum_pools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem_maximum_pools.setStatus("current")
_FwHmem_bytes_used_Type = Integer32
_FwHmem_bytes_used_Object = MibScalar
fwHmem_bytes_used = _FwHmem_bytes_used_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1, 11),
    _FwHmem_bytes_used_Type()
)
fwHmem_bytes_used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem_bytes_used.setStatus("current")
_FwHmem_blocks_used_Type = Integer32
_FwHmem_blocks_used_Object = MibScalar
fwHmem_blocks_used = _FwHmem_blocks_used_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1, 12),
    _FwHmem_blocks_used_Type()
)
fwHmem_blocks_used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem_blocks_used.setStatus("current")
_FwHmem_bytes_unused_Type = Integer32
_FwHmem_bytes_unused_Object = MibScalar
fwHmem_bytes_unused = _FwHmem_bytes_unused_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1, 13),
    _FwHmem_bytes_unused_Type()
)
fwHmem_bytes_unused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem_bytes_unused.setStatus("current")
_FwHmem_blocks_unused_Type = Integer32
_FwHmem_blocks_unused_Object = MibScalar
fwHmem_blocks_unused = _FwHmem_blocks_unused_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1, 14),
    _FwHmem_blocks_unused_Type()
)
fwHmem_blocks_unused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem_blocks_unused.setStatus("current")
_FwHmem_bytes_peak_Type = Integer32
_FwHmem_bytes_peak_Object = MibScalar
fwHmem_bytes_peak = _FwHmem_bytes_peak_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1, 15),
    _FwHmem_bytes_peak_Type()
)
fwHmem_bytes_peak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem_bytes_peak.setStatus("current")
_FwHmem_blocks_peak_Type = Integer32
_FwHmem_blocks_peak_Object = MibScalar
fwHmem_blocks_peak = _FwHmem_blocks_peak_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1, 16),
    _FwHmem_blocks_peak_Type()
)
fwHmem_blocks_peak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem_blocks_peak.setStatus("current")
_FwHmem_bytes_internal_use_Type = Integer32
_FwHmem_bytes_internal_use_Object = MibScalar
fwHmem_bytes_internal_use = _FwHmem_bytes_internal_use_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1, 17),
    _FwHmem_bytes_internal_use_Type()
)
fwHmem_bytes_internal_use.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem_bytes_internal_use.setStatus("current")
_FwHmem_number_of_items_Type = Integer32
_FwHmem_number_of_items_Object = MibScalar
fwHmem_number_of_items = _FwHmem_number_of_items_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1, 18),
    _FwHmem_number_of_items_Type()
)
fwHmem_number_of_items.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem_number_of_items.setStatus("current")
_FwHmem_alloc_operations_Type = Integer32
_FwHmem_alloc_operations_Object = MibScalar
fwHmem_alloc_operations = _FwHmem_alloc_operations_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1, 19),
    _FwHmem_alloc_operations_Type()
)
fwHmem_alloc_operations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem_alloc_operations.setStatus("current")
_FwHmem_free_operations_Type = Integer32
_FwHmem_free_operations_Object = MibScalar
fwHmem_free_operations = _FwHmem_free_operations_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1, 20),
    _FwHmem_free_operations_Type()
)
fwHmem_free_operations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem_free_operations.setStatus("current")
_FwHmem_failed_alloc_Type = Integer32
_FwHmem_failed_alloc_Object = MibScalar
fwHmem_failed_alloc = _FwHmem_failed_alloc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1, 21),
    _FwHmem_failed_alloc_Type()
)
fwHmem_failed_alloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem_failed_alloc.setStatus("current")
_FwHmem_failed_free_Type = Integer32
_FwHmem_failed_free_Object = MibScalar
fwHmem_failed_free = _FwHmem_failed_free_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 1, 22),
    _FwHmem_failed_free_Type()
)
fwHmem_failed_free.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem_failed_free.setStatus("current")
_FwKmem_ObjectIdentity = ObjectIdentity
fwKmem = _FwKmem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 2)
)
_FwKmem_system_physical_mem_Type = Integer32
_FwKmem_system_physical_mem_Object = MibScalar
fwKmem_system_physical_mem = _FwKmem_system_physical_mem_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 2, 1),
    _FwKmem_system_physical_mem_Type()
)
fwKmem_system_physical_mem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwKmem_system_physical_mem.setStatus("current")
_FwKmem_available_physical_mem_Type = Integer32
_FwKmem_available_physical_mem_Object = MibScalar
fwKmem_available_physical_mem = _FwKmem_available_physical_mem_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 2, 2),
    _FwKmem_available_physical_mem_Type()
)
fwKmem_available_physical_mem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwKmem_available_physical_mem.setStatus("current")
_FwKmem_aix_heap_size_Type = Integer32
_FwKmem_aix_heap_size_Object = MibScalar
fwKmem_aix_heap_size = _FwKmem_aix_heap_size_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 2, 3),
    _FwKmem_aix_heap_size_Type()
)
fwKmem_aix_heap_size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwKmem_aix_heap_size.setStatus("current")
_FwKmem_bytes_used_Type = Integer32
_FwKmem_bytes_used_Object = MibScalar
fwKmem_bytes_used = _FwKmem_bytes_used_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 2, 4),
    _FwKmem_bytes_used_Type()
)
fwKmem_bytes_used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwKmem_bytes_used.setStatus("current")
_FwKmem_blocking_bytes_used_Type = Integer32
_FwKmem_blocking_bytes_used_Object = MibScalar
fwKmem_blocking_bytes_used = _FwKmem_blocking_bytes_used_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 2, 5),
    _FwKmem_blocking_bytes_used_Type()
)
fwKmem_blocking_bytes_used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwKmem_blocking_bytes_used.setStatus("current")
_FwKmem_non_blocking_bytes_used_Type = Integer32
_FwKmem_non_blocking_bytes_used_Object = MibScalar
fwKmem_non_blocking_bytes_used = _FwKmem_non_blocking_bytes_used_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 2, 6),
    _FwKmem_non_blocking_bytes_used_Type()
)
fwKmem_non_blocking_bytes_used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwKmem_non_blocking_bytes_used.setStatus("current")
_FwKmem_bytes_unused_Type = Integer32
_FwKmem_bytes_unused_Object = MibScalar
fwKmem_bytes_unused = _FwKmem_bytes_unused_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 2, 7),
    _FwKmem_bytes_unused_Type()
)
fwKmem_bytes_unused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwKmem_bytes_unused.setStatus("current")
_FwKmem_bytes_peak_Type = Integer32
_FwKmem_bytes_peak_Object = MibScalar
fwKmem_bytes_peak = _FwKmem_bytes_peak_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 2, 8),
    _FwKmem_bytes_peak_Type()
)
fwKmem_bytes_peak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwKmem_bytes_peak.setStatus("current")
_FwKmem_blocking_bytes_peak_Type = Integer32
_FwKmem_blocking_bytes_peak_Object = MibScalar
fwKmem_blocking_bytes_peak = _FwKmem_blocking_bytes_peak_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 2, 9),
    _FwKmem_blocking_bytes_peak_Type()
)
fwKmem_blocking_bytes_peak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwKmem_blocking_bytes_peak.setStatus("current")
_FwKmem_non_blocking_bytes_peak_Type = Integer32
_FwKmem_non_blocking_bytes_peak_Object = MibScalar
fwKmem_non_blocking_bytes_peak = _FwKmem_non_blocking_bytes_peak_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 2, 10),
    _FwKmem_non_blocking_bytes_peak_Type()
)
fwKmem_non_blocking_bytes_peak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwKmem_non_blocking_bytes_peak.setStatus("current")
_FwKmem_bytes_internal_use_Type = Integer32
_FwKmem_bytes_internal_use_Object = MibScalar
fwKmem_bytes_internal_use = _FwKmem_bytes_internal_use_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 2, 11),
    _FwKmem_bytes_internal_use_Type()
)
fwKmem_bytes_internal_use.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwKmem_bytes_internal_use.setStatus("current")
_FwKmem_number_of_items_Type = Integer32
_FwKmem_number_of_items_Object = MibScalar
fwKmem_number_of_items = _FwKmem_number_of_items_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 2, 12),
    _FwKmem_number_of_items_Type()
)
fwKmem_number_of_items.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwKmem_number_of_items.setStatus("current")
_FwKmem_alloc_operations_Type = Integer32
_FwKmem_alloc_operations_Object = MibScalar
fwKmem_alloc_operations = _FwKmem_alloc_operations_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 2, 13),
    _FwKmem_alloc_operations_Type()
)
fwKmem_alloc_operations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwKmem_alloc_operations.setStatus("current")
_FwKmem_free_operations_Type = Integer32
_FwKmem_free_operations_Object = MibScalar
fwKmem_free_operations = _FwKmem_free_operations_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 2, 14),
    _FwKmem_free_operations_Type()
)
fwKmem_free_operations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwKmem_free_operations.setStatus("current")
_FwKmem_failed_alloc_Type = Integer32
_FwKmem_failed_alloc_Object = MibScalar
fwKmem_failed_alloc = _FwKmem_failed_alloc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 2, 15),
    _FwKmem_failed_alloc_Type()
)
fwKmem_failed_alloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwKmem_failed_alloc.setStatus("current")
_FwKmem_failed_free_Type = Integer32
_FwKmem_failed_free_Object = MibScalar
fwKmem_failed_free = _FwKmem_failed_free_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 2, 16),
    _FwKmem_failed_free_Type()
)
fwKmem_failed_free.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwKmem_failed_free.setStatus("current")
_FwInspect_ObjectIdentity = ObjectIdentity
fwInspect = _FwInspect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 3)
)
_FwInspect_packets_Type = Integer32
_FwInspect_packets_Object = MibScalar
fwInspect_packets = _FwInspect_packets_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 3, 1),
    _FwInspect_packets_Type()
)
fwInspect_packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwInspect_packets.setStatus("current")
_FwInspect_operations_Type = Integer32
_FwInspect_operations_Object = MibScalar
fwInspect_operations = _FwInspect_operations_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 3, 2),
    _FwInspect_operations_Type()
)
fwInspect_operations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwInspect_operations.setStatus("current")
_FwInspect_lookups_Type = Integer32
_FwInspect_lookups_Object = MibScalar
fwInspect_lookups = _FwInspect_lookups_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 3, 3),
    _FwInspect_lookups_Type()
)
fwInspect_lookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwInspect_lookups.setStatus("current")
_FwInspect_record_Type = Integer32
_FwInspect_record_Object = MibScalar
fwInspect_record = _FwInspect_record_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 3, 4),
    _FwInspect_record_Type()
)
fwInspect_record.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwInspect_record.setStatus("current")
_FwInspect_extract_Type = Integer32
_FwInspect_extract_Object = MibScalar
fwInspect_extract = _FwInspect_extract_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 3, 5),
    _FwInspect_extract_Type()
)
fwInspect_extract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwInspect_extract.setStatus("current")
_FwCookies_ObjectIdentity = ObjectIdentity
fwCookies = _FwCookies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 4)
)
_FwCookies_total_Type = Integer32
_FwCookies_total_Object = MibScalar
fwCookies_total = _FwCookies_total_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 4, 1),
    _FwCookies_total_Type()
)
fwCookies_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCookies_total.setStatus("current")
_FwCookies_allocfwCookies_total_Type = Integer32
_FwCookies_allocfwCookies_total_Object = MibScalar
fwCookies_allocfwCookies_total = _FwCookies_allocfwCookies_total_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 4, 2),
    _FwCookies_allocfwCookies_total_Type()
)
fwCookies_allocfwCookies_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCookies_allocfwCookies_total.setStatus("current")
_FwCookies_freefwCookies_total_Type = Integer32
_FwCookies_freefwCookies_total_Object = MibScalar
fwCookies_freefwCookies_total = _FwCookies_freefwCookies_total_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 4, 3),
    _FwCookies_freefwCookies_total_Type()
)
fwCookies_freefwCookies_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCookies_freefwCookies_total.setStatus("current")
_FwCookies_dupfwCookies_total_Type = Integer32
_FwCookies_dupfwCookies_total_Object = MibScalar
fwCookies_dupfwCookies_total = _FwCookies_dupfwCookies_total_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 4, 4),
    _FwCookies_dupfwCookies_total_Type()
)
fwCookies_dupfwCookies_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCookies_dupfwCookies_total.setStatus("current")
_FwCookies_getfwCookies_total_Type = Integer32
_FwCookies_getfwCookies_total_Object = MibScalar
fwCookies_getfwCookies_total = _FwCookies_getfwCookies_total_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 4, 5),
    _FwCookies_getfwCookies_total_Type()
)
fwCookies_getfwCookies_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCookies_getfwCookies_total.setStatus("current")
_FwCookies_putfwCookies_total_Type = Integer32
_FwCookies_putfwCookies_total_Object = MibScalar
fwCookies_putfwCookies_total = _FwCookies_putfwCookies_total_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 4, 6),
    _FwCookies_putfwCookies_total_Type()
)
fwCookies_putfwCookies_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCookies_putfwCookies_total.setStatus("current")
_FwCookies_lenfwCookies_total_Type = Integer32
_FwCookies_lenfwCookies_total_Object = MibScalar
fwCookies_lenfwCookies_total = _FwCookies_lenfwCookies_total_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 4, 7),
    _FwCookies_lenfwCookies_total_Type()
)
fwCookies_lenfwCookies_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwCookies_lenfwCookies_total.setStatus("current")
_FwChains_ObjectIdentity = ObjectIdentity
fwChains = _FwChains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 5)
)
_FwChains_alloc_Type = Integer32
_FwChains_alloc_Object = MibScalar
fwChains_alloc = _FwChains_alloc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 5, 1),
    _FwChains_alloc_Type()
)
fwChains_alloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwChains_alloc.setStatus("current")
_FwChains_free_Type = Integer32
_FwChains_free_Object = MibScalar
fwChains_free = _FwChains_free_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 5, 2),
    _FwChains_free_Type()
)
fwChains_free.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwChains_free.setStatus("current")
_FwFragments_ObjectIdentity = ObjectIdentity
fwFragments = _FwFragments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 6)
)
_FwFrag_fragments_Type = Integer32
_FwFrag_fragments_Object = MibScalar
fwFrag_fragments = _FwFrag_fragments_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 6, 1),
    _FwFrag_fragments_Type()
)
fwFrag_fragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwFrag_fragments.setStatus("current")
_FwFrag_expired_Type = Integer32
_FwFrag_expired_Object = MibScalar
fwFrag_expired = _FwFrag_expired_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 6, 2),
    _FwFrag_expired_Type()
)
fwFrag_expired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwFrag_expired.setStatus("current")
_FwFrag_packets_Type = Integer32
_FwFrag_packets_Object = MibScalar
fwFrag_packets = _FwFrag_packets_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 6, 3),
    _FwFrag_packets_Type()
)
fwFrag_packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwFrag_packets.setStatus("current")
_FwUfp_ObjectIdentity = ObjectIdentity
fwUfp = _FwUfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 8)
)
_FwUfpHitRatio_Type = Integer32
_FwUfpHitRatio_Object = MibScalar
fwUfpHitRatio = _FwUfpHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 8, 1),
    _FwUfpHitRatio_Type()
)
fwUfpHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwUfpHitRatio.setStatus("current")
_FwUfpInspected_Type = Integer32
_FwUfpInspected_Object = MibScalar
fwUfpInspected = _FwUfpInspected_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 8, 2),
    _FwUfpInspected_Type()
)
fwUfpInspected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwUfpInspected.setStatus("current")
_FwUfpHits_Type = Integer32
_FwUfpHits_Object = MibScalar
fwUfpHits = _FwUfpHits_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 8, 3),
    _FwUfpHits_Type()
)
fwUfpHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwUfpHits.setStatus("current")
_FwSS_ObjectIdentity = ObjectIdentity
fwSS = _FwSS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9)
)
_FwSS_http_ObjectIdentity = ObjectIdentity
fwSS_http = _FwSS_http_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1)
)
_FwSS_http_pid_Type = Integer32
_FwSS_http_pid_Object = MibScalar
fwSS_http_pid = _FwSS_http_pid_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 1),
    _FwSS_http_pid_Type()
)
fwSS_http_pid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_pid.setStatus("current")
_FwSS_http_proto_Type = Integer32
_FwSS_http_proto_Object = MibScalar
fwSS_http_proto = _FwSS_http_proto_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 2),
    _FwSS_http_proto_Type()
)
fwSS_http_proto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_proto.setStatus("current")
_FwSS_http_port_Type = Integer32
_FwSS_http_port_Object = MibScalar
fwSS_http_port = _FwSS_http_port_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 3),
    _FwSS_http_port_Type()
)
fwSS_http_port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_port.setStatus("current")
_FwSS_http_logical_port_Type = Integer32
_FwSS_http_logical_port_Object = MibScalar
fwSS_http_logical_port = _FwSS_http_logical_port_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 4),
    _FwSS_http_logical_port_Type()
)
fwSS_http_logical_port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_logical_port.setStatus("current")
_FwSS_http_max_avail_socket_Type = Integer32
_FwSS_http_max_avail_socket_Object = MibScalar
fwSS_http_max_avail_socket = _FwSS_http_max_avail_socket_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 5),
    _FwSS_http_max_avail_socket_Type()
)
fwSS_http_max_avail_socket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_max_avail_socket.setStatus("current")
_FwSS_http_socket_in_use_max_Type = Integer32
_FwSS_http_socket_in_use_max_Object = MibScalar
fwSS_http_socket_in_use_max = _FwSS_http_socket_in_use_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 6),
    _FwSS_http_socket_in_use_max_Type()
)
fwSS_http_socket_in_use_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_socket_in_use_max.setStatus("current")
_FwSS_http_socket_in_use_curr_Type = Integer32
_FwSS_http_socket_in_use_curr_Object = MibScalar
fwSS_http_socket_in_use_curr = _FwSS_http_socket_in_use_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 7),
    _FwSS_http_socket_in_use_curr_Type()
)
fwSS_http_socket_in_use_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_socket_in_use_curr.setStatus("current")
_FwSS_http_socket_in_use_count_Type = Integer32
_FwSS_http_socket_in_use_count_Object = MibScalar
fwSS_http_socket_in_use_count = _FwSS_http_socket_in_use_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 8),
    _FwSS_http_socket_in_use_count_Type()
)
fwSS_http_socket_in_use_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_socket_in_use_count.setStatus("current")
_FwSS_http_sess_max_Type = Integer32
_FwSS_http_sess_max_Object = MibScalar
fwSS_http_sess_max = _FwSS_http_sess_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 9),
    _FwSS_http_sess_max_Type()
)
fwSS_http_sess_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_sess_max.setStatus("current")
_FwSS_http_sess_curr_Type = Integer32
_FwSS_http_sess_curr_Object = MibScalar
fwSS_http_sess_curr = _FwSS_http_sess_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 10),
    _FwSS_http_sess_curr_Type()
)
fwSS_http_sess_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_sess_curr.setStatus("current")
_FwSS_http_sess_count_Type = Integer32
_FwSS_http_sess_count_Object = MibScalar
fwSS_http_sess_count = _FwSS_http_sess_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 11),
    _FwSS_http_sess_count_Type()
)
fwSS_http_sess_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_sess_count.setStatus("current")
_FwSS_http_auth_sess_max_Type = Integer32
_FwSS_http_auth_sess_max_Object = MibScalar
fwSS_http_auth_sess_max = _FwSS_http_auth_sess_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 12),
    _FwSS_http_auth_sess_max_Type()
)
fwSS_http_auth_sess_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_auth_sess_max.setStatus("current")
_FwSS_http_auth_sess_curr_Type = Integer32
_FwSS_http_auth_sess_curr_Object = MibScalar
fwSS_http_auth_sess_curr = _FwSS_http_auth_sess_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 13),
    _FwSS_http_auth_sess_curr_Type()
)
fwSS_http_auth_sess_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_auth_sess_curr.setStatus("current")
_FwSS_http_auth_sess_count_Type = Integer32
_FwSS_http_auth_sess_count_Object = MibScalar
fwSS_http_auth_sess_count = _FwSS_http_auth_sess_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 14),
    _FwSS_http_auth_sess_count_Type()
)
fwSS_http_auth_sess_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_auth_sess_count.setStatus("current")
_FwSS_http_accepted_sess_Type = Integer32
_FwSS_http_accepted_sess_Object = MibScalar
fwSS_http_accepted_sess = _FwSS_http_accepted_sess_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 15),
    _FwSS_http_accepted_sess_Type()
)
fwSS_http_accepted_sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_accepted_sess.setStatus("current")
_FwSS_http_rejected_sess_Type = Integer32
_FwSS_http_rejected_sess_Object = MibScalar
fwSS_http_rejected_sess = _FwSS_http_rejected_sess_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 16),
    _FwSS_http_rejected_sess_Type()
)
fwSS_http_rejected_sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_rejected_sess.setStatus("current")
_FwSS_http_auth_failures_Type = Integer32
_FwSS_http_auth_failures_Object = MibScalar
fwSS_http_auth_failures = _FwSS_http_auth_failures_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 17),
    _FwSS_http_auth_failures_Type()
)
fwSS_http_auth_failures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_auth_failures.setStatus("current")
_FwSS_http_ops_cvp_sess_max_Type = Integer32
_FwSS_http_ops_cvp_sess_max_Object = MibScalar
fwSS_http_ops_cvp_sess_max = _FwSS_http_ops_cvp_sess_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 18),
    _FwSS_http_ops_cvp_sess_max_Type()
)
fwSS_http_ops_cvp_sess_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_ops_cvp_sess_max.setStatus("current")
_FwSS_http_ops_cvp_sess_curr_Type = Integer32
_FwSS_http_ops_cvp_sess_curr_Object = MibScalar
fwSS_http_ops_cvp_sess_curr = _FwSS_http_ops_cvp_sess_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 19),
    _FwSS_http_ops_cvp_sess_curr_Type()
)
fwSS_http_ops_cvp_sess_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_ops_cvp_sess_curr.setStatus("current")
_FwSS_http_ops_cvp_sess_count_Type = Integer32
_FwSS_http_ops_cvp_sess_count_Object = MibScalar
fwSS_http_ops_cvp_sess_count = _FwSS_http_ops_cvp_sess_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 20),
    _FwSS_http_ops_cvp_sess_count_Type()
)
fwSS_http_ops_cvp_sess_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_ops_cvp_sess_count.setStatus("current")
_FwSS_http_ops_cvp_rej_sess_Type = Integer32
_FwSS_http_ops_cvp_rej_sess_Object = MibScalar
fwSS_http_ops_cvp_rej_sess = _FwSS_http_ops_cvp_rej_sess_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 21),
    _FwSS_http_ops_cvp_rej_sess_Type()
)
fwSS_http_ops_cvp_rej_sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_ops_cvp_rej_sess.setStatus("current")
_FwSS_http_ssl_encryp_sess_max_Type = Integer32
_FwSS_http_ssl_encryp_sess_max_Object = MibScalar
fwSS_http_ssl_encryp_sess_max = _FwSS_http_ssl_encryp_sess_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 22),
    _FwSS_http_ssl_encryp_sess_max_Type()
)
fwSS_http_ssl_encryp_sess_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_ssl_encryp_sess_max.setStatus("current")
_FwSS_http_ssl_encryp_sess_curr_Type = Integer32
_FwSS_http_ssl_encryp_sess_curr_Object = MibScalar
fwSS_http_ssl_encryp_sess_curr = _FwSS_http_ssl_encryp_sess_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 23),
    _FwSS_http_ssl_encryp_sess_curr_Type()
)
fwSS_http_ssl_encryp_sess_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_ssl_encryp_sess_curr.setStatus("current")
_FwSS_http_ssl_encryp_sess_count_Type = Integer32
_FwSS_http_ssl_encryp_sess_count_Object = MibScalar
fwSS_http_ssl_encryp_sess_count = _FwSS_http_ssl_encryp_sess_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 24),
    _FwSS_http_ssl_encryp_sess_count_Type()
)
fwSS_http_ssl_encryp_sess_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_ssl_encryp_sess_count.setStatus("current")
_FwSS_http_transp_sess_max_Type = Integer32
_FwSS_http_transp_sess_max_Object = MibScalar
fwSS_http_transp_sess_max = _FwSS_http_transp_sess_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 25),
    _FwSS_http_transp_sess_max_Type()
)
fwSS_http_transp_sess_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_transp_sess_max.setStatus("current")
_FwSS_http_transp_sess_curr_Type = Integer32
_FwSS_http_transp_sess_curr_Object = MibScalar
fwSS_http_transp_sess_curr = _FwSS_http_transp_sess_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 26),
    _FwSS_http_transp_sess_curr_Type()
)
fwSS_http_transp_sess_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_transp_sess_curr.setStatus("current")
_FwSS_http_transp_sess_count_Type = Integer32
_FwSS_http_transp_sess_count_Object = MibScalar
fwSS_http_transp_sess_count = _FwSS_http_transp_sess_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 27),
    _FwSS_http_transp_sess_count_Type()
)
fwSS_http_transp_sess_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_transp_sess_count.setStatus("current")
_FwSS_http_proxied_sess_max_Type = Integer32
_FwSS_http_proxied_sess_max_Object = MibScalar
fwSS_http_proxied_sess_max = _FwSS_http_proxied_sess_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 28),
    _FwSS_http_proxied_sess_max_Type()
)
fwSS_http_proxied_sess_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_proxied_sess_max.setStatus("current")
_FwSS_http_proxied_sess_curr_Type = Integer32
_FwSS_http_proxied_sess_curr_Object = MibScalar
fwSS_http_proxied_sess_curr = _FwSS_http_proxied_sess_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 29),
    _FwSS_http_proxied_sess_curr_Type()
)
fwSS_http_proxied_sess_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_proxied_sess_curr.setStatus("current")
_FwSS_http_proxied_sess_count_Type = Integer32
_FwSS_http_proxied_sess_count_Object = MibScalar
fwSS_http_proxied_sess_count = _FwSS_http_proxied_sess_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 30),
    _FwSS_http_proxied_sess_count_Type()
)
fwSS_http_proxied_sess_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_proxied_sess_count.setStatus("current")
_FwSS_http_tunneled_sess_max_Type = Integer32
_FwSS_http_tunneled_sess_max_Object = MibScalar
fwSS_http_tunneled_sess_max = _FwSS_http_tunneled_sess_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 31),
    _FwSS_http_tunneled_sess_max_Type()
)
fwSS_http_tunneled_sess_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_tunneled_sess_max.setStatus("current")
_FwSS_http_tunneled_sess_curr_Type = Integer32
_FwSS_http_tunneled_sess_curr_Object = MibScalar
fwSS_http_tunneled_sess_curr = _FwSS_http_tunneled_sess_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 32),
    _FwSS_http_tunneled_sess_curr_Type()
)
fwSS_http_tunneled_sess_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_tunneled_sess_curr.setStatus("current")
_FwSS_http_tunneled_sess_count_Type = Integer32
_FwSS_http_tunneled_sess_count_Object = MibScalar
fwSS_http_tunneled_sess_count = _FwSS_http_tunneled_sess_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 33),
    _FwSS_http_tunneled_sess_count_Type()
)
fwSS_http_tunneled_sess_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_tunneled_sess_count.setStatus("current")
_FwSS_http_ftp_sess_max_Type = Integer32
_FwSS_http_ftp_sess_max_Object = MibScalar
fwSS_http_ftp_sess_max = _FwSS_http_ftp_sess_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 34),
    _FwSS_http_ftp_sess_max_Type()
)
fwSS_http_ftp_sess_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_ftp_sess_max.setStatus("current")
_FwSS_http_ftp_sess_curr_Type = Integer32
_FwSS_http_ftp_sess_curr_Object = MibScalar
fwSS_http_ftp_sess_curr = _FwSS_http_ftp_sess_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 35),
    _FwSS_http_ftp_sess_curr_Type()
)
fwSS_http_ftp_sess_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_ftp_sess_curr.setStatus("current")
_FwSS_http_ftp_sess_count_Type = Integer32
_FwSS_http_ftp_sess_count_Object = MibScalar
fwSS_http_ftp_sess_count = _FwSS_http_ftp_sess_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 36),
    _FwSS_http_ftp_sess_count_Type()
)
fwSS_http_ftp_sess_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_ftp_sess_count.setStatus("current")


class _FwSS_http_time_stamp_Type(DisplayString):
    """Custom type fwSS_http_time_stamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwSS_http_time_stamp_Type.__name__ = "DisplayString"
_FwSS_http_time_stamp_Object = MibScalar
fwSS_http_time_stamp = _FwSS_http_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 37),
    _FwSS_http_time_stamp_Type()
)
fwSS_http_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_time_stamp.setStatus("current")
_FwSS_http_is_alive_Type = Integer32
_FwSS_http_is_alive_Object = MibScalar
fwSS_http_is_alive = _FwSS_http_is_alive_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 38),
    _FwSS_http_is_alive_Type()
)
fwSS_http_is_alive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_is_alive.setStatus("current")
_FwSS_http_blocked_cnt_Type = Integer32
_FwSS_http_blocked_cnt_Object = MibScalar
fwSS_http_blocked_cnt = _FwSS_http_blocked_cnt_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 39),
    _FwSS_http_blocked_cnt_Type()
)
fwSS_http_blocked_cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_blocked_cnt.setStatus("current")
_FwSS_http_blocked_total_Type = Integer32
_FwSS_http_blocked_total_Object = MibScalar
fwSS_http_blocked_total = _FwSS_http_blocked_total_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 40),
    _FwSS_http_blocked_total_Type()
)
fwSS_http_blocked_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_blocked_total.setStatus("current")
_FwSS_http_scanned_total_Type = Integer32
_FwSS_http_scanned_total_Object = MibScalar
fwSS_http_scanned_total = _FwSS_http_scanned_total_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 41),
    _FwSS_http_scanned_total_Type()
)
fwSS_http_scanned_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_scanned_total.setStatus("current")
_FwSS_http_blocked_by_file_type_Type = Integer32
_FwSS_http_blocked_by_file_type_Object = MibScalar
fwSS_http_blocked_by_file_type = _FwSS_http_blocked_by_file_type_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 42),
    _FwSS_http_blocked_by_file_type_Type()
)
fwSS_http_blocked_by_file_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_blocked_by_file_type.setStatus("current")
_FwSS_http_blocked_by_size_limit_Type = Integer32
_FwSS_http_blocked_by_size_limit_Object = MibScalar
fwSS_http_blocked_by_size_limit = _FwSS_http_blocked_by_size_limit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 43),
    _FwSS_http_blocked_by_size_limit_Type()
)
fwSS_http_blocked_by_size_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_blocked_by_size_limit.setStatus("current")
_FwSS_http_blocked_by_archive_limit_Type = Integer32
_FwSS_http_blocked_by_archive_limit_Object = MibScalar
fwSS_http_blocked_by_archive_limit = _FwSS_http_blocked_by_archive_limit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 44),
    _FwSS_http_blocked_by_archive_limit_Type()
)
fwSS_http_blocked_by_archive_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_blocked_by_archive_limit.setStatus("current")
_FwSS_http_blocked_by_internal_error_Type = Integer32
_FwSS_http_blocked_by_internal_error_Object = MibScalar
fwSS_http_blocked_by_internal_error = _FwSS_http_blocked_by_internal_error_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 45),
    _FwSS_http_blocked_by_internal_error_Type()
)
fwSS_http_blocked_by_internal_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_blocked_by_internal_error.setStatus("current")
_FwSS_http_passed_cnt_Type = Integer32
_FwSS_http_passed_cnt_Object = MibScalar
fwSS_http_passed_cnt = _FwSS_http_passed_cnt_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 46),
    _FwSS_http_passed_cnt_Type()
)
fwSS_http_passed_cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_passed_cnt.setStatus("current")
_FwSS_http_passed_by_file_type_Type = Integer32
_FwSS_http_passed_by_file_type_Object = MibScalar
fwSS_http_passed_by_file_type = _FwSS_http_passed_by_file_type_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 47),
    _FwSS_http_passed_by_file_type_Type()
)
fwSS_http_passed_by_file_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_passed_by_file_type.setStatus("current")
_FwSS_http_passed_by_size_limit_Type = Integer32
_FwSS_http_passed_by_size_limit_Object = MibScalar
fwSS_http_passed_by_size_limit = _FwSS_http_passed_by_size_limit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 48),
    _FwSS_http_passed_by_size_limit_Type()
)
fwSS_http_passed_by_size_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_passed_by_size_limit.setStatus("current")
_FwSS_http_passed_by_archive_limit_Type = Integer32
_FwSS_http_passed_by_archive_limit_Object = MibScalar
fwSS_http_passed_by_archive_limit = _FwSS_http_passed_by_archive_limit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 49),
    _FwSS_http_passed_by_archive_limit_Type()
)
fwSS_http_passed_by_archive_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_passed_by_archive_limit.setStatus("current")
_FwSS_http_passed_by_internal_error_Type = Integer32
_FwSS_http_passed_by_internal_error_Object = MibScalar
fwSS_http_passed_by_internal_error = _FwSS_http_passed_by_internal_error_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 50),
    _FwSS_http_passed_by_internal_error_Type()
)
fwSS_http_passed_by_internal_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_passed_by_internal_error.setStatus("current")
_FwSS_http_passed_total_Type = Integer32
_FwSS_http_passed_total_Object = MibScalar
fwSS_http_passed_total = _FwSS_http_passed_total_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 51),
    _FwSS_http_passed_total_Type()
)
fwSS_http_passed_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_passed_total.setStatus("current")
_FwSS_http_blocked_by_AV_settings_Type = Integer32
_FwSS_http_blocked_by_AV_settings_Object = MibScalar
fwSS_http_blocked_by_AV_settings = _FwSS_http_blocked_by_AV_settings_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 52),
    _FwSS_http_blocked_by_AV_settings_Type()
)
fwSS_http_blocked_by_AV_settings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_blocked_by_AV_settings.setStatus("current")
_FwSS_http_passed_by_AV_settings_Type = Integer32
_FwSS_http_passed_by_AV_settings_Object = MibScalar
fwSS_http_passed_by_AV_settings = _FwSS_http_passed_by_AV_settings_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 53),
    _FwSS_http_passed_by_AV_settings_Type()
)
fwSS_http_passed_by_AV_settings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_passed_by_AV_settings.setStatus("current")
_FwSS_http_blocked_by_URL_filter_category_Type = Integer32
_FwSS_http_blocked_by_URL_filter_category_Object = MibScalar
fwSS_http_blocked_by_URL_filter_category = _FwSS_http_blocked_by_URL_filter_category_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 54),
    _FwSS_http_blocked_by_URL_filter_category_Type()
)
fwSS_http_blocked_by_URL_filter_category.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_blocked_by_URL_filter_category.setStatus("current")
_FwSS_http_blocked_by_URL_block_list_Type = Integer32
_FwSS_http_blocked_by_URL_block_list_Object = MibScalar
fwSS_http_blocked_by_URL_block_list = _FwSS_http_blocked_by_URL_block_list_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 55),
    _FwSS_http_blocked_by_URL_block_list_Type()
)
fwSS_http_blocked_by_URL_block_list.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_blocked_by_URL_block_list.setStatus("current")
_FwSS_http_passed_by_URL_allow_list_Type = Integer32
_FwSS_http_passed_by_URL_allow_list_Object = MibScalar
fwSS_http_passed_by_URL_allow_list = _FwSS_http_passed_by_URL_allow_list_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 56),
    _FwSS_http_passed_by_URL_allow_list_Type()
)
fwSS_http_passed_by_URL_allow_list.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_passed_by_URL_allow_list.setStatus("current")
_FwSS_http_passed_by_URL_filter_category_Type = Integer32
_FwSS_http_passed_by_URL_filter_category_Object = MibScalar
fwSS_http_passed_by_URL_filter_category = _FwSS_http_passed_by_URL_filter_category_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 1, 57),
    _FwSS_http_passed_by_URL_filter_category_Type()
)
fwSS_http_passed_by_URL_filter_category.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_http_passed_by_URL_filter_category.setStatus("current")
_FwSS_ftp_ObjectIdentity = ObjectIdentity
fwSS_ftp = _FwSS_ftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2)
)
_FwSS_ftp_pid_Type = Integer32
_FwSS_ftp_pid_Object = MibScalar
fwSS_ftp_pid = _FwSS_ftp_pid_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 1),
    _FwSS_ftp_pid_Type()
)
fwSS_ftp_pid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_pid.setStatus("current")
_FwSS_ftp_proto_Type = Integer32
_FwSS_ftp_proto_Object = MibScalar
fwSS_ftp_proto = _FwSS_ftp_proto_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 2),
    _FwSS_ftp_proto_Type()
)
fwSS_ftp_proto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_proto.setStatus("current")
_FwSS_ftp_port_Type = Integer32
_FwSS_ftp_port_Object = MibScalar
fwSS_ftp_port = _FwSS_ftp_port_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 3),
    _FwSS_ftp_port_Type()
)
fwSS_ftp_port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_port.setStatus("current")
_FwSS_ftp_logical_port_Type = Integer32
_FwSS_ftp_logical_port_Object = MibScalar
fwSS_ftp_logical_port = _FwSS_ftp_logical_port_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 4),
    _FwSS_ftp_logical_port_Type()
)
fwSS_ftp_logical_port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_logical_port.setStatus("current")
_FwSS_ftp_max_avail_socket_Type = Integer32
_FwSS_ftp_max_avail_socket_Object = MibScalar
fwSS_ftp_max_avail_socket = _FwSS_ftp_max_avail_socket_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 5),
    _FwSS_ftp_max_avail_socket_Type()
)
fwSS_ftp_max_avail_socket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_max_avail_socket.setStatus("current")
_FwSS_ftp_socket_in_use_max_Type = Integer32
_FwSS_ftp_socket_in_use_max_Object = MibScalar
fwSS_ftp_socket_in_use_max = _FwSS_ftp_socket_in_use_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 6),
    _FwSS_ftp_socket_in_use_max_Type()
)
fwSS_ftp_socket_in_use_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_socket_in_use_max.setStatus("current")
_FwSS_ftp_socket_in_use_curr_Type = Integer32
_FwSS_ftp_socket_in_use_curr_Object = MibScalar
fwSS_ftp_socket_in_use_curr = _FwSS_ftp_socket_in_use_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 7),
    _FwSS_ftp_socket_in_use_curr_Type()
)
fwSS_ftp_socket_in_use_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_socket_in_use_curr.setStatus("current")
_FwSS_ftp_socket_in_use_count_Type = Integer32
_FwSS_ftp_socket_in_use_count_Object = MibScalar
fwSS_ftp_socket_in_use_count = _FwSS_ftp_socket_in_use_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 8),
    _FwSS_ftp_socket_in_use_count_Type()
)
fwSS_ftp_socket_in_use_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_socket_in_use_count.setStatus("current")
_FwSS_ftp_sess_max_Type = Integer32
_FwSS_ftp_sess_max_Object = MibScalar
fwSS_ftp_sess_max = _FwSS_ftp_sess_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 9),
    _FwSS_ftp_sess_max_Type()
)
fwSS_ftp_sess_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_sess_max.setStatus("current")
_FwSS_ftp_sess_curr_Type = Integer32
_FwSS_ftp_sess_curr_Object = MibScalar
fwSS_ftp_sess_curr = _FwSS_ftp_sess_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 10),
    _FwSS_ftp_sess_curr_Type()
)
fwSS_ftp_sess_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_sess_curr.setStatus("current")
_FwSS_ftp_sess_count_Type = Integer32
_FwSS_ftp_sess_count_Object = MibScalar
fwSS_ftp_sess_count = _FwSS_ftp_sess_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 11),
    _FwSS_ftp_sess_count_Type()
)
fwSS_ftp_sess_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_sess_count.setStatus("current")
_FwSS_ftp_auth_sess_max_Type = Integer32
_FwSS_ftp_auth_sess_max_Object = MibScalar
fwSS_ftp_auth_sess_max = _FwSS_ftp_auth_sess_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 12),
    _FwSS_ftp_auth_sess_max_Type()
)
fwSS_ftp_auth_sess_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_auth_sess_max.setStatus("current")
_FwSS_ftp_auth_sess_curr_Type = Integer32
_FwSS_ftp_auth_sess_curr_Object = MibScalar
fwSS_ftp_auth_sess_curr = _FwSS_ftp_auth_sess_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 13),
    _FwSS_ftp_auth_sess_curr_Type()
)
fwSS_ftp_auth_sess_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_auth_sess_curr.setStatus("current")
_FwSS_ftp_auth_sess_count_Type = Integer32
_FwSS_ftp_auth_sess_count_Object = MibScalar
fwSS_ftp_auth_sess_count = _FwSS_ftp_auth_sess_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 14),
    _FwSS_ftp_auth_sess_count_Type()
)
fwSS_ftp_auth_sess_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_auth_sess_count.setStatus("current")
_FwSS_ftp_accepted_sess_Type = Integer32
_FwSS_ftp_accepted_sess_Object = MibScalar
fwSS_ftp_accepted_sess = _FwSS_ftp_accepted_sess_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 15),
    _FwSS_ftp_accepted_sess_Type()
)
fwSS_ftp_accepted_sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_accepted_sess.setStatus("current")
_FwSS_ftp_rejected_sess_Type = Integer32
_FwSS_ftp_rejected_sess_Object = MibScalar
fwSS_ftp_rejected_sess = _FwSS_ftp_rejected_sess_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 16),
    _FwSS_ftp_rejected_sess_Type()
)
fwSS_ftp_rejected_sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_rejected_sess.setStatus("current")
_FwSS_ftp_auth_failures_Type = Integer32
_FwSS_ftp_auth_failures_Object = MibScalar
fwSS_ftp_auth_failures = _FwSS_ftp_auth_failures_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 17),
    _FwSS_ftp_auth_failures_Type()
)
fwSS_ftp_auth_failures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_auth_failures.setStatus("current")
_FwSS_ftp_ops_cvp_sess_max_Type = Integer32
_FwSS_ftp_ops_cvp_sess_max_Object = MibScalar
fwSS_ftp_ops_cvp_sess_max = _FwSS_ftp_ops_cvp_sess_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 18),
    _FwSS_ftp_ops_cvp_sess_max_Type()
)
fwSS_ftp_ops_cvp_sess_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_ops_cvp_sess_max.setStatus("current")
_FwSS_ftp_ops_cvp_sess_curr_Type = Integer32
_FwSS_ftp_ops_cvp_sess_curr_Object = MibScalar
fwSS_ftp_ops_cvp_sess_curr = _FwSS_ftp_ops_cvp_sess_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 19),
    _FwSS_ftp_ops_cvp_sess_curr_Type()
)
fwSS_ftp_ops_cvp_sess_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_ops_cvp_sess_curr.setStatus("current")
_FwSS_ftp_ops_cvp_sess_count_Type = Integer32
_FwSS_ftp_ops_cvp_sess_count_Object = MibScalar
fwSS_ftp_ops_cvp_sess_count = _FwSS_ftp_ops_cvp_sess_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 20),
    _FwSS_ftp_ops_cvp_sess_count_Type()
)
fwSS_ftp_ops_cvp_sess_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_ops_cvp_sess_count.setStatus("current")
_FwSS_ftp_ops_cvp_rej_sess_Type = Integer32
_FwSS_ftp_ops_cvp_rej_sess_Object = MibScalar
fwSS_ftp_ops_cvp_rej_sess = _FwSS_ftp_ops_cvp_rej_sess_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 21),
    _FwSS_ftp_ops_cvp_rej_sess_Type()
)
fwSS_ftp_ops_cvp_rej_sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_ops_cvp_rej_sess.setStatus("current")


class _FwSS_ftp_time_stamp_Type(DisplayString):
    """Custom type fwSS_ftp_time_stamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwSS_ftp_time_stamp_Type.__name__ = "DisplayString"
_FwSS_ftp_time_stamp_Object = MibScalar
fwSS_ftp_time_stamp = _FwSS_ftp_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 22),
    _FwSS_ftp_time_stamp_Type()
)
fwSS_ftp_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_time_stamp.setStatus("current")
_FwSS_ftp_is_alive_Type = Integer32
_FwSS_ftp_is_alive_Object = MibScalar
fwSS_ftp_is_alive = _FwSS_ftp_is_alive_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 23),
    _FwSS_ftp_is_alive_Type()
)
fwSS_ftp_is_alive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_is_alive.setStatus("current")
_FwSS_ftp_blocked_cnt_Type = Integer32
_FwSS_ftp_blocked_cnt_Object = MibScalar
fwSS_ftp_blocked_cnt = _FwSS_ftp_blocked_cnt_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 24),
    _FwSS_ftp_blocked_cnt_Type()
)
fwSS_ftp_blocked_cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_blocked_cnt.setStatus("current")
_FwSS_ftp_blocked_total_Type = Integer32
_FwSS_ftp_blocked_total_Object = MibScalar
fwSS_ftp_blocked_total = _FwSS_ftp_blocked_total_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 25),
    _FwSS_ftp_blocked_total_Type()
)
fwSS_ftp_blocked_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_blocked_total.setStatus("current")
_FwSS_ftp_scanned_total_Type = Integer32
_FwSS_ftp_scanned_total_Object = MibScalar
fwSS_ftp_scanned_total = _FwSS_ftp_scanned_total_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 26),
    _FwSS_ftp_scanned_total_Type()
)
fwSS_ftp_scanned_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_scanned_total.setStatus("current")
_FwSS_ftp_blocked_by_file_type_Type = Integer32
_FwSS_ftp_blocked_by_file_type_Object = MibScalar
fwSS_ftp_blocked_by_file_type = _FwSS_ftp_blocked_by_file_type_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 27),
    _FwSS_ftp_blocked_by_file_type_Type()
)
fwSS_ftp_blocked_by_file_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_blocked_by_file_type.setStatus("current")
_FwSS_ftp_blocked_by_size_limit_Type = Integer32
_FwSS_ftp_blocked_by_size_limit_Object = MibScalar
fwSS_ftp_blocked_by_size_limit = _FwSS_ftp_blocked_by_size_limit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 28),
    _FwSS_ftp_blocked_by_size_limit_Type()
)
fwSS_ftp_blocked_by_size_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_blocked_by_size_limit.setStatus("current")
_FwSS_ftp_blocked_by_archive_limit_Type = Integer32
_FwSS_ftp_blocked_by_archive_limit_Object = MibScalar
fwSS_ftp_blocked_by_archive_limit = _FwSS_ftp_blocked_by_archive_limit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 29),
    _FwSS_ftp_blocked_by_archive_limit_Type()
)
fwSS_ftp_blocked_by_archive_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_blocked_by_archive_limit.setStatus("current")
_FwSS_ftp_blocked_by_internal_error_Type = Integer32
_FwSS_ftp_blocked_by_internal_error_Object = MibScalar
fwSS_ftp_blocked_by_internal_error = _FwSS_ftp_blocked_by_internal_error_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 30),
    _FwSS_ftp_blocked_by_internal_error_Type()
)
fwSS_ftp_blocked_by_internal_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_blocked_by_internal_error.setStatus("current")
_FwSS_ftp_passed_cnt_Type = Integer32
_FwSS_ftp_passed_cnt_Object = MibScalar
fwSS_ftp_passed_cnt = _FwSS_ftp_passed_cnt_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 31),
    _FwSS_ftp_passed_cnt_Type()
)
fwSS_ftp_passed_cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_passed_cnt.setStatus("current")
_FwSS_ftp_passed_by_file_type_Type = Integer32
_FwSS_ftp_passed_by_file_type_Object = MibScalar
fwSS_ftp_passed_by_file_type = _FwSS_ftp_passed_by_file_type_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 32),
    _FwSS_ftp_passed_by_file_type_Type()
)
fwSS_ftp_passed_by_file_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_passed_by_file_type.setStatus("current")
_FwSS_ftp_passed_by_size_limit_Type = Integer32
_FwSS_ftp_passed_by_size_limit_Object = MibScalar
fwSS_ftp_passed_by_size_limit = _FwSS_ftp_passed_by_size_limit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 33),
    _FwSS_ftp_passed_by_size_limit_Type()
)
fwSS_ftp_passed_by_size_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_passed_by_size_limit.setStatus("current")
_FwSS_ftp_passed_by_archive_limit_Type = Integer32
_FwSS_ftp_passed_by_archive_limit_Object = MibScalar
fwSS_ftp_passed_by_archive_limit = _FwSS_ftp_passed_by_archive_limit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 34),
    _FwSS_ftp_passed_by_archive_limit_Type()
)
fwSS_ftp_passed_by_archive_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_passed_by_archive_limit.setStatus("current")
_FwSS_ftp_passed_by_internal_error_Type = Integer32
_FwSS_ftp_passed_by_internal_error_Object = MibScalar
fwSS_ftp_passed_by_internal_error = _FwSS_ftp_passed_by_internal_error_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 35),
    _FwSS_ftp_passed_by_internal_error_Type()
)
fwSS_ftp_passed_by_internal_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_passed_by_internal_error.setStatus("current")
_FwSS_ftp_passed_total_Type = Integer32
_FwSS_ftp_passed_total_Object = MibScalar
fwSS_ftp_passed_total = _FwSS_ftp_passed_total_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 36),
    _FwSS_ftp_passed_total_Type()
)
fwSS_ftp_passed_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_passed_total.setStatus("current")
_FwSS_ftp_blocked_by_AV_settings_Type = Integer32
_FwSS_ftp_blocked_by_AV_settings_Object = MibScalar
fwSS_ftp_blocked_by_AV_settings = _FwSS_ftp_blocked_by_AV_settings_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 37),
    _FwSS_ftp_blocked_by_AV_settings_Type()
)
fwSS_ftp_blocked_by_AV_settings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_blocked_by_AV_settings.setStatus("current")
_FwSS_ftp_passed_by_AV_settings_Type = Integer32
_FwSS_ftp_passed_by_AV_settings_Object = MibScalar
fwSS_ftp_passed_by_AV_settings = _FwSS_ftp_passed_by_AV_settings_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 2, 38),
    _FwSS_ftp_passed_by_AV_settings_Type()
)
fwSS_ftp_passed_by_AV_settings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ftp_passed_by_AV_settings.setStatus("current")
_FwSS_telnet_ObjectIdentity = ObjectIdentity
fwSS_telnet = _FwSS_telnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 3)
)
_FwSS_telnet_pid_Type = Integer32
_FwSS_telnet_pid_Object = MibScalar
fwSS_telnet_pid = _FwSS_telnet_pid_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 3, 1),
    _FwSS_telnet_pid_Type()
)
fwSS_telnet_pid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_telnet_pid.setStatus("current")
_FwSS_telnet_proto_Type = Integer32
_FwSS_telnet_proto_Object = MibScalar
fwSS_telnet_proto = _FwSS_telnet_proto_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 3, 2),
    _FwSS_telnet_proto_Type()
)
fwSS_telnet_proto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_telnet_proto.setStatus("current")
_FwSS_telnet_port_Type = Integer32
_FwSS_telnet_port_Object = MibScalar
fwSS_telnet_port = _FwSS_telnet_port_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 3, 3),
    _FwSS_telnet_port_Type()
)
fwSS_telnet_port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_telnet_port.setStatus("current")
_FwSS_telnet_logical_port_Type = Integer32
_FwSS_telnet_logical_port_Object = MibScalar
fwSS_telnet_logical_port = _FwSS_telnet_logical_port_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 3, 4),
    _FwSS_telnet_logical_port_Type()
)
fwSS_telnet_logical_port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_telnet_logical_port.setStatus("current")
_FwSS_telnet_max_avail_socket_Type = Integer32
_FwSS_telnet_max_avail_socket_Object = MibScalar
fwSS_telnet_max_avail_socket = _FwSS_telnet_max_avail_socket_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 3, 5),
    _FwSS_telnet_max_avail_socket_Type()
)
fwSS_telnet_max_avail_socket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_telnet_max_avail_socket.setStatus("current")
_FwSS_telnet_socket_in_use_max_Type = Integer32
_FwSS_telnet_socket_in_use_max_Object = MibScalar
fwSS_telnet_socket_in_use_max = _FwSS_telnet_socket_in_use_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 3, 6),
    _FwSS_telnet_socket_in_use_max_Type()
)
fwSS_telnet_socket_in_use_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_telnet_socket_in_use_max.setStatus("current")
_FwSS_telnet_socket_in_use_curr_Type = Integer32
_FwSS_telnet_socket_in_use_curr_Object = MibScalar
fwSS_telnet_socket_in_use_curr = _FwSS_telnet_socket_in_use_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 3, 7),
    _FwSS_telnet_socket_in_use_curr_Type()
)
fwSS_telnet_socket_in_use_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_telnet_socket_in_use_curr.setStatus("current")
_FwSS_telnet_socket_in_use_count_Type = Integer32
_FwSS_telnet_socket_in_use_count_Object = MibScalar
fwSS_telnet_socket_in_use_count = _FwSS_telnet_socket_in_use_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 3, 8),
    _FwSS_telnet_socket_in_use_count_Type()
)
fwSS_telnet_socket_in_use_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_telnet_socket_in_use_count.setStatus("current")
_FwSS_telnet_sess_max_Type = Integer32
_FwSS_telnet_sess_max_Object = MibScalar
fwSS_telnet_sess_max = _FwSS_telnet_sess_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 3, 9),
    _FwSS_telnet_sess_max_Type()
)
fwSS_telnet_sess_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_telnet_sess_max.setStatus("current")
_FwSS_telnet_sess_curr_Type = Integer32
_FwSS_telnet_sess_curr_Object = MibScalar
fwSS_telnet_sess_curr = _FwSS_telnet_sess_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 3, 10),
    _FwSS_telnet_sess_curr_Type()
)
fwSS_telnet_sess_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_telnet_sess_curr.setStatus("current")
_FwSS_telnet_sess_count_Type = Integer32
_FwSS_telnet_sess_count_Object = MibScalar
fwSS_telnet_sess_count = _FwSS_telnet_sess_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 3, 11),
    _FwSS_telnet_sess_count_Type()
)
fwSS_telnet_sess_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_telnet_sess_count.setStatus("current")
_FwSS_telnet_auth_sess_max_Type = Integer32
_FwSS_telnet_auth_sess_max_Object = MibScalar
fwSS_telnet_auth_sess_max = _FwSS_telnet_auth_sess_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 3, 12),
    _FwSS_telnet_auth_sess_max_Type()
)
fwSS_telnet_auth_sess_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_telnet_auth_sess_max.setStatus("current")
_FwSS_telnet_auth_sess_curr_Type = Integer32
_FwSS_telnet_auth_sess_curr_Object = MibScalar
fwSS_telnet_auth_sess_curr = _FwSS_telnet_auth_sess_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 3, 13),
    _FwSS_telnet_auth_sess_curr_Type()
)
fwSS_telnet_auth_sess_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_telnet_auth_sess_curr.setStatus("current")
_FwSS_telnet_auth_sess_count_Type = Integer32
_FwSS_telnet_auth_sess_count_Object = MibScalar
fwSS_telnet_auth_sess_count = _FwSS_telnet_auth_sess_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 3, 14),
    _FwSS_telnet_auth_sess_count_Type()
)
fwSS_telnet_auth_sess_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_telnet_auth_sess_count.setStatus("current")
_FwSS_telnet_accepted_sess_Type = Integer32
_FwSS_telnet_accepted_sess_Object = MibScalar
fwSS_telnet_accepted_sess = _FwSS_telnet_accepted_sess_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 3, 15),
    _FwSS_telnet_accepted_sess_Type()
)
fwSS_telnet_accepted_sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_telnet_accepted_sess.setStatus("current")
_FwSS_telnet_rejected_sess_Type = Integer32
_FwSS_telnet_rejected_sess_Object = MibScalar
fwSS_telnet_rejected_sess = _FwSS_telnet_rejected_sess_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 3, 16),
    _FwSS_telnet_rejected_sess_Type()
)
fwSS_telnet_rejected_sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_telnet_rejected_sess.setStatus("current")
_FwSS_telnet_auth_failures_Type = Integer32
_FwSS_telnet_auth_failures_Object = MibScalar
fwSS_telnet_auth_failures = _FwSS_telnet_auth_failures_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 3, 17),
    _FwSS_telnet_auth_failures_Type()
)
fwSS_telnet_auth_failures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_telnet_auth_failures.setStatus("current")


class _FwSS_telnet_time_stamp_Type(DisplayString):
    """Custom type fwSS_telnet_time_stamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwSS_telnet_time_stamp_Type.__name__ = "DisplayString"
_FwSS_telnet_time_stamp_Object = MibScalar
fwSS_telnet_time_stamp = _FwSS_telnet_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 3, 18),
    _FwSS_telnet_time_stamp_Type()
)
fwSS_telnet_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_telnet_time_stamp.setStatus("current")
_FwSS_telnet_is_alive_Type = Integer32
_FwSS_telnet_is_alive_Object = MibScalar
fwSS_telnet_is_alive = _FwSS_telnet_is_alive_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 3, 19),
    _FwSS_telnet_is_alive_Type()
)
fwSS_telnet_is_alive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_telnet_is_alive.setStatus("current")
_FwSS_rlogin_ObjectIdentity = ObjectIdentity
fwSS_rlogin = _FwSS_rlogin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 4)
)
_FwSS_rlogin_pid_Type = Integer32
_FwSS_rlogin_pid_Object = MibScalar
fwSS_rlogin_pid = _FwSS_rlogin_pid_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 4, 1),
    _FwSS_rlogin_pid_Type()
)
fwSS_rlogin_pid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_rlogin_pid.setStatus("current")
_FwSS_rlogin_proto_Type = Integer32
_FwSS_rlogin_proto_Object = MibScalar
fwSS_rlogin_proto = _FwSS_rlogin_proto_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 4, 2),
    _FwSS_rlogin_proto_Type()
)
fwSS_rlogin_proto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_rlogin_proto.setStatus("current")
_FwSS_rlogin_port_Type = Integer32
_FwSS_rlogin_port_Object = MibScalar
fwSS_rlogin_port = _FwSS_rlogin_port_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 4, 3),
    _FwSS_rlogin_port_Type()
)
fwSS_rlogin_port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_rlogin_port.setStatus("current")
_FwSS_rlogin_logical_port_Type = Integer32
_FwSS_rlogin_logical_port_Object = MibScalar
fwSS_rlogin_logical_port = _FwSS_rlogin_logical_port_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 4, 4),
    _FwSS_rlogin_logical_port_Type()
)
fwSS_rlogin_logical_port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_rlogin_logical_port.setStatus("current")
_FwSS_rlogin_max_avail_socket_Type = Integer32
_FwSS_rlogin_max_avail_socket_Object = MibScalar
fwSS_rlogin_max_avail_socket = _FwSS_rlogin_max_avail_socket_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 4, 5),
    _FwSS_rlogin_max_avail_socket_Type()
)
fwSS_rlogin_max_avail_socket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_rlogin_max_avail_socket.setStatus("current")
_FwSS_rlogin_socket_in_use_max_Type = Integer32
_FwSS_rlogin_socket_in_use_max_Object = MibScalar
fwSS_rlogin_socket_in_use_max = _FwSS_rlogin_socket_in_use_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 4, 6),
    _FwSS_rlogin_socket_in_use_max_Type()
)
fwSS_rlogin_socket_in_use_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_rlogin_socket_in_use_max.setStatus("current")
_FwSS_rlogin_socket_in_use_curr_Type = Integer32
_FwSS_rlogin_socket_in_use_curr_Object = MibScalar
fwSS_rlogin_socket_in_use_curr = _FwSS_rlogin_socket_in_use_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 4, 7),
    _FwSS_rlogin_socket_in_use_curr_Type()
)
fwSS_rlogin_socket_in_use_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_rlogin_socket_in_use_curr.setStatus("current")
_FwSS_rlogin_socket_in_use_count_Type = Integer32
_FwSS_rlogin_socket_in_use_count_Object = MibScalar
fwSS_rlogin_socket_in_use_count = _FwSS_rlogin_socket_in_use_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 4, 8),
    _FwSS_rlogin_socket_in_use_count_Type()
)
fwSS_rlogin_socket_in_use_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_rlogin_socket_in_use_count.setStatus("current")
_FwSS_rlogin_sess_max_Type = Integer32
_FwSS_rlogin_sess_max_Object = MibScalar
fwSS_rlogin_sess_max = _FwSS_rlogin_sess_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 4, 9),
    _FwSS_rlogin_sess_max_Type()
)
fwSS_rlogin_sess_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_rlogin_sess_max.setStatus("current")
_FwSS_rlogin_sess_curr_Type = Integer32
_FwSS_rlogin_sess_curr_Object = MibScalar
fwSS_rlogin_sess_curr = _FwSS_rlogin_sess_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 4, 10),
    _FwSS_rlogin_sess_curr_Type()
)
fwSS_rlogin_sess_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_rlogin_sess_curr.setStatus("current")
_FwSS_rlogin_sess_count_Type = Integer32
_FwSS_rlogin_sess_count_Object = MibScalar
fwSS_rlogin_sess_count = _FwSS_rlogin_sess_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 4, 11),
    _FwSS_rlogin_sess_count_Type()
)
fwSS_rlogin_sess_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_rlogin_sess_count.setStatus("current")
_FwSS_rlogin_auth_sess_max_Type = Integer32
_FwSS_rlogin_auth_sess_max_Object = MibScalar
fwSS_rlogin_auth_sess_max = _FwSS_rlogin_auth_sess_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 4, 12),
    _FwSS_rlogin_auth_sess_max_Type()
)
fwSS_rlogin_auth_sess_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_rlogin_auth_sess_max.setStatus("current")
_FwSS_rlogin_auth_sess_curr_Type = Integer32
_FwSS_rlogin_auth_sess_curr_Object = MibScalar
fwSS_rlogin_auth_sess_curr = _FwSS_rlogin_auth_sess_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 4, 13),
    _FwSS_rlogin_auth_sess_curr_Type()
)
fwSS_rlogin_auth_sess_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_rlogin_auth_sess_curr.setStatus("current")
_FwSS_rlogin_auth_sess_count_Type = Integer32
_FwSS_rlogin_auth_sess_count_Object = MibScalar
fwSS_rlogin_auth_sess_count = _FwSS_rlogin_auth_sess_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 4, 14),
    _FwSS_rlogin_auth_sess_count_Type()
)
fwSS_rlogin_auth_sess_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_rlogin_auth_sess_count.setStatus("current")
_FwSS_rlogin_accepted_sess_Type = Integer32
_FwSS_rlogin_accepted_sess_Object = MibScalar
fwSS_rlogin_accepted_sess = _FwSS_rlogin_accepted_sess_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 4, 15),
    _FwSS_rlogin_accepted_sess_Type()
)
fwSS_rlogin_accepted_sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_rlogin_accepted_sess.setStatus("current")
_FwSS_rlogin_rejected_sess_Type = Integer32
_FwSS_rlogin_rejected_sess_Object = MibScalar
fwSS_rlogin_rejected_sess = _FwSS_rlogin_rejected_sess_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 4, 16),
    _FwSS_rlogin_rejected_sess_Type()
)
fwSS_rlogin_rejected_sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_rlogin_rejected_sess.setStatus("current")
_FwSS_rlogin_auth_failures_Type = Integer32
_FwSS_rlogin_auth_failures_Object = MibScalar
fwSS_rlogin_auth_failures = _FwSS_rlogin_auth_failures_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 4, 17),
    _FwSS_rlogin_auth_failures_Type()
)
fwSS_rlogin_auth_failures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_rlogin_auth_failures.setStatus("current")


class _FwSS_rlogin_time_stamp_Type(DisplayString):
    """Custom type fwSS_rlogin_time_stamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwSS_rlogin_time_stamp_Type.__name__ = "DisplayString"
_FwSS_rlogin_time_stamp_Object = MibScalar
fwSS_rlogin_time_stamp = _FwSS_rlogin_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 4, 18),
    _FwSS_rlogin_time_stamp_Type()
)
fwSS_rlogin_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_rlogin_time_stamp.setStatus("current")
_FwSS_rlogin_is_alive_Type = Integer32
_FwSS_rlogin_is_alive_Object = MibScalar
fwSS_rlogin_is_alive = _FwSS_rlogin_is_alive_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 4, 19),
    _FwSS_rlogin_is_alive_Type()
)
fwSS_rlogin_is_alive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_rlogin_is_alive.setStatus("current")
_FwSS_ufp_ObjectIdentity = ObjectIdentity
fwSS_ufp = _FwSS_ufp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 5)
)
_FwSS_ufp_ops_ufp_sess_max_Type = Integer32
_FwSS_ufp_ops_ufp_sess_max_Object = MibScalar
fwSS_ufp_ops_ufp_sess_max = _FwSS_ufp_ops_ufp_sess_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 5, 1),
    _FwSS_ufp_ops_ufp_sess_max_Type()
)
fwSS_ufp_ops_ufp_sess_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ufp_ops_ufp_sess_max.setStatus("current")
_FwSS_ufp_ops_ufp_sess_curr_Type = Integer32
_FwSS_ufp_ops_ufp_sess_curr_Object = MibScalar
fwSS_ufp_ops_ufp_sess_curr = _FwSS_ufp_ops_ufp_sess_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 5, 2),
    _FwSS_ufp_ops_ufp_sess_curr_Type()
)
fwSS_ufp_ops_ufp_sess_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ufp_ops_ufp_sess_curr.setStatus("current")
_FwSS_ufp_ops_ufp_sess_count_Type = Integer32
_FwSS_ufp_ops_ufp_sess_count_Object = MibScalar
fwSS_ufp_ops_ufp_sess_count = _FwSS_ufp_ops_ufp_sess_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 5, 3),
    _FwSS_ufp_ops_ufp_sess_count_Type()
)
fwSS_ufp_ops_ufp_sess_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ufp_ops_ufp_sess_count.setStatus("current")
_FwSS_ufp_ops_ufp_rej_sess_Type = Integer32
_FwSS_ufp_ops_ufp_rej_sess_Object = MibScalar
fwSS_ufp_ops_ufp_rej_sess = _FwSS_ufp_ops_ufp_rej_sess_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 5, 4),
    _FwSS_ufp_ops_ufp_rej_sess_Type()
)
fwSS_ufp_ops_ufp_rej_sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ufp_ops_ufp_rej_sess.setStatus("current")


class _FwSS_ufp_time_stamp_Type(DisplayString):
    """Custom type fwSS_ufp_time_stamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwSS_ufp_time_stamp_Type.__name__ = "DisplayString"
_FwSS_ufp_time_stamp_Object = MibScalar
fwSS_ufp_time_stamp = _FwSS_ufp_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 5, 5),
    _FwSS_ufp_time_stamp_Type()
)
fwSS_ufp_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ufp_time_stamp.setStatus("current")
_FwSS_ufp_is_alive_Type = Integer32
_FwSS_ufp_is_alive_Object = MibScalar
fwSS_ufp_is_alive = _FwSS_ufp_is_alive_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 5, 6),
    _FwSS_ufp_is_alive_Type()
)
fwSS_ufp_is_alive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_ufp_is_alive.setStatus("current")
_FwSS_smtp_ObjectIdentity = ObjectIdentity
fwSS_smtp = _FwSS_smtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6)
)
_FwSS_smtp_pid_Type = Integer32
_FwSS_smtp_pid_Object = MibScalar
fwSS_smtp_pid = _FwSS_smtp_pid_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 1),
    _FwSS_smtp_pid_Type()
)
fwSS_smtp_pid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_pid.setStatus("current")
_FwSS_smtp_proto_Type = Integer32
_FwSS_smtp_proto_Object = MibScalar
fwSS_smtp_proto = _FwSS_smtp_proto_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 2),
    _FwSS_smtp_proto_Type()
)
fwSS_smtp_proto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_proto.setStatus("current")
_FwSS_smtp_port_Type = Integer32
_FwSS_smtp_port_Object = MibScalar
fwSS_smtp_port = _FwSS_smtp_port_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 3),
    _FwSS_smtp_port_Type()
)
fwSS_smtp_port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_port.setStatus("current")
_FwSS_smtp_logical_port_Type = Integer32
_FwSS_smtp_logical_port_Object = MibScalar
fwSS_smtp_logical_port = _FwSS_smtp_logical_port_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 4),
    _FwSS_smtp_logical_port_Type()
)
fwSS_smtp_logical_port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_logical_port.setStatus("current")
_FwSS_smtp_max_avail_socket_Type = Integer32
_FwSS_smtp_max_avail_socket_Object = MibScalar
fwSS_smtp_max_avail_socket = _FwSS_smtp_max_avail_socket_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 5),
    _FwSS_smtp_max_avail_socket_Type()
)
fwSS_smtp_max_avail_socket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_max_avail_socket.setStatus("current")
_FwSS_smtp_socket_in_use_max_Type = Integer32
_FwSS_smtp_socket_in_use_max_Object = MibScalar
fwSS_smtp_socket_in_use_max = _FwSS_smtp_socket_in_use_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 6),
    _FwSS_smtp_socket_in_use_max_Type()
)
fwSS_smtp_socket_in_use_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_socket_in_use_max.setStatus("current")
_FwSS_smtp_socket_in_use_curr_Type = Integer32
_FwSS_smtp_socket_in_use_curr_Object = MibScalar
fwSS_smtp_socket_in_use_curr = _FwSS_smtp_socket_in_use_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 7),
    _FwSS_smtp_socket_in_use_curr_Type()
)
fwSS_smtp_socket_in_use_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_socket_in_use_curr.setStatus("current")
_FwSS_smtp_socket_in_use_count_Type = Integer32
_FwSS_smtp_socket_in_use_count_Object = MibScalar
fwSS_smtp_socket_in_use_count = _FwSS_smtp_socket_in_use_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 8),
    _FwSS_smtp_socket_in_use_count_Type()
)
fwSS_smtp_socket_in_use_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_socket_in_use_count.setStatus("current")
_FwSS_smtp_sess_max_Type = Integer32
_FwSS_smtp_sess_max_Object = MibScalar
fwSS_smtp_sess_max = _FwSS_smtp_sess_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 9),
    _FwSS_smtp_sess_max_Type()
)
fwSS_smtp_sess_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_sess_max.setStatus("current")
_FwSS_smtp_sess_curr_Type = Integer32
_FwSS_smtp_sess_curr_Object = MibScalar
fwSS_smtp_sess_curr = _FwSS_smtp_sess_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 10),
    _FwSS_smtp_sess_curr_Type()
)
fwSS_smtp_sess_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_sess_curr.setStatus("current")
_FwSS_smtp_sess_count_Type = Integer32
_FwSS_smtp_sess_count_Object = MibScalar
fwSS_smtp_sess_count = _FwSS_smtp_sess_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 11),
    _FwSS_smtp_sess_count_Type()
)
fwSS_smtp_sess_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_sess_count.setStatus("current")
_FwSS_smtp_auth_sess_max_Type = Integer32
_FwSS_smtp_auth_sess_max_Object = MibScalar
fwSS_smtp_auth_sess_max = _FwSS_smtp_auth_sess_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 12),
    _FwSS_smtp_auth_sess_max_Type()
)
fwSS_smtp_auth_sess_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_auth_sess_max.setStatus("current")
_FwSS_smtp_auth_sess_curr_Type = Integer32
_FwSS_smtp_auth_sess_curr_Object = MibScalar
fwSS_smtp_auth_sess_curr = _FwSS_smtp_auth_sess_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 13),
    _FwSS_smtp_auth_sess_curr_Type()
)
fwSS_smtp_auth_sess_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_auth_sess_curr.setStatus("current")
_FwSS_smtp_auth_sess_count_Type = Integer32
_FwSS_smtp_auth_sess_count_Object = MibScalar
fwSS_smtp_auth_sess_count = _FwSS_smtp_auth_sess_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 14),
    _FwSS_smtp_auth_sess_count_Type()
)
fwSS_smtp_auth_sess_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_auth_sess_count.setStatus("current")
_FwSS_smtp_accepted_sess_Type = Integer32
_FwSS_smtp_accepted_sess_Object = MibScalar
fwSS_smtp_accepted_sess = _FwSS_smtp_accepted_sess_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 15),
    _FwSS_smtp_accepted_sess_Type()
)
fwSS_smtp_accepted_sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_accepted_sess.setStatus("current")
_FwSS_smtp_rejected_sess_Type = Integer32
_FwSS_smtp_rejected_sess_Object = MibScalar
fwSS_smtp_rejected_sess = _FwSS_smtp_rejected_sess_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 16),
    _FwSS_smtp_rejected_sess_Type()
)
fwSS_smtp_rejected_sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_rejected_sess.setStatus("current")
_FwSS_smtp_auth_failures_Type = Integer32
_FwSS_smtp_auth_failures_Object = MibScalar
fwSS_smtp_auth_failures = _FwSS_smtp_auth_failures_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 17),
    _FwSS_smtp_auth_failures_Type()
)
fwSS_smtp_auth_failures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_auth_failures.setStatus("current")
_FwSS_smtp_mail_max_Type = Integer32
_FwSS_smtp_mail_max_Object = MibScalar
fwSS_smtp_mail_max = _FwSS_smtp_mail_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 18),
    _FwSS_smtp_mail_max_Type()
)
fwSS_smtp_mail_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_mail_max.setStatus("current")
_FwSS_smtp_mail_curr_Type = Integer32
_FwSS_smtp_mail_curr_Object = MibScalar
fwSS_smtp_mail_curr = _FwSS_smtp_mail_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 19),
    _FwSS_smtp_mail_curr_Type()
)
fwSS_smtp_mail_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_mail_curr.setStatus("current")
_FwSS_smtp_mail_count_Type = Integer32
_FwSS_smtp_mail_count_Object = MibScalar
fwSS_smtp_mail_count = _FwSS_smtp_mail_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 20),
    _FwSS_smtp_mail_count_Type()
)
fwSS_smtp_mail_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_mail_count.setStatus("current")
_FwSS_smtp_outgoing_mail_max_Type = Integer32
_FwSS_smtp_outgoing_mail_max_Object = MibScalar
fwSS_smtp_outgoing_mail_max = _FwSS_smtp_outgoing_mail_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 21),
    _FwSS_smtp_outgoing_mail_max_Type()
)
fwSS_smtp_outgoing_mail_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_outgoing_mail_max.setStatus("current")
_FwSS_smtp_outgoing_mail_curr_Type = Integer32
_FwSS_smtp_outgoing_mail_curr_Object = MibScalar
fwSS_smtp_outgoing_mail_curr = _FwSS_smtp_outgoing_mail_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 22),
    _FwSS_smtp_outgoing_mail_curr_Type()
)
fwSS_smtp_outgoing_mail_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_outgoing_mail_curr.setStatus("current")
_FwSS_smtp_outgoing_mail_count_Type = Integer32
_FwSS_smtp_outgoing_mail_count_Object = MibScalar
fwSS_smtp_outgoing_mail_count = _FwSS_smtp_outgoing_mail_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 23),
    _FwSS_smtp_outgoing_mail_count_Type()
)
fwSS_smtp_outgoing_mail_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_outgoing_mail_count.setStatus("current")
_FwSS_smtp_max_mail_on_conn_Type = Integer32
_FwSS_smtp_max_mail_on_conn_Object = MibScalar
fwSS_smtp_max_mail_on_conn = _FwSS_smtp_max_mail_on_conn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 24),
    _FwSS_smtp_max_mail_on_conn_Type()
)
fwSS_smtp_max_mail_on_conn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_max_mail_on_conn.setStatus("current")
_FwSS_smtp_total_mails_Type = Integer32
_FwSS_smtp_total_mails_Object = MibScalar
fwSS_smtp_total_mails = _FwSS_smtp_total_mails_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 25),
    _FwSS_smtp_total_mails_Type()
)
fwSS_smtp_total_mails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_total_mails.setStatus("current")


class _FwSS_smtp_time_stamp_Type(DisplayString):
    """Custom type fwSS_smtp_time_stamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwSS_smtp_time_stamp_Type.__name__ = "DisplayString"
_FwSS_smtp_time_stamp_Object = MibScalar
fwSS_smtp_time_stamp = _FwSS_smtp_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 26),
    _FwSS_smtp_time_stamp_Type()
)
fwSS_smtp_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_time_stamp.setStatus("current")
_FwSS_smtp_is_alive_Type = Integer32
_FwSS_smtp_is_alive_Object = MibScalar
fwSS_smtp_is_alive = _FwSS_smtp_is_alive_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 27),
    _FwSS_smtp_is_alive_Type()
)
fwSS_smtp_is_alive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_is_alive.setStatus("current")
_FwSS_smtp_blocked_cnt_Type = Integer32
_FwSS_smtp_blocked_cnt_Object = MibScalar
fwSS_smtp_blocked_cnt = _FwSS_smtp_blocked_cnt_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 28),
    _FwSS_smtp_blocked_cnt_Type()
)
fwSS_smtp_blocked_cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_blocked_cnt.setStatus("current")
_FwSS_smtp_blocked_total_Type = Integer32
_FwSS_smtp_blocked_total_Object = MibScalar
fwSS_smtp_blocked_total = _FwSS_smtp_blocked_total_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 29),
    _FwSS_smtp_blocked_total_Type()
)
fwSS_smtp_blocked_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_blocked_total.setStatus("current")
_FwSS_smtp_scanned_total_Type = Integer32
_FwSS_smtp_scanned_total_Object = MibScalar
fwSS_smtp_scanned_total = _FwSS_smtp_scanned_total_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 30),
    _FwSS_smtp_scanned_total_Type()
)
fwSS_smtp_scanned_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_scanned_total.setStatus("current")
_FwSS_smtp_blocked_by_file_type_Type = Integer32
_FwSS_smtp_blocked_by_file_type_Object = MibScalar
fwSS_smtp_blocked_by_file_type = _FwSS_smtp_blocked_by_file_type_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 31),
    _FwSS_smtp_blocked_by_file_type_Type()
)
fwSS_smtp_blocked_by_file_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_blocked_by_file_type.setStatus("current")
_FwSS_smtp_blocked_by_size_limit_Type = Integer32
_FwSS_smtp_blocked_by_size_limit_Object = MibScalar
fwSS_smtp_blocked_by_size_limit = _FwSS_smtp_blocked_by_size_limit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 32),
    _FwSS_smtp_blocked_by_size_limit_Type()
)
fwSS_smtp_blocked_by_size_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_blocked_by_size_limit.setStatus("current")
_FwSS_smtp_blocked_by_archive_limit_Type = Integer32
_FwSS_smtp_blocked_by_archive_limit_Object = MibScalar
fwSS_smtp_blocked_by_archive_limit = _FwSS_smtp_blocked_by_archive_limit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 33),
    _FwSS_smtp_blocked_by_archive_limit_Type()
)
fwSS_smtp_blocked_by_archive_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_blocked_by_archive_limit.setStatus("current")
_FwSS_smtp_blocked_by_internal_error_Type = Integer32
_FwSS_smtp_blocked_by_internal_error_Object = MibScalar
fwSS_smtp_blocked_by_internal_error = _FwSS_smtp_blocked_by_internal_error_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 34),
    _FwSS_smtp_blocked_by_internal_error_Type()
)
fwSS_smtp_blocked_by_internal_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_blocked_by_internal_error.setStatus("current")
_FwSS_smtp_passed_cnt_Type = Integer32
_FwSS_smtp_passed_cnt_Object = MibScalar
fwSS_smtp_passed_cnt = _FwSS_smtp_passed_cnt_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 35),
    _FwSS_smtp_passed_cnt_Type()
)
fwSS_smtp_passed_cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_passed_cnt.setStatus("current")
_FwSS_smtp_passed_by_file_type_Type = Integer32
_FwSS_smtp_passed_by_file_type_Object = MibScalar
fwSS_smtp_passed_by_file_type = _FwSS_smtp_passed_by_file_type_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 36),
    _FwSS_smtp_passed_by_file_type_Type()
)
fwSS_smtp_passed_by_file_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_passed_by_file_type.setStatus("current")
_FwSS_smtp_passed_by_size_limit_Type = Integer32
_FwSS_smtp_passed_by_size_limit_Object = MibScalar
fwSS_smtp_passed_by_size_limit = _FwSS_smtp_passed_by_size_limit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 37),
    _FwSS_smtp_passed_by_size_limit_Type()
)
fwSS_smtp_passed_by_size_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_passed_by_size_limit.setStatus("current")
_FwSS_smtp_passed_by_archive_limit_Type = Integer32
_FwSS_smtp_passed_by_archive_limit_Object = MibScalar
fwSS_smtp_passed_by_archive_limit = _FwSS_smtp_passed_by_archive_limit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 38),
    _FwSS_smtp_passed_by_archive_limit_Type()
)
fwSS_smtp_passed_by_archive_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_passed_by_archive_limit.setStatus("current")
_FwSS_smtp_passed_by_internal_error_Type = Integer32
_FwSS_smtp_passed_by_internal_error_Object = MibScalar
fwSS_smtp_passed_by_internal_error = _FwSS_smtp_passed_by_internal_error_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 39),
    _FwSS_smtp_passed_by_internal_error_Type()
)
fwSS_smtp_passed_by_internal_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_passed_by_internal_error.setStatus("current")
_FwSS_smtp_passed_total_Type = Integer32
_FwSS_smtp_passed_total_Object = MibScalar
fwSS_smtp_passed_total = _FwSS_smtp_passed_total_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 40),
    _FwSS_smtp_passed_total_Type()
)
fwSS_smtp_passed_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_passed_total.setStatus("current")
_FwSS_smtp_blocked_by_AV_settings_Type = Integer32
_FwSS_smtp_blocked_by_AV_settings_Object = MibScalar
fwSS_smtp_blocked_by_AV_settings = _FwSS_smtp_blocked_by_AV_settings_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 41),
    _FwSS_smtp_blocked_by_AV_settings_Type()
)
fwSS_smtp_blocked_by_AV_settings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_blocked_by_AV_settings.setStatus("current")
_FwSS_smtp_passed_by_AV_settings_Type = Integer32
_FwSS_smtp_passed_by_AV_settings_Object = MibScalar
fwSS_smtp_passed_by_AV_settings = _FwSS_smtp_passed_by_AV_settings_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 6, 42),
    _FwSS_smtp_passed_by_AV_settings_Type()
)
fwSS_smtp_passed_by_AV_settings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_smtp_passed_by_AV_settings.setStatus("current")
_FwSS_POP3_ObjectIdentity = ObjectIdentity
fwSS_POP3 = _FwSS_POP3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7)
)
_FwSS_POP3_pid_Type = Integer32
_FwSS_POP3_pid_Object = MibScalar
fwSS_POP3_pid = _FwSS_POP3_pid_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 1),
    _FwSS_POP3_pid_Type()
)
fwSS_POP3_pid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_pid.setStatus("current")
_FwSS_POP3_proto_Type = Integer32
_FwSS_POP3_proto_Object = MibScalar
fwSS_POP3_proto = _FwSS_POP3_proto_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 2),
    _FwSS_POP3_proto_Type()
)
fwSS_POP3_proto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_proto.setStatus("current")
_FwSS_POP3_port_Type = Integer32
_FwSS_POP3_port_Object = MibScalar
fwSS_POP3_port = _FwSS_POP3_port_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 3),
    _FwSS_POP3_port_Type()
)
fwSS_POP3_port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_port.setStatus("current")
_FwSS_POP3_logical_port_Type = Integer32
_FwSS_POP3_logical_port_Object = MibScalar
fwSS_POP3_logical_port = _FwSS_POP3_logical_port_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 4),
    _FwSS_POP3_logical_port_Type()
)
fwSS_POP3_logical_port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_logical_port.setStatus("current")
_FwSS_POP3_max_avail_socket_Type = Integer32
_FwSS_POP3_max_avail_socket_Object = MibScalar
fwSS_POP3_max_avail_socket = _FwSS_POP3_max_avail_socket_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 5),
    _FwSS_POP3_max_avail_socket_Type()
)
fwSS_POP3_max_avail_socket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_max_avail_socket.setStatus("current")
_FwSS_POP3_socket_in_use_max_Type = Integer32
_FwSS_POP3_socket_in_use_max_Object = MibScalar
fwSS_POP3_socket_in_use_max = _FwSS_POP3_socket_in_use_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 6),
    _FwSS_POP3_socket_in_use_max_Type()
)
fwSS_POP3_socket_in_use_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_socket_in_use_max.setStatus("current")
_FwSS_POP3_socket_in_use_curr_Type = Integer32
_FwSS_POP3_socket_in_use_curr_Object = MibScalar
fwSS_POP3_socket_in_use_curr = _FwSS_POP3_socket_in_use_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 7),
    _FwSS_POP3_socket_in_use_curr_Type()
)
fwSS_POP3_socket_in_use_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_socket_in_use_curr.setStatus("current")
_FwSS_POP3_socket_in_use_count_Type = Integer32
_FwSS_POP3_socket_in_use_count_Object = MibScalar
fwSS_POP3_socket_in_use_count = _FwSS_POP3_socket_in_use_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 8),
    _FwSS_POP3_socket_in_use_count_Type()
)
fwSS_POP3_socket_in_use_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_socket_in_use_count.setStatus("current")
_FwSS_POP3_sess_max_Type = Integer32
_FwSS_POP3_sess_max_Object = MibScalar
fwSS_POP3_sess_max = _FwSS_POP3_sess_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 9),
    _FwSS_POP3_sess_max_Type()
)
fwSS_POP3_sess_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_sess_max.setStatus("current")
_FwSS_POP3_sess_curr_Type = Integer32
_FwSS_POP3_sess_curr_Object = MibScalar
fwSS_POP3_sess_curr = _FwSS_POP3_sess_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 10),
    _FwSS_POP3_sess_curr_Type()
)
fwSS_POP3_sess_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_sess_curr.setStatus("current")
_FwSS_POP3_sess_count_Type = Integer32
_FwSS_POP3_sess_count_Object = MibScalar
fwSS_POP3_sess_count = _FwSS_POP3_sess_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 11),
    _FwSS_POP3_sess_count_Type()
)
fwSS_POP3_sess_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_sess_count.setStatus("current")
_FwSS_POP3_auth_sess_max_Type = Integer32
_FwSS_POP3_auth_sess_max_Object = MibScalar
fwSS_POP3_auth_sess_max = _FwSS_POP3_auth_sess_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 12),
    _FwSS_POP3_auth_sess_max_Type()
)
fwSS_POP3_auth_sess_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_auth_sess_max.setStatus("current")
_FwSS_POP3_auth_sess_curr_Type = Integer32
_FwSS_POP3_auth_sess_curr_Object = MibScalar
fwSS_POP3_auth_sess_curr = _FwSS_POP3_auth_sess_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 13),
    _FwSS_POP3_auth_sess_curr_Type()
)
fwSS_POP3_auth_sess_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_auth_sess_curr.setStatus("current")
_FwSS_POP3_auth_sess_count_Type = Integer32
_FwSS_POP3_auth_sess_count_Object = MibScalar
fwSS_POP3_auth_sess_count = _FwSS_POP3_auth_sess_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 14),
    _FwSS_POP3_auth_sess_count_Type()
)
fwSS_POP3_auth_sess_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_auth_sess_count.setStatus("current")
_FwSS_POP3_accepted_sess_Type = Integer32
_FwSS_POP3_accepted_sess_Object = MibScalar
fwSS_POP3_accepted_sess = _FwSS_POP3_accepted_sess_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 15),
    _FwSS_POP3_accepted_sess_Type()
)
fwSS_POP3_accepted_sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_accepted_sess.setStatus("current")
_FwSS_POP3_rejected_sess_Type = Integer32
_FwSS_POP3_rejected_sess_Object = MibScalar
fwSS_POP3_rejected_sess = _FwSS_POP3_rejected_sess_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 16),
    _FwSS_POP3_rejected_sess_Type()
)
fwSS_POP3_rejected_sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_rejected_sess.setStatus("current")
_FwSS_POP3_auth_failures_Type = Integer32
_FwSS_POP3_auth_failures_Object = MibScalar
fwSS_POP3_auth_failures = _FwSS_POP3_auth_failures_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 17),
    _FwSS_POP3_auth_failures_Type()
)
fwSS_POP3_auth_failures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_auth_failures.setStatus("current")
_FwSS_POP3_mail_max_Type = Integer32
_FwSS_POP3_mail_max_Object = MibScalar
fwSS_POP3_mail_max = _FwSS_POP3_mail_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 18),
    _FwSS_POP3_mail_max_Type()
)
fwSS_POP3_mail_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_mail_max.setStatus("current")
_FwSS_POP3_mail_curr_Type = Integer32
_FwSS_POP3_mail_curr_Object = MibScalar
fwSS_POP3_mail_curr = _FwSS_POP3_mail_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 19),
    _FwSS_POP3_mail_curr_Type()
)
fwSS_POP3_mail_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_mail_curr.setStatus("current")
_FwSS_POP3_mail_count_Type = Integer32
_FwSS_POP3_mail_count_Object = MibScalar
fwSS_POP3_mail_count = _FwSS_POP3_mail_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 20),
    _FwSS_POP3_mail_count_Type()
)
fwSS_POP3_mail_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_mail_count.setStatus("current")
_FwSS_POP3_outgoing_mail_max_Type = Integer32
_FwSS_POP3_outgoing_mail_max_Object = MibScalar
fwSS_POP3_outgoing_mail_max = _FwSS_POP3_outgoing_mail_max_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 21),
    _FwSS_POP3_outgoing_mail_max_Type()
)
fwSS_POP3_outgoing_mail_max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_outgoing_mail_max.setStatus("current")
_FwSS_POP3_outgoing_mail_curr_Type = Integer32
_FwSS_POP3_outgoing_mail_curr_Object = MibScalar
fwSS_POP3_outgoing_mail_curr = _FwSS_POP3_outgoing_mail_curr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 22),
    _FwSS_POP3_outgoing_mail_curr_Type()
)
fwSS_POP3_outgoing_mail_curr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_outgoing_mail_curr.setStatus("current")
_FwSS_POP3_outgoing_mail_count_Type = Integer32
_FwSS_POP3_outgoing_mail_count_Object = MibScalar
fwSS_POP3_outgoing_mail_count = _FwSS_POP3_outgoing_mail_count_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 23),
    _FwSS_POP3_outgoing_mail_count_Type()
)
fwSS_POP3_outgoing_mail_count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_outgoing_mail_count.setStatus("current")
_FwSS_POP3_max_mail_on_conn_Type = Integer32
_FwSS_POP3_max_mail_on_conn_Object = MibScalar
fwSS_POP3_max_mail_on_conn = _FwSS_POP3_max_mail_on_conn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 24),
    _FwSS_POP3_max_mail_on_conn_Type()
)
fwSS_POP3_max_mail_on_conn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_max_mail_on_conn.setStatus("current")
_FwSS_POP3_total_mails_Type = Integer32
_FwSS_POP3_total_mails_Object = MibScalar
fwSS_POP3_total_mails = _FwSS_POP3_total_mails_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 25),
    _FwSS_POP3_total_mails_Type()
)
fwSS_POP3_total_mails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_total_mails.setStatus("current")


class _FwSS_POP3_time_stamp_Type(DisplayString):
    """Custom type fwSS_POP3_time_stamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwSS_POP3_time_stamp_Type.__name__ = "DisplayString"
_FwSS_POP3_time_stamp_Object = MibScalar
fwSS_POP3_time_stamp = _FwSS_POP3_time_stamp_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 26),
    _FwSS_POP3_time_stamp_Type()
)
fwSS_POP3_time_stamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_time_stamp.setStatus("current")
_FwSS_POP3_is_alive_Type = Integer32
_FwSS_POP3_is_alive_Object = MibScalar
fwSS_POP3_is_alive = _FwSS_POP3_is_alive_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 27),
    _FwSS_POP3_is_alive_Type()
)
fwSS_POP3_is_alive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_is_alive.setStatus("current")
_FwSS_POP3_blocked_cnt_Type = Integer32
_FwSS_POP3_blocked_cnt_Object = MibScalar
fwSS_POP3_blocked_cnt = _FwSS_POP3_blocked_cnt_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 28),
    _FwSS_POP3_blocked_cnt_Type()
)
fwSS_POP3_blocked_cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_blocked_cnt.setStatus("current")
_FwSS_POP3_blocked_total_Type = Integer32
_FwSS_POP3_blocked_total_Object = MibScalar
fwSS_POP3_blocked_total = _FwSS_POP3_blocked_total_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 29),
    _FwSS_POP3_blocked_total_Type()
)
fwSS_POP3_blocked_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_blocked_total.setStatus("current")
_FwSS_POP3_scanned_total_Type = Integer32
_FwSS_POP3_scanned_total_Object = MibScalar
fwSS_POP3_scanned_total = _FwSS_POP3_scanned_total_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 30),
    _FwSS_POP3_scanned_total_Type()
)
fwSS_POP3_scanned_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_scanned_total.setStatus("current")
_FwSS_POP3_blocked_by_file_type_Type = Integer32
_FwSS_POP3_blocked_by_file_type_Object = MibScalar
fwSS_POP3_blocked_by_file_type = _FwSS_POP3_blocked_by_file_type_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 31),
    _FwSS_POP3_blocked_by_file_type_Type()
)
fwSS_POP3_blocked_by_file_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_blocked_by_file_type.setStatus("current")
_FwSS_POP3_blocked_by_size_limit_Type = Integer32
_FwSS_POP3_blocked_by_size_limit_Object = MibScalar
fwSS_POP3_blocked_by_size_limit = _FwSS_POP3_blocked_by_size_limit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 32),
    _FwSS_POP3_blocked_by_size_limit_Type()
)
fwSS_POP3_blocked_by_size_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_blocked_by_size_limit.setStatus("current")
_FwSS_POP3_blocked_by_archive_limit_Type = Integer32
_FwSS_POP3_blocked_by_archive_limit_Object = MibScalar
fwSS_POP3_blocked_by_archive_limit = _FwSS_POP3_blocked_by_archive_limit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 33),
    _FwSS_POP3_blocked_by_archive_limit_Type()
)
fwSS_POP3_blocked_by_archive_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_blocked_by_archive_limit.setStatus("current")
_FwSS_POP3_blocked_by_internal_error_Type = Integer32
_FwSS_POP3_blocked_by_internal_error_Object = MibScalar
fwSS_POP3_blocked_by_internal_error = _FwSS_POP3_blocked_by_internal_error_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 34),
    _FwSS_POP3_blocked_by_internal_error_Type()
)
fwSS_POP3_blocked_by_internal_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_blocked_by_internal_error.setStatus("current")
_FwSS_POP3_passed_cnt_Type = Integer32
_FwSS_POP3_passed_cnt_Object = MibScalar
fwSS_POP3_passed_cnt = _FwSS_POP3_passed_cnt_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 35),
    _FwSS_POP3_passed_cnt_Type()
)
fwSS_POP3_passed_cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_passed_cnt.setStatus("current")
_FwSS_POP3_passed_by_file_type_Type = Integer32
_FwSS_POP3_passed_by_file_type_Object = MibScalar
fwSS_POP3_passed_by_file_type = _FwSS_POP3_passed_by_file_type_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 36),
    _FwSS_POP3_passed_by_file_type_Type()
)
fwSS_POP3_passed_by_file_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_passed_by_file_type.setStatus("current")
_FwSS_POP3_passed_by_size_limit_Type = Integer32
_FwSS_POP3_passed_by_size_limit_Object = MibScalar
fwSS_POP3_passed_by_size_limit = _FwSS_POP3_passed_by_size_limit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 37),
    _FwSS_POP3_passed_by_size_limit_Type()
)
fwSS_POP3_passed_by_size_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_passed_by_size_limit.setStatus("current")
_FwSS_POP3_passed_by_archive_limit_Type = Integer32
_FwSS_POP3_passed_by_archive_limit_Object = MibScalar
fwSS_POP3_passed_by_archive_limit = _FwSS_POP3_passed_by_archive_limit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 38),
    _FwSS_POP3_passed_by_archive_limit_Type()
)
fwSS_POP3_passed_by_archive_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_passed_by_archive_limit.setStatus("current")
_FwSS_POP3_passed_by_internal_error_Type = Integer32
_FwSS_POP3_passed_by_internal_error_Object = MibScalar
fwSS_POP3_passed_by_internal_error = _FwSS_POP3_passed_by_internal_error_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 39),
    _FwSS_POP3_passed_by_internal_error_Type()
)
fwSS_POP3_passed_by_internal_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_passed_by_internal_error.setStatus("current")
_FwSS_POP3_passed_total_Type = Integer32
_FwSS_POP3_passed_total_Object = MibScalar
fwSS_POP3_passed_total = _FwSS_POP3_passed_total_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 40),
    _FwSS_POP3_passed_total_Type()
)
fwSS_POP3_passed_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_passed_total.setStatus("current")
_FwSS_POP3_blocked_by_AV_settings_Type = Integer32
_FwSS_POP3_blocked_by_AV_settings_Object = MibScalar
fwSS_POP3_blocked_by_AV_settings = _FwSS_POP3_blocked_by_AV_settings_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 41),
    _FwSS_POP3_blocked_by_AV_settings_Type()
)
fwSS_POP3_blocked_by_AV_settings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_blocked_by_AV_settings.setStatus("current")
_FwSS_POP3_passed_by_AV_settings_Type = Integer32
_FwSS_POP3_passed_by_AV_settings_Object = MibScalar
fwSS_POP3_passed_by_AV_settings = _FwSS_POP3_passed_by_AV_settings_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 7, 42),
    _FwSS_POP3_passed_by_AV_settings_Type()
)
fwSS_POP3_passed_by_AV_settings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_POP3_passed_by_AV_settings.setStatus("current")
_FwSS_av_total_ObjectIdentity = ObjectIdentity
fwSS_av_total = _FwSS_av_total_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 10)
)
_FwSS_total_blocked_by_av_Type = Integer32
_FwSS_total_blocked_by_av_Object = MibScalar
fwSS_total_blocked_by_av = _FwSS_total_blocked_by_av_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 10, 1),
    _FwSS_total_blocked_by_av_Type()
)
fwSS_total_blocked_by_av.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_total_blocked_by_av.setStatus("current")
_FwSS_total_blocked_Type = Integer32
_FwSS_total_blocked_Object = MibScalar
fwSS_total_blocked = _FwSS_total_blocked_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 10, 2),
    _FwSS_total_blocked_Type()
)
fwSS_total_blocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_total_blocked.setStatus("current")
_FwSS_total_scanned_Type = Integer32
_FwSS_total_scanned_Object = MibScalar
fwSS_total_scanned = _FwSS_total_scanned_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 10, 3),
    _FwSS_total_scanned_Type()
)
fwSS_total_scanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_total_scanned.setStatus("current")
_FwSS_total_blocked_by_file_type_Type = Integer32
_FwSS_total_blocked_by_file_type_Object = MibScalar
fwSS_total_blocked_by_file_type = _FwSS_total_blocked_by_file_type_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 10, 4),
    _FwSS_total_blocked_by_file_type_Type()
)
fwSS_total_blocked_by_file_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_total_blocked_by_file_type.setStatus("current")
_FwSS_total_blocked_by_size_limit_Type = Integer32
_FwSS_total_blocked_by_size_limit_Object = MibScalar
fwSS_total_blocked_by_size_limit = _FwSS_total_blocked_by_size_limit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 10, 5),
    _FwSS_total_blocked_by_size_limit_Type()
)
fwSS_total_blocked_by_size_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_total_blocked_by_size_limit.setStatus("current")
_FwSS_total_blocked_by_archive_limit_Type = Integer32
_FwSS_total_blocked_by_archive_limit_Object = MibScalar
fwSS_total_blocked_by_archive_limit = _FwSS_total_blocked_by_archive_limit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 10, 6),
    _FwSS_total_blocked_by_archive_limit_Type()
)
fwSS_total_blocked_by_archive_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_total_blocked_by_archive_limit.setStatus("current")
_FwSS_total_blocked_by_interal_error_Type = Integer32
_FwSS_total_blocked_by_interal_error_Object = MibScalar
fwSS_total_blocked_by_interal_error = _FwSS_total_blocked_by_interal_error_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 10, 7),
    _FwSS_total_blocked_by_interal_error_Type()
)
fwSS_total_blocked_by_interal_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_total_blocked_by_interal_error.setStatus("current")
_FwSS_total_passed_by_av_Type = Integer32
_FwSS_total_passed_by_av_Object = MibScalar
fwSS_total_passed_by_av = _FwSS_total_passed_by_av_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 10, 8),
    _FwSS_total_passed_by_av_Type()
)
fwSS_total_passed_by_av.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_total_passed_by_av.setStatus("current")
_FwSS_total_passed_by_file_type_Type = Integer32
_FwSS_total_passed_by_file_type_Object = MibScalar
fwSS_total_passed_by_file_type = _FwSS_total_passed_by_file_type_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 10, 9),
    _FwSS_total_passed_by_file_type_Type()
)
fwSS_total_passed_by_file_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_total_passed_by_file_type.setStatus("current")
_FwSS_total_passed_by_size_limit_Type = Integer32
_FwSS_total_passed_by_size_limit_Object = MibScalar
fwSS_total_passed_by_size_limit = _FwSS_total_passed_by_size_limit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 10, 10),
    _FwSS_total_passed_by_size_limit_Type()
)
fwSS_total_passed_by_size_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_total_passed_by_size_limit.setStatus("current")
_FwSS_total_passed_by_archive_limit_Type = Integer32
_FwSS_total_passed_by_archive_limit_Object = MibScalar
fwSS_total_passed_by_archive_limit = _FwSS_total_passed_by_archive_limit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 10, 11),
    _FwSS_total_passed_by_archive_limit_Type()
)
fwSS_total_passed_by_archive_limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_total_passed_by_archive_limit.setStatus("current")
_FwSS_total_passed_by_interal_error_Type = Integer32
_FwSS_total_passed_by_interal_error_Object = MibScalar
fwSS_total_passed_by_interal_error = _FwSS_total_passed_by_interal_error_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 10, 12),
    _FwSS_total_passed_by_interal_error_Type()
)
fwSS_total_passed_by_interal_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_total_passed_by_interal_error.setStatus("current")
_FwSS_total_passed_Type = Integer32
_FwSS_total_passed_Object = MibScalar
fwSS_total_passed = _FwSS_total_passed_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 10, 13),
    _FwSS_total_passed_Type()
)
fwSS_total_passed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_total_passed.setStatus("current")
_FwSS_total_blocked_by_av_settings_Type = Integer32
_FwSS_total_blocked_by_av_settings_Object = MibScalar
fwSS_total_blocked_by_av_settings = _FwSS_total_blocked_by_av_settings_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 10, 14),
    _FwSS_total_blocked_by_av_settings_Type()
)
fwSS_total_blocked_by_av_settings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_total_blocked_by_av_settings.setStatus("current")
_FwSS_total_passed_by_av_settings_Type = Integer32
_FwSS_total_passed_by_av_settings_Object = MibScalar
fwSS_total_passed_by_av_settings = _FwSS_total_passed_by_av_settings_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 9, 10, 15),
    _FwSS_total_passed_by_av_settings_Type()
)
fwSS_total_passed_by_av_settings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSS_total_passed_by_av_settings.setStatus("current")
_FwConnectionsStat_ObjectIdentity = ObjectIdentity
fwConnectionsStat = _FwConnectionsStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 11)
)
_FwConnectionsStatConnectionsTcp_Type = Integer32
_FwConnectionsStatConnectionsTcp_Object = MibScalar
fwConnectionsStatConnectionsTcp = _FwConnectionsStatConnectionsTcp_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 11, 1),
    _FwConnectionsStatConnectionsTcp_Type()
)
fwConnectionsStatConnectionsTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwConnectionsStatConnectionsTcp.setStatus("current")
_FwConnectionsStatConnectionsUdp_Type = Integer32
_FwConnectionsStatConnectionsUdp_Object = MibScalar
fwConnectionsStatConnectionsUdp = _FwConnectionsStatConnectionsUdp_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 11, 2),
    _FwConnectionsStatConnectionsUdp_Type()
)
fwConnectionsStatConnectionsUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwConnectionsStatConnectionsUdp.setStatus("current")
_FwConnectionsStatConnectionsIcmp_Type = Integer32
_FwConnectionsStatConnectionsIcmp_Object = MibScalar
fwConnectionsStatConnectionsIcmp = _FwConnectionsStatConnectionsIcmp_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 11, 3),
    _FwConnectionsStatConnectionsIcmp_Type()
)
fwConnectionsStatConnectionsIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwConnectionsStatConnectionsIcmp.setStatus("current")
_FwConnectionsStatConnectionsOther_Type = Integer32
_FwConnectionsStatConnectionsOther_Object = MibScalar
fwConnectionsStatConnectionsOther = _FwConnectionsStatConnectionsOther_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 11, 4),
    _FwConnectionsStatConnectionsOther_Type()
)
fwConnectionsStatConnectionsOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwConnectionsStatConnectionsOther.setStatus("current")
_FwConnectionsStatConnections_Type = Integer32
_FwConnectionsStatConnections_Object = MibScalar
fwConnectionsStatConnections = _FwConnectionsStatConnections_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 11, 5),
    _FwConnectionsStatConnections_Type()
)
fwConnectionsStatConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwConnectionsStatConnections.setStatus("current")
_FwConnectionsStatConnectionRate_Type = Integer32
_FwConnectionsStatConnectionRate_Object = MibScalar
fwConnectionsStatConnectionRate = _FwConnectionsStatConnectionRate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 11, 6),
    _FwConnectionsStatConnectionRate_Type()
)
fwConnectionsStatConnectionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwConnectionsStatConnectionRate.setStatus("current")
_FwHmem64_ObjectIdentity = ObjectIdentity
fwHmem64 = _FwHmem64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12)
)
_FwHmem64_block_size_Type = DisplayString
_FwHmem64_block_size_Object = MibScalar
fwHmem64_block_size = _FwHmem64_block_size_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12, 1),
    _FwHmem64_block_size_Type()
)
fwHmem64_block_size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem64_block_size.setStatus("current")
_FwHmem64_requested_bytes_Type = DisplayString
_FwHmem64_requested_bytes_Object = MibScalar
fwHmem64_requested_bytes = _FwHmem64_requested_bytes_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12, 2),
    _FwHmem64_requested_bytes_Type()
)
fwHmem64_requested_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem64_requested_bytes.setStatus("current")
_FwHmem64_initial_allocated_bytes_Type = DisplayString
_FwHmem64_initial_allocated_bytes_Object = MibScalar
fwHmem64_initial_allocated_bytes = _FwHmem64_initial_allocated_bytes_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12, 3),
    _FwHmem64_initial_allocated_bytes_Type()
)
fwHmem64_initial_allocated_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem64_initial_allocated_bytes.setStatus("current")
_FwHmem64_initial_allocated_blocks_Type = Integer32
_FwHmem64_initial_allocated_blocks_Object = MibScalar
fwHmem64_initial_allocated_blocks = _FwHmem64_initial_allocated_blocks_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12, 4),
    _FwHmem64_initial_allocated_blocks_Type()
)
fwHmem64_initial_allocated_blocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem64_initial_allocated_blocks.setStatus("current")
_FwHmem64_initial_allocated_pools_Type = Integer32
_FwHmem64_initial_allocated_pools_Object = MibScalar
fwHmem64_initial_allocated_pools = _FwHmem64_initial_allocated_pools_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12, 5),
    _FwHmem64_initial_allocated_pools_Type()
)
fwHmem64_initial_allocated_pools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem64_initial_allocated_pools.setStatus("current")
_FwHmem64_current_allocated_bytes_Type = DisplayString
_FwHmem64_current_allocated_bytes_Object = MibScalar
fwHmem64_current_allocated_bytes = _FwHmem64_current_allocated_bytes_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12, 6),
    _FwHmem64_current_allocated_bytes_Type()
)
fwHmem64_current_allocated_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem64_current_allocated_bytes.setStatus("current")
_FwHmem64_current_allocated_blocks_Type = Integer32
_FwHmem64_current_allocated_blocks_Object = MibScalar
fwHmem64_current_allocated_blocks = _FwHmem64_current_allocated_blocks_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12, 7),
    _FwHmem64_current_allocated_blocks_Type()
)
fwHmem64_current_allocated_blocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem64_current_allocated_blocks.setStatus("current")
_FwHmem64_current_allocated_pools_Type = Integer32
_FwHmem64_current_allocated_pools_Object = MibScalar
fwHmem64_current_allocated_pools = _FwHmem64_current_allocated_pools_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12, 8),
    _FwHmem64_current_allocated_pools_Type()
)
fwHmem64_current_allocated_pools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem64_current_allocated_pools.setStatus("current")
_FwHmem64_maximum_bytes_Type = DisplayString
_FwHmem64_maximum_bytes_Object = MibScalar
fwHmem64_maximum_bytes = _FwHmem64_maximum_bytes_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12, 9),
    _FwHmem64_maximum_bytes_Type()
)
fwHmem64_maximum_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem64_maximum_bytes.setStatus("current")
_FwHmem64_maximum_pools_Type = Integer32
_FwHmem64_maximum_pools_Object = MibScalar
fwHmem64_maximum_pools = _FwHmem64_maximum_pools_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12, 10),
    _FwHmem64_maximum_pools_Type()
)
fwHmem64_maximum_pools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem64_maximum_pools.setStatus("current")
_FwHmem64_bytes_used_Type = DisplayString
_FwHmem64_bytes_used_Object = MibScalar
fwHmem64_bytes_used = _FwHmem64_bytes_used_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12, 11),
    _FwHmem64_bytes_used_Type()
)
fwHmem64_bytes_used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem64_bytes_used.setStatus("current")
_FwHmem64_blocks_used_Type = Integer32
_FwHmem64_blocks_used_Object = MibScalar
fwHmem64_blocks_used = _FwHmem64_blocks_used_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12, 12),
    _FwHmem64_blocks_used_Type()
)
fwHmem64_blocks_used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem64_blocks_used.setStatus("current")
_FwHmem64_bytes_unused_Type = DisplayString
_FwHmem64_bytes_unused_Object = MibScalar
fwHmem64_bytes_unused = _FwHmem64_bytes_unused_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12, 13),
    _FwHmem64_bytes_unused_Type()
)
fwHmem64_bytes_unused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem64_bytes_unused.setStatus("current")
_FwHmem64_blocks_unused_Type = Integer32
_FwHmem64_blocks_unused_Object = MibScalar
fwHmem64_blocks_unused = _FwHmem64_blocks_unused_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12, 14),
    _FwHmem64_blocks_unused_Type()
)
fwHmem64_blocks_unused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem64_blocks_unused.setStatus("current")
_FwHmem64_bytes_peak_Type = DisplayString
_FwHmem64_bytes_peak_Object = MibScalar
fwHmem64_bytes_peak = _FwHmem64_bytes_peak_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12, 15),
    _FwHmem64_bytes_peak_Type()
)
fwHmem64_bytes_peak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem64_bytes_peak.setStatus("current")
_FwHmem64_blocks_peak_Type = Integer32
_FwHmem64_blocks_peak_Object = MibScalar
fwHmem64_blocks_peak = _FwHmem64_blocks_peak_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12, 16),
    _FwHmem64_blocks_peak_Type()
)
fwHmem64_blocks_peak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem64_blocks_peak.setStatus("current")
_FwHmem64_bytes_internal_use_Type = Integer32
_FwHmem64_bytes_internal_use_Object = MibScalar
fwHmem64_bytes_internal_use = _FwHmem64_bytes_internal_use_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12, 17),
    _FwHmem64_bytes_internal_use_Type()
)
fwHmem64_bytes_internal_use.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem64_bytes_internal_use.setStatus("current")
_FwHmem64_number_of_items_Type = DisplayString
_FwHmem64_number_of_items_Object = MibScalar
fwHmem64_number_of_items = _FwHmem64_number_of_items_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12, 18),
    _FwHmem64_number_of_items_Type()
)
fwHmem64_number_of_items.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem64_number_of_items.setStatus("current")
_FwHmem64_alloc_operations_Type = Integer32
_FwHmem64_alloc_operations_Object = MibScalar
fwHmem64_alloc_operations = _FwHmem64_alloc_operations_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12, 19),
    _FwHmem64_alloc_operations_Type()
)
fwHmem64_alloc_operations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem64_alloc_operations.setStatus("current")
_FwHmem64_free_operations_Type = Integer32
_FwHmem64_free_operations_Object = MibScalar
fwHmem64_free_operations = _FwHmem64_free_operations_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12, 20),
    _FwHmem64_free_operations_Type()
)
fwHmem64_free_operations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem64_free_operations.setStatus("current")
_FwHmem64_failed_alloc_Type = Integer32
_FwHmem64_failed_alloc_Object = MibScalar
fwHmem64_failed_alloc = _FwHmem64_failed_alloc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12, 21),
    _FwHmem64_failed_alloc_Type()
)
fwHmem64_failed_alloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem64_failed_alloc.setStatus("current")
_FwHmem64_failed_free_Type = Integer32
_FwHmem64_failed_free_Object = MibScalar
fwHmem64_failed_free = _FwHmem64_failed_free_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 26, 12, 22),
    _FwHmem64_failed_free_Type()
)
fwHmem64_failed_free.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwHmem64_failed_free.setStatus("current")
_FwNetIfTable_Object = MibTable
fwNetIfTable = _FwNetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 27)
)
if mibBuilder.loadTexts:
    fwNetIfTable.setStatus("current")
_FwNetIfEntry_Object = MibTableRow
fwNetIfEntry = _FwNetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 27, 1)
)
fwNetIfEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "fwNetIfIndex"),
)
if mibBuilder.loadTexts:
    fwNetIfEntry.setStatus("current")
_FwNetIfIndex_Type = Unsigned32
_FwNetIfIndex_Object = MibTableColumn
fwNetIfIndex = _FwNetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 27, 1, 1),
    _FwNetIfIndex_Type()
)
fwNetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwNetIfIndex.setStatus("current")
_FwNetIfName_Type = DisplayString
_FwNetIfName_Object = MibTableColumn
fwNetIfName = _FwNetIfName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 27, 1, 2),
    _FwNetIfName_Type()
)
fwNetIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwNetIfName.setStatus("current")
_FwNetIfIPAddr_Type = Integer32
_FwNetIfIPAddr_Object = MibTableColumn
fwNetIfIPAddr = _FwNetIfIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 27, 1, 3),
    _FwNetIfIPAddr_Type()
)
fwNetIfIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwNetIfIPAddr.setStatus("current")
_FwNetIfNetmask_Type = Integer32
_FwNetIfNetmask_Object = MibTableColumn
fwNetIfNetmask = _FwNetIfNetmask_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 27, 1, 4),
    _FwNetIfNetmask_Type()
)
fwNetIfNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwNetIfNetmask.setStatus("current")
_FwNetIfFlags_Type = Integer32
_FwNetIfFlags_Object = MibTableColumn
fwNetIfFlags = _FwNetIfFlags_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 27, 1, 5),
    _FwNetIfFlags_Type()
)
fwNetIfFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwNetIfFlags.setStatus("current")
_FwNetIfPeerName_Type = DisplayString
_FwNetIfPeerName_Object = MibTableColumn
fwNetIfPeerName = _FwNetIfPeerName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 27, 1, 6),
    _FwNetIfPeerName_Type()
)
fwNetIfPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwNetIfPeerName.setStatus("current")
_FwNetIfRemoteIp_Type = Integer32
_FwNetIfRemoteIp_Object = MibTableColumn
fwNetIfRemoteIp = _FwNetIfRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 27, 1, 7),
    _FwNetIfRemoteIp_Type()
)
fwNetIfRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwNetIfRemoteIp.setStatus("current")
_FwNetIfTopology_Type = Integer32
_FwNetIfTopology_Object = MibTableColumn
fwNetIfTopology = _FwNetIfTopology_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 27, 1, 8),
    _FwNetIfTopology_Type()
)
fwNetIfTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwNetIfTopology.setStatus("current")
_FwNetIfProxyName_Type = DisplayString
_FwNetIfProxyName_Object = MibTableColumn
fwNetIfProxyName = _FwNetIfProxyName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 27, 1, 9),
    _FwNetIfProxyName_Type()
)
fwNetIfProxyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwNetIfProxyName.setStatus("current")
_FwNetIfSlaves_Type = DisplayString
_FwNetIfSlaves_Object = MibTableColumn
fwNetIfSlaves = _FwNetIfSlaves_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 27, 1, 10),
    _FwNetIfSlaves_Type()
)
fwNetIfSlaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwNetIfSlaves.setStatus("current")
_FwNetIfPorts_Type = DisplayString
_FwNetIfPorts_Object = MibTableColumn
fwNetIfPorts = _FwNetIfPorts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 27, 1, 11),
    _FwNetIfPorts_Type()
)
fwNetIfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwNetIfPorts.setStatus("current")
_FwLSConn_ObjectIdentity = ObjectIdentity
fwLSConn = _FwLSConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 30)
)
_FwLSConnOverall_Type = Integer32
_FwLSConnOverall_Object = MibScalar
fwLSConnOverall = _FwLSConnOverall_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 30, 1),
    _FwLSConnOverall_Type()
)
fwLSConnOverall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwLSConnOverall.setStatus("current")
_FwLSConnOverallDesc_Type = DisplayString
_FwLSConnOverallDesc_Object = MibScalar
fwLSConnOverallDesc = _FwLSConnOverallDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 30, 2),
    _FwLSConnOverallDesc_Type()
)
fwLSConnOverallDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwLSConnOverallDesc.setStatus("current")
_FwLSConnTable_Object = MibTable
fwLSConnTable = _FwLSConnTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 30, 3)
)
if mibBuilder.loadTexts:
    fwLSConnTable.setStatus("current")
_FwLSConnEntry_Object = MibTableRow
fwLSConnEntry = _FwLSConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 30, 3, 1)
)
fwLSConnEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "fwLSConnIndex"),
)
if mibBuilder.loadTexts:
    fwLSConnEntry.setStatus("current")
_FwLSConnIndex_Type = Unsigned32
_FwLSConnIndex_Object = MibTableColumn
fwLSConnIndex = _FwLSConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 30, 3, 1, 1),
    _FwLSConnIndex_Type()
)
fwLSConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwLSConnIndex.setStatus("current")
_FwLSConnName_Type = DisplayString
_FwLSConnName_Object = MibTableColumn
fwLSConnName = _FwLSConnName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 30, 3, 1, 2),
    _FwLSConnName_Type()
)
fwLSConnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwLSConnName.setStatus("current")
_FwLSConnState_Type = Integer32
_FwLSConnState_Object = MibTableColumn
fwLSConnState = _FwLSConnState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 30, 3, 1, 3),
    _FwLSConnState_Type()
)
fwLSConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwLSConnState.setStatus("current")
_FwLSConnStateDesc_Type = DisplayString
_FwLSConnStateDesc_Object = MibTableColumn
fwLSConnStateDesc = _FwLSConnStateDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 30, 3, 1, 4),
    _FwLSConnStateDesc_Type()
)
fwLSConnStateDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwLSConnStateDesc.setStatus("current")
_FwLocalLoggingDesc_Type = DisplayString
_FwLocalLoggingDesc_Object = MibScalar
fwLocalLoggingDesc = _FwLocalLoggingDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 30, 4),
    _FwLocalLoggingDesc_Type()
)
fwLocalLoggingDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwLocalLoggingDesc.setStatus("current")
_FwLocalLoggingStat_Type = Integer32
_FwLocalLoggingStat_Object = MibScalar
fwLocalLoggingStat = _FwLocalLoggingStat_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 30, 5),
    _FwLocalLoggingStat_Type()
)
fwLocalLoggingStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwLocalLoggingStat.setStatus("current")
_Vpn_ObjectIdentity = ObjectIdentity
vpn = _Vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2)
)


class _CpvProdName_Type(DisplayString):
    """Custom type cpvProdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpvProdName_Type.__name__ = "DisplayString"
_CpvProdName_Object = MibScalar
cpvProdName = _CpvProdName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 1),
    _CpvProdName_Type()
)
cpvProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvProdName.setStatus("current")
_CpvVerMajor_Type = Integer32
_CpvVerMajor_Object = MibScalar
cpvVerMajor = _CpvVerMajor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 2),
    _CpvVerMajor_Type()
)
cpvVerMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvVerMajor.setStatus("current")
_CpvVerMinor_Type = Integer32
_CpvVerMinor_Object = MibScalar
cpvVerMinor = _CpvVerMinor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 3),
    _CpvVerMinor_Type()
)
cpvVerMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvVerMinor.setStatus("current")
_CpvGeneral_ObjectIdentity = ObjectIdentity
cpvGeneral = _CpvGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 4)
)
_CpvStatistics_ObjectIdentity = ObjectIdentity
cpvStatistics = _CpvStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 4, 1)
)
_CpvEncPackets_Type = DisplayString
_CpvEncPackets_Object = MibScalar
cpvEncPackets = _CpvEncPackets_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 4, 1, 1),
    _CpvEncPackets_Type()
)
cpvEncPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvEncPackets.setStatus("current")
_CpvDecPackets_Type = DisplayString
_CpvDecPackets_Object = MibScalar
cpvDecPackets = _CpvDecPackets_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 4, 1, 2),
    _CpvDecPackets_Type()
)
cpvDecPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvDecPackets.setStatus("current")
_CpvErrors_ObjectIdentity = ObjectIdentity
cpvErrors = _CpvErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 4, 2)
)
_CpvErrOut_Type = DisplayString
_CpvErrOut_Object = MibScalar
cpvErrOut = _CpvErrOut_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 4, 2, 1),
    _CpvErrOut_Type()
)
cpvErrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvErrOut.setStatus("current")
_CpvErrIn_Type = DisplayString
_CpvErrIn_Object = MibScalar
cpvErrIn = _CpvErrIn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 4, 2, 2),
    _CpvErrIn_Type()
)
cpvErrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvErrIn.setStatus("current")
_CpvErrIke_Type = DisplayString
_CpvErrIke_Object = MibScalar
cpvErrIke = _CpvErrIke_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 4, 2, 3),
    _CpvErrIke_Type()
)
cpvErrIke.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvErrIke.setStatus("current")
_CpvErrPolicy_Type = DisplayString
_CpvErrPolicy_Object = MibScalar
cpvErrPolicy = _CpvErrPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 4, 2, 4),
    _CpvErrPolicy_Type()
)
cpvErrPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvErrPolicy.setStatus("current")
_CpvIpsec_ObjectIdentity = ObjectIdentity
cpvIpsec = _CpvIpsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5)
)
_CpvSaStatistics_ObjectIdentity = ObjectIdentity
cpvSaStatistics = _CpvSaStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 2)
)
_CpvCurrEspSAsIn_Type = DisplayString
_CpvCurrEspSAsIn_Object = MibScalar
cpvCurrEspSAsIn = _CpvCurrEspSAsIn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 2, 1),
    _CpvCurrEspSAsIn_Type()
)
cpvCurrEspSAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvCurrEspSAsIn.setStatus("current")
_CpvTotalEspSAsIn_Type = DisplayString
_CpvTotalEspSAsIn_Object = MibScalar
cpvTotalEspSAsIn = _CpvTotalEspSAsIn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 2, 2),
    _CpvTotalEspSAsIn_Type()
)
cpvTotalEspSAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvTotalEspSAsIn.setStatus("current")
_CpvCurrEspSAsOut_Type = DisplayString
_CpvCurrEspSAsOut_Object = MibScalar
cpvCurrEspSAsOut = _CpvCurrEspSAsOut_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 2, 3),
    _CpvCurrEspSAsOut_Type()
)
cpvCurrEspSAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvCurrEspSAsOut.setStatus("current")
_CpvTotalEspSAsOut_Type = DisplayString
_CpvTotalEspSAsOut_Object = MibScalar
cpvTotalEspSAsOut = _CpvTotalEspSAsOut_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 2, 4),
    _CpvTotalEspSAsOut_Type()
)
cpvTotalEspSAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvTotalEspSAsOut.setStatus("current")
_CpvCurrAhSAsIn_Type = DisplayString
_CpvCurrAhSAsIn_Object = MibScalar
cpvCurrAhSAsIn = _CpvCurrAhSAsIn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 2, 5),
    _CpvCurrAhSAsIn_Type()
)
cpvCurrAhSAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvCurrAhSAsIn.setStatus("current")
_CpvTotalAhSAsIn_Type = DisplayString
_CpvTotalAhSAsIn_Object = MibScalar
cpvTotalAhSAsIn = _CpvTotalAhSAsIn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 2, 6),
    _CpvTotalAhSAsIn_Type()
)
cpvTotalAhSAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvTotalAhSAsIn.setStatus("current")
_CpvCurrAhSAsOut_Type = DisplayString
_CpvCurrAhSAsOut_Object = MibScalar
cpvCurrAhSAsOut = _CpvCurrAhSAsOut_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 2, 7),
    _CpvCurrAhSAsOut_Type()
)
cpvCurrAhSAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvCurrAhSAsOut.setStatus("current")
_CpvTotalAhSAsOut_Type = DisplayString
_CpvTotalAhSAsOut_Object = MibScalar
cpvTotalAhSAsOut = _CpvTotalAhSAsOut_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 2, 8),
    _CpvTotalAhSAsOut_Type()
)
cpvTotalAhSAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvTotalAhSAsOut.setStatus("current")
_CpvMaxConncurEspSAsIn_Type = DisplayString
_CpvMaxConncurEspSAsIn_Object = MibScalar
cpvMaxConncurEspSAsIn = _CpvMaxConncurEspSAsIn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 2, 9),
    _CpvMaxConncurEspSAsIn_Type()
)
cpvMaxConncurEspSAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvMaxConncurEspSAsIn.setStatus("current")
_CpvMaxConncurEspSAsOut_Type = DisplayString
_CpvMaxConncurEspSAsOut_Object = MibScalar
cpvMaxConncurEspSAsOut = _CpvMaxConncurEspSAsOut_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 2, 10),
    _CpvMaxConncurEspSAsOut_Type()
)
cpvMaxConncurEspSAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvMaxConncurEspSAsOut.setStatus("current")
_CpvMaxConncurAhSAsIn_Type = DisplayString
_CpvMaxConncurAhSAsIn_Object = MibScalar
cpvMaxConncurAhSAsIn = _CpvMaxConncurAhSAsIn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 2, 11),
    _CpvMaxConncurAhSAsIn_Type()
)
cpvMaxConncurAhSAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvMaxConncurAhSAsIn.setStatus("current")
_CpvMaxConncurAhSAsOut_Type = DisplayString
_CpvMaxConncurAhSAsOut_Object = MibScalar
cpvMaxConncurAhSAsOut = _CpvMaxConncurAhSAsOut_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 2, 12),
    _CpvMaxConncurAhSAsOut_Type()
)
cpvMaxConncurAhSAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvMaxConncurAhSAsOut.setStatus("current")
_CpvSaErrors_ObjectIdentity = ObjectIdentity
cpvSaErrors = _CpvSaErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 3)
)
_CpvSaDecrErr_Type = DisplayString
_CpvSaDecrErr_Object = MibScalar
cpvSaDecrErr = _CpvSaDecrErr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 3, 1),
    _CpvSaDecrErr_Type()
)
cpvSaDecrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvSaDecrErr.setStatus("current")
_CpvSaAuthErr_Type = DisplayString
_CpvSaAuthErr_Object = MibScalar
cpvSaAuthErr = _CpvSaAuthErr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 3, 2),
    _CpvSaAuthErr_Type()
)
cpvSaAuthErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvSaAuthErr.setStatus("current")
_CpvSaReplayErr_Type = DisplayString
_CpvSaReplayErr_Object = MibScalar
cpvSaReplayErr = _CpvSaReplayErr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 3, 3),
    _CpvSaReplayErr_Type()
)
cpvSaReplayErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvSaReplayErr.setStatus("current")
_CpvSaPolicyErr_Type = DisplayString
_CpvSaPolicyErr_Object = MibScalar
cpvSaPolicyErr = _CpvSaPolicyErr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 3, 4),
    _CpvSaPolicyErr_Type()
)
cpvSaPolicyErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvSaPolicyErr.setStatus("current")
_CpvSaOtherErrIn_Type = DisplayString
_CpvSaOtherErrIn_Object = MibScalar
cpvSaOtherErrIn = _CpvSaOtherErrIn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 3, 5),
    _CpvSaOtherErrIn_Type()
)
cpvSaOtherErrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvSaOtherErrIn.setStatus("current")
_CpvSaOtherErrOut_Type = DisplayString
_CpvSaOtherErrOut_Object = MibScalar
cpvSaOtherErrOut = _CpvSaOtherErrOut_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 3, 6),
    _CpvSaOtherErrOut_Type()
)
cpvSaOtherErrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvSaOtherErrOut.setStatus("current")
_CpvSaUnknownSpiErr_Type = DisplayString
_CpvSaUnknownSpiErr_Object = MibScalar
cpvSaUnknownSpiErr = _CpvSaUnknownSpiErr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 3, 7),
    _CpvSaUnknownSpiErr_Type()
)
cpvSaUnknownSpiErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvSaUnknownSpiErr.setStatus("current")
_CpvIpsecStatistics_ObjectIdentity = ObjectIdentity
cpvIpsecStatistics = _CpvIpsecStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 4)
)
_CpvIpsecUdpEspEncPkts_Type = DisplayString
_CpvIpsecUdpEspEncPkts_Object = MibScalar
cpvIpsecUdpEspEncPkts = _CpvIpsecUdpEspEncPkts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 4, 1),
    _CpvIpsecUdpEspEncPkts_Type()
)
cpvIpsecUdpEspEncPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIpsecUdpEspEncPkts.setStatus("current")
_CpvIpsecUdpEspDecPkts_Type = DisplayString
_CpvIpsecUdpEspDecPkts_Object = MibScalar
cpvIpsecUdpEspDecPkts = _CpvIpsecUdpEspDecPkts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 4, 2),
    _CpvIpsecUdpEspDecPkts_Type()
)
cpvIpsecUdpEspDecPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIpsecUdpEspDecPkts.setStatus("current")
_CpvIpsecAhEncPkts_Type = DisplayString
_CpvIpsecAhEncPkts_Object = MibScalar
cpvIpsecAhEncPkts = _CpvIpsecAhEncPkts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 4, 3),
    _CpvIpsecAhEncPkts_Type()
)
cpvIpsecAhEncPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIpsecAhEncPkts.setStatus("current")
_CpvIpsecAhDecPkts_Type = DisplayString
_CpvIpsecAhDecPkts_Object = MibScalar
cpvIpsecAhDecPkts = _CpvIpsecAhDecPkts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 4, 4),
    _CpvIpsecAhDecPkts_Type()
)
cpvIpsecAhDecPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIpsecAhDecPkts.setStatus("current")
_CpvIpsecEspEncPkts_Type = DisplayString
_CpvIpsecEspEncPkts_Object = MibScalar
cpvIpsecEspEncPkts = _CpvIpsecEspEncPkts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 4, 5),
    _CpvIpsecEspEncPkts_Type()
)
cpvIpsecEspEncPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIpsecEspEncPkts.setStatus("current")
_CpvIpsecEspDecPkts_Type = DisplayString
_CpvIpsecEspDecPkts_Object = MibScalar
cpvIpsecEspDecPkts = _CpvIpsecEspDecPkts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 4, 6),
    _CpvIpsecEspDecPkts_Type()
)
cpvIpsecEspDecPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIpsecEspDecPkts.setStatus("current")
_CpvIpsecDecomprBytesBefore_Type = DisplayString
_CpvIpsecDecomprBytesBefore_Object = MibScalar
cpvIpsecDecomprBytesBefore = _CpvIpsecDecomprBytesBefore_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 4, 7),
    _CpvIpsecDecomprBytesBefore_Type()
)
cpvIpsecDecomprBytesBefore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIpsecDecomprBytesBefore.setStatus("current")
_CpvIpsecDecomprBytesAfter_Type = DisplayString
_CpvIpsecDecomprBytesAfter_Object = MibScalar
cpvIpsecDecomprBytesAfter = _CpvIpsecDecomprBytesAfter_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 4, 8),
    _CpvIpsecDecomprBytesAfter_Type()
)
cpvIpsecDecomprBytesAfter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIpsecDecomprBytesAfter.setStatus("current")
_CpvIpsecDecomprOverhead_Type = DisplayString
_CpvIpsecDecomprOverhead_Object = MibScalar
cpvIpsecDecomprOverhead = _CpvIpsecDecomprOverhead_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 4, 9),
    _CpvIpsecDecomprOverhead_Type()
)
cpvIpsecDecomprOverhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIpsecDecomprOverhead.setStatus("current")
_CpvIpsecDecomprPkts_Type = DisplayString
_CpvIpsecDecomprPkts_Object = MibScalar
cpvIpsecDecomprPkts = _CpvIpsecDecomprPkts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 4, 10),
    _CpvIpsecDecomprPkts_Type()
)
cpvIpsecDecomprPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIpsecDecomprPkts.setStatus("current")
_CpvIpsecDecomprErr_Type = DisplayString
_CpvIpsecDecomprErr_Object = MibScalar
cpvIpsecDecomprErr = _CpvIpsecDecomprErr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 4, 11),
    _CpvIpsecDecomprErr_Type()
)
cpvIpsecDecomprErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIpsecDecomprErr.setStatus("current")
_CpvIpsecComprBytesBefore_Type = DisplayString
_CpvIpsecComprBytesBefore_Object = MibScalar
cpvIpsecComprBytesBefore = _CpvIpsecComprBytesBefore_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 4, 12),
    _CpvIpsecComprBytesBefore_Type()
)
cpvIpsecComprBytesBefore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIpsecComprBytesBefore.setStatus("current")
_CpvIpsecComprBytesAfter_Type = DisplayString
_CpvIpsecComprBytesAfter_Object = MibScalar
cpvIpsecComprBytesAfter = _CpvIpsecComprBytesAfter_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 4, 13),
    _CpvIpsecComprBytesAfter_Type()
)
cpvIpsecComprBytesAfter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIpsecComprBytesAfter.setStatus("current")
_CpvIpsecComprOverhead_Type = DisplayString
_CpvIpsecComprOverhead_Object = MibScalar
cpvIpsecComprOverhead = _CpvIpsecComprOverhead_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 4, 14),
    _CpvIpsecComprOverhead_Type()
)
cpvIpsecComprOverhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIpsecComprOverhead.setStatus("current")
_CpvIpsecNonCompressibleBytes_Type = DisplayString
_CpvIpsecNonCompressibleBytes_Object = MibScalar
cpvIpsecNonCompressibleBytes = _CpvIpsecNonCompressibleBytes_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 4, 15),
    _CpvIpsecNonCompressibleBytes_Type()
)
cpvIpsecNonCompressibleBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIpsecNonCompressibleBytes.setStatus("current")
_CpvIpsecCompressiblePkts_Type = DisplayString
_CpvIpsecCompressiblePkts_Object = MibScalar
cpvIpsecCompressiblePkts = _CpvIpsecCompressiblePkts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 4, 16),
    _CpvIpsecCompressiblePkts_Type()
)
cpvIpsecCompressiblePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIpsecCompressiblePkts.setStatus("current")
_CpvIpsecNonCompressiblePkts_Type = DisplayString
_CpvIpsecNonCompressiblePkts_Object = MibScalar
cpvIpsecNonCompressiblePkts = _CpvIpsecNonCompressiblePkts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 4, 17),
    _CpvIpsecNonCompressiblePkts_Type()
)
cpvIpsecNonCompressiblePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIpsecNonCompressiblePkts.setStatus("current")
_CpvIpsecComprErrors_Type = DisplayString
_CpvIpsecComprErrors_Object = MibScalar
cpvIpsecComprErrors = _CpvIpsecComprErrors_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 4, 18),
    _CpvIpsecComprErrors_Type()
)
cpvIpsecComprErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIpsecComprErrors.setStatus("current")
_CpvIpsecEspEncBytes_Type = DisplayString
_CpvIpsecEspEncBytes_Object = MibScalar
cpvIpsecEspEncBytes = _CpvIpsecEspEncBytes_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 4, 19),
    _CpvIpsecEspEncBytes_Type()
)
cpvIpsecEspEncBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIpsecEspEncBytes.setStatus("current")
_CpvIpsecEspDecBytes_Type = DisplayString
_CpvIpsecEspDecBytes_Object = MibScalar
cpvIpsecEspDecBytes = _CpvIpsecEspDecBytes_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 5, 4, 20),
    _CpvIpsecEspDecBytes_Type()
)
cpvIpsecEspDecBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIpsecEspDecBytes.setStatus("current")
_CpvFwz_ObjectIdentity = ObjectIdentity
cpvFwz = _CpvFwz_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 6)
)
_CpvFwzStatistics_ObjectIdentity = ObjectIdentity
cpvFwzStatistics = _CpvFwzStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 6, 1)
)
_CpvFwzEncapsEncPkts_Type = Integer32
_CpvFwzEncapsEncPkts_Object = MibScalar
cpvFwzEncapsEncPkts = _CpvFwzEncapsEncPkts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 6, 1, 1),
    _CpvFwzEncapsEncPkts_Type()
)
cpvFwzEncapsEncPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvFwzEncapsEncPkts.setStatus("current")
_CpvFwzEncapsDecPkts_Type = Integer32
_CpvFwzEncapsDecPkts_Object = MibScalar
cpvFwzEncapsDecPkts = _CpvFwzEncapsDecPkts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 6, 1, 2),
    _CpvFwzEncapsDecPkts_Type()
)
cpvFwzEncapsDecPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvFwzEncapsDecPkts.setStatus("current")
_CpvFwzEncPkts_Type = Integer32
_CpvFwzEncPkts_Object = MibScalar
cpvFwzEncPkts = _CpvFwzEncPkts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 6, 1, 3),
    _CpvFwzEncPkts_Type()
)
cpvFwzEncPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvFwzEncPkts.setStatus("current")
_CpvFwzDecPkts_Type = Integer32
_CpvFwzDecPkts_Object = MibScalar
cpvFwzDecPkts = _CpvFwzDecPkts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 6, 1, 4),
    _CpvFwzDecPkts_Type()
)
cpvFwzDecPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvFwzDecPkts.setStatus("current")
_CpvFwzErrors_ObjectIdentity = ObjectIdentity
cpvFwzErrors = _CpvFwzErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 6, 2)
)
_CpvFwzEncapsEncErrs_Type = Integer32
_CpvFwzEncapsEncErrs_Object = MibScalar
cpvFwzEncapsEncErrs = _CpvFwzEncapsEncErrs_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 6, 2, 1),
    _CpvFwzEncapsEncErrs_Type()
)
cpvFwzEncapsEncErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvFwzEncapsEncErrs.setStatus("current")
_CpvFwzEncapsDecErrs_Type = Integer32
_CpvFwzEncapsDecErrs_Object = MibScalar
cpvFwzEncapsDecErrs = _CpvFwzEncapsDecErrs_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 6, 2, 2),
    _CpvFwzEncapsDecErrs_Type()
)
cpvFwzEncapsDecErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvFwzEncapsDecErrs.setStatus("current")
_CpvFwzEncErrs_Type = Integer32
_CpvFwzEncErrs_Object = MibScalar
cpvFwzEncErrs = _CpvFwzEncErrs_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 6, 2, 3),
    _CpvFwzEncErrs_Type()
)
cpvFwzEncErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvFwzEncErrs.setStatus("current")
_CpvFwzDecErrs_Type = Integer32
_CpvFwzDecErrs_Object = MibScalar
cpvFwzDecErrs = _CpvFwzDecErrs_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 6, 2, 4),
    _CpvFwzDecErrs_Type()
)
cpvFwzDecErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvFwzDecErrs.setStatus("current")
_CpvAccelerator_ObjectIdentity = ObjectIdentity
cpvAccelerator = _CpvAccelerator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 8)
)
_CpvHwAccelGeneral_ObjectIdentity = ObjectIdentity
cpvHwAccelGeneral = _CpvHwAccelGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 8, 1)
)
_CpvHwAccelVendor_Type = DisplayString
_CpvHwAccelVendor_Object = MibScalar
cpvHwAccelVendor = _CpvHwAccelVendor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 8, 1, 1),
    _CpvHwAccelVendor_Type()
)
cpvHwAccelVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvHwAccelVendor.setStatus("current")
_CpvHwAccelStatus_Type = DisplayString
_CpvHwAccelStatus_Object = MibScalar
cpvHwAccelStatus = _CpvHwAccelStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 8, 1, 2),
    _CpvHwAccelStatus_Type()
)
cpvHwAccelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvHwAccelStatus.setStatus("current")
_CpvHwAccelDriverMajorVer_Type = Integer32
_CpvHwAccelDriverMajorVer_Object = MibScalar
cpvHwAccelDriverMajorVer = _CpvHwAccelDriverMajorVer_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 8, 1, 3),
    _CpvHwAccelDriverMajorVer_Type()
)
cpvHwAccelDriverMajorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvHwAccelDriverMajorVer.setStatus("current")
_CpvHwAccelDriverMinorVer_Type = Integer32
_CpvHwAccelDriverMinorVer_Object = MibScalar
cpvHwAccelDriverMinorVer = _CpvHwAccelDriverMinorVer_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 8, 1, 4),
    _CpvHwAccelDriverMinorVer_Type()
)
cpvHwAccelDriverMinorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvHwAccelDriverMinorVer.setStatus("current")
_CpvHwAccelStatistics_ObjectIdentity = ObjectIdentity
cpvHwAccelStatistics = _CpvHwAccelStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 8, 2)
)
_CpvHwAccelEspEncPkts_Type = DisplayString
_CpvHwAccelEspEncPkts_Object = MibScalar
cpvHwAccelEspEncPkts = _CpvHwAccelEspEncPkts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 8, 2, 1),
    _CpvHwAccelEspEncPkts_Type()
)
cpvHwAccelEspEncPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvHwAccelEspEncPkts.setStatus("current")
_CpvHwAccelEspDecPkts_Type = DisplayString
_CpvHwAccelEspDecPkts_Object = MibScalar
cpvHwAccelEspDecPkts = _CpvHwAccelEspDecPkts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 8, 2, 2),
    _CpvHwAccelEspDecPkts_Type()
)
cpvHwAccelEspDecPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvHwAccelEspDecPkts.setStatus("current")
_CpvHwAccelEspEncBytes_Type = DisplayString
_CpvHwAccelEspEncBytes_Object = MibScalar
cpvHwAccelEspEncBytes = _CpvHwAccelEspEncBytes_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 8, 2, 3),
    _CpvHwAccelEspEncBytes_Type()
)
cpvHwAccelEspEncBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvHwAccelEspEncBytes.setStatus("current")
_CpvHwAccelEspDecBytes_Type = DisplayString
_CpvHwAccelEspDecBytes_Object = MibScalar
cpvHwAccelEspDecBytes = _CpvHwAccelEspDecBytes_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 8, 2, 4),
    _CpvHwAccelEspDecBytes_Type()
)
cpvHwAccelEspDecBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvHwAccelEspDecBytes.setStatus("current")
_CpvHwAccelAhEncPkts_Type = DisplayString
_CpvHwAccelAhEncPkts_Object = MibScalar
cpvHwAccelAhEncPkts = _CpvHwAccelAhEncPkts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 8, 2, 5),
    _CpvHwAccelAhEncPkts_Type()
)
cpvHwAccelAhEncPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvHwAccelAhEncPkts.setStatus("current")
_CpvHwAccelAhDecPkts_Type = DisplayString
_CpvHwAccelAhDecPkts_Object = MibScalar
cpvHwAccelAhDecPkts = _CpvHwAccelAhDecPkts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 8, 2, 6),
    _CpvHwAccelAhDecPkts_Type()
)
cpvHwAccelAhDecPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvHwAccelAhDecPkts.setStatus("current")
_CpvHwAccelAhEncBytes_Type = DisplayString
_CpvHwAccelAhEncBytes_Object = MibScalar
cpvHwAccelAhEncBytes = _CpvHwAccelAhEncBytes_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 8, 2, 7),
    _CpvHwAccelAhEncBytes_Type()
)
cpvHwAccelAhEncBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvHwAccelAhEncBytes.setStatus("current")
_CpvHwAccelAhDecBytes_Type = DisplayString
_CpvHwAccelAhDecBytes_Object = MibScalar
cpvHwAccelAhDecBytes = _CpvHwAccelAhDecBytes_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 8, 2, 8),
    _CpvHwAccelAhDecBytes_Type()
)
cpvHwAccelAhDecBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvHwAccelAhDecBytes.setStatus("current")
_CpvIKE_ObjectIdentity = ObjectIdentity
cpvIKE = _CpvIKE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 9)
)
_CpvIKEglobals_ObjectIdentity = ObjectIdentity
cpvIKEglobals = _CpvIKEglobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 9, 1)
)
_CpvIKECurrSAs_Type = DisplayString
_CpvIKECurrSAs_Object = MibScalar
cpvIKECurrSAs = _CpvIKECurrSAs_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 9, 1, 1),
    _CpvIKECurrSAs_Type()
)
cpvIKECurrSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIKECurrSAs.setStatus("current")
_CpvIKECurrInitSAs_Type = DisplayString
_CpvIKECurrInitSAs_Object = MibScalar
cpvIKECurrInitSAs = _CpvIKECurrInitSAs_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 9, 1, 2),
    _CpvIKECurrInitSAs_Type()
)
cpvIKECurrInitSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIKECurrInitSAs.setStatus("current")
_CpvIKECurrRespSAs_Type = DisplayString
_CpvIKECurrRespSAs_Object = MibScalar
cpvIKECurrRespSAs = _CpvIKECurrRespSAs_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 9, 1, 3),
    _CpvIKECurrRespSAs_Type()
)
cpvIKECurrRespSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIKECurrRespSAs.setStatus("current")
_CpvIKETotalSAs_Type = DisplayString
_CpvIKETotalSAs_Object = MibScalar
cpvIKETotalSAs = _CpvIKETotalSAs_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 9, 1, 4),
    _CpvIKETotalSAs_Type()
)
cpvIKETotalSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIKETotalSAs.setStatus("current")
_CpvIKETotalInitSAs_Type = DisplayString
_CpvIKETotalInitSAs_Object = MibScalar
cpvIKETotalInitSAs = _CpvIKETotalInitSAs_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 9, 1, 5),
    _CpvIKETotalInitSAs_Type()
)
cpvIKETotalInitSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIKETotalInitSAs.setStatus("current")
_CpvIKETotalRespSAs_Type = DisplayString
_CpvIKETotalRespSAs_Object = MibScalar
cpvIKETotalRespSAs = _CpvIKETotalRespSAs_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 9, 1, 6),
    _CpvIKETotalRespSAs_Type()
)
cpvIKETotalRespSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIKETotalRespSAs.setStatus("current")
_CpvIKETotalSAsAttempts_Type = DisplayString
_CpvIKETotalSAsAttempts_Object = MibScalar
cpvIKETotalSAsAttempts = _CpvIKETotalSAsAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 9, 1, 7),
    _CpvIKETotalSAsAttempts_Type()
)
cpvIKETotalSAsAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIKETotalSAsAttempts.setStatus("current")
_CpvIKETotalSAsInitAttempts_Type = DisplayString
_CpvIKETotalSAsInitAttempts_Object = MibScalar
cpvIKETotalSAsInitAttempts = _CpvIKETotalSAsInitAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 9, 1, 8),
    _CpvIKETotalSAsInitAttempts_Type()
)
cpvIKETotalSAsInitAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIKETotalSAsInitAttempts.setStatus("current")
_CpvIKETotalSAsRespAttempts_Type = DisplayString
_CpvIKETotalSAsRespAttempts_Object = MibScalar
cpvIKETotalSAsRespAttempts = _CpvIKETotalSAsRespAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 9, 1, 9),
    _CpvIKETotalSAsRespAttempts_Type()
)
cpvIKETotalSAsRespAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIKETotalSAsRespAttempts.setStatus("current")
_CpvIKEMaxConncurSAs_Type = DisplayString
_CpvIKEMaxConncurSAs_Object = MibScalar
cpvIKEMaxConncurSAs = _CpvIKEMaxConncurSAs_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 9, 1, 10),
    _CpvIKEMaxConncurSAs_Type()
)
cpvIKEMaxConncurSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIKEMaxConncurSAs.setStatus("current")
_CpvIKEMaxConncurInitSAs_Type = DisplayString
_CpvIKEMaxConncurInitSAs_Object = MibScalar
cpvIKEMaxConncurInitSAs = _CpvIKEMaxConncurInitSAs_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 9, 1, 11),
    _CpvIKEMaxConncurInitSAs_Type()
)
cpvIKEMaxConncurInitSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIKEMaxConncurInitSAs.setStatus("current")
_CpvIKEMaxConncurRespSAs_Type = DisplayString
_CpvIKEMaxConncurRespSAs_Object = MibScalar
cpvIKEMaxConncurRespSAs = _CpvIKEMaxConncurRespSAs_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 9, 1, 12),
    _CpvIKEMaxConncurRespSAs_Type()
)
cpvIKEMaxConncurRespSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIKEMaxConncurRespSAs.setStatus("current")
_CpvIKEerrors_ObjectIdentity = ObjectIdentity
cpvIKEerrors = _CpvIKEerrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 9, 2)
)
_CpvIKETotalFailuresInit_Type = DisplayString
_CpvIKETotalFailuresInit_Object = MibScalar
cpvIKETotalFailuresInit = _CpvIKETotalFailuresInit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 9, 2, 1),
    _CpvIKETotalFailuresInit_Type()
)
cpvIKETotalFailuresInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIKETotalFailuresInit.setStatus("current")
_CpvIKENoResp_Type = DisplayString
_CpvIKENoResp_Object = MibScalar
cpvIKENoResp = _CpvIKENoResp_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 9, 2, 2),
    _CpvIKENoResp_Type()
)
cpvIKENoResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIKENoResp.setStatus("current")
_CpvIKETotalFailuresResp_Type = DisplayString
_CpvIKETotalFailuresResp_Object = MibScalar
cpvIKETotalFailuresResp = _CpvIKETotalFailuresResp_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 9, 2, 3),
    _CpvIKETotalFailuresResp_Type()
)
cpvIKETotalFailuresResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIKETotalFailuresResp.setStatus("current")
_CpvIPsec_ObjectIdentity = ObjectIdentity
cpvIPsec = _CpvIPsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 10)
)
_CpvIPsecNIC_ObjectIdentity = ObjectIdentity
cpvIPsecNIC = _CpvIPsecNIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 10, 1)
)
_CpvIPsecNICsNum_Type = Integer32
_CpvIPsecNICsNum_Object = MibScalar
cpvIPsecNICsNum = _CpvIPsecNICsNum_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 10, 1, 1),
    _CpvIPsecNICsNum_Type()
)
cpvIPsecNICsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIPsecNICsNum.setStatus("current")
_CpvIPsecNICTotalDownLoadedSAs_Type = DisplayString
_CpvIPsecNICTotalDownLoadedSAs_Object = MibScalar
cpvIPsecNICTotalDownLoadedSAs = _CpvIPsecNICTotalDownLoadedSAs_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 10, 1, 2),
    _CpvIPsecNICTotalDownLoadedSAs_Type()
)
cpvIPsecNICTotalDownLoadedSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIPsecNICTotalDownLoadedSAs.setStatus("current")
_CpvIPsecNICCurrDownLoadedSAs_Type = DisplayString
_CpvIPsecNICCurrDownLoadedSAs_Object = MibScalar
cpvIPsecNICCurrDownLoadedSAs = _CpvIPsecNICCurrDownLoadedSAs_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 10, 1, 3),
    _CpvIPsecNICCurrDownLoadedSAs_Type()
)
cpvIPsecNICCurrDownLoadedSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIPsecNICCurrDownLoadedSAs.setStatus("current")
_CpvIPsecNICDecrBytes_Type = DisplayString
_CpvIPsecNICDecrBytes_Object = MibScalar
cpvIPsecNICDecrBytes = _CpvIPsecNICDecrBytes_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 10, 1, 4),
    _CpvIPsecNICDecrBytes_Type()
)
cpvIPsecNICDecrBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIPsecNICDecrBytes.setStatus("current")
_CpvIPsecNICEncrBytes_Type = DisplayString
_CpvIPsecNICEncrBytes_Object = MibScalar
cpvIPsecNICEncrBytes = _CpvIPsecNICEncrBytes_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 10, 1, 5),
    _CpvIPsecNICEncrBytes_Type()
)
cpvIPsecNICEncrBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIPsecNICEncrBytes.setStatus("current")
_CpvIPsecNICDecrPackets_Type = DisplayString
_CpvIPsecNICDecrPackets_Object = MibScalar
cpvIPsecNICDecrPackets = _CpvIPsecNICDecrPackets_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 10, 1, 6),
    _CpvIPsecNICDecrPackets_Type()
)
cpvIPsecNICDecrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIPsecNICDecrPackets.setStatus("current")
_CpvIPsecNICEncrPackets_Type = DisplayString
_CpvIPsecNICEncrPackets_Object = MibScalar
cpvIPsecNICEncrPackets = _CpvIPsecNICEncrPackets_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2, 10, 1, 7),
    _CpvIPsecNICEncrPackets_Type()
)
cpvIPsecNICEncrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpvIPsecNICEncrPackets.setStatus("current")
_Fg_ObjectIdentity = ObjectIdentity
fg = _Fg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3)
)


class _FgProdName_Type(DisplayString):
    """Custom type fgProdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FgProdName_Type.__name__ = "DisplayString"
_FgProdName_Object = MibScalar
fgProdName = _FgProdName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 1),
    _FgProdName_Type()
)
fgProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProdName.setStatus("current")
_FgVerMajor_Type = Integer32
_FgVerMajor_Object = MibScalar
fgVerMajor = _FgVerMajor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 2),
    _FgVerMajor_Type()
)
fgVerMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVerMajor.setStatus("current")
_FgVerMinor_Type = Integer32
_FgVerMinor_Object = MibScalar
fgVerMinor = _FgVerMinor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 3),
    _FgVerMinor_Type()
)
fgVerMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVerMinor.setStatus("current")


class _FgVersionString_Type(DisplayString):
    """Custom type fgVersionString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FgVersionString_Type.__name__ = "DisplayString"
_FgVersionString_Object = MibScalar
fgVersionString = _FgVersionString_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 4),
    _FgVersionString_Type()
)
fgVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVersionString.setStatus("current")
_FgModuleKernelBuild_Type = Integer32
_FgModuleKernelBuild_Object = MibScalar
fgModuleKernelBuild = _FgModuleKernelBuild_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 5),
    _FgModuleKernelBuild_Type()
)
fgModuleKernelBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgModuleKernelBuild.setStatus("current")


class _FgStrPolicyName_Type(DisplayString):
    """Custom type fgStrPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FgStrPolicyName_Type.__name__ = "DisplayString"
_FgStrPolicyName_Object = MibScalar
fgStrPolicyName = _FgStrPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 6),
    _FgStrPolicyName_Type()
)
fgStrPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgStrPolicyName.setStatus("current")


class _FgInstallTime_Type(DisplayString):
    """Custom type fgInstallTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FgInstallTime_Type.__name__ = "DisplayString"
_FgInstallTime_Object = MibScalar
fgInstallTime = _FgInstallTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 7),
    _FgInstallTime_Type()
)
fgInstallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgInstallTime.setStatus("current")


class _FgNumInterfaces_Type(DisplayString):
    """Custom type fgNumInterfaces based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FgNumInterfaces_Type.__name__ = "DisplayString"
_FgNumInterfaces_Object = MibScalar
fgNumInterfaces = _FgNumInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 8),
    _FgNumInterfaces_Type()
)
fgNumInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgNumInterfaces.setStatus("current")
_FgIfTable_Object = MibTable
fgIfTable = _FgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 9)
)
if mibBuilder.loadTexts:
    fgIfTable.setStatus("current")
_FgIfEntry_Object = MibTableRow
fgIfEntry = _FgIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 9, 1)
)
fgIfEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "fgIfIndex"),
)
if mibBuilder.loadTexts:
    fgIfEntry.setStatus("current")
_FgIfIndex_Type = Unsigned32
_FgIfIndex_Object = MibTableColumn
fgIfIndex = _FgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 9, 1, 1),
    _FgIfIndex_Type()
)
fgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIfIndex.setStatus("current")
_FgIfName_Type = DisplayString
_FgIfName_Object = MibTableColumn
fgIfName = _FgIfName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 9, 1, 2),
    _FgIfName_Type()
)
fgIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIfName.setStatus("current")
_FgPolicyName_Type = DisplayString
_FgPolicyName_Object = MibTableColumn
fgPolicyName = _FgPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 9, 1, 3),
    _FgPolicyName_Type()
)
fgPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgPolicyName.setStatus("current")
_FgRateLimitIn_Type = Integer32
_FgRateLimitIn_Object = MibTableColumn
fgRateLimitIn = _FgRateLimitIn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 9, 1, 4),
    _FgRateLimitIn_Type()
)
fgRateLimitIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgRateLimitIn.setStatus("current")
_FgRateLimitOut_Type = Integer32
_FgRateLimitOut_Object = MibTableColumn
fgRateLimitOut = _FgRateLimitOut_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 9, 1, 5),
    _FgRateLimitOut_Type()
)
fgRateLimitOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgRateLimitOut.setStatus("current")
_FgAvrRateIn_Type = Integer32
_FgAvrRateIn_Object = MibTableColumn
fgAvrRateIn = _FgAvrRateIn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 9, 1, 6),
    _FgAvrRateIn_Type()
)
fgAvrRateIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvrRateIn.setStatus("current")
_FgAvrRateOut_Type = Integer32
_FgAvrRateOut_Object = MibTableColumn
fgAvrRateOut = _FgAvrRateOut_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 9, 1, 7),
    _FgAvrRateOut_Type()
)
fgAvrRateOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvrRateOut.setStatus("current")
_FgRetransPcktsIn_Type = Integer32
_FgRetransPcktsIn_Object = MibTableColumn
fgRetransPcktsIn = _FgRetransPcktsIn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 9, 1, 8),
    _FgRetransPcktsIn_Type()
)
fgRetransPcktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgRetransPcktsIn.setStatus("current")
_FgRetransPcktsOut_Type = Integer32
_FgRetransPcktsOut_Object = MibTableColumn
fgRetransPcktsOut = _FgRetransPcktsOut_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 9, 1, 9),
    _FgRetransPcktsOut_Type()
)
fgRetransPcktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgRetransPcktsOut.setStatus("current")
_FgPendPcktsIn_Type = Integer32
_FgPendPcktsIn_Object = MibTableColumn
fgPendPcktsIn = _FgPendPcktsIn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 9, 1, 10),
    _FgPendPcktsIn_Type()
)
fgPendPcktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgPendPcktsIn.setStatus("current")
_FgPendPcktsOut_Type = Integer32
_FgPendPcktsOut_Object = MibTableColumn
fgPendPcktsOut = _FgPendPcktsOut_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 9, 1, 11),
    _FgPendPcktsOut_Type()
)
fgPendPcktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgPendPcktsOut.setStatus("current")
_FgPendBytesIn_Type = Integer32
_FgPendBytesIn_Object = MibTableColumn
fgPendBytesIn = _FgPendBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 9, 1, 12),
    _FgPendBytesIn_Type()
)
fgPendBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgPendBytesIn.setStatus("current")
_FgPendBytesOut_Type = Integer32
_FgPendBytesOut_Object = MibTableColumn
fgPendBytesOut = _FgPendBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 9, 1, 13),
    _FgPendBytesOut_Type()
)
fgPendBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgPendBytesOut.setStatus("current")
_FgNumConnIn_Type = Integer32
_FgNumConnIn_Object = MibTableColumn
fgNumConnIn = _FgNumConnIn_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 9, 1, 14),
    _FgNumConnIn_Type()
)
fgNumConnIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgNumConnIn.setStatus("current")
_FgNumConnOut_Type = Integer32
_FgNumConnOut_Object = MibTableColumn
fgNumConnOut = _FgNumConnOut_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 3, 9, 1, 15),
    _FgNumConnOut_Type()
)
fgNumConnOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgNumConnOut.setStatus("current")
_Ha_ObjectIdentity = ObjectIdentity
ha = _Ha_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5)
)


class _HaProdName_Type(DisplayString):
    """Custom type haProdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HaProdName_Type.__name__ = "DisplayString"
_HaProdName_Object = MibScalar
haProdName = _HaProdName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 1),
    _HaProdName_Type()
)
haProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haProdName.setStatus("current")
_HaInstalled_Type = Integer32
_HaInstalled_Object = MibScalar
haInstalled = _HaInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 2),
    _HaInstalled_Type()
)
haInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haInstalled.setStatus("current")
_HaVerMajor_Type = Integer32
_HaVerMajor_Object = MibScalar
haVerMajor = _HaVerMajor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 3),
    _HaVerMajor_Type()
)
haVerMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haVerMajor.setStatus("current")
_HaVerMinor_Type = Integer32
_HaVerMinor_Object = MibScalar
haVerMinor = _HaVerMinor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 4),
    _HaVerMinor_Type()
)
haVerMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haVerMinor.setStatus("current")


class _HaStarted_Type(DisplayString):
    """Custom type haStarted based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HaStarted_Type.__name__ = "DisplayString"
_HaStarted_Object = MibScalar
haStarted = _HaStarted_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 5),
    _HaStarted_Type()
)
haStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haStarted.setStatus("current")


class _HaState_Type(DisplayString):
    """Custom type haState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HaState_Type.__name__ = "DisplayString"
_HaState_Object = MibScalar
haState = _HaState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 6),
    _HaState_Type()
)
haState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haState.setStatus("current")


class _HaBlockState_Type(DisplayString):
    """Custom type haBlockState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HaBlockState_Type.__name__ = "DisplayString"
_HaBlockState_Object = MibScalar
haBlockState = _HaBlockState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 7),
    _HaBlockState_Type()
)
haBlockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haBlockState.setStatus("current")
_HaIdentifier_Type = Integer32
_HaIdentifier_Object = MibScalar
haIdentifier = _HaIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 8),
    _HaIdentifier_Type()
)
haIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haIdentifier.setStatus("current")
_HaProtoVersion_Type = Integer32
_HaProtoVersion_Object = MibScalar
haProtoVersion = _HaProtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 10),
    _HaProtoVersion_Type()
)
haProtoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haProtoVersion.setStatus("current")


class _HaWorkMode_Type(DisplayString):
    """Custom type haWorkMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HaWorkMode_Type.__name__ = "DisplayString"
_HaWorkMode_Object = MibScalar
haWorkMode = _HaWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 11),
    _HaWorkMode_Type()
)
haWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haWorkMode.setStatus("current")
_HaIfTable_Object = MibTable
haIfTable = _HaIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 12)
)
if mibBuilder.loadTexts:
    haIfTable.setStatus("current")
_HaIfEntry_Object = MibTableRow
haIfEntry = _HaIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 12, 1)
)
haIfEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "haIfIndex"),
)
if mibBuilder.loadTexts:
    haIfEntry.setStatus("current")
_HaIfIndex_Type = Unsigned32
_HaIfIndex_Object = MibTableColumn
haIfIndex = _HaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 12, 1, 1),
    _HaIfIndex_Type()
)
haIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haIfIndex.setStatus("current")
_HaIfName_Type = DisplayString
_HaIfName_Object = MibTableColumn
haIfName = _HaIfName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 12, 1, 2),
    _HaIfName_Type()
)
haIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haIfName.setStatus("current")
_HaIP_Type = IpAddress
_HaIP_Object = MibTableColumn
haIP = _HaIP_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 12, 1, 3),
    _HaIP_Type()
)
haIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haIP.setStatus("current")
_HaStatus_Type = DisplayString
_HaStatus_Object = MibTableColumn
haStatus = _HaStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 12, 1, 4),
    _HaStatus_Type()
)
haStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haStatus.setStatus("current")
_HaVerified_Type = Integer32
_HaVerified_Object = MibTableColumn
haVerified = _HaVerified_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 12, 1, 5),
    _HaVerified_Type()
)
haVerified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haVerified.setStatus("current")
_HaTrusted_Type = Integer32
_HaTrusted_Object = MibTableColumn
haTrusted = _HaTrusted_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 12, 1, 6),
    _HaTrusted_Type()
)
haTrusted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haTrusted.setStatus("current")
_HaShared_Type = Integer32
_HaShared_Object = MibTableColumn
haShared = _HaShared_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 12, 1, 7),
    _HaShared_Type()
)
haShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haShared.setStatus("current")
_HaProblemTable_Object = MibTable
haProblemTable = _HaProblemTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 13)
)
if mibBuilder.loadTexts:
    haProblemTable.setStatus("current")
_HaProblemEntry_Object = MibTableRow
haProblemEntry = _HaProblemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 13, 1)
)
haProblemEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "haIfIndex"),
)
if mibBuilder.loadTexts:
    haProblemEntry.setStatus("current")
_HaProblemIndex_Type = Integer32
_HaProblemIndex_Object = MibTableColumn
haProblemIndex = _HaProblemIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 13, 1, 1),
    _HaProblemIndex_Type()
)
haProblemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haProblemIndex.setStatus("current")
_HaProblemName_Type = DisplayString
_HaProblemName_Object = MibTableColumn
haProblemName = _HaProblemName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 13, 1, 2),
    _HaProblemName_Type()
)
haProblemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haProblemName.setStatus("current")
_HaProblemStatus_Type = DisplayString
_HaProblemStatus_Object = MibTableColumn
haProblemStatus = _HaProblemStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 13, 1, 3),
    _HaProblemStatus_Type()
)
haProblemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haProblemStatus.setStatus("current")
_HaProblemPriority_Type = Integer32
_HaProblemPriority_Object = MibTableColumn
haProblemPriority = _HaProblemPriority_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 13, 1, 4),
    _HaProblemPriority_Type()
)
haProblemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haProblemPriority.setStatus("current")
_HaProblemVerified_Type = Integer32
_HaProblemVerified_Object = MibTableColumn
haProblemVerified = _HaProblemVerified_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 13, 1, 5),
    _HaProblemVerified_Type()
)
haProblemVerified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haProblemVerified.setStatus("current")
_HaProblemDescr_Type = DisplayString
_HaProblemDescr_Object = MibTableColumn
haProblemDescr = _HaProblemDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 13, 1, 6),
    _HaProblemDescr_Type()
)
haProblemDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haProblemDescr.setStatus("current")


class _HaVersionSting_Type(DisplayString):
    """Custom type haVersionSting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HaVersionSting_Type.__name__ = "DisplayString"
_HaVersionSting_Object = MibScalar
haVersionSting = _HaVersionSting_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 14),
    _HaVersionSting_Type()
)
haVersionSting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haVersionSting.setStatus("current")
_HaClusterIpTable_Object = MibTable
haClusterIpTable = _HaClusterIpTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 15)
)
if mibBuilder.loadTexts:
    haClusterIpTable.setStatus("current")
_HaClusterIpEntry_Object = MibTableRow
haClusterIpEntry = _HaClusterIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 15, 1)
)
haClusterIpEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "haClusterIpIndex"),
)
if mibBuilder.loadTexts:
    haClusterIpEntry.setStatus("current")
_HaClusterIpIndex_Type = Unsigned32
_HaClusterIpIndex_Object = MibTableColumn
haClusterIpIndex = _HaClusterIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 15, 1, 1),
    _HaClusterIpIndex_Type()
)
haClusterIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haClusterIpIndex.setStatus("current")
_HaClusterIpIfName_Type = DisplayString
_HaClusterIpIfName_Object = MibTableColumn
haClusterIpIfName = _HaClusterIpIfName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 15, 1, 2),
    _HaClusterIpIfName_Type()
)
haClusterIpIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haClusterIpIfName.setStatus("current")
_HaClusterIpAddr_Type = Integer32
_HaClusterIpAddr_Object = MibTableColumn
haClusterIpAddr = _HaClusterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 15, 1, 3),
    _HaClusterIpAddr_Type()
)
haClusterIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haClusterIpAddr.setStatus("current")
_HaClusterIpNetMask_Type = Integer32
_HaClusterIpNetMask_Object = MibTableColumn
haClusterIpNetMask = _HaClusterIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 15, 1, 4),
    _HaClusterIpNetMask_Type()
)
haClusterIpNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haClusterIpNetMask.setStatus("current")
_HaClusterIpMemberNet_Type = Integer32
_HaClusterIpMemberNet_Object = MibTableColumn
haClusterIpMemberNet = _HaClusterIpMemberNet_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 15, 1, 5),
    _HaClusterIpMemberNet_Type()
)
haClusterIpMemberNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haClusterIpMemberNet.setStatus("current")
_HaClusterIpMemberNetMask_Type = Integer32
_HaClusterIpMemberNetMask_Object = MibTableColumn
haClusterIpMemberNetMask = _HaClusterIpMemberNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 15, 1, 6),
    _HaClusterIpMemberNetMask_Type()
)
haClusterIpMemberNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haClusterIpMemberNetMask.setStatus("current")
_HaClusterSyncTable_Object = MibTable
haClusterSyncTable = _HaClusterSyncTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 16)
)
if mibBuilder.loadTexts:
    haClusterSyncTable.setStatus("current")
_HaClusterSyncEntry_Object = MibTableRow
haClusterSyncEntry = _HaClusterSyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 16, 1)
)
haClusterSyncEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "haClusterSyncIndex"),
)
if mibBuilder.loadTexts:
    haClusterSyncEntry.setStatus("current")
_HaClusterSyncIndex_Type = Unsigned32
_HaClusterSyncIndex_Object = MibTableColumn
haClusterSyncIndex = _HaClusterSyncIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 16, 1, 1),
    _HaClusterSyncIndex_Type()
)
haClusterSyncIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haClusterSyncIndex.setStatus("current")
_HaClusterSyncName_Type = DisplayString
_HaClusterSyncName_Object = MibTableColumn
haClusterSyncName = _HaClusterSyncName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 16, 1, 2),
    _HaClusterSyncName_Type()
)
haClusterSyncName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haClusterSyncName.setStatus("current")
_HaClusterSyncAddr_Type = Integer32
_HaClusterSyncAddr_Object = MibTableColumn
haClusterSyncAddr = _HaClusterSyncAddr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 16, 1, 3),
    _HaClusterSyncAddr_Type()
)
haClusterSyncAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haClusterSyncAddr.setStatus("current")
_HaClusterSyncNetMask_Type = Integer32
_HaClusterSyncNetMask_Object = MibTableColumn
haClusterSyncNetMask = _HaClusterSyncNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 16, 1, 4),
    _HaClusterSyncNetMask_Type()
)
haClusterSyncNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haClusterSyncNetMask.setStatus("current")
_HaStatCode_Type = Integer32
_HaStatCode_Object = MibScalar
haStatCode = _HaStatCode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 101),
    _HaStatCode_Type()
)
haStatCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haStatCode.setStatus("current")


class _HaStatShort_Type(DisplayString):
    """Custom type haStatShort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HaStatShort_Type.__name__ = "DisplayString"
_HaStatShort_Object = MibScalar
haStatShort = _HaStatShort_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 102),
    _HaStatShort_Type()
)
haStatShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haStatShort.setStatus("current")


class _HaStatLong_Type(DisplayString):
    """Custom type haStatLong based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HaStatLong_Type.__name__ = "DisplayString"
_HaStatLong_Object = MibScalar
haStatLong = _HaStatLong_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 103),
    _HaStatLong_Type()
)
haStatLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haStatLong.setStatus("current")
_HaServicePack_Type = Integer32
_HaServicePack_Object = MibScalar
haServicePack = _HaServicePack_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 5, 999),
    _HaServicePack_Type()
)
haServicePack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haServicePack.setStatus("current")
_Svn_ObjectIdentity = ObjectIdentity
svn = _Svn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6)
)


class _SvnProdName_Type(DisplayString):
    """Custom type svnProdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvnProdName_Type.__name__ = "DisplayString"
_SvnProdName_Object = MibScalar
svnProdName = _SvnProdName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 1),
    _SvnProdName_Type()
)
svnProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnProdName.setStatus("current")
_SvnProdVerMajor_Type = Integer32
_SvnProdVerMajor_Object = MibScalar
svnProdVerMajor = _SvnProdVerMajor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 2),
    _SvnProdVerMajor_Type()
)
svnProdVerMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnProdVerMajor.setStatus("current")
_SvnProdVerMinor_Type = Integer32
_SvnProdVerMinor_Object = MibScalar
svnProdVerMinor = _SvnProdVerMinor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 3),
    _SvnProdVerMinor_Type()
)
svnProdVerMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnProdVerMinor.setStatus("current")
_SvnInfo_ObjectIdentity = ObjectIdentity
svnInfo = _SvnInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 4)
)


class _SvnVersion_Type(DisplayString):
    """Custom type svnVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvnVersion_Type.__name__ = "DisplayString"
_SvnVersion_Object = MibScalar
svnVersion = _SvnVersion_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 4, 1),
    _SvnVersion_Type()
)
svnVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnVersion.setStatus("current")
_SvnBuild_Type = Integer32
_SvnBuild_Object = MibScalar
svnBuild = _SvnBuild_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 4, 2),
    _SvnBuild_Type()
)
svnBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnBuild.setStatus("current")
_SvnOSInfo_ObjectIdentity = ObjectIdentity
svnOSInfo = _SvnOSInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 5)
)


class _OsName_Type(DisplayString):
    """Custom type osName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OsName_Type.__name__ = "DisplayString"
_OsName_Object = MibScalar
osName = _OsName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 5, 1),
    _OsName_Type()
)
osName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osName.setStatus("current")
_OsMajorVer_Type = Integer32
_OsMajorVer_Object = MibScalar
osMajorVer = _OsMajorVer_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 5, 2),
    _OsMajorVer_Type()
)
osMajorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osMajorVer.setStatus("current")
_OsMinorVer_Type = Integer32
_OsMinorVer_Object = MibScalar
osMinorVer = _OsMinorVer_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 5, 3),
    _OsMinorVer_Type()
)
osMinorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osMinorVer.setStatus("current")
_OsBuildNum_Type = Integer32
_OsBuildNum_Object = MibScalar
osBuildNum = _OsBuildNum_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 5, 4),
    _OsBuildNum_Type()
)
osBuildNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osBuildNum.setStatus("current")
_OsSPmajor_Type = Integer32
_OsSPmajor_Object = MibScalar
osSPmajor = _OsSPmajor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 5, 5),
    _OsSPmajor_Type()
)
osSPmajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSPmajor.setStatus("current")
_OsSPminor_Type = Integer32
_OsSPminor_Object = MibScalar
osSPminor = _OsSPminor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 5, 6),
    _OsSPminor_Type()
)
osSPminor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSPminor.setStatus("current")


class _OsVersionLevel_Type(DisplayString):
    """Custom type osVersionLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OsVersionLevel_Type.__name__ = "DisplayString"
_OsVersionLevel_Object = MibScalar
osVersionLevel = _OsVersionLevel_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 5, 7),
    _OsVersionLevel_Type()
)
osVersionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osVersionLevel.setStatus("current")
_RoutingTable_Object = MibTable
routingTable = _RoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 6)
)
if mibBuilder.loadTexts:
    routingTable.setStatus("current")
_RoutingEntry_Object = MibTableRow
routingEntry = _RoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 6, 1)
)
routingEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "routingIndex"),
)
if mibBuilder.loadTexts:
    routingEntry.setStatus("current")
_RoutingIndex_Type = Unsigned32
_RoutingIndex_Object = MibTableColumn
routingIndex = _RoutingIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 6, 1, 1),
    _RoutingIndex_Type()
)
routingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingIndex.setStatus("current")
_RoutingDest_Type = IpAddress
_RoutingDest_Object = MibTableColumn
routingDest = _RoutingDest_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 6, 1, 2),
    _RoutingDest_Type()
)
routingDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingDest.setStatus("current")
_RoutingMask_Type = IpAddress
_RoutingMask_Object = MibTableColumn
routingMask = _RoutingMask_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 6, 1, 3),
    _RoutingMask_Type()
)
routingMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingMask.setStatus("current")
_RoutingGatweway_Type = IpAddress
_RoutingGatweway_Object = MibTableColumn
routingGatweway = _RoutingGatweway_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 6, 1, 4),
    _RoutingGatweway_Type()
)
routingGatweway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingGatweway.setStatus("current")
_RoutingIntrfName_Type = DisplayString
_RoutingIntrfName_Object = MibTableColumn
routingIntrfName = _RoutingIntrfName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 6, 1, 5),
    _RoutingIntrfName_Type()
)
routingIntrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingIntrfName.setStatus("current")
_SvnPerf_ObjectIdentity = ObjectIdentity
svnPerf = _SvnPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7)
)
_SvnMem_ObjectIdentity = ObjectIdentity
svnMem = _SvnMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 1)
)
_MemTotalVirtual_Type = Integer32
_MemTotalVirtual_Object = MibScalar
memTotalVirtual = _MemTotalVirtual_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 1, 1),
    _MemTotalVirtual_Type()
)
memTotalVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalVirtual.setStatus("current")
_MemActiveVirtual_Type = Integer32
_MemActiveVirtual_Object = MibScalar
memActiveVirtual = _MemActiveVirtual_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 1, 2),
    _MemActiveVirtual_Type()
)
memActiveVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memActiveVirtual.setStatus("current")
_MemTotalReal_Type = Integer32
_MemTotalReal_Object = MibScalar
memTotalReal = _MemTotalReal_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 1, 3),
    _MemTotalReal_Type()
)
memTotalReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalReal.setStatus("current")
_MemActiveReal_Type = Integer32
_MemActiveReal_Object = MibScalar
memActiveReal = _MemActiveReal_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 1, 4),
    _MemActiveReal_Type()
)
memActiveReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memActiveReal.setStatus("current")
_MemFreeReal_Type = Integer32
_MemFreeReal_Object = MibScalar
memFreeReal = _MemFreeReal_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 1, 5),
    _MemFreeReal_Type()
)
memFreeReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memFreeReal.setStatus("current")
_MemSwapsSec_Type = Integer32
_MemSwapsSec_Object = MibScalar
memSwapsSec = _MemSwapsSec_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 1, 6),
    _MemSwapsSec_Type()
)
memSwapsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memSwapsSec.setStatus("current")
_MemDiskTransfers_Type = Integer32
_MemDiskTransfers_Object = MibScalar
memDiskTransfers = _MemDiskTransfers_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 1, 7),
    _MemDiskTransfers_Type()
)
memDiskTransfers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memDiskTransfers.setStatus("current")
_SvnProc_ObjectIdentity = ObjectIdentity
svnProc = _SvnProc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 2)
)
_ProcUsrTime_Type = Integer32
_ProcUsrTime_Object = MibScalar
procUsrTime = _ProcUsrTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 2, 1),
    _ProcUsrTime_Type()
)
procUsrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procUsrTime.setStatus("current")
_ProcSysTime_Type = Integer32
_ProcSysTime_Object = MibScalar
procSysTime = _ProcSysTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 2, 2),
    _ProcSysTime_Type()
)
procSysTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procSysTime.setStatus("current")
_ProcIdleTime_Type = Integer32
_ProcIdleTime_Object = MibScalar
procIdleTime = _ProcIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 2, 3),
    _ProcIdleTime_Type()
)
procIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procIdleTime.setStatus("current")
_ProcUsage_Type = Integer32
_ProcUsage_Object = MibScalar
procUsage = _ProcUsage_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 2, 4),
    _ProcUsage_Type()
)
procUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procUsage.setStatus("current")
_ProcQueue_Type = Integer32
_ProcQueue_Object = MibScalar
procQueue = _ProcQueue_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 2, 5),
    _ProcQueue_Type()
)
procQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procQueue.setStatus("current")
_ProcInterrupts_Type = Integer32
_ProcInterrupts_Object = MibScalar
procInterrupts = _ProcInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 2, 6),
    _ProcInterrupts_Type()
)
procInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procInterrupts.setStatus("current")
_ProcNum_Type = Integer32
_ProcNum_Object = MibScalar
procNum = _ProcNum_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 2, 7),
    _ProcNum_Type()
)
procNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procNum.setStatus("current")
_SvnDisk_ObjectIdentity = ObjectIdentity
svnDisk = _SvnDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 3)
)
_DiskTime_Type = Integer32
_DiskTime_Object = MibScalar
diskTime = _DiskTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 3, 1),
    _DiskTime_Type()
)
diskTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTime.setStatus("current")
_DiskQueue_Type = Integer32
_DiskQueue_Object = MibScalar
diskQueue = _DiskQueue_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 3, 2),
    _DiskQueue_Type()
)
diskQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskQueue.setStatus("current")
_DiskPercent_Type = Integer32
_DiskPercent_Object = MibScalar
diskPercent = _DiskPercent_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 3, 3),
    _DiskPercent_Type()
)
diskPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPercent.setStatus("current")


class _DiskFreeTotal_Type(DisplayString):
    """Custom type diskFreeTotal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DiskFreeTotal_Type.__name__ = "DisplayString"
_DiskFreeTotal_Object = MibScalar
diskFreeTotal = _DiskFreeTotal_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 3, 4),
    _DiskFreeTotal_Type()
)
diskFreeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskFreeTotal.setStatus("current")


class _DiskFreeAvail_Type(DisplayString):
    """Custom type diskFreeAvail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DiskFreeAvail_Type.__name__ = "DisplayString"
_DiskFreeAvail_Object = MibScalar
diskFreeAvail = _DiskFreeAvail_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 3, 5),
    _DiskFreeAvail_Type()
)
diskFreeAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskFreeAvail.setStatus("current")


class _DiskTotal_Type(DisplayString):
    """Custom type diskTotal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DiskTotal_Type.__name__ = "DisplayString"
_DiskTotal_Object = MibScalar
diskTotal = _DiskTotal_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 3, 6),
    _DiskTotal_Type()
)
diskTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTotal.setStatus("current")
_SvnMem64_ObjectIdentity = ObjectIdentity
svnMem64 = _SvnMem64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 4)
)


class _MemTotalVirtual64_Type(DisplayString):
    """Custom type memTotalVirtual64 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MemTotalVirtual64_Type.__name__ = "DisplayString"
_MemTotalVirtual64_Object = MibScalar
memTotalVirtual64 = _MemTotalVirtual64_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 4, 1),
    _MemTotalVirtual64_Type()
)
memTotalVirtual64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalVirtual64.setStatus("current")


class _MemActiveVirtual64_Type(DisplayString):
    """Custom type memActiveVirtual64 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MemActiveVirtual64_Type.__name__ = "DisplayString"
_MemActiveVirtual64_Object = MibScalar
memActiveVirtual64 = _MemActiveVirtual64_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 4, 2),
    _MemActiveVirtual64_Type()
)
memActiveVirtual64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memActiveVirtual64.setStatus("current")


class _MemTotalReal64_Type(DisplayString):
    """Custom type memTotalReal64 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MemTotalReal64_Type.__name__ = "DisplayString"
_MemTotalReal64_Object = MibScalar
memTotalReal64 = _MemTotalReal64_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 4, 3),
    _MemTotalReal64_Type()
)
memTotalReal64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalReal64.setStatus("current")


class _MemActiveReal64_Type(DisplayString):
    """Custom type memActiveReal64 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MemActiveReal64_Type.__name__ = "DisplayString"
_MemActiveReal64_Object = MibScalar
memActiveReal64 = _MemActiveReal64_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 4, 4),
    _MemActiveReal64_Type()
)
memActiveReal64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memActiveReal64.setStatus("current")


class _MemFreeReal64_Type(DisplayString):
    """Custom type memFreeReal64 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MemFreeReal64_Type.__name__ = "DisplayString"
_MemFreeReal64_Object = MibScalar
memFreeReal64 = _MemFreeReal64_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 4, 5),
    _MemFreeReal64_Type()
)
memFreeReal64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memFreeReal64.setStatus("current")
_MemSwapsSec64_Type = Integer32
_MemSwapsSec64_Object = MibScalar
memSwapsSec64 = _MemSwapsSec64_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 4, 6),
    _MemSwapsSec64_Type()
)
memSwapsSec64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memSwapsSec64.setStatus("current")
_MemDiskTransfers64_Type = Integer32
_MemDiskTransfers64_Object = MibScalar
memDiskTransfers64 = _MemDiskTransfers64_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 4, 7),
    _MemDiskTransfers64_Type()
)
memDiskTransfers64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memDiskTransfers64.setStatus("current")
_MultiProcTable_Object = MibTable
multiProcTable = _MultiProcTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 5)
)
if mibBuilder.loadTexts:
    multiProcTable.setStatus("current")
_MultiProcEntry_Object = MibTableRow
multiProcEntry = _MultiProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 5, 1)
)
multiProcEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "multiProcIndex"),
)
if mibBuilder.loadTexts:
    multiProcEntry.setStatus("current")
_MultiProcIndex_Type = Unsigned32
_MultiProcIndex_Object = MibTableColumn
multiProcIndex = _MultiProcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 5, 1, 1),
    _MultiProcIndex_Type()
)
multiProcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiProcIndex.setStatus("current")
_MultiProcUserTime_Type = Integer32
_MultiProcUserTime_Object = MibTableColumn
multiProcUserTime = _MultiProcUserTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 5, 1, 2),
    _MultiProcUserTime_Type()
)
multiProcUserTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiProcUserTime.setStatus("current")
_MultiProcSystemTime_Type = Integer32
_MultiProcSystemTime_Object = MibTableColumn
multiProcSystemTime = _MultiProcSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 5, 1, 3),
    _MultiProcSystemTime_Type()
)
multiProcSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiProcSystemTime.setStatus("current")
_MultiProcIdleTime_Type = Integer32
_MultiProcIdleTime_Object = MibTableColumn
multiProcIdleTime = _MultiProcIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 5, 1, 4),
    _MultiProcIdleTime_Type()
)
multiProcIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiProcIdleTime.setStatus("current")
_MultiProcUsage_Type = Integer32
_MultiProcUsage_Object = MibTableColumn
multiProcUsage = _MultiProcUsage_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 5, 1, 5),
    _MultiProcUsage_Type()
)
multiProcUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiProcUsage.setStatus("current")
_MultiProcRunQueue_Type = Integer32
_MultiProcRunQueue_Object = MibTableColumn
multiProcRunQueue = _MultiProcRunQueue_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 5, 1, 6),
    _MultiProcRunQueue_Type()
)
multiProcRunQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiProcRunQueue.setStatus("current")
_MultiProcInterrupts_Type = Integer32
_MultiProcInterrupts_Object = MibTableColumn
multiProcInterrupts = _MultiProcInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 5, 1, 7),
    _MultiProcInterrupts_Type()
)
multiProcInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiProcInterrupts.setStatus("current")
_MultiDiskTable_Object = MibTable
multiDiskTable = _MultiDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 6)
)
if mibBuilder.loadTexts:
    multiDiskTable.setStatus("current")
_MultiDiskEntry_Object = MibTableRow
multiDiskEntry = _MultiDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 6, 1)
)
multiDiskEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "multiDiskIndex"),
)
if mibBuilder.loadTexts:
    multiDiskEntry.setStatus("current")
_MultiDiskIndex_Type = Unsigned32
_MultiDiskIndex_Object = MibTableColumn
multiDiskIndex = _MultiDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 6, 1, 1),
    _MultiDiskIndex_Type()
)
multiDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiDiskIndex.setStatus("current")
_MultiDiskName_Type = DisplayString
_MultiDiskName_Object = MibTableColumn
multiDiskName = _MultiDiskName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 6, 1, 2),
    _MultiDiskName_Type()
)
multiDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiDiskName.setStatus("current")
_MultiDiskSize_Type = DisplayString
_MultiDiskSize_Object = MibTableColumn
multiDiskSize = _MultiDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 6, 1, 3),
    _MultiDiskSize_Type()
)
multiDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiDiskSize.setStatus("current")
_MultiDiskUsed_Type = DisplayString
_MultiDiskUsed_Object = MibTableColumn
multiDiskUsed = _MultiDiskUsed_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 6, 1, 4),
    _MultiDiskUsed_Type()
)
multiDiskUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiDiskUsed.setStatus("current")
_MultiDiskFreeTotalBytes_Type = DisplayString
_MultiDiskFreeTotalBytes_Object = MibTableColumn
multiDiskFreeTotalBytes = _MultiDiskFreeTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 6, 1, 5),
    _MultiDiskFreeTotalBytes_Type()
)
multiDiskFreeTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiDiskFreeTotalBytes.setStatus("current")
_MultiDiskFreeTotalPercent_Type = Integer32
_MultiDiskFreeTotalPercent_Object = MibTableColumn
multiDiskFreeTotalPercent = _MultiDiskFreeTotalPercent_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 6, 1, 6),
    _MultiDiskFreeTotalPercent_Type()
)
multiDiskFreeTotalPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiDiskFreeTotalPercent.setStatus("current")
_MultiDiskFreeAvailableBytes_Type = DisplayString
_MultiDiskFreeAvailableBytes_Object = MibTableColumn
multiDiskFreeAvailableBytes = _MultiDiskFreeAvailableBytes_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 6, 1, 7),
    _MultiDiskFreeAvailableBytes_Type()
)
multiDiskFreeAvailableBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiDiskFreeAvailableBytes.setStatus("current")
_MultiDiskFreeAvailablePercent_Type = Integer32
_MultiDiskFreeAvailablePercent_Object = MibTableColumn
multiDiskFreeAvailablePercent = _MultiDiskFreeAvailablePercent_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 6, 1, 8),
    _MultiDiskFreeAvailablePercent_Type()
)
multiDiskFreeAvailablePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiDiskFreeAvailablePercent.setStatus("current")
_RaidInfo_ObjectIdentity = ObjectIdentity
raidInfo = _RaidInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7)
)
_RaidVolumeTable_Object = MibTable
raidVolumeTable = _RaidVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 1)
)
if mibBuilder.loadTexts:
    raidVolumeTable.setStatus("current")
_RaidVolumeEntry_Object = MibTableRow
raidVolumeEntry = _RaidVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 1, 1)
)
raidVolumeEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "raidVolumeIndex"),
)
if mibBuilder.loadTexts:
    raidVolumeEntry.setStatus("current")
_RaidVolumeIndex_Type = Unsigned32
_RaidVolumeIndex_Object = MibTableColumn
raidVolumeIndex = _RaidVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 1, 1, 1),
    _RaidVolumeIndex_Type()
)
raidVolumeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVolumeIndex.setStatus("current")
_RaidVolumeID_Type = Integer32
_RaidVolumeID_Object = MibTableColumn
raidVolumeID = _RaidVolumeID_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 1, 1, 2),
    _RaidVolumeID_Type()
)
raidVolumeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVolumeID.setStatus("current")
_RaidVolumeType_Type = Integer32
_RaidVolumeType_Object = MibTableColumn
raidVolumeType = _RaidVolumeType_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 1, 1, 3),
    _RaidVolumeType_Type()
)
raidVolumeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVolumeType.setStatus("current")
_NumOfDisksOnRaid_Type = Integer32
_NumOfDisksOnRaid_Object = MibTableColumn
numOfDisksOnRaid = _NumOfDisksOnRaid_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 1, 1, 4),
    _NumOfDisksOnRaid_Type()
)
numOfDisksOnRaid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfDisksOnRaid.setStatus("current")
_RaidVolumeMaxLBA_Type = Integer32
_RaidVolumeMaxLBA_Object = MibTableColumn
raidVolumeMaxLBA = _RaidVolumeMaxLBA_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 1, 1, 5),
    _RaidVolumeMaxLBA_Type()
)
raidVolumeMaxLBA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVolumeMaxLBA.setStatus("current")
_RaidVolumeState_Type = Integer32
_RaidVolumeState_Object = MibTableColumn
raidVolumeState = _RaidVolumeState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 1, 1, 6),
    _RaidVolumeState_Type()
)
raidVolumeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVolumeState.setStatus("current")
_RaidVolumeFlags_Type = Integer32
_RaidVolumeFlags_Object = MibTableColumn
raidVolumeFlags = _RaidVolumeFlags_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 1, 1, 7),
    _RaidVolumeFlags_Type()
)
raidVolumeFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVolumeFlags.setStatus("current")
_RaidVolumeSize_Type = Integer32
_RaidVolumeSize_Object = MibTableColumn
raidVolumeSize = _RaidVolumeSize_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 1, 1, 8),
    _RaidVolumeSize_Type()
)
raidVolumeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidVolumeSize.setStatus("current")
_RaidDiskTable_Object = MibTable
raidDiskTable = _RaidDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 2)
)
if mibBuilder.loadTexts:
    raidDiskTable.setStatus("current")
_RaidDiskEntry_Object = MibTableRow
raidDiskEntry = _RaidDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 2, 1)
)
raidDiskEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "raidDiskIndex"),
)
if mibBuilder.loadTexts:
    raidDiskEntry.setStatus("current")
_RaidDiskIndex_Type = Unsigned32
_RaidDiskIndex_Object = MibTableColumn
raidDiskIndex = _RaidDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 2, 1, 1),
    _RaidDiskIndex_Type()
)
raidDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskIndex.setStatus("current")
_RaidDiskVolumeID_Type = Integer32
_RaidDiskVolumeID_Object = MibTableColumn
raidDiskVolumeID = _RaidDiskVolumeID_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 2, 1, 2),
    _RaidDiskVolumeID_Type()
)
raidDiskVolumeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskVolumeID.setStatus("current")
_RaidDiskID_Type = Integer32
_RaidDiskID_Object = MibTableColumn
raidDiskID = _RaidDiskID_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 2, 1, 3),
    _RaidDiskID_Type()
)
raidDiskID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskID.setStatus("current")
_RaidDiskNumber_Type = Integer32
_RaidDiskNumber_Object = MibTableColumn
raidDiskNumber = _RaidDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 2, 1, 4),
    _RaidDiskNumber_Type()
)
raidDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskNumber.setStatus("current")


class _RaidDiskVendor_Type(DisplayString):
    """Custom type raidDiskVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RaidDiskVendor_Type.__name__ = "DisplayString"
_RaidDiskVendor_Object = MibTableColumn
raidDiskVendor = _RaidDiskVendor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 2, 1, 5),
    _RaidDiskVendor_Type()
)
raidDiskVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskVendor.setStatus("current")


class _RaidDiskProductID_Type(DisplayString):
    """Custom type raidDiskProductID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RaidDiskProductID_Type.__name__ = "DisplayString"
_RaidDiskProductID_Object = MibTableColumn
raidDiskProductID = _RaidDiskProductID_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 2, 1, 6),
    _RaidDiskProductID_Type()
)
raidDiskProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskProductID.setStatus("current")


class _RaidDiskRevision_Type(DisplayString):
    """Custom type raidDiskRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RaidDiskRevision_Type.__name__ = "DisplayString"
_RaidDiskRevision_Object = MibTableColumn
raidDiskRevision = _RaidDiskRevision_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 2, 1, 7),
    _RaidDiskRevision_Type()
)
raidDiskRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskRevision.setStatus("current")
_RaidDiskMaxLBA_Type = Integer32
_RaidDiskMaxLBA_Object = MibTableColumn
raidDiskMaxLBA = _RaidDiskMaxLBA_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 2, 1, 8),
    _RaidDiskMaxLBA_Type()
)
raidDiskMaxLBA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskMaxLBA.setStatus("current")
_RaidDiskState_Type = Integer32
_RaidDiskState_Object = MibTableColumn
raidDiskState = _RaidDiskState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 2, 1, 9),
    _RaidDiskState_Type()
)
raidDiskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskState.setStatus("current")
_RaidDiskFlags_Type = Integer32
_RaidDiskFlags_Object = MibTableColumn
raidDiskFlags = _RaidDiskFlags_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 2, 1, 10),
    _RaidDiskFlags_Type()
)
raidDiskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskFlags.setStatus("current")
_RaidDiskSyncState_Type = Integer32
_RaidDiskSyncState_Object = MibTableColumn
raidDiskSyncState = _RaidDiskSyncState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 2, 1, 11),
    _RaidDiskSyncState_Type()
)
raidDiskSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskSyncState.setStatus("current")
_RaidDiskSize_Type = Integer32
_RaidDiskSize_Object = MibTableColumn
raidDiskSize = _RaidDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 7, 2, 1, 12),
    _RaidDiskSize_Type()
)
raidDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDiskSize.setStatus("current")
_SensorInfo_ObjectIdentity = ObjectIdentity
sensorInfo = _SensorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8)
)
_TempertureSensorTable_Object = MibTable
tempertureSensorTable = _TempertureSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 1)
)
if mibBuilder.loadTexts:
    tempertureSensorTable.setStatus("current")
_TempertureSensorEntry_Object = MibTableRow
tempertureSensorEntry = _TempertureSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 1, 1)
)
tempertureSensorEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "tempertureSensorIndex"),
)
if mibBuilder.loadTexts:
    tempertureSensorEntry.setStatus("current")
_TempertureSensorIndex_Type = Unsigned32
_TempertureSensorIndex_Object = MibTableColumn
tempertureSensorIndex = _TempertureSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 1, 1, 1),
    _TempertureSensorIndex_Type()
)
tempertureSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempertureSensorIndex.setStatus("current")


class _TempertureSensorName_Type(DisplayString):
    """Custom type tempertureSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TempertureSensorName_Type.__name__ = "DisplayString"
_TempertureSensorName_Object = MibTableColumn
tempertureSensorName = _TempertureSensorName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 1, 1, 2),
    _TempertureSensorName_Type()
)
tempertureSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempertureSensorName.setStatus("current")


class _TempertureSensorValue_Type(DisplayString):
    """Custom type tempertureSensorValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TempertureSensorValue_Type.__name__ = "DisplayString"
_TempertureSensorValue_Object = MibTableColumn
tempertureSensorValue = _TempertureSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 1, 1, 3),
    _TempertureSensorValue_Type()
)
tempertureSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempertureSensorValue.setStatus("current")


class _TempertureSensorUnit_Type(DisplayString):
    """Custom type tempertureSensorUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TempertureSensorUnit_Type.__name__ = "DisplayString"
_TempertureSensorUnit_Object = MibTableColumn
tempertureSensorUnit = _TempertureSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 1, 1, 4),
    _TempertureSensorUnit_Type()
)
tempertureSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempertureSensorUnit.setStatus("current")


class _TempertureSensorType_Type(DisplayString):
    """Custom type tempertureSensorType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TempertureSensorType_Type.__name__ = "DisplayString"
_TempertureSensorType_Object = MibTableColumn
tempertureSensorType = _TempertureSensorType_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 1, 1, 5),
    _TempertureSensorType_Type()
)
tempertureSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempertureSensorType.setStatus("current")
_TempertureSensorStatus_Type = Integer32
_TempertureSensorStatus_Object = MibTableColumn
tempertureSensorStatus = _TempertureSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 1, 1, 6),
    _TempertureSensorStatus_Type()
)
tempertureSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempertureSensorStatus.setStatus("current")
_FanSpeedSensorTable_Object = MibTable
fanSpeedSensorTable = _FanSpeedSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 2)
)
if mibBuilder.loadTexts:
    fanSpeedSensorTable.setStatus("current")
_FanSpeedSensorEntry_Object = MibTableRow
fanSpeedSensorEntry = _FanSpeedSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 2, 1)
)
fanSpeedSensorEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "fanSpeedSensorIndex"),
)
if mibBuilder.loadTexts:
    fanSpeedSensorEntry.setStatus("current")
_FanSpeedSensorIndex_Type = Unsigned32
_FanSpeedSensorIndex_Object = MibTableColumn
fanSpeedSensorIndex = _FanSpeedSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 2, 1, 1),
    _FanSpeedSensorIndex_Type()
)
fanSpeedSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedSensorIndex.setStatus("current")


class _FanSpeedSensorName_Type(DisplayString):
    """Custom type fanSpeedSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FanSpeedSensorName_Type.__name__ = "DisplayString"
_FanSpeedSensorName_Object = MibTableColumn
fanSpeedSensorName = _FanSpeedSensorName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 2, 1, 2),
    _FanSpeedSensorName_Type()
)
fanSpeedSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedSensorName.setStatus("current")


class _FanSpeedSensorValue_Type(DisplayString):
    """Custom type fanSpeedSensorValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FanSpeedSensorValue_Type.__name__ = "DisplayString"
_FanSpeedSensorValue_Object = MibTableColumn
fanSpeedSensorValue = _FanSpeedSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 2, 1, 3),
    _FanSpeedSensorValue_Type()
)
fanSpeedSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedSensorValue.setStatus("current")


class _FanSpeedSensorUnit_Type(DisplayString):
    """Custom type fanSpeedSensorUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FanSpeedSensorUnit_Type.__name__ = "DisplayString"
_FanSpeedSensorUnit_Object = MibTableColumn
fanSpeedSensorUnit = _FanSpeedSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 2, 1, 4),
    _FanSpeedSensorUnit_Type()
)
fanSpeedSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedSensorUnit.setStatus("current")


class _FanSpeedSensorType_Type(DisplayString):
    """Custom type fanSpeedSensorType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FanSpeedSensorType_Type.__name__ = "DisplayString"
_FanSpeedSensorType_Object = MibTableColumn
fanSpeedSensorType = _FanSpeedSensorType_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 2, 1, 5),
    _FanSpeedSensorType_Type()
)
fanSpeedSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedSensorType.setStatus("current")
_FanSpeedSensorStatus_Type = Integer32
_FanSpeedSensorStatus_Object = MibTableColumn
fanSpeedSensorStatus = _FanSpeedSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 2, 1, 6),
    _FanSpeedSensorStatus_Type()
)
fanSpeedSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedSensorStatus.setStatus("current")
_VoltageSensorTable_Object = MibTable
voltageSensorTable = _VoltageSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 3)
)
if mibBuilder.loadTexts:
    voltageSensorTable.setStatus("current")
_VoltageSensorEntry_Object = MibTableRow
voltageSensorEntry = _VoltageSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 3, 1)
)
voltageSensorEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "voltageSensorIndex"),
)
if mibBuilder.loadTexts:
    voltageSensorEntry.setStatus("current")
_VoltageSensorIndex_Type = Unsigned32
_VoltageSensorIndex_Object = MibTableColumn
voltageSensorIndex = _VoltageSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 3, 1, 1),
    _VoltageSensorIndex_Type()
)
voltageSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorIndex.setStatus("current")


class _VoltageSensorName_Type(DisplayString):
    """Custom type voltageSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoltageSensorName_Type.__name__ = "DisplayString"
_VoltageSensorName_Object = MibTableColumn
voltageSensorName = _VoltageSensorName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 3, 1, 2),
    _VoltageSensorName_Type()
)
voltageSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorName.setStatus("current")


class _VoltageSensorValue_Type(DisplayString):
    """Custom type voltageSensorValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoltageSensorValue_Type.__name__ = "DisplayString"
_VoltageSensorValue_Object = MibTableColumn
voltageSensorValue = _VoltageSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 3, 1, 3),
    _VoltageSensorValue_Type()
)
voltageSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorValue.setStatus("current")


class _VoltageSensorUnit_Type(DisplayString):
    """Custom type voltageSensorUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoltageSensorUnit_Type.__name__ = "DisplayString"
_VoltageSensorUnit_Object = MibTableColumn
voltageSensorUnit = _VoltageSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 3, 1, 4),
    _VoltageSensorUnit_Type()
)
voltageSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorUnit.setStatus("current")


class _VoltageSensorType_Type(DisplayString):
    """Custom type voltageSensorType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoltageSensorType_Type.__name__ = "DisplayString"
_VoltageSensorType_Object = MibTableColumn
voltageSensorType = _VoltageSensorType_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 3, 1, 5),
    _VoltageSensorType_Type()
)
voltageSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorType.setStatus("current")
_VoltageSensorStatus_Type = Integer32
_VoltageSensorStatus_Object = MibTableColumn
voltageSensorStatus = _VoltageSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 8, 3, 1, 6),
    _VoltageSensorStatus_Type()
)
voltageSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorStatus.setStatus("current")
_PowerSupplyInfo_ObjectIdentity = ObjectIdentity
powerSupplyInfo = _PowerSupplyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 9)
)
_PowerSupplyTable_Object = MibTable
powerSupplyTable = _PowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 9, 1)
)
if mibBuilder.loadTexts:
    powerSupplyTable.setStatus("current")
_PowerSupplyEntry_Object = MibTableRow
powerSupplyEntry = _PowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 9, 1, 1)
)
powerSupplyEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "powerSupplyIndex"),
)
if mibBuilder.loadTexts:
    powerSupplyEntry.setStatus("current")
_PowerSupplyIndex_Type = Unsigned32
_PowerSupplyIndex_Object = MibTableColumn
powerSupplyIndex = _PowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 9, 1, 1, 1),
    _PowerSupplyIndex_Type()
)
powerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyIndex.setStatus("current")
_PowerSupplyStatus_Type = DisplayString
_PowerSupplyStatus_Object = MibTableColumn
powerSupplyStatus = _PowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 7, 9, 1, 1, 2),
    _PowerSupplyStatus_Type()
)
powerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyStatus.setStatus("current")
_SvnSysTime_Type = Integer32
_SvnSysTime_Object = MibScalar
svnSysTime = _SvnSysTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 8),
    _SvnSysTime_Type()
)
svnSysTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnSysTime.setStatus("current")
_SvnRoutingModify_ObjectIdentity = ObjectIdentity
svnRoutingModify = _SvnRoutingModify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 9)
)
_SvnRouteModDest_Type = IpAddress
_SvnRouteModDest_Object = MibScalar
svnRouteModDest = _SvnRouteModDest_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 9, 2),
    _SvnRouteModDest_Type()
)
svnRouteModDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnRouteModDest.setStatus("current")
_SvnRouteModMask_Type = IpAddress
_SvnRouteModMask_Object = MibScalar
svnRouteModMask = _SvnRouteModMask_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 9, 3),
    _SvnRouteModMask_Type()
)
svnRouteModMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnRouteModMask.setStatus("current")
_SvnRouteModGateway_Type = IpAddress
_SvnRouteModGateway_Object = MibScalar
svnRouteModGateway = _SvnRouteModGateway_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 9, 4),
    _SvnRouteModGateway_Type()
)
svnRouteModGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnRouteModGateway.setStatus("current")
_SvnRouteModIfIndex_Type = Integer32
_SvnRouteModIfIndex_Object = MibScalar
svnRouteModIfIndex = _SvnRouteModIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 9, 5),
    _SvnRouteModIfIndex_Type()
)
svnRouteModIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnRouteModIfIndex.setStatus("current")


class _SvnRouteModIfName_Type(DisplayString):
    """Custom type svnRouteModIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvnRouteModIfName_Type.__name__ = "DisplayString"
_SvnRouteModIfName_Object = MibScalar
svnRouteModIfName = _SvnRouteModIfName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 9, 6),
    _SvnRouteModIfName_Type()
)
svnRouteModIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnRouteModIfName.setStatus("current")
_SvnRouteModAction_Type = Integer32
_SvnRouteModAction_Object = MibScalar
svnRouteModAction = _SvnRouteModAction_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 9, 10),
    _SvnRouteModAction_Type()
)
svnRouteModAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnRouteModAction.setStatus("current")
_SvnUTCTimeOffset_Type = Integer32
_SvnUTCTimeOffset_Object = MibScalar
svnUTCTimeOffset = _SvnUTCTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 10),
    _SvnUTCTimeOffset_Type()
)
svnUTCTimeOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnUTCTimeOffset.setStatus("current")
_SvnLogDaemon_ObjectIdentity = ObjectIdentity
svnLogDaemon = _SvnLogDaemon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 11)
)


class _SvnLogDStat_Type(DisplayString):
    """Custom type svnLogDStat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvnLogDStat_Type.__name__ = "DisplayString"
_SvnLogDStat_Object = MibScalar
svnLogDStat = _SvnLogDStat_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 11, 1),
    _SvnLogDStat_Type()
)
svnLogDStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnLogDStat.setStatus("current")
_SvnSysStartTime_Type = Integer32
_SvnSysStartTime_Object = MibScalar
svnSysStartTime = _SvnSysStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 12),
    _SvnSysStartTime_Type()
)
svnSysStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnSysStartTime.setStatus("current")
_SvnSysUniqId_Type = DisplayString
_SvnSysUniqId_Object = MibScalar
svnSysUniqId = _SvnSysUniqId_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 13),
    _SvnSysUniqId_Type()
)
svnSysUniqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnSysUniqId.setStatus("current")
_SvnWebUIPort_Type = Integer32
_SvnWebUIPort_Object = MibScalar
svnWebUIPort = _SvnWebUIPort_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 15),
    _SvnWebUIPort_Type()
)
svnWebUIPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnWebUIPort.setStatus("current")
_SvnApplianceInfo_ObjectIdentity = ObjectIdentity
svnApplianceInfo = _SvnApplianceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 16)
)


class _SvnApplianceSerialNumber_Type(DisplayString):
    """Custom type svnApplianceSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvnApplianceSerialNumber_Type.__name__ = "DisplayString"
_SvnApplianceSerialNumber_Object = MibScalar
svnApplianceSerialNumber = _SvnApplianceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 16, 3),
    _SvnApplianceSerialNumber_Type()
)
svnApplianceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnApplianceSerialNumber.setStatus("current")


class _SvnApplianceProductName_Type(DisplayString):
    """Custom type svnApplianceProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvnApplianceProductName_Type.__name__ = "DisplayString"
_SvnApplianceProductName_Object = MibScalar
svnApplianceProductName = _SvnApplianceProductName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 16, 7),
    _SvnApplianceProductName_Type()
)
svnApplianceProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnApplianceProductName.setStatus("current")


class _SvnApplianceManufacturer_Type(DisplayString):
    """Custom type svnApplianceManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvnApplianceManufacturer_Type.__name__ = "DisplayString"
_SvnApplianceManufacturer_Object = MibScalar
svnApplianceManufacturer = _SvnApplianceManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 16, 9),
    _SvnApplianceManufacturer_Type()
)
svnApplianceManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnApplianceManufacturer.setStatus("current")
_SvnNetStat_ObjectIdentity = ObjectIdentity
svnNetStat = _SvnNetStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 50)
)
_SvnNetIfTable_Object = MibTable
svnNetIfTable = _SvnNetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 50, 1)
)
if mibBuilder.loadTexts:
    svnNetIfTable.setStatus("current")
_SvnNetIfTableEntry_Object = MibTableRow
svnNetIfTableEntry = _SvnNetIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 50, 1, 1)
)
svnNetIfTableEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "svnNetIfIndex"),
)
if mibBuilder.loadTexts:
    svnNetIfTableEntry.setStatus("current")
_SvnNetIfIndex_Type = Unsigned32
_SvnNetIfIndex_Object = MibTableColumn
svnNetIfIndex = _SvnNetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 50, 1, 1, 1),
    _SvnNetIfIndex_Type()
)
svnNetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnNetIfIndex.setStatus("current")
_SvnNetIfVsid_Type = Integer32
_SvnNetIfVsid_Object = MibTableColumn
svnNetIfVsid = _SvnNetIfVsid_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 50, 1, 1, 2),
    _SvnNetIfVsid_Type()
)
svnNetIfVsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnNetIfVsid.setStatus("current")
_SvnNetIfName_Type = DisplayString
_SvnNetIfName_Object = MibTableColumn
svnNetIfName = _SvnNetIfName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 50, 1, 1, 3),
    _SvnNetIfName_Type()
)
svnNetIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnNetIfName.setStatus("current")
_SvnNetIfAddress_Type = IpAddress
_SvnNetIfAddress_Object = MibTableColumn
svnNetIfAddress = _SvnNetIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 50, 1, 1, 4),
    _SvnNetIfAddress_Type()
)
svnNetIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnNetIfAddress.setStatus("current")
_SvnNetIfMask_Type = IpAddress
_SvnNetIfMask_Object = MibTableColumn
svnNetIfMask = _SvnNetIfMask_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 50, 1, 1, 5),
    _SvnNetIfMask_Type()
)
svnNetIfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnNetIfMask.setStatus("current")
_SvnNetIfMTU_Type = Integer32
_SvnNetIfMTU_Object = MibTableColumn
svnNetIfMTU = _SvnNetIfMTU_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 50, 1, 1, 6),
    _SvnNetIfMTU_Type()
)
svnNetIfMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnNetIfMTU.setStatus("current")
_SvnNetIfState_Type = Integer32
_SvnNetIfState_Object = MibTableColumn
svnNetIfState = _SvnNetIfState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 50, 1, 1, 7),
    _SvnNetIfState_Type()
)
svnNetIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnNetIfState.setStatus("current")
_SvnNetIfMAC_Type = DisplayString
_SvnNetIfMAC_Object = MibTableColumn
svnNetIfMAC = _SvnNetIfMAC_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 50, 1, 1, 8),
    _SvnNetIfMAC_Type()
)
svnNetIfMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnNetIfMAC.setStatus("current")
_SvnNetIfDescription_Type = DisplayString
_SvnNetIfDescription_Object = MibTableColumn
svnNetIfDescription = _SvnNetIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 50, 1, 1, 9),
    _SvnNetIfDescription_Type()
)
svnNetIfDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnNetIfDescription.setStatus("current")
_SvnNetIfOperState_Type = Integer32
_SvnNetIfOperState_Object = MibTableColumn
svnNetIfOperState = _SvnNetIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 50, 1, 1, 10),
    _SvnNetIfOperState_Type()
)
svnNetIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnNetIfOperState.setStatus("current")
_VsRoutingTable_Object = MibTable
vsRoutingTable = _VsRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 51)
)
if mibBuilder.loadTexts:
    vsRoutingTable.setStatus("current")
_VsRoutingEntry_Object = MibTableRow
vsRoutingEntry = _VsRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 51, 1)
)
vsRoutingEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "vsRoutingIndex"),
)
if mibBuilder.loadTexts:
    vsRoutingEntry.setStatus("current")
_VsRoutingIndex_Type = Unsigned32
_VsRoutingIndex_Object = MibTableColumn
vsRoutingIndex = _VsRoutingIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 51, 1, 1),
    _VsRoutingIndex_Type()
)
vsRoutingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsRoutingIndex.setStatus("current")
_VsRoutingDest_Type = IpAddress
_VsRoutingDest_Object = MibTableColumn
vsRoutingDest = _VsRoutingDest_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 51, 1, 2),
    _VsRoutingDest_Type()
)
vsRoutingDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsRoutingDest.setStatus("current")
_VsRoutingMask_Type = IpAddress
_VsRoutingMask_Object = MibTableColumn
vsRoutingMask = _VsRoutingMask_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 51, 1, 3),
    _VsRoutingMask_Type()
)
vsRoutingMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsRoutingMask.setStatus("current")
_VsRoutingGateway_Type = IpAddress
_VsRoutingGateway_Object = MibTableColumn
vsRoutingGateway = _VsRoutingGateway_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 51, 1, 4),
    _VsRoutingGateway_Type()
)
vsRoutingGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsRoutingGateway.setStatus("current")
_VsRoutingIntrfName_Type = DisplayString
_VsRoutingIntrfName_Object = MibTableColumn
vsRoutingIntrfName = _VsRoutingIntrfName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 51, 1, 5),
    _VsRoutingIntrfName_Type()
)
vsRoutingIntrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsRoutingIntrfName.setStatus("current")
_VsRoutingVsId_Type = Integer32
_VsRoutingVsId_Object = MibTableColumn
vsRoutingVsId = _VsRoutingVsId_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 51, 1, 6),
    _VsRoutingVsId_Type()
)
vsRoutingVsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsRoutingVsId.setStatus("current")
_SvnStatCode_Type = Integer32
_SvnStatCode_Object = MibScalar
svnStatCode = _SvnStatCode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 101),
    _SvnStatCode_Type()
)
svnStatCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnStatCode.setStatus("current")


class _SvnStatShortDescr_Type(DisplayString):
    """Custom type svnStatShortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvnStatShortDescr_Type.__name__ = "DisplayString"
_SvnStatShortDescr_Object = MibScalar
svnStatShortDescr = _SvnStatShortDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 102),
    _SvnStatShortDescr_Type()
)
svnStatShortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnStatShortDescr.setStatus("current")


class _SvnStatLongDescr_Type(DisplayString):
    """Custom type svnStatLongDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvnStatLongDescr_Type.__name__ = "DisplayString"
_SvnStatLongDescr_Object = MibScalar
svnStatLongDescr = _SvnStatLongDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 103),
    _SvnStatLongDescr_Type()
)
svnStatLongDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnStatLongDescr.setStatus("current")
_SvnServicePack_Type = Integer32
_SvnServicePack_Object = MibScalar
svnServicePack = _SvnServicePack_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 6, 999),
    _SvnServicePack_Type()
)
svnServicePack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svnServicePack.setStatus("current")
_Mngmt_ObjectIdentity = ObjectIdentity
mngmt = _Mngmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 7)
)


class _MgProdName_Type(DisplayString):
    """Custom type mgProdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MgProdName_Type.__name__ = "DisplayString"
_MgProdName_Object = MibScalar
mgProdName = _MgProdName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 7, 1),
    _MgProdName_Type()
)
mgProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgProdName.setStatus("current")
_MgVerMajor_Type = Integer32
_MgVerMajor_Object = MibScalar
mgVerMajor = _MgVerMajor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 7, 2),
    _MgVerMajor_Type()
)
mgVerMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgVerMajor.setStatus("current")
_MgVerMinor_Type = Integer32
_MgVerMinor_Object = MibScalar
mgVerMinor = _MgVerMinor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 7, 3),
    _MgVerMinor_Type()
)
mgVerMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgVerMinor.setStatus("current")
_MgBuildNumber_Type = Integer32
_MgBuildNumber_Object = MibScalar
mgBuildNumber = _MgBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 7, 4),
    _MgBuildNumber_Type()
)
mgBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgBuildNumber.setStatus("current")
_MgActiveStatus_Type = DisplayString
_MgActiveStatus_Object = MibScalar
mgActiveStatus = _MgActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 7, 5),
    _MgActiveStatus_Type()
)
mgActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgActiveStatus.setStatus("current")
_MgFwmIsAlive_Type = Integer32
_MgFwmIsAlive_Object = MibScalar
mgFwmIsAlive = _MgFwmIsAlive_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 7, 6),
    _MgFwmIsAlive_Type()
)
mgFwmIsAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgFwmIsAlive.setStatus("current")
_MgConnectedClientsTable_Object = MibTable
mgConnectedClientsTable = _MgConnectedClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 7, 7)
)
if mibBuilder.loadTexts:
    mgConnectedClientsTable.setStatus("current")
_MgConnectedClientsEntry_Object = MibTableRow
mgConnectedClientsEntry = _MgConnectedClientsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 7, 7, 1)
)
mgConnectedClientsEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "mgIndex"),
)
if mibBuilder.loadTexts:
    mgConnectedClientsEntry.setStatus("current")
_MgIndex_Type = Unsigned32
_MgIndex_Object = MibTableColumn
mgIndex = _MgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 7, 7, 1, 1),
    _MgIndex_Type()
)
mgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgIndex.setStatus("current")
_MgClientName_Type = DisplayString
_MgClientName_Object = MibTableColumn
mgClientName = _MgClientName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 7, 7, 1, 2),
    _MgClientName_Type()
)
mgClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgClientName.setStatus("current")
_MgClientHost_Type = DisplayString
_MgClientHost_Object = MibTableColumn
mgClientHost = _MgClientHost_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 7, 7, 1, 3),
    _MgClientHost_Type()
)
mgClientHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgClientHost.setStatus("current")
_MgClientDbLock_Type = DisplayString
_MgClientDbLock_Object = MibTableColumn
mgClientDbLock = _MgClientDbLock_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 7, 7, 1, 4),
    _MgClientDbLock_Type()
)
mgClientDbLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgClientDbLock.setStatus("current")
_MgApplicationType_Type = DisplayString
_MgApplicationType_Object = MibTableColumn
mgApplicationType = _MgApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 7, 7, 1, 5),
    _MgApplicationType_Type()
)
mgApplicationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgApplicationType.setStatus("current")
_MgStatCode_Type = Integer32
_MgStatCode_Object = MibScalar
mgStatCode = _MgStatCode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 7, 101),
    _MgStatCode_Type()
)
mgStatCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgStatCode.setStatus("current")


class _MgStatShortDescr_Type(DisplayString):
    """Custom type mgStatShortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MgStatShortDescr_Type.__name__ = "DisplayString"
_MgStatShortDescr_Object = MibScalar
mgStatShortDescr = _MgStatShortDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 7, 102),
    _MgStatShortDescr_Type()
)
mgStatShortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgStatShortDescr.setStatus("current")


class _MgStatLongDescr_Type(DisplayString):
    """Custom type mgStatLongDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MgStatLongDescr_Type.__name__ = "DisplayString"
_MgStatLongDescr_Object = MibScalar
mgStatLongDescr = _MgStatLongDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 7, 103),
    _MgStatLongDescr_Type()
)
mgStatLongDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgStatLongDescr.setStatus("current")
_Wam_ObjectIdentity = ObjectIdentity
wam = _Wam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8)
)


class _WamProdName_Type(DisplayString):
    """Custom type wamProdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WamProdName_Type.__name__ = "DisplayString"
_WamProdName_Object = MibScalar
wamProdName = _WamProdName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 1),
    _WamProdName_Type()
)
wamProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamProdName.setStatus("current")
_WamVerMajor_Type = Integer32
_WamVerMajor_Object = MibScalar
wamVerMajor = _WamVerMajor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 2),
    _WamVerMajor_Type()
)
wamVerMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamVerMajor.setStatus("current")
_WamVerMinor_Type = Integer32
_WamVerMinor_Object = MibScalar
wamVerMinor = _WamVerMinor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 3),
    _WamVerMinor_Type()
)
wamVerMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamVerMinor.setStatus("current")


class _WamState_Type(DisplayString):
    """Custom type wamState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WamState_Type.__name__ = "DisplayString"
_WamState_Object = MibScalar
wamState = _WamState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 4),
    _WamState_Type()
)
wamState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamState.setStatus("current")


class _WamName_Type(DisplayString):
    """Custom type wamName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WamName_Type.__name__ = "DisplayString"
_WamName_Object = MibScalar
wamName = _WamName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 5),
    _WamName_Type()
)
wamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamName.setStatus("current")
_WamPluginPerformance_ObjectIdentity = ObjectIdentity
wamPluginPerformance = _WamPluginPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 6)
)
_WamAcceptReq_Type = Integer32
_WamAcceptReq_Object = MibScalar
wamAcceptReq = _WamAcceptReq_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 6, 1),
    _WamAcceptReq_Type()
)
wamAcceptReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAcceptReq.setStatus("current")
_WamRejectReq_Type = Integer32
_WamRejectReq_Object = MibScalar
wamRejectReq = _WamRejectReq_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 6, 2),
    _WamRejectReq_Type()
)
wamRejectReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamRejectReq.setStatus("current")
_WamPolicy_ObjectIdentity = ObjectIdentity
wamPolicy = _WamPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 7)
)


class _WamPolicyName_Type(DisplayString):
    """Custom type wamPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WamPolicyName_Type.__name__ = "DisplayString"
_WamPolicyName_Object = MibScalar
wamPolicyName = _WamPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 7, 1),
    _WamPolicyName_Type()
)
wamPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamPolicyName.setStatus("current")


class _WamPolicyUpdate_Type(DisplayString):
    """Custom type wamPolicyUpdate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WamPolicyUpdate_Type.__name__ = "DisplayString"
_WamPolicyUpdate_Object = MibScalar
wamPolicyUpdate = _WamPolicyUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 7, 2),
    _WamPolicyUpdate_Type()
)
wamPolicyUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamPolicyUpdate.setStatus("current")
_WamUagQueries_ObjectIdentity = ObjectIdentity
wamUagQueries = _WamUagQueries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 8)
)


class _WamUagHost_Type(DisplayString):
    """Custom type wamUagHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WamUagHost_Type.__name__ = "DisplayString"
_WamUagHost_Object = MibScalar
wamUagHost = _WamUagHost_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 8, 1),
    _WamUagHost_Type()
)
wamUagHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamUagHost.setStatus("current")
_WamUagIp_Type = Integer32
_WamUagIp_Object = MibScalar
wamUagIp = _WamUagIp_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 8, 2),
    _WamUagIp_Type()
)
wamUagIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamUagIp.setStatus("current")
_WamUagPort_Type = Integer32
_WamUagPort_Object = MibScalar
wamUagPort = _WamUagPort_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 8, 3),
    _WamUagPort_Type()
)
wamUagPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamUagPort.setStatus("current")
_WamUagNoQueries_Type = Integer32
_WamUagNoQueries_Object = MibScalar
wamUagNoQueries = _WamUagNoQueries_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 8, 4),
    _WamUagNoQueries_Type()
)
wamUagNoQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamUagNoQueries.setStatus("current")


class _WamUagLastQuery_Type(DisplayString):
    """Custom type wamUagLastQuery based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WamUagLastQuery_Type.__name__ = "DisplayString"
_WamUagLastQuery_Object = MibScalar
wamUagLastQuery = _WamUagLastQuery_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 8, 5),
    _WamUagLastQuery_Type()
)
wamUagLastQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamUagLastQuery.setStatus("current")
_WamGlobalPerformance_ObjectIdentity = ObjectIdentity
wamGlobalPerformance = _WamGlobalPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 9)
)
_WamOpenSessions_Type = Integer32
_WamOpenSessions_Object = MibScalar
wamOpenSessions = _WamOpenSessions_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 9, 1),
    _WamOpenSessions_Type()
)
wamOpenSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamOpenSessions.setStatus("current")


class _WamLastSession_Type(DisplayString):
    """Custom type wamLastSession based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WamLastSession_Type.__name__ = "DisplayString"
_WamLastSession_Object = MibScalar
wamLastSession = _WamLastSession_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 9, 2),
    _WamLastSession_Type()
)
wamLastSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamLastSession.setStatus("current")
_WamStatCode_Type = Integer32
_WamStatCode_Object = MibScalar
wamStatCode = _WamStatCode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 101),
    _WamStatCode_Type()
)
wamStatCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamStatCode.setStatus("current")


class _WamStatShortDescr_Type(DisplayString):
    """Custom type wamStatShortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WamStatShortDescr_Type.__name__ = "DisplayString"
_WamStatShortDescr_Object = MibScalar
wamStatShortDescr = _WamStatShortDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 102),
    _WamStatShortDescr_Type()
)
wamStatShortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamStatShortDescr.setStatus("current")


class _WamStatLongDescr_Type(DisplayString):
    """Custom type wamStatLongDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WamStatLongDescr_Type.__name__ = "DisplayString"
_WamStatLongDescr_Object = MibScalar
wamStatLongDescr = _WamStatLongDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 8, 103),
    _WamStatLongDescr_Type()
)
wamStatLongDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamStatLongDescr.setStatus("current")
_Dtps_ObjectIdentity = ObjectIdentity
dtps = _Dtps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 9)
)


class _DtpsProdName_Type(DisplayString):
    """Custom type dtpsProdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DtpsProdName_Type.__name__ = "DisplayString"
_DtpsProdName_Object = MibScalar
dtpsProdName = _DtpsProdName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 9, 1),
    _DtpsProdName_Type()
)
dtpsProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpsProdName.setStatus("current")
_DtpsVerMajor_Type = Integer32
_DtpsVerMajor_Object = MibScalar
dtpsVerMajor = _DtpsVerMajor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 9, 2),
    _DtpsVerMajor_Type()
)
dtpsVerMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpsVerMajor.setStatus("current")
_DtpsVerMinor_Type = Integer32
_DtpsVerMinor_Object = MibScalar
dtpsVerMinor = _DtpsVerMinor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 9, 3),
    _DtpsVerMinor_Type()
)
dtpsVerMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpsVerMinor.setStatus("current")
_DtpsLicensedUsers_Type = Integer32
_DtpsLicensedUsers_Object = MibScalar
dtpsLicensedUsers = _DtpsLicensedUsers_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 9, 4),
    _DtpsLicensedUsers_Type()
)
dtpsLicensedUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpsLicensedUsers.setStatus("current")
_DtpsConnectedUsers_Type = Integer32
_DtpsConnectedUsers_Object = MibScalar
dtpsConnectedUsers = _DtpsConnectedUsers_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 9, 5),
    _DtpsConnectedUsers_Type()
)
dtpsConnectedUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpsConnectedUsers.setStatus("current")
_DtpsStatCode_Type = Integer32
_DtpsStatCode_Object = MibScalar
dtpsStatCode = _DtpsStatCode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 9, 101),
    _DtpsStatCode_Type()
)
dtpsStatCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpsStatCode.setStatus("current")


class _DtpsStatShortDescr_Type(DisplayString):
    """Custom type dtpsStatShortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DtpsStatShortDescr_Type.__name__ = "DisplayString"
_DtpsStatShortDescr_Object = MibScalar
dtpsStatShortDescr = _DtpsStatShortDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 9, 102),
    _DtpsStatShortDescr_Type()
)
dtpsStatShortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpsStatShortDescr.setStatus("current")


class _DtpsStatLongDescr_Type(DisplayString):
    """Custom type dtpsStatLongDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DtpsStatLongDescr_Type.__name__ = "DisplayString"
_DtpsStatLongDescr_Object = MibScalar
dtpsStatLongDescr = _DtpsStatLongDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 9, 103),
    _DtpsStatLongDescr_Type()
)
dtpsStatLongDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpsStatLongDescr.setStatus("current")
_Ls_ObjectIdentity = ObjectIdentity
ls = _Ls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 11)
)


class _LsProdName_Type(DisplayString):
    """Custom type lsProdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LsProdName_Type.__name__ = "DisplayString"
_LsProdName_Object = MibScalar
lsProdName = _LsProdName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 11, 1),
    _LsProdName_Type()
)
lsProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsProdName.setStatus("current")
_LsVerMajor_Type = Integer32
_LsVerMajor_Object = MibScalar
lsVerMajor = _LsVerMajor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 11, 2),
    _LsVerMajor_Type()
)
lsVerMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsVerMajor.setStatus("current")
_LsVerMinor_Type = Integer32
_LsVerMinor_Object = MibScalar
lsVerMinor = _LsVerMinor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 11, 3),
    _LsVerMinor_Type()
)
lsVerMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsVerMinor.setStatus("current")
_LsBuildNumber_Type = Integer32
_LsBuildNumber_Object = MibScalar
lsBuildNumber = _LsBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 11, 4),
    _LsBuildNumber_Type()
)
lsBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsBuildNumber.setStatus("current")
_LsFwmIsAlive_Type = Integer32
_LsFwmIsAlive_Object = MibScalar
lsFwmIsAlive = _LsFwmIsAlive_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 11, 5),
    _LsFwmIsAlive_Type()
)
lsFwmIsAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsFwmIsAlive.setStatus("current")
_LsConnectedClientsTable_Object = MibTable
lsConnectedClientsTable = _LsConnectedClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 11, 7)
)
if mibBuilder.loadTexts:
    lsConnectedClientsTable.setStatus("current")
_LsConnectedClientsEntry_Object = MibTableRow
lsConnectedClientsEntry = _LsConnectedClientsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 11, 7, 1)
)
lsConnectedClientsEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "lsIndex"),
)
if mibBuilder.loadTexts:
    lsConnectedClientsEntry.setStatus("current")
_LsIndex_Type = Unsigned32
_LsIndex_Object = MibTableColumn
lsIndex = _LsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 11, 7, 1, 1),
    _LsIndex_Type()
)
lsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsIndex.setStatus("current")
_LsClientName_Type = DisplayString
_LsClientName_Object = MibTableColumn
lsClientName = _LsClientName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 11, 7, 1, 2),
    _LsClientName_Type()
)
lsClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsClientName.setStatus("current")
_LsClientHost_Type = DisplayString
_LsClientHost_Object = MibTableColumn
lsClientHost = _LsClientHost_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 11, 7, 1, 3),
    _LsClientHost_Type()
)
lsClientHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsClientHost.setStatus("current")
_LsClientDbLock_Type = DisplayString
_LsClientDbLock_Object = MibTableColumn
lsClientDbLock = _LsClientDbLock_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 11, 7, 1, 4),
    _LsClientDbLock_Type()
)
lsClientDbLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsClientDbLock.setStatus("current")
_LsApplicationType_Type = DisplayString
_LsApplicationType_Object = MibTableColumn
lsApplicationType = _LsApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 11, 7, 1, 5),
    _LsApplicationType_Type()
)
lsApplicationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsApplicationType.setStatus("current")
_LsStatCode_Type = Integer32
_LsStatCode_Object = MibScalar
lsStatCode = _LsStatCode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 11, 101),
    _LsStatCode_Type()
)
lsStatCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsStatCode.setStatus("current")


class _LsStatShortDescr_Type(DisplayString):
    """Custom type lsStatShortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LsStatShortDescr_Type.__name__ = "DisplayString"
_LsStatShortDescr_Object = MibScalar
lsStatShortDescr = _LsStatShortDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 11, 102),
    _LsStatShortDescr_Type()
)
lsStatShortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsStatShortDescr.setStatus("current")


class _LsStatLongDescr_Type(DisplayString):
    """Custom type lsStatLongDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LsStatLongDescr_Type.__name__ = "DisplayString"
_LsStatLongDescr_Object = MibScalar
lsStatLongDescr = _LsStatLongDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 11, 103),
    _LsStatLongDescr_Type()
)
lsStatLongDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsStatLongDescr.setStatus("current")
_Vsx_ObjectIdentity = ObjectIdentity
vsx = _Vsx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16)
)
_VsxVsSupported_Type = Integer32
_VsxVsSupported_Object = MibScalar
vsxVsSupported = _VsxVsSupported_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 11),
    _VsxVsSupported_Type()
)
vsxVsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxVsSupported.setStatus("current")
_VsxVsConfigured_Type = Integer32
_VsxVsConfigured_Object = MibScalar
vsxVsConfigured = _VsxVsConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 12),
    _VsxVsConfigured_Type()
)
vsxVsConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxVsConfigured.setStatus("current")
_VsxVsInstalled_Type = Integer32
_VsxVsInstalled_Object = MibScalar
vsxVsInstalled = _VsxVsInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 13),
    _VsxVsInstalled_Type()
)
vsxVsInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxVsInstalled.setStatus("current")
_VsxStatus_ObjectIdentity = ObjectIdentity
vsxStatus = _VsxStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 22)
)
_VsxStatusTable_Object = MibTable
vsxStatusTable = _VsxStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 22, 1)
)
if mibBuilder.loadTexts:
    vsxStatusTable.setStatus("current")
_VsxStatusEntry_Object = MibTableRow
vsxStatusEntry = _VsxStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 22, 1, 1)
)
vsxStatusEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "vsxStatusVSId"),
)
if mibBuilder.loadTexts:
    vsxStatusEntry.setStatus("current")
_VsxStatusVSId_Type = Unsigned32
_VsxStatusVSId_Object = MibTableColumn
vsxStatusVSId = _VsxStatusVSId_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 22, 1, 1, 1),
    _VsxStatusVSId_Type()
)
vsxStatusVSId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxStatusVSId.setStatus("current")
_VsxStatusVRId_Type = Unsigned32
_VsxStatusVRId_Object = MibTableColumn
vsxStatusVRId = _VsxStatusVRId_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 22, 1, 1, 2),
    _VsxStatusVRId_Type()
)
vsxStatusVRId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxStatusVRId.setStatus("current")
_VsxStatusVsName_Type = DisplayString
_VsxStatusVsName_Object = MibTableColumn
vsxStatusVsName = _VsxStatusVsName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 22, 1, 1, 3),
    _VsxStatusVsName_Type()
)
vsxStatusVsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxStatusVsName.setStatus("current")
_VsxStatusVsType_Type = DisplayString
_VsxStatusVsType_Object = MibTableColumn
vsxStatusVsType = _VsxStatusVsType_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 22, 1, 1, 4),
    _VsxStatusVsType_Type()
)
vsxStatusVsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxStatusVsType.setStatus("current")
_VsxStatusMainIP_Type = DisplayString
_VsxStatusMainIP_Object = MibTableColumn
vsxStatusMainIP = _VsxStatusMainIP_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 22, 1, 1, 5),
    _VsxStatusMainIP_Type()
)
vsxStatusMainIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxStatusMainIP.setStatus("current")
_VsxStatusPolicyName_Type = DisplayString
_VsxStatusPolicyName_Object = MibTableColumn
vsxStatusPolicyName = _VsxStatusPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 22, 1, 1, 6),
    _VsxStatusPolicyName_Type()
)
vsxStatusPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxStatusPolicyName.setStatus("current")
_VsxStatusVsPolicyType_Type = DisplayString
_VsxStatusVsPolicyType_Object = MibTableColumn
vsxStatusVsPolicyType = _VsxStatusVsPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 22, 1, 1, 7),
    _VsxStatusVsPolicyType_Type()
)
vsxStatusVsPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxStatusVsPolicyType.setStatus("current")
_VsxStatusSicTrustState_Type = DisplayString
_VsxStatusSicTrustState_Object = MibTableColumn
vsxStatusSicTrustState = _VsxStatusSicTrustState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 22, 1, 1, 8),
    _VsxStatusSicTrustState_Type()
)
vsxStatusSicTrustState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxStatusSicTrustState.setStatus("current")


class _VsxStatusHAState_Type(DisplayString):
    """Custom type vsxStatusHAState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VsxStatusHAState_Type.__name__ = "DisplayString"
_VsxStatusHAState_Object = MibTableColumn
vsxStatusHAState = _VsxStatusHAState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 22, 1, 1, 9),
    _VsxStatusHAState_Type()
)
vsxStatusHAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxStatusHAState.setStatus("current")
_VsxStatusVSWeight_Type = Integer32
_VsxStatusVSWeight_Object = MibTableColumn
vsxStatusVSWeight = _VsxStatusVSWeight_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 22, 1, 1, 10),
    _VsxStatusVSWeight_Type()
)
vsxStatusVSWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxStatusVSWeight.setStatus("current")
_VsxStatusCPUUsageTable_Object = MibTable
vsxStatusCPUUsageTable = _VsxStatusCPUUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 22, 2)
)
if mibBuilder.loadTexts:
    vsxStatusCPUUsageTable.setStatus("current")
_VsxStatusCPUUsageEntry_Object = MibTableRow
vsxStatusCPUUsageEntry = _VsxStatusCPUUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 22, 2, 1)
)
vsxStatusCPUUsageEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "vsxStatusVSId"),
)
if mibBuilder.loadTexts:
    vsxStatusCPUUsageEntry.setStatus("current")


class _VsxStatusCPUUsage1sec_Type(Integer32):
    """Custom type vsxStatusCPUUsage1sec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VsxStatusCPUUsage1sec_Type.__name__ = "Integer32"
_VsxStatusCPUUsage1sec_Object = MibTableColumn
vsxStatusCPUUsage1sec = _VsxStatusCPUUsage1sec_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 22, 2, 1, 1),
    _VsxStatusCPUUsage1sec_Type()
)
vsxStatusCPUUsage1sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxStatusCPUUsage1sec.setStatus("current")


class _VsxStatusCPUUsage10sec_Type(Integer32):
    """Custom type vsxStatusCPUUsage10sec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VsxStatusCPUUsage10sec_Type.__name__ = "Integer32"
_VsxStatusCPUUsage10sec_Object = MibTableColumn
vsxStatusCPUUsage10sec = _VsxStatusCPUUsage10sec_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 22, 2, 1, 2),
    _VsxStatusCPUUsage10sec_Type()
)
vsxStatusCPUUsage10sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxStatusCPUUsage10sec.setStatus("current")


class _VsxStatusCPUUsage1min_Type(Integer32):
    """Custom type vsxStatusCPUUsage1min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VsxStatusCPUUsage1min_Type.__name__ = "Integer32"
_VsxStatusCPUUsage1min_Object = MibTableColumn
vsxStatusCPUUsage1min = _VsxStatusCPUUsage1min_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 22, 2, 1, 3),
    _VsxStatusCPUUsage1min_Type()
)
vsxStatusCPUUsage1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxStatusCPUUsage1min.setStatus("current")


class _VsxStatusCPUUsage1hr_Type(Integer32):
    """Custom type vsxStatusCPUUsage1hr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VsxStatusCPUUsage1hr_Type.__name__ = "Integer32"
_VsxStatusCPUUsage1hr_Object = MibTableColumn
vsxStatusCPUUsage1hr = _VsxStatusCPUUsage1hr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 22, 2, 1, 4),
    _VsxStatusCPUUsage1hr_Type()
)
vsxStatusCPUUsage1hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxStatusCPUUsage1hr.setStatus("current")


class _VsxStatusCPUUsage24hr_Type(Integer32):
    """Custom type vsxStatusCPUUsage24hr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VsxStatusCPUUsage24hr_Type.__name__ = "Integer32"
_VsxStatusCPUUsage24hr_Object = MibTableColumn
vsxStatusCPUUsage24hr = _VsxStatusCPUUsage24hr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 22, 2, 1, 5),
    _VsxStatusCPUUsage24hr_Type()
)
vsxStatusCPUUsage24hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxStatusCPUUsage24hr.setStatus("current")
_VsxStatusCPUUsageVSId_Type = Integer32
_VsxStatusCPUUsageVSId_Object = MibTableColumn
vsxStatusCPUUsageVSId = _VsxStatusCPUUsageVSId_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 22, 2, 1, 6),
    _VsxStatusCPUUsageVSId_Type()
)
vsxStatusCPUUsageVSId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxStatusCPUUsageVSId.setStatus("current")
_VsxCounters_ObjectIdentity = ObjectIdentity
vsxCounters = _VsxCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 23)
)
_VsxCountersTable_Object = MibTable
vsxCountersTable = _VsxCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 23, 1)
)
if mibBuilder.loadTexts:
    vsxCountersTable.setStatus("current")
_VsxCountersEntry_Object = MibTableRow
vsxCountersEntry = _VsxCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 23, 1, 1)
)
vsxCountersEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "vsxStatusVSId"),
)
if mibBuilder.loadTexts:
    vsxCountersEntry.setStatus("current")
_VsxCountersVSId_Type = Integer32
_VsxCountersVSId_Object = MibTableColumn
vsxCountersVSId = _VsxCountersVSId_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 23, 1, 1, 1),
    _VsxCountersVSId_Type()
)
vsxCountersVSId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxCountersVSId.setStatus("current")
_VsxCountersConnNum_Type = Integer32
_VsxCountersConnNum_Object = MibTableColumn
vsxCountersConnNum = _VsxCountersConnNum_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 23, 1, 1, 2),
    _VsxCountersConnNum_Type()
)
vsxCountersConnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxCountersConnNum.setStatus("current")
_VsxCountersConnPeakNum_Type = Integer32
_VsxCountersConnPeakNum_Object = MibTableColumn
vsxCountersConnPeakNum = _VsxCountersConnPeakNum_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 23, 1, 1, 3),
    _VsxCountersConnPeakNum_Type()
)
vsxCountersConnPeakNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxCountersConnPeakNum.setStatus("current")
_VsxCountersConnTableLimit_Type = Integer32
_VsxCountersConnTableLimit_Object = MibTableColumn
vsxCountersConnTableLimit = _VsxCountersConnTableLimit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 23, 1, 1, 4),
    _VsxCountersConnTableLimit_Type()
)
vsxCountersConnTableLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxCountersConnTableLimit.setStatus("current")


class _VsxCountersPackets_Type(DisplayString):
    """Custom type vsxCountersPackets based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VsxCountersPackets_Type.__name__ = "DisplayString"
_VsxCountersPackets_Object = MibTableColumn
vsxCountersPackets = _VsxCountersPackets_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 23, 1, 1, 5),
    _VsxCountersPackets_Type()
)
vsxCountersPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxCountersPackets.setStatus("current")


class _VsxCountersDroppedTotal_Type(DisplayString):
    """Custom type vsxCountersDroppedTotal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VsxCountersDroppedTotal_Type.__name__ = "DisplayString"
_VsxCountersDroppedTotal_Object = MibTableColumn
vsxCountersDroppedTotal = _VsxCountersDroppedTotal_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 23, 1, 1, 6),
    _VsxCountersDroppedTotal_Type()
)
vsxCountersDroppedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxCountersDroppedTotal.setStatus("current")


class _VsxCountersAcceptedTotal_Type(DisplayString):
    """Custom type vsxCountersAcceptedTotal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VsxCountersAcceptedTotal_Type.__name__ = "DisplayString"
_VsxCountersAcceptedTotal_Object = MibTableColumn
vsxCountersAcceptedTotal = _VsxCountersAcceptedTotal_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 23, 1, 1, 7),
    _VsxCountersAcceptedTotal_Type()
)
vsxCountersAcceptedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxCountersAcceptedTotal.setStatus("current")


class _VsxCountersRejectedTotal_Type(DisplayString):
    """Custom type vsxCountersRejectedTotal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VsxCountersRejectedTotal_Type.__name__ = "DisplayString"
_VsxCountersRejectedTotal_Object = MibTableColumn
vsxCountersRejectedTotal = _VsxCountersRejectedTotal_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 23, 1, 1, 8),
    _VsxCountersRejectedTotal_Type()
)
vsxCountersRejectedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxCountersRejectedTotal.setStatus("current")


class _VsxCountersBytesAcceptedTotal_Type(DisplayString):
    """Custom type vsxCountersBytesAcceptedTotal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VsxCountersBytesAcceptedTotal_Type.__name__ = "DisplayString"
_VsxCountersBytesAcceptedTotal_Object = MibTableColumn
vsxCountersBytesAcceptedTotal = _VsxCountersBytesAcceptedTotal_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 23, 1, 1, 9),
    _VsxCountersBytesAcceptedTotal_Type()
)
vsxCountersBytesAcceptedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxCountersBytesAcceptedTotal.setStatus("current")


class _VsxCountersBytesDroppedTotal_Type(DisplayString):
    """Custom type vsxCountersBytesDroppedTotal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VsxCountersBytesDroppedTotal_Type.__name__ = "DisplayString"
_VsxCountersBytesDroppedTotal_Object = MibTableColumn
vsxCountersBytesDroppedTotal = _VsxCountersBytesDroppedTotal_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 23, 1, 1, 10),
    _VsxCountersBytesDroppedTotal_Type()
)
vsxCountersBytesDroppedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxCountersBytesDroppedTotal.setStatus("current")


class _VsxCountersBytesRejectedTotal_Type(DisplayString):
    """Custom type vsxCountersBytesRejectedTotal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VsxCountersBytesRejectedTotal_Type.__name__ = "DisplayString"
_VsxCountersBytesRejectedTotal_Object = MibTableColumn
vsxCountersBytesRejectedTotal = _VsxCountersBytesRejectedTotal_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 23, 1, 1, 11),
    _VsxCountersBytesRejectedTotal_Type()
)
vsxCountersBytesRejectedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxCountersBytesRejectedTotal.setStatus("current")


class _VsxCountersLoggedTotal_Type(DisplayString):
    """Custom type vsxCountersLoggedTotal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VsxCountersLoggedTotal_Type.__name__ = "DisplayString"
_VsxCountersLoggedTotal_Object = MibTableColumn
vsxCountersLoggedTotal = _VsxCountersLoggedTotal_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 23, 1, 1, 12),
    _VsxCountersLoggedTotal_Type()
)
vsxCountersLoggedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxCountersLoggedTotal.setStatus("current")


class _VsxCountersIsDataValid_Type(Integer32):
    """Custom type vsxCountersIsDataValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_VsxCountersIsDataValid_Type.__name__ = "Integer32"
_VsxCountersIsDataValid_Object = MibTableColumn
vsxCountersIsDataValid = _VsxCountersIsDataValid_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 16, 23, 1, 1, 13),
    _VsxCountersIsDataValid_Type()
)
vsxCountersIsDataValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsxCountersIsDataValid.setStatus("current")
_SmartDefense_ObjectIdentity = ObjectIdentity
smartDefense = _SmartDefense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17)
)
_AsmAttacks_ObjectIdentity = ObjectIdentity
asmAttacks = _AsmAttacks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1)
)
_AsmLayer3_ObjectIdentity = ObjectIdentity
asmLayer3 = _AsmLayer3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 1)
)
_AsmLayer4_ObjectIdentity = ObjectIdentity
asmLayer4 = _AsmLayer4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 2)
)
_AsmTCP_ObjectIdentity = ObjectIdentity
asmTCP = _AsmTCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 2, 1)
)
_AsmSynatk_ObjectIdentity = ObjectIdentity
asmSynatk = _AsmSynatk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 2, 1, 1)
)
_AsmSynatkSynAckTimeout_Type = Integer32
_AsmSynatkSynAckTimeout_Object = MibScalar
asmSynatkSynAckTimeout = _AsmSynatkSynAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 2, 1, 1, 1),
    _AsmSynatkSynAckTimeout_Type()
)
asmSynatkSynAckTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asmSynatkSynAckTimeout.setStatus("current")
_AsmSynatkSynAckReset_Type = Integer32
_AsmSynatkSynAckReset_Object = MibScalar
asmSynatkSynAckReset = _AsmSynatkSynAckReset_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 2, 1, 1, 2),
    _AsmSynatkSynAckReset_Type()
)
asmSynatkSynAckReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asmSynatkSynAckReset.setStatus("current")
_AsmSynatkModeChange_Type = Integer32
_AsmSynatkModeChange_Object = MibScalar
asmSynatkModeChange = _AsmSynatkModeChange_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 2, 1, 1, 3),
    _AsmSynatkModeChange_Type()
)
asmSynatkModeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asmSynatkModeChange.setStatus("current")
_AsmSynatkCurrentMode_Type = Integer32
_AsmSynatkCurrentMode_Object = MibScalar
asmSynatkCurrentMode = _AsmSynatkCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 2, 1, 1, 4),
    _AsmSynatkCurrentMode_Type()
)
asmSynatkCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asmSynatkCurrentMode.setStatus("current")
_AsmSynatkNumberofunAckedSyns_Type = Integer32
_AsmSynatkNumberofunAckedSyns_Object = MibScalar
asmSynatkNumberofunAckedSyns = _AsmSynatkNumberofunAckedSyns_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 2, 1, 1, 5),
    _AsmSynatkNumberofunAckedSyns_Type()
)
asmSynatkNumberofunAckedSyns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asmSynatkNumberofunAckedSyns.setStatus("current")
_AsmSmallPmtu_ObjectIdentity = ObjectIdentity
asmSmallPmtu = _AsmSmallPmtu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 2, 1, 2)
)
_SmallPMTUNumberOfAttacks_Type = Integer32
_SmallPMTUNumberOfAttacks_Object = MibScalar
smallPMTUNumberOfAttacks = _SmallPMTUNumberOfAttacks_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 2, 1, 2, 1),
    _SmallPMTUNumberOfAttacks_Type()
)
smallPMTUNumberOfAttacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smallPMTUNumberOfAttacks.setStatus("current")
_SmallPMTUValueOfMinimalMTUsize_Type = Integer32
_SmallPMTUValueOfMinimalMTUsize_Object = MibScalar
smallPMTUValueOfMinimalMTUsize = _SmallPMTUValueOfMinimalMTUsize_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 2, 1, 2, 2),
    _SmallPMTUValueOfMinimalMTUsize_Type()
)
smallPMTUValueOfMinimalMTUsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smallPMTUValueOfMinimalMTUsize.setStatus("current")
_AsmSeqval_ObjectIdentity = ObjectIdentity
asmSeqval = _AsmSeqval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 2, 1, 3)
)
_SequenceVerifierInvalidAck_Type = Integer32
_SequenceVerifierInvalidAck_Object = MibScalar
sequenceVerifierInvalidAck = _SequenceVerifierInvalidAck_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 2, 1, 3, 1),
    _SequenceVerifierInvalidAck_Type()
)
sequenceVerifierInvalidAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sequenceVerifierInvalidAck.setStatus("current")
_SequenceVerifierInvalidSequence_Type = Integer32
_SequenceVerifierInvalidSequence_Object = MibScalar
sequenceVerifierInvalidSequence = _SequenceVerifierInvalidSequence_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 2, 1, 3, 2),
    _SequenceVerifierInvalidSequence_Type()
)
sequenceVerifierInvalidSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sequenceVerifierInvalidSequence.setStatus("current")
_SequenceVerifierInvalidretransmit_Type = Integer32
_SequenceVerifierInvalidretransmit_Object = MibScalar
sequenceVerifierInvalidretransmit = _SequenceVerifierInvalidretransmit_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 2, 1, 3, 3),
    _SequenceVerifierInvalidretransmit_Type()
)
sequenceVerifierInvalidretransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sequenceVerifierInvalidretransmit.setStatus("current")
_AsmUDP_ObjectIdentity = ObjectIdentity
asmUDP = _AsmUDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 2, 2)
)
_AsmScans_ObjectIdentity = ObjectIdentity
asmScans = _AsmScans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 2, 3)
)
_AsmHostPortScan_ObjectIdentity = ObjectIdentity
asmHostPortScan = _AsmHostPortScan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 2, 3, 1)
)
_NumOfhostPortScan_Type = Integer32
_NumOfhostPortScan_Object = MibScalar
numOfhostPortScan = _NumOfhostPortScan_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 2, 3, 1, 1),
    _NumOfhostPortScan_Type()
)
numOfhostPortScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfhostPortScan.setStatus("current")
_AsmIPSweep_ObjectIdentity = ObjectIdentity
asmIPSweep = _AsmIPSweep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 2, 3, 2)
)
_NumOfIpSweep_Type = Integer32
_NumOfIpSweep_Object = MibScalar
numOfIpSweep = _NumOfIpSweep_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 2, 3, 2, 1),
    _NumOfIpSweep_Type()
)
numOfIpSweep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfIpSweep.setStatus("current")
_AsmLayer5_ObjectIdentity = ObjectIdentity
asmLayer5 = _AsmLayer5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3)
)
_AsmHTTP_ObjectIdentity = ObjectIdentity
asmHTTP = _AsmHTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 1)
)
_AsmHttpWorms_ObjectIdentity = ObjectIdentity
asmHttpWorms = _AsmHttpWorms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 1, 1)
)
_HttpWorms_Type = Integer32
_HttpWorms_Object = MibScalar
httpWorms = _HttpWorms_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 1, 1, 1),
    _HttpWorms_Type()
)
httpWorms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpWorms.setStatus("current")
_AsmHttpFormatViolatoin_ObjectIdentity = ObjectIdentity
asmHttpFormatViolatoin = _AsmHttpFormatViolatoin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 1, 2)
)
_HttpURLLengthViolation_Type = Integer32
_HttpURLLengthViolation_Object = MibScalar
httpURLLengthViolation = _HttpURLLengthViolation_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 1, 2, 1),
    _HttpURLLengthViolation_Type()
)
httpURLLengthViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpURLLengthViolation.setStatus("current")
_HttpHeaderLengthViolations_Type = Integer32
_HttpHeaderLengthViolations_Object = MibScalar
httpHeaderLengthViolations = _HttpHeaderLengthViolations_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 1, 2, 2),
    _HttpHeaderLengthViolations_Type()
)
httpHeaderLengthViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpHeaderLengthViolations.setStatus("current")
_HttpMaxHeaderReached_Type = Integer32
_HttpMaxHeaderReached_Object = MibScalar
httpMaxHeaderReached = _HttpMaxHeaderReached_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 1, 2, 3),
    _HttpMaxHeaderReached_Type()
)
httpMaxHeaderReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpMaxHeaderReached.setStatus("current")
_AsmHttpAsciiViolation_ObjectIdentity = ObjectIdentity
asmHttpAsciiViolation = _AsmHttpAsciiViolation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 1, 3)
)
_NumOfHttpASCIIViolations_Type = Integer32
_NumOfHttpASCIIViolations_Object = MibScalar
numOfHttpASCIIViolations = _NumOfHttpASCIIViolations_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 1, 3, 1),
    _NumOfHttpASCIIViolations_Type()
)
numOfHttpASCIIViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfHttpASCIIViolations.setStatus("current")
_AsmHttpP2PHeaderFilter_ObjectIdentity = ObjectIdentity
asmHttpP2PHeaderFilter = _AsmHttpP2PHeaderFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 1, 4)
)
_NumOfHttpP2PHeaders_Type = Integer32
_NumOfHttpP2PHeaders_Object = MibScalar
numOfHttpP2PHeaders = _NumOfHttpP2PHeaders_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 1, 4, 1),
    _NumOfHttpP2PHeaders_Type()
)
numOfHttpP2PHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfHttpP2PHeaders.setStatus("current")
_AsmCIFS_ObjectIdentity = ObjectIdentity
asmCIFS = _AsmCIFS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 2)
)
_AsmCIFSWorms_ObjectIdentity = ObjectIdentity
asmCIFSWorms = _AsmCIFSWorms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 2, 1)
)
_NumOfCIFSworms_Type = Integer32
_NumOfCIFSworms_Object = MibScalar
numOfCIFSworms = _NumOfCIFSworms_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 2, 1, 1),
    _NumOfCIFSworms_Type()
)
numOfCIFSworms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfCIFSworms.setStatus("current")
_AsmCIFSNullSession_ObjectIdentity = ObjectIdentity
asmCIFSNullSession = _AsmCIFSNullSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 2, 2)
)
_NumOfCIFSNullSessions_Type = Integer32
_NumOfCIFSNullSessions_Object = MibScalar
numOfCIFSNullSessions = _NumOfCIFSNullSessions_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 2, 2, 1),
    _NumOfCIFSNullSessions_Type()
)
numOfCIFSNullSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfCIFSNullSessions.setStatus("current")
_AsmCIFSBlockedPopUps_ObjectIdentity = ObjectIdentity
asmCIFSBlockedPopUps = _AsmCIFSBlockedPopUps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 2, 3)
)
_NumOfCIFSBlockedPopUps_Type = Integer32
_NumOfCIFSBlockedPopUps_Object = MibScalar
numOfCIFSBlockedPopUps = _NumOfCIFSBlockedPopUps_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 2, 3, 1),
    _NumOfCIFSBlockedPopUps_Type()
)
numOfCIFSBlockedPopUps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfCIFSBlockedPopUps.setStatus("current")
_AsmCIFSBlockedCommands_ObjectIdentity = ObjectIdentity
asmCIFSBlockedCommands = _AsmCIFSBlockedCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 2, 4)
)
_NumOfCIFSBlockedCommands_Type = Integer32
_NumOfCIFSBlockedCommands_Object = MibScalar
numOfCIFSBlockedCommands = _NumOfCIFSBlockedCommands_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 2, 4, 1),
    _NumOfCIFSBlockedCommands_Type()
)
numOfCIFSBlockedCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfCIFSBlockedCommands.setStatus("current")
_AsmCIFSPasswordLengthViolations_ObjectIdentity = ObjectIdentity
asmCIFSPasswordLengthViolations = _AsmCIFSPasswordLengthViolations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 2, 5)
)
_NumOfCIFSPasswordLengthViolations_Type = Integer32
_NumOfCIFSPasswordLengthViolations_Object = MibScalar
numOfCIFSPasswordLengthViolations = _NumOfCIFSPasswordLengthViolations_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 2, 5, 1),
    _NumOfCIFSPasswordLengthViolations_Type()
)
numOfCIFSPasswordLengthViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfCIFSPasswordLengthViolations.setStatus("current")
_AsmP2P_ObjectIdentity = ObjectIdentity
asmP2P = _AsmP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 3)
)
_AsmP2POtherConAttempts_ObjectIdentity = ObjectIdentity
asmP2POtherConAttempts = _AsmP2POtherConAttempts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 3, 1)
)
_NumOfP2POtherConAttempts_Type = Integer32
_NumOfP2POtherConAttempts_Object = MibScalar
numOfP2POtherConAttempts = _NumOfP2POtherConAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 3, 1, 1),
    _NumOfP2POtherConAttempts_Type()
)
numOfP2POtherConAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfP2POtherConAttempts.setStatus("current")
_AsmP2PKazaaConAttempts_ObjectIdentity = ObjectIdentity
asmP2PKazaaConAttempts = _AsmP2PKazaaConAttempts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 3, 2)
)
_NumOfP2PKazaaConAttempts_Type = Integer32
_NumOfP2PKazaaConAttempts_Object = MibScalar
numOfP2PKazaaConAttempts = _NumOfP2PKazaaConAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 3, 2, 1),
    _NumOfP2PKazaaConAttempts_Type()
)
numOfP2PKazaaConAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfP2PKazaaConAttempts.setStatus("current")
_AsmP2PeMuleConAttempts_ObjectIdentity = ObjectIdentity
asmP2PeMuleConAttempts = _AsmP2PeMuleConAttempts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 3, 3)
)
_NumOfP2PeMuleConAttempts_Type = Integer32
_NumOfP2PeMuleConAttempts_Object = MibScalar
numOfP2PeMuleConAttempts = _NumOfP2PeMuleConAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 3, 3, 1),
    _NumOfP2PeMuleConAttempts_Type()
)
numOfP2PeMuleConAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfP2PeMuleConAttempts.setStatus("current")
_AsmP2PGnutellaConAttempts_ObjectIdentity = ObjectIdentity
asmP2PGnutellaConAttempts = _AsmP2PGnutellaConAttempts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 3, 4)
)
_NumOfGnutellaConAttempts_Type = Integer32
_NumOfGnutellaConAttempts_Object = MibScalar
numOfGnutellaConAttempts = _NumOfGnutellaConAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 3, 4, 1),
    _NumOfGnutellaConAttempts_Type()
)
numOfGnutellaConAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfGnutellaConAttempts.setStatus("current")
_AsmP2PSkypeCon_ObjectIdentity = ObjectIdentity
asmP2PSkypeCon = _AsmP2PSkypeCon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 3, 5)
)
_NumOfP2PSkypeCon_Type = Integer32
_NumOfP2PSkypeCon_Object = MibScalar
numOfP2PSkypeCon = _NumOfP2PSkypeCon_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 3, 5, 1),
    _NumOfP2PSkypeCon_Type()
)
numOfP2PSkypeCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfP2PSkypeCon.setStatus("current")
_AsmP2PBitTorrentCon_ObjectIdentity = ObjectIdentity
asmP2PBitTorrentCon = _AsmP2PBitTorrentCon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 3, 6)
)
_NumOfBitTorrentCon_Type = Integer32
_NumOfBitTorrentCon_Object = MibScalar
numOfBitTorrentCon = _NumOfBitTorrentCon_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 17, 1, 3, 3, 6, 1),
    _NumOfBitTorrentCon_Type()
)
numOfBitTorrentCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfBitTorrentCon.setStatus("current")
_Avi_ObjectIdentity = ObjectIdentity
avi = _Avi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24)
)
_AviEngines_ObjectIdentity = ObjectIdentity
aviEngines = _AviEngines_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 1)
)
_AviEngineTable_Object = MibTable
aviEngineTable = _AviEngineTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 1, 1)
)
if mibBuilder.loadTexts:
    aviEngineTable.setStatus("current")
_AviEngineEntry_Object = MibTableRow
aviEngineEntry = _AviEngineEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 1, 1, 1)
)
aviEngineEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "aviEngineIndex"),
)
if mibBuilder.loadTexts:
    aviEngineEntry.setStatus("current")
_AviEngineIndex_Type = Unsigned32
_AviEngineIndex_Object = MibTableColumn
aviEngineIndex = _AviEngineIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 1, 1, 1, 1),
    _AviEngineIndex_Type()
)
aviEngineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviEngineIndex.setStatus("current")
_AviEngineName_Type = DisplayString
_AviEngineName_Object = MibTableColumn
aviEngineName = _AviEngineName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 1, 1, 1, 2),
    _AviEngineName_Type()
)
aviEngineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviEngineName.setStatus("current")
_AviEngineVer_Type = DisplayString
_AviEngineVer_Object = MibTableColumn
aviEngineVer = _AviEngineVer_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 1, 1, 1, 3),
    _AviEngineVer_Type()
)
aviEngineVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviEngineVer.setStatus("current")
_AviEngineDate_Type = Integer32
_AviEngineDate_Object = MibTableColumn
aviEngineDate = _AviEngineDate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 1, 1, 1, 4),
    _AviEngineDate_Type()
)
aviEngineDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviEngineDate.setStatus("current")
_AviSignatureName_Type = DisplayString
_AviSignatureName_Object = MibTableColumn
aviSignatureName = _AviSignatureName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 1, 1, 1, 5),
    _AviSignatureName_Type()
)
aviSignatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviSignatureName.setStatus("current")
_AviSignatureVer_Type = DisplayString
_AviSignatureVer_Object = MibTableColumn
aviSignatureVer = _AviSignatureVer_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 1, 1, 1, 6),
    _AviSignatureVer_Type()
)
aviSignatureVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviSignatureVer.setStatus("current")
_AviSignatureDate_Type = Integer32
_AviSignatureDate_Object = MibTableColumn
aviSignatureDate = _AviSignatureDate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 1, 1, 1, 7),
    _AviSignatureDate_Type()
)
aviSignatureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviSignatureDate.setStatus("current")
_AviLastSigCheckTime_Type = Integer32
_AviLastSigCheckTime_Object = MibTableColumn
aviLastSigCheckTime = _AviLastSigCheckTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 1, 1, 1, 8),
    _AviLastSigCheckTime_Type()
)
aviLastSigCheckTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviLastSigCheckTime.setStatus("current")
_AviLastSigLocation_Type = DisplayString
_AviLastSigLocation_Object = MibTableColumn
aviLastSigLocation = _AviLastSigLocation_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 1, 1, 1, 9),
    _AviLastSigLocation_Type()
)
aviLastSigLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviLastSigLocation.setStatus("current")
_AviLastLicExp_Type = DisplayString
_AviLastLicExp_Object = MibTableColumn
aviLastLicExp = _AviLastLicExp_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 1, 1, 1, 10),
    _AviLastLicExp_Type()
)
aviLastLicExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviLastLicExp.setStatus("current")
_AviTopViruses_ObjectIdentity = ObjectIdentity
aviTopViruses = _AviTopViruses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 2)
)
_AviTopVirusesTable_Object = MibTable
aviTopVirusesTable = _AviTopVirusesTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 2, 1)
)
if mibBuilder.loadTexts:
    aviTopVirusesTable.setStatus("current")
_AviTopVirusesEntry_Object = MibTableRow
aviTopVirusesEntry = _AviTopVirusesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 2, 1, 1)
)
aviTopVirusesEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "aviTopVirusesIndex"),
)
if mibBuilder.loadTexts:
    aviTopVirusesEntry.setStatus("current")
_AviTopVirusesIndex_Type = Unsigned32
_AviTopVirusesIndex_Object = MibTableColumn
aviTopVirusesIndex = _AviTopVirusesIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 2, 1, 1, 1),
    _AviTopVirusesIndex_Type()
)
aviTopVirusesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviTopVirusesIndex.setStatus("current")
_AviTopVirusesName_Type = DisplayString
_AviTopVirusesName_Object = MibTableColumn
aviTopVirusesName = _AviTopVirusesName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 2, 1, 1, 2),
    _AviTopVirusesName_Type()
)
aviTopVirusesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviTopVirusesName.setStatus("current")
_AviTopVirusesCnt_Type = Integer32
_AviTopVirusesCnt_Object = MibTableColumn
aviTopVirusesCnt = _AviTopVirusesCnt_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 2, 1, 1, 3),
    _AviTopVirusesCnt_Type()
)
aviTopVirusesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviTopVirusesCnt.setStatus("current")
_AviTopEverViruses_ObjectIdentity = ObjectIdentity
aviTopEverViruses = _AviTopEverViruses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 3)
)
_AviTopEverVirusesTable_Object = MibTable
aviTopEverVirusesTable = _AviTopEverVirusesTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 3, 1)
)
if mibBuilder.loadTexts:
    aviTopEverVirusesTable.setStatus("current")
_AviTopEverVirusesEntry_Object = MibTableRow
aviTopEverVirusesEntry = _AviTopEverVirusesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 3, 1, 1)
)
aviTopEverVirusesEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "aviTopEverVirusesIndex"),
)
if mibBuilder.loadTexts:
    aviTopEverVirusesEntry.setStatus("current")
_AviTopEverVirusesIndex_Type = Unsigned32
_AviTopEverVirusesIndex_Object = MibTableColumn
aviTopEverVirusesIndex = _AviTopEverVirusesIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 3, 1, 1, 1),
    _AviTopEverVirusesIndex_Type()
)
aviTopEverVirusesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviTopEverVirusesIndex.setStatus("current")
_AviTopEverVirusesName_Type = DisplayString
_AviTopEverVirusesName_Object = MibTableColumn
aviTopEverVirusesName = _AviTopEverVirusesName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 3, 1, 1, 2),
    _AviTopEverVirusesName_Type()
)
aviTopEverVirusesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviTopEverVirusesName.setStatus("current")
_AviTopEverVirusesCnt_Type = Integer32
_AviTopEverVirusesCnt_Object = MibTableColumn
aviTopEverVirusesCnt = _AviTopEverVirusesCnt_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 3, 1, 1, 3),
    _AviTopEverVirusesCnt_Type()
)
aviTopEverVirusesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviTopEverVirusesCnt.setStatus("current")
_AviServices_ObjectIdentity = ObjectIdentity
aviServices = _AviServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4)
)
_AviServicesHTTP_ObjectIdentity = ObjectIdentity
aviServicesHTTP = _AviServicesHTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 1)
)
_AviHTTPState_Type = Integer32
_AviHTTPState_Object = MibScalar
aviHTTPState = _AviHTTPState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 1, 1),
    _AviHTTPState_Type()
)
aviHTTPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviHTTPState.setStatus("current")
_AviHTTPLastVirusName_Type = DisplayString
_AviHTTPLastVirusName_Object = MibScalar
aviHTTPLastVirusName = _AviHTTPLastVirusName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 1, 2),
    _AviHTTPLastVirusName_Type()
)
aviHTTPLastVirusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviHTTPLastVirusName.setStatus("current")
_AviHTTPLastVirusTime_Type = Integer32
_AviHTTPLastVirusTime_Object = MibScalar
aviHTTPLastVirusTime = _AviHTTPLastVirusTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 1, 3),
    _AviHTTPLastVirusTime_Type()
)
aviHTTPLastVirusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviHTTPLastVirusTime.setStatus("current")
_AviHTTPTopVirusesTable_Object = MibTable
aviHTTPTopVirusesTable = _AviHTTPTopVirusesTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 1, 4)
)
if mibBuilder.loadTexts:
    aviHTTPTopVirusesTable.setStatus("current")
_AviHTTPTopVirusesEntry_Object = MibTableRow
aviHTTPTopVirusesEntry = _AviHTTPTopVirusesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 1, 4, 1)
)
aviHTTPTopVirusesEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "aviHTTPTopVirusesIndex"),
)
if mibBuilder.loadTexts:
    aviHTTPTopVirusesEntry.setStatus("current")
_AviHTTPTopVirusesIndex_Type = Unsigned32
_AviHTTPTopVirusesIndex_Object = MibTableColumn
aviHTTPTopVirusesIndex = _AviHTTPTopVirusesIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 1, 4, 1, 1),
    _AviHTTPTopVirusesIndex_Type()
)
aviHTTPTopVirusesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviHTTPTopVirusesIndex.setStatus("current")
_AviHTTPTopVirusesName_Type = DisplayString
_AviHTTPTopVirusesName_Object = MibTableColumn
aviHTTPTopVirusesName = _AviHTTPTopVirusesName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 1, 4, 1, 2),
    _AviHTTPTopVirusesName_Type()
)
aviHTTPTopVirusesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviHTTPTopVirusesName.setStatus("current")
_AviHTTPTopVirusesCnt_Type = Integer32
_AviHTTPTopVirusesCnt_Object = MibTableColumn
aviHTTPTopVirusesCnt = _AviHTTPTopVirusesCnt_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 1, 4, 1, 3),
    _AviHTTPTopVirusesCnt_Type()
)
aviHTTPTopVirusesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviHTTPTopVirusesCnt.setStatus("current")
_AviServicesFTP_ObjectIdentity = ObjectIdentity
aviServicesFTP = _AviServicesFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 2)
)
_AviFTPState_Type = Integer32
_AviFTPState_Object = MibScalar
aviFTPState = _AviFTPState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 2, 1),
    _AviFTPState_Type()
)
aviFTPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviFTPState.setStatus("current")
_AviFTPLastVirusName_Type = DisplayString
_AviFTPLastVirusName_Object = MibScalar
aviFTPLastVirusName = _AviFTPLastVirusName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 2, 2),
    _AviFTPLastVirusName_Type()
)
aviFTPLastVirusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviFTPLastVirusName.setStatus("current")
_AviFTPLastVirusTime_Type = Integer32
_AviFTPLastVirusTime_Object = MibScalar
aviFTPLastVirusTime = _AviFTPLastVirusTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 2, 3),
    _AviFTPLastVirusTime_Type()
)
aviFTPLastVirusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviFTPLastVirusTime.setStatus("current")
_AviFTPTopVirusesTable_Object = MibTable
aviFTPTopVirusesTable = _AviFTPTopVirusesTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 2, 4)
)
if mibBuilder.loadTexts:
    aviFTPTopVirusesTable.setStatus("current")
_AviFTPTopVirusesEntry_Object = MibTableRow
aviFTPTopVirusesEntry = _AviFTPTopVirusesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 2, 4, 1)
)
aviFTPTopVirusesEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "aviFTPTopVirusesIndex"),
)
if mibBuilder.loadTexts:
    aviFTPTopVirusesEntry.setStatus("current")
_AviFTPTopVirusesIndex_Type = Unsigned32
_AviFTPTopVirusesIndex_Object = MibTableColumn
aviFTPTopVirusesIndex = _AviFTPTopVirusesIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 2, 4, 1, 1),
    _AviFTPTopVirusesIndex_Type()
)
aviFTPTopVirusesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviFTPTopVirusesIndex.setStatus("current")
_AviFTPTopVirusesName_Type = DisplayString
_AviFTPTopVirusesName_Object = MibTableColumn
aviFTPTopVirusesName = _AviFTPTopVirusesName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 2, 4, 1, 2),
    _AviFTPTopVirusesName_Type()
)
aviFTPTopVirusesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviFTPTopVirusesName.setStatus("current")
_AviFTPTopVirusesCnt_Type = Integer32
_AviFTPTopVirusesCnt_Object = MibTableColumn
aviFTPTopVirusesCnt = _AviFTPTopVirusesCnt_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 2, 4, 1, 3),
    _AviFTPTopVirusesCnt_Type()
)
aviFTPTopVirusesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviFTPTopVirusesCnt.setStatus("current")
_AviServicesSMTP_ObjectIdentity = ObjectIdentity
aviServicesSMTP = _AviServicesSMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 3)
)
_AviSMTPState_Type = Integer32
_AviSMTPState_Object = MibScalar
aviSMTPState = _AviSMTPState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 3, 1),
    _AviSMTPState_Type()
)
aviSMTPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviSMTPState.setStatus("current")
_AviSMTPLastVirusName_Type = DisplayString
_AviSMTPLastVirusName_Object = MibScalar
aviSMTPLastVirusName = _AviSMTPLastVirusName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 3, 2),
    _AviSMTPLastVirusName_Type()
)
aviSMTPLastVirusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviSMTPLastVirusName.setStatus("current")
_AviSMTPLastVirusTime_Type = Integer32
_AviSMTPLastVirusTime_Object = MibScalar
aviSMTPLastVirusTime = _AviSMTPLastVirusTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 3, 3),
    _AviSMTPLastVirusTime_Type()
)
aviSMTPLastVirusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviSMTPLastVirusTime.setStatus("current")
_AviSMTPTopVirusesTable_Object = MibTable
aviSMTPTopVirusesTable = _AviSMTPTopVirusesTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 3, 4)
)
if mibBuilder.loadTexts:
    aviSMTPTopVirusesTable.setStatus("current")
_AviSMTPTopVirusesEntry_Object = MibTableRow
aviSMTPTopVirusesEntry = _AviSMTPTopVirusesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 3, 4, 1)
)
aviSMTPTopVirusesEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "aviSMTPTopVirusesIndex"),
)
if mibBuilder.loadTexts:
    aviSMTPTopVirusesEntry.setStatus("current")
_AviSMTPTopVirusesIndex_Type = Unsigned32
_AviSMTPTopVirusesIndex_Object = MibTableColumn
aviSMTPTopVirusesIndex = _AviSMTPTopVirusesIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 3, 4, 1, 1),
    _AviSMTPTopVirusesIndex_Type()
)
aviSMTPTopVirusesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviSMTPTopVirusesIndex.setStatus("current")
_AviSMTPTopVirusesName_Type = DisplayString
_AviSMTPTopVirusesName_Object = MibTableColumn
aviSMTPTopVirusesName = _AviSMTPTopVirusesName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 3, 4, 1, 2),
    _AviSMTPTopVirusesName_Type()
)
aviSMTPTopVirusesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviSMTPTopVirusesName.setStatus("current")
_AviSMTPTopVirusesCnt_Type = Integer32
_AviSMTPTopVirusesCnt_Object = MibTableColumn
aviSMTPTopVirusesCnt = _AviSMTPTopVirusesCnt_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 3, 4, 1, 3),
    _AviSMTPTopVirusesCnt_Type()
)
aviSMTPTopVirusesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviSMTPTopVirusesCnt.setStatus("current")
_AviServicesPOP3_ObjectIdentity = ObjectIdentity
aviServicesPOP3 = _AviServicesPOP3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 4)
)
_AviPOP3State_Type = Integer32
_AviPOP3State_Object = MibScalar
aviPOP3State = _AviPOP3State_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 4, 1),
    _AviPOP3State_Type()
)
aviPOP3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviPOP3State.setStatus("current")
_AviPOP3LastVirusName_Type = DisplayString
_AviPOP3LastVirusName_Object = MibScalar
aviPOP3LastVirusName = _AviPOP3LastVirusName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 4, 2),
    _AviPOP3LastVirusName_Type()
)
aviPOP3LastVirusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviPOP3LastVirusName.setStatus("current")
_AviPOP3LastVirusTime_Type = Integer32
_AviPOP3LastVirusTime_Object = MibScalar
aviPOP3LastVirusTime = _AviPOP3LastVirusTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 4, 3),
    _AviPOP3LastVirusTime_Type()
)
aviPOP3LastVirusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviPOP3LastVirusTime.setStatus("current")
_AviPOP3TopVirusesTable_Object = MibTable
aviPOP3TopVirusesTable = _AviPOP3TopVirusesTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 4, 4)
)
if mibBuilder.loadTexts:
    aviPOP3TopVirusesTable.setStatus("current")
_AviPOP3TopVirusesEntry_Object = MibTableRow
aviPOP3TopVirusesEntry = _AviPOP3TopVirusesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 4, 4, 1)
)
aviPOP3TopVirusesEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "aviPOP3TopVirusesIndex"),
)
if mibBuilder.loadTexts:
    aviPOP3TopVirusesEntry.setStatus("current")
_AviPOP3TopVirusesIndex_Type = Unsigned32
_AviPOP3TopVirusesIndex_Object = MibTableColumn
aviPOP3TopVirusesIndex = _AviPOP3TopVirusesIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 4, 4, 1, 1),
    _AviPOP3TopVirusesIndex_Type()
)
aviPOP3TopVirusesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviPOP3TopVirusesIndex.setStatus("current")
_AviPOP3TopVirusesName_Type = DisplayString
_AviPOP3TopVirusesName_Object = MibTableColumn
aviPOP3TopVirusesName = _AviPOP3TopVirusesName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 4, 4, 1, 2),
    _AviPOP3TopVirusesName_Type()
)
aviPOP3TopVirusesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviPOP3TopVirusesName.setStatus("current")
_AviPOP3TopVirusesCnt_Type = Integer32
_AviPOP3TopVirusesCnt_Object = MibTableColumn
aviPOP3TopVirusesCnt = _AviPOP3TopVirusesCnt_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 4, 4, 4, 1, 3),
    _AviPOP3TopVirusesCnt_Type()
)
aviPOP3TopVirusesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviPOP3TopVirusesCnt.setStatus("current")
_AviStatCode_Type = Integer32
_AviStatCode_Object = MibScalar
aviStatCode = _AviStatCode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 101),
    _AviStatCode_Type()
)
aviStatCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviStatCode.setStatus("current")
_AviStatShortDescr_Type = DisplayString
_AviStatShortDescr_Object = MibScalar
aviStatShortDescr = _AviStatShortDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 102),
    _AviStatShortDescr_Type()
)
aviStatShortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviStatShortDescr.setStatus("current")
_AviStatLongDescr_Type = DisplayString
_AviStatLongDescr_Object = MibScalar
aviStatLongDescr = _AviStatLongDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 24, 103),
    _AviStatLongDescr_Type()
)
aviStatLongDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviStatLongDescr.setStatus("current")
_EventiaAnalyzer_ObjectIdentity = ObjectIdentity
eventiaAnalyzer = _EventiaAnalyzer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25)
)
_Cpsemd_ObjectIdentity = ObjectIdentity
cpsemd = _Cpsemd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 1)
)
_CpsemdProcAlive_Type = Integer32
_CpsemdProcAlive_Object = MibScalar
cpsemdProcAlive = _CpsemdProcAlive_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 1, 1),
    _CpsemdProcAlive_Type()
)
cpsemdProcAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsemdProcAlive.setStatus("current")
_CpsemdNewEventsHandled_Type = Integer32
_CpsemdNewEventsHandled_Object = MibScalar
cpsemdNewEventsHandled = _CpsemdNewEventsHandled_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 1, 2),
    _CpsemdNewEventsHandled_Type()
)
cpsemdNewEventsHandled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsemdNewEventsHandled.setStatus("current")
_CpsemdUpdatesHandled_Type = Integer32
_CpsemdUpdatesHandled_Object = MibScalar
cpsemdUpdatesHandled = _CpsemdUpdatesHandled_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 1, 3),
    _CpsemdUpdatesHandled_Type()
)
cpsemdUpdatesHandled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsemdUpdatesHandled.setStatus("current")
_CpsemdLastEventTime_Type = DisplayString
_CpsemdLastEventTime_Object = MibScalar
cpsemdLastEventTime = _CpsemdLastEventTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 1, 4),
    _CpsemdLastEventTime_Type()
)
cpsemdLastEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsemdLastEventTime.setStatus("current")
_CpsemdCurrentDBSize_Type = DisplayString
_CpsemdCurrentDBSize_Object = MibScalar
cpsemdCurrentDBSize = _CpsemdCurrentDBSize_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 1, 5),
    _CpsemdCurrentDBSize_Type()
)
cpsemdCurrentDBSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsemdCurrentDBSize.setStatus("current")
_CpsemdDBCapacity_Type = DisplayString
_CpsemdDBCapacity_Object = MibScalar
cpsemdDBCapacity = _CpsemdDBCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 1, 6),
    _CpsemdDBCapacity_Type()
)
cpsemdDBCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsemdDBCapacity.setStatus("current")
_CpsemdNumEvents_Type = Integer32
_CpsemdNumEvents_Object = MibScalar
cpsemdNumEvents = _CpsemdNumEvents_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 1, 7),
    _CpsemdNumEvents_Type()
)
cpsemdNumEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsemdNumEvents.setStatus("current")
_CpsemdDBDiskSpace_Type = DisplayString
_CpsemdDBDiskSpace_Object = MibScalar
cpsemdDBDiskSpace = _CpsemdDBDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 1, 8),
    _CpsemdDBDiskSpace_Type()
)
cpsemdDBDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsemdDBDiskSpace.setStatus("current")
_CpsemdCorrelationUnitTable_Object = MibTable
cpsemdCorrelationUnitTable = _CpsemdCorrelationUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 1, 9)
)
if mibBuilder.loadTexts:
    cpsemdCorrelationUnitTable.setStatus("current")
_CpsemdCorrelationUnitEntry_Object = MibTableRow
cpsemdCorrelationUnitEntry = _CpsemdCorrelationUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 1, 9, 1)
)
cpsemdCorrelationUnitEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "cpsemdCorrelationUnitIndex"),
)
if mibBuilder.loadTexts:
    cpsemdCorrelationUnitEntry.setStatus("current")
_CpsemdCorrelationUnitIndex_Type = Unsigned32
_CpsemdCorrelationUnitIndex_Object = MibTableColumn
cpsemdCorrelationUnitIndex = _CpsemdCorrelationUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 1, 9, 1, 1),
    _CpsemdCorrelationUnitIndex_Type()
)
cpsemdCorrelationUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsemdCorrelationUnitIndex.setStatus("current")
_CpsemdCorrelationUnitIP_Type = DisplayString
_CpsemdCorrelationUnitIP_Object = MibTableColumn
cpsemdCorrelationUnitIP = _CpsemdCorrelationUnitIP_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 1, 9, 1, 2),
    _CpsemdCorrelationUnitIP_Type()
)
cpsemdCorrelationUnitIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsemdCorrelationUnitIP.setStatus("current")
_CpsemdCorrelationUnitLastRcvdTime_Type = DisplayString
_CpsemdCorrelationUnitLastRcvdTime_Object = MibTableColumn
cpsemdCorrelationUnitLastRcvdTime = _CpsemdCorrelationUnitLastRcvdTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 1, 9, 1, 3),
    _CpsemdCorrelationUnitLastRcvdTime_Type()
)
cpsemdCorrelationUnitLastRcvdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsemdCorrelationUnitLastRcvdTime.setStatus("current")
_CpsemdCorrelationUnitNumEventsRcvd_Type = Integer32
_CpsemdCorrelationUnitNumEventsRcvd_Object = MibTableColumn
cpsemdCorrelationUnitNumEventsRcvd = _CpsemdCorrelationUnitNumEventsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 1, 9, 1, 4),
    _CpsemdCorrelationUnitNumEventsRcvd_Type()
)
cpsemdCorrelationUnitNumEventsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsemdCorrelationUnitNumEventsRcvd.setStatus("current")
_CpsemdConnectionDuration_Type = Integer32
_CpsemdConnectionDuration_Object = MibTableColumn
cpsemdConnectionDuration = _CpsemdConnectionDuration_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 1, 9, 1, 5),
    _CpsemdConnectionDuration_Type()
)
cpsemdConnectionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsemdConnectionDuration.setStatus("current")
_CpsemdDBIsFull_Type = Integer32
_CpsemdDBIsFull_Object = MibScalar
cpsemdDBIsFull = _CpsemdDBIsFull_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 1, 10),
    _CpsemdDBIsFull_Type()
)
cpsemdDBIsFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsemdDBIsFull.setStatus("current")
_CpsemdStatCode_Type = Integer32
_CpsemdStatCode_Object = MibScalar
cpsemdStatCode = _CpsemdStatCode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 1, 101),
    _CpsemdStatCode_Type()
)
cpsemdStatCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsemdStatCode.setStatus("current")
_CpsemdStatShortDescr_Type = DisplayString
_CpsemdStatShortDescr_Object = MibScalar
cpsemdStatShortDescr = _CpsemdStatShortDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 1, 102),
    _CpsemdStatShortDescr_Type()
)
cpsemdStatShortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsemdStatShortDescr.setStatus("current")
_CpsemdStatLongDescr_Type = DisplayString
_CpsemdStatLongDescr_Object = MibScalar
cpsemdStatLongDescr = _CpsemdStatLongDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 1, 103),
    _CpsemdStatLongDescr_Type()
)
cpsemdStatLongDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsemdStatLongDescr.setStatus("current")
_Cpsead_ObjectIdentity = ObjectIdentity
cpsead = _Cpsead_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2)
)
_CpseadProcAlive_Type = Integer32
_CpseadProcAlive_Object = MibScalar
cpseadProcAlive = _CpseadProcAlive_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2, 1),
    _CpseadProcAlive_Type()
)
cpseadProcAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpseadProcAlive.setStatus("current")
_CpseadConnectedToSem_Type = Integer32
_CpseadConnectedToSem_Object = MibScalar
cpseadConnectedToSem = _CpseadConnectedToSem_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2, 2),
    _CpseadConnectedToSem_Type()
)
cpseadConnectedToSem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpseadConnectedToSem.setStatus("current")
_CpseadNumProcessedLogs_Type = DisplayString
_CpseadNumProcessedLogs_Object = MibScalar
cpseadNumProcessedLogs = _CpseadNumProcessedLogs_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2, 3),
    _CpseadNumProcessedLogs_Type()
)
cpseadNumProcessedLogs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpseadNumProcessedLogs.setStatus("current")
_CpseadJobsTable_Object = MibTable
cpseadJobsTable = _CpseadJobsTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2, 4)
)
if mibBuilder.loadTexts:
    cpseadJobsTable.setStatus("current")
_CpseadJobsEntry_Object = MibTableRow
cpseadJobsEntry = _CpseadJobsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2, 4, 1)
)
cpseadJobsEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "cpseadJobIndex"),
)
if mibBuilder.loadTexts:
    cpseadJobsEntry.setStatus("current")
_CpseadJobIndex_Type = Unsigned32
_CpseadJobIndex_Object = MibTableColumn
cpseadJobIndex = _CpseadJobIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2, 4, 1, 1),
    _CpseadJobIndex_Type()
)
cpseadJobIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpseadJobIndex.setStatus("current")
_CpseadJobID_Type = DisplayString
_CpseadJobID_Object = MibTableColumn
cpseadJobID = _CpseadJobID_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2, 4, 1, 2),
    _CpseadJobID_Type()
)
cpseadJobID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpseadJobID.setStatus("current")
_CpseadJobName_Type = DisplayString
_CpseadJobName_Object = MibTableColumn
cpseadJobName = _CpseadJobName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2, 4, 1, 3),
    _CpseadJobName_Type()
)
cpseadJobName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpseadJobName.setStatus("current")
_CpseadJobState_Type = DisplayString
_CpseadJobState_Object = MibTableColumn
cpseadJobState = _CpseadJobState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2, 4, 1, 4),
    _CpseadJobState_Type()
)
cpseadJobState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpseadJobState.setStatus("current")
_CpseadJobIsOnline_Type = Integer32
_CpseadJobIsOnline_Object = MibTableColumn
cpseadJobIsOnline = _CpseadJobIsOnline_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2, 4, 1, 5),
    _CpseadJobIsOnline_Type()
)
cpseadJobIsOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpseadJobIsOnline.setStatus("current")
_CpseadJobLogServer_Type = DisplayString
_CpseadJobLogServer_Object = MibTableColumn
cpseadJobLogServer = _CpseadJobLogServer_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2, 4, 1, 6),
    _CpseadJobLogServer_Type()
)
cpseadJobLogServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpseadJobLogServer.setStatus("current")
_CpseadJobDataType_Type = DisplayString
_CpseadJobDataType_Object = MibTableColumn
cpseadJobDataType = _CpseadJobDataType_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2, 4, 1, 7),
    _CpseadJobDataType_Type()
)
cpseadJobDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpseadJobDataType.setStatus("current")
_CpseadConnectedToLogServer_Type = Integer32
_CpseadConnectedToLogServer_Object = MibTableColumn
cpseadConnectedToLogServer = _CpseadConnectedToLogServer_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2, 4, 1, 8),
    _CpseadConnectedToLogServer_Type()
)
cpseadConnectedToLogServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpseadConnectedToLogServer.setStatus("current")
_CpseadNumAnalyzedLogs_Type = DisplayString
_CpseadNumAnalyzedLogs_Object = MibTableColumn
cpseadNumAnalyzedLogs = _CpseadNumAnalyzedLogs_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2, 4, 1, 9),
    _CpseadNumAnalyzedLogs_Type()
)
cpseadNumAnalyzedLogs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpseadNumAnalyzedLogs.setStatus("current")
_CpseadFileName_Type = DisplayString
_CpseadFileName_Object = MibTableColumn
cpseadFileName = _CpseadFileName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2, 4, 1, 10),
    _CpseadFileName_Type()
)
cpseadFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpseadFileName.setStatus("current")
_CpseadFileCurrentPosition_Type = DisplayString
_CpseadFileCurrentPosition_Object = MibTableColumn
cpseadFileCurrentPosition = _CpseadFileCurrentPosition_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2, 4, 1, 11),
    _CpseadFileCurrentPosition_Type()
)
cpseadFileCurrentPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpseadFileCurrentPosition.setStatus("current")
_CpseadStateDescriptionCode_Type = DisplayString
_CpseadStateDescriptionCode_Object = MibTableColumn
cpseadStateDescriptionCode = _CpseadStateDescriptionCode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2, 4, 1, 12),
    _CpseadStateDescriptionCode_Type()
)
cpseadStateDescriptionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpseadStateDescriptionCode.setStatus("current")
_CpseadStateDescription_Type = DisplayString
_CpseadStateDescription_Object = MibTableColumn
cpseadStateDescription = _CpseadStateDescription_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2, 4, 1, 13),
    _CpseadStateDescription_Type()
)
cpseadStateDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpseadStateDescription.setStatus("current")
_CpseadNoFreeDiskSpace_Type = Integer32
_CpseadNoFreeDiskSpace_Object = MibScalar
cpseadNoFreeDiskSpace = _CpseadNoFreeDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2, 5),
    _CpseadNoFreeDiskSpace_Type()
)
cpseadNoFreeDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpseadNoFreeDiskSpace.setStatus("current")
_CpseadStatCode_Type = Integer32
_CpseadStatCode_Object = MibScalar
cpseadStatCode = _CpseadStatCode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2, 101),
    _CpseadStatCode_Type()
)
cpseadStatCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpseadStatCode.setStatus("current")
_CpseadStatShortDescr_Type = DisplayString
_CpseadStatShortDescr_Object = MibScalar
cpseadStatShortDescr = _CpseadStatShortDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2, 102),
    _CpseadStatShortDescr_Type()
)
cpseadStatShortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpseadStatShortDescr.setStatus("current")
_CpseadStatLongDescr_Type = DisplayString
_CpseadStatLongDescr_Object = MibScalar
cpseadStatLongDescr = _CpseadStatLongDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 25, 2, 103),
    _CpseadStatLongDescr_Type()
)
cpseadStatLongDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpseadStatLongDescr.setStatus("current")
_Uf_ObjectIdentity = ObjectIdentity
uf = _Uf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29)
)
_UfEngine_ObjectIdentity = ObjectIdentity
ufEngine = _UfEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 1)
)
_UfEngineName_Type = DisplayString
_UfEngineName_Object = MibScalar
ufEngineName = _UfEngineName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 1, 1),
    _UfEngineName_Type()
)
ufEngineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufEngineName.setStatus("current")
_UfEngineVer_Type = DisplayString
_UfEngineVer_Object = MibScalar
ufEngineVer = _UfEngineVer_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 1, 2),
    _UfEngineVer_Type()
)
ufEngineVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufEngineVer.setStatus("current")
_UfEngineDate_Type = Integer32
_UfEngineDate_Object = MibScalar
ufEngineDate = _UfEngineDate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 1, 3),
    _UfEngineDate_Type()
)
ufEngineDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufEngineDate.setStatus("current")
_UfSignatureDate_Type = Integer32
_UfSignatureDate_Object = MibScalar
ufSignatureDate = _UfSignatureDate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 1, 4),
    _UfSignatureDate_Type()
)
ufSignatureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufSignatureDate.setStatus("current")
_UfSignatureVer_Type = DisplayString
_UfSignatureVer_Object = MibScalar
ufSignatureVer = _UfSignatureVer_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 1, 5),
    _UfSignatureVer_Type()
)
ufSignatureVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufSignatureVer.setStatus("current")
_UfLastSigCheckTime_Type = Integer32
_UfLastSigCheckTime_Object = MibScalar
ufLastSigCheckTime = _UfLastSigCheckTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 1, 6),
    _UfLastSigCheckTime_Type()
)
ufLastSigCheckTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufLastSigCheckTime.setStatus("current")
_UfLastSigLocation_Type = DisplayString
_UfLastSigLocation_Object = MibScalar
ufLastSigLocation = _UfLastSigLocation_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 1, 7),
    _UfLastSigLocation_Type()
)
ufLastSigLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufLastSigLocation.setStatus("current")
_UfLastLicExp_Type = DisplayString
_UfLastLicExp_Object = MibScalar
ufLastLicExp = _UfLastLicExp_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 1, 8),
    _UfLastLicExp_Type()
)
ufLastLicExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufLastLicExp.setStatus("current")
_UfSS_ObjectIdentity = ObjectIdentity
ufSS = _UfSS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 2)
)
_UfIsMonitor_Type = DisplayString
_UfIsMonitor_Object = MibScalar
ufIsMonitor = _UfIsMonitor_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 2, 1),
    _UfIsMonitor_Type()
)
ufIsMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufIsMonitor.setStatus("current")
_UfScannedCnt_Type = Integer32
_UfScannedCnt_Object = MibScalar
ufScannedCnt = _UfScannedCnt_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 2, 2),
    _UfScannedCnt_Type()
)
ufScannedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufScannedCnt.setStatus("current")
_UfBlockedCnt_Type = Integer32
_UfBlockedCnt_Object = MibScalar
ufBlockedCnt = _UfBlockedCnt_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 2, 3),
    _UfBlockedCnt_Type()
)
ufBlockedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufBlockedCnt.setStatus("current")
_UfTopBlockedCatTable_Object = MibTable
ufTopBlockedCatTable = _UfTopBlockedCatTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 2, 4)
)
if mibBuilder.loadTexts:
    ufTopBlockedCatTable.setStatus("current")
_UfTopBlockedCatEntry_Object = MibTableRow
ufTopBlockedCatEntry = _UfTopBlockedCatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 2, 4, 1)
)
ufTopBlockedCatEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "ufTopBlockedCatIndex"),
)
if mibBuilder.loadTexts:
    ufTopBlockedCatEntry.setStatus("current")
_UfTopBlockedCatIndex_Type = Unsigned32
_UfTopBlockedCatIndex_Object = MibTableColumn
ufTopBlockedCatIndex = _UfTopBlockedCatIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 2, 4, 1, 1),
    _UfTopBlockedCatIndex_Type()
)
ufTopBlockedCatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufTopBlockedCatIndex.setStatus("current")
_UfTopBlockedCatName_Type = DisplayString
_UfTopBlockedCatName_Object = MibTableColumn
ufTopBlockedCatName = _UfTopBlockedCatName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 2, 4, 1, 2),
    _UfTopBlockedCatName_Type()
)
ufTopBlockedCatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufTopBlockedCatName.setStatus("current")
_UfTopBlockedCatCnt_Type = Integer32
_UfTopBlockedCatCnt_Object = MibTableColumn
ufTopBlockedCatCnt = _UfTopBlockedCatCnt_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 2, 4, 1, 3),
    _UfTopBlockedCatCnt_Type()
)
ufTopBlockedCatCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufTopBlockedCatCnt.setStatus("current")
_UfTopBlockedSiteTable_Object = MibTable
ufTopBlockedSiteTable = _UfTopBlockedSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 2, 5)
)
if mibBuilder.loadTexts:
    ufTopBlockedSiteTable.setStatus("current")
_UfTopBlockedSiteEntry_Object = MibTableRow
ufTopBlockedSiteEntry = _UfTopBlockedSiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 2, 5, 1)
)
ufTopBlockedSiteEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "ufTopBlockedSiteIndex"),
)
if mibBuilder.loadTexts:
    ufTopBlockedSiteEntry.setStatus("current")
_UfTopBlockedSiteIndex_Type = Unsigned32
_UfTopBlockedSiteIndex_Object = MibTableColumn
ufTopBlockedSiteIndex = _UfTopBlockedSiteIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 2, 5, 1, 1),
    _UfTopBlockedSiteIndex_Type()
)
ufTopBlockedSiteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufTopBlockedSiteIndex.setStatus("current")
_UfTopBlockedSiteName_Type = DisplayString
_UfTopBlockedSiteName_Object = MibTableColumn
ufTopBlockedSiteName = _UfTopBlockedSiteName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 2, 5, 1, 2),
    _UfTopBlockedSiteName_Type()
)
ufTopBlockedSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufTopBlockedSiteName.setStatus("current")
_UfTopBlockedSiteCnt_Type = Integer32
_UfTopBlockedSiteCnt_Object = MibTableColumn
ufTopBlockedSiteCnt = _UfTopBlockedSiteCnt_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 2, 5, 1, 3),
    _UfTopBlockedSiteCnt_Type()
)
ufTopBlockedSiteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufTopBlockedSiteCnt.setStatus("current")
_UfTopBlockedUserTable_Object = MibTable
ufTopBlockedUserTable = _UfTopBlockedUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 2, 6)
)
if mibBuilder.loadTexts:
    ufTopBlockedUserTable.setStatus("current")
_UfTopBlockedUserEntry_Object = MibTableRow
ufTopBlockedUserEntry = _UfTopBlockedUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 2, 6, 1)
)
ufTopBlockedUserEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "ufTopBlockedUserIndex"),
)
if mibBuilder.loadTexts:
    ufTopBlockedUserEntry.setStatus("current")
_UfTopBlockedUserIndex_Type = Unsigned32
_UfTopBlockedUserIndex_Object = MibTableColumn
ufTopBlockedUserIndex = _UfTopBlockedUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 2, 6, 1, 1),
    _UfTopBlockedUserIndex_Type()
)
ufTopBlockedUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufTopBlockedUserIndex.setStatus("current")
_UfTopBlockedUserName_Type = DisplayString
_UfTopBlockedUserName_Object = MibTableColumn
ufTopBlockedUserName = _UfTopBlockedUserName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 2, 6, 1, 2),
    _UfTopBlockedUserName_Type()
)
ufTopBlockedUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufTopBlockedUserName.setStatus("current")
_UfTopBlockedUserCnt_Type = Integer32
_UfTopBlockedUserCnt_Object = MibTableColumn
ufTopBlockedUserCnt = _UfTopBlockedUserCnt_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 2, 6, 1, 3),
    _UfTopBlockedUserCnt_Type()
)
ufTopBlockedUserCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufTopBlockedUserCnt.setStatus("current")
_UfStatCode_Type = Integer32
_UfStatCode_Object = MibScalar
ufStatCode = _UfStatCode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 101),
    _UfStatCode_Type()
)
ufStatCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufStatCode.setStatus("current")
_UfStatShortDescr_Type = DisplayString
_UfStatShortDescr_Object = MibScalar
ufStatShortDescr = _UfStatShortDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 102),
    _UfStatShortDescr_Type()
)
ufStatShortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufStatShortDescr.setStatus("current")
_UfStatLongDescr_Type = DisplayString
_UfStatLongDescr_Object = MibScalar
ufStatLongDescr = _UfStatLongDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 29, 103),
    _UfStatLongDescr_Type()
)
ufStatLongDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufStatLongDescr.setStatus("current")
_Ms_ObjectIdentity = ObjectIdentity
ms = _Ms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30)
)
_MsProductName_Type = DisplayString
_MsProductName_Object = MibScalar
msProductName = _MsProductName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 1),
    _MsProductName_Type()
)
msProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msProductName.setStatus("current")
_MsMajorVersion_Type = Integer32
_MsMajorVersion_Object = MibScalar
msMajorVersion = _MsMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 2),
    _MsMajorVersion_Type()
)
msMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msMajorVersion.setStatus("current")
_MsMinorVersion_Type = Integer32
_MsMinorVersion_Object = MibScalar
msMinorVersion = _MsMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 3),
    _MsMinorVersion_Type()
)
msMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msMinorVersion.setStatus("current")
_MsBuildNumber_Type = Integer32
_MsBuildNumber_Object = MibScalar
msBuildNumber = _MsBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 4),
    _MsBuildNumber_Type()
)
msBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msBuildNumber.setStatus("current")
_MsVersionStr_Type = DisplayString
_MsVersionStr_Object = MibScalar
msVersionStr = _MsVersionStr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 5),
    _MsVersionStr_Type()
)
msVersionStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msVersionStr.setStatus("current")
_MsSpam_ObjectIdentity = ObjectIdentity
msSpam = _MsSpam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 6)
)
_MsSpamNumScannedEmails_Type = Integer32
_MsSpamNumScannedEmails_Object = MibScalar
msSpamNumScannedEmails = _MsSpamNumScannedEmails_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 6, 1),
    _MsSpamNumScannedEmails_Type()
)
msSpamNumScannedEmails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSpamNumScannedEmails.setStatus("current")
_MsSpamNumSpamEmails_Type = Integer32
_MsSpamNumSpamEmails_Object = MibScalar
msSpamNumSpamEmails = _MsSpamNumSpamEmails_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 6, 2),
    _MsSpamNumSpamEmails_Type()
)
msSpamNumSpamEmails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSpamNumSpamEmails.setStatus("current")
_MsSpamNumHandledSpamEmails_Type = Integer32
_MsSpamNumHandledSpamEmails_Object = MibScalar
msSpamNumHandledSpamEmails = _MsSpamNumHandledSpamEmails_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 6, 3),
    _MsSpamNumHandledSpamEmails_Type()
)
msSpamNumHandledSpamEmails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSpamNumHandledSpamEmails.setStatus("current")
_MsSpamControls_ObjectIdentity = ObjectIdentity
msSpamControls = _MsSpamControls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 6, 4)
)
_MsSpamControlsSpamEngine_Type = Integer32
_MsSpamControlsSpamEngine_Object = MibScalar
msSpamControlsSpamEngine = _MsSpamControlsSpamEngine_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 6, 4, 1),
    _MsSpamControlsSpamEngine_Type()
)
msSpamControlsSpamEngine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSpamControlsSpamEngine.setStatus("current")
_MsSpamControlsIpRepuatation_Type = Integer32
_MsSpamControlsIpRepuatation_Object = MibScalar
msSpamControlsIpRepuatation = _MsSpamControlsIpRepuatation_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 6, 4, 2),
    _MsSpamControlsIpRepuatation_Type()
)
msSpamControlsIpRepuatation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSpamControlsIpRepuatation.setStatus("current")
_MsSpamControlsSPF_Type = Integer32
_MsSpamControlsSPF_Object = MibScalar
msSpamControlsSPF = _MsSpamControlsSPF_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 6, 4, 3),
    _MsSpamControlsSPF_Type()
)
msSpamControlsSPF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSpamControlsSPF.setStatus("current")
_MsSpamControlsDomainKeys_Type = Integer32
_MsSpamControlsDomainKeys_Object = MibScalar
msSpamControlsDomainKeys = _MsSpamControlsDomainKeys_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 6, 4, 4),
    _MsSpamControlsDomainKeys_Type()
)
msSpamControlsDomainKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSpamControlsDomainKeys.setStatus("current")
_MsSpamControlsRDNS_Type = Integer32
_MsSpamControlsRDNS_Object = MibScalar
msSpamControlsRDNS = _MsSpamControlsRDNS_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 6, 4, 5),
    _MsSpamControlsRDNS_Type()
)
msSpamControlsRDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSpamControlsRDNS.setStatus("current")
_MsSpamControlsRBL_Type = Integer32
_MsSpamControlsRBL_Object = MibScalar
msSpamControlsRBL = _MsSpamControlsRBL_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 6, 4, 6),
    _MsSpamControlsRBL_Type()
)
msSpamControlsRBL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSpamControlsRBL.setStatus("current")
_MsExpirationDate_Type = DisplayString
_MsExpirationDate_Object = MibScalar
msExpirationDate = _MsExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 7),
    _MsExpirationDate_Type()
)
msExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msExpirationDate.setStatus("current")
_MsEngineVer_Type = DisplayString
_MsEngineVer_Object = MibScalar
msEngineVer = _MsEngineVer_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 8),
    _MsEngineVer_Type()
)
msEngineVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msEngineVer.setStatus("current")
_MsEngineDate_Type = Integer32
_MsEngineDate_Object = MibScalar
msEngineDate = _MsEngineDate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 9),
    _MsEngineDate_Type()
)
msEngineDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msEngineDate.setStatus("current")
_MsStatCode_Type = Integer32
_MsStatCode_Object = MibScalar
msStatCode = _MsStatCode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 101),
    _MsStatCode_Type()
)
msStatCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msStatCode.setStatus("current")
_MsStatShortDescr_Type = DisplayString
_MsStatShortDescr_Object = MibScalar
msStatShortDescr = _MsStatShortDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 102),
    _MsStatShortDescr_Type()
)
msStatShortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msStatShortDescr.setStatus("current")
_MsStatLongDescr_Type = DisplayString
_MsStatLongDescr_Object = MibScalar
msStatLongDescr = _MsStatLongDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 103),
    _MsStatLongDescr_Type()
)
msStatLongDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msStatLongDescr.setStatus("current")
_MsServicePack_Type = DisplayString
_MsServicePack_Object = MibScalar
msServicePack = _MsServicePack_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 30, 999),
    _MsServicePack_Type()
)
msServicePack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msServicePack.setStatus("current")
_Voip_ObjectIdentity = ObjectIdentity
voip = _Voip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31)
)
_VoipProductName_Type = DisplayString
_VoipProductName_Object = MibScalar
voipProductName = _VoipProductName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 1),
    _VoipProductName_Type()
)
voipProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipProductName.setStatus("current")
_VoipMajorVersion_Type = Integer32
_VoipMajorVersion_Object = MibScalar
voipMajorVersion = _VoipMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 2),
    _VoipMajorVersion_Type()
)
voipMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipMajorVersion.setStatus("current")
_VoipMinorVersion_Type = Integer32
_VoipMinorVersion_Object = MibScalar
voipMinorVersion = _VoipMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 3),
    _VoipMinorVersion_Type()
)
voipMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipMinorVersion.setStatus("current")
_VoipBuildNumber_Type = Integer32
_VoipBuildNumber_Object = MibScalar
voipBuildNumber = _VoipBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 4),
    _VoipBuildNumber_Type()
)
voipBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipBuildNumber.setStatus("current")
_VoipVersionStr_Type = DisplayString
_VoipVersionStr_Object = MibScalar
voipVersionStr = _VoipVersionStr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 5),
    _VoipVersionStr_Type()
)
voipVersionStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipVersionStr.setStatus("current")
_VoipDOS_ObjectIdentity = ObjectIdentity
voipDOS = _VoipDOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 6)
)
_VoipDOSSip_ObjectIdentity = ObjectIdentity
voipDOSSip = _VoipDOSSip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 6, 1)
)
_VoipDOSSipNetwork_ObjectIdentity = ObjectIdentity
voipDOSSipNetwork = _VoipDOSSipNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 6, 1, 1)
)
_VoipDOSSipNetworkReqInterval_Type = Integer32
_VoipDOSSipNetworkReqInterval_Object = MibScalar
voipDOSSipNetworkReqInterval = _VoipDOSSipNetworkReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 6, 1, 1, 1),
    _VoipDOSSipNetworkReqInterval_Type()
)
voipDOSSipNetworkReqInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipDOSSipNetworkReqInterval.setStatus("current")
_VoipDOSSipNetworkReqConfThreshold_Type = Integer32
_VoipDOSSipNetworkReqConfThreshold_Object = MibScalar
voipDOSSipNetworkReqConfThreshold = _VoipDOSSipNetworkReqConfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 6, 1, 1, 2),
    _VoipDOSSipNetworkReqConfThreshold_Type()
)
voipDOSSipNetworkReqConfThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipDOSSipNetworkReqConfThreshold.setStatus("current")
_VoipDOSSipNetworkReqCurrentVal_Type = Integer32
_VoipDOSSipNetworkReqCurrentVal_Object = MibScalar
voipDOSSipNetworkReqCurrentVal = _VoipDOSSipNetworkReqCurrentVal_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 6, 1, 1, 3),
    _VoipDOSSipNetworkReqCurrentVal_Type()
)
voipDOSSipNetworkReqCurrentVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipDOSSipNetworkReqCurrentVal.setStatus("current")
_VoipDOSSipNetworkRegInterval_Type = Integer32
_VoipDOSSipNetworkRegInterval_Object = MibScalar
voipDOSSipNetworkRegInterval = _VoipDOSSipNetworkRegInterval_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 6, 1, 1, 4),
    _VoipDOSSipNetworkRegInterval_Type()
)
voipDOSSipNetworkRegInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipDOSSipNetworkRegInterval.setStatus("current")
_VoipDOSSipNetworkRegConfThreshold_Type = Integer32
_VoipDOSSipNetworkRegConfThreshold_Object = MibScalar
voipDOSSipNetworkRegConfThreshold = _VoipDOSSipNetworkRegConfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 6, 1, 1, 5),
    _VoipDOSSipNetworkRegConfThreshold_Type()
)
voipDOSSipNetworkRegConfThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipDOSSipNetworkRegConfThreshold.setStatus("current")
_VoipDOSSipNetworkRegCurrentVal_Type = Integer32
_VoipDOSSipNetworkRegCurrentVal_Object = MibScalar
voipDOSSipNetworkRegCurrentVal = _VoipDOSSipNetworkRegCurrentVal_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 6, 1, 1, 6),
    _VoipDOSSipNetworkRegCurrentVal_Type()
)
voipDOSSipNetworkRegCurrentVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipDOSSipNetworkRegCurrentVal.setStatus("current")
_VoipDOSSipNetworkCallInitInterval_Type = Integer32
_VoipDOSSipNetworkCallInitInterval_Object = MibScalar
voipDOSSipNetworkCallInitInterval = _VoipDOSSipNetworkCallInitInterval_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 6, 1, 1, 7),
    _VoipDOSSipNetworkCallInitInterval_Type()
)
voipDOSSipNetworkCallInitInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipDOSSipNetworkCallInitInterval.setStatus("current")
_VoipDOSSipNetworkCallInitConfThreshold_Type = Integer32
_VoipDOSSipNetworkCallInitConfThreshold_Object = MibScalar
voipDOSSipNetworkCallInitConfThreshold = _VoipDOSSipNetworkCallInitConfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 6, 1, 1, 8),
    _VoipDOSSipNetworkCallInitConfThreshold_Type()
)
voipDOSSipNetworkCallInitConfThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipDOSSipNetworkCallInitConfThreshold.setStatus("current")
_VoipDOSSipNetworkCallInitICurrentVal_Type = Integer32
_VoipDOSSipNetworkCallInitICurrentVal_Object = MibScalar
voipDOSSipNetworkCallInitICurrentVal = _VoipDOSSipNetworkCallInitICurrentVal_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 6, 1, 1, 9),
    _VoipDOSSipNetworkCallInitICurrentVal_Type()
)
voipDOSSipNetworkCallInitICurrentVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipDOSSipNetworkCallInitICurrentVal.setStatus("current")
_VoipDOSSipRateLimitingTable_Object = MibTable
voipDOSSipRateLimitingTable = _VoipDOSSipRateLimitingTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 6, 1, 2)
)
if mibBuilder.loadTexts:
    voipDOSSipRateLimitingTable.setStatus("current")
_VoipDOSSipRateLimitingEntry_Object = MibTableRow
voipDOSSipRateLimitingEntry = _VoipDOSSipRateLimitingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 6, 1, 2, 1)
)
voipDOSSipRateLimitingEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "voipDOSSipRateLimitingTableIndex"),
)
if mibBuilder.loadTexts:
    voipDOSSipRateLimitingEntry.setStatus("current")
_VoipDOSSipRateLimitingTableIndex_Type = Unsigned32
_VoipDOSSipRateLimitingTableIndex_Object = MibTableColumn
voipDOSSipRateLimitingTableIndex = _VoipDOSSipRateLimitingTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 6, 1, 2, 1, 1),
    _VoipDOSSipRateLimitingTableIndex_Type()
)
voipDOSSipRateLimitingTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipDOSSipRateLimitingTableIndex.setStatus("current")
_VoipDOSSipRateLimitingTableIpAddress_Type = Integer32
_VoipDOSSipRateLimitingTableIpAddress_Object = MibTableColumn
voipDOSSipRateLimitingTableIpAddress = _VoipDOSSipRateLimitingTableIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 6, 1, 2, 1, 2),
    _VoipDOSSipRateLimitingTableIpAddress_Type()
)
voipDOSSipRateLimitingTableIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipDOSSipRateLimitingTableIpAddress.setStatus("current")
_VoipDOSSipRateLimitingTableInterval_Type = Integer32
_VoipDOSSipRateLimitingTableInterval_Object = MibTableColumn
voipDOSSipRateLimitingTableInterval = _VoipDOSSipRateLimitingTableInterval_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 6, 1, 2, 1, 3),
    _VoipDOSSipRateLimitingTableInterval_Type()
)
voipDOSSipRateLimitingTableInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipDOSSipRateLimitingTableInterval.setStatus("current")
_VoipDOSSipRateLimitingTableConfThreshold_Type = Integer32
_VoipDOSSipRateLimitingTableConfThreshold_Object = MibTableColumn
voipDOSSipRateLimitingTableConfThreshold = _VoipDOSSipRateLimitingTableConfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 6, 1, 2, 1, 4),
    _VoipDOSSipRateLimitingTableConfThreshold_Type()
)
voipDOSSipRateLimitingTableConfThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipDOSSipRateLimitingTableConfThreshold.setStatus("current")
_VoipDOSSipRateLimitingTableNumDOSSipRequests_Type = Integer32
_VoipDOSSipRateLimitingTableNumDOSSipRequests_Object = MibTableColumn
voipDOSSipRateLimitingTableNumDOSSipRequests = _VoipDOSSipRateLimitingTableNumDOSSipRequests_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 6, 1, 2, 1, 5),
    _VoipDOSSipRateLimitingTableNumDOSSipRequests_Type()
)
voipDOSSipRateLimitingTableNumDOSSipRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipDOSSipRateLimitingTableNumDOSSipRequests.setStatus("current")
_VoipDOSSipRateLimitingTableNumTrustedRequests_Type = Integer32
_VoipDOSSipRateLimitingTableNumTrustedRequests_Object = MibTableColumn
voipDOSSipRateLimitingTableNumTrustedRequests = _VoipDOSSipRateLimitingTableNumTrustedRequests_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 6, 1, 2, 1, 6),
    _VoipDOSSipRateLimitingTableNumTrustedRequests_Type()
)
voipDOSSipRateLimitingTableNumTrustedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipDOSSipRateLimitingTableNumTrustedRequests.setStatus("current")
_VoipDOSSipRateLimitingTableNumNonTrustedRequests_Type = Integer32
_VoipDOSSipRateLimitingTableNumNonTrustedRequests_Object = MibTableColumn
voipDOSSipRateLimitingTableNumNonTrustedRequests = _VoipDOSSipRateLimitingTableNumNonTrustedRequests_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 6, 1, 2, 1, 7),
    _VoipDOSSipRateLimitingTableNumNonTrustedRequests_Type()
)
voipDOSSipRateLimitingTableNumNonTrustedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipDOSSipRateLimitingTableNumNonTrustedRequests.setStatus("current")
_VoipDOSSipRateLimitingTableNumRequestsfromServers_Type = Integer32
_VoipDOSSipRateLimitingTableNumRequestsfromServers_Object = MibTableColumn
voipDOSSipRateLimitingTableNumRequestsfromServers = _VoipDOSSipRateLimitingTableNumRequestsfromServers_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 6, 1, 2, 1, 8),
    _VoipDOSSipRateLimitingTableNumRequestsfromServers_Type()
)
voipDOSSipRateLimitingTableNumRequestsfromServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipDOSSipRateLimitingTableNumRequestsfromServers.setStatus("current")
_VoipCAC_ObjectIdentity = ObjectIdentity
voipCAC = _VoipCAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 7)
)
_VoipCACConcurrentCalls_ObjectIdentity = ObjectIdentity
voipCACConcurrentCalls = _VoipCACConcurrentCalls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 7, 1)
)
_VoipCACConcurrentCallsConfThreshold_Type = Integer32
_VoipCACConcurrentCallsConfThreshold_Object = MibScalar
voipCACConcurrentCallsConfThreshold = _VoipCACConcurrentCallsConfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 7, 1, 1),
    _VoipCACConcurrentCallsConfThreshold_Type()
)
voipCACConcurrentCallsConfThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipCACConcurrentCallsConfThreshold.setStatus("current")
_VoipCACConcurrentCallsCurrentVal_Type = Integer32
_VoipCACConcurrentCallsCurrentVal_Object = MibScalar
voipCACConcurrentCallsCurrentVal = _VoipCACConcurrentCallsCurrentVal_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 7, 1, 2),
    _VoipCACConcurrentCallsCurrentVal_Type()
)
voipCACConcurrentCallsCurrentVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipCACConcurrentCallsCurrentVal.setStatus("current")
_VoipStatCode_Type = Integer32
_VoipStatCode_Object = MibScalar
voipStatCode = _VoipStatCode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 101),
    _VoipStatCode_Type()
)
voipStatCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipStatCode.setStatus("current")
_VoipStatShortDescr_Type = DisplayString
_VoipStatShortDescr_Object = MibScalar
voipStatShortDescr = _VoipStatShortDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 102),
    _VoipStatShortDescr_Type()
)
voipStatShortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipStatShortDescr.setStatus("current")
_VoipStatLongDescr_Type = DisplayString
_VoipStatLongDescr_Object = MibScalar
voipStatLongDescr = _VoipStatLongDescr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 103),
    _VoipStatLongDescr_Type()
)
voipStatLongDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipStatLongDescr.setStatus("current")
_VoipServicePack_Type = DisplayString
_VoipServicePack_Object = MibScalar
voipServicePack = _VoipServicePack_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 31, 999),
    _VoipServicePack_Type()
)
voipServicePack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipServicePack.setStatus("current")
_Sxl_ObjectIdentity = ObjectIdentity
sxl = _Sxl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 36)
)
_FwSXLGroup_ObjectIdentity = ObjectIdentity
fwSXLGroup = _FwSXLGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 36, 1)
)


class _FwSXLStatus_Type(Integer32):
    """Custom type fwSXLStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_FwSXLStatus_Type.__name__ = "Integer32"
_FwSXLStatus_Object = MibScalar
fwSXLStatus = _FwSXLStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 36, 1, 1),
    _FwSXLStatus_Type()
)
fwSXLStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSXLStatus.setStatus("current")
_FwSXLConnsExisting_Type = Integer32
_FwSXLConnsExisting_Object = MibScalar
fwSXLConnsExisting = _FwSXLConnsExisting_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 36, 1, 2),
    _FwSXLConnsExisting_Type()
)
fwSXLConnsExisting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSXLConnsExisting.setStatus("current")
_FwSXLConnsAdded_Type = Integer32
_FwSXLConnsAdded_Object = MibScalar
fwSXLConnsAdded = _FwSXLConnsAdded_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 36, 1, 3),
    _FwSXLConnsAdded_Type()
)
fwSXLConnsAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSXLConnsAdded.setStatus("current")
_FwSXLConnsDeleted_Type = Integer32
_FwSXLConnsDeleted_Object = MibScalar
fwSXLConnsDeleted = _FwSXLConnsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 36, 1, 4),
    _FwSXLConnsDeleted_Type()
)
fwSXLConnsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwSXLConnsDeleted.setStatus("current")
_IdentityAwareness_ObjectIdentity = ObjectIdentity
identityAwareness = _IdentityAwareness_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38)
)
_IdentityAwarenessProductName_Type = DisplayString
_IdentityAwarenessProductName_Object = MibScalar
identityAwarenessProductName = _IdentityAwarenessProductName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 1),
    _IdentityAwarenessProductName_Type()
)
identityAwarenessProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessProductName.setStatus("current")
_IdentityAwarenessAuthUsers_Type = Integer32
_IdentityAwarenessAuthUsers_Object = MibScalar
identityAwarenessAuthUsers = _IdentityAwarenessAuthUsers_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 2),
    _IdentityAwarenessAuthUsers_Type()
)
identityAwarenessAuthUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessAuthUsers.setStatus("current")
_IdentityAwarenessUnAuthUsers_Type = Integer32
_IdentityAwarenessUnAuthUsers_Object = MibScalar
identityAwarenessUnAuthUsers = _IdentityAwarenessUnAuthUsers_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 3),
    _IdentityAwarenessUnAuthUsers_Type()
)
identityAwarenessUnAuthUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessUnAuthUsers.setStatus("current")
_IdentityAwarenessAuthUsersKerberos_Type = Integer32
_IdentityAwarenessAuthUsersKerberos_Object = MibScalar
identityAwarenessAuthUsersKerberos = _IdentityAwarenessAuthUsersKerberos_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 4),
    _IdentityAwarenessAuthUsersKerberos_Type()
)
identityAwarenessAuthUsersKerberos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessAuthUsersKerberos.setStatus("current")
_IdentityAwarenessAuthMachKerberos_Type = Integer32
_IdentityAwarenessAuthMachKerberos_Object = MibScalar
identityAwarenessAuthMachKerberos = _IdentityAwarenessAuthMachKerberos_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 5),
    _IdentityAwarenessAuthMachKerberos_Type()
)
identityAwarenessAuthMachKerberos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessAuthMachKerberos.setStatus("current")
_IdentityAwarenessAuthUsersPass_Type = Integer32
_IdentityAwarenessAuthUsersPass_Object = MibScalar
identityAwarenessAuthUsersPass = _IdentityAwarenessAuthUsersPass_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 6),
    _IdentityAwarenessAuthUsersPass_Type()
)
identityAwarenessAuthUsersPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessAuthUsersPass.setStatus("current")
_IdentityAwarenessAuthUsersADQuery_Type = Integer32
_IdentityAwarenessAuthUsersADQuery_Object = MibScalar
identityAwarenessAuthUsersADQuery = _IdentityAwarenessAuthUsersADQuery_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 7),
    _IdentityAwarenessAuthUsersADQuery_Type()
)
identityAwarenessAuthUsersADQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessAuthUsersADQuery.setStatus("current")
_IdentityAwarenessAuthMachADQuery_Type = Integer32
_IdentityAwarenessAuthMachADQuery_Object = MibScalar
identityAwarenessAuthMachADQuery = _IdentityAwarenessAuthMachADQuery_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 8),
    _IdentityAwarenessAuthMachADQuery_Type()
)
identityAwarenessAuthMachADQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessAuthMachADQuery.setStatus("current")
_IdentityAwarenessLoggedInAgent_Type = Integer32
_IdentityAwarenessLoggedInAgent_Object = MibScalar
identityAwarenessLoggedInAgent = _IdentityAwarenessLoggedInAgent_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 9),
    _IdentityAwarenessLoggedInAgent_Type()
)
identityAwarenessLoggedInAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessLoggedInAgent.setStatus("current")
_IdentityAwarenessLoggedInCaptivePortal_Type = Integer32
_IdentityAwarenessLoggedInCaptivePortal_Object = MibScalar
identityAwarenessLoggedInCaptivePortal = _IdentityAwarenessLoggedInCaptivePortal_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 10),
    _IdentityAwarenessLoggedInCaptivePortal_Type()
)
identityAwarenessLoggedInCaptivePortal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessLoggedInCaptivePortal.setStatus("current")
_IdentityAwarenessLoggedInADQuery_Type = Integer32
_IdentityAwarenessLoggedInADQuery_Object = MibScalar
identityAwarenessLoggedInADQuery = _IdentityAwarenessLoggedInADQuery_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 11),
    _IdentityAwarenessLoggedInADQuery_Type()
)
identityAwarenessLoggedInADQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessLoggedInADQuery.setStatus("current")
_IdentityAwarenessAntiSpoffProtection_Type = Integer32
_IdentityAwarenessAntiSpoffProtection_Object = MibScalar
identityAwarenessAntiSpoffProtection = _IdentityAwarenessAntiSpoffProtection_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 12),
    _IdentityAwarenessAntiSpoffProtection_Type()
)
identityAwarenessAntiSpoffProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessAntiSpoffProtection.setStatus("current")
_IdentityAwarenessSuccUserLoginKerberos_Type = Integer32
_IdentityAwarenessSuccUserLoginKerberos_Object = MibScalar
identityAwarenessSuccUserLoginKerberos = _IdentityAwarenessSuccUserLoginKerberos_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 13),
    _IdentityAwarenessSuccUserLoginKerberos_Type()
)
identityAwarenessSuccUserLoginKerberos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessSuccUserLoginKerberos.setStatus("current")
_IdentityAwarenessSuccMachLoginKerberos_Type = Integer32
_IdentityAwarenessSuccMachLoginKerberos_Object = MibScalar
identityAwarenessSuccMachLoginKerberos = _IdentityAwarenessSuccMachLoginKerberos_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 14),
    _IdentityAwarenessSuccMachLoginKerberos_Type()
)
identityAwarenessSuccMachLoginKerberos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessSuccMachLoginKerberos.setStatus("current")
_IdentityAwarenessSuccUserLoginPass_Type = Integer32
_IdentityAwarenessSuccUserLoginPass_Object = MibScalar
identityAwarenessSuccUserLoginPass = _IdentityAwarenessSuccUserLoginPass_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 15),
    _IdentityAwarenessSuccUserLoginPass_Type()
)
identityAwarenessSuccUserLoginPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessSuccUserLoginPass.setStatus("current")
_IdentityAwarenessSuccUserLoginADQuery_Type = Integer32
_IdentityAwarenessSuccUserLoginADQuery_Object = MibScalar
identityAwarenessSuccUserLoginADQuery = _IdentityAwarenessSuccUserLoginADQuery_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 16),
    _IdentityAwarenessSuccUserLoginADQuery_Type()
)
identityAwarenessSuccUserLoginADQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessSuccUserLoginADQuery.setStatus("current")
_IdentityAwarenessSuccMachLoginADQuery_Type = Integer32
_IdentityAwarenessSuccMachLoginADQuery_Object = MibScalar
identityAwarenessSuccMachLoginADQuery = _IdentityAwarenessSuccMachLoginADQuery_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 17),
    _IdentityAwarenessSuccMachLoginADQuery_Type()
)
identityAwarenessSuccMachLoginADQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessSuccMachLoginADQuery.setStatus("current")
_IdentityAwarenessUnSuccUserLoginKerberos_Type = Integer32
_IdentityAwarenessUnSuccUserLoginKerberos_Object = MibScalar
identityAwarenessUnSuccUserLoginKerberos = _IdentityAwarenessUnSuccUserLoginKerberos_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 18),
    _IdentityAwarenessUnSuccUserLoginKerberos_Type()
)
identityAwarenessUnSuccUserLoginKerberos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessUnSuccUserLoginKerberos.setStatus("current")
_IdentityAwarenessUnSuccMachLoginKerberos_Type = Integer32
_IdentityAwarenessUnSuccMachLoginKerberos_Object = MibScalar
identityAwarenessUnSuccMachLoginKerberos = _IdentityAwarenessUnSuccMachLoginKerberos_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 19),
    _IdentityAwarenessUnSuccMachLoginKerberos_Type()
)
identityAwarenessUnSuccMachLoginKerberos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessUnSuccMachLoginKerberos.setStatus("current")
_IdentityAwarenessUnSuccUserLoginPass_Type = Integer32
_IdentityAwarenessUnSuccUserLoginPass_Object = MibScalar
identityAwarenessUnSuccUserLoginPass = _IdentityAwarenessUnSuccUserLoginPass_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 20),
    _IdentityAwarenessUnSuccUserLoginPass_Type()
)
identityAwarenessUnSuccUserLoginPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessUnSuccUserLoginPass.setStatus("current")
_IdentityAwarenessSuccUserLDAP_Type = Integer32
_IdentityAwarenessSuccUserLDAP_Object = MibScalar
identityAwarenessSuccUserLDAP = _IdentityAwarenessSuccUserLDAP_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 21),
    _IdentityAwarenessSuccUserLDAP_Type()
)
identityAwarenessSuccUserLDAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessSuccUserLDAP.setStatus("current")
_IdentityAwarenessUnSuccUserLDAP_Type = Integer32
_IdentityAwarenessUnSuccUserLDAP_Object = MibScalar
identityAwarenessUnSuccUserLDAP = _IdentityAwarenessUnSuccUserLDAP_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 22),
    _IdentityAwarenessUnSuccUserLDAP_Type()
)
identityAwarenessUnSuccUserLDAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessUnSuccUserLDAP.setStatus("current")
_IdentityAwarenessDataTrans_Type = Integer32
_IdentityAwarenessDataTrans_Object = MibScalar
identityAwarenessDataTrans = _IdentityAwarenessDataTrans_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 23),
    _IdentityAwarenessDataTrans_Type()
)
identityAwarenessDataTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessDataTrans.setStatus("current")
_IdentityAwarenessDistributedEnvTable_Object = MibTable
identityAwarenessDistributedEnvTable = _IdentityAwarenessDistributedEnvTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 24)
)
if mibBuilder.loadTexts:
    identityAwarenessDistributedEnvTable.setStatus("current")
_IdentityAwarenessDistributedEnvEntry_Object = MibTableRow
identityAwarenessDistributedEnvEntry = _IdentityAwarenessDistributedEnvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 24, 1)
)
identityAwarenessDistributedEnvEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "identityAwarenessDistributedEnvTableIndex"),
)
if mibBuilder.loadTexts:
    identityAwarenessDistributedEnvEntry.setStatus("current")
_IdentityAwarenessDistributedEnvTableIndex_Type = Unsigned32
_IdentityAwarenessDistributedEnvTableIndex_Object = MibTableColumn
identityAwarenessDistributedEnvTableIndex = _IdentityAwarenessDistributedEnvTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 24, 1, 1),
    _IdentityAwarenessDistributedEnvTableIndex_Type()
)
identityAwarenessDistributedEnvTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessDistributedEnvTableIndex.setStatus("current")
_IdentityAwarenessDistributedEnvTableGwName_Type = DisplayString
_IdentityAwarenessDistributedEnvTableGwName_Object = MibTableColumn
identityAwarenessDistributedEnvTableGwName = _IdentityAwarenessDistributedEnvTableGwName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 24, 1, 2),
    _IdentityAwarenessDistributedEnvTableGwName_Type()
)
identityAwarenessDistributedEnvTableGwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessDistributedEnvTableGwName.setStatus("current")
_IdentityAwarenessDistributedEnvTableDisconnections_Type = Integer32
_IdentityAwarenessDistributedEnvTableDisconnections_Object = MibTableColumn
identityAwarenessDistributedEnvTableDisconnections = _IdentityAwarenessDistributedEnvTableDisconnections_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 24, 1, 3),
    _IdentityAwarenessDistributedEnvTableDisconnections_Type()
)
identityAwarenessDistributedEnvTableDisconnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessDistributedEnvTableDisconnections.setStatus("current")
_IdentityAwarenessDistributedEnvTableBruteForceAtt_Type = Integer32
_IdentityAwarenessDistributedEnvTableBruteForceAtt_Object = MibTableColumn
identityAwarenessDistributedEnvTableBruteForceAtt = _IdentityAwarenessDistributedEnvTableBruteForceAtt_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 24, 1, 4),
    _IdentityAwarenessDistributedEnvTableBruteForceAtt_Type()
)
identityAwarenessDistributedEnvTableBruteForceAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessDistributedEnvTableBruteForceAtt.setStatus("current")
_IdentityAwarenessDistributedEnvTableStatus_Type = Integer32
_IdentityAwarenessDistributedEnvTableStatus_Object = MibTableColumn
identityAwarenessDistributedEnvTableStatus = _IdentityAwarenessDistributedEnvTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 24, 1, 5),
    _IdentityAwarenessDistributedEnvTableStatus_Type()
)
identityAwarenessDistributedEnvTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessDistributedEnvTableStatus.setStatus("current")
_IdentityAwarenessDistributedEnvTableIsLocal_Type = Integer32
_IdentityAwarenessDistributedEnvTableIsLocal_Object = MibTableColumn
identityAwarenessDistributedEnvTableIsLocal = _IdentityAwarenessDistributedEnvTableIsLocal_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 24, 1, 6),
    _IdentityAwarenessDistributedEnvTableIsLocal_Type()
)
identityAwarenessDistributedEnvTableIsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessDistributedEnvTableIsLocal.setStatus("current")
_IdentityAwarenessADQueryStatusTable_Object = MibTable
identityAwarenessADQueryStatusTable = _IdentityAwarenessADQueryStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 25)
)
if mibBuilder.loadTexts:
    identityAwarenessADQueryStatusTable.setStatus("current")
_IdentityAwarenessADQueryStatusEntry_Object = MibTableRow
identityAwarenessADQueryStatusEntry = _IdentityAwarenessADQueryStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 25, 1)
)
identityAwarenessADQueryStatusEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "identityAwarenessADQueryStatusTableIndex"),
)
if mibBuilder.loadTexts:
    identityAwarenessADQueryStatusEntry.setStatus("current")
_IdentityAwarenessADQueryStatusTableIndex_Type = Unsigned32
_IdentityAwarenessADQueryStatusTableIndex_Object = MibTableColumn
identityAwarenessADQueryStatusTableIndex = _IdentityAwarenessADQueryStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 25, 1, 1),
    _IdentityAwarenessADQueryStatusTableIndex_Type()
)
identityAwarenessADQueryStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessADQueryStatusTableIndex.setStatus("current")
_IdentityAwarenessADQueryStatusCurrStatus_Type = Integer32
_IdentityAwarenessADQueryStatusCurrStatus_Object = MibTableColumn
identityAwarenessADQueryStatusCurrStatus = _IdentityAwarenessADQueryStatusCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 25, 1, 2),
    _IdentityAwarenessADQueryStatusCurrStatus_Type()
)
identityAwarenessADQueryStatusCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessADQueryStatusCurrStatus.setStatus("current")
_IdentityAwarenessADQueryStatusDomainName_Type = DisplayString
_IdentityAwarenessADQueryStatusDomainName_Object = MibTableColumn
identityAwarenessADQueryStatusDomainName = _IdentityAwarenessADQueryStatusDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 25, 1, 3),
    _IdentityAwarenessADQueryStatusDomainName_Type()
)
identityAwarenessADQueryStatusDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessADQueryStatusDomainName.setStatus("current")
_IdentityAwarenessADQueryStatusDomainIP_Type = IpAddress
_IdentityAwarenessADQueryStatusDomainIP_Object = MibTableColumn
identityAwarenessADQueryStatusDomainIP = _IdentityAwarenessADQueryStatusDomainIP_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 25, 1, 4),
    _IdentityAwarenessADQueryStatusDomainIP_Type()
)
identityAwarenessADQueryStatusDomainIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessADQueryStatusDomainIP.setStatus("current")
_IdentityAwarenessADQueryStatusEvents_Type = Integer32
_IdentityAwarenessADQueryStatusEvents_Object = MibTableColumn
identityAwarenessADQueryStatusEvents = _IdentityAwarenessADQueryStatusEvents_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 25, 1, 5),
    _IdentityAwarenessADQueryStatusEvents_Type()
)
identityAwarenessADQueryStatusEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessADQueryStatusEvents.setStatus("current")
_IdentityAwarenessStatus_Type = Integer32
_IdentityAwarenessStatus_Object = MibScalar
identityAwarenessStatus = _IdentityAwarenessStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 101),
    _IdentityAwarenessStatus_Type()
)
identityAwarenessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessStatus.setStatus("current")
_IdentityAwarenessStatusShortDesc_Type = DisplayString
_IdentityAwarenessStatusShortDesc_Object = MibScalar
identityAwarenessStatusShortDesc = _IdentityAwarenessStatusShortDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 102),
    _IdentityAwarenessStatusShortDesc_Type()
)
identityAwarenessStatusShortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessStatusShortDesc.setStatus("current")
_IdentityAwarenessStatusLongDesc_Type = DisplayString
_IdentityAwarenessStatusLongDesc_Object = MibScalar
identityAwarenessStatusLongDesc = _IdentityAwarenessStatusLongDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 38, 103),
    _IdentityAwarenessStatusLongDesc_Type()
)
identityAwarenessStatusLongDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identityAwarenessStatusLongDesc.setStatus("current")
_ApplicationControl_ObjectIdentity = ObjectIdentity
applicationControl = _ApplicationControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 39)
)
_ApplicationControlSubscription_ObjectIdentity = ObjectIdentity
applicationControlSubscription = _ApplicationControlSubscription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 39, 1)
)
_ApplicationControlSubscriptionStatus_Type = DisplayString
_ApplicationControlSubscriptionStatus_Object = MibScalar
applicationControlSubscriptionStatus = _ApplicationControlSubscriptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 39, 1, 1),
    _ApplicationControlSubscriptionStatus_Type()
)
applicationControlSubscriptionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationControlSubscriptionStatus.setStatus("current")
_ApplicationControlSubscriptionExpDate_Type = DisplayString
_ApplicationControlSubscriptionExpDate_Object = MibScalar
applicationControlSubscriptionExpDate = _ApplicationControlSubscriptionExpDate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 39, 1, 2),
    _ApplicationControlSubscriptionExpDate_Type()
)
applicationControlSubscriptionExpDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationControlSubscriptionExpDate.setStatus("current")
_ApplicationControlSubscriptionDesc_Type = DisplayString
_ApplicationControlSubscriptionDesc_Object = MibScalar
applicationControlSubscriptionDesc = _ApplicationControlSubscriptionDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 39, 1, 3),
    _ApplicationControlSubscriptionDesc_Type()
)
applicationControlSubscriptionDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationControlSubscriptionDesc.setStatus("current")
_ApplicationControlUpdate_ObjectIdentity = ObjectIdentity
applicationControlUpdate = _ApplicationControlUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 39, 2)
)
_ApplicationControlUpdateStatus_Type = DisplayString
_ApplicationControlUpdateStatus_Object = MibScalar
applicationControlUpdateStatus = _ApplicationControlUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 39, 2, 1),
    _ApplicationControlUpdateStatus_Type()
)
applicationControlUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationControlUpdateStatus.setStatus("current")
_ApplicationControlUpdateDesc_Type = DisplayString
_ApplicationControlUpdateDesc_Object = MibScalar
applicationControlUpdateDesc = _ApplicationControlUpdateDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 39, 2, 2),
    _ApplicationControlUpdateDesc_Type()
)
applicationControlUpdateDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationControlUpdateDesc.setStatus("current")
_ApplicationControlNextUpdate_Type = DisplayString
_ApplicationControlNextUpdate_Object = MibScalar
applicationControlNextUpdate = _ApplicationControlNextUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 39, 2, 3),
    _ApplicationControlNextUpdate_Type()
)
applicationControlNextUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationControlNextUpdate.setStatus("current")
_ApplicationControlVersion_Type = DisplayString
_ApplicationControlVersion_Object = MibScalar
applicationControlVersion = _ApplicationControlVersion_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 39, 2, 4),
    _ApplicationControlVersion_Type()
)
applicationControlVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationControlVersion.setStatus("current")
_ApplicationControlStatusCode_Type = Integer32
_ApplicationControlStatusCode_Object = MibScalar
applicationControlStatusCode = _ApplicationControlStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 39, 101),
    _ApplicationControlStatusCode_Type()
)
applicationControlStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationControlStatusCode.setStatus("current")
_ApplicationControlStatusShortDesc_Type = DisplayString
_ApplicationControlStatusShortDesc_Object = MibScalar
applicationControlStatusShortDesc = _ApplicationControlStatusShortDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 39, 102),
    _ApplicationControlStatusShortDesc_Type()
)
applicationControlStatusShortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationControlStatusShortDesc.setStatus("current")
_ApplicationControlStatusLongDesc_Type = DisplayString
_ApplicationControlStatusLongDesc_Object = MibScalar
applicationControlStatusLongDesc = _ApplicationControlStatusLongDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 39, 103),
    _ApplicationControlStatusLongDesc_Type()
)
applicationControlStatusLongDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationControlStatusLongDesc.setStatus("current")
_Thresholds_ObjectIdentity = ObjectIdentity
thresholds = _Thresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42)
)
_ThresholdPolicy_Type = DisplayString
_ThresholdPolicy_Object = MibScalar
thresholdPolicy = _ThresholdPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 1),
    _ThresholdPolicy_Type()
)
thresholdPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdPolicy.setStatus("current")
_ThresholdState_Type = Integer32
_ThresholdState_Object = MibScalar
thresholdState = _ThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 2),
    _ThresholdState_Type()
)
thresholdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdState.setStatus("current")
_ThresholdStateDesc_Type = DisplayString
_ThresholdStateDesc_Object = MibScalar
thresholdStateDesc = _ThresholdStateDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 3),
    _ThresholdStateDesc_Type()
)
thresholdStateDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdStateDesc.setStatus("current")
_ThresholdEnabled_Type = Integer32
_ThresholdEnabled_Object = MibScalar
thresholdEnabled = _ThresholdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 4),
    _ThresholdEnabled_Type()
)
thresholdEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdEnabled.setStatus("current")
_ThresholdActive_Type = Integer32
_ThresholdActive_Object = MibScalar
thresholdActive = _ThresholdActive_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 5),
    _ThresholdActive_Type()
)
thresholdActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdActive.setStatus("current")
_ThresholdEventsSinceStartup_Type = Integer32
_ThresholdEventsSinceStartup_Object = MibScalar
thresholdEventsSinceStartup = _ThresholdEventsSinceStartup_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 6),
    _ThresholdEventsSinceStartup_Type()
)
thresholdEventsSinceStartup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdEventsSinceStartup.setStatus("current")
_ThresholdActiveEventsTable_Object = MibTable
thresholdActiveEventsTable = _ThresholdActiveEventsTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 7)
)
if mibBuilder.loadTexts:
    thresholdActiveEventsTable.setStatus("current")
_ThresholdActiveEventsEntry_Object = MibTableRow
thresholdActiveEventsEntry = _ThresholdActiveEventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 7, 1)
)
thresholdActiveEventsEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "thresholdActiveEventsIndex"),
)
if mibBuilder.loadTexts:
    thresholdActiveEventsEntry.setStatus("current")
_ThresholdActiveEventsIndex_Type = Unsigned32
_ThresholdActiveEventsIndex_Object = MibTableColumn
thresholdActiveEventsIndex = _ThresholdActiveEventsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 7, 1, 1),
    _ThresholdActiveEventsIndex_Type()
)
thresholdActiveEventsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdActiveEventsIndex.setStatus("current")
_ThresholdActiveEventName_Type = DisplayString
_ThresholdActiveEventName_Object = MibTableColumn
thresholdActiveEventName = _ThresholdActiveEventName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 7, 1, 2),
    _ThresholdActiveEventName_Type()
)
thresholdActiveEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdActiveEventName.setStatus("current")
_ThresholdActiveEventCategory_Type = DisplayString
_ThresholdActiveEventCategory_Object = MibTableColumn
thresholdActiveEventCategory = _ThresholdActiveEventCategory_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 7, 1, 3),
    _ThresholdActiveEventCategory_Type()
)
thresholdActiveEventCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdActiveEventCategory.setStatus("current")
_ThresholdActiveEventSeverity_Type = Integer32
_ThresholdActiveEventSeverity_Object = MibTableColumn
thresholdActiveEventSeverity = _ThresholdActiveEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 7, 1, 4),
    _ThresholdActiveEventSeverity_Type()
)
thresholdActiveEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdActiveEventSeverity.setStatus("current")
_ThresholdActiveEventSubject_Type = DisplayString
_ThresholdActiveEventSubject_Object = MibTableColumn
thresholdActiveEventSubject = _ThresholdActiveEventSubject_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 7, 1, 5),
    _ThresholdActiveEventSubject_Type()
)
thresholdActiveEventSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdActiveEventSubject.setStatus("current")
_ThresholdActiveEventSubjectValue_Type = DisplayString
_ThresholdActiveEventSubjectValue_Object = MibTableColumn
thresholdActiveEventSubjectValue = _ThresholdActiveEventSubjectValue_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 7, 1, 6),
    _ThresholdActiveEventSubjectValue_Type()
)
thresholdActiveEventSubjectValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdActiveEventSubjectValue.setStatus("current")
_ThresholdActiveEventActivationTime_Type = DisplayString
_ThresholdActiveEventActivationTime_Object = MibTableColumn
thresholdActiveEventActivationTime = _ThresholdActiveEventActivationTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 7, 1, 7),
    _ThresholdActiveEventActivationTime_Type()
)
thresholdActiveEventActivationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdActiveEventActivationTime.setStatus("current")
_ThresholdActiveEventState_Type = DisplayString
_ThresholdActiveEventState_Object = MibTableColumn
thresholdActiveEventState = _ThresholdActiveEventState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 7, 1, 8),
    _ThresholdActiveEventState_Type()
)
thresholdActiveEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdActiveEventState.setStatus("current")
_ThresholdDestinationsTable_Object = MibTable
thresholdDestinationsTable = _ThresholdDestinationsTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 8)
)
if mibBuilder.loadTexts:
    thresholdDestinationsTable.setStatus("current")
_ThresholdDestinationsEntry_Object = MibTableRow
thresholdDestinationsEntry = _ThresholdDestinationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 8, 1)
)
thresholdDestinationsEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "thresholdDestinationIndex"),
)
if mibBuilder.loadTexts:
    thresholdDestinationsEntry.setStatus("current")
_ThresholdDestinationIndex_Type = Unsigned32
_ThresholdDestinationIndex_Object = MibTableColumn
thresholdDestinationIndex = _ThresholdDestinationIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 8, 1, 1),
    _ThresholdDestinationIndex_Type()
)
thresholdDestinationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdDestinationIndex.setStatus("current")
_ThresholdDestinationName_Type = DisplayString
_ThresholdDestinationName_Object = MibTableColumn
thresholdDestinationName = _ThresholdDestinationName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 8, 1, 2),
    _ThresholdDestinationName_Type()
)
thresholdDestinationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdDestinationName.setStatus("current")
_ThresholdDestinationType_Type = DisplayString
_ThresholdDestinationType_Object = MibTableColumn
thresholdDestinationType = _ThresholdDestinationType_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 8, 1, 3),
    _ThresholdDestinationType_Type()
)
thresholdDestinationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdDestinationType.setStatus("current")
_ThresholdSendingState_Type = Integer32
_ThresholdSendingState_Object = MibTableColumn
thresholdSendingState = _ThresholdSendingState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 8, 1, 4),
    _ThresholdSendingState_Type()
)
thresholdSendingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdSendingState.setStatus("current")
_ThresholdSendingStateDesc_Type = DisplayString
_ThresholdSendingStateDesc_Object = MibTableColumn
thresholdSendingStateDesc = _ThresholdSendingStateDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 8, 1, 5),
    _ThresholdSendingStateDesc_Type()
)
thresholdSendingStateDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdSendingStateDesc.setStatus("current")
_ThresholdAlertCount_Type = Integer32
_ThresholdAlertCount_Object = MibTableColumn
thresholdAlertCount = _ThresholdAlertCount_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 8, 1, 6),
    _ThresholdAlertCount_Type()
)
thresholdAlertCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdAlertCount.setStatus("current")
_ThresholdErrorsTable_Object = MibTable
thresholdErrorsTable = _ThresholdErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 9)
)
if mibBuilder.loadTexts:
    thresholdErrorsTable.setStatus("current")
_ThresholdErrorsEntry_Object = MibTableRow
thresholdErrorsEntry = _ThresholdErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 9, 1)
)
thresholdErrorsEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "thresholdErrorIndex"),
)
if mibBuilder.loadTexts:
    thresholdErrorsEntry.setStatus("current")
_ThresholdErrorIndex_Type = Unsigned32
_ThresholdErrorIndex_Object = MibTableColumn
thresholdErrorIndex = _ThresholdErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 9, 1, 1),
    _ThresholdErrorIndex_Type()
)
thresholdErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdErrorIndex.setStatus("current")
_ThresholdName_Type = DisplayString
_ThresholdName_Object = MibTableColumn
thresholdName = _ThresholdName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 9, 1, 2),
    _ThresholdName_Type()
)
thresholdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdName.setStatus("current")
_ThresholdThresholdOID_Type = DisplayString
_ThresholdThresholdOID_Object = MibTableColumn
thresholdThresholdOID = _ThresholdThresholdOID_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 9, 1, 3),
    _ThresholdThresholdOID_Type()
)
thresholdThresholdOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdThresholdOID.setStatus("current")
_ThresholdErrorDesc_Type = DisplayString
_ThresholdErrorDesc_Object = MibTableColumn
thresholdErrorDesc = _ThresholdErrorDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 9, 1, 4),
    _ThresholdErrorDesc_Type()
)
thresholdErrorDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdErrorDesc.setStatus("current")
_ThresholdErrorTime_Type = DisplayString
_ThresholdErrorTime_Object = MibTableColumn
thresholdErrorTime = _ThresholdErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 42, 9, 1, 5),
    _ThresholdErrorTime_Type()
)
thresholdErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdErrorTime.setStatus("current")
_AdvancedUrlFiltering_ObjectIdentity = ObjectIdentity
advancedUrlFiltering = _AdvancedUrlFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 43)
)
_AdvancedUrlFilteringSubscription_ObjectIdentity = ObjectIdentity
advancedUrlFilteringSubscription = _AdvancedUrlFilteringSubscription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 43, 1)
)
_AdvancedUrlFilteringSubscriptionStatus_Type = DisplayString
_AdvancedUrlFilteringSubscriptionStatus_Object = MibScalar
advancedUrlFilteringSubscriptionStatus = _AdvancedUrlFilteringSubscriptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 43, 1, 1),
    _AdvancedUrlFilteringSubscriptionStatus_Type()
)
advancedUrlFilteringSubscriptionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedUrlFilteringSubscriptionStatus.setStatus("current")
_AdvancedUrlFilteringSubscriptionExpDate_Type = DisplayString
_AdvancedUrlFilteringSubscriptionExpDate_Object = MibScalar
advancedUrlFilteringSubscriptionExpDate = _AdvancedUrlFilteringSubscriptionExpDate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 43, 1, 2),
    _AdvancedUrlFilteringSubscriptionExpDate_Type()
)
advancedUrlFilteringSubscriptionExpDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedUrlFilteringSubscriptionExpDate.setStatus("current")
_AdvancedUrlFilteringSubscriptionDesc_Type = DisplayString
_AdvancedUrlFilteringSubscriptionDesc_Object = MibScalar
advancedUrlFilteringSubscriptionDesc = _AdvancedUrlFilteringSubscriptionDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 43, 1, 3),
    _AdvancedUrlFilteringSubscriptionDesc_Type()
)
advancedUrlFilteringSubscriptionDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedUrlFilteringSubscriptionDesc.setStatus("current")
_AdvancedUrlFilteringUpdate_ObjectIdentity = ObjectIdentity
advancedUrlFilteringUpdate = _AdvancedUrlFilteringUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 43, 2)
)
_AdvancedUrlFilteringUpdateStatus_Type = DisplayString
_AdvancedUrlFilteringUpdateStatus_Object = MibScalar
advancedUrlFilteringUpdateStatus = _AdvancedUrlFilteringUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 43, 2, 1),
    _AdvancedUrlFilteringUpdateStatus_Type()
)
advancedUrlFilteringUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedUrlFilteringUpdateStatus.setStatus("current")
_AdvancedUrlFilteringUpdateDesc_Type = DisplayString
_AdvancedUrlFilteringUpdateDesc_Object = MibScalar
advancedUrlFilteringUpdateDesc = _AdvancedUrlFilteringUpdateDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 43, 2, 2),
    _AdvancedUrlFilteringUpdateDesc_Type()
)
advancedUrlFilteringUpdateDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedUrlFilteringUpdateDesc.setStatus("current")
_AdvancedUrlFilteringNextUpdate_Type = DisplayString
_AdvancedUrlFilteringNextUpdate_Object = MibScalar
advancedUrlFilteringNextUpdate = _AdvancedUrlFilteringNextUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 43, 2, 3),
    _AdvancedUrlFilteringNextUpdate_Type()
)
advancedUrlFilteringNextUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedUrlFilteringNextUpdate.setStatus("current")
_AdvancedUrlFilteringVersion_Type = DisplayString
_AdvancedUrlFilteringVersion_Object = MibScalar
advancedUrlFilteringVersion = _AdvancedUrlFilteringVersion_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 43, 2, 4),
    _AdvancedUrlFilteringVersion_Type()
)
advancedUrlFilteringVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedUrlFilteringVersion.setStatus("current")
_AdvancedUrlFilteringRADStatus_ObjectIdentity = ObjectIdentity
advancedUrlFilteringRADStatus = _AdvancedUrlFilteringRADStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 43, 3)
)
_AdvancedUrlFilteringRADStatusCode_Type = Integer32
_AdvancedUrlFilteringRADStatusCode_Object = MibScalar
advancedUrlFilteringRADStatusCode = _AdvancedUrlFilteringRADStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 43, 3, 1),
    _AdvancedUrlFilteringRADStatusCode_Type()
)
advancedUrlFilteringRADStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedUrlFilteringRADStatusCode.setStatus("current")
_AdvancedUrlFilteringRADStatusDesc_Type = DisplayString
_AdvancedUrlFilteringRADStatusDesc_Object = MibScalar
advancedUrlFilteringRADStatusDesc = _AdvancedUrlFilteringRADStatusDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 43, 3, 2),
    _AdvancedUrlFilteringRADStatusDesc_Type()
)
advancedUrlFilteringRADStatusDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedUrlFilteringRADStatusDesc.setStatus("current")
_AdvancedUrlFilteringStatusCode_Type = Integer32
_AdvancedUrlFilteringStatusCode_Object = MibScalar
advancedUrlFilteringStatusCode = _AdvancedUrlFilteringStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 43, 101),
    _AdvancedUrlFilteringStatusCode_Type()
)
advancedUrlFilteringStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedUrlFilteringStatusCode.setStatus("current")
_AdvancedUrlFilteringStatusShortDesc_Type = DisplayString
_AdvancedUrlFilteringStatusShortDesc_Object = MibScalar
advancedUrlFilteringStatusShortDesc = _AdvancedUrlFilteringStatusShortDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 43, 102),
    _AdvancedUrlFilteringStatusShortDesc_Type()
)
advancedUrlFilteringStatusShortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedUrlFilteringStatusShortDesc.setStatus("current")
_AdvancedUrlFilteringStatusLongDesc_Type = DisplayString
_AdvancedUrlFilteringStatusLongDesc_Object = MibScalar
advancedUrlFilteringStatusLongDesc = _AdvancedUrlFilteringStatusLongDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 43, 103),
    _AdvancedUrlFilteringStatusLongDesc_Type()
)
advancedUrlFilteringStatusLongDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedUrlFilteringStatusLongDesc.setStatus("current")
_Dlp_ObjectIdentity = ObjectIdentity
dlp = _Dlp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44)
)
_ExchangeAgents_ObjectIdentity = ObjectIdentity
exchangeAgents = _ExchangeAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 1)
)
_ExchangeAgentsTable_Object = MibTable
exchangeAgentsTable = _ExchangeAgentsTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 1, 1)
)
if mibBuilder.loadTexts:
    exchangeAgentsTable.setStatus("current")
_ExchangeAgentsStatusEntry_Object = MibTableRow
exchangeAgentsStatusEntry = _ExchangeAgentsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 1, 1, 1)
)
exchangeAgentsStatusEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "exchangeAgentsStatusTableIndex"),
)
if mibBuilder.loadTexts:
    exchangeAgentsStatusEntry.setStatus("current")
_ExchangeAgentsStatusTableIndex_Type = Unsigned32
_ExchangeAgentsStatusTableIndex_Object = MibTableColumn
exchangeAgentsStatusTableIndex = _ExchangeAgentsStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 1, 1, 1, 1),
    _ExchangeAgentsStatusTableIndex_Type()
)
exchangeAgentsStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchangeAgentsStatusTableIndex.setStatus("current")
_ExchangeAgentName_Type = DisplayString
_ExchangeAgentName_Object = MibTableColumn
exchangeAgentName = _ExchangeAgentName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 1, 1, 1, 2),
    _ExchangeAgentName_Type()
)
exchangeAgentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchangeAgentName.setStatus("current")
_ExchangeAgentStatus_Type = DisplayString
_ExchangeAgentStatus_Object = MibTableColumn
exchangeAgentStatus = _ExchangeAgentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 1, 1, 1, 3),
    _ExchangeAgentStatus_Type()
)
exchangeAgentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchangeAgentStatus.setStatus("current")
_ExchangeAgentTotalMsg_Type = Integer32
_ExchangeAgentTotalMsg_Object = MibTableColumn
exchangeAgentTotalMsg = _ExchangeAgentTotalMsg_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 1, 1, 1, 4),
    _ExchangeAgentTotalMsg_Type()
)
exchangeAgentTotalMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchangeAgentTotalMsg.setStatus("current")
_ExchangeAgentTotalScannedMsg_Type = Integer32
_ExchangeAgentTotalScannedMsg_Object = MibTableColumn
exchangeAgentTotalScannedMsg = _ExchangeAgentTotalScannedMsg_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 1, 1, 1, 5),
    _ExchangeAgentTotalScannedMsg_Type()
)
exchangeAgentTotalScannedMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchangeAgentTotalScannedMsg.setStatus("current")
_ExchangeAgentDroppedMsg_Type = Integer32
_ExchangeAgentDroppedMsg_Object = MibTableColumn
exchangeAgentDroppedMsg = _ExchangeAgentDroppedMsg_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 1, 1, 1, 6),
    _ExchangeAgentDroppedMsg_Type()
)
exchangeAgentDroppedMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchangeAgentDroppedMsg.setStatus("current")
_ExchangeAgentUpTime_Type = Integer32
_ExchangeAgentUpTime_Object = MibTableColumn
exchangeAgentUpTime = _ExchangeAgentUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 1, 1, 1, 7),
    _ExchangeAgentUpTime_Type()
)
exchangeAgentUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchangeAgentUpTime.setStatus("current")
_ExchangeAgentTimeSinceLastMsg_Type = Integer32
_ExchangeAgentTimeSinceLastMsg_Object = MibTableColumn
exchangeAgentTimeSinceLastMsg = _ExchangeAgentTimeSinceLastMsg_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 1, 1, 1, 8),
    _ExchangeAgentTimeSinceLastMsg_Type()
)
exchangeAgentTimeSinceLastMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchangeAgentTimeSinceLastMsg.setStatus("current")
_ExchangeAgentQueueLen_Type = Integer32
_ExchangeAgentQueueLen_Object = MibTableColumn
exchangeAgentQueueLen = _ExchangeAgentQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 1, 1, 1, 9),
    _ExchangeAgentQueueLen_Type()
)
exchangeAgentQueueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchangeAgentQueueLen.setStatus("current")
_ExchangeQueueLen_Type = Integer32
_ExchangeQueueLen_Object = MibTableColumn
exchangeQueueLen = _ExchangeQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 1, 1, 1, 10),
    _ExchangeQueueLen_Type()
)
exchangeQueueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchangeQueueLen.setStatus("current")
_ExchangeAgentAvgTimePerMsg_Type = DisplayString
_ExchangeAgentAvgTimePerMsg_Object = MibTableColumn
exchangeAgentAvgTimePerMsg = _ExchangeAgentAvgTimePerMsg_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 1, 1, 1, 11),
    _ExchangeAgentAvgTimePerMsg_Type()
)
exchangeAgentAvgTimePerMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchangeAgentAvgTimePerMsg.setStatus("current")
_ExchangeAgentAvgTimePerScannedMsg_Type = DisplayString
_ExchangeAgentAvgTimePerScannedMsg_Object = MibTableColumn
exchangeAgentAvgTimePerScannedMsg = _ExchangeAgentAvgTimePerScannedMsg_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 1, 1, 1, 12),
    _ExchangeAgentAvgTimePerScannedMsg_Type()
)
exchangeAgentAvgTimePerScannedMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchangeAgentAvgTimePerScannedMsg.setStatus("current")
_ExchangeAgentVersion_Type = DisplayString
_ExchangeAgentVersion_Object = MibTableColumn
exchangeAgentVersion = _ExchangeAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 1, 1, 1, 13),
    _ExchangeAgentVersion_Type()
)
exchangeAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchangeAgentVersion.setStatus("current")
_ExchangeCPUUsage_Type = DisplayString
_ExchangeCPUUsage_Object = MibTableColumn
exchangeCPUUsage = _ExchangeCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 1, 1, 1, 14),
    _ExchangeCPUUsage_Type()
)
exchangeCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchangeCPUUsage.setStatus("current")
_ExchangeMemoryUsage_Type = DisplayString
_ExchangeMemoryUsage_Object = MibTableColumn
exchangeMemoryUsage = _ExchangeMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 1, 1, 1, 15),
    _ExchangeMemoryUsage_Type()
)
exchangeMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchangeMemoryUsage.setStatus("current")
_ExchangeAgentPolicyTimeStamp_Type = Integer32
_ExchangeAgentPolicyTimeStamp_Object = MibTableColumn
exchangeAgentPolicyTimeStamp = _ExchangeAgentPolicyTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 1, 1, 1, 16),
    _ExchangeAgentPolicyTimeStamp_Type()
)
exchangeAgentPolicyTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exchangeAgentPolicyTimeStamp.setStatus("current")
_DlpVersionString_Type = DisplayString
_DlpVersionString_Object = MibScalar
dlpVersionString = _DlpVersionString_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 11),
    _DlpVersionString_Type()
)
dlpVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpVersionString.setStatus("current")
_DlpLicenseStatus_Type = DisplayString
_DlpLicenseStatus_Object = MibScalar
dlpLicenseStatus = _DlpLicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 12),
    _DlpLicenseStatus_Type()
)
dlpLicenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpLicenseStatus.setStatus("current")
_DlpLdapStatus_Type = DisplayString
_DlpLdapStatus_Object = MibScalar
dlpLdapStatus = _DlpLdapStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 13),
    _DlpLdapStatus_Type()
)
dlpLdapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpLdapStatus.setStatus("current")
_DlpTotalScans_Type = DisplayString
_DlpTotalScans_Object = MibScalar
dlpTotalScans = _DlpTotalScans_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 14),
    _DlpTotalScans_Type()
)
dlpTotalScans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpTotalScans.setStatus("current")
_DlpSMTPScans_Type = DisplayString
_DlpSMTPScans_Object = MibScalar
dlpSMTPScans = _DlpSMTPScans_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 15),
    _DlpSMTPScans_Type()
)
dlpSMTPScans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpSMTPScans.setStatus("current")
_DlpSMTPIncidents_Type = DisplayString
_DlpSMTPIncidents_Object = MibScalar
dlpSMTPIncidents = _DlpSMTPIncidents_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 16),
    _DlpSMTPIncidents_Type()
)
dlpSMTPIncidents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpSMTPIncidents.setStatus("current")
_DlpLastSMTPScan_Type = DisplayString
_DlpLastSMTPScan_Object = MibScalar
dlpLastSMTPScan = _DlpLastSMTPScan_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 17),
    _DlpLastSMTPScan_Type()
)
dlpLastSMTPScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpLastSMTPScan.setStatus("current")
_DlpNumQuarantined_Type = Integer32
_DlpNumQuarantined_Object = MibScalar
dlpNumQuarantined = _DlpNumQuarantined_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 18),
    _DlpNumQuarantined_Type()
)
dlpNumQuarantined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpNumQuarantined.setStatus("current")
_DlpQrntMsgsSize_Type = Integer32
_DlpQrntMsgsSize_Object = MibScalar
dlpQrntMsgsSize = _DlpQrntMsgsSize_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 19),
    _DlpQrntMsgsSize_Type()
)
dlpQrntMsgsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpQrntMsgsSize.setStatus("current")
_DlpSentEMails_Type = DisplayString
_DlpSentEMails_Object = MibScalar
dlpSentEMails = _DlpSentEMails_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 20),
    _DlpSentEMails_Type()
)
dlpSentEMails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpSentEMails.setStatus("current")
_DlpExpiredEMails_Type = DisplayString
_DlpExpiredEMails_Object = MibScalar
dlpExpiredEMails = _DlpExpiredEMails_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 21),
    _DlpExpiredEMails_Type()
)
dlpExpiredEMails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpExpiredEMails.setStatus("current")
_DlpDiscardEMails_Type = DisplayString
_DlpDiscardEMails_Object = MibScalar
dlpDiscardEMails = _DlpDiscardEMails_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 22),
    _DlpDiscardEMails_Type()
)
dlpDiscardEMails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpDiscardEMails.setStatus("current")
_DlpPostfixQLen_Type = Integer32
_DlpPostfixQLen_Object = MibScalar
dlpPostfixQLen = _DlpPostfixQLen_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 23),
    _DlpPostfixQLen_Type()
)
dlpPostfixQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpPostfixQLen.setStatus("current")
_DlpPostfixErrors_Type = Integer32
_DlpPostfixErrors_Object = MibScalar
dlpPostfixErrors = _DlpPostfixErrors_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 24),
    _DlpPostfixErrors_Type()
)
dlpPostfixErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpPostfixErrors.setStatus("current")
_DlpPostfixQOldMsg_Type = Integer32
_DlpPostfixQOldMsg_Object = MibScalar
dlpPostfixQOldMsg = _DlpPostfixQOldMsg_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 25),
    _DlpPostfixQOldMsg_Type()
)
dlpPostfixQOldMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpPostfixQOldMsg.setStatus("current")
_DlpPostfixQMsgsSz_Type = Integer32
_DlpPostfixQMsgsSz_Object = MibScalar
dlpPostfixQMsgsSz = _DlpPostfixQMsgsSz_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 26),
    _DlpPostfixQMsgsSz_Type()
)
dlpPostfixQMsgsSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpPostfixQMsgsSz.setStatus("current")
_DlpPostfixQFreeSp_Type = Integer32
_DlpPostfixQFreeSp_Object = MibScalar
dlpPostfixQFreeSp = _DlpPostfixQFreeSp_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 27),
    _DlpPostfixQFreeSp_Type()
)
dlpPostfixQFreeSp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpPostfixQFreeSp.setStatus("current")
_DlpQrntFreeSpace_Type = DisplayString
_DlpQrntFreeSpace_Object = MibScalar
dlpQrntFreeSpace = _DlpQrntFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 28),
    _DlpQrntFreeSpace_Type()
)
dlpQrntFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpQrntFreeSpace.setStatus("current")
_DlpQrntStatus_Type = DisplayString
_DlpQrntStatus_Object = MibScalar
dlpQrntStatus = _DlpQrntStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 29),
    _DlpQrntStatus_Type()
)
dlpQrntStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpQrntStatus.setStatus("current")
_DlpHttpScans_Type = DisplayString
_DlpHttpScans_Object = MibScalar
dlpHttpScans = _DlpHttpScans_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 30),
    _DlpHttpScans_Type()
)
dlpHttpScans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpHttpScans.setStatus("current")
_DlpHttpIncidents_Type = DisplayString
_DlpHttpIncidents_Object = MibScalar
dlpHttpIncidents = _DlpHttpIncidents_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 31),
    _DlpHttpIncidents_Type()
)
dlpHttpIncidents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpHttpIncidents.setStatus("current")
_DlpHttpLastScan_Type = DisplayString
_DlpHttpLastScan_Object = MibScalar
dlpHttpLastScan = _DlpHttpLastScan_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 32),
    _DlpHttpLastScan_Type()
)
dlpHttpLastScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpHttpLastScan.setStatus("current")
_DlpFtpScans_Type = DisplayString
_DlpFtpScans_Object = MibScalar
dlpFtpScans = _DlpFtpScans_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 33),
    _DlpFtpScans_Type()
)
dlpFtpScans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpFtpScans.setStatus("current")
_DlpFtpIncidents_Type = DisplayString
_DlpFtpIncidents_Object = MibScalar
dlpFtpIncidents = _DlpFtpIncidents_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 34),
    _DlpFtpIncidents_Type()
)
dlpFtpIncidents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpFtpIncidents.setStatus("current")
_DlpFtpLastScan_Type = DisplayString
_DlpFtpLastScan_Object = MibScalar
dlpFtpLastScan = _DlpFtpLastScan_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 35),
    _DlpFtpLastScan_Type()
)
dlpFtpLastScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpFtpLastScan.setStatus("current")
_DlpBypassStatus_Type = DisplayString
_DlpBypassStatus_Object = MibScalar
dlpBypassStatus = _DlpBypassStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 36),
    _DlpBypassStatus_Type()
)
dlpBypassStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpBypassStatus.setStatus("current")
_DlpUserCheckClnts_Type = Integer32
_DlpUserCheckClnts_Object = MibScalar
dlpUserCheckClnts = _DlpUserCheckClnts_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 37),
    _DlpUserCheckClnts_Type()
)
dlpUserCheckClnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpUserCheckClnts.setStatus("current")
_DlpLastPolStatus_Type = DisplayString
_DlpLastPolStatus_Object = MibScalar
dlpLastPolStatus = _DlpLastPolStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 38),
    _DlpLastPolStatus_Type()
)
dlpLastPolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpLastPolStatus.setStatus("current")
_DlpStatusCode_Type = Integer32
_DlpStatusCode_Object = MibScalar
dlpStatusCode = _DlpStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 101),
    _DlpStatusCode_Type()
)
dlpStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpStatusCode.setStatus("current")
_DlpStatusShortDesc_Type = DisplayString
_DlpStatusShortDesc_Object = MibScalar
dlpStatusShortDesc = _DlpStatusShortDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 102),
    _DlpStatusShortDesc_Type()
)
dlpStatusShortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpStatusShortDesc.setStatus("current")
_DlpStatusLongDesc_Type = DisplayString
_DlpStatusLongDesc_Object = MibScalar
dlpStatusLongDesc = _DlpStatusLongDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 44, 103),
    _DlpStatusLongDesc_Type()
)
dlpStatusLongDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlpStatusLongDesc.setStatus("current")
_Amw_ObjectIdentity = ObjectIdentity
amw = _Amw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46)
)
_AmwABUpdate_ObjectIdentity = ObjectIdentity
amwABUpdate = _AmwABUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 1)
)
_AmwABUpdateStatus_Type = DisplayString
_AmwABUpdateStatus_Object = MibScalar
amwABUpdateStatus = _AmwABUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 1, 1),
    _AmwABUpdateStatus_Type()
)
amwABUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amwABUpdateStatus.setStatus("current")
_AmwABUpdateDesc_Type = DisplayString
_AmwABUpdateDesc_Object = MibScalar
amwABUpdateDesc = _AmwABUpdateDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 1, 2),
    _AmwABUpdateDesc_Type()
)
amwABUpdateDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amwABUpdateDesc.setStatus("current")
_AmwABNextUpdate_Type = DisplayString
_AmwABNextUpdate_Object = MibScalar
amwABNextUpdate = _AmwABNextUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 1, 3),
    _AmwABNextUpdate_Type()
)
amwABNextUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amwABNextUpdate.setStatus("current")
_AmwABVersion_Type = DisplayString
_AmwABVersion_Object = MibScalar
amwABVersion = _AmwABVersion_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 1, 4),
    _AmwABVersion_Type()
)
amwABVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amwABVersion.setStatus("current")
_AntiBotSubscription_ObjectIdentity = ObjectIdentity
antiBotSubscription = _AntiBotSubscription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 2)
)
_AntiBotSubscriptionStatus_Type = DisplayString
_AntiBotSubscriptionStatus_Object = MibScalar
antiBotSubscriptionStatus = _AntiBotSubscriptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 2, 1),
    _AntiBotSubscriptionStatus_Type()
)
antiBotSubscriptionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antiBotSubscriptionStatus.setStatus("current")
_AntiBotSubscriptionExpDate_Type = DisplayString
_AntiBotSubscriptionExpDate_Object = MibScalar
antiBotSubscriptionExpDate = _AntiBotSubscriptionExpDate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 2, 2),
    _AntiBotSubscriptionExpDate_Type()
)
antiBotSubscriptionExpDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antiBotSubscriptionExpDate.setStatus("current")
_AntiBotSubscriptionDesc_Type = DisplayString
_AntiBotSubscriptionDesc_Object = MibScalar
antiBotSubscriptionDesc = _AntiBotSubscriptionDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 2, 3),
    _AntiBotSubscriptionDesc_Type()
)
antiBotSubscriptionDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antiBotSubscriptionDesc.setStatus("current")
_AntiVirusSubscription_ObjectIdentity = ObjectIdentity
antiVirusSubscription = _AntiVirusSubscription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 3)
)
_AntiVirusSubscriptionStatus_Type = DisplayString
_AntiVirusSubscriptionStatus_Object = MibScalar
antiVirusSubscriptionStatus = _AntiVirusSubscriptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 3, 1),
    _AntiVirusSubscriptionStatus_Type()
)
antiVirusSubscriptionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antiVirusSubscriptionStatus.setStatus("current")
_AntiVirusSubscriptionExpDate_Type = DisplayString
_AntiVirusSubscriptionExpDate_Object = MibScalar
antiVirusSubscriptionExpDate = _AntiVirusSubscriptionExpDate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 3, 2),
    _AntiVirusSubscriptionExpDate_Type()
)
antiVirusSubscriptionExpDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antiVirusSubscriptionExpDate.setStatus("current")
_AntiVirusSubscriptionDesc_Type = DisplayString
_AntiVirusSubscriptionDesc_Object = MibScalar
antiVirusSubscriptionDesc = _AntiVirusSubscriptionDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 3, 3),
    _AntiVirusSubscriptionDesc_Type()
)
antiVirusSubscriptionDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antiVirusSubscriptionDesc.setStatus("current")
_AntiSpamSubscription_ObjectIdentity = ObjectIdentity
antiSpamSubscription = _AntiSpamSubscription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 4)
)
_AntiSpamSubscriptionStatus_Type = DisplayString
_AntiSpamSubscriptionStatus_Object = MibScalar
antiSpamSubscriptionStatus = _AntiSpamSubscriptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 4, 1),
    _AntiSpamSubscriptionStatus_Type()
)
antiSpamSubscriptionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antiSpamSubscriptionStatus.setStatus("current")
_AntiSpamSubscriptionExpDate_Type = DisplayString
_AntiSpamSubscriptionExpDate_Object = MibScalar
antiSpamSubscriptionExpDate = _AntiSpamSubscriptionExpDate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 4, 2),
    _AntiSpamSubscriptionExpDate_Type()
)
antiSpamSubscriptionExpDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antiSpamSubscriptionExpDate.setStatus("current")
_AntiSpamSubscriptionDesc_Type = DisplayString
_AntiSpamSubscriptionDesc_Object = MibScalar
antiSpamSubscriptionDesc = _AntiSpamSubscriptionDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 4, 3),
    _AntiSpamSubscriptionDesc_Type()
)
antiSpamSubscriptionDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antiSpamSubscriptionDesc.setStatus("current")
_AmwAVUpdate_ObjectIdentity = ObjectIdentity
amwAVUpdate = _AmwAVUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 5)
)
_AmwAVUpdateStatus_Type = DisplayString
_AmwAVUpdateStatus_Object = MibScalar
amwAVUpdateStatus = _AmwAVUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 5, 1),
    _AmwAVUpdateStatus_Type()
)
amwAVUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amwAVUpdateStatus.setStatus("current")
_AmwAVUpdateDesc_Type = DisplayString
_AmwAVUpdateDesc_Object = MibScalar
amwAVUpdateDesc = _AmwAVUpdateDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 5, 2),
    _AmwAVUpdateDesc_Type()
)
amwAVUpdateDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amwAVUpdateDesc.setStatus("current")
_AmwAVNextUpdate_Type = DisplayString
_AmwAVNextUpdate_Object = MibScalar
amwAVNextUpdate = _AmwAVNextUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 5, 3),
    _AmwAVNextUpdate_Type()
)
amwAVNextUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amwAVNextUpdate.setStatus("current")
_AmwAVVersion_Type = DisplayString
_AmwAVVersion_Object = MibScalar
amwAVVersion = _AmwAVVersion_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 5, 4),
    _AmwAVVersion_Type()
)
amwAVVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amwAVVersion.setStatus("current")
_AmwStatusCode_Type = Integer32
_AmwStatusCode_Object = MibScalar
amwStatusCode = _AmwStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 101),
    _AmwStatusCode_Type()
)
amwStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amwStatusCode.setStatus("current")
_AmwStatusShortDesc_Type = DisplayString
_AmwStatusShortDesc_Object = MibScalar
amwStatusShortDesc = _AmwStatusShortDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 102),
    _AmwStatusShortDesc_Type()
)
amwStatusShortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amwStatusShortDesc.setStatus("current")
_AmwStatusLongDesc_Type = DisplayString
_AmwStatusLongDesc_Object = MibScalar
amwStatusLongDesc = _AmwStatusLongDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 46, 103),
    _AmwStatusLongDesc_Type()
)
amwStatusLongDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amwStatusLongDesc.setStatus("current")
_Te_ObjectIdentity = ObjectIdentity
te = _Te_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 49)
)
_TeUpdateStatus_Type = DisplayString
_TeUpdateStatus_Object = MibScalar
teUpdateStatus = _TeUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 49, 16),
    _TeUpdateStatus_Type()
)
teUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teUpdateStatus.setStatus("current")
_TeUpdateDesc_Type = DisplayString
_TeUpdateDesc_Object = MibScalar
teUpdateDesc = _TeUpdateDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 49, 17),
    _TeUpdateDesc_Type()
)
teUpdateDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teUpdateDesc.setStatus("current")
_TeSubscriptionExpDate_Type = DisplayString
_TeSubscriptionExpDate_Object = MibScalar
teSubscriptionExpDate = _TeSubscriptionExpDate_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 49, 20),
    _TeSubscriptionExpDate_Type()
)
teSubscriptionExpDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teSubscriptionExpDate.setStatus("current")
_TeSubscriptionStatus_Type = DisplayString
_TeSubscriptionStatus_Object = MibScalar
teSubscriptionStatus = _TeSubscriptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 49, 25),
    _TeSubscriptionStatus_Type()
)
teSubscriptionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teSubscriptionStatus.setStatus("current")
_TeCloudSubscriptionStatus_Type = DisplayString
_TeCloudSubscriptionStatus_Object = MibScalar
teCloudSubscriptionStatus = _TeCloudSubscriptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 49, 26),
    _TeCloudSubscriptionStatus_Type()
)
teCloudSubscriptionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teCloudSubscriptionStatus.setStatus("current")
_TeSubscriptionDesc_Type = DisplayString
_TeSubscriptionDesc_Object = MibScalar
teSubscriptionDesc = _TeSubscriptionDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 49, 27),
    _TeSubscriptionDesc_Type()
)
teSubscriptionDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teSubscriptionDesc.setStatus("current")
_TeStatusCode_Type = Integer32
_TeStatusCode_Object = MibScalar
teStatusCode = _TeStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 49, 101),
    _TeStatusCode_Type()
)
teStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teStatusCode.setStatus("current")
_TeStatusShortDesc_Type = DisplayString
_TeStatusShortDesc_Object = MibScalar
teStatusShortDesc = _TeStatusShortDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 49, 102),
    _TeStatusShortDesc_Type()
)
teStatusShortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teStatusShortDesc.setStatus("current")
_TeStatusLongDesc_Type = DisplayString
_TeStatusLongDesc_Object = MibScalar
teStatusLongDesc = _TeStatusLongDesc_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 49, 103),
    _TeStatusLongDesc_Type()
)
teStatusLongDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teStatusLongDesc.setStatus("current")
_Tables_ObjectIdentity = ObjectIdentity
tables = _Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 500)
)
_RaUsersTable_Object = MibTable
raUsersTable = _RaUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9000)
)
if mibBuilder.loadTexts:
    raUsersTable.setStatus("current")
_RaUsersEntry_Object = MibTableRow
raUsersEntry = _RaUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9000, 1)
)
raUsersEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "raInternalIpAddr"),
)
if mibBuilder.loadTexts:
    raUsersEntry.setStatus("current")
_RaInternalIpAddr_Type = IpAddress
_RaInternalIpAddr_Object = MibTableColumn
raInternalIpAddr = _RaInternalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9000, 1, 1),
    _RaInternalIpAddr_Type()
)
raInternalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raInternalIpAddr.setStatus("current")
_RaExternalIpAddr_Type = IpAddress
_RaExternalIpAddr_Object = MibTableColumn
raExternalIpAddr = _RaExternalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9000, 1, 19),
    _RaExternalIpAddr_Type()
)
raExternalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raExternalIpAddr.setStatus("current")


class _RaUserState_Type(Integer32):
    """Custom type raUserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              129,
              130,
              131,
              132)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("destroy", 4),
          ("down", 131),
          ("idle", 129),
          ("init", 132),
          ("phase1", 130))
    )


_RaUserState_Type.__name__ = "Integer32"
_RaUserState_Object = MibTableColumn
raUserState = _RaUserState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9000, 1, 20),
    _RaUserState_Type()
)
raUserState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raUserState.setStatus("current")
_RaOfficeMode_Type = Integer32
_RaOfficeMode_Object = MibTableColumn
raOfficeMode = _RaOfficeMode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9000, 1, 21),
    _RaOfficeMode_Type()
)
raOfficeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raOfficeMode.setStatus("current")
_RaIkeOverTCP_Type = Integer32
_RaIkeOverTCP_Object = MibTableColumn
raIkeOverTCP = _RaIkeOverTCP_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9000, 1, 22),
    _RaIkeOverTCP_Type()
)
raIkeOverTCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raIkeOverTCP.setStatus("current")
_RaUseUDPEncap_Type = Integer32
_RaUseUDPEncap_Object = MibTableColumn
raUseUDPEncap = _RaUseUDPEncap_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9000, 1, 23),
    _RaUseUDPEncap_Type()
)
raUseUDPEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raUseUDPEncap.setStatus("current")
_RaVisitorMode_Type = Integer32
_RaVisitorMode_Object = MibTableColumn
raVisitorMode = _RaVisitorMode_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9000, 1, 24),
    _RaVisitorMode_Type()
)
raVisitorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raVisitorMode.setStatus("current")
_RaRouteTraffic_Type = Integer32
_RaRouteTraffic_Object = MibTableColumn
raRouteTraffic = _RaRouteTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9000, 1, 25),
    _RaRouteTraffic_Type()
)
raRouteTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raRouteTraffic.setStatus("current")
_RaCommunity_Type = DisplayString
_RaCommunity_Object = MibTableColumn
raCommunity = _RaCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9000, 1, 26),
    _RaCommunity_Type()
)
raCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raCommunity.setStatus("current")


class _RaTunnelEncAlgorithm_Type(Integer32):
    """Custom type raTunnelEncAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              7,
              9,
              129,
              130)
        )
    )
    namedValues = NamedValues(
        *(("esp3DES", 2),
          ("esp3IDEA", 7),
          ("espAES128", 129),
          ("espAES256", 130),
          ("espCAST", 5),
          ("espDES", 1),
          ("espNULL", 9))
    )


_RaTunnelEncAlgorithm_Type.__name__ = "Integer32"
_RaTunnelEncAlgorithm_Object = MibTableColumn
raTunnelEncAlgorithm = _RaTunnelEncAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9000, 1, 27),
    _RaTunnelEncAlgorithm_Type()
)
raTunnelEncAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raTunnelEncAlgorithm.setStatus("current")


class _RaTunnelAuthMethod_Type(Integer32):
    """Custom type raTunnelAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              129,
              130)
        )
    )
    namedValues = NamedValues(
        *(("crack", 130),
          ("dss-signature", 2),
          ("preshared-key", 1),
          ("rev-rsa-encryption", 5),
          ("rsa-encryption", 4),
          ("rsa-signature", 3),
          ("xauth", 129))
    )


_RaTunnelAuthMethod_Type.__name__ = "Integer32"
_RaTunnelAuthMethod_Object = MibTableColumn
raTunnelAuthMethod = _RaTunnelAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9000, 1, 28),
    _RaTunnelAuthMethod_Type()
)
raTunnelAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raTunnelAuthMethod.setStatus("current")
_RaLogonTime_Type = Integer32
_RaLogonTime_Object = MibTableColumn
raLogonTime = _RaLogonTime_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9000, 1, 29),
    _RaLogonTime_Type()
)
raLogonTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raLogonTime.setStatus("current")
_TunnelTable_Object = MibTable
tunnelTable = _TunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9002)
)
if mibBuilder.loadTexts:
    tunnelTable.setStatus("current")
_TunnelEntry_Object = MibTableRow
tunnelEntry = _TunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9002, 1)
)
tunnelEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "tunnelPeerIpAddr"),
)
if mibBuilder.loadTexts:
    tunnelEntry.setStatus("current")
_TunnelPeerIpAddr_Type = IpAddress
_TunnelPeerIpAddr_Object = MibTableColumn
tunnelPeerIpAddr = _TunnelPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9002, 1, 1),
    _TunnelPeerIpAddr_Type()
)
tunnelPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelPeerIpAddr.setStatus("current")
_TunnelPeerObjName_Type = DisplayString
_TunnelPeerObjName_Object = MibTableColumn
tunnelPeerObjName = _TunnelPeerObjName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9002, 1, 2),
    _TunnelPeerObjName_Type()
)
tunnelPeerObjName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelPeerObjName.setStatus("current")


class _TunnelState_Type(Integer32):
    """Custom type tunnelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              129,
              130,
              131,
              132)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("destroy", 4),
          ("down", 131),
          ("idle", 129),
          ("init", 132),
          ("phase1", 130))
    )


_TunnelState_Type.__name__ = "Integer32"
_TunnelState_Object = MibTableColumn
tunnelState = _TunnelState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9002, 1, 3),
    _TunnelState_Type()
)
tunnelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelState.setStatus("current")
_TunnelCommunity_Type = DisplayString
_TunnelCommunity_Object = MibTableColumn
tunnelCommunity = _TunnelCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9002, 1, 4),
    _TunnelCommunity_Type()
)
tunnelCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelCommunity.setStatus("current")
_TunnelNextHop_Type = IpAddress
_TunnelNextHop_Object = MibTableColumn
tunnelNextHop = _TunnelNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9002, 1, 5),
    _TunnelNextHop_Type()
)
tunnelNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelNextHop.setStatus("current")
_TunnelInterface_Type = DisplayString
_TunnelInterface_Object = MibTableColumn
tunnelInterface = _TunnelInterface_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9002, 1, 6),
    _TunnelInterface_Type()
)
tunnelInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelInterface.setStatus("current")
_TunnelSourceIpAddr_Type = IpAddress
_TunnelSourceIpAddr_Object = MibTableColumn
tunnelSourceIpAddr = _TunnelSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9002, 1, 7),
    _TunnelSourceIpAddr_Type()
)
tunnelSourceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelSourceIpAddr.setStatus("current")


class _TunnelLinkPriority_Type(Integer32):
    """Custom type tunnelLinkPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("on-demand", 2),
          ("primary", 0))
    )


_TunnelLinkPriority_Type.__name__ = "Integer32"
_TunnelLinkPriority_Object = MibTableColumn
tunnelLinkPriority = _TunnelLinkPriority_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9002, 1, 8),
    _TunnelLinkPriority_Type()
)
tunnelLinkPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelLinkPriority.setStatus("current")


class _TunnelProbState_Type(Integer32):
    """Custom type tunnelProbState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alive", 1),
          ("dead", 2),
          ("unknown", 0))
    )


_TunnelProbState_Type.__name__ = "Integer32"
_TunnelProbState_Object = MibTableColumn
tunnelProbState = _TunnelProbState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9002, 1, 9),
    _TunnelProbState_Type()
)
tunnelProbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelProbState.setStatus("current")


class _TunnelPeerType_Type(Integer32):
    """Custom type tunnelPeerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("daip", 2),
          ("regular", 1),
          ("robo", 3))
    )


_TunnelPeerType_Type.__name__ = "Integer32"
_TunnelPeerType_Object = MibTableColumn
tunnelPeerType = _TunnelPeerType_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9002, 1, 10),
    _TunnelPeerType_Type()
)
tunnelPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelPeerType.setStatus("current")


class _TunnelType_Type(Integer32):
    """Custom type tunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 2),
          ("regular", 1))
    )


_TunnelType_Type.__name__ = "Integer32"
_TunnelType_Object = MibTableColumn
tunnelType = _TunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9002, 1, 11),
    _TunnelType_Type()
)
tunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelType.setStatus("current")
_PermanentTunnelTable_Object = MibTable
permanentTunnelTable = _PermanentTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9003)
)
if mibBuilder.loadTexts:
    permanentTunnelTable.setStatus("current")
_PermanentTunnelEntry_Object = MibTableRow
permanentTunnelEntry = _PermanentTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9003, 1)
)
permanentTunnelEntry.setIndexNames(
    (0, "CHECKPOINT-MIB", "permanentTunnelPeerIpAddr"),
)
if mibBuilder.loadTexts:
    permanentTunnelEntry.setStatus("current")
_PermanentTunnelPeerIpAddr_Type = IpAddress
_PermanentTunnelPeerIpAddr_Object = MibTableColumn
permanentTunnelPeerIpAddr = _PermanentTunnelPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9003, 1, 1),
    _PermanentTunnelPeerIpAddr_Type()
)
permanentTunnelPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permanentTunnelPeerIpAddr.setStatus("current")
_PermanentTunnelPeerObjName_Type = DisplayString
_PermanentTunnelPeerObjName_Object = MibTableColumn
permanentTunnelPeerObjName = _PermanentTunnelPeerObjName_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9003, 1, 2),
    _PermanentTunnelPeerObjName_Type()
)
permanentTunnelPeerObjName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permanentTunnelPeerObjName.setStatus("current")


class _PermanentTunnelState_Type(Integer32):
    """Custom type permanentTunnelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              129,
              130,
              131,
              132)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("destroy", 4),
          ("down", 131),
          ("idle", 129),
          ("init", 132),
          ("phase1", 130))
    )


_PermanentTunnelState_Type.__name__ = "Integer32"
_PermanentTunnelState_Object = MibTableColumn
permanentTunnelState = _PermanentTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9003, 1, 3),
    _PermanentTunnelState_Type()
)
permanentTunnelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    permanentTunnelState.setStatus("current")
_PermanentTunnelCommunity_Type = DisplayString
_PermanentTunnelCommunity_Object = MibTableColumn
permanentTunnelCommunity = _PermanentTunnelCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9003, 1, 4),
    _PermanentTunnelCommunity_Type()
)
permanentTunnelCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permanentTunnelCommunity.setStatus("current")
_PermanentTunnelNextHop_Type = IpAddress
_PermanentTunnelNextHop_Object = MibTableColumn
permanentTunnelNextHop = _PermanentTunnelNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9003, 1, 5),
    _PermanentTunnelNextHop_Type()
)
permanentTunnelNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permanentTunnelNextHop.setStatus("current")
_PermanentTunnelInterface_Type = IpAddress
_PermanentTunnelInterface_Object = MibTableColumn
permanentTunnelInterface = _PermanentTunnelInterface_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9003, 1, 6),
    _PermanentTunnelInterface_Type()
)
permanentTunnelInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permanentTunnelInterface.setStatus("current")
_PermanentTunnelSourceIpAddr_Type = IpAddress
_PermanentTunnelSourceIpAddr_Object = MibTableColumn
permanentTunnelSourceIpAddr = _PermanentTunnelSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9003, 1, 7),
    _PermanentTunnelSourceIpAddr_Type()
)
permanentTunnelSourceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permanentTunnelSourceIpAddr.setStatus("current")


class _PermanentTunnelLinkPriority_Type(Integer32):
    """Custom type permanentTunnelLinkPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("on-demand", 2),
          ("primary", 0))
    )


_PermanentTunnelLinkPriority_Type.__name__ = "Integer32"
_PermanentTunnelLinkPriority_Object = MibTableColumn
permanentTunnelLinkPriority = _PermanentTunnelLinkPriority_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9003, 1, 8),
    _PermanentTunnelLinkPriority_Type()
)
permanentTunnelLinkPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permanentTunnelLinkPriority.setStatus("current")


class _PermanentTunnelProbState_Type(Integer32):
    """Custom type permanentTunnelProbState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alive", 1),
          ("dead", 2),
          ("unknown", 0))
    )


_PermanentTunnelProbState_Type.__name__ = "Integer32"
_PermanentTunnelProbState_Object = MibTableColumn
permanentTunnelProbState = _PermanentTunnelProbState_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9003, 1, 9),
    _PermanentTunnelProbState_Type()
)
permanentTunnelProbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permanentTunnelProbState.setStatus("current")


class _PermanentTunnelPeerType_Type(Integer32):
    """Custom type permanentTunnelPeerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("daip", 2),
          ("regular", 1),
          ("robo", 3))
    )


_PermanentTunnelPeerType_Type.__name__ = "Integer32"
_PermanentTunnelPeerType_Object = MibTableColumn
permanentTunnelPeerType = _PermanentTunnelPeerType_Object(
    (1, 3, 6, 1, 4, 1, 2620, 500, 9003, 1, 10),
    _PermanentTunnelPeerType_Type()
)
permanentTunnelPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permanentTunnelPeerType.setStatus("current")

# Managed Objects groups


# Notification objects

fwTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 1, 0, 1)
)
fwTrap.setObjects(
    ("CHECKPOINT-MIB", "fwEvent")
)
if mibBuilder.loadTexts:
    fwTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHECKPOINT-MIB",
    **{"checkpoint": checkpoint,
       "products": products,
       "fw": fw,
       "fwTrapPrefix": fwTrapPrefix,
       "fwTrap": fwTrap,
       "fwModuleState": fwModuleState,
       "fwFilterName": fwFilterName,
       "fwFilterDate": fwFilterDate,
       "fwAccepted": fwAccepted,
       "fwRejected": fwRejected,
       "fwDropped": fwDropped,
       "fwLogged": fwLogged,
       "fwMajor": fwMajor,
       "fwMinor": fwMinor,
       "fwProduct": fwProduct,
       "fwEvent": fwEvent,
       "fwSICTrustState": fwSICTrustState,
       "fwProdName": fwProdName,
       "fwVerMajor": fwVerMajor,
       "fwVerMinor": fwVerMinor,
       "fwKernelBuild": fwKernelBuild,
       "fwPolicyStat": fwPolicyStat,
       "fwPolicyName": fwPolicyName,
       "fwInstallTime": fwInstallTime,
       "fwNumConn": fwNumConn,
       "fwPeakNumConn": fwPeakNumConn,
       "fwIfTable": fwIfTable,
       "fwIfEntry": fwIfEntry,
       "fwIfIndex": fwIfIndex,
       "fwIfName": fwIfName,
       "fwAcceptPcktsIn": fwAcceptPcktsIn,
       "fwAcceptPcktsOut": fwAcceptPcktsOut,
       "fwAcceptBytesIn": fwAcceptBytesIn,
       "fwAcceptBytesOut": fwAcceptBytesOut,
       "fwDropPcktsIn": fwDropPcktsIn,
       "fwDropPcktsOut": fwDropPcktsOut,
       "fwRejectPcktsIn": fwRejectPcktsIn,
       "fwRejectPcktsOut": fwRejectPcktsOut,
       "fwLogIn": fwLogIn,
       "fwLogOut": fwLogOut,
       "fwPacketsRate": fwPacketsRate,
       "fwAcceptedBytesTotalRate": fwAcceptedBytesTotalRate,
       "fwDroppedBytesTotalRate": fwDroppedBytesTotalRate,
       "fwConnTableLimit": fwConnTableLimit,
       "fwDroppedTotalRate": fwDroppedTotalRate,
       "fwPerfStat": fwPerfStat,
       "fwHmem": fwHmem,
       "fwHmem-block-size": fwHmem_block_size,
       "fwHmem-requested-bytes": fwHmem_requested_bytes,
       "fwHmem-initial-allocated-bytes": fwHmem_initial_allocated_bytes,
       "fwHmem-initial-allocated-blocks": fwHmem_initial_allocated_blocks,
       "fwHmem-initial-allocated-pools": fwHmem_initial_allocated_pools,
       "fwHmem-current-allocated-bytes": fwHmem_current_allocated_bytes,
       "fwHmem-current-allocated-blocks": fwHmem_current_allocated_blocks,
       "fwHmem-current-allocated-pools": fwHmem_current_allocated_pools,
       "fwHmem-maximum-bytes": fwHmem_maximum_bytes,
       "fwHmem-maximum-pools": fwHmem_maximum_pools,
       "fwHmem-bytes-used": fwHmem_bytes_used,
       "fwHmem-blocks-used": fwHmem_blocks_used,
       "fwHmem-bytes-unused": fwHmem_bytes_unused,
       "fwHmem-blocks-unused": fwHmem_blocks_unused,
       "fwHmem-bytes-peak": fwHmem_bytes_peak,
       "fwHmem-blocks-peak": fwHmem_blocks_peak,
       "fwHmem-bytes-internal-use": fwHmem_bytes_internal_use,
       "fwHmem-number-of-items": fwHmem_number_of_items,
       "fwHmem-alloc-operations": fwHmem_alloc_operations,
       "fwHmem-free-operations": fwHmem_free_operations,
       "fwHmem-failed-alloc": fwHmem_failed_alloc,
       "fwHmem-failed-free": fwHmem_failed_free,
       "fwKmem": fwKmem,
       "fwKmem-system-physical-mem": fwKmem_system_physical_mem,
       "fwKmem-available-physical-mem": fwKmem_available_physical_mem,
       "fwKmem-aix-heap-size": fwKmem_aix_heap_size,
       "fwKmem-bytes-used": fwKmem_bytes_used,
       "fwKmem-blocking-bytes-used": fwKmem_blocking_bytes_used,
       "fwKmem-non-blocking-bytes-used": fwKmem_non_blocking_bytes_used,
       "fwKmem-bytes-unused": fwKmem_bytes_unused,
       "fwKmem-bytes-peak": fwKmem_bytes_peak,
       "fwKmem-blocking-bytes-peak": fwKmem_blocking_bytes_peak,
       "fwKmem-non-blocking-bytes-peak": fwKmem_non_blocking_bytes_peak,
       "fwKmem-bytes-internal-use": fwKmem_bytes_internal_use,
       "fwKmem-number-of-items": fwKmem_number_of_items,
       "fwKmem-alloc-operations": fwKmem_alloc_operations,
       "fwKmem-free-operations": fwKmem_free_operations,
       "fwKmem-failed-alloc": fwKmem_failed_alloc,
       "fwKmem-failed-free": fwKmem_failed_free,
       "fwInspect": fwInspect,
       "fwInspect-packets": fwInspect_packets,
       "fwInspect-operations": fwInspect_operations,
       "fwInspect-lookups": fwInspect_lookups,
       "fwInspect-record": fwInspect_record,
       "fwInspect-extract": fwInspect_extract,
       "fwCookies": fwCookies,
       "fwCookies-total": fwCookies_total,
       "fwCookies-allocfwCookies-total": fwCookies_allocfwCookies_total,
       "fwCookies-freefwCookies-total": fwCookies_freefwCookies_total,
       "fwCookies-dupfwCookies-total": fwCookies_dupfwCookies_total,
       "fwCookies-getfwCookies-total": fwCookies_getfwCookies_total,
       "fwCookies-putfwCookies-total": fwCookies_putfwCookies_total,
       "fwCookies-lenfwCookies-total": fwCookies_lenfwCookies_total,
       "fwChains": fwChains,
       "fwChains-alloc": fwChains_alloc,
       "fwChains-free": fwChains_free,
       "fwFragments": fwFragments,
       "fwFrag-fragments": fwFrag_fragments,
       "fwFrag-expired": fwFrag_expired,
       "fwFrag-packets": fwFrag_packets,
       "fwUfp": fwUfp,
       "fwUfpHitRatio": fwUfpHitRatio,
       "fwUfpInspected": fwUfpInspected,
       "fwUfpHits": fwUfpHits,
       "fwSS": fwSS,
       "fwSS-http": fwSS_http,
       "fwSS-http-pid": fwSS_http_pid,
       "fwSS-http-proto": fwSS_http_proto,
       "fwSS-http-port": fwSS_http_port,
       "fwSS-http-logical-port": fwSS_http_logical_port,
       "fwSS-http-max-avail-socket": fwSS_http_max_avail_socket,
       "fwSS-http-socket-in-use-max": fwSS_http_socket_in_use_max,
       "fwSS-http-socket-in-use-curr": fwSS_http_socket_in_use_curr,
       "fwSS-http-socket-in-use-count": fwSS_http_socket_in_use_count,
       "fwSS-http-sess-max": fwSS_http_sess_max,
       "fwSS-http-sess-curr": fwSS_http_sess_curr,
       "fwSS-http-sess-count": fwSS_http_sess_count,
       "fwSS-http-auth-sess-max": fwSS_http_auth_sess_max,
       "fwSS-http-auth-sess-curr": fwSS_http_auth_sess_curr,
       "fwSS-http-auth-sess-count": fwSS_http_auth_sess_count,
       "fwSS-http-accepted-sess": fwSS_http_accepted_sess,
       "fwSS-http-rejected-sess": fwSS_http_rejected_sess,
       "fwSS-http-auth-failures": fwSS_http_auth_failures,
       "fwSS-http-ops-cvp-sess-max": fwSS_http_ops_cvp_sess_max,
       "fwSS-http-ops-cvp-sess-curr": fwSS_http_ops_cvp_sess_curr,
       "fwSS-http-ops-cvp-sess-count": fwSS_http_ops_cvp_sess_count,
       "fwSS-http-ops-cvp-rej-sess": fwSS_http_ops_cvp_rej_sess,
       "fwSS-http-ssl-encryp-sess-max": fwSS_http_ssl_encryp_sess_max,
       "fwSS-http-ssl-encryp-sess-curr": fwSS_http_ssl_encryp_sess_curr,
       "fwSS-http-ssl-encryp-sess-count": fwSS_http_ssl_encryp_sess_count,
       "fwSS-http-transp-sess-max": fwSS_http_transp_sess_max,
       "fwSS-http-transp-sess-curr": fwSS_http_transp_sess_curr,
       "fwSS-http-transp-sess-count": fwSS_http_transp_sess_count,
       "fwSS-http-proxied-sess-max": fwSS_http_proxied_sess_max,
       "fwSS-http-proxied-sess-curr": fwSS_http_proxied_sess_curr,
       "fwSS-http-proxied-sess-count": fwSS_http_proxied_sess_count,
       "fwSS-http-tunneled-sess-max": fwSS_http_tunneled_sess_max,
       "fwSS-http-tunneled-sess-curr": fwSS_http_tunneled_sess_curr,
       "fwSS-http-tunneled-sess-count": fwSS_http_tunneled_sess_count,
       "fwSS-http-ftp-sess-max": fwSS_http_ftp_sess_max,
       "fwSS-http-ftp-sess-curr": fwSS_http_ftp_sess_curr,
       "fwSS-http-ftp-sess-count": fwSS_http_ftp_sess_count,
       "fwSS-http-time-stamp": fwSS_http_time_stamp,
       "fwSS-http-is-alive": fwSS_http_is_alive,
       "fwSS-http-blocked-cnt": fwSS_http_blocked_cnt,
       "fwSS-http-blocked-total": fwSS_http_blocked_total,
       "fwSS-http-scanned-total": fwSS_http_scanned_total,
       "fwSS-http-blocked-by-file-type": fwSS_http_blocked_by_file_type,
       "fwSS-http-blocked-by-size-limit": fwSS_http_blocked_by_size_limit,
       "fwSS-http-blocked-by-archive-limit": fwSS_http_blocked_by_archive_limit,
       "fwSS-http-blocked-by-internal-error": fwSS_http_blocked_by_internal_error,
       "fwSS-http-passed-cnt": fwSS_http_passed_cnt,
       "fwSS-http-passed-by-file-type": fwSS_http_passed_by_file_type,
       "fwSS-http-passed-by-size-limit": fwSS_http_passed_by_size_limit,
       "fwSS-http-passed-by-archive-limit": fwSS_http_passed_by_archive_limit,
       "fwSS-http-passed-by-internal-error": fwSS_http_passed_by_internal_error,
       "fwSS-http-passed-total": fwSS_http_passed_total,
       "fwSS-http-blocked-by-AV-settings": fwSS_http_blocked_by_AV_settings,
       "fwSS-http-passed-by-AV-settings": fwSS_http_passed_by_AV_settings,
       "fwSS-http-blocked-by-URL-filter-category": fwSS_http_blocked_by_URL_filter_category,
       "fwSS-http-blocked-by-URL-block-list": fwSS_http_blocked_by_URL_block_list,
       "fwSS-http-passed-by-URL-allow-list": fwSS_http_passed_by_URL_allow_list,
       "fwSS-http-passed-by-URL-filter-category": fwSS_http_passed_by_URL_filter_category,
       "fwSS-ftp": fwSS_ftp,
       "fwSS-ftp-pid": fwSS_ftp_pid,
       "fwSS-ftp-proto": fwSS_ftp_proto,
       "fwSS-ftp-port": fwSS_ftp_port,
       "fwSS-ftp-logical-port": fwSS_ftp_logical_port,
       "fwSS-ftp-max-avail-socket": fwSS_ftp_max_avail_socket,
       "fwSS-ftp-socket-in-use-max": fwSS_ftp_socket_in_use_max,
       "fwSS-ftp-socket-in-use-curr": fwSS_ftp_socket_in_use_curr,
       "fwSS-ftp-socket-in-use-count": fwSS_ftp_socket_in_use_count,
       "fwSS-ftp-sess-max": fwSS_ftp_sess_max,
       "fwSS-ftp-sess-curr": fwSS_ftp_sess_curr,
       "fwSS-ftp-sess-count": fwSS_ftp_sess_count,
       "fwSS-ftp-auth-sess-max": fwSS_ftp_auth_sess_max,
       "fwSS-ftp-auth-sess-curr": fwSS_ftp_auth_sess_curr,
       "fwSS-ftp-auth-sess-count": fwSS_ftp_auth_sess_count,
       "fwSS-ftp-accepted-sess": fwSS_ftp_accepted_sess,
       "fwSS-ftp-rejected-sess": fwSS_ftp_rejected_sess,
       "fwSS-ftp-auth-failures": fwSS_ftp_auth_failures,
       "fwSS-ftp-ops-cvp-sess-max": fwSS_ftp_ops_cvp_sess_max,
       "fwSS-ftp-ops-cvp-sess-curr": fwSS_ftp_ops_cvp_sess_curr,
       "fwSS-ftp-ops-cvp-sess-count": fwSS_ftp_ops_cvp_sess_count,
       "fwSS-ftp-ops-cvp-rej-sess": fwSS_ftp_ops_cvp_rej_sess,
       "fwSS-ftp-time-stamp": fwSS_ftp_time_stamp,
       "fwSS-ftp-is-alive": fwSS_ftp_is_alive,
       "fwSS-ftp-blocked-cnt": fwSS_ftp_blocked_cnt,
       "fwSS-ftp-blocked-total": fwSS_ftp_blocked_total,
       "fwSS-ftp-scanned-total": fwSS_ftp_scanned_total,
       "fwSS-ftp-blocked-by-file-type": fwSS_ftp_blocked_by_file_type,
       "fwSS-ftp-blocked-by-size-limit": fwSS_ftp_blocked_by_size_limit,
       "fwSS-ftp-blocked-by-archive-limit": fwSS_ftp_blocked_by_archive_limit,
       "fwSS-ftp-blocked-by-internal-error": fwSS_ftp_blocked_by_internal_error,
       "fwSS-ftp-passed-cnt": fwSS_ftp_passed_cnt,
       "fwSS-ftp-passed-by-file-type": fwSS_ftp_passed_by_file_type,
       "fwSS-ftp-passed-by-size-limit": fwSS_ftp_passed_by_size_limit,
       "fwSS-ftp-passed-by-archive-limit": fwSS_ftp_passed_by_archive_limit,
       "fwSS-ftp-passed-by-internal-error": fwSS_ftp_passed_by_internal_error,
       "fwSS-ftp-passed-total": fwSS_ftp_passed_total,
       "fwSS-ftp-blocked-by-AV-settings": fwSS_ftp_blocked_by_AV_settings,
       "fwSS-ftp-passed-by-AV-settings": fwSS_ftp_passed_by_AV_settings,
       "fwSS-telnet": fwSS_telnet,
       "fwSS-telnet-pid": fwSS_telnet_pid,
       "fwSS-telnet-proto": fwSS_telnet_proto,
       "fwSS-telnet-port": fwSS_telnet_port,
       "fwSS-telnet-logical-port": fwSS_telnet_logical_port,
       "fwSS-telnet-max-avail-socket": fwSS_telnet_max_avail_socket,
       "fwSS-telnet-socket-in-use-max": fwSS_telnet_socket_in_use_max,
       "fwSS-telnet-socket-in-use-curr": fwSS_telnet_socket_in_use_curr,
       "fwSS-telnet-socket-in-use-count": fwSS_telnet_socket_in_use_count,
       "fwSS-telnet-sess-max": fwSS_telnet_sess_max,
       "fwSS-telnet-sess-curr": fwSS_telnet_sess_curr,
       "fwSS-telnet-sess-count": fwSS_telnet_sess_count,
       "fwSS-telnet-auth-sess-max": fwSS_telnet_auth_sess_max,
       "fwSS-telnet-auth-sess-curr": fwSS_telnet_auth_sess_curr,
       "fwSS-telnet-auth-sess-count": fwSS_telnet_auth_sess_count,
       "fwSS-telnet-accepted-sess": fwSS_telnet_accepted_sess,
       "fwSS-telnet-rejected-sess": fwSS_telnet_rejected_sess,
       "fwSS-telnet-auth-failures": fwSS_telnet_auth_failures,
       "fwSS-telnet-time-stamp": fwSS_telnet_time_stamp,
       "fwSS-telnet-is-alive": fwSS_telnet_is_alive,
       "fwSS-rlogin": fwSS_rlogin,
       "fwSS-rlogin-pid": fwSS_rlogin_pid,
       "fwSS-rlogin-proto": fwSS_rlogin_proto,
       "fwSS-rlogin-port": fwSS_rlogin_port,
       "fwSS-rlogin-logical-port": fwSS_rlogin_logical_port,
       "fwSS-rlogin-max-avail-socket": fwSS_rlogin_max_avail_socket,
       "fwSS-rlogin-socket-in-use-max": fwSS_rlogin_socket_in_use_max,
       "fwSS-rlogin-socket-in-use-curr": fwSS_rlogin_socket_in_use_curr,
       "fwSS-rlogin-socket-in-use-count": fwSS_rlogin_socket_in_use_count,
       "fwSS-rlogin-sess-max": fwSS_rlogin_sess_max,
       "fwSS-rlogin-sess-curr": fwSS_rlogin_sess_curr,
       "fwSS-rlogin-sess-count": fwSS_rlogin_sess_count,
       "fwSS-rlogin-auth-sess-max": fwSS_rlogin_auth_sess_max,
       "fwSS-rlogin-auth-sess-curr": fwSS_rlogin_auth_sess_curr,
       "fwSS-rlogin-auth-sess-count": fwSS_rlogin_auth_sess_count,
       "fwSS-rlogin-accepted-sess": fwSS_rlogin_accepted_sess,
       "fwSS-rlogin-rejected-sess": fwSS_rlogin_rejected_sess,
       "fwSS-rlogin-auth-failures": fwSS_rlogin_auth_failures,
       "fwSS-rlogin-time-stamp": fwSS_rlogin_time_stamp,
       "fwSS-rlogin-is-alive": fwSS_rlogin_is_alive,
       "fwSS-ufp": fwSS_ufp,
       "fwSS-ufp-ops-ufp-sess-max": fwSS_ufp_ops_ufp_sess_max,
       "fwSS-ufp-ops-ufp-sess-curr": fwSS_ufp_ops_ufp_sess_curr,
       "fwSS-ufp-ops-ufp-sess-count": fwSS_ufp_ops_ufp_sess_count,
       "fwSS-ufp-ops-ufp-rej-sess": fwSS_ufp_ops_ufp_rej_sess,
       "fwSS-ufp-time-stamp": fwSS_ufp_time_stamp,
       "fwSS-ufp-is-alive": fwSS_ufp_is_alive,
       "fwSS-smtp": fwSS_smtp,
       "fwSS-smtp-pid": fwSS_smtp_pid,
       "fwSS-smtp-proto": fwSS_smtp_proto,
       "fwSS-smtp-port": fwSS_smtp_port,
       "fwSS-smtp-logical-port": fwSS_smtp_logical_port,
       "fwSS-smtp-max-avail-socket": fwSS_smtp_max_avail_socket,
       "fwSS-smtp-socket-in-use-max": fwSS_smtp_socket_in_use_max,
       "fwSS-smtp-socket-in-use-curr": fwSS_smtp_socket_in_use_curr,
       "fwSS-smtp-socket-in-use-count": fwSS_smtp_socket_in_use_count,
       "fwSS-smtp-sess-max": fwSS_smtp_sess_max,
       "fwSS-smtp-sess-curr": fwSS_smtp_sess_curr,
       "fwSS-smtp-sess-count": fwSS_smtp_sess_count,
       "fwSS-smtp-auth-sess-max": fwSS_smtp_auth_sess_max,
       "fwSS-smtp-auth-sess-curr": fwSS_smtp_auth_sess_curr,
       "fwSS-smtp-auth-sess-count": fwSS_smtp_auth_sess_count,
       "fwSS-smtp-accepted-sess": fwSS_smtp_accepted_sess,
       "fwSS-smtp-rejected-sess": fwSS_smtp_rejected_sess,
       "fwSS-smtp-auth-failures": fwSS_smtp_auth_failures,
       "fwSS-smtp-mail-max": fwSS_smtp_mail_max,
       "fwSS-smtp-mail-curr": fwSS_smtp_mail_curr,
       "fwSS-smtp-mail-count": fwSS_smtp_mail_count,
       "fwSS-smtp-outgoing-mail-max": fwSS_smtp_outgoing_mail_max,
       "fwSS-smtp-outgoing-mail-curr": fwSS_smtp_outgoing_mail_curr,
       "fwSS-smtp-outgoing-mail-count": fwSS_smtp_outgoing_mail_count,
       "fwSS-smtp-max-mail-on-conn": fwSS_smtp_max_mail_on_conn,
       "fwSS-smtp-total-mails": fwSS_smtp_total_mails,
       "fwSS-smtp-time-stamp": fwSS_smtp_time_stamp,
       "fwSS-smtp-is-alive": fwSS_smtp_is_alive,
       "fwSS-smtp-blocked-cnt": fwSS_smtp_blocked_cnt,
       "fwSS-smtp-blocked-total": fwSS_smtp_blocked_total,
       "fwSS-smtp-scanned-total": fwSS_smtp_scanned_total,
       "fwSS-smtp-blocked-by-file-type": fwSS_smtp_blocked_by_file_type,
       "fwSS-smtp-blocked-by-size-limit": fwSS_smtp_blocked_by_size_limit,
       "fwSS-smtp-blocked-by-archive-limit": fwSS_smtp_blocked_by_archive_limit,
       "fwSS-smtp-blocked-by-internal-error": fwSS_smtp_blocked_by_internal_error,
       "fwSS-smtp-passed-cnt": fwSS_smtp_passed_cnt,
       "fwSS-smtp-passed-by-file-type": fwSS_smtp_passed_by_file_type,
       "fwSS-smtp-passed-by-size-limit": fwSS_smtp_passed_by_size_limit,
       "fwSS-smtp-passed-by-archive-limit": fwSS_smtp_passed_by_archive_limit,
       "fwSS-smtp-passed-by-internal-error": fwSS_smtp_passed_by_internal_error,
       "fwSS-smtp-passed-total": fwSS_smtp_passed_total,
       "fwSS-smtp-blocked-by-AV-settings": fwSS_smtp_blocked_by_AV_settings,
       "fwSS-smtp-passed-by-AV-settings": fwSS_smtp_passed_by_AV_settings,
       "fwSS-POP3": fwSS_POP3,
       "fwSS-POP3-pid": fwSS_POP3_pid,
       "fwSS-POP3-proto": fwSS_POP3_proto,
       "fwSS-POP3-port": fwSS_POP3_port,
       "fwSS-POP3-logical-port": fwSS_POP3_logical_port,
       "fwSS-POP3-max-avail-socket": fwSS_POP3_max_avail_socket,
       "fwSS-POP3-socket-in-use-max": fwSS_POP3_socket_in_use_max,
       "fwSS-POP3-socket-in-use-curr": fwSS_POP3_socket_in_use_curr,
       "fwSS-POP3-socket-in-use-count": fwSS_POP3_socket_in_use_count,
       "fwSS-POP3-sess-max": fwSS_POP3_sess_max,
       "fwSS-POP3-sess-curr": fwSS_POP3_sess_curr,
       "fwSS-POP3-sess-count": fwSS_POP3_sess_count,
       "fwSS-POP3-auth-sess-max": fwSS_POP3_auth_sess_max,
       "fwSS-POP3-auth-sess-curr": fwSS_POP3_auth_sess_curr,
       "fwSS-POP3-auth-sess-count": fwSS_POP3_auth_sess_count,
       "fwSS-POP3-accepted-sess": fwSS_POP3_accepted_sess,
       "fwSS-POP3-rejected-sess": fwSS_POP3_rejected_sess,
       "fwSS-POP3-auth-failures": fwSS_POP3_auth_failures,
       "fwSS-POP3-mail-max": fwSS_POP3_mail_max,
       "fwSS-POP3-mail-curr": fwSS_POP3_mail_curr,
       "fwSS-POP3-mail-count": fwSS_POP3_mail_count,
       "fwSS-POP3-outgoing-mail-max": fwSS_POP3_outgoing_mail_max,
       "fwSS-POP3-outgoing-mail-curr": fwSS_POP3_outgoing_mail_curr,
       "fwSS-POP3-outgoing-mail-count": fwSS_POP3_outgoing_mail_count,
       "fwSS-POP3-max-mail-on-conn": fwSS_POP3_max_mail_on_conn,
       "fwSS-POP3-total-mails": fwSS_POP3_total_mails,
       "fwSS-POP3-time-stamp": fwSS_POP3_time_stamp,
       "fwSS-POP3-is-alive": fwSS_POP3_is_alive,
       "fwSS-POP3-blocked-cnt": fwSS_POP3_blocked_cnt,
       "fwSS-POP3-blocked-total": fwSS_POP3_blocked_total,
       "fwSS-POP3-scanned-total": fwSS_POP3_scanned_total,
       "fwSS-POP3-blocked-by-file-type": fwSS_POP3_blocked_by_file_type,
       "fwSS-POP3-blocked-by-size-limit": fwSS_POP3_blocked_by_size_limit,
       "fwSS-POP3-blocked-by-archive-limit": fwSS_POP3_blocked_by_archive_limit,
       "fwSS-POP3-blocked-by-internal-error": fwSS_POP3_blocked_by_internal_error,
       "fwSS-POP3-passed-cnt": fwSS_POP3_passed_cnt,
       "fwSS-POP3-passed-by-file-type": fwSS_POP3_passed_by_file_type,
       "fwSS-POP3-passed-by-size-limit": fwSS_POP3_passed_by_size_limit,
       "fwSS-POP3-passed-by-archive-limit": fwSS_POP3_passed_by_archive_limit,
       "fwSS-POP3-passed-by-internal-error": fwSS_POP3_passed_by_internal_error,
       "fwSS-POP3-passed-total": fwSS_POP3_passed_total,
       "fwSS-POP3-blocked-by-AV-settings": fwSS_POP3_blocked_by_AV_settings,
       "fwSS-POP3-passed-by-AV-settings": fwSS_POP3_passed_by_AV_settings,
       "fwSS-av-total": fwSS_av_total,
       "fwSS-total-blocked-by-av": fwSS_total_blocked_by_av,
       "fwSS-total-blocked": fwSS_total_blocked,
       "fwSS-total-scanned": fwSS_total_scanned,
       "fwSS-total-blocked-by-file-type": fwSS_total_blocked_by_file_type,
       "fwSS-total-blocked-by-size-limit": fwSS_total_blocked_by_size_limit,
       "fwSS-total-blocked-by-archive-limit": fwSS_total_blocked_by_archive_limit,
       "fwSS-total-blocked-by-interal-error": fwSS_total_blocked_by_interal_error,
       "fwSS-total-passed-by-av": fwSS_total_passed_by_av,
       "fwSS-total-passed-by-file-type": fwSS_total_passed_by_file_type,
       "fwSS-total-passed-by-size-limit": fwSS_total_passed_by_size_limit,
       "fwSS-total-passed-by-archive-limit": fwSS_total_passed_by_archive_limit,
       "fwSS-total-passed-by-interal-error": fwSS_total_passed_by_interal_error,
       "fwSS-total-passed": fwSS_total_passed,
       "fwSS-total-blocked-by-av-settings": fwSS_total_blocked_by_av_settings,
       "fwSS-total-passed-by-av-settings": fwSS_total_passed_by_av_settings,
       "fwConnectionsStat": fwConnectionsStat,
       "fwConnectionsStatConnectionsTcp": fwConnectionsStatConnectionsTcp,
       "fwConnectionsStatConnectionsUdp": fwConnectionsStatConnectionsUdp,
       "fwConnectionsStatConnectionsIcmp": fwConnectionsStatConnectionsIcmp,
       "fwConnectionsStatConnectionsOther": fwConnectionsStatConnectionsOther,
       "fwConnectionsStatConnections": fwConnectionsStatConnections,
       "fwConnectionsStatConnectionRate": fwConnectionsStatConnectionRate,
       "fwHmem64": fwHmem64,
       "fwHmem64-block-size": fwHmem64_block_size,
       "fwHmem64-requested-bytes": fwHmem64_requested_bytes,
       "fwHmem64-initial-allocated-bytes": fwHmem64_initial_allocated_bytes,
       "fwHmem64-initial-allocated-blocks": fwHmem64_initial_allocated_blocks,
       "fwHmem64-initial-allocated-pools": fwHmem64_initial_allocated_pools,
       "fwHmem64-current-allocated-bytes": fwHmem64_current_allocated_bytes,
       "fwHmem64-current-allocated-blocks": fwHmem64_current_allocated_blocks,
       "fwHmem64-current-allocated-pools": fwHmem64_current_allocated_pools,
       "fwHmem64-maximum-bytes": fwHmem64_maximum_bytes,
       "fwHmem64-maximum-pools": fwHmem64_maximum_pools,
       "fwHmem64-bytes-used": fwHmem64_bytes_used,
       "fwHmem64-blocks-used": fwHmem64_blocks_used,
       "fwHmem64-bytes-unused": fwHmem64_bytes_unused,
       "fwHmem64-blocks-unused": fwHmem64_blocks_unused,
       "fwHmem64-bytes-peak": fwHmem64_bytes_peak,
       "fwHmem64-blocks-peak": fwHmem64_blocks_peak,
       "fwHmem64-bytes-internal-use": fwHmem64_bytes_internal_use,
       "fwHmem64-number-of-items": fwHmem64_number_of_items,
       "fwHmem64-alloc-operations": fwHmem64_alloc_operations,
       "fwHmem64-free-operations": fwHmem64_free_operations,
       "fwHmem64-failed-alloc": fwHmem64_failed_alloc,
       "fwHmem64-failed-free": fwHmem64_failed_free,
       "fwNetIfTable": fwNetIfTable,
       "fwNetIfEntry": fwNetIfEntry,
       "fwNetIfIndex": fwNetIfIndex,
       "fwNetIfName": fwNetIfName,
       "fwNetIfIPAddr": fwNetIfIPAddr,
       "fwNetIfNetmask": fwNetIfNetmask,
       "fwNetIfFlags": fwNetIfFlags,
       "fwNetIfPeerName": fwNetIfPeerName,
       "fwNetIfRemoteIp": fwNetIfRemoteIp,
       "fwNetIfTopology": fwNetIfTopology,
       "fwNetIfProxyName": fwNetIfProxyName,
       "fwNetIfSlaves": fwNetIfSlaves,
       "fwNetIfPorts": fwNetIfPorts,
       "fwLSConn": fwLSConn,
       "fwLSConnOverall": fwLSConnOverall,
       "fwLSConnOverallDesc": fwLSConnOverallDesc,
       "fwLSConnTable": fwLSConnTable,
       "fwLSConnEntry": fwLSConnEntry,
       "fwLSConnIndex": fwLSConnIndex,
       "fwLSConnName": fwLSConnName,
       "fwLSConnState": fwLSConnState,
       "fwLSConnStateDesc": fwLSConnStateDesc,
       "fwLocalLoggingDesc": fwLocalLoggingDesc,
       "fwLocalLoggingStat": fwLocalLoggingStat,
       "vpn": vpn,
       "cpvProdName": cpvProdName,
       "cpvVerMajor": cpvVerMajor,
       "cpvVerMinor": cpvVerMinor,
       "cpvGeneral": cpvGeneral,
       "cpvStatistics": cpvStatistics,
       "cpvEncPackets": cpvEncPackets,
       "cpvDecPackets": cpvDecPackets,
       "cpvErrors": cpvErrors,
       "cpvErrOut": cpvErrOut,
       "cpvErrIn": cpvErrIn,
       "cpvErrIke": cpvErrIke,
       "cpvErrPolicy": cpvErrPolicy,
       "cpvIpsec": cpvIpsec,
       "cpvSaStatistics": cpvSaStatistics,
       "cpvCurrEspSAsIn": cpvCurrEspSAsIn,
       "cpvTotalEspSAsIn": cpvTotalEspSAsIn,
       "cpvCurrEspSAsOut": cpvCurrEspSAsOut,
       "cpvTotalEspSAsOut": cpvTotalEspSAsOut,
       "cpvCurrAhSAsIn": cpvCurrAhSAsIn,
       "cpvTotalAhSAsIn": cpvTotalAhSAsIn,
       "cpvCurrAhSAsOut": cpvCurrAhSAsOut,
       "cpvTotalAhSAsOut": cpvTotalAhSAsOut,
       "cpvMaxConncurEspSAsIn": cpvMaxConncurEspSAsIn,
       "cpvMaxConncurEspSAsOut": cpvMaxConncurEspSAsOut,
       "cpvMaxConncurAhSAsIn": cpvMaxConncurAhSAsIn,
       "cpvMaxConncurAhSAsOut": cpvMaxConncurAhSAsOut,
       "cpvSaErrors": cpvSaErrors,
       "cpvSaDecrErr": cpvSaDecrErr,
       "cpvSaAuthErr": cpvSaAuthErr,
       "cpvSaReplayErr": cpvSaReplayErr,
       "cpvSaPolicyErr": cpvSaPolicyErr,
       "cpvSaOtherErrIn": cpvSaOtherErrIn,
       "cpvSaOtherErrOut": cpvSaOtherErrOut,
       "cpvSaUnknownSpiErr": cpvSaUnknownSpiErr,
       "cpvIpsecStatistics": cpvIpsecStatistics,
       "cpvIpsecUdpEspEncPkts": cpvIpsecUdpEspEncPkts,
       "cpvIpsecUdpEspDecPkts": cpvIpsecUdpEspDecPkts,
       "cpvIpsecAhEncPkts": cpvIpsecAhEncPkts,
       "cpvIpsecAhDecPkts": cpvIpsecAhDecPkts,
       "cpvIpsecEspEncPkts": cpvIpsecEspEncPkts,
       "cpvIpsecEspDecPkts": cpvIpsecEspDecPkts,
       "cpvIpsecDecomprBytesBefore": cpvIpsecDecomprBytesBefore,
       "cpvIpsecDecomprBytesAfter": cpvIpsecDecomprBytesAfter,
       "cpvIpsecDecomprOverhead": cpvIpsecDecomprOverhead,
       "cpvIpsecDecomprPkts": cpvIpsecDecomprPkts,
       "cpvIpsecDecomprErr": cpvIpsecDecomprErr,
       "cpvIpsecComprBytesBefore": cpvIpsecComprBytesBefore,
       "cpvIpsecComprBytesAfter": cpvIpsecComprBytesAfter,
       "cpvIpsecComprOverhead": cpvIpsecComprOverhead,
       "cpvIpsecNonCompressibleBytes": cpvIpsecNonCompressibleBytes,
       "cpvIpsecCompressiblePkts": cpvIpsecCompressiblePkts,
       "cpvIpsecNonCompressiblePkts": cpvIpsecNonCompressiblePkts,
       "cpvIpsecComprErrors": cpvIpsecComprErrors,
       "cpvIpsecEspEncBytes": cpvIpsecEspEncBytes,
       "cpvIpsecEspDecBytes": cpvIpsecEspDecBytes,
       "cpvFwz": cpvFwz,
       "cpvFwzStatistics": cpvFwzStatistics,
       "cpvFwzEncapsEncPkts": cpvFwzEncapsEncPkts,
       "cpvFwzEncapsDecPkts": cpvFwzEncapsDecPkts,
       "cpvFwzEncPkts": cpvFwzEncPkts,
       "cpvFwzDecPkts": cpvFwzDecPkts,
       "cpvFwzErrors": cpvFwzErrors,
       "cpvFwzEncapsEncErrs": cpvFwzEncapsEncErrs,
       "cpvFwzEncapsDecErrs": cpvFwzEncapsDecErrs,
       "cpvFwzEncErrs": cpvFwzEncErrs,
       "cpvFwzDecErrs": cpvFwzDecErrs,
       "cpvAccelerator": cpvAccelerator,
       "cpvHwAccelGeneral": cpvHwAccelGeneral,
       "cpvHwAccelVendor": cpvHwAccelVendor,
       "cpvHwAccelStatus": cpvHwAccelStatus,
       "cpvHwAccelDriverMajorVer": cpvHwAccelDriverMajorVer,
       "cpvHwAccelDriverMinorVer": cpvHwAccelDriverMinorVer,
       "cpvHwAccelStatistics": cpvHwAccelStatistics,
       "cpvHwAccelEspEncPkts": cpvHwAccelEspEncPkts,
       "cpvHwAccelEspDecPkts": cpvHwAccelEspDecPkts,
       "cpvHwAccelEspEncBytes": cpvHwAccelEspEncBytes,
       "cpvHwAccelEspDecBytes": cpvHwAccelEspDecBytes,
       "cpvHwAccelAhEncPkts": cpvHwAccelAhEncPkts,
       "cpvHwAccelAhDecPkts": cpvHwAccelAhDecPkts,
       "cpvHwAccelAhEncBytes": cpvHwAccelAhEncBytes,
       "cpvHwAccelAhDecBytes": cpvHwAccelAhDecBytes,
       "cpvIKE": cpvIKE,
       "cpvIKEglobals": cpvIKEglobals,
       "cpvIKECurrSAs": cpvIKECurrSAs,
       "cpvIKECurrInitSAs": cpvIKECurrInitSAs,
       "cpvIKECurrRespSAs": cpvIKECurrRespSAs,
       "cpvIKETotalSAs": cpvIKETotalSAs,
       "cpvIKETotalInitSAs": cpvIKETotalInitSAs,
       "cpvIKETotalRespSAs": cpvIKETotalRespSAs,
       "cpvIKETotalSAsAttempts": cpvIKETotalSAsAttempts,
       "cpvIKETotalSAsInitAttempts": cpvIKETotalSAsInitAttempts,
       "cpvIKETotalSAsRespAttempts": cpvIKETotalSAsRespAttempts,
       "cpvIKEMaxConncurSAs": cpvIKEMaxConncurSAs,
       "cpvIKEMaxConncurInitSAs": cpvIKEMaxConncurInitSAs,
       "cpvIKEMaxConncurRespSAs": cpvIKEMaxConncurRespSAs,
       "cpvIKEerrors": cpvIKEerrors,
       "cpvIKETotalFailuresInit": cpvIKETotalFailuresInit,
       "cpvIKENoResp": cpvIKENoResp,
       "cpvIKETotalFailuresResp": cpvIKETotalFailuresResp,
       "cpvIPsec": cpvIPsec,
       "cpvIPsecNIC": cpvIPsecNIC,
       "cpvIPsecNICsNum": cpvIPsecNICsNum,
       "cpvIPsecNICTotalDownLoadedSAs": cpvIPsecNICTotalDownLoadedSAs,
       "cpvIPsecNICCurrDownLoadedSAs": cpvIPsecNICCurrDownLoadedSAs,
       "cpvIPsecNICDecrBytes": cpvIPsecNICDecrBytes,
       "cpvIPsecNICEncrBytes": cpvIPsecNICEncrBytes,
       "cpvIPsecNICDecrPackets": cpvIPsecNICDecrPackets,
       "cpvIPsecNICEncrPackets": cpvIPsecNICEncrPackets,
       "fg": fg,
       "fgProdName": fgProdName,
       "fgVerMajor": fgVerMajor,
       "fgVerMinor": fgVerMinor,
       "fgVersionString": fgVersionString,
       "fgModuleKernelBuild": fgModuleKernelBuild,
       "fgStrPolicyName": fgStrPolicyName,
       "fgInstallTime": fgInstallTime,
       "fgNumInterfaces": fgNumInterfaces,
       "fgIfTable": fgIfTable,
       "fgIfEntry": fgIfEntry,
       "fgIfIndex": fgIfIndex,
       "fgIfName": fgIfName,
       "fgPolicyName": fgPolicyName,
       "fgRateLimitIn": fgRateLimitIn,
       "fgRateLimitOut": fgRateLimitOut,
       "fgAvrRateIn": fgAvrRateIn,
       "fgAvrRateOut": fgAvrRateOut,
       "fgRetransPcktsIn": fgRetransPcktsIn,
       "fgRetransPcktsOut": fgRetransPcktsOut,
       "fgPendPcktsIn": fgPendPcktsIn,
       "fgPendPcktsOut": fgPendPcktsOut,
       "fgPendBytesIn": fgPendBytesIn,
       "fgPendBytesOut": fgPendBytesOut,
       "fgNumConnIn": fgNumConnIn,
       "fgNumConnOut": fgNumConnOut,
       "ha": ha,
       "haProdName": haProdName,
       "haInstalled": haInstalled,
       "haVerMajor": haVerMajor,
       "haVerMinor": haVerMinor,
       "haStarted": haStarted,
       "haState": haState,
       "haBlockState": haBlockState,
       "haIdentifier": haIdentifier,
       "haProtoVersion": haProtoVersion,
       "haWorkMode": haWorkMode,
       "haIfTable": haIfTable,
       "haIfEntry": haIfEntry,
       "haIfIndex": haIfIndex,
       "haIfName": haIfName,
       "haIP": haIP,
       "haStatus": haStatus,
       "haVerified": haVerified,
       "haTrusted": haTrusted,
       "haShared": haShared,
       "haProblemTable": haProblemTable,
       "haProblemEntry": haProblemEntry,
       "haProblemIndex": haProblemIndex,
       "haProblemName": haProblemName,
       "haProblemStatus": haProblemStatus,
       "haProblemPriority": haProblemPriority,
       "haProblemVerified": haProblemVerified,
       "haProblemDescr": haProblemDescr,
       "haVersionSting": haVersionSting,
       "haClusterIpTable": haClusterIpTable,
       "haClusterIpEntry": haClusterIpEntry,
       "haClusterIpIndex": haClusterIpIndex,
       "haClusterIpIfName": haClusterIpIfName,
       "haClusterIpAddr": haClusterIpAddr,
       "haClusterIpNetMask": haClusterIpNetMask,
       "haClusterIpMemberNet": haClusterIpMemberNet,
       "haClusterIpMemberNetMask": haClusterIpMemberNetMask,
       "haClusterSyncTable": haClusterSyncTable,
       "haClusterSyncEntry": haClusterSyncEntry,
       "haClusterSyncIndex": haClusterSyncIndex,
       "haClusterSyncName": haClusterSyncName,
       "haClusterSyncAddr": haClusterSyncAddr,
       "haClusterSyncNetMask": haClusterSyncNetMask,
       "haStatCode": haStatCode,
       "haStatShort": haStatShort,
       "haStatLong": haStatLong,
       "haServicePack": haServicePack,
       "svn": svn,
       "svnProdName": svnProdName,
       "svnProdVerMajor": svnProdVerMajor,
       "svnProdVerMinor": svnProdVerMinor,
       "svnInfo": svnInfo,
       "svnVersion": svnVersion,
       "svnBuild": svnBuild,
       "svnOSInfo": svnOSInfo,
       "osName": osName,
       "osMajorVer": osMajorVer,
       "osMinorVer": osMinorVer,
       "osBuildNum": osBuildNum,
       "osSPmajor": osSPmajor,
       "osSPminor": osSPminor,
       "osVersionLevel": osVersionLevel,
       "routingTable": routingTable,
       "routingEntry": routingEntry,
       "routingIndex": routingIndex,
       "routingDest": routingDest,
       "routingMask": routingMask,
       "routingGatweway": routingGatweway,
       "routingIntrfName": routingIntrfName,
       "svnPerf": svnPerf,
       "svnMem": svnMem,
       "memTotalVirtual": memTotalVirtual,
       "memActiveVirtual": memActiveVirtual,
       "memTotalReal": memTotalReal,
       "memActiveReal": memActiveReal,
       "memFreeReal": memFreeReal,
       "memSwapsSec": memSwapsSec,
       "memDiskTransfers": memDiskTransfers,
       "svnProc": svnProc,
       "procUsrTime": procUsrTime,
       "procSysTime": procSysTime,
       "procIdleTime": procIdleTime,
       "procUsage": procUsage,
       "procQueue": procQueue,
       "procInterrupts": procInterrupts,
       "procNum": procNum,
       "svnDisk": svnDisk,
       "diskTime": diskTime,
       "diskQueue": diskQueue,
       "diskPercent": diskPercent,
       "diskFreeTotal": diskFreeTotal,
       "diskFreeAvail": diskFreeAvail,
       "diskTotal": diskTotal,
       "svnMem64": svnMem64,
       "memTotalVirtual64": memTotalVirtual64,
       "memActiveVirtual64": memActiveVirtual64,
       "memTotalReal64": memTotalReal64,
       "memActiveReal64": memActiveReal64,
       "memFreeReal64": memFreeReal64,
       "memSwapsSec64": memSwapsSec64,
       "memDiskTransfers64": memDiskTransfers64,
       "multiProcTable": multiProcTable,
       "multiProcEntry": multiProcEntry,
       "multiProcIndex": multiProcIndex,
       "multiProcUserTime": multiProcUserTime,
       "multiProcSystemTime": multiProcSystemTime,
       "multiProcIdleTime": multiProcIdleTime,
       "multiProcUsage": multiProcUsage,
       "multiProcRunQueue": multiProcRunQueue,
       "multiProcInterrupts": multiProcInterrupts,
       "multiDiskTable": multiDiskTable,
       "multiDiskEntry": multiDiskEntry,
       "multiDiskIndex": multiDiskIndex,
       "multiDiskName": multiDiskName,
       "multiDiskSize": multiDiskSize,
       "multiDiskUsed": multiDiskUsed,
       "multiDiskFreeTotalBytes": multiDiskFreeTotalBytes,
       "multiDiskFreeTotalPercent": multiDiskFreeTotalPercent,
       "multiDiskFreeAvailableBytes": multiDiskFreeAvailableBytes,
       "multiDiskFreeAvailablePercent": multiDiskFreeAvailablePercent,
       "raidInfo": raidInfo,
       "raidVolumeTable": raidVolumeTable,
       "raidVolumeEntry": raidVolumeEntry,
       "raidVolumeIndex": raidVolumeIndex,
       "raidVolumeID": raidVolumeID,
       "raidVolumeType": raidVolumeType,
       "numOfDisksOnRaid": numOfDisksOnRaid,
       "raidVolumeMaxLBA": raidVolumeMaxLBA,
       "raidVolumeState": raidVolumeState,
       "raidVolumeFlags": raidVolumeFlags,
       "raidVolumeSize": raidVolumeSize,
       "raidDiskTable": raidDiskTable,
       "raidDiskEntry": raidDiskEntry,
       "raidDiskIndex": raidDiskIndex,
       "raidDiskVolumeID": raidDiskVolumeID,
       "raidDiskID": raidDiskID,
       "raidDiskNumber": raidDiskNumber,
       "raidDiskVendor": raidDiskVendor,
       "raidDiskProductID": raidDiskProductID,
       "raidDiskRevision": raidDiskRevision,
       "raidDiskMaxLBA": raidDiskMaxLBA,
       "raidDiskState": raidDiskState,
       "raidDiskFlags": raidDiskFlags,
       "raidDiskSyncState": raidDiskSyncState,
       "raidDiskSize": raidDiskSize,
       "sensorInfo": sensorInfo,
       "tempertureSensorTable": tempertureSensorTable,
       "tempertureSensorEntry": tempertureSensorEntry,
       "tempertureSensorIndex": tempertureSensorIndex,
       "tempertureSensorName": tempertureSensorName,
       "tempertureSensorValue": tempertureSensorValue,
       "tempertureSensorUnit": tempertureSensorUnit,
       "tempertureSensorType": tempertureSensorType,
       "tempertureSensorStatus": tempertureSensorStatus,
       "fanSpeedSensorTable": fanSpeedSensorTable,
       "fanSpeedSensorEntry": fanSpeedSensorEntry,
       "fanSpeedSensorIndex": fanSpeedSensorIndex,
       "fanSpeedSensorName": fanSpeedSensorName,
       "fanSpeedSensorValue": fanSpeedSensorValue,
       "fanSpeedSensorUnit": fanSpeedSensorUnit,
       "fanSpeedSensorType": fanSpeedSensorType,
       "fanSpeedSensorStatus": fanSpeedSensorStatus,
       "voltageSensorTable": voltageSensorTable,
       "voltageSensorEntry": voltageSensorEntry,
       "voltageSensorIndex": voltageSensorIndex,
       "voltageSensorName": voltageSensorName,
       "voltageSensorValue": voltageSensorValue,
       "voltageSensorUnit": voltageSensorUnit,
       "voltageSensorType": voltageSensorType,
       "voltageSensorStatus": voltageSensorStatus,
       "powerSupplyInfo": powerSupplyInfo,
       "powerSupplyTable": powerSupplyTable,
       "powerSupplyEntry": powerSupplyEntry,
       "powerSupplyIndex": powerSupplyIndex,
       "powerSupplyStatus": powerSupplyStatus,
       "svnSysTime": svnSysTime,
       "svnRoutingModify": svnRoutingModify,
       "svnRouteModDest": svnRouteModDest,
       "svnRouteModMask": svnRouteModMask,
       "svnRouteModGateway": svnRouteModGateway,
       "svnRouteModIfIndex": svnRouteModIfIndex,
       "svnRouteModIfName": svnRouteModIfName,
       "svnRouteModAction": svnRouteModAction,
       "svnUTCTimeOffset": svnUTCTimeOffset,
       "svnLogDaemon": svnLogDaemon,
       "svnLogDStat": svnLogDStat,
       "svnSysStartTime": svnSysStartTime,
       "svnSysUniqId": svnSysUniqId,
       "svnWebUIPort": svnWebUIPort,
       "svnApplianceInfo": svnApplianceInfo,
       "svnApplianceSerialNumber": svnApplianceSerialNumber,
       "svnApplianceProductName": svnApplianceProductName,
       "svnApplianceManufacturer": svnApplianceManufacturer,
       "svnNetStat": svnNetStat,
       "svnNetIfTable": svnNetIfTable,
       "svnNetIfTableEntry": svnNetIfTableEntry,
       "svnNetIfIndex": svnNetIfIndex,
       "svnNetIfVsid": svnNetIfVsid,
       "svnNetIfName": svnNetIfName,
       "svnNetIfAddress": svnNetIfAddress,
       "svnNetIfMask": svnNetIfMask,
       "svnNetIfMTU": svnNetIfMTU,
       "svnNetIfState": svnNetIfState,
       "svnNetIfMAC": svnNetIfMAC,
       "svnNetIfDescription": svnNetIfDescription,
       "svnNetIfOperState": svnNetIfOperState,
       "vsRoutingTable": vsRoutingTable,
       "vsRoutingEntry": vsRoutingEntry,
       "vsRoutingIndex": vsRoutingIndex,
       "vsRoutingDest": vsRoutingDest,
       "vsRoutingMask": vsRoutingMask,
       "vsRoutingGateway": vsRoutingGateway,
       "vsRoutingIntrfName": vsRoutingIntrfName,
       "vsRoutingVsId": vsRoutingVsId,
       "svnStatCode": svnStatCode,
       "svnStatShortDescr": svnStatShortDescr,
       "svnStatLongDescr": svnStatLongDescr,
       "svnServicePack": svnServicePack,
       "mngmt": mngmt,
       "mgProdName": mgProdName,
       "mgVerMajor": mgVerMajor,
       "mgVerMinor": mgVerMinor,
       "mgBuildNumber": mgBuildNumber,
       "mgActiveStatus": mgActiveStatus,
       "mgFwmIsAlive": mgFwmIsAlive,
       "mgConnectedClientsTable": mgConnectedClientsTable,
       "mgConnectedClientsEntry": mgConnectedClientsEntry,
       "mgIndex": mgIndex,
       "mgClientName": mgClientName,
       "mgClientHost": mgClientHost,
       "mgClientDbLock": mgClientDbLock,
       "mgApplicationType": mgApplicationType,
       "mgStatCode": mgStatCode,
       "mgStatShortDescr": mgStatShortDescr,
       "mgStatLongDescr": mgStatLongDescr,
       "wam": wam,
       "wamProdName": wamProdName,
       "wamVerMajor": wamVerMajor,
       "wamVerMinor": wamVerMinor,
       "wamState": wamState,
       "wamName": wamName,
       "wamPluginPerformance": wamPluginPerformance,
       "wamAcceptReq": wamAcceptReq,
       "wamRejectReq": wamRejectReq,
       "wamPolicy": wamPolicy,
       "wamPolicyName": wamPolicyName,
       "wamPolicyUpdate": wamPolicyUpdate,
       "wamUagQueries": wamUagQueries,
       "wamUagHost": wamUagHost,
       "wamUagIp": wamUagIp,
       "wamUagPort": wamUagPort,
       "wamUagNoQueries": wamUagNoQueries,
       "wamUagLastQuery": wamUagLastQuery,
       "wamGlobalPerformance": wamGlobalPerformance,
       "wamOpenSessions": wamOpenSessions,
       "wamLastSession": wamLastSession,
       "wamStatCode": wamStatCode,
       "wamStatShortDescr": wamStatShortDescr,
       "wamStatLongDescr": wamStatLongDescr,
       "dtps": dtps,
       "dtpsProdName": dtpsProdName,
       "dtpsVerMajor": dtpsVerMajor,
       "dtpsVerMinor": dtpsVerMinor,
       "dtpsLicensedUsers": dtpsLicensedUsers,
       "dtpsConnectedUsers": dtpsConnectedUsers,
       "dtpsStatCode": dtpsStatCode,
       "dtpsStatShortDescr": dtpsStatShortDescr,
       "dtpsStatLongDescr": dtpsStatLongDescr,
       "ls": ls,
       "lsProdName": lsProdName,
       "lsVerMajor": lsVerMajor,
       "lsVerMinor": lsVerMinor,
       "lsBuildNumber": lsBuildNumber,
       "lsFwmIsAlive": lsFwmIsAlive,
       "lsConnectedClientsTable": lsConnectedClientsTable,
       "lsConnectedClientsEntry": lsConnectedClientsEntry,
       "lsIndex": lsIndex,
       "lsClientName": lsClientName,
       "lsClientHost": lsClientHost,
       "lsClientDbLock": lsClientDbLock,
       "lsApplicationType": lsApplicationType,
       "lsStatCode": lsStatCode,
       "lsStatShortDescr": lsStatShortDescr,
       "lsStatLongDescr": lsStatLongDescr,
       "vsx": vsx,
       "vsxVsSupported": vsxVsSupported,
       "vsxVsConfigured": vsxVsConfigured,
       "vsxVsInstalled": vsxVsInstalled,
       "vsxStatus": vsxStatus,
       "vsxStatusTable": vsxStatusTable,
       "vsxStatusEntry": vsxStatusEntry,
       "vsxStatusVSId": vsxStatusVSId,
       "vsxStatusVRId": vsxStatusVRId,
       "vsxStatusVsName": vsxStatusVsName,
       "vsxStatusVsType": vsxStatusVsType,
       "vsxStatusMainIP": vsxStatusMainIP,
       "vsxStatusPolicyName": vsxStatusPolicyName,
       "vsxStatusVsPolicyType": vsxStatusVsPolicyType,
       "vsxStatusSicTrustState": vsxStatusSicTrustState,
       "vsxStatusHAState": vsxStatusHAState,
       "vsxStatusVSWeight": vsxStatusVSWeight,
       "vsxStatusCPUUsageTable": vsxStatusCPUUsageTable,
       "vsxStatusCPUUsageEntry": vsxStatusCPUUsageEntry,
       "vsxStatusCPUUsage1sec": vsxStatusCPUUsage1sec,
       "vsxStatusCPUUsage10sec": vsxStatusCPUUsage10sec,
       "vsxStatusCPUUsage1min": vsxStatusCPUUsage1min,
       "vsxStatusCPUUsage1hr": vsxStatusCPUUsage1hr,
       "vsxStatusCPUUsage24hr": vsxStatusCPUUsage24hr,
       "vsxStatusCPUUsageVSId": vsxStatusCPUUsageVSId,
       "vsxCounters": vsxCounters,
       "vsxCountersTable": vsxCountersTable,
       "vsxCountersEntry": vsxCountersEntry,
       "vsxCountersVSId": vsxCountersVSId,
       "vsxCountersConnNum": vsxCountersConnNum,
       "vsxCountersConnPeakNum": vsxCountersConnPeakNum,
       "vsxCountersConnTableLimit": vsxCountersConnTableLimit,
       "vsxCountersPackets": vsxCountersPackets,
       "vsxCountersDroppedTotal": vsxCountersDroppedTotal,
       "vsxCountersAcceptedTotal": vsxCountersAcceptedTotal,
       "vsxCountersRejectedTotal": vsxCountersRejectedTotal,
       "vsxCountersBytesAcceptedTotal": vsxCountersBytesAcceptedTotal,
       "vsxCountersBytesDroppedTotal": vsxCountersBytesDroppedTotal,
       "vsxCountersBytesRejectedTotal": vsxCountersBytesRejectedTotal,
       "vsxCountersLoggedTotal": vsxCountersLoggedTotal,
       "vsxCountersIsDataValid": vsxCountersIsDataValid,
       "smartDefense": smartDefense,
       "asmAttacks": asmAttacks,
       "asmLayer3": asmLayer3,
       "asmLayer4": asmLayer4,
       "asmTCP": asmTCP,
       "asmSynatk": asmSynatk,
       "asmSynatkSynAckTimeout": asmSynatkSynAckTimeout,
       "asmSynatkSynAckReset": asmSynatkSynAckReset,
       "asmSynatkModeChange": asmSynatkModeChange,
       "asmSynatkCurrentMode": asmSynatkCurrentMode,
       "asmSynatkNumberofunAckedSyns": asmSynatkNumberofunAckedSyns,
       "asmSmallPmtu": asmSmallPmtu,
       "smallPMTUNumberOfAttacks": smallPMTUNumberOfAttacks,
       "smallPMTUValueOfMinimalMTUsize": smallPMTUValueOfMinimalMTUsize,
       "asmSeqval": asmSeqval,
       "sequenceVerifierInvalidAck": sequenceVerifierInvalidAck,
       "sequenceVerifierInvalidSequence": sequenceVerifierInvalidSequence,
       "sequenceVerifierInvalidretransmit": sequenceVerifierInvalidretransmit,
       "asmUDP": asmUDP,
       "asmScans": asmScans,
       "asmHostPortScan": asmHostPortScan,
       "numOfhostPortScan": numOfhostPortScan,
       "asmIPSweep": asmIPSweep,
       "numOfIpSweep": numOfIpSweep,
       "asmLayer5": asmLayer5,
       "asmHTTP": asmHTTP,
       "asmHttpWorms": asmHttpWorms,
       "httpWorms": httpWorms,
       "asmHttpFormatViolatoin": asmHttpFormatViolatoin,
       "httpURLLengthViolation": httpURLLengthViolation,
       "httpHeaderLengthViolations": httpHeaderLengthViolations,
       "httpMaxHeaderReached": httpMaxHeaderReached,
       "asmHttpAsciiViolation": asmHttpAsciiViolation,
       "numOfHttpASCIIViolations": numOfHttpASCIIViolations,
       "asmHttpP2PHeaderFilter": asmHttpP2PHeaderFilter,
       "numOfHttpP2PHeaders": numOfHttpP2PHeaders,
       "asmCIFS": asmCIFS,
       "asmCIFSWorms": asmCIFSWorms,
       "numOfCIFSworms": numOfCIFSworms,
       "asmCIFSNullSession": asmCIFSNullSession,
       "numOfCIFSNullSessions": numOfCIFSNullSessions,
       "asmCIFSBlockedPopUps": asmCIFSBlockedPopUps,
       "numOfCIFSBlockedPopUps": numOfCIFSBlockedPopUps,
       "asmCIFSBlockedCommands": asmCIFSBlockedCommands,
       "numOfCIFSBlockedCommands": numOfCIFSBlockedCommands,
       "asmCIFSPasswordLengthViolations": asmCIFSPasswordLengthViolations,
       "numOfCIFSPasswordLengthViolations": numOfCIFSPasswordLengthViolations,
       "asmP2P": asmP2P,
       "asmP2POtherConAttempts": asmP2POtherConAttempts,
       "numOfP2POtherConAttempts": numOfP2POtherConAttempts,
       "asmP2PKazaaConAttempts": asmP2PKazaaConAttempts,
       "numOfP2PKazaaConAttempts": numOfP2PKazaaConAttempts,
       "asmP2PeMuleConAttempts": asmP2PeMuleConAttempts,
       "numOfP2PeMuleConAttempts": numOfP2PeMuleConAttempts,
       "asmP2PGnutellaConAttempts": asmP2PGnutellaConAttempts,
       "numOfGnutellaConAttempts": numOfGnutellaConAttempts,
       "asmP2PSkypeCon": asmP2PSkypeCon,
       "numOfP2PSkypeCon": numOfP2PSkypeCon,
       "asmP2PBitTorrentCon": asmP2PBitTorrentCon,
       "numOfBitTorrentCon": numOfBitTorrentCon,
       "avi": avi,
       "aviEngines": aviEngines,
       "aviEngineTable": aviEngineTable,
       "aviEngineEntry": aviEngineEntry,
       "aviEngineIndex": aviEngineIndex,
       "aviEngineName": aviEngineName,
       "aviEngineVer": aviEngineVer,
       "aviEngineDate": aviEngineDate,
       "aviSignatureName": aviSignatureName,
       "aviSignatureVer": aviSignatureVer,
       "aviSignatureDate": aviSignatureDate,
       "aviLastSigCheckTime": aviLastSigCheckTime,
       "aviLastSigLocation": aviLastSigLocation,
       "aviLastLicExp": aviLastLicExp,
       "aviTopViruses": aviTopViruses,
       "aviTopVirusesTable": aviTopVirusesTable,
       "aviTopVirusesEntry": aviTopVirusesEntry,
       "aviTopVirusesIndex": aviTopVirusesIndex,
       "aviTopVirusesName": aviTopVirusesName,
       "aviTopVirusesCnt": aviTopVirusesCnt,
       "aviTopEverViruses": aviTopEverViruses,
       "aviTopEverVirusesTable": aviTopEverVirusesTable,
       "aviTopEverVirusesEntry": aviTopEverVirusesEntry,
       "aviTopEverVirusesIndex": aviTopEverVirusesIndex,
       "aviTopEverVirusesName": aviTopEverVirusesName,
       "aviTopEverVirusesCnt": aviTopEverVirusesCnt,
       "aviServices": aviServices,
       "aviServicesHTTP": aviServicesHTTP,
       "aviHTTPState": aviHTTPState,
       "aviHTTPLastVirusName": aviHTTPLastVirusName,
       "aviHTTPLastVirusTime": aviHTTPLastVirusTime,
       "aviHTTPTopVirusesTable": aviHTTPTopVirusesTable,
       "aviHTTPTopVirusesEntry": aviHTTPTopVirusesEntry,
       "aviHTTPTopVirusesIndex": aviHTTPTopVirusesIndex,
       "aviHTTPTopVirusesName": aviHTTPTopVirusesName,
       "aviHTTPTopVirusesCnt": aviHTTPTopVirusesCnt,
       "aviServicesFTP": aviServicesFTP,
       "aviFTPState": aviFTPState,
       "aviFTPLastVirusName": aviFTPLastVirusName,
       "aviFTPLastVirusTime": aviFTPLastVirusTime,
       "aviFTPTopVirusesTable": aviFTPTopVirusesTable,
       "aviFTPTopVirusesEntry": aviFTPTopVirusesEntry,
       "aviFTPTopVirusesIndex": aviFTPTopVirusesIndex,
       "aviFTPTopVirusesName": aviFTPTopVirusesName,
       "aviFTPTopVirusesCnt": aviFTPTopVirusesCnt,
       "aviServicesSMTP": aviServicesSMTP,
       "aviSMTPState": aviSMTPState,
       "aviSMTPLastVirusName": aviSMTPLastVirusName,
       "aviSMTPLastVirusTime": aviSMTPLastVirusTime,
       "aviSMTPTopVirusesTable": aviSMTPTopVirusesTable,
       "aviSMTPTopVirusesEntry": aviSMTPTopVirusesEntry,
       "aviSMTPTopVirusesIndex": aviSMTPTopVirusesIndex,
       "aviSMTPTopVirusesName": aviSMTPTopVirusesName,
       "aviSMTPTopVirusesCnt": aviSMTPTopVirusesCnt,
       "aviServicesPOP3": aviServicesPOP3,
       "aviPOP3State": aviPOP3State,
       "aviPOP3LastVirusName": aviPOP3LastVirusName,
       "aviPOP3LastVirusTime": aviPOP3LastVirusTime,
       "aviPOP3TopVirusesTable": aviPOP3TopVirusesTable,
       "aviPOP3TopVirusesEntry": aviPOP3TopVirusesEntry,
       "aviPOP3TopVirusesIndex": aviPOP3TopVirusesIndex,
       "aviPOP3TopVirusesName": aviPOP3TopVirusesName,
       "aviPOP3TopVirusesCnt": aviPOP3TopVirusesCnt,
       "aviStatCode": aviStatCode,
       "aviStatShortDescr": aviStatShortDescr,
       "aviStatLongDescr": aviStatLongDescr,
       "eventiaAnalyzer": eventiaAnalyzer,
       "cpsemd": cpsemd,
       "cpsemdProcAlive": cpsemdProcAlive,
       "cpsemdNewEventsHandled": cpsemdNewEventsHandled,
       "cpsemdUpdatesHandled": cpsemdUpdatesHandled,
       "cpsemdLastEventTime": cpsemdLastEventTime,
       "cpsemdCurrentDBSize": cpsemdCurrentDBSize,
       "cpsemdDBCapacity": cpsemdDBCapacity,
       "cpsemdNumEvents": cpsemdNumEvents,
       "cpsemdDBDiskSpace": cpsemdDBDiskSpace,
       "cpsemdCorrelationUnitTable": cpsemdCorrelationUnitTable,
       "cpsemdCorrelationUnitEntry": cpsemdCorrelationUnitEntry,
       "cpsemdCorrelationUnitIndex": cpsemdCorrelationUnitIndex,
       "cpsemdCorrelationUnitIP": cpsemdCorrelationUnitIP,
       "cpsemdCorrelationUnitLastRcvdTime": cpsemdCorrelationUnitLastRcvdTime,
       "cpsemdCorrelationUnitNumEventsRcvd": cpsemdCorrelationUnitNumEventsRcvd,
       "cpsemdConnectionDuration": cpsemdConnectionDuration,
       "cpsemdDBIsFull": cpsemdDBIsFull,
       "cpsemdStatCode": cpsemdStatCode,
       "cpsemdStatShortDescr": cpsemdStatShortDescr,
       "cpsemdStatLongDescr": cpsemdStatLongDescr,
       "cpsead": cpsead,
       "cpseadProcAlive": cpseadProcAlive,
       "cpseadConnectedToSem": cpseadConnectedToSem,
       "cpseadNumProcessedLogs": cpseadNumProcessedLogs,
       "cpseadJobsTable": cpseadJobsTable,
       "cpseadJobsEntry": cpseadJobsEntry,
       "cpseadJobIndex": cpseadJobIndex,
       "cpseadJobID": cpseadJobID,
       "cpseadJobName": cpseadJobName,
       "cpseadJobState": cpseadJobState,
       "cpseadJobIsOnline": cpseadJobIsOnline,
       "cpseadJobLogServer": cpseadJobLogServer,
       "cpseadJobDataType": cpseadJobDataType,
       "cpseadConnectedToLogServer": cpseadConnectedToLogServer,
       "cpseadNumAnalyzedLogs": cpseadNumAnalyzedLogs,
       "cpseadFileName": cpseadFileName,
       "cpseadFileCurrentPosition": cpseadFileCurrentPosition,
       "cpseadStateDescriptionCode": cpseadStateDescriptionCode,
       "cpseadStateDescription": cpseadStateDescription,
       "cpseadNoFreeDiskSpace": cpseadNoFreeDiskSpace,
       "cpseadStatCode": cpseadStatCode,
       "cpseadStatShortDescr": cpseadStatShortDescr,
       "cpseadStatLongDescr": cpseadStatLongDescr,
       "uf": uf,
       "ufEngine": ufEngine,
       "ufEngineName": ufEngineName,
       "ufEngineVer": ufEngineVer,
       "ufEngineDate": ufEngineDate,
       "ufSignatureDate": ufSignatureDate,
       "ufSignatureVer": ufSignatureVer,
       "ufLastSigCheckTime": ufLastSigCheckTime,
       "ufLastSigLocation": ufLastSigLocation,
       "ufLastLicExp": ufLastLicExp,
       "ufSS": ufSS,
       "ufIsMonitor": ufIsMonitor,
       "ufScannedCnt": ufScannedCnt,
       "ufBlockedCnt": ufBlockedCnt,
       "ufTopBlockedCatTable": ufTopBlockedCatTable,
       "ufTopBlockedCatEntry": ufTopBlockedCatEntry,
       "ufTopBlockedCatIndex": ufTopBlockedCatIndex,
       "ufTopBlockedCatName": ufTopBlockedCatName,
       "ufTopBlockedCatCnt": ufTopBlockedCatCnt,
       "ufTopBlockedSiteTable": ufTopBlockedSiteTable,
       "ufTopBlockedSiteEntry": ufTopBlockedSiteEntry,
       "ufTopBlockedSiteIndex": ufTopBlockedSiteIndex,
       "ufTopBlockedSiteName": ufTopBlockedSiteName,
       "ufTopBlockedSiteCnt": ufTopBlockedSiteCnt,
       "ufTopBlockedUserTable": ufTopBlockedUserTable,
       "ufTopBlockedUserEntry": ufTopBlockedUserEntry,
       "ufTopBlockedUserIndex": ufTopBlockedUserIndex,
       "ufTopBlockedUserName": ufTopBlockedUserName,
       "ufTopBlockedUserCnt": ufTopBlockedUserCnt,
       "ufStatCode": ufStatCode,
       "ufStatShortDescr": ufStatShortDescr,
       "ufStatLongDescr": ufStatLongDescr,
       "ms": ms,
       "msProductName": msProductName,
       "msMajorVersion": msMajorVersion,
       "msMinorVersion": msMinorVersion,
       "msBuildNumber": msBuildNumber,
       "msVersionStr": msVersionStr,
       "msSpam": msSpam,
       "msSpamNumScannedEmails": msSpamNumScannedEmails,
       "msSpamNumSpamEmails": msSpamNumSpamEmails,
       "msSpamNumHandledSpamEmails": msSpamNumHandledSpamEmails,
       "msSpamControls": msSpamControls,
       "msSpamControlsSpamEngine": msSpamControlsSpamEngine,
       "msSpamControlsIpRepuatation": msSpamControlsIpRepuatation,
       "msSpamControlsSPF": msSpamControlsSPF,
       "msSpamControlsDomainKeys": msSpamControlsDomainKeys,
       "msSpamControlsRDNS": msSpamControlsRDNS,
       "msSpamControlsRBL": msSpamControlsRBL,
       "msExpirationDate": msExpirationDate,
       "msEngineVer": msEngineVer,
       "msEngineDate": msEngineDate,
       "msStatCode": msStatCode,
       "msStatShortDescr": msStatShortDescr,
       "msStatLongDescr": msStatLongDescr,
       "msServicePack": msServicePack,
       "voip": voip,
       "voipProductName": voipProductName,
       "voipMajorVersion": voipMajorVersion,
       "voipMinorVersion": voipMinorVersion,
       "voipBuildNumber": voipBuildNumber,
       "voipVersionStr": voipVersionStr,
       "voipDOS": voipDOS,
       "voipDOSSip": voipDOSSip,
       "voipDOSSipNetwork": voipDOSSipNetwork,
       "voipDOSSipNetworkReqInterval": voipDOSSipNetworkReqInterval,
       "voipDOSSipNetworkReqConfThreshold": voipDOSSipNetworkReqConfThreshold,
       "voipDOSSipNetworkReqCurrentVal": voipDOSSipNetworkReqCurrentVal,
       "voipDOSSipNetworkRegInterval": voipDOSSipNetworkRegInterval,
       "voipDOSSipNetworkRegConfThreshold": voipDOSSipNetworkRegConfThreshold,
       "voipDOSSipNetworkRegCurrentVal": voipDOSSipNetworkRegCurrentVal,
       "voipDOSSipNetworkCallInitInterval": voipDOSSipNetworkCallInitInterval,
       "voipDOSSipNetworkCallInitConfThreshold": voipDOSSipNetworkCallInitConfThreshold,
       "voipDOSSipNetworkCallInitICurrentVal": voipDOSSipNetworkCallInitICurrentVal,
       "voipDOSSipRateLimitingTable": voipDOSSipRateLimitingTable,
       "voipDOSSipRateLimitingEntry": voipDOSSipRateLimitingEntry,
       "voipDOSSipRateLimitingTableIndex": voipDOSSipRateLimitingTableIndex,
       "voipDOSSipRateLimitingTableIpAddress": voipDOSSipRateLimitingTableIpAddress,
       "voipDOSSipRateLimitingTableInterval": voipDOSSipRateLimitingTableInterval,
       "voipDOSSipRateLimitingTableConfThreshold": voipDOSSipRateLimitingTableConfThreshold,
       "voipDOSSipRateLimitingTableNumDOSSipRequests": voipDOSSipRateLimitingTableNumDOSSipRequests,
       "voipDOSSipRateLimitingTableNumTrustedRequests": voipDOSSipRateLimitingTableNumTrustedRequests,
       "voipDOSSipRateLimitingTableNumNonTrustedRequests": voipDOSSipRateLimitingTableNumNonTrustedRequests,
       "voipDOSSipRateLimitingTableNumRequestsfromServers": voipDOSSipRateLimitingTableNumRequestsfromServers,
       "voipCAC": voipCAC,
       "voipCACConcurrentCalls": voipCACConcurrentCalls,
       "voipCACConcurrentCallsConfThreshold": voipCACConcurrentCallsConfThreshold,
       "voipCACConcurrentCallsCurrentVal": voipCACConcurrentCallsCurrentVal,
       "voipStatCode": voipStatCode,
       "voipStatShortDescr": voipStatShortDescr,
       "voipStatLongDescr": voipStatLongDescr,
       "voipServicePack": voipServicePack,
       "sxl": sxl,
       "fwSXLGroup": fwSXLGroup,
       "fwSXLStatus": fwSXLStatus,
       "fwSXLConnsExisting": fwSXLConnsExisting,
       "fwSXLConnsAdded": fwSXLConnsAdded,
       "fwSXLConnsDeleted": fwSXLConnsDeleted,
       "identityAwareness": identityAwareness,
       "identityAwarenessProductName": identityAwarenessProductName,
       "identityAwarenessAuthUsers": identityAwarenessAuthUsers,
       "identityAwarenessUnAuthUsers": identityAwarenessUnAuthUsers,
       "identityAwarenessAuthUsersKerberos": identityAwarenessAuthUsersKerberos,
       "identityAwarenessAuthMachKerberos": identityAwarenessAuthMachKerberos,
       "identityAwarenessAuthUsersPass": identityAwarenessAuthUsersPass,
       "identityAwarenessAuthUsersADQuery": identityAwarenessAuthUsersADQuery,
       "identityAwarenessAuthMachADQuery": identityAwarenessAuthMachADQuery,
       "identityAwarenessLoggedInAgent": identityAwarenessLoggedInAgent,
       "identityAwarenessLoggedInCaptivePortal": identityAwarenessLoggedInCaptivePortal,
       "identityAwarenessLoggedInADQuery": identityAwarenessLoggedInADQuery,
       "identityAwarenessAntiSpoffProtection": identityAwarenessAntiSpoffProtection,
       "identityAwarenessSuccUserLoginKerberos": identityAwarenessSuccUserLoginKerberos,
       "identityAwarenessSuccMachLoginKerberos": identityAwarenessSuccMachLoginKerberos,
       "identityAwarenessSuccUserLoginPass": identityAwarenessSuccUserLoginPass,
       "identityAwarenessSuccUserLoginADQuery": identityAwarenessSuccUserLoginADQuery,
       "identityAwarenessSuccMachLoginADQuery": identityAwarenessSuccMachLoginADQuery,
       "identityAwarenessUnSuccUserLoginKerberos": identityAwarenessUnSuccUserLoginKerberos,
       "identityAwarenessUnSuccMachLoginKerberos": identityAwarenessUnSuccMachLoginKerberos,
       "identityAwarenessUnSuccUserLoginPass": identityAwarenessUnSuccUserLoginPass,
       "identityAwarenessSuccUserLDAP": identityAwarenessSuccUserLDAP,
       "identityAwarenessUnSuccUserLDAP": identityAwarenessUnSuccUserLDAP,
       "identityAwarenessDataTrans": identityAwarenessDataTrans,
       "identityAwarenessDistributedEnvTable": identityAwarenessDistributedEnvTable,
       "identityAwarenessDistributedEnvEntry": identityAwarenessDistributedEnvEntry,
       "identityAwarenessDistributedEnvTableIndex": identityAwarenessDistributedEnvTableIndex,
       "identityAwarenessDistributedEnvTableGwName": identityAwarenessDistributedEnvTableGwName,
       "identityAwarenessDistributedEnvTableDisconnections": identityAwarenessDistributedEnvTableDisconnections,
       "identityAwarenessDistributedEnvTableBruteForceAtt": identityAwarenessDistributedEnvTableBruteForceAtt,
       "identityAwarenessDistributedEnvTableStatus": identityAwarenessDistributedEnvTableStatus,
       "identityAwarenessDistributedEnvTableIsLocal": identityAwarenessDistributedEnvTableIsLocal,
       "identityAwarenessADQueryStatusTable": identityAwarenessADQueryStatusTable,
       "identityAwarenessADQueryStatusEntry": identityAwarenessADQueryStatusEntry,
       "identityAwarenessADQueryStatusTableIndex": identityAwarenessADQueryStatusTableIndex,
       "identityAwarenessADQueryStatusCurrStatus": identityAwarenessADQueryStatusCurrStatus,
       "identityAwarenessADQueryStatusDomainName": identityAwarenessADQueryStatusDomainName,
       "identityAwarenessADQueryStatusDomainIP": identityAwarenessADQueryStatusDomainIP,
       "identityAwarenessADQueryStatusEvents": identityAwarenessADQueryStatusEvents,
       "identityAwarenessStatus": identityAwarenessStatus,
       "identityAwarenessStatusShortDesc": identityAwarenessStatusShortDesc,
       "identityAwarenessStatusLongDesc": identityAwarenessStatusLongDesc,
       "applicationControl": applicationControl,
       "applicationControlSubscription": applicationControlSubscription,
       "applicationControlSubscriptionStatus": applicationControlSubscriptionStatus,
       "applicationControlSubscriptionExpDate": applicationControlSubscriptionExpDate,
       "applicationControlSubscriptionDesc": applicationControlSubscriptionDesc,
       "applicationControlUpdate": applicationControlUpdate,
       "applicationControlUpdateStatus": applicationControlUpdateStatus,
       "applicationControlUpdateDesc": applicationControlUpdateDesc,
       "applicationControlNextUpdate": applicationControlNextUpdate,
       "applicationControlVersion": applicationControlVersion,
       "applicationControlStatusCode": applicationControlStatusCode,
       "applicationControlStatusShortDesc": applicationControlStatusShortDesc,
       "applicationControlStatusLongDesc": applicationControlStatusLongDesc,
       "thresholds": thresholds,
       "thresholdPolicy": thresholdPolicy,
       "thresholdState": thresholdState,
       "thresholdStateDesc": thresholdStateDesc,
       "thresholdEnabled": thresholdEnabled,
       "thresholdActive": thresholdActive,
       "thresholdEventsSinceStartup": thresholdEventsSinceStartup,
       "thresholdActiveEventsTable": thresholdActiveEventsTable,
       "thresholdActiveEventsEntry": thresholdActiveEventsEntry,
       "thresholdActiveEventsIndex": thresholdActiveEventsIndex,
       "thresholdActiveEventName": thresholdActiveEventName,
       "thresholdActiveEventCategory": thresholdActiveEventCategory,
       "thresholdActiveEventSeverity": thresholdActiveEventSeverity,
       "thresholdActiveEventSubject": thresholdActiveEventSubject,
       "thresholdActiveEventSubjectValue": thresholdActiveEventSubjectValue,
       "thresholdActiveEventActivationTime": thresholdActiveEventActivationTime,
       "thresholdActiveEventState": thresholdActiveEventState,
       "thresholdDestinationsTable": thresholdDestinationsTable,
       "thresholdDestinationsEntry": thresholdDestinationsEntry,
       "thresholdDestinationIndex": thresholdDestinationIndex,
       "thresholdDestinationName": thresholdDestinationName,
       "thresholdDestinationType": thresholdDestinationType,
       "thresholdSendingState": thresholdSendingState,
       "thresholdSendingStateDesc": thresholdSendingStateDesc,
       "thresholdAlertCount": thresholdAlertCount,
       "thresholdErrorsTable": thresholdErrorsTable,
       "thresholdErrorsEntry": thresholdErrorsEntry,
       "thresholdErrorIndex": thresholdErrorIndex,
       "thresholdName": thresholdName,
       "thresholdThresholdOID": thresholdThresholdOID,
       "thresholdErrorDesc": thresholdErrorDesc,
       "thresholdErrorTime": thresholdErrorTime,
       "advancedUrlFiltering": advancedUrlFiltering,
       "advancedUrlFilteringSubscription": advancedUrlFilteringSubscription,
       "advancedUrlFilteringSubscriptionStatus": advancedUrlFilteringSubscriptionStatus,
       "advancedUrlFilteringSubscriptionExpDate": advancedUrlFilteringSubscriptionExpDate,
       "advancedUrlFilteringSubscriptionDesc": advancedUrlFilteringSubscriptionDesc,
       "advancedUrlFilteringUpdate": advancedUrlFilteringUpdate,
       "advancedUrlFilteringUpdateStatus": advancedUrlFilteringUpdateStatus,
       "advancedUrlFilteringUpdateDesc": advancedUrlFilteringUpdateDesc,
       "advancedUrlFilteringNextUpdate": advancedUrlFilteringNextUpdate,
       "advancedUrlFilteringVersion": advancedUrlFilteringVersion,
       "advancedUrlFilteringRADStatus": advancedUrlFilteringRADStatus,
       "advancedUrlFilteringRADStatusCode": advancedUrlFilteringRADStatusCode,
       "advancedUrlFilteringRADStatusDesc": advancedUrlFilteringRADStatusDesc,
       "advancedUrlFilteringStatusCode": advancedUrlFilteringStatusCode,
       "advancedUrlFilteringStatusShortDesc": advancedUrlFilteringStatusShortDesc,
       "advancedUrlFilteringStatusLongDesc": advancedUrlFilteringStatusLongDesc,
       "dlp": dlp,
       "exchangeAgents": exchangeAgents,
       "exchangeAgentsTable": exchangeAgentsTable,
       "exchangeAgentsStatusEntry": exchangeAgentsStatusEntry,
       "exchangeAgentsStatusTableIndex": exchangeAgentsStatusTableIndex,
       "exchangeAgentName": exchangeAgentName,
       "exchangeAgentStatus": exchangeAgentStatus,
       "exchangeAgentTotalMsg": exchangeAgentTotalMsg,
       "exchangeAgentTotalScannedMsg": exchangeAgentTotalScannedMsg,
       "exchangeAgentDroppedMsg": exchangeAgentDroppedMsg,
       "exchangeAgentUpTime": exchangeAgentUpTime,
       "exchangeAgentTimeSinceLastMsg": exchangeAgentTimeSinceLastMsg,
       "exchangeAgentQueueLen": exchangeAgentQueueLen,
       "exchangeQueueLen": exchangeQueueLen,
       "exchangeAgentAvgTimePerMsg": exchangeAgentAvgTimePerMsg,
       "exchangeAgentAvgTimePerScannedMsg": exchangeAgentAvgTimePerScannedMsg,
       "exchangeAgentVersion": exchangeAgentVersion,
       "exchangeCPUUsage": exchangeCPUUsage,
       "exchangeMemoryUsage": exchangeMemoryUsage,
       "exchangeAgentPolicyTimeStamp": exchangeAgentPolicyTimeStamp,
       "dlpVersionString": dlpVersionString,
       "dlpLicenseStatus": dlpLicenseStatus,
       "dlpLdapStatus": dlpLdapStatus,
       "dlpTotalScans": dlpTotalScans,
       "dlpSMTPScans": dlpSMTPScans,
       "dlpSMTPIncidents": dlpSMTPIncidents,
       "dlpLastSMTPScan": dlpLastSMTPScan,
       "dlpNumQuarantined": dlpNumQuarantined,
       "dlpQrntMsgsSize": dlpQrntMsgsSize,
       "dlpSentEMails": dlpSentEMails,
       "dlpExpiredEMails": dlpExpiredEMails,
       "dlpDiscardEMails": dlpDiscardEMails,
       "dlpPostfixQLen": dlpPostfixQLen,
       "dlpPostfixErrors": dlpPostfixErrors,
       "dlpPostfixQOldMsg": dlpPostfixQOldMsg,
       "dlpPostfixQMsgsSz": dlpPostfixQMsgsSz,
       "dlpPostfixQFreeSp": dlpPostfixQFreeSp,
       "dlpQrntFreeSpace": dlpQrntFreeSpace,
       "dlpQrntStatus": dlpQrntStatus,
       "dlpHttpScans": dlpHttpScans,
       "dlpHttpIncidents": dlpHttpIncidents,
       "dlpHttpLastScan": dlpHttpLastScan,
       "dlpFtpScans": dlpFtpScans,
       "dlpFtpIncidents": dlpFtpIncidents,
       "dlpFtpLastScan": dlpFtpLastScan,
       "dlpBypassStatus": dlpBypassStatus,
       "dlpUserCheckClnts": dlpUserCheckClnts,
       "dlpLastPolStatus": dlpLastPolStatus,
       "dlpStatusCode": dlpStatusCode,
       "dlpStatusShortDesc": dlpStatusShortDesc,
       "dlpStatusLongDesc": dlpStatusLongDesc,
       "amw": amw,
       "amwABUpdate": amwABUpdate,
       "amwABUpdateStatus": amwABUpdateStatus,
       "amwABUpdateDesc": amwABUpdateDesc,
       "amwABNextUpdate": amwABNextUpdate,
       "amwABVersion": amwABVersion,
       "antiBotSubscription": antiBotSubscription,
       "antiBotSubscriptionStatus": antiBotSubscriptionStatus,
       "antiBotSubscriptionExpDate": antiBotSubscriptionExpDate,
       "antiBotSubscriptionDesc": antiBotSubscriptionDesc,
       "antiVirusSubscription": antiVirusSubscription,
       "antiVirusSubscriptionStatus": antiVirusSubscriptionStatus,
       "antiVirusSubscriptionExpDate": antiVirusSubscriptionExpDate,
       "antiVirusSubscriptionDesc": antiVirusSubscriptionDesc,
       "antiSpamSubscription": antiSpamSubscription,
       "antiSpamSubscriptionStatus": antiSpamSubscriptionStatus,
       "antiSpamSubscriptionExpDate": antiSpamSubscriptionExpDate,
       "antiSpamSubscriptionDesc": antiSpamSubscriptionDesc,
       "amwAVUpdate": amwAVUpdate,
       "amwAVUpdateStatus": amwAVUpdateStatus,
       "amwAVUpdateDesc": amwAVUpdateDesc,
       "amwAVNextUpdate": amwAVNextUpdate,
       "amwAVVersion": amwAVVersion,
       "amwStatusCode": amwStatusCode,
       "amwStatusShortDesc": amwStatusShortDesc,
       "amwStatusLongDesc": amwStatusLongDesc,
       "te": te,
       "teUpdateStatus": teUpdateStatus,
       "teUpdateDesc": teUpdateDesc,
       "teSubscriptionExpDate": teSubscriptionExpDate,
       "teSubscriptionStatus": teSubscriptionStatus,
       "teCloudSubscriptionStatus": teCloudSubscriptionStatus,
       "teSubscriptionDesc": teSubscriptionDesc,
       "teStatusCode": teStatusCode,
       "teStatusShortDesc": teStatusShortDesc,
       "teStatusLongDesc": teStatusLongDesc,
       "tables": tables,
       "raUsersTable": raUsersTable,
       "raUsersEntry": raUsersEntry,
       "raInternalIpAddr": raInternalIpAddr,
       "raExternalIpAddr": raExternalIpAddr,
       "raUserState": raUserState,
       "raOfficeMode": raOfficeMode,
       "raIkeOverTCP": raIkeOverTCP,
       "raUseUDPEncap": raUseUDPEncap,
       "raVisitorMode": raVisitorMode,
       "raRouteTraffic": raRouteTraffic,
       "raCommunity": raCommunity,
       "raTunnelEncAlgorithm": raTunnelEncAlgorithm,
       "raTunnelAuthMethod": raTunnelAuthMethod,
       "raLogonTime": raLogonTime,
       "tunnelTable": tunnelTable,
       "tunnelEntry": tunnelEntry,
       "tunnelPeerIpAddr": tunnelPeerIpAddr,
       "tunnelPeerObjName": tunnelPeerObjName,
       "tunnelState": tunnelState,
       "tunnelCommunity": tunnelCommunity,
       "tunnelNextHop": tunnelNextHop,
       "tunnelInterface": tunnelInterface,
       "tunnelSourceIpAddr": tunnelSourceIpAddr,
       "tunnelLinkPriority": tunnelLinkPriority,
       "tunnelProbState": tunnelProbState,
       "tunnelPeerType": tunnelPeerType,
       "tunnelType": tunnelType,
       "permanentTunnelTable": permanentTunnelTable,
       "permanentTunnelEntry": permanentTunnelEntry,
       "permanentTunnelPeerIpAddr": permanentTunnelPeerIpAddr,
       "permanentTunnelPeerObjName": permanentTunnelPeerObjName,
       "permanentTunnelState": permanentTunnelState,
       "permanentTunnelCommunity": permanentTunnelCommunity,
       "permanentTunnelNextHop": permanentTunnelNextHop,
       "permanentTunnelInterface": permanentTunnelInterface,
       "permanentTunnelSourceIpAddr": permanentTunnelSourceIpAddr,
       "permanentTunnelLinkPriority": permanentTunnelLinkPriority,
       "permanentTunnelProbState": permanentTunnelProbState,
       "permanentTunnelPeerType": permanentTunnelPeerType}
)
