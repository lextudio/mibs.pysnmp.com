# SNMP MIB module (JUNIPER-MOBILITY-CHARGING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-MOBILITY-CHARGING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:54 2024
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

(jnxMobileGatewayPgwGgsn,) = mibBuilder.importSymbols(
    "JUNIPER-MBG-SMI",
    "jnxMobileGatewayPgwGgsn")

(jnxMbgGwIndex,
 jnxMbgGwName) = mibBuilder.importSymbols(
    "JUNIPER-MOBILE-GATEWAYS",
    "jnxMbgGwIndex",
    "jnxMbgGwName")

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

jnxMbgPgwChargingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3)
)
jnxMbgPgwChargingMib.setRevisions(
        ("2010-06-15 14:30",
         "2011-10-10 14:30",
         "2012-03-16 14:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxMbgPgwCgNotifications_ObjectIdentity = ObjectIdentity
jnxMbgPgwCgNotifications = _JnxMbgPgwCgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 0)
)
_JnxMbgPgwChargingObjects_ObjectIdentity = ObjectIdentity
jnxMbgPgwChargingObjects = _JnxMbgPgwChargingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1)
)
_JnxMbgPgwCgLcStorageStats_ObjectIdentity = ObjectIdentity
jnxMbgPgwCgLcStorageStats = _JnxMbgPgwCgLcStorageStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 1)
)
_JnxMbgPgwCgFilesOnLcStorage_Type = Counter64
_JnxMbgPgwCgFilesOnLcStorage_Object = MibScalar
jnxMbgPgwCgFilesOnLcStorage = _JnxMbgPgwCgFilesOnLcStorage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 1, 1),
    _JnxMbgPgwCgFilesOnLcStorage_Type()
)
jnxMbgPgwCgFilesOnLcStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgFilesOnLcStorage.setStatus("obsolete")
_JnxMbgPgwCgLcStorageAvailSpace_Type = Counter64
_JnxMbgPgwCgLcStorageAvailSpace_Object = MibScalar
jnxMbgPgwCgLcStorageAvailSpace = _JnxMbgPgwCgLcStorageAvailSpace_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 1, 2),
    _JnxMbgPgwCgLcStorageAvailSpace_Type()
)
jnxMbgPgwCgLcStorageAvailSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgLcStorageAvailSpace.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxMbgPgwCgLcStorageAvailSpace.setUnits("MBytes")
_JnxMbgPgwCgCgfGroupsStatsTable_Object = MibTable
jnxMbgPgwCgCgfGroupsStatsTable = _JnxMbgPgwCgCgfGroupsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfGroupsStatsTable.setStatus("current")
_JnxMbgPgwCgCgfGroupStatsEntry_Object = MibTableRow
jnxMbgPgwCgCgfGroupStatsEntry = _JnxMbgPgwCgCgfGroupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 2, 1)
)
jnxMbgPgwCgCgfGroupStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgCgfGrpProfName"),
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfGroupStatsEntry.setStatus("obsolete")


class _JnxMbgPgwCgCgfGrpProfName_Type(DisplayString):
    """Custom type jnxMbgPgwCgCgfGrpProfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_JnxMbgPgwCgCgfGrpProfName_Type.__name__ = "DisplayString"
_JnxMbgPgwCgCgfGrpProfName_Object = MibTableColumn
jnxMbgPgwCgCgfGrpProfName = _JnxMbgPgwCgCgfGrpProfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 2, 1, 1),
    _JnxMbgPgwCgCgfGrpProfName_Type()
)
jnxMbgPgwCgCgfGrpProfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfGrpProfName.setStatus("current")
_JnxMbgPgwCgCgfGrpDRTReqTx_Type = Counter32
_JnxMbgPgwCgCgfGrpDRTReqTx_Object = MibTableColumn
jnxMbgPgwCgCgfGrpDRTReqTx = _JnxMbgPgwCgCgfGrpDRTReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 2, 1, 2),
    _JnxMbgPgwCgCgfGrpDRTReqTx_Type()
)
jnxMbgPgwCgCgfGrpDRTReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfGrpDRTReqTx.setStatus("current")
_JnxMbgPgwCgCgfGrpDRTReqRx_Type = Counter32
_JnxMbgPgwCgCgfGrpDRTReqRx_Object = MibTableColumn
jnxMbgPgwCgCgfGrpDRTReqRx = _JnxMbgPgwCgCgfGrpDRTReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 2, 1, 3),
    _JnxMbgPgwCgCgfGrpDRTReqRx_Type()
)
jnxMbgPgwCgCgfGrpDRTReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfGrpDRTReqRx.setStatus("current")
_JnxMbgPgwCgCgfGrpDRTReqTmout_Type = Counter32
_JnxMbgPgwCgCgfGrpDRTReqTmout_Object = MibTableColumn
jnxMbgPgwCgCgfGrpDRTReqTmout = _JnxMbgPgwCgCgfGrpDRTReqTmout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 2, 1, 4),
    _JnxMbgPgwCgCgfGrpDRTReqTmout_Type()
)
jnxMbgPgwCgCgfGrpDRTReqTmout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfGrpDRTReqTmout.setStatus("current")
_JnxMbgPgwCgCgfGrpDRTSucRspRx_Type = Counter32
_JnxMbgPgwCgCgfGrpDRTSucRspRx_Object = MibTableColumn
jnxMbgPgwCgCgfGrpDRTSucRspRx = _JnxMbgPgwCgCgfGrpDRTSucRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 2, 1, 5),
    _JnxMbgPgwCgCgfGrpDRTSucRspRx_Type()
)
jnxMbgPgwCgCgfGrpDRTSucRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfGrpDRTSucRspRx.setStatus("current")
_JnxMbgPgwCgCgfGrpDRTErrRspRx_Type = Counter32
_JnxMbgPgwCgCgfGrpDRTErrRspRx_Object = MibTableColumn
jnxMbgPgwCgCgfGrpDRTErrRspRx = _JnxMbgPgwCgCgfGrpDRTErrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 2, 1, 6),
    _JnxMbgPgwCgCgfGrpDRTErrRspRx_Type()
)
jnxMbgPgwCgCgfGrpDRTErrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfGrpDRTErrRspRx.setStatus("current")
_JnxMbgPgwCgCgfGrpRediReqRx_Type = Counter32
_JnxMbgPgwCgCgfGrpRediReqRx_Object = MibTableColumn
jnxMbgPgwCgCgfGrpRediReqRx = _JnxMbgPgwCgCgfGrpRediReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 2, 1, 7),
    _JnxMbgPgwCgCgfGrpRediReqRx_Type()
)
jnxMbgPgwCgCgfGrpRediReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfGrpRediReqRx.setStatus("current")
_JnxMbgPgwCgCgfGrpRediRspTx_Type = Counter32
_JnxMbgPgwCgCgfGrpRediRspTx_Object = MibTableColumn
jnxMbgPgwCgCgfGrpRediRspTx = _JnxMbgPgwCgCgfGrpRediRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 2, 1, 8),
    _JnxMbgPgwCgCgfGrpRediRspTx_Type()
)
jnxMbgPgwCgCgfGrpRediRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfGrpRediRspTx.setStatus("current")
_JnxMbgPgwCgCgfGrpSwitchovers_Type = Counter32
_JnxMbgPgwCgCgfGrpSwitchovers_Object = MibTableColumn
jnxMbgPgwCgCgfGrpSwitchovers = _JnxMbgPgwCgCgfGrpSwitchovers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 2, 1, 9),
    _JnxMbgPgwCgCgfGrpSwitchovers_Type()
)
jnxMbgPgwCgCgfGrpSwitchovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfGrpSwitchovers.setStatus("current")
_JnxMbgPgwCgCgfGrpBatchReqTx_Type = Counter32
_JnxMbgPgwCgCgfGrpBatchReqTx_Object = MibTableColumn
jnxMbgPgwCgCgfGrpBatchReqTx = _JnxMbgPgwCgCgfGrpBatchReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 2, 1, 10),
    _JnxMbgPgwCgCgfGrpBatchReqTx_Type()
)
jnxMbgPgwCgCgfGrpBatchReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfGrpBatchReqTx.setStatus("current")
_JnxMbgPgwCgCgfGrpBatchRspErrors_Type = Counter32
_JnxMbgPgwCgCgfGrpBatchRspErrors_Object = MibTableColumn
jnxMbgPgwCgCgfGrpBatchRspErrors = _JnxMbgPgwCgCgfGrpBatchRspErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 2, 1, 11),
    _JnxMbgPgwCgCgfGrpBatchRspErrors_Type()
)
jnxMbgPgwCgCgfGrpBatchRspErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfGrpBatchRspErrors.setStatus("current")
_JnxMbgPgwCgCgfGrpBatchCDRsTx_Type = Counter32
_JnxMbgPgwCgCgfGrpBatchCDRsTx_Object = MibTableColumn
jnxMbgPgwCgCgfGrpBatchCDRsTx = _JnxMbgPgwCgCgfGrpBatchCDRsTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 2, 1, 12),
    _JnxMbgPgwCgCgfGrpBatchCDRsTx_Type()
)
jnxMbgPgwCgCgfGrpBatchCDRsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfGrpBatchCDRsTx.setStatus("current")
_JnxMbgPgwCgCgfGroupTotalWFA_Type = Counter32
_JnxMbgPgwCgCgfGroupTotalWFA_Object = MibTableColumn
jnxMbgPgwCgCgfGroupTotalWFA = _JnxMbgPgwCgCgfGroupTotalWFA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 2, 1, 13),
    _JnxMbgPgwCgCgfGroupTotalWFA_Type()
)
jnxMbgPgwCgCgfGroupTotalWFA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfGroupTotalWFA.setStatus("current")
_JnxMbgPgwCgNotificationVars_ObjectIdentity = ObjectIdentity
jnxMbgPgwCgNotificationVars = _JnxMbgPgwCgNotificationVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 3)
)


class _JnxMbgPgwCgServerName_Type(DisplayString):
    """Custom type jnxMbgPgwCgServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_JnxMbgPgwCgServerName_Type.__name__ = "DisplayString"
_JnxMbgPgwCgServerName_Object = MibScalar
jnxMbgPgwCgServerName = _JnxMbgPgwCgServerName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 3, 1),
    _JnxMbgPgwCgServerName_Type()
)
jnxMbgPgwCgServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwCgServerName.setStatus("current")


class _JnxMbgPgwCgServicePicName_Type(DisplayString):
    """Custom type jnxMbgPgwCgServicePicName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_JnxMbgPgwCgServicePicName_Type.__name__ = "DisplayString"
_JnxMbgPgwCgServicePicName_Object = MibScalar
jnxMbgPgwCgServicePicName = _JnxMbgPgwCgServicePicName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 3, 2),
    _JnxMbgPgwCgServicePicName_Type()
)
jnxMbgPgwCgServicePicName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwCgServicePicName.setStatus("current")


class _JnxMbgPgwCgCDRDest_Type(Integer32):
    """Custom type jnxMbgPgwCgCDRDest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cdrbackup", 2),
          ("cdrcgf", 1),
          ("cdrnobackup", 3))
    )


_JnxMbgPgwCgCDRDest_Type.__name__ = "Integer32"
_JnxMbgPgwCgCDRDest_Object = MibScalar
jnxMbgPgwCgCDRDest = _JnxMbgPgwCgCDRDest_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 3, 3),
    _JnxMbgPgwCgCDRDest_Type()
)
jnxMbgPgwCgCDRDest.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCDRDest.setStatus("current")
_JnxMbgPgwCgActiveCgfIpAddr_Type = IpAddress
_JnxMbgPgwCgActiveCgfIpAddr_Object = MibScalar
jnxMbgPgwCgActiveCgfIpAddr = _JnxMbgPgwCgActiveCgfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 3, 4),
    _JnxMbgPgwCgActiveCgfIpAddr_Type()
)
jnxMbgPgwCgActiveCgfIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwCgActiveCgfIpAddr.setStatus("current")


class _JnxMbgPgwCgTSPName_Type(DisplayString):
    """Custom type jnxMbgPgwCgTSPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_JnxMbgPgwCgTSPName_Type.__name__ = "DisplayString"
_JnxMbgPgwCgTSPName_Object = MibScalar
jnxMbgPgwCgTSPName = _JnxMbgPgwCgTSPName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 3, 5),
    _JnxMbgPgwCgTSPName_Type()
)
jnxMbgPgwCgTSPName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwCgTSPName.setStatus("deprecated")


class _JnxMbgPgwCgMemLimit_Type(Integer32):
    """Custom type jnxMbgPgwCgMemLimit based on Integer32"""
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
        *(("memfulldisconnectexistnew", 3),
          ("memfulldisconnectexistnewrslvd", 4),
          ("memfulldisconnectnew", 1),
          ("memfulldisconnectnewrslvd", 2))
    )


_JnxMbgPgwCgMemLimit_Type.__name__ = "Integer32"
_JnxMbgPgwCgMemLimit_Object = MibScalar
jnxMbgPgwCgMemLimit = _JnxMbgPgwCgMemLimit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 3, 6),
    _JnxMbgPgwCgMemLimit_Type()
)
jnxMbgPgwCgMemLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwCgMemLimit.setStatus("current")


class _JnxMbgPgwCgLcsSpace_Type(Integer32):
    """Custom type jnxMbgPgwCgLcsSpace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localstoragememlevel1", 1),
          ("localstoragememlevel2", 2),
          ("localstoragememlevel3", 3))
    )


_JnxMbgPgwCgLcsSpace_Type.__name__ = "Integer32"
_JnxMbgPgwCgLcsSpace_Object = MibScalar
jnxMbgPgwCgLcsSpace = _JnxMbgPgwCgLcsSpace_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 3, 7),
    _JnxMbgPgwCgLcsSpace_Type()
)
jnxMbgPgwCgLcsSpace.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwCgLcsSpace.setStatus("current")
_JnxMbgPgwCgLcsUtil_Type = Gauge32
_JnxMbgPgwCgLcsUtil_Object = MibScalar
jnxMbgPgwCgLcsUtil = _JnxMbgPgwCgLcsUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 3, 8),
    _JnxMbgPgwCgLcsUtil_Type()
)
jnxMbgPgwCgLcsUtil.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwCgLcsUtil.setStatus("current")
if mibBuilder.loadTexts:
    jnxMbgPgwCgLcsUtil.setUnits("percent")


class _JnxMbgPgwCgAlarmStatus_Type(Integer32):
    """Custom type jnxMbgPgwCgAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 2),
          ("raised", 1))
    )


_JnxMbgPgwCgAlarmStatus_Type.__name__ = "Integer32"
_JnxMbgPgwCgAlarmStatus_Object = MibScalar
jnxMbgPgwCgAlarmStatus = _JnxMbgPgwCgAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 3, 9),
    _JnxMbgPgwCgAlarmStatus_Type()
)
jnxMbgPgwCgAlarmStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwCgAlarmStatus.setStatus("current")
_JnxMbgPgwCgProfileName_Type = DisplayString
_JnxMbgPgwCgProfileName_Object = MibScalar
jnxMbgPgwCgProfileName = _JnxMbgPgwCgProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 3, 10),
    _JnxMbgPgwCgProfileName_Type()
)
jnxMbgPgwCgProfileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwCgProfileName.setStatus("deprecated")
_JnxMbgPgwCgPrevMMState_Type = DisplayString
_JnxMbgPgwCgPrevMMState_Object = MibScalar
jnxMbgPgwCgPrevMMState = _JnxMbgPgwCgPrevMMState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 3, 11),
    _JnxMbgPgwCgPrevMMState_Type()
)
jnxMbgPgwCgPrevMMState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwCgPrevMMState.setStatus("current")
_JnxMbgPgwCgNewMMState_Type = DisplayString
_JnxMbgPgwCgNewMMState_Object = MibScalar
jnxMbgPgwCgNewMMState = _JnxMbgPgwCgNewMMState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 3, 12),
    _JnxMbgPgwCgNewMMState_Type()
)
jnxMbgPgwCgNewMMState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwCgNewMMState.setStatus("current")
_JnxMbgPgwCgTProfileName_Type = DisplayString
_JnxMbgPgwCgTProfileName_Object = MibScalar
jnxMbgPgwCgTProfileName = _JnxMbgPgwCgTProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 3, 13),
    _JnxMbgPgwCgTProfileName_Type()
)
jnxMbgPgwCgTProfileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwCgTProfileName.setStatus("deprecated")
_JnxMbgPgwCgTPrevMMState_Type = DisplayString
_JnxMbgPgwCgTPrevMMState_Object = MibScalar
jnxMbgPgwCgTPrevMMState = _JnxMbgPgwCgTPrevMMState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 3, 14),
    _JnxMbgPgwCgTPrevMMState_Type()
)
jnxMbgPgwCgTPrevMMState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwCgTPrevMMState.setStatus("deprecated")
_JnxMbgPgwCgTNewMMState_Type = DisplayString
_JnxMbgPgwCgTNewMMState_Object = MibScalar
jnxMbgPgwCgTNewMMState = _JnxMbgPgwCgTNewMMState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 3, 15),
    _JnxMbgPgwCgTNewMMState_Type()
)
jnxMbgPgwCgTNewMMState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwCgTNewMMState.setStatus("deprecated")
_JnxMbgPgwCgPeerProfName_Type = DisplayString
_JnxMbgPgwCgPeerProfName_Object = MibScalar
jnxMbgPgwCgPeerProfName = _JnxMbgPgwCgPeerProfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 3, 16),
    _JnxMbgPgwCgPeerProfName_Type()
)
jnxMbgPgwCgPeerProfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwCgPeerProfName.setStatus("current")
_JnxMbgPgwCgCgfStatsTable_Object = MibTable
jnxMbgPgwCgCgfStatsTable = _JnxMbgPgwCgCgfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfStatsTable.setStatus("current")
_JnxMbgPgwCgCgfStatsEntry_Object = MibTableRow
jnxMbgPgwCgCgfStatsEntry = _JnxMbgPgwCgCgfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1)
)
jnxMbgPgwCgCgfStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgCgfIndex"),
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfStatsEntry.setStatus("obsolete")


class _JnxMbgPgwCgCgfProfName_Type(DisplayString):
    """Custom type jnxMbgPgwCgCgfProfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_JnxMbgPgwCgCgfProfName_Type.__name__ = "DisplayString"
_JnxMbgPgwCgCgfProfName_Object = MibTableColumn
jnxMbgPgwCgCgfProfName = _JnxMbgPgwCgCgfProfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 1),
    _JnxMbgPgwCgCgfProfName_Type()
)
jnxMbgPgwCgCgfProfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfProfName.setStatus("current")


class _JnxMbgPgwCgCgfIndex_Type(Integer32):
    """Custom type jnxMbgPgwCgCgfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_JnxMbgPgwCgCgfIndex_Type.__name__ = "Integer32"
_JnxMbgPgwCgCgfIndex_Object = MibTableColumn
jnxMbgPgwCgCgfIndex = _JnxMbgPgwCgCgfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 2),
    _JnxMbgPgwCgCgfIndex_Type()
)
jnxMbgPgwCgCgfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfIndex.setStatus("current")
_JnxMbgPgwCgCgfIpAddress_Type = IpAddress
_JnxMbgPgwCgCgfIpAddress_Object = MibTableColumn
jnxMbgPgwCgCgfIpAddress = _JnxMbgPgwCgCgfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 3),
    _JnxMbgPgwCgCgfIpAddress_Type()
)
jnxMbgPgwCgCgfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfIpAddress.setStatus("current")


class _JnxMbgPgwCgCgfStatus_Type(Integer32):
    """Custom type jnxMbgPgwCgCgfStatus based on Integer32"""
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


_JnxMbgPgwCgCgfStatus_Type.__name__ = "Integer32"
_JnxMbgPgwCgCgfStatus_Object = MibTableColumn
jnxMbgPgwCgCgfStatus = _JnxMbgPgwCgCgfStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 4),
    _JnxMbgPgwCgCgfStatus_Type()
)
jnxMbgPgwCgCgfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfStatus.setStatus("current")
_JnxMbgPgwCgCgfUpDuration_Type = Counter64
_JnxMbgPgwCgCgfUpDuration_Object = MibTableColumn
jnxMbgPgwCgCgfUpDuration = _JnxMbgPgwCgCgfUpDuration_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 5),
    _JnxMbgPgwCgCgfUpDuration_Type()
)
jnxMbgPgwCgCgfUpDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfUpDuration.setStatus("current")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfUpDuration.setUnits("minutes")
_JnxMbgPgwCgCgfDownDuration_Type = Counter64
_JnxMbgPgwCgCgfDownDuration_Object = MibTableColumn
jnxMbgPgwCgCgfDownDuration = _JnxMbgPgwCgCgfDownDuration_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 6),
    _JnxMbgPgwCgCgfDownDuration_Type()
)
jnxMbgPgwCgCgfDownDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfDownDuration.setStatus("current")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfDownDuration.setUnits("minutes")
_JnxMbgPgwCgCgfEchoReqTx_Type = Counter64
_JnxMbgPgwCgCgfEchoReqTx_Object = MibTableColumn
jnxMbgPgwCgCgfEchoReqTx = _JnxMbgPgwCgCgfEchoReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 7),
    _JnxMbgPgwCgCgfEchoReqTx_Type()
)
jnxMbgPgwCgCgfEchoReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfEchoReqTx.setStatus("current")
_JnxMbgPgwCgCgfEchoReqRx_Type = Counter64
_JnxMbgPgwCgCgfEchoReqRx_Object = MibTableColumn
jnxMbgPgwCgCgfEchoReqRx = _JnxMbgPgwCgCgfEchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 8),
    _JnxMbgPgwCgCgfEchoReqRx_Type()
)
jnxMbgPgwCgCgfEchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfEchoReqRx.setStatus("current")
_JnxMbgPgwCgCgfEchoReqTmout_Type = Counter64
_JnxMbgPgwCgCgfEchoReqTmout_Object = MibTableColumn
jnxMbgPgwCgCgfEchoReqTmout = _JnxMbgPgwCgCgfEchoReqTmout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 9),
    _JnxMbgPgwCgCgfEchoReqTmout_Type()
)
jnxMbgPgwCgCgfEchoReqTmout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfEchoReqTmout.setStatus("current")
_JnxMbgPgwCgCgfEchoRespTx_Type = Counter64
_JnxMbgPgwCgCgfEchoRespTx_Object = MibTableColumn
jnxMbgPgwCgCgfEchoRespTx = _JnxMbgPgwCgCgfEchoRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 10),
    _JnxMbgPgwCgCgfEchoRespTx_Type()
)
jnxMbgPgwCgCgfEchoRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfEchoRespTx.setStatus("current")
_JnxMbgPgwCgCgfEchoRespRx_Type = Counter64
_JnxMbgPgwCgCgfEchoRespRx_Object = MibTableColumn
jnxMbgPgwCgCgfEchoRespRx = _JnxMbgPgwCgCgfEchoRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 11),
    _JnxMbgPgwCgCgfEchoRespRx_Type()
)
jnxMbgPgwCgCgfEchoRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfEchoRespRx.setStatus("current")
_JnxMbgPgwCgCgfVerUnsuppTx_Type = Counter64
_JnxMbgPgwCgCgfVerUnsuppTx_Object = MibTableColumn
jnxMbgPgwCgCgfVerUnsuppTx = _JnxMbgPgwCgCgfVerUnsuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 12),
    _JnxMbgPgwCgCgfVerUnsuppTx_Type()
)
jnxMbgPgwCgCgfVerUnsuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfVerUnsuppTx.setStatus("current")
_JnxMbgPgwCgCgfVerUnsuppRx_Type = Counter64
_JnxMbgPgwCgCgfVerUnsuppRx_Object = MibTableColumn
jnxMbgPgwCgCgfVerUnsuppRx = _JnxMbgPgwCgCgfVerUnsuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 13),
    _JnxMbgPgwCgCgfVerUnsuppRx_Type()
)
jnxMbgPgwCgCgfVerUnsuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfVerUnsuppRx.setStatus("current")
_JnxMbgPgwCgCgfNodeAliveReqTx_Type = Counter64
_JnxMbgPgwCgCgfNodeAliveReqTx_Object = MibTableColumn
jnxMbgPgwCgCgfNodeAliveReqTx = _JnxMbgPgwCgCgfNodeAliveReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 14),
    _JnxMbgPgwCgCgfNodeAliveReqTx_Type()
)
jnxMbgPgwCgCgfNodeAliveReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfNodeAliveReqTx.setStatus("current")
_JnxMbgPgwCgCgfNodeAliveReqRx_Type = Counter64
_JnxMbgPgwCgCgfNodeAliveReqRx_Object = MibTableColumn
jnxMbgPgwCgCgfNodeAliveReqRx = _JnxMbgPgwCgCgfNodeAliveReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 15),
    _JnxMbgPgwCgCgfNodeAliveReqRx_Type()
)
jnxMbgPgwCgCgfNodeAliveReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfNodeAliveReqRx.setStatus("current")
_JnxMbgPgwCgCgfNodeAliveReqTmout_Type = Counter64
_JnxMbgPgwCgCgfNodeAliveReqTmout_Object = MibTableColumn
jnxMbgPgwCgCgfNodeAliveReqTmout = _JnxMbgPgwCgCgfNodeAliveReqTmout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 16),
    _JnxMbgPgwCgCgfNodeAliveReqTmout_Type()
)
jnxMbgPgwCgCgfNodeAliveReqTmout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfNodeAliveReqTmout.setStatus("current")
_JnxMbgPgwCgCgfNodeAliveRespTx_Type = Counter64
_JnxMbgPgwCgCgfNodeAliveRespTx_Object = MibTableColumn
jnxMbgPgwCgCgfNodeAliveRespTx = _JnxMbgPgwCgCgfNodeAliveRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 17),
    _JnxMbgPgwCgCgfNodeAliveRespTx_Type()
)
jnxMbgPgwCgCgfNodeAliveRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfNodeAliveRespTx.setStatus("current")
_JnxMbgPgwCgCgfNodeAliveRespRx_Type = Counter64
_JnxMbgPgwCgCgfNodeAliveRespRx_Object = MibTableColumn
jnxMbgPgwCgCgfNodeAliveRespRx = _JnxMbgPgwCgCgfNodeAliveRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 18),
    _JnxMbgPgwCgCgfNodeAliveRespRx_Type()
)
jnxMbgPgwCgCgfNodeAliveRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfNodeAliveRespRx.setStatus("current")
_JnxMbgPgwCgCgfRedirectReqRx_Type = Counter64
_JnxMbgPgwCgCgfRedirectReqRx_Object = MibTableColumn
jnxMbgPgwCgCgfRedirectReqRx = _JnxMbgPgwCgCgfRedirectReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 19),
    _JnxMbgPgwCgCgfRedirectReqRx_Type()
)
jnxMbgPgwCgCgfRedirectReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfRedirectReqRx.setStatus("current")
_JnxMbgPgwCgCgfRedirectRespTx_Type = Counter64
_JnxMbgPgwCgCgfRedirectRespTx_Object = MibTableColumn
jnxMbgPgwCgCgfRedirectRespTx = _JnxMbgPgwCgCgfRedirectRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 20),
    _JnxMbgPgwCgCgfRedirectRespTx_Type()
)
jnxMbgPgwCgCgfRedirectRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfRedirectRespTx.setStatus("current")
_JnxMbgPgwCgCgfDRTReqTx_Type = Counter64
_JnxMbgPgwCgCgfDRTReqTx_Object = MibTableColumn
jnxMbgPgwCgCgfDRTReqTx = _JnxMbgPgwCgCgfDRTReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 21),
    _JnxMbgPgwCgCgfDRTReqTx_Type()
)
jnxMbgPgwCgCgfDRTReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfDRTReqTx.setStatus("current")
_JnxMbgPgwCgCgfDRTReqTmout_Type = Counter64
_JnxMbgPgwCgCgfDRTReqTmout_Object = MibTableColumn
jnxMbgPgwCgCgfDRTReqTmout = _JnxMbgPgwCgCgfDRTReqTmout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 22),
    _JnxMbgPgwCgCgfDRTReqTmout_Type()
)
jnxMbgPgwCgCgfDRTReqTmout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfDRTReqTmout.setStatus("current")
_JnxMbgPgwCgCgfDRTSuccRespRx_Type = Counter64
_JnxMbgPgwCgCgfDRTSuccRespRx_Object = MibTableColumn
jnxMbgPgwCgCgfDRTSuccRespRx = _JnxMbgPgwCgCgfDRTSuccRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 23),
    _JnxMbgPgwCgCgfDRTSuccRespRx_Type()
)
jnxMbgPgwCgCgfDRTSuccRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfDRTSuccRespRx.setStatus("current")
_JnxMbgPgwCgCgfDRTErrRespRx_Type = Counter64
_JnxMbgPgwCgCgfDRTErrRespRx_Object = MibTableColumn
jnxMbgPgwCgCgfDRTErrRespRx = _JnxMbgPgwCgCgfDRTErrRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 24),
    _JnxMbgPgwCgCgfDRTErrRespRx_Type()
)
jnxMbgPgwCgCgfDRTErrRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfDRTErrRespRx.setStatus("current")
_JnxMbgPgwCgCgfCdrTx_Type = Counter64
_JnxMbgPgwCgCgfCdrTx_Object = MibTableColumn
jnxMbgPgwCgCgfCdrTx = _JnxMbgPgwCgCgfCdrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 25),
    _JnxMbgPgwCgCgfCdrTx_Type()
)
jnxMbgPgwCgCgfCdrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfCdrTx.setStatus("current")
_JnxMbgPgwCgCgfDRTRTTMean_Type = Counter64
_JnxMbgPgwCgCgfDRTRTTMean_Object = MibTableColumn
jnxMbgPgwCgCgfDRTRTTMean = _JnxMbgPgwCgCgfDRTRTTMean_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 26),
    _JnxMbgPgwCgCgfDRTRTTMean_Type()
)
jnxMbgPgwCgCgfDRTRTTMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfDRTRTTMean.setStatus("current")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfDRTRTTMean.setUnits("seconds")
_JnxMbgPgwCgCgfDRTRTTMin_Type = Counter64
_JnxMbgPgwCgCgfDRTRTTMin_Object = MibTableColumn
jnxMbgPgwCgCgfDRTRTTMin = _JnxMbgPgwCgCgfDRTRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 27),
    _JnxMbgPgwCgCgfDRTRTTMin_Type()
)
jnxMbgPgwCgCgfDRTRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfDRTRTTMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfDRTRTTMin.setUnits("seconds")
_JnxMbgPgwCgCgfDRTRTTMax_Type = Counter64
_JnxMbgPgwCgCgfDRTRTTMax_Object = MibTableColumn
jnxMbgPgwCgCgfDRTRTTMax = _JnxMbgPgwCgCgfDRTRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 28),
    _JnxMbgPgwCgCgfDRTRTTMax_Type()
)
jnxMbgPgwCgCgfDRTRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfDRTRTTMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfDRTRTTMax.setUnits("seconds")
_JnxMbgPgwCgCgfTransToDownState_Type = Counter64
_JnxMbgPgwCgCgfTransToDownState_Object = MibTableColumn
jnxMbgPgwCgCgfTransToDownState = _JnxMbgPgwCgCgfTransToDownState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 29),
    _JnxMbgPgwCgCgfTransToDownState_Type()
)
jnxMbgPgwCgCgfTransToDownState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfTransToDownState.setStatus("current")
_JnxMbgPgwCgCgfContainers_Type = Counter64
_JnxMbgPgwCgCgfContainers_Object = MibTableColumn
jnxMbgPgwCgCgfContainers = _JnxMbgPgwCgCgfContainers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 4, 1, 30),
    _JnxMbgPgwCgCgfContainers_Type()
)
jnxMbgPgwCgCgfContainers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCgfContainers.setStatus("current")
_JnxMbgPgwCgLpsStatsTable_Object = MibTable
jnxMbgPgwCgLpsStatsTable = _JnxMbgPgwCgLpsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 5)
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgLpsStatsTable.setStatus("current")
_JnxMbgPgwCgLpsStatsEntry_Object = MibTableRow
jnxMbgPgwCgLpsStatsEntry = _JnxMbgPgwCgLpsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 5, 1)
)
jnxMbgPgwCgLpsStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgLpsStatsEntry.setStatus("current")
_JnxMbgPgwCgLpsFilesOnLcStorage_Type = Gauge32
_JnxMbgPgwCgLpsFilesOnLcStorage_Object = MibTableColumn
jnxMbgPgwCgLpsFilesOnLcStorage = _JnxMbgPgwCgLpsFilesOnLcStorage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 5, 1, 1),
    _JnxMbgPgwCgLpsFilesOnLcStorage_Type()
)
jnxMbgPgwCgLpsFilesOnLcStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgLpsFilesOnLcStorage.setStatus("current")
_JnxMbgPgwCgLpsStorageAvailSpace_Type = Gauge32
_JnxMbgPgwCgLpsStorageAvailSpace_Object = MibTableColumn
jnxMbgPgwCgLpsStorageAvailSpace = _JnxMbgPgwCgLpsStorageAvailSpace_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 5, 1, 2),
    _JnxMbgPgwCgLpsStorageAvailSpace_Type()
)
jnxMbgPgwCgLpsStorageAvailSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgLpsStorageAvailSpace.setStatus("current")
if mibBuilder.loadTexts:
    jnxMbgPgwCgLpsStorageAvailSpace.setUnits("MBytes")
_JnxMbgPgwCgTspStatsTable_Object = MibTable
jnxMbgPgwCgTspStatsTable = _JnxMbgPgwCgTspStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 6)
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgTspStatsTable.setStatus("current")
_JnxMbgPgwCgTspStatsEntry_Object = MibTableRow
jnxMbgPgwCgTspStatsEntry = _JnxMbgPgwCgTspStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 6, 1)
)
jnxMbgPgwCgTspStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
    (0, "JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgTspProfId"),
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgTspStatsEntry.setStatus("current")
_JnxMbgPgwCgTspProfId_Type = Unsigned32
_JnxMbgPgwCgTspProfId_Object = MibTableColumn
jnxMbgPgwCgTspProfId = _JnxMbgPgwCgTspProfId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 6, 1, 1),
    _JnxMbgPgwCgTspProfId_Type()
)
jnxMbgPgwCgTspProfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgPgwCgTspProfId.setStatus("current")
_JnxMbgPgwCgTspDRTReqTx_Type = Counter32
_JnxMbgPgwCgTspDRTReqTx_Object = MibTableColumn
jnxMbgPgwCgTspDRTReqTx = _JnxMbgPgwCgTspDRTReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 6, 1, 2),
    _JnxMbgPgwCgTspDRTReqTx_Type()
)
jnxMbgPgwCgTspDRTReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgTspDRTReqTx.setStatus("current")
_JnxMbgPgwCgTspDRTReqTmout_Type = Counter32
_JnxMbgPgwCgTspDRTReqTmout_Object = MibTableColumn
jnxMbgPgwCgTspDRTReqTmout = _JnxMbgPgwCgTspDRTReqTmout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 6, 1, 3),
    _JnxMbgPgwCgTspDRTReqTmout_Type()
)
jnxMbgPgwCgTspDRTReqTmout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgTspDRTReqTmout.setStatus("current")
_JnxMbgPgwCgTspDRTSucRspRx_Type = Counter32
_JnxMbgPgwCgTspDRTSucRspRx_Object = MibTableColumn
jnxMbgPgwCgTspDRTSucRspRx = _JnxMbgPgwCgTspDRTSucRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 6, 1, 4),
    _JnxMbgPgwCgTspDRTSucRspRx_Type()
)
jnxMbgPgwCgTspDRTSucRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgTspDRTSucRspRx.setStatus("current")
_JnxMbgPgwCgTspDRTErrRspRx_Type = Counter32
_JnxMbgPgwCgTspDRTErrRspRx_Object = MibTableColumn
jnxMbgPgwCgTspDRTErrRspRx = _JnxMbgPgwCgTspDRTErrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 6, 1, 5),
    _JnxMbgPgwCgTspDRTErrRspRx_Type()
)
jnxMbgPgwCgTspDRTErrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgTspDRTErrRspRx.setStatus("current")
_JnxMbgPgwCgTspRediReqRx_Type = Counter32
_JnxMbgPgwCgTspRediReqRx_Object = MibTableColumn
jnxMbgPgwCgTspRediReqRx = _JnxMbgPgwCgTspRediReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 6, 1, 6),
    _JnxMbgPgwCgTspRediReqRx_Type()
)
jnxMbgPgwCgTspRediReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgTspRediReqRx.setStatus("current")
_JnxMbgPgwCgTspRediRspTx_Type = Counter32
_JnxMbgPgwCgTspRediRspTx_Object = MibTableColumn
jnxMbgPgwCgTspRediRspTx = _JnxMbgPgwCgTspRediRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 6, 1, 7),
    _JnxMbgPgwCgTspRediRspTx_Type()
)
jnxMbgPgwCgTspRediRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgTspRediRspTx.setStatus("current")
_JnxMbgPgwCgTspSwitchovers_Type = Counter32
_JnxMbgPgwCgTspSwitchovers_Object = MibTableColumn
jnxMbgPgwCgTspSwitchovers = _JnxMbgPgwCgTspSwitchovers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 6, 1, 8),
    _JnxMbgPgwCgTspSwitchovers_Type()
)
jnxMbgPgwCgTspSwitchovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgTspSwitchovers.setStatus("current")
_JnxMbgPgwCgTspBatchReqTx_Type = Counter32
_JnxMbgPgwCgTspBatchReqTx_Object = MibTableColumn
jnxMbgPgwCgTspBatchReqTx = _JnxMbgPgwCgTspBatchReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 6, 1, 9),
    _JnxMbgPgwCgTspBatchReqTx_Type()
)
jnxMbgPgwCgTspBatchReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgTspBatchReqTx.setStatus("current")
_JnxMbgPgwCgTspBatchRspErrors_Type = Counter32
_JnxMbgPgwCgTspBatchRspErrors_Object = MibTableColumn
jnxMbgPgwCgTspBatchRspErrors = _JnxMbgPgwCgTspBatchRspErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 6, 1, 10),
    _JnxMbgPgwCgTspBatchRspErrors_Type()
)
jnxMbgPgwCgTspBatchRspErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgTspBatchRspErrors.setStatus("current")
_JnxMbgPgwCgTspBatchCDRsTx_Type = Counter32
_JnxMbgPgwCgTspBatchCDRsTx_Object = MibTableColumn
jnxMbgPgwCgTspBatchCDRsTx = _JnxMbgPgwCgTspBatchCDRsTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 6, 1, 11),
    _JnxMbgPgwCgTspBatchCDRsTx_Type()
)
jnxMbgPgwCgTspBatchCDRsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgTspBatchCDRsTx.setStatus("current")
_JnxMbgPgwCgTspTotalWFA_Type = Counter32
_JnxMbgPgwCgTspTotalWFA_Object = MibTableColumn
jnxMbgPgwCgTspTotalWFA = _JnxMbgPgwCgTspTotalWFA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 6, 1, 12),
    _JnxMbgPgwCgTspTotalWFA_Type()
)
jnxMbgPgwCgTspTotalWFA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgTspTotalWFA.setStatus("current")
_JnxMbgPgwCgTspProfName_Type = DisplayString
_JnxMbgPgwCgTspProfName_Object = MibTableColumn
jnxMbgPgwCgTspProfName = _JnxMbgPgwCgTspProfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 6, 1, 13),
    _JnxMbgPgwCgTspProfName_Type()
)
jnxMbgPgwCgTspProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgTspProfName.setStatus("current")
_JnxMbgPgwCgPeerStatsTable_Object = MibTable
jnxMbgPgwCgPeerStatsTable = _JnxMbgPgwCgPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 7)
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgPeerStatsTable.setStatus("current")
_JnxMbgPgwCgPeerStatsEntry_Object = MibTableRow
jnxMbgPgwCgPeerStatsEntry = _JnxMbgPgwCgPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 7, 1)
)
jnxMbgPgwCgPeerStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
    (0, "JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgPeerIndex"),
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgPeerStatsEntry.setStatus("current")
_JnxMbgPgwCgPeerIndex_Type = Unsigned32
_JnxMbgPgwCgPeerIndex_Object = MibTableColumn
jnxMbgPgwCgPeerIndex = _JnxMbgPgwCgPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 7, 1, 1),
    _JnxMbgPgwCgPeerIndex_Type()
)
jnxMbgPgwCgPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgPgwCgPeerIndex.setStatus("current")
_JnxMbgPgwCgPeerIpAddress_Type = IpAddress
_JnxMbgPgwCgPeerIpAddress_Object = MibTableColumn
jnxMbgPgwCgPeerIpAddress = _JnxMbgPgwCgPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 7, 1, 2),
    _JnxMbgPgwCgPeerIpAddress_Type()
)
jnxMbgPgwCgPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgPeerIpAddress.setStatus("current")


class _JnxMbgPgwCgPeerStatus_Type(Integer32):
    """Custom type jnxMbgPgwCgPeerStatus based on Integer32"""
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


_JnxMbgPgwCgPeerStatus_Type.__name__ = "Integer32"
_JnxMbgPgwCgPeerStatus_Object = MibTableColumn
jnxMbgPgwCgPeerStatus = _JnxMbgPgwCgPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 7, 1, 3),
    _JnxMbgPgwCgPeerStatus_Type()
)
jnxMbgPgwCgPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgPeerStatus.setStatus("current")
_JnxMbgPgwCgPeerEchoReqTx_Type = Counter64
_JnxMbgPgwCgPeerEchoReqTx_Object = MibTableColumn
jnxMbgPgwCgPeerEchoReqTx = _JnxMbgPgwCgPeerEchoReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 7, 1, 4),
    _JnxMbgPgwCgPeerEchoReqTx_Type()
)
jnxMbgPgwCgPeerEchoReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgPeerEchoReqTx.setStatus("current")
_JnxMbgPgwCgPeerEchoReqRx_Type = Counter64
_JnxMbgPgwCgPeerEchoReqRx_Object = MibTableColumn
jnxMbgPgwCgPeerEchoReqRx = _JnxMbgPgwCgPeerEchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 7, 1, 5),
    _JnxMbgPgwCgPeerEchoReqRx_Type()
)
jnxMbgPgwCgPeerEchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgPeerEchoReqRx.setStatus("current")
_JnxMbgPgwCgPeerEchoReqTmout_Type = Counter64
_JnxMbgPgwCgPeerEchoReqTmout_Object = MibTableColumn
jnxMbgPgwCgPeerEchoReqTmout = _JnxMbgPgwCgPeerEchoReqTmout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 7, 1, 6),
    _JnxMbgPgwCgPeerEchoReqTmout_Type()
)
jnxMbgPgwCgPeerEchoReqTmout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgPeerEchoReqTmout.setStatus("current")
_JnxMbgPgwCgPeerEchoRespTx_Type = Counter64
_JnxMbgPgwCgPeerEchoRespTx_Object = MibTableColumn
jnxMbgPgwCgPeerEchoRespTx = _JnxMbgPgwCgPeerEchoRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 7, 1, 7),
    _JnxMbgPgwCgPeerEchoRespTx_Type()
)
jnxMbgPgwCgPeerEchoRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgPeerEchoRespTx.setStatus("current")
_JnxMbgPgwCgPeerEchoRespRx_Type = Counter64
_JnxMbgPgwCgPeerEchoRespRx_Object = MibTableColumn
jnxMbgPgwCgPeerEchoRespRx = _JnxMbgPgwCgPeerEchoRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 7, 1, 8),
    _JnxMbgPgwCgPeerEchoRespRx_Type()
)
jnxMbgPgwCgPeerEchoRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgPeerEchoRespRx.setStatus("current")
_JnxMbgPgwCgPeerVerUnsuppTx_Type = Counter64
_JnxMbgPgwCgPeerVerUnsuppTx_Object = MibTableColumn
jnxMbgPgwCgPeerVerUnsuppTx = _JnxMbgPgwCgPeerVerUnsuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 7, 1, 9),
    _JnxMbgPgwCgPeerVerUnsuppTx_Type()
)
jnxMbgPgwCgPeerVerUnsuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgPeerVerUnsuppTx.setStatus("current")
_JnxMbgPgwCgPeerVerUnsuppRx_Type = Counter64
_JnxMbgPgwCgPeerVerUnsuppRx_Object = MibTableColumn
jnxMbgPgwCgPeerVerUnsuppRx = _JnxMbgPgwCgPeerVerUnsuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 7, 1, 10),
    _JnxMbgPgwCgPeerVerUnsuppRx_Type()
)
jnxMbgPgwCgPeerVerUnsuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgPeerVerUnsuppRx.setStatus("current")
_JnxMbgPgwCgPeerNodeAliveReqRx_Type = Counter64
_JnxMbgPgwCgPeerNodeAliveReqRx_Object = MibTableColumn
jnxMbgPgwCgPeerNodeAliveReqRx = _JnxMbgPgwCgPeerNodeAliveReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 7, 1, 11),
    _JnxMbgPgwCgPeerNodeAliveReqRx_Type()
)
jnxMbgPgwCgPeerNodeAliveReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgPeerNodeAliveReqRx.setStatus("current")
_JnxMbgPgwCgPeerNodeAliveRespTx_Type = Counter64
_JnxMbgPgwCgPeerNodeAliveRespTx_Object = MibTableColumn
jnxMbgPgwCgPeerNodeAliveRespTx = _JnxMbgPgwCgPeerNodeAliveRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 7, 1, 12),
    _JnxMbgPgwCgPeerNodeAliveRespTx_Type()
)
jnxMbgPgwCgPeerNodeAliveRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgPeerNodeAliveRespTx.setStatus("current")
_JnxMbgPgwCgPeerRedirectReqRx_Type = Counter64
_JnxMbgPgwCgPeerRedirectReqRx_Object = MibTableColumn
jnxMbgPgwCgPeerRedirectReqRx = _JnxMbgPgwCgPeerRedirectReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 7, 1, 13),
    _JnxMbgPgwCgPeerRedirectReqRx_Type()
)
jnxMbgPgwCgPeerRedirectReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgPeerRedirectReqRx.setStatus("current")
_JnxMbgPgwCgPeerRedirectRespTx_Type = Counter64
_JnxMbgPgwCgPeerRedirectRespTx_Object = MibTableColumn
jnxMbgPgwCgPeerRedirectRespTx = _JnxMbgPgwCgPeerRedirectRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 7, 1, 14),
    _JnxMbgPgwCgPeerRedirectRespTx_Type()
)
jnxMbgPgwCgPeerRedirectRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgPeerRedirectRespTx.setStatus("current")
_JnxMbgPgwCgPeerDRTReqTx_Type = Counter64
_JnxMbgPgwCgPeerDRTReqTx_Object = MibTableColumn
jnxMbgPgwCgPeerDRTReqTx = _JnxMbgPgwCgPeerDRTReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 7, 1, 15),
    _JnxMbgPgwCgPeerDRTReqTx_Type()
)
jnxMbgPgwCgPeerDRTReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgPeerDRTReqTx.setStatus("current")
_JnxMbgPgwCgPeerDRTSuccRespRx_Type = Counter64
_JnxMbgPgwCgPeerDRTSuccRespRx_Object = MibTableColumn
jnxMbgPgwCgPeerDRTSuccRespRx = _JnxMbgPgwCgPeerDRTSuccRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 7, 1, 16),
    _JnxMbgPgwCgPeerDRTSuccRespRx_Type()
)
jnxMbgPgwCgPeerDRTSuccRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgPeerDRTSuccRespRx.setStatus("current")
_JnxMbgPgwCgPeerDRTErrRespRx_Type = Counter64
_JnxMbgPgwCgPeerDRTErrRespRx_Object = MibTableColumn
jnxMbgPgwCgPeerDRTErrRespRx = _JnxMbgPgwCgPeerDRTErrRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 7, 1, 17),
    _JnxMbgPgwCgPeerDRTErrRespRx_Type()
)
jnxMbgPgwCgPeerDRTErrRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgPeerDRTErrRespRx.setStatus("current")
_JnxMbgPgwCgPeerProfileName_Type = DisplayString
_JnxMbgPgwCgPeerProfileName_Object = MibTableColumn
jnxMbgPgwCgPeerProfileName = _JnxMbgPgwCgPeerProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 7, 1, 18),
    _JnxMbgPgwCgPeerProfileName_Type()
)
jnxMbgPgwCgPeerProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgPeerProfileName.setStatus("current")
_JnxMbgPgwCgGlobalStatsTable_Object = MibTable
jnxMbgPgwCgGlobalStatsTable = _JnxMbgPgwCgGlobalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 8)
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgGlobalStatsTable.setStatus("current")
_JnxMbgPgwCgGlobalStatsEntry_Object = MibTableRow
jnxMbgPgwCgGlobalStatsEntry = _JnxMbgPgwCgGlobalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 8, 1)
)
jnxMbgPgwCgGlobalStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgGlobalStatsEntry.setStatus("current")
_JnxMbgPgwCgCdrSendErrors_Type = Counter64
_JnxMbgPgwCgCdrSendErrors_Object = MibTableColumn
jnxMbgPgwCgCdrSendErrors = _JnxMbgPgwCgCdrSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 8, 1, 1),
    _JnxMbgPgwCgCdrSendErrors_Type()
)
jnxMbgPgwCgCdrSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCdrSendErrors.setStatus("current")
_JnxMbgPgwCgCdrEncodeErrors_Type = Counter64
_JnxMbgPgwCgCdrEncodeErrors_Object = MibTableColumn
jnxMbgPgwCgCdrEncodeErrors = _JnxMbgPgwCgCdrEncodeErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 8, 1, 2),
    _JnxMbgPgwCgCdrEncodeErrors_Type()
)
jnxMbgPgwCgCdrEncodeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCdrEncodeErrors.setStatus("current")
_JnxMbgPgwCgCdrAllocFailures_Type = Counter64
_JnxMbgPgwCgCdrAllocFailures_Object = MibTableColumn
jnxMbgPgwCgCdrAllocFailures = _JnxMbgPgwCgCdrAllocFailures_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 8, 1, 3),
    _JnxMbgPgwCgCdrAllocFailures_Type()
)
jnxMbgPgwCgCdrAllocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCdrAllocFailures.setStatus("current")
_JnxMbgPgwCgContFailures_Type = Counter64
_JnxMbgPgwCgContFailures_Object = MibTableColumn
jnxMbgPgwCgContFailures = _JnxMbgPgwCgContFailures_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 8, 1, 4),
    _JnxMbgPgwCgContFailures_Type()
)
jnxMbgPgwCgContFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgContFailures.setStatus("current")
_JnxMbgPgwCgCmBearersCreated_Type = Counter64
_JnxMbgPgwCgCmBearersCreated_Object = MibTableColumn
jnxMbgPgwCgCmBearersCreated = _JnxMbgPgwCgCmBearersCreated_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 8, 1, 5),
    _JnxMbgPgwCgCmBearersCreated_Type()
)
jnxMbgPgwCgCmBearersCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCmBearersCreated.setStatus("current")
_JnxMbgPgwCgCmBearersDeleted_Type = Counter64
_JnxMbgPgwCgCmBearersDeleted_Object = MibTableColumn
jnxMbgPgwCgCmBearersDeleted = _JnxMbgPgwCgCmBearersDeleted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 1, 8, 1, 6),
    _JnxMbgPgwCgCmBearersDeleted_Type()
)
jnxMbgPgwCgCmBearersDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCgCmBearersDeleted.setStatus("current")

# Managed Objects groups


# Notification objects

jnxMbgPgwCgGtpGWUpNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 0, 1)
)
jnxMbgPgwCgGtpGWUpNotif.setObjects(
      *(("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgServerName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgServicePicName"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgGtpGWUpNotif.setStatus(
        "deprecated"
    )

jnxMbgPgwCgGtpGWDownNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 0, 2)
)
jnxMbgPgwCgGtpGWDownNotif.setObjects(
      *(("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgServerName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgServicePicName"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgGtpGWDownNotif.setStatus(
        "deprecated"
    )

jnxMbgPgwCgCDRDestNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 0, 3)
)
jnxMbgPgwCgCDRDestNotif.setObjects(
      *(("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgCDRDest"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgTSPName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgActiveCgfIpAddr"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgCDRDestNotif.setStatus(
        "deprecated"
    )

jnxMbgPgwCgMemThresNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 0, 4)
)
jnxMbgPgwCgMemThresNotif.setObjects(
      *(("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgAlarmStatus"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgMemLimit"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgTSPName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgServicePicName"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgMemThresNotif.setStatus(
        "deprecated"
    )

jnxMbgPgwCgLcsThresNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 0, 5)
)
jnxMbgPgwCgLcsThresNotif.setObjects(
      *(("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgLcsSpace"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgLcsUtil"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgLcsThresNotif.setStatus(
        "deprecated"
    )

jnxMbgPgwCgServiceUpNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 0, 6)
)
jnxMbgPgwCgServiceUpNotif.setObjects(
    ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgServicePicName")
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgServiceUpNotif.setStatus(
        "deprecated"
    )

jnxMbgPgwCgMMStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 0, 7)
)
jnxMbgPgwCgMMStateChange.setObjects(
      *(("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgProfileName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgPrevMMState"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgNewMMState"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgMMStateChange.setStatus(
        "deprecated"
    )

jnxMbgPgwCgTMMStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 0, 8)
)
jnxMbgPgwCgTMMStateChange.setObjects(
      *(("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgTProfileName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgTPrevMMState"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgTNewMMState"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgTMMStateChange.setStatus(
        "deprecated"
    )

jnxMbgPgwCgGtpGWUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 0, 9)
)
jnxMbgPgwCgGtpGWUpNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgServerName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgServicePicName"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgGtpGWUpNotify.setStatus(
        "current"
    )

jnxMbgPgwCgGtpGWDownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 0, 10)
)
jnxMbgPgwCgGtpGWDownNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgServerName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgServicePicName"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgGtpGWDownNotify.setStatus(
        "current"
    )

jnxMbgPgwCgCDRDestNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 0, 11)
)
jnxMbgPgwCgCDRDestNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgCDRDest"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgPeerProfName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgActiveCgfIpAddr"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgCDRDestNotify.setStatus(
        "current"
    )

jnxMbgPgwCgServiceUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 0, 12)
)
jnxMbgPgwCgServiceUpNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgServicePicName"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgServiceUpNotify.setStatus(
        "current"
    )

jnxMbgPgwCgMMStateChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 0, 13)
)
jnxMbgPgwCgMMStateChangeNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgPeerProfName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgPrevMMState"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgNewMMState"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgMMStateChangeNotify.setStatus(
        "current"
    )

jnxMbgPgwCgTMMStateChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 0, 14)
)
jnxMbgPgwCgTMMStateChangeNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgPeerProfName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgPrevMMState"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgNewMMState"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgTMMStateChangeNotify.setStatus(
        "current"
    )

jnxMbgPgwCgMemHighThresNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 0, 15)
)
jnxMbgPgwCgMemHighThresNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgPeerProfName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgServicePicName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgMemLimit"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgAlarmStatus"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgMemHighThresNotify.setStatus(
        "current"
    )

jnxMbgPgwCgMemMediumThresNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 0, 16)
)
jnxMbgPgwCgMemMediumThresNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgPeerProfName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgServicePicName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgMemLimit"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgAlarmStatus"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgMemMediumThresNotify.setStatus(
        "current"
    )

jnxMbgPgwCgMemLowThresNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 0, 17)
)
jnxMbgPgwCgMemLowThresNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgPeerProfName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgServicePicName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgMemLimit"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgAlarmStatus"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgMemLowThresNotify.setStatus(
        "current"
    )

jnxMbgPgwCgLcsThresHighNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 0, 18)
)
jnxMbgPgwCgLcsThresHighNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgAlarmStatus"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgLcsUtil"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgLcsThresHighNotify.setStatus(
        "current"
    )

jnxMbgPgwCgLcsThresMediumNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 0, 19)
)
jnxMbgPgwCgLcsThresMediumNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgAlarmStatus"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgLcsUtil"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgLcsThresMediumNotify.setStatus(
        "current"
    )

jnxMbgPgwCgLcsThresLowNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 3, 0, 20)
)
jnxMbgPgwCgLcsThresLowNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgAlarmStatus"),
        ("JUNIPER-MOBILITY-CHARGING-MIB", "jnxMbgPgwCgLcsUtil"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwCgLcsThresLowNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MOBILITY-CHARGING-MIB",
    **{"jnxMbgPgwChargingMib": jnxMbgPgwChargingMib,
       "jnxMbgPgwCgNotifications": jnxMbgPgwCgNotifications,
       "jnxMbgPgwCgGtpGWUpNotif": jnxMbgPgwCgGtpGWUpNotif,
       "jnxMbgPgwCgGtpGWDownNotif": jnxMbgPgwCgGtpGWDownNotif,
       "jnxMbgPgwCgCDRDestNotif": jnxMbgPgwCgCDRDestNotif,
       "jnxMbgPgwCgMemThresNotif": jnxMbgPgwCgMemThresNotif,
       "jnxMbgPgwCgLcsThresNotif": jnxMbgPgwCgLcsThresNotif,
       "jnxMbgPgwCgServiceUpNotif": jnxMbgPgwCgServiceUpNotif,
       "jnxMbgPgwCgMMStateChange": jnxMbgPgwCgMMStateChange,
       "jnxMbgPgwCgTMMStateChange": jnxMbgPgwCgTMMStateChange,
       "jnxMbgPgwCgGtpGWUpNotify": jnxMbgPgwCgGtpGWUpNotify,
       "jnxMbgPgwCgGtpGWDownNotify": jnxMbgPgwCgGtpGWDownNotify,
       "jnxMbgPgwCgCDRDestNotify": jnxMbgPgwCgCDRDestNotify,
       "jnxMbgPgwCgServiceUpNotify": jnxMbgPgwCgServiceUpNotify,
       "jnxMbgPgwCgMMStateChangeNotify": jnxMbgPgwCgMMStateChangeNotify,
       "jnxMbgPgwCgTMMStateChangeNotify": jnxMbgPgwCgTMMStateChangeNotify,
       "jnxMbgPgwCgMemHighThresNotify": jnxMbgPgwCgMemHighThresNotify,
       "jnxMbgPgwCgMemMediumThresNotify": jnxMbgPgwCgMemMediumThresNotify,
       "jnxMbgPgwCgMemLowThresNotify": jnxMbgPgwCgMemLowThresNotify,
       "jnxMbgPgwCgLcsThresHighNotify": jnxMbgPgwCgLcsThresHighNotify,
       "jnxMbgPgwCgLcsThresMediumNotify": jnxMbgPgwCgLcsThresMediumNotify,
       "jnxMbgPgwCgLcsThresLowNotify": jnxMbgPgwCgLcsThresLowNotify,
       "jnxMbgPgwChargingObjects": jnxMbgPgwChargingObjects,
       "jnxMbgPgwCgLcStorageStats": jnxMbgPgwCgLcStorageStats,
       "jnxMbgPgwCgFilesOnLcStorage": jnxMbgPgwCgFilesOnLcStorage,
       "jnxMbgPgwCgLcStorageAvailSpace": jnxMbgPgwCgLcStorageAvailSpace,
       "jnxMbgPgwCgCgfGroupsStatsTable": jnxMbgPgwCgCgfGroupsStatsTable,
       "jnxMbgPgwCgCgfGroupStatsEntry": jnxMbgPgwCgCgfGroupStatsEntry,
       "jnxMbgPgwCgCgfGrpProfName": jnxMbgPgwCgCgfGrpProfName,
       "jnxMbgPgwCgCgfGrpDRTReqTx": jnxMbgPgwCgCgfGrpDRTReqTx,
       "jnxMbgPgwCgCgfGrpDRTReqRx": jnxMbgPgwCgCgfGrpDRTReqRx,
       "jnxMbgPgwCgCgfGrpDRTReqTmout": jnxMbgPgwCgCgfGrpDRTReqTmout,
       "jnxMbgPgwCgCgfGrpDRTSucRspRx": jnxMbgPgwCgCgfGrpDRTSucRspRx,
       "jnxMbgPgwCgCgfGrpDRTErrRspRx": jnxMbgPgwCgCgfGrpDRTErrRspRx,
       "jnxMbgPgwCgCgfGrpRediReqRx": jnxMbgPgwCgCgfGrpRediReqRx,
       "jnxMbgPgwCgCgfGrpRediRspTx": jnxMbgPgwCgCgfGrpRediRspTx,
       "jnxMbgPgwCgCgfGrpSwitchovers": jnxMbgPgwCgCgfGrpSwitchovers,
       "jnxMbgPgwCgCgfGrpBatchReqTx": jnxMbgPgwCgCgfGrpBatchReqTx,
       "jnxMbgPgwCgCgfGrpBatchRspErrors": jnxMbgPgwCgCgfGrpBatchRspErrors,
       "jnxMbgPgwCgCgfGrpBatchCDRsTx": jnxMbgPgwCgCgfGrpBatchCDRsTx,
       "jnxMbgPgwCgCgfGroupTotalWFA": jnxMbgPgwCgCgfGroupTotalWFA,
       "jnxMbgPgwCgNotificationVars": jnxMbgPgwCgNotificationVars,
       "jnxMbgPgwCgServerName": jnxMbgPgwCgServerName,
       "jnxMbgPgwCgServicePicName": jnxMbgPgwCgServicePicName,
       "jnxMbgPgwCgCDRDest": jnxMbgPgwCgCDRDest,
       "jnxMbgPgwCgActiveCgfIpAddr": jnxMbgPgwCgActiveCgfIpAddr,
       "jnxMbgPgwCgTSPName": jnxMbgPgwCgTSPName,
       "jnxMbgPgwCgMemLimit": jnxMbgPgwCgMemLimit,
       "jnxMbgPgwCgLcsSpace": jnxMbgPgwCgLcsSpace,
       "jnxMbgPgwCgLcsUtil": jnxMbgPgwCgLcsUtil,
       "jnxMbgPgwCgAlarmStatus": jnxMbgPgwCgAlarmStatus,
       "jnxMbgPgwCgProfileName": jnxMbgPgwCgProfileName,
       "jnxMbgPgwCgPrevMMState": jnxMbgPgwCgPrevMMState,
       "jnxMbgPgwCgNewMMState": jnxMbgPgwCgNewMMState,
       "jnxMbgPgwCgTProfileName": jnxMbgPgwCgTProfileName,
       "jnxMbgPgwCgTPrevMMState": jnxMbgPgwCgTPrevMMState,
       "jnxMbgPgwCgTNewMMState": jnxMbgPgwCgTNewMMState,
       "jnxMbgPgwCgPeerProfName": jnxMbgPgwCgPeerProfName,
       "jnxMbgPgwCgCgfStatsTable": jnxMbgPgwCgCgfStatsTable,
       "jnxMbgPgwCgCgfStatsEntry": jnxMbgPgwCgCgfStatsEntry,
       "jnxMbgPgwCgCgfProfName": jnxMbgPgwCgCgfProfName,
       "jnxMbgPgwCgCgfIndex": jnxMbgPgwCgCgfIndex,
       "jnxMbgPgwCgCgfIpAddress": jnxMbgPgwCgCgfIpAddress,
       "jnxMbgPgwCgCgfStatus": jnxMbgPgwCgCgfStatus,
       "jnxMbgPgwCgCgfUpDuration": jnxMbgPgwCgCgfUpDuration,
       "jnxMbgPgwCgCgfDownDuration": jnxMbgPgwCgCgfDownDuration,
       "jnxMbgPgwCgCgfEchoReqTx": jnxMbgPgwCgCgfEchoReqTx,
       "jnxMbgPgwCgCgfEchoReqRx": jnxMbgPgwCgCgfEchoReqRx,
       "jnxMbgPgwCgCgfEchoReqTmout": jnxMbgPgwCgCgfEchoReqTmout,
       "jnxMbgPgwCgCgfEchoRespTx": jnxMbgPgwCgCgfEchoRespTx,
       "jnxMbgPgwCgCgfEchoRespRx": jnxMbgPgwCgCgfEchoRespRx,
       "jnxMbgPgwCgCgfVerUnsuppTx": jnxMbgPgwCgCgfVerUnsuppTx,
       "jnxMbgPgwCgCgfVerUnsuppRx": jnxMbgPgwCgCgfVerUnsuppRx,
       "jnxMbgPgwCgCgfNodeAliveReqTx": jnxMbgPgwCgCgfNodeAliveReqTx,
       "jnxMbgPgwCgCgfNodeAliveReqRx": jnxMbgPgwCgCgfNodeAliveReqRx,
       "jnxMbgPgwCgCgfNodeAliveReqTmout": jnxMbgPgwCgCgfNodeAliveReqTmout,
       "jnxMbgPgwCgCgfNodeAliveRespTx": jnxMbgPgwCgCgfNodeAliveRespTx,
       "jnxMbgPgwCgCgfNodeAliveRespRx": jnxMbgPgwCgCgfNodeAliveRespRx,
       "jnxMbgPgwCgCgfRedirectReqRx": jnxMbgPgwCgCgfRedirectReqRx,
       "jnxMbgPgwCgCgfRedirectRespTx": jnxMbgPgwCgCgfRedirectRespTx,
       "jnxMbgPgwCgCgfDRTReqTx": jnxMbgPgwCgCgfDRTReqTx,
       "jnxMbgPgwCgCgfDRTReqTmout": jnxMbgPgwCgCgfDRTReqTmout,
       "jnxMbgPgwCgCgfDRTSuccRespRx": jnxMbgPgwCgCgfDRTSuccRespRx,
       "jnxMbgPgwCgCgfDRTErrRespRx": jnxMbgPgwCgCgfDRTErrRespRx,
       "jnxMbgPgwCgCgfCdrTx": jnxMbgPgwCgCgfCdrTx,
       "jnxMbgPgwCgCgfDRTRTTMean": jnxMbgPgwCgCgfDRTRTTMean,
       "jnxMbgPgwCgCgfDRTRTTMin": jnxMbgPgwCgCgfDRTRTTMin,
       "jnxMbgPgwCgCgfDRTRTTMax": jnxMbgPgwCgCgfDRTRTTMax,
       "jnxMbgPgwCgCgfTransToDownState": jnxMbgPgwCgCgfTransToDownState,
       "jnxMbgPgwCgCgfContainers": jnxMbgPgwCgCgfContainers,
       "jnxMbgPgwCgLpsStatsTable": jnxMbgPgwCgLpsStatsTable,
       "jnxMbgPgwCgLpsStatsEntry": jnxMbgPgwCgLpsStatsEntry,
       "jnxMbgPgwCgLpsFilesOnLcStorage": jnxMbgPgwCgLpsFilesOnLcStorage,
       "jnxMbgPgwCgLpsStorageAvailSpace": jnxMbgPgwCgLpsStorageAvailSpace,
       "jnxMbgPgwCgTspStatsTable": jnxMbgPgwCgTspStatsTable,
       "jnxMbgPgwCgTspStatsEntry": jnxMbgPgwCgTspStatsEntry,
       "jnxMbgPgwCgTspProfId": jnxMbgPgwCgTspProfId,
       "jnxMbgPgwCgTspDRTReqTx": jnxMbgPgwCgTspDRTReqTx,
       "jnxMbgPgwCgTspDRTReqTmout": jnxMbgPgwCgTspDRTReqTmout,
       "jnxMbgPgwCgTspDRTSucRspRx": jnxMbgPgwCgTspDRTSucRspRx,
       "jnxMbgPgwCgTspDRTErrRspRx": jnxMbgPgwCgTspDRTErrRspRx,
       "jnxMbgPgwCgTspRediReqRx": jnxMbgPgwCgTspRediReqRx,
       "jnxMbgPgwCgTspRediRspTx": jnxMbgPgwCgTspRediRspTx,
       "jnxMbgPgwCgTspSwitchovers": jnxMbgPgwCgTspSwitchovers,
       "jnxMbgPgwCgTspBatchReqTx": jnxMbgPgwCgTspBatchReqTx,
       "jnxMbgPgwCgTspBatchRspErrors": jnxMbgPgwCgTspBatchRspErrors,
       "jnxMbgPgwCgTspBatchCDRsTx": jnxMbgPgwCgTspBatchCDRsTx,
       "jnxMbgPgwCgTspTotalWFA": jnxMbgPgwCgTspTotalWFA,
       "jnxMbgPgwCgTspProfName": jnxMbgPgwCgTspProfName,
       "jnxMbgPgwCgPeerStatsTable": jnxMbgPgwCgPeerStatsTable,
       "jnxMbgPgwCgPeerStatsEntry": jnxMbgPgwCgPeerStatsEntry,
       "jnxMbgPgwCgPeerIndex": jnxMbgPgwCgPeerIndex,
       "jnxMbgPgwCgPeerIpAddress": jnxMbgPgwCgPeerIpAddress,
       "jnxMbgPgwCgPeerStatus": jnxMbgPgwCgPeerStatus,
       "jnxMbgPgwCgPeerEchoReqTx": jnxMbgPgwCgPeerEchoReqTx,
       "jnxMbgPgwCgPeerEchoReqRx": jnxMbgPgwCgPeerEchoReqRx,
       "jnxMbgPgwCgPeerEchoReqTmout": jnxMbgPgwCgPeerEchoReqTmout,
       "jnxMbgPgwCgPeerEchoRespTx": jnxMbgPgwCgPeerEchoRespTx,
       "jnxMbgPgwCgPeerEchoRespRx": jnxMbgPgwCgPeerEchoRespRx,
       "jnxMbgPgwCgPeerVerUnsuppTx": jnxMbgPgwCgPeerVerUnsuppTx,
       "jnxMbgPgwCgPeerVerUnsuppRx": jnxMbgPgwCgPeerVerUnsuppRx,
       "jnxMbgPgwCgPeerNodeAliveReqRx": jnxMbgPgwCgPeerNodeAliveReqRx,
       "jnxMbgPgwCgPeerNodeAliveRespTx": jnxMbgPgwCgPeerNodeAliveRespTx,
       "jnxMbgPgwCgPeerRedirectReqRx": jnxMbgPgwCgPeerRedirectReqRx,
       "jnxMbgPgwCgPeerRedirectRespTx": jnxMbgPgwCgPeerRedirectRespTx,
       "jnxMbgPgwCgPeerDRTReqTx": jnxMbgPgwCgPeerDRTReqTx,
       "jnxMbgPgwCgPeerDRTSuccRespRx": jnxMbgPgwCgPeerDRTSuccRespRx,
       "jnxMbgPgwCgPeerDRTErrRespRx": jnxMbgPgwCgPeerDRTErrRespRx,
       "jnxMbgPgwCgPeerProfileName": jnxMbgPgwCgPeerProfileName,
       "jnxMbgPgwCgGlobalStatsTable": jnxMbgPgwCgGlobalStatsTable,
       "jnxMbgPgwCgGlobalStatsEntry": jnxMbgPgwCgGlobalStatsEntry,
       "jnxMbgPgwCgCdrSendErrors": jnxMbgPgwCgCdrSendErrors,
       "jnxMbgPgwCgCdrEncodeErrors": jnxMbgPgwCgCdrEncodeErrors,
       "jnxMbgPgwCgCdrAllocFailures": jnxMbgPgwCgCdrAllocFailures,
       "jnxMbgPgwCgContFailures": jnxMbgPgwCgContFailures,
       "jnxMbgPgwCgCmBearersCreated": jnxMbgPgwCgCmBearersCreated,
       "jnxMbgPgwCgCmBearersDeleted": jnxMbgPgwCgCmBearersDeleted}
)
