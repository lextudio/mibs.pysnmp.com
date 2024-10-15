# SNMP MIB module (EMPIRE-SVCRSP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EMPIRE-SVCRSP
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:29 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Empire_ObjectIdentity = ObjectIdentity
empire = _Empire_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546)
)
_Applications_ObjectIdentity = ObjectIdentity
applications = _Applications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16)
)
_SvcRsp_ObjectIdentity = ObjectIdentity
svcRsp = _SvcRsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 6)
)
_SvcRspVersion_Type = DisplayString
_SvcRspVersion_Object = MibScalar
svcRspVersion = _SvcRspVersion_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 1),
    _SvcRspVersion_Type()
)
svcRspVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspVersion.setStatus("mandatory")
_SvcRspPID_Type = Integer32
_SvcRspPID_Object = MibScalar
svcRspPID = _SvcRspPID_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 2),
    _SvcRspPID_Type()
)
svcRspPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspPID.setStatus("mandatory")


class _SvcRspModMode_Type(Integer32):
    """Custom type svcRspModMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullMode", 1),
          ("restrictedMode", 2))
    )


_SvcRspModMode_Type.__name__ = "Integer32"
_SvcRspModMode_Object = MibScalar
svcRspModMode = _SvcRspModMode_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 3),
    _SvcRspModMode_Type()
)
svcRspModMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspModMode.setStatus("mandatory")
_SvcRspTable_Object = MibTable
svcRspTable = _SvcRspTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10)
)
if mibBuilder.loadTexts:
    svcRspTable.setStatus("mandatory")
_SvcRspTableEntry_Object = MibTableRow
svcRspTableEntry = _SvcRspTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1)
)
svcRspTableEntry.setIndexNames(
    (0, "EMPIRE-SVCRSP", "svcRspTableIndex"),
)
if mibBuilder.loadTexts:
    svcRspTableEntry.setStatus("mandatory")
_SvcRspTableIndex_Type = Integer32
_SvcRspTableIndex_Object = MibTableColumn
svcRspTableIndex = _SvcRspTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 1),
    _SvcRspTableIndex_Type()
)
svcRspTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableIndex.setStatus("mandatory")


class _SvcRspTableDescr_Type(DisplayString):
    """Custom type svcRspTableDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SvcRspTableDescr_Type.__name__ = "DisplayString"
_SvcRspTableDescr_Object = MibTableColumn
svcRspTableDescr = _SvcRspTableDescr_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 2),
    _SvcRspTableDescr_Type()
)
svcRspTableDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcRspTableDescr.setStatus("mandatory")


class _SvcRspTableSvc_Type(Integer32):
    """Custom type svcRspTableSvc based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("activeDirectory", 19),
          ("custom", 9),
          ("dhcp", 16),
          ("dns", 2),
          ("fileIO", 22),
          ("ftp", 5),
          ("http", 4),
          ("https", 10),
          ("imap", 11),
          ("ldap", 18),
          ("mapi", 17),
          ("nis", 14),
          ("nntp", 1),
          ("ping", 7),
          ("pop3", 3),
          ("roundTripEmail", 12),
          ("smtp", 6),
          ("snmp", 21),
          ("sqlQuery", 20),
          ("tcpconnect", 8),
          ("tftp", 15),
          ("virtualUserTest", 13))
    )


_SvcRspTableSvc_Type.__name__ = "Integer32"
_SvcRspTableSvc_Object = MibTableColumn
svcRspTableSvc = _SvcRspTableSvc_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 3),
    _SvcRspTableSvc_Type()
)
svcRspTableSvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcRspTableSvc.setStatus("mandatory")


class _SvcRspTableArgs_Type(DisplayString):
    """Custom type svcRspTableArgs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SvcRspTableArgs_Type.__name__ = "DisplayString"
_SvcRspTableArgs_Object = MibTableColumn
svcRspTableArgs = _SvcRspTableArgs_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 4),
    _SvcRspTableArgs_Type()
)
svcRspTableArgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcRspTableArgs.setStatus("mandatory")
_SvcRspTableInterval_Type = Integer32
_SvcRspTableInterval_Object = MibTableColumn
svcRspTableInterval = _SvcRspTableInterval_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 5),
    _SvcRspTableInterval_Type()
)
svcRspTableInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcRspTableInterval.setStatus("mandatory")
_SvcRspTableSamplesPerInterval_Type = Integer32
_SvcRspTableSamplesPerInterval_Object = MibTableColumn
svcRspTableSamplesPerInterval = _SvcRspTableSamplesPerInterval_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 6),
    _SvcRspTableSamplesPerInterval_Type()
)
svcRspTableSamplesPerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcRspTableSamplesPerInterval.setStatus("mandatory")
_SvcRspTableTimeout_Type = Integer32
_SvcRspTableTimeout_Object = MibTableColumn
svcRspTableTimeout = _SvcRspTableTimeout_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 7),
    _SvcRspTableTimeout_Type()
)
svcRspTableTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcRspTableTimeout.setStatus("mandatory")
_SvcRspTableStatsWindow_Type = Integer32
_SvcRspTableStatsWindow_Object = MibTableColumn
svcRspTableStatsWindow = _SvcRspTableStatsWindow_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 8),
    _SvcRspTableStatsWindow_Type()
)
svcRspTableStatsWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcRspTableStatsWindow.setStatus("mandatory")


class _SvcRspTableStatus_Type(Integer32):
    """Custom type svcRspTableStatus based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_SvcRspTableStatus_Type.__name__ = "Integer32"
_SvcRspTableStatus_Object = MibTableColumn
svcRspTableStatus = _SvcRspTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 9),
    _SvcRspTableStatus_Type()
)
svcRspTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcRspTableStatus.setStatus("mandatory")
_SvcRspTableLastUpdate_Type = TimeTicks
_SvcRspTableLastUpdate_Object = MibTableColumn
svcRspTableLastUpdate = _SvcRspTableLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 10),
    _SvcRspTableLastUpdate_Type()
)
svcRspTableLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableLastUpdate.setStatus("mandatory")
_SvcRspTableNumSamples_Type = Counter32
_SvcRspTableNumSamples_Object = MibTableColumn
svcRspTableNumSamples = _SvcRspTableNumSamples_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 11),
    _SvcRspTableNumSamples_Type()
)
svcRspTableNumSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableNumSamples.setStatus("mandatory")
_SvcRspTableTotalLastSample_Type = Integer32
_SvcRspTableTotalLastSample_Object = MibTableColumn
svcRspTableTotalLastSample = _SvcRspTableTotalLastSample_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 12),
    _SvcRspTableTotalLastSample_Type()
)
svcRspTableTotalLastSample.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableTotalLastSample.setStatus("mandatory")
_SvcRspTableTotalMin_Type = Integer32
_SvcRspTableTotalMin_Object = MibTableColumn
svcRspTableTotalMin = _SvcRspTableTotalMin_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 13),
    _SvcRspTableTotalMin_Type()
)
svcRspTableTotalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableTotalMin.setStatus("mandatory")
_SvcRspTableTotalMax_Type = Integer32
_SvcRspTableTotalMax_Object = MibTableColumn
svcRspTableTotalMax = _SvcRspTableTotalMax_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 14),
    _SvcRspTableTotalMax_Type()
)
svcRspTableTotalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableTotalMax.setStatus("mandatory")
_SvcRspTableTotalMean_Type = Integer32
_SvcRspTableTotalMean_Object = MibTableColumn
svcRspTableTotalMean = _SvcRspTableTotalMean_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 15),
    _SvcRspTableTotalMean_Type()
)
svcRspTableTotalMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableTotalMean.setStatus("mandatory")
_SvcRspTableTotalVariance_Type = Integer32
_SvcRspTableTotalVariance_Object = MibTableColumn
svcRspTableTotalVariance = _SvcRspTableTotalVariance_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 16),
    _SvcRspTableTotalVariance_Type()
)
svcRspTableTotalVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableTotalVariance.setStatus("mandatory")
_SvcRspTableTotalAvailability_Type = Integer32
_SvcRspTableTotalAvailability_Object = MibTableColumn
svcRspTableTotalAvailability = _SvcRspTableTotalAvailability_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 17),
    _SvcRspTableTotalAvailability_Type()
)
svcRspTableTotalAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableTotalAvailability.setStatus("mandatory")
_SvcRspTableNameLastSample_Type = Integer32
_SvcRspTableNameLastSample_Object = MibTableColumn
svcRspTableNameLastSample = _SvcRspTableNameLastSample_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 18),
    _SvcRspTableNameLastSample_Type()
)
svcRspTableNameLastSample.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableNameLastSample.setStatus("mandatory")
_SvcRspTableNameMin_Type = Integer32
_SvcRspTableNameMin_Object = MibTableColumn
svcRspTableNameMin = _SvcRspTableNameMin_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 19),
    _SvcRspTableNameMin_Type()
)
svcRspTableNameMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableNameMin.setStatus("mandatory")
_SvcRspTableNameMax_Type = Integer32
_SvcRspTableNameMax_Object = MibTableColumn
svcRspTableNameMax = _SvcRspTableNameMax_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 20),
    _SvcRspTableNameMax_Type()
)
svcRspTableNameMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableNameMax.setStatus("mandatory")
_SvcRspTableNameMean_Type = Integer32
_SvcRspTableNameMean_Object = MibTableColumn
svcRspTableNameMean = _SvcRspTableNameMean_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 21),
    _SvcRspTableNameMean_Type()
)
svcRspTableNameMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableNameMean.setStatus("mandatory")
_SvcRspTableNameVariance_Type = Integer32
_SvcRspTableNameVariance_Object = MibTableColumn
svcRspTableNameVariance = _SvcRspTableNameVariance_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 22),
    _SvcRspTableNameVariance_Type()
)
svcRspTableNameVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableNameVariance.setStatus("mandatory")
_SvcRspTableConnLastSample_Type = Integer32
_SvcRspTableConnLastSample_Object = MibTableColumn
svcRspTableConnLastSample = _SvcRspTableConnLastSample_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 23),
    _SvcRspTableConnLastSample_Type()
)
svcRspTableConnLastSample.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableConnLastSample.setStatus("mandatory")
_SvcRspTableConnMin_Type = Integer32
_SvcRspTableConnMin_Object = MibTableColumn
svcRspTableConnMin = _SvcRspTableConnMin_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 24),
    _SvcRspTableConnMin_Type()
)
svcRspTableConnMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableConnMin.setStatus("mandatory")
_SvcRspTableConnMax_Type = Integer32
_SvcRspTableConnMax_Object = MibTableColumn
svcRspTableConnMax = _SvcRspTableConnMax_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 25),
    _SvcRspTableConnMax_Type()
)
svcRspTableConnMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableConnMax.setStatus("mandatory")
_SvcRspTableConnMean_Type = Integer32
_SvcRspTableConnMean_Object = MibTableColumn
svcRspTableConnMean = _SvcRspTableConnMean_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 26),
    _SvcRspTableConnMean_Type()
)
svcRspTableConnMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableConnMean.setStatus("mandatory")
_SvcRspTableConnVariance_Type = Integer32
_SvcRspTableConnVariance_Object = MibTableColumn
svcRspTableConnVariance = _SvcRspTableConnVariance_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 27),
    _SvcRspTableConnVariance_Type()
)
svcRspTableConnVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableConnVariance.setStatus("mandatory")
_SvcRspTableTranLastSample_Type = Integer32
_SvcRspTableTranLastSample_Object = MibTableColumn
svcRspTableTranLastSample = _SvcRspTableTranLastSample_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 28),
    _SvcRspTableTranLastSample_Type()
)
svcRspTableTranLastSample.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableTranLastSample.setStatus("mandatory")
_SvcRspTableTranMin_Type = Integer32
_SvcRspTableTranMin_Object = MibTableColumn
svcRspTableTranMin = _SvcRspTableTranMin_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 29),
    _SvcRspTableTranMin_Type()
)
svcRspTableTranMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableTranMin.setStatus("mandatory")
_SvcRspTableTranMax_Type = Integer32
_SvcRspTableTranMax_Object = MibTableColumn
svcRspTableTranMax = _SvcRspTableTranMax_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 30),
    _SvcRspTableTranMax_Type()
)
svcRspTableTranMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableTranMax.setStatus("mandatory")
_SvcRspTableTranMean_Type = Integer32
_SvcRspTableTranMean_Object = MibTableColumn
svcRspTableTranMean = _SvcRspTableTranMean_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 31),
    _SvcRspTableTranMean_Type()
)
svcRspTableTranMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableTranMean.setStatus("mandatory")
_SvcRspTableTranVariance_Type = Integer32
_SvcRspTableTranVariance_Object = MibTableColumn
svcRspTableTranVariance = _SvcRspTableTranVariance_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 32),
    _SvcRspTableTranVariance_Type()
)
svcRspTableTranVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableTranVariance.setStatus("mandatory")
_SvcRspTableBytesInLastSample_Type = Integer32
_SvcRspTableBytesInLastSample_Object = MibTableColumn
svcRspTableBytesInLastSample = _SvcRspTableBytesInLastSample_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 33),
    _SvcRspTableBytesInLastSample_Type()
)
svcRspTableBytesInLastSample.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableBytesInLastSample.setStatus("mandatory")
_SvcRspTableBytesOutLastSample_Type = Integer32
_SvcRspTableBytesOutLastSample_Object = MibTableColumn
svcRspTableBytesOutLastSample = _SvcRspTableBytesOutLastSample_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 34),
    _SvcRspTableBytesOutLastSample_Type()
)
svcRspTableBytesOutLastSample.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableBytesOutLastSample.setStatus("mandatory")
_SvcRspTableTotalBytesIn_Type = Integer32
_SvcRspTableTotalBytesIn_Object = MibTableColumn
svcRspTableTotalBytesIn = _SvcRspTableTotalBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 35),
    _SvcRspTableTotalBytesIn_Type()
)
svcRspTableTotalBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableTotalBytesIn.setStatus("mandatory")
_SvcRspTableTotalBytesOut_Type = Integer32
_SvcRspTableTotalBytesOut_Object = MibTableColumn
svcRspTableTotalBytesOut = _SvcRspTableTotalBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 36),
    _SvcRspTableTotalBytesOut_Type()
)
svcRspTableTotalBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableTotalBytesOut.setStatus("mandatory")
_SvcRspTableThroughput_Type = Integer32
_SvcRspTableThroughput_Object = MibTableColumn
svcRspTableThroughput = _SvcRspTableThroughput_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 37),
    _SvcRspTableThroughput_Type()
)
svcRspTableThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableThroughput.setStatus("mandatory")
_SvcRspTableResults_Type = Integer32
_SvcRspTableResults_Object = MibTableColumn
svcRspTableResults = _SvcRspTableResults_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 38),
    _SvcRspTableResults_Type()
)
svcRspTableResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableResults.setStatus("mandatory")
_SvcRspTableErrorCode_Type = Integer32
_SvcRspTableErrorCode_Object = MibTableColumn
svcRspTableErrorCode = _SvcRspTableErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 39),
    _SvcRspTableErrorCode_Type()
)
svcRspTableErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableErrorCode.setStatus("mandatory")


class _SvcRspTableTOSField_Type(Integer32):
    """Custom type svcRspTableTOSField based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SvcRspTableTOSField_Type.__name__ = "Integer32"
_SvcRspTableTOSField_Object = MibTableColumn
svcRspTableTOSField = _SvcRspTableTOSField_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 40),
    _SvcRspTableTOSField_Type()
)
svcRspTableTOSField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableTOSField.setStatus("mandatory")
_SvcRspTableFlags_Type = Integer32
_SvcRspTableFlags_Object = MibTableColumn
svcRspTableFlags = _SvcRspTableFlags_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 41),
    _SvcRspTableFlags_Type()
)
svcRspTableFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcRspTableFlags.setStatus("mandatory")
_SvcRspTableLimit_Type = Integer32
_SvcRspTableLimit_Object = MibTableColumn
svcRspTableLimit = _SvcRspTableLimit_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 42),
    _SvcRspTableLimit_Type()
)
svcRspTableLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcRspTableLimit.setStatus("mandatory")


class _SvcRspTableUsername_Type(DisplayString):
    """Custom type svcRspTableUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SvcRspTableUsername_Type.__name__ = "DisplayString"
_SvcRspTableUsername_Object = MibTableColumn
svcRspTableUsername = _SvcRspTableUsername_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 43),
    _SvcRspTableUsername_Type()
)
svcRspTableUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcRspTableUsername.setStatus("mandatory")


class _SvcRspTablePassword_Type(DisplayString):
    """Custom type svcRspTablePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SvcRspTablePassword_Type.__name__ = "DisplayString"
_SvcRspTablePassword_Object = MibTableColumn
svcRspTablePassword = _SvcRspTablePassword_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 44),
    _SvcRspTablePassword_Type()
)
svcRspTablePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcRspTablePassword.setStatus("mandatory")


class _SvcRspTableDest_Type(DisplayString):
    """Custom type svcRspTableDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SvcRspTableDest_Type.__name__ = "DisplayString"
_SvcRspTableDest_Object = MibTableColumn
svcRspTableDest = _SvcRspTableDest_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 45),
    _SvcRspTableDest_Type()
)
svcRspTableDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcRspTableDest.setStatus("mandatory")
_SvcRspTableTotalErrors_Type = Counter32
_SvcRspTableTotalErrors_Object = MibTableColumn
svcRspTableTotalErrors = _SvcRspTableTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 46),
    _SvcRspTableTotalErrors_Type()
)
svcRspTableTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableTotalErrors.setStatus("mandatory")
_SvcRspTableSamplesInWindow_Type = Integer32
_SvcRspTableSamplesInWindow_Object = MibTableColumn
svcRspTableSamplesInWindow = _SvcRspTableSamplesInWindow_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 47),
    _SvcRspTableSamplesInWindow_Type()
)
svcRspTableSamplesInWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableSamplesInWindow.setStatus("mandatory")
_SvcRspTableSuccessesInWindow_Type = Integer32
_SvcRspTableSuccessesInWindow_Object = MibTableColumn
svcRspTableSuccessesInWindow = _SvcRspTableSuccessesInWindow_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 10, 1, 48),
    _SvcRspTableSuccessesInWindow_Type()
)
svcRspTableSuccessesInWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspTableSuccessesInWindow.setStatus("mandatory")


class _SvcRspUnusedIndex_Type(Integer32):
    """Custom type svcRspUnusedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SvcRspUnusedIndex_Type.__name__ = "Integer32"
_SvcRspUnusedIndex_Object = MibScalar
svcRspUnusedIndex = _SvcRspUnusedIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 11),
    _SvcRspUnusedIndex_Type()
)
svcRspUnusedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspUnusedIndex.setStatus("mandatory")
_SvcRspMatchDescr_Type = DisplayString
_SvcRspMatchDescr_Object = MibScalar
svcRspMatchDescr = _SvcRspMatchDescr_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 12),
    _SvcRspMatchDescr_Type()
)
svcRspMatchDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcRspMatchDescr.setStatus("mandatory")


class _SvcRspMatchIndex_Type(Integer32):
    """Custom type svcRspMatchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SvcRspMatchIndex_Type.__name__ = "Integer32"
_SvcRspMatchIndex_Object = MibScalar
svcRspMatchIndex = _SvcRspMatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 13),
    _SvcRspMatchIndex_Type()
)
svcRspMatchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspMatchIndex.setStatus("mandatory")
_SvcRspNumTests_Type = Integer32
_SvcRspNumTests_Object = MibScalar
svcRspNumTests = _SvcRspNumTests_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 14),
    _SvcRspNumTests_Type()
)
svcRspNumTests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspNumTests.setStatus("mandatory")
_SvcRspMaxThreads_Type = Integer32
_SvcRspMaxThreads_Object = MibScalar
svcRspMaxThreads = _SvcRspMaxThreads_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 15),
    _SvcRspMaxThreads_Type()
)
svcRspMaxThreads.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svcRspMaxThreads.setStatus("mandatory")
_SvcRspSecurityFlags_Type = Integer32
_SvcRspSecurityFlags_Object = MibScalar
svcRspSecurityFlags = _SvcRspSecurityFlags_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 6, 16),
    _SvcRspSecurityFlags_Type()
)
svcRspSecurityFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcRspSecurityFlags.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EMPIRE-SVCRSP",
    **{"empire": empire,
       "applications": applications,
       "svcRsp": svcRsp,
       "svcRspVersion": svcRspVersion,
       "svcRspPID": svcRspPID,
       "svcRspModMode": svcRspModMode,
       "svcRspTable": svcRspTable,
       "svcRspTableEntry": svcRspTableEntry,
       "svcRspTableIndex": svcRspTableIndex,
       "svcRspTableDescr": svcRspTableDescr,
       "svcRspTableSvc": svcRspTableSvc,
       "svcRspTableArgs": svcRspTableArgs,
       "svcRspTableInterval": svcRspTableInterval,
       "svcRspTableSamplesPerInterval": svcRspTableSamplesPerInterval,
       "svcRspTableTimeout": svcRspTableTimeout,
       "svcRspTableStatsWindow": svcRspTableStatsWindow,
       "svcRspTableStatus": svcRspTableStatus,
       "svcRspTableLastUpdate": svcRspTableLastUpdate,
       "svcRspTableNumSamples": svcRspTableNumSamples,
       "svcRspTableTotalLastSample": svcRspTableTotalLastSample,
       "svcRspTableTotalMin": svcRspTableTotalMin,
       "svcRspTableTotalMax": svcRspTableTotalMax,
       "svcRspTableTotalMean": svcRspTableTotalMean,
       "svcRspTableTotalVariance": svcRspTableTotalVariance,
       "svcRspTableTotalAvailability": svcRspTableTotalAvailability,
       "svcRspTableNameLastSample": svcRspTableNameLastSample,
       "svcRspTableNameMin": svcRspTableNameMin,
       "svcRspTableNameMax": svcRspTableNameMax,
       "svcRspTableNameMean": svcRspTableNameMean,
       "svcRspTableNameVariance": svcRspTableNameVariance,
       "svcRspTableConnLastSample": svcRspTableConnLastSample,
       "svcRspTableConnMin": svcRspTableConnMin,
       "svcRspTableConnMax": svcRspTableConnMax,
       "svcRspTableConnMean": svcRspTableConnMean,
       "svcRspTableConnVariance": svcRspTableConnVariance,
       "svcRspTableTranLastSample": svcRspTableTranLastSample,
       "svcRspTableTranMin": svcRspTableTranMin,
       "svcRspTableTranMax": svcRspTableTranMax,
       "svcRspTableTranMean": svcRspTableTranMean,
       "svcRspTableTranVariance": svcRspTableTranVariance,
       "svcRspTableBytesInLastSample": svcRspTableBytesInLastSample,
       "svcRspTableBytesOutLastSample": svcRspTableBytesOutLastSample,
       "svcRspTableTotalBytesIn": svcRspTableTotalBytesIn,
       "svcRspTableTotalBytesOut": svcRspTableTotalBytesOut,
       "svcRspTableThroughput": svcRspTableThroughput,
       "svcRspTableResults": svcRspTableResults,
       "svcRspTableErrorCode": svcRspTableErrorCode,
       "svcRspTableTOSField": svcRspTableTOSField,
       "svcRspTableFlags": svcRspTableFlags,
       "svcRspTableLimit": svcRspTableLimit,
       "svcRspTableUsername": svcRspTableUsername,
       "svcRspTablePassword": svcRspTablePassword,
       "svcRspTableDest": svcRspTableDest,
       "svcRspTableTotalErrors": svcRspTableTotalErrors,
       "svcRspTableSamplesInWindow": svcRspTableSamplesInWindow,
       "svcRspTableSuccessesInWindow": svcRspTableSuccessesInWindow,
       "svcRspUnusedIndex": svcRspUnusedIndex,
       "svcRspMatchDescr": svcRspMatchDescr,
       "svcRspMatchIndex": svcRspMatchIndex,
       "svcRspNumTests": svcRspNumTests,
       "svcRspMaxThreads": svcRspMaxThreads,
       "svcRspSecurityFlags": svcRspSecurityFlags}
)
