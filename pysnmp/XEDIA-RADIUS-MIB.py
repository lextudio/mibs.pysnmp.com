# SNMP MIB module (XEDIA-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-RADIUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:03 2024
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

(radiusAccServerEntry,) = mibBuilder.importSymbols(
    "RADIUS-ACC-CLIENT-MIB",
    "radiusAccServerEntry")

(radiusAuthServerEntry,) = mibBuilder.importSymbols(
    "RADIUS-AUTH-CLIENT-MIB",
    "radiusAuthServerEntry")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xediaRadiusMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XRadiusObjects_ObjectIdentity = ObjectIdentity
xRadiusObjects = _XRadiusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1)
)
_XRadiuscObjects_ObjectIdentity = ObjectIdentity
xRadiuscObjects = _XRadiuscObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1)
)
_XRadiuscGlobal_ObjectIdentity = ObjectIdentity
xRadiuscGlobal = _XRadiuscGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1)
)
_XRadiuscGlobalCfg_ObjectIdentity = ObjectIdentity
xRadiuscGlobalCfg = _XRadiuscGlobalCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 1)
)


class _XradiuscAdminAuthStatus_Type(Integer32):
    """Custom type xradiuscAdminAuthStatus based on Integer32"""
    defaultValue = 1

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


_XradiuscAdminAuthStatus_Type.__name__ = "Integer32"
_XradiuscAdminAuthStatus_Object = MibScalar
xradiuscAdminAuthStatus = _XradiuscAdminAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 1, 1),
    _XradiuscAdminAuthStatus_Type()
)
xradiuscAdminAuthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xradiuscAdminAuthStatus.setStatus("current")


class _XradiuscAdminActgStatus_Type(Integer32):
    """Custom type xradiuscAdminActgStatus based on Integer32"""
    defaultValue = 1

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


_XradiuscAdminActgStatus_Type.__name__ = "Integer32"
_XradiuscAdminActgStatus_Object = MibScalar
xradiuscAdminActgStatus = _XradiuscAdminActgStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 1, 2),
    _XradiuscAdminActgStatus_Type()
)
xradiuscAdminActgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xradiuscAdminActgStatus.setStatus("current")


class _XradiuscDebugCmd_Type(DisplayString):
    """Custom type xradiuscDebugCmd based on DisplayString"""
    defaultValue = OctetString("rx-pkt-dump:off; tx-pkt-dump:off; error-print:off; trace-print:off")


_XradiuscDebugCmd_Object = MibScalar
xradiuscDebugCmd = _XradiuscDebugCmd_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 1, 3),
    _XradiuscDebugCmd_Type()
)
xradiuscDebugCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xradiuscDebugCmd.setStatus("current")


class _XradiuscNasId_Type(DisplayString):
    """Custom type xradiuscNasId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_XradiuscNasId_Type.__name__ = "DisplayString"
_XradiuscNasId_Object = MibScalar
xradiuscNasId = _XradiuscNasId_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 1, 4),
    _XradiuscNasId_Type()
)
xradiuscNasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xradiuscNasId.setStatus("current")


class _XradiuscNasIP_Type(IpAddress):
    """Custom type xradiuscNasIP based on IpAddress"""
    defaultValue = 0


_XradiuscNasIP_Object = MibScalar
xradiuscNasIP = _XradiuscNasIP_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 1, 5),
    _XradiuscNasIP_Type()
)
xradiuscNasIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xradiuscNasIP.setStatus("current")


class _XradiuscBackgroundTimer_Type(Integer32):
    """Custom type xradiuscBackgroundTimer based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 86400),
    )


_XradiuscBackgroundTimer_Type.__name__ = "Integer32"
_XradiuscBackgroundTimer_Object = MibScalar
xradiuscBackgroundTimer = _XradiuscBackgroundTimer_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 1, 6),
    _XradiuscBackgroundTimer_Type()
)
xradiuscBackgroundTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xradiuscBackgroundTimer.setStatus("current")


class _XradiuscMaxOutstanding_Type(Integer32):
    """Custom type xradiuscMaxOutstanding based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_XradiuscMaxOutstanding_Type.__name__ = "Integer32"
_XradiuscMaxOutstanding_Object = MibScalar
xradiuscMaxOutstanding = _XradiuscMaxOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 1, 7),
    _XradiuscMaxOutstanding_Type()
)
xradiuscMaxOutstanding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xradiuscMaxOutstanding.setStatus("current")
_XRadiuscGlobalStat_ObjectIdentity = ObjectIdentity
xRadiuscGlobalStat = _XRadiuscGlobalStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2)
)


class _XradiuscOperAuthStatus_Type(Integer32):
    """Custom type xradiuscOperAuthStatus based on Integer32"""
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
          ("stalled", 3),
          ("up", 1))
    )


_XradiuscOperAuthStatus_Type.__name__ = "Integer32"
_XradiuscOperAuthStatus_Object = MibScalar
xradiuscOperAuthStatus = _XradiuscOperAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 1),
    _XradiuscOperAuthStatus_Type()
)
xradiuscOperAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperAuthStatus.setStatus("current")


class _XradiuscOperActgStatus_Type(Integer32):
    """Custom type xradiuscOperActgStatus based on Integer32"""
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
          ("stalled", 3),
          ("up", 1))
    )


_XradiuscOperActgStatus_Type.__name__ = "Integer32"
_XradiuscOperActgStatus_Object = MibScalar
xradiuscOperActgStatus = _XradiuscOperActgStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 2),
    _XradiuscOperActgStatus_Type()
)
xradiuscOperActgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperActgStatus.setStatus("current")
_XradiuscOperNasId_Type = DisplayString
_XradiuscOperNasId_Object = MibScalar
xradiuscOperNasId = _XradiuscOperNasId_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 3),
    _XradiuscOperNasId_Type()
)
xradiuscOperNasId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperNasId.setStatus("current")
_XradiuscOperNasIP_Type = IpAddress
_XradiuscOperNasIP_Object = MibScalar
xradiuscOperNasIP = _XradiuscOperNasIP_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 4),
    _XradiuscOperNasIP_Type()
)
xradiuscOperNasIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperNasIP.setStatus("current")
_XradiuscOperGenErrors_Type = Counter32
_XradiuscOperGenErrors_Object = MibScalar
xradiuscOperGenErrors = _XradiuscOperGenErrors_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 5),
    _XradiuscOperGenErrors_Type()
)
xradiuscOperGenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperGenErrors.setStatus("current")
_XradiuscOperAuthQCurr_Type = Integer32
_XradiuscOperAuthQCurr_Object = MibScalar
xradiuscOperAuthQCurr = _XradiuscOperAuthQCurr_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 6),
    _XradiuscOperAuthQCurr_Type()
)
xradiuscOperAuthQCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperAuthQCurr.setStatus("current")
_XradiuscOperAuthQMax_Type = Gauge32
_XradiuscOperAuthQMax_Object = MibScalar
xradiuscOperAuthQMax = _XradiuscOperAuthQMax_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 7),
    _XradiuscOperAuthQMax_Type()
)
xradiuscOperAuthQMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperAuthQMax.setStatus("current")
_XradiuscOperAuthExpected_Type = Integer32
_XradiuscOperAuthExpected_Object = MibScalar
xradiuscOperAuthExpected = _XradiuscOperAuthExpected_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 8),
    _XradiuscOperAuthExpected_Type()
)
xradiuscOperAuthExpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperAuthExpected.setStatus("current")
_XradiuscOperAuthEnqueued_Type = Counter32
_XradiuscOperAuthEnqueued_Object = MibScalar
xradiuscOperAuthEnqueued = _XradiuscOperAuthEnqueued_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 9),
    _XradiuscOperAuthEnqueued_Type()
)
xradiuscOperAuthEnqueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperAuthEnqueued.setStatus("current")
_XradiuscOperAuthDequeued_Type = Counter32
_XradiuscOperAuthDequeued_Object = MibScalar
xradiuscOperAuthDequeued = _XradiuscOperAuthDequeued_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 10),
    _XradiuscOperAuthDequeued_Type()
)
xradiuscOperAuthDequeued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperAuthDequeued.setStatus("current")
_XradiuscOperActgQCurr_Type = Integer32
_XradiuscOperActgQCurr_Object = MibScalar
xradiuscOperActgQCurr = _XradiuscOperActgQCurr_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 11),
    _XradiuscOperActgQCurr_Type()
)
xradiuscOperActgQCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperActgQCurr.setStatus("current")
_XradiuscOperActgQMax_Type = Gauge32
_XradiuscOperActgQMax_Object = MibScalar
xradiuscOperActgQMax = _XradiuscOperActgQMax_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 12),
    _XradiuscOperActgQMax_Type()
)
xradiuscOperActgQMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperActgQMax.setStatus("current")
_XradiuscOperActgExpected_Type = Integer32
_XradiuscOperActgExpected_Object = MibScalar
xradiuscOperActgExpected = _XradiuscOperActgExpected_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 13),
    _XradiuscOperActgExpected_Type()
)
xradiuscOperActgExpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperActgExpected.setStatus("current")
_XradiuscOperActgEnqueued_Type = Counter32
_XradiuscOperActgEnqueued_Object = MibScalar
xradiuscOperActgEnqueued = _XradiuscOperActgEnqueued_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 14),
    _XradiuscOperActgEnqueued_Type()
)
xradiuscOperActgEnqueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperActgEnqueued.setStatus("current")
_XradiuscOperActgDequeued_Type = Counter32
_XradiuscOperActgDequeued_Object = MibScalar
xradiuscOperActgDequeued = _XradiuscOperActgDequeued_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 15),
    _XradiuscOperActgDequeued_Type()
)
xradiuscOperActgDequeued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperActgDequeued.setStatus("current")
_XradiuscOperPendingListCurr_Type = Integer32
_XradiuscOperPendingListCurr_Object = MibScalar
xradiuscOperPendingListCurr = _XradiuscOperPendingListCurr_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 16),
    _XradiuscOperPendingListCurr_Type()
)
xradiuscOperPendingListCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperPendingListCurr.setStatus("current")
_XradiuscOperPendingListMax_Type = Gauge32
_XradiuscOperPendingListMax_Object = MibScalar
xradiuscOperPendingListMax = _XradiuscOperPendingListMax_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 17),
    _XradiuscOperPendingListMax_Type()
)
xradiuscOperPendingListMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperPendingListMax.setStatus("current")
_XradiuscOperPendingExpected_Type = Integer32
_XradiuscOperPendingExpected_Object = MibScalar
xradiuscOperPendingExpected = _XradiuscOperPendingExpected_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 18),
    _XradiuscOperPendingExpected_Type()
)
xradiuscOperPendingExpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperPendingExpected.setStatus("current")
_XradiuscOperPendingEnqueued_Type = Counter32
_XradiuscOperPendingEnqueued_Object = MibScalar
xradiuscOperPendingEnqueued = _XradiuscOperPendingEnqueued_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 19),
    _XradiuscOperPendingEnqueued_Type()
)
xradiuscOperPendingEnqueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperPendingEnqueued.setStatus("current")
_XradiuscOperPendingDequeued_Type = Counter32
_XradiuscOperPendingDequeued_Object = MibScalar
xradiuscOperPendingDequeued = _XradiuscOperPendingDequeued_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 20),
    _XradiuscOperPendingDequeued_Type()
)
xradiuscOperPendingDequeued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperPendingDequeued.setStatus("current")
_XradiuscOperLastPktID_Type = Integer32
_XradiuscOperLastPktID_Object = MibScalar
xradiuscOperLastPktID = _XradiuscOperLastPktID_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 21),
    _XradiuscOperLastPktID_Type()
)
xradiuscOperLastPktID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperLastPktID.setStatus("current")
_XradiuscOperNextPktID_Type = Integer32
_XradiuscOperNextPktID_Object = MibScalar
xradiuscOperNextPktID = _XradiuscOperNextPktID_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 22),
    _XradiuscOperNextPktID_Type()
)
xradiuscOperNextPktID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperNextPktID.setStatus("current")
_XradiuscOperLastAuthIndex_Type = Integer32
_XradiuscOperLastAuthIndex_Object = MibScalar
xradiuscOperLastAuthIndex = _XradiuscOperLastAuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 23),
    _XradiuscOperLastAuthIndex_Type()
)
xradiuscOperLastAuthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperLastAuthIndex.setStatus("current")
_XradiuscOperLastActgIndex_Type = Integer32
_XradiuscOperLastActgIndex_Object = MibScalar
xradiuscOperLastActgIndex = _XradiuscOperLastActgIndex_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 1, 2, 24),
    _XradiuscOperLastActgIndex_Type()
)
xradiuscOperLastActgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscOperLastActgIndex.setStatus("current")
_XRadiuscAuthentication_ObjectIdentity = ObjectIdentity
xRadiuscAuthentication = _XRadiuscAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 2)
)
_XRadiuscAuthSvrTable_Object = MibTable
xRadiuscAuthSvrTable = _XRadiuscAuthSvrTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    xRadiuscAuthSvrTable.setStatus("current")
_XRadiuscAuthSvrEntry_Object = MibTableRow
xRadiuscAuthSvrEntry = _XRadiuscAuthSvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xRadiuscAuthSvrEntry.setStatus("current")


class _XradiuscAuthSvrIpAddress_Type(IpAddress):
    """Custom type xradiuscAuthSvrIpAddress based on IpAddress"""
    defaultValue = 0


_XradiuscAuthSvrIpAddress_Object = MibTableColumn
xradiuscAuthSvrIpAddress = _XradiuscAuthSvrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 2, 1, 1, 1),
    _XradiuscAuthSvrIpAddress_Type()
)
xradiuscAuthSvrIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xradiuscAuthSvrIpAddress.setStatus("current")
_XradiuscAuthSvrName_Type = DisplayString
_XradiuscAuthSvrName_Object = MibTableColumn
xradiuscAuthSvrName = _XradiuscAuthSvrName_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 2, 1, 1, 2),
    _XradiuscAuthSvrName_Type()
)
xradiuscAuthSvrName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xradiuscAuthSvrName.setStatus("current")


class _XradiuscAuthSvrPort_Type(Integer32):
    """Custom type xradiuscAuthSvrPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_XradiuscAuthSvrPort_Type.__name__ = "Integer32"
_XradiuscAuthSvrPort_Object = MibTableColumn
xradiuscAuthSvrPort = _XradiuscAuthSvrPort_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 2, 1, 1, 3),
    _XradiuscAuthSvrPort_Type()
)
xradiuscAuthSvrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xradiuscAuthSvrPort.setStatus("current")


class _XradiuscAuthSvrTimeout_Type(Integer32):
    """Custom type xradiuscAuthSvrTimeout based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_XradiuscAuthSvrTimeout_Type.__name__ = "Integer32"
_XradiuscAuthSvrTimeout_Object = MibTableColumn
xradiuscAuthSvrTimeout = _XradiuscAuthSvrTimeout_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 2, 1, 1, 4),
    _XradiuscAuthSvrTimeout_Type()
)
xradiuscAuthSvrTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xradiuscAuthSvrTimeout.setStatus("current")


class _XradiuscAuthSvrRetries_Type(Integer32):
    """Custom type xradiuscAuthSvrRetries based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_XradiuscAuthSvrRetries_Type.__name__ = "Integer32"
_XradiuscAuthSvrRetries_Object = MibTableColumn
xradiuscAuthSvrRetries = _XradiuscAuthSvrRetries_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 2, 1, 1, 5),
    _XradiuscAuthSvrRetries_Type()
)
xradiuscAuthSvrRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xradiuscAuthSvrRetries.setStatus("current")


class _XradiuscAuthSvrPriority_Type(Integer32):
    """Custom type xradiuscAuthSvrPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_XradiuscAuthSvrPriority_Type.__name__ = "Integer32"
_XradiuscAuthSvrPriority_Object = MibTableColumn
xradiuscAuthSvrPriority = _XradiuscAuthSvrPriority_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 2, 1, 1, 6),
    _XradiuscAuthSvrPriority_Type()
)
xradiuscAuthSvrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xradiuscAuthSvrPriority.setStatus("current")
_XradiuscAuthSvrSecretKey_Type = DisplayString
_XradiuscAuthSvrSecretKey_Object = MibTableColumn
xradiuscAuthSvrSecretKey = _XradiuscAuthSvrSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 2, 1, 1, 7),
    _XradiuscAuthSvrSecretKey_Type()
)
xradiuscAuthSvrSecretKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xradiuscAuthSvrSecretKey.setStatus("current")


class _XradiuscAuthSvrVendorOffset_Type(Integer32):
    """Custom type xradiuscAuthSvrVendorOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_XradiuscAuthSvrVendorOffset_Type.__name__ = "Integer32"
_XradiuscAuthSvrVendorOffset_Object = MibTableColumn
xradiuscAuthSvrVendorOffset = _XradiuscAuthSvrVendorOffset_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 2, 1, 1, 8),
    _XradiuscAuthSvrVendorOffset_Type()
)
xradiuscAuthSvrVendorOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xradiuscAuthSvrVendorOffset.setStatus("current")
_XradiuscAuthSvrOperIpAddress_Type = IpAddress
_XradiuscAuthSvrOperIpAddress_Object = MibTableColumn
xradiuscAuthSvrOperIpAddress = _XradiuscAuthSvrOperIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 2, 1, 1, 9),
    _XradiuscAuthSvrOperIpAddress_Type()
)
xradiuscAuthSvrOperIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscAuthSvrOperIpAddress.setStatus("current")


class _XradiuscAuthSvrOperState_Type(Integer32):
    """Custom type xradiuscAuthSvrOperState based on Integer32"""
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
        *(("notAvailable", 4),
          ("notResponding", 3),
          ("responding", 2),
          ("unknown", 1))
    )


_XradiuscAuthSvrOperState_Type.__name__ = "Integer32"
_XradiuscAuthSvrOperState_Object = MibTableColumn
xradiuscAuthSvrOperState = _XradiuscAuthSvrOperState_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 2, 1, 1, 10),
    _XradiuscAuthSvrOperState_Type()
)
xradiuscAuthSvrOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscAuthSvrOperState.setStatus("current")
_XradiuscAuthSvrOperStateChange_Type = TimeTicks
_XradiuscAuthSvrOperStateChange_Object = MibTableColumn
xradiuscAuthSvrOperStateChange = _XradiuscAuthSvrOperStateChange_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 2, 1, 1, 11),
    _XradiuscAuthSvrOperStateChange_Type()
)
xradiuscAuthSvrOperStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscAuthSvrOperStateChange.setStatus("current")
_XradiuscAuthSvrOperBadPktIds_Type = Counter32
_XradiuscAuthSvrOperBadPktIds_Object = MibTableColumn
xradiuscAuthSvrOperBadPktIds = _XradiuscAuthSvrOperBadPktIds_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 2, 1, 1, 12),
    _XradiuscAuthSvrOperBadPktIds_Type()
)
xradiuscAuthSvrOperBadPktIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscAuthSvrOperBadPktIds.setStatus("current")
_XradiuscAuthSvrOperRxErrors_Type = Counter32
_XradiuscAuthSvrOperRxErrors_Object = MibTableColumn
xradiuscAuthSvrOperRxErrors = _XradiuscAuthSvrOperRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 2, 1, 1, 13),
    _XradiuscAuthSvrOperRxErrors_Type()
)
xradiuscAuthSvrOperRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscAuthSvrOperRxErrors.setStatus("current")
_XradiuscAuthSvrOperTxErrors_Type = Counter32
_XradiuscAuthSvrOperTxErrors_Object = MibTableColumn
xradiuscAuthSvrOperTxErrors = _XradiuscAuthSvrOperTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 2, 1, 1, 14),
    _XradiuscAuthSvrOperTxErrors_Type()
)
xradiuscAuthSvrOperTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscAuthSvrOperTxErrors.setStatus("current")
_XradiuscAuthSvrRowStatus_Type = RowStatus
_XradiuscAuthSvrRowStatus_Object = MibTableColumn
xradiuscAuthSvrRowStatus = _XradiuscAuthSvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 2, 1, 1, 15),
    _XradiuscAuthSvrRowStatus_Type()
)
xradiuscAuthSvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xradiuscAuthSvrRowStatus.setStatus("current")
_XRadiuscAccounting_ObjectIdentity = ObjectIdentity
xRadiuscAccounting = _XRadiuscAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 3)
)
_XRadiuscActgSvrTable_Object = MibTable
xRadiuscActgSvrTable = _XRadiuscActgSvrTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    xRadiuscActgSvrTable.setStatus("current")
_XRadiuscActgSvrEntry_Object = MibTableRow
xRadiuscActgSvrEntry = _XRadiuscActgSvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    xRadiuscActgSvrEntry.setStatus("current")


class _XradiuscActgSvrIpAddress_Type(IpAddress):
    """Custom type xradiuscActgSvrIpAddress based on IpAddress"""
    defaultValue = 0


_XradiuscActgSvrIpAddress_Object = MibTableColumn
xradiuscActgSvrIpAddress = _XradiuscActgSvrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 3, 1, 1, 1),
    _XradiuscActgSvrIpAddress_Type()
)
xradiuscActgSvrIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xradiuscActgSvrIpAddress.setStatus("current")
_XradiuscActgSvrName_Type = DisplayString
_XradiuscActgSvrName_Object = MibTableColumn
xradiuscActgSvrName = _XradiuscActgSvrName_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 3, 1, 1, 2),
    _XradiuscActgSvrName_Type()
)
xradiuscActgSvrName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xradiuscActgSvrName.setStatus("current")


class _XradiuscActgSvrPort_Type(Integer32):
    """Custom type xradiuscActgSvrPort based on Integer32"""
    defaultValue = 1813

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_XradiuscActgSvrPort_Type.__name__ = "Integer32"
_XradiuscActgSvrPort_Object = MibTableColumn
xradiuscActgSvrPort = _XradiuscActgSvrPort_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 3, 1, 1, 3),
    _XradiuscActgSvrPort_Type()
)
xradiuscActgSvrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xradiuscActgSvrPort.setStatus("current")


class _XradiuscActgSvrTimeout_Type(Integer32):
    """Custom type xradiuscActgSvrTimeout based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_XradiuscActgSvrTimeout_Type.__name__ = "Integer32"
_XradiuscActgSvrTimeout_Object = MibTableColumn
xradiuscActgSvrTimeout = _XradiuscActgSvrTimeout_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 3, 1, 1, 4),
    _XradiuscActgSvrTimeout_Type()
)
xradiuscActgSvrTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xradiuscActgSvrTimeout.setStatus("current")


class _XradiuscActgSvrRetries_Type(Integer32):
    """Custom type xradiuscActgSvrRetries based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_XradiuscActgSvrRetries_Type.__name__ = "Integer32"
_XradiuscActgSvrRetries_Object = MibTableColumn
xradiuscActgSvrRetries = _XradiuscActgSvrRetries_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 3, 1, 1, 5),
    _XradiuscActgSvrRetries_Type()
)
xradiuscActgSvrRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xradiuscActgSvrRetries.setStatus("current")


class _XradiuscActgSvrPriority_Type(Integer32):
    """Custom type xradiuscActgSvrPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_XradiuscActgSvrPriority_Type.__name__ = "Integer32"
_XradiuscActgSvrPriority_Object = MibTableColumn
xradiuscActgSvrPriority = _XradiuscActgSvrPriority_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 3, 1, 1, 6),
    _XradiuscActgSvrPriority_Type()
)
xradiuscActgSvrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xradiuscActgSvrPriority.setStatus("current")
_XradiuscActgSvrSecretKey_Type = DisplayString
_XradiuscActgSvrSecretKey_Object = MibTableColumn
xradiuscActgSvrSecretKey = _XradiuscActgSvrSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 3, 1, 1, 7),
    _XradiuscActgSvrSecretKey_Type()
)
xradiuscActgSvrSecretKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xradiuscActgSvrSecretKey.setStatus("current")


class _XradiuscActgSvrVendorOffset_Type(Integer32):
    """Custom type xradiuscActgSvrVendorOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_XradiuscActgSvrVendorOffset_Type.__name__ = "Integer32"
_XradiuscActgSvrVendorOffset_Object = MibTableColumn
xradiuscActgSvrVendorOffset = _XradiuscActgSvrVendorOffset_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 3, 1, 1, 8),
    _XradiuscActgSvrVendorOffset_Type()
)
xradiuscActgSvrVendorOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xradiuscActgSvrVendorOffset.setStatus("current")
_XradiuscActgSvrOperIpAddress_Type = IpAddress
_XradiuscActgSvrOperIpAddress_Object = MibTableColumn
xradiuscActgSvrOperIpAddress = _XradiuscActgSvrOperIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 3, 1, 1, 9),
    _XradiuscActgSvrOperIpAddress_Type()
)
xradiuscActgSvrOperIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscActgSvrOperIpAddress.setStatus("current")


class _XradiuscActgSvrOperState_Type(Integer32):
    """Custom type xradiuscActgSvrOperState based on Integer32"""
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
        *(("notAvailable", 4),
          ("notResponding", 3),
          ("responding", 2),
          ("unknown", 1))
    )


_XradiuscActgSvrOperState_Type.__name__ = "Integer32"
_XradiuscActgSvrOperState_Object = MibTableColumn
xradiuscActgSvrOperState = _XradiuscActgSvrOperState_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 3, 1, 1, 10),
    _XradiuscActgSvrOperState_Type()
)
xradiuscActgSvrOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscActgSvrOperState.setStatus("current")
_XradiuscActgSvrOperStateChange_Type = TimeTicks
_XradiuscActgSvrOperStateChange_Object = MibTableColumn
xradiuscActgSvrOperStateChange = _XradiuscActgSvrOperStateChange_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 3, 1, 1, 11),
    _XradiuscActgSvrOperStateChange_Type()
)
xradiuscActgSvrOperStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscActgSvrOperStateChange.setStatus("current")
_XradiuscActgSvrOperBadPktIds_Type = Counter32
_XradiuscActgSvrOperBadPktIds_Object = MibTableColumn
xradiuscActgSvrOperBadPktIds = _XradiuscActgSvrOperBadPktIds_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 3, 1, 1, 12),
    _XradiuscActgSvrOperBadPktIds_Type()
)
xradiuscActgSvrOperBadPktIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscActgSvrOperBadPktIds.setStatus("current")
_XradiuscActgSvrOperRxErrors_Type = Counter32
_XradiuscActgSvrOperRxErrors_Object = MibTableColumn
xradiuscActgSvrOperRxErrors = _XradiuscActgSvrOperRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 3, 1, 1, 13),
    _XradiuscActgSvrOperRxErrors_Type()
)
xradiuscActgSvrOperRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscActgSvrOperRxErrors.setStatus("current")
_XradiuscActgSvrOperTxErrors_Type = Counter32
_XradiuscActgSvrOperTxErrors_Object = MibTableColumn
xradiuscActgSvrOperTxErrors = _XradiuscActgSvrOperTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 3, 1, 1, 14),
    _XradiuscActgSvrOperTxErrors_Type()
)
xradiuscActgSvrOperTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xradiuscActgSvrOperTxErrors.setStatus("current")
_XradiuscActgSvrRowStatus_Type = RowStatus
_XradiuscActgSvrRowStatus_Object = MibTableColumn
xradiuscActgSvrRowStatus = _XradiuscActgSvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 1, 1, 3, 1, 1, 15),
    _XradiuscActgSvrRowStatus_Type()
)
xradiuscActgSvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xradiuscActgSvrRowStatus.setStatus("current")
_XRadiusConformance_ObjectIdentity = ObjectIdentity
xRadiusConformance = _XRadiusConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 2)
)
_XradiusCompliances_ObjectIdentity = ObjectIdentity
xradiusCompliances = _XradiusCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 2, 1)
)
_XradiusGroups_ObjectIdentity = ObjectIdentity
xradiusGroups = _XradiusGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 2, 2)
)
radiusAuthServerEntry.registerAugmentions(
    ("XEDIA-RADIUS-MIB",
     "xRadiuscAuthSvrEntry")
)
xRadiuscAuthSvrEntry.setIndexNames(*radiusAuthServerEntry.getIndexNames())
radiusAccServerEntry.registerAugmentions(
    ("XEDIA-RADIUS-MIB",
     "xRadiuscActgSvrEntry")
)
xRadiuscActgSvrEntry.setIndexNames(*radiusAccServerEntry.getIndexNames())

# Managed Objects groups

xradiusAllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 2, 2, 1)
)
xradiusAllGroup.setObjects(
      *(("XEDIA-RADIUS-MIB", "xradiuscAdminAuthStatus"),
        ("XEDIA-RADIUS-MIB", "xradiuscAdminActgStatus"),
        ("XEDIA-RADIUS-MIB", "xradiuscDebugCmd"),
        ("XEDIA-RADIUS-MIB", "xradiuscNasId"),
        ("XEDIA-RADIUS-MIB", "xradiuscNasIP"),
        ("XEDIA-RADIUS-MIB", "xradiuscBackgroundTimer"),
        ("XEDIA-RADIUS-MIB", "xradiuscMaxOutstanding"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperAuthStatus"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperActgStatus"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperNasId"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperNasIP"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperGenErrors"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperAuthQCurr"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperAuthQMax"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperAuthExpected"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperAuthEnqueued"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperAuthDequeued"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperActgQCurr"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperActgQMax"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperActgExpected"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperActgEnqueued"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperActgDequeued"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperLastPktID"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperNextPktID"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperLastAuthIndex"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperLastActgIndex"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperPendingListCurr"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperPendingListMax"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperPendingExpected"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperPendingEnqueued"),
        ("XEDIA-RADIUS-MIB", "xradiuscOperPendingDequeued"),
        ("XEDIA-RADIUS-MIB", "xradiuscAuthSvrIpAddress"),
        ("XEDIA-RADIUS-MIB", "xradiuscAuthSvrName"),
        ("XEDIA-RADIUS-MIB", "xradiuscAuthSvrPort"),
        ("XEDIA-RADIUS-MIB", "xradiuscAuthSvrTimeout"),
        ("XEDIA-RADIUS-MIB", "xradiuscAuthSvrRetries"),
        ("XEDIA-RADIUS-MIB", "xradiuscAuthSvrPriority"),
        ("XEDIA-RADIUS-MIB", "xradiuscAuthSvrSecretKey"),
        ("XEDIA-RADIUS-MIB", "xradiuscAuthSvrVendorOffset"),
        ("XEDIA-RADIUS-MIB", "xradiuscAuthSvrRowStatus"),
        ("XEDIA-RADIUS-MIB", "xradiuscAuthSvrOperIpAddress"),
        ("XEDIA-RADIUS-MIB", "xradiuscAuthSvrOperState"),
        ("XEDIA-RADIUS-MIB", "xradiuscAuthSvrOperStateChange"),
        ("XEDIA-RADIUS-MIB", "xradiuscAuthSvrOperBadPktIds"),
        ("XEDIA-RADIUS-MIB", "xradiuscAuthSvrOperRxErrors"),
        ("XEDIA-RADIUS-MIB", "xradiuscAuthSvrOperTxErrors"),
        ("XEDIA-RADIUS-MIB", "xradiuscActgSvrIpAddress"),
        ("XEDIA-RADIUS-MIB", "xradiuscActgSvrName"),
        ("XEDIA-RADIUS-MIB", "xradiuscActgSvrPort"),
        ("XEDIA-RADIUS-MIB", "xradiuscActgSvrTimeout"),
        ("XEDIA-RADIUS-MIB", "xradiuscActgSvrRetries"),
        ("XEDIA-RADIUS-MIB", "xradiuscActgSvrPriority"),
        ("XEDIA-RADIUS-MIB", "xradiuscActgSvrSecretKey"),
        ("XEDIA-RADIUS-MIB", "xradiuscActgSvrVendorOffset"),
        ("XEDIA-RADIUS-MIB", "xradiuscActgSvrOperIpAddress"),
        ("XEDIA-RADIUS-MIB", "xradiuscActgSvrOperState"),
        ("XEDIA-RADIUS-MIB", "xradiuscActgSvrOperStateChange"),
        ("XEDIA-RADIUS-MIB", "xradiuscActgSvrOperBadPktIds"),
        ("XEDIA-RADIUS-MIB", "xradiuscActgSvrOperRxErrors"),
        ("XEDIA-RADIUS-MIB", "xradiuscActgSvrOperTxErrors"),
        ("XEDIA-RADIUS-MIB", "xradiuscActgSvrRowStatus"))
)
if mibBuilder.loadTexts:
    xradiusAllGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xradiusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 838, 3, 16, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xradiusCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-RADIUS-MIB",
    **{"xediaRadiusMIB": xediaRadiusMIB,
       "xRadiusObjects": xRadiusObjects,
       "xRadiuscObjects": xRadiuscObjects,
       "xRadiuscGlobal": xRadiuscGlobal,
       "xRadiuscGlobalCfg": xRadiuscGlobalCfg,
       "xradiuscAdminAuthStatus": xradiuscAdminAuthStatus,
       "xradiuscAdminActgStatus": xradiuscAdminActgStatus,
       "xradiuscDebugCmd": xradiuscDebugCmd,
       "xradiuscNasId": xradiuscNasId,
       "xradiuscNasIP": xradiuscNasIP,
       "xradiuscBackgroundTimer": xradiuscBackgroundTimer,
       "xradiuscMaxOutstanding": xradiuscMaxOutstanding,
       "xRadiuscGlobalStat": xRadiuscGlobalStat,
       "xradiuscOperAuthStatus": xradiuscOperAuthStatus,
       "xradiuscOperActgStatus": xradiuscOperActgStatus,
       "xradiuscOperNasId": xradiuscOperNasId,
       "xradiuscOperNasIP": xradiuscOperNasIP,
       "xradiuscOperGenErrors": xradiuscOperGenErrors,
       "xradiuscOperAuthQCurr": xradiuscOperAuthQCurr,
       "xradiuscOperAuthQMax": xradiuscOperAuthQMax,
       "xradiuscOperAuthExpected": xradiuscOperAuthExpected,
       "xradiuscOperAuthEnqueued": xradiuscOperAuthEnqueued,
       "xradiuscOperAuthDequeued": xradiuscOperAuthDequeued,
       "xradiuscOperActgQCurr": xradiuscOperActgQCurr,
       "xradiuscOperActgQMax": xradiuscOperActgQMax,
       "xradiuscOperActgExpected": xradiuscOperActgExpected,
       "xradiuscOperActgEnqueued": xradiuscOperActgEnqueued,
       "xradiuscOperActgDequeued": xradiuscOperActgDequeued,
       "xradiuscOperPendingListCurr": xradiuscOperPendingListCurr,
       "xradiuscOperPendingListMax": xradiuscOperPendingListMax,
       "xradiuscOperPendingExpected": xradiuscOperPendingExpected,
       "xradiuscOperPendingEnqueued": xradiuscOperPendingEnqueued,
       "xradiuscOperPendingDequeued": xradiuscOperPendingDequeued,
       "xradiuscOperLastPktID": xradiuscOperLastPktID,
       "xradiuscOperNextPktID": xradiuscOperNextPktID,
       "xradiuscOperLastAuthIndex": xradiuscOperLastAuthIndex,
       "xradiuscOperLastActgIndex": xradiuscOperLastActgIndex,
       "xRadiuscAuthentication": xRadiuscAuthentication,
       "xRadiuscAuthSvrTable": xRadiuscAuthSvrTable,
       "xRadiuscAuthSvrEntry": xRadiuscAuthSvrEntry,
       "xradiuscAuthSvrIpAddress": xradiuscAuthSvrIpAddress,
       "xradiuscAuthSvrName": xradiuscAuthSvrName,
       "xradiuscAuthSvrPort": xradiuscAuthSvrPort,
       "xradiuscAuthSvrTimeout": xradiuscAuthSvrTimeout,
       "xradiuscAuthSvrRetries": xradiuscAuthSvrRetries,
       "xradiuscAuthSvrPriority": xradiuscAuthSvrPriority,
       "xradiuscAuthSvrSecretKey": xradiuscAuthSvrSecretKey,
       "xradiuscAuthSvrVendorOffset": xradiuscAuthSvrVendorOffset,
       "xradiuscAuthSvrOperIpAddress": xradiuscAuthSvrOperIpAddress,
       "xradiuscAuthSvrOperState": xradiuscAuthSvrOperState,
       "xradiuscAuthSvrOperStateChange": xradiuscAuthSvrOperStateChange,
       "xradiuscAuthSvrOperBadPktIds": xradiuscAuthSvrOperBadPktIds,
       "xradiuscAuthSvrOperRxErrors": xradiuscAuthSvrOperRxErrors,
       "xradiuscAuthSvrOperTxErrors": xradiuscAuthSvrOperTxErrors,
       "xradiuscAuthSvrRowStatus": xradiuscAuthSvrRowStatus,
       "xRadiuscAccounting": xRadiuscAccounting,
       "xRadiuscActgSvrTable": xRadiuscActgSvrTable,
       "xRadiuscActgSvrEntry": xRadiuscActgSvrEntry,
       "xradiuscActgSvrIpAddress": xradiuscActgSvrIpAddress,
       "xradiuscActgSvrName": xradiuscActgSvrName,
       "xradiuscActgSvrPort": xradiuscActgSvrPort,
       "xradiuscActgSvrTimeout": xradiuscActgSvrTimeout,
       "xradiuscActgSvrRetries": xradiuscActgSvrRetries,
       "xradiuscActgSvrPriority": xradiuscActgSvrPriority,
       "xradiuscActgSvrSecretKey": xradiuscActgSvrSecretKey,
       "xradiuscActgSvrVendorOffset": xradiuscActgSvrVendorOffset,
       "xradiuscActgSvrOperIpAddress": xradiuscActgSvrOperIpAddress,
       "xradiuscActgSvrOperState": xradiuscActgSvrOperState,
       "xradiuscActgSvrOperStateChange": xradiuscActgSvrOperStateChange,
       "xradiuscActgSvrOperBadPktIds": xradiuscActgSvrOperBadPktIds,
       "xradiuscActgSvrOperRxErrors": xradiuscActgSvrOperRxErrors,
       "xradiuscActgSvrOperTxErrors": xradiuscActgSvrOperTxErrors,
       "xradiuscActgSvrRowStatus": xradiuscActgSvrRowStatus,
       "xRadiusConformance": xRadiusConformance,
       "xradiusCompliances": xradiusCompliances,
       "xradiusCompliance": xradiusCompliance,
       "xradiusGroups": xradiusGroups,
       "xradiusAllGroup": xradiusAllGroup}
)
