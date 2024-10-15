# SNMP MIB module (RUCKUS-RADIO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RUCKUS-RADIO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:43 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ruckusCommonRadioModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusCommonRadioModule")

(RuckusCountryCode,
 RuckusRadioMode,
 RuckusRate) = mibBuilder.importSymbols(
    "RUCKUS-TC-MIB",
    "RuckusCountryCode",
    "RuckusRadioMode",
    "RuckusRate")

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

ruckusRadioMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusRadioObjects_ObjectIdentity = ObjectIdentity
ruckusRadioObjects = _RuckusRadioObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1)
)
_RuckusRadioInfo_ObjectIdentity = ObjectIdentity
ruckusRadioInfo = _RuckusRadioInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1)
)
_RuckusRadioNumber_Type = Integer32
_RuckusRadioNumber_Object = MibScalar
ruckusRadioNumber = _RuckusRadioNumber_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 1),
    _RuckusRadioNumber_Type()
)
ruckusRadioNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioNumber.setStatus("current")
_RuckusRadioTable_Object = MibTable
ruckusRadioTable = _RuckusRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ruckusRadioTable.setStatus("current")
_RuckusRadioEntry_Object = MibTableRow
ruckusRadioEntry = _RuckusRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 2, 1)
)
ruckusRadioEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruckusRadioEntry.setStatus("current")


class _RuckusRadioMode_Type(Integer32):
    """Custom type ruckusRadioMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("ieee802dot11a-only", 5),
          ("ieee802dot11b-only", 2),
          ("ieee802dot11g-only", 1),
          ("ieee802dot11na", 4),
          ("ieee802dot11ng", 3))
    )


_RuckusRadioMode_Type.__name__ = "Integer32"
_RuckusRadioMode_Object = MibTableColumn
ruckusRadioMode = _RuckusRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 2, 1, 1),
    _RuckusRadioMode_Type()
)
ruckusRadioMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusRadioMode.setStatus("current")
_RuckusRadioCountry_Type = RuckusCountryCode
_RuckusRadioCountry_Object = MibTableColumn
ruckusRadioCountry = _RuckusRadioCountry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 2, 1, 2),
    _RuckusRadioCountry_Type()
)
ruckusRadioCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusRadioCountry.setStatus("current")


class _RuckusRadioBSSType_Type(Integer32):
    """Custom type ruckusRadioBSSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("independent", 3),
          ("master", 2),
          ("station", 1))
    )


_RuckusRadioBSSType_Type.__name__ = "Integer32"
_RuckusRadioBSSType_Object = MibTableColumn
ruckusRadioBSSType = _RuckusRadioBSSType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 2, 1, 3),
    _RuckusRadioBSSType_Type()
)
ruckusRadioBSSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioBSSType.setStatus("current")


class _RuckusRadioChannel_Type(Integer32):
    """Custom type ruckusRadioChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_RuckusRadioChannel_Type.__name__ = "Integer32"
_RuckusRadioChannel_Object = MibTableColumn
ruckusRadioChannel = _RuckusRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 2, 1, 4),
    _RuckusRadioChannel_Type()
)
ruckusRadioChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusRadioChannel.setStatus("current")


class _RuckusRadioDataRate_Type(OctetString):
    """Custom type ruckusRadioDataRate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_RuckusRadioDataRate_Type.__name__ = "OctetString"
_RuckusRadioDataRate_Object = MibTableColumn
ruckusRadioDataRate = _RuckusRadioDataRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 2, 1, 5),
    _RuckusRadioDataRate_Type()
)
ruckusRadioDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioDataRate.setStatus("current")


class _RuckusRadioTxPower_Type(Integer32):
    """Custom type ruckusRadioTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("eighth", 3),
          ("full", 0),
          ("half", 1),
          ("minimum", 4),
          ("quarter", 2))
    )


_RuckusRadioTxPower_Type.__name__ = "Integer32"
_RuckusRadioTxPower_Object = MibTableColumn
ruckusRadioTxPower = _RuckusRadioTxPower_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 2, 1, 6),
    _RuckusRadioTxPower_Type()
)
ruckusRadioTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusRadioTxPower.setStatus("current")


class _RuckusRadioProtectionMode_Type(Integer32):
    """Custom type ruckusRadioProtectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ctsOnly", 1),
          ("ctsRts", 2),
          ("none", 0))
    )


_RuckusRadioProtectionMode_Type.__name__ = "Integer32"
_RuckusRadioProtectionMode_Object = MibTableColumn
ruckusRadioProtectionMode = _RuckusRadioProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 2, 1, 7),
    _RuckusRadioProtectionMode_Type()
)
ruckusRadioProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusRadioProtectionMode.setStatus("current")
_RuckusRadioStatsTable_Object = MibTable
ruckusRadioStatsTable = _RuckusRadioStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ruckusRadioStatsTable.setStatus("current")
_RuckusRadioStatsEntry_Object = MibTableRow
ruckusRadioStatsEntry = _RuckusRadioStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1)
)
ruckusRadioStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruckusRadioStatsEntry.setStatus("current")
_RuckusRadioStatsMaxSta_Type = Counter32
_RuckusRadioStatsMaxSta_Object = MibTableColumn
ruckusRadioStatsMaxSta = _RuckusRadioStatsMaxSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 1),
    _RuckusRadioStatsMaxSta_Type()
)
ruckusRadioStatsMaxSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsMaxSta.setStatus("current")
_RuckusRadioStatsNumSta_Type = Counter32
_RuckusRadioStatsNumSta_Object = MibTableColumn
ruckusRadioStatsNumSta = _RuckusRadioStatsNumSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 2),
    _RuckusRadioStatsNumSta_Type()
)
ruckusRadioStatsNumSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsNumSta.setStatus("current")
_RuckusRadioStatsNumAuthSta_Type = Counter32
_RuckusRadioStatsNumAuthSta_Object = MibTableColumn
ruckusRadioStatsNumAuthSta = _RuckusRadioStatsNumAuthSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 3),
    _RuckusRadioStatsNumAuthSta_Type()
)
ruckusRadioStatsNumAuthSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsNumAuthSta.setStatus("current")
_RuckusRadioStatsNumAuthReq_Type = Counter32
_RuckusRadioStatsNumAuthReq_Object = MibTableColumn
ruckusRadioStatsNumAuthReq = _RuckusRadioStatsNumAuthReq_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 4),
    _RuckusRadioStatsNumAuthReq_Type()
)
ruckusRadioStatsNumAuthReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsNumAuthReq.setStatus("current")
_RuckusRadioStatsNumAuthResp_Type = Counter32
_RuckusRadioStatsNumAuthResp_Object = MibTableColumn
ruckusRadioStatsNumAuthResp = _RuckusRadioStatsNumAuthResp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 5),
    _RuckusRadioStatsNumAuthResp_Type()
)
ruckusRadioStatsNumAuthResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsNumAuthResp.setStatus("current")
_RuckusRadioStatsNumAuthSuccess_Type = Counter32
_RuckusRadioStatsNumAuthSuccess_Object = MibTableColumn
ruckusRadioStatsNumAuthSuccess = _RuckusRadioStatsNumAuthSuccess_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 6),
    _RuckusRadioStatsNumAuthSuccess_Type()
)
ruckusRadioStatsNumAuthSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsNumAuthSuccess.setStatus("current")
_RuckusRadioStatsNumAuthFail_Type = Counter32
_RuckusRadioStatsNumAuthFail_Object = MibTableColumn
ruckusRadioStatsNumAuthFail = _RuckusRadioStatsNumAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 7),
    _RuckusRadioStatsNumAuthFail_Type()
)
ruckusRadioStatsNumAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsNumAuthFail.setStatus("current")
_RuckusRadioStatsNumAssocReq_Type = Counter32
_RuckusRadioStatsNumAssocReq_Object = MibTableColumn
ruckusRadioStatsNumAssocReq = _RuckusRadioStatsNumAssocReq_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 8),
    _RuckusRadioStatsNumAssocReq_Type()
)
ruckusRadioStatsNumAssocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsNumAssocReq.setStatus("current")
_RuckusRadioStatsNumAssocResp_Type = Counter32
_RuckusRadioStatsNumAssocResp_Object = MibTableColumn
ruckusRadioStatsNumAssocResp = _RuckusRadioStatsNumAssocResp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 9),
    _RuckusRadioStatsNumAssocResp_Type()
)
ruckusRadioStatsNumAssocResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsNumAssocResp.setStatus("current")
_RuckusRadioStatsNumAssocSuccess_Type = Counter32
_RuckusRadioStatsNumAssocSuccess_Object = MibTableColumn
ruckusRadioStatsNumAssocSuccess = _RuckusRadioStatsNumAssocSuccess_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 10),
    _RuckusRadioStatsNumAssocSuccess_Type()
)
ruckusRadioStatsNumAssocSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsNumAssocSuccess.setStatus("current")
_RuckusRadioStatsNumAssocFail_Type = Counter32
_RuckusRadioStatsNumAssocFail_Object = MibTableColumn
ruckusRadioStatsNumAssocFail = _RuckusRadioStatsNumAssocFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 11),
    _RuckusRadioStatsNumAssocFail_Type()
)
ruckusRadioStatsNumAssocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsNumAssocFail.setStatus("current")
_RuckusRadioStatsAssocFailRate_Type = Unsigned32
_RuckusRadioStatsAssocFailRate_Object = MibTableColumn
ruckusRadioStatsAssocFailRate = _RuckusRadioStatsAssocFailRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 12),
    _RuckusRadioStatsAssocFailRate_Type()
)
ruckusRadioStatsAssocFailRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsAssocFailRate.setStatus("current")
_RuckusRadioStatsAuthFailRate_Type = Unsigned32
_RuckusRadioStatsAuthFailRate_Object = MibTableColumn
ruckusRadioStatsAuthFailRate = _RuckusRadioStatsAuthFailRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 13),
    _RuckusRadioStatsAuthFailRate_Type()
)
ruckusRadioStatsAuthFailRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsAuthFailRate.setStatus("current")
_RuckusRadioStatsAssocSuccessRate_Type = Unsigned32
_RuckusRadioStatsAssocSuccessRate_Object = MibTableColumn
ruckusRadioStatsAssocSuccessRate = _RuckusRadioStatsAssocSuccessRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 14),
    _RuckusRadioStatsAssocSuccessRate_Type()
)
ruckusRadioStatsAssocSuccessRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsAssocSuccessRate.setStatus("current")
_RuckusRadioStatsResourceUtil_Type = Unsigned32
_RuckusRadioStatsResourceUtil_Object = MibTableColumn
ruckusRadioStatsResourceUtil = _RuckusRadioStatsResourceUtil_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 15),
    _RuckusRadioStatsResourceUtil_Type()
)
ruckusRadioStatsResourceUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsResourceUtil.setStatus("current")
_RuckusRadioStatsRxBytes_Type = Counter32
_RuckusRadioStatsRxBytes_Object = MibTableColumn
ruckusRadioStatsRxBytes = _RuckusRadioStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 16),
    _RuckusRadioStatsRxBytes_Type()
)
ruckusRadioStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsRxBytes.setStatus("current")
_RuckusRadioStatsRxFrames_Type = Counter32
_RuckusRadioStatsRxFrames_Object = MibTableColumn
ruckusRadioStatsRxFrames = _RuckusRadioStatsRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 17),
    _RuckusRadioStatsRxFrames_Type()
)
ruckusRadioStatsRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsRxFrames.setStatus("current")
_RuckusRadioStatsRxWEPFail_Type = Counter32
_RuckusRadioStatsRxWEPFail_Object = MibTableColumn
ruckusRadioStatsRxWEPFail = _RuckusRadioStatsRxWEPFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 18),
    _RuckusRadioStatsRxWEPFail_Type()
)
ruckusRadioStatsRxWEPFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsRxWEPFail.setStatus("current")
_RuckusRadioStatsRxDecryptCRCError_Type = Counter32
_RuckusRadioStatsRxDecryptCRCError_Object = MibTableColumn
ruckusRadioStatsRxDecryptCRCError = _RuckusRadioStatsRxDecryptCRCError_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 19),
    _RuckusRadioStatsRxDecryptCRCError_Type()
)
ruckusRadioStatsRxDecryptCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsRxDecryptCRCError.setStatus("current")
_RuckusRadioStatsRxMICError_Type = Counter32
_RuckusRadioStatsRxMICError_Object = MibTableColumn
ruckusRadioStatsRxMICError = _RuckusRadioStatsRxMICError_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 20),
    _RuckusRadioStatsRxMICError_Type()
)
ruckusRadioStatsRxMICError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsRxMICError.setStatus("current")
_RuckusRadioStatsRxErrors_Type = Counter32
_RuckusRadioStatsRxErrors_Object = MibTableColumn
ruckusRadioStatsRxErrors = _RuckusRadioStatsRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 21),
    _RuckusRadioStatsRxErrors_Type()
)
ruckusRadioStatsRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsRxErrors.setStatus("current")
_RuckusRadioStatsTxBytes_Type = Counter32
_RuckusRadioStatsTxBytes_Object = MibTableColumn
ruckusRadioStatsTxBytes = _RuckusRadioStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 22),
    _RuckusRadioStatsTxBytes_Type()
)
ruckusRadioStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsTxBytes.setStatus("current")
_RuckusRadioStatsTxFrames_Type = Counter32
_RuckusRadioStatsTxFrames_Object = MibTableColumn
ruckusRadioStatsTxFrames = _RuckusRadioStatsTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 23),
    _RuckusRadioStatsTxFrames_Type()
)
ruckusRadioStatsTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusRadioStatsTxFrames.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-RADIO-MIB",
    **{"ruckusRadioMIB": ruckusRadioMIB,
       "ruckusRadioObjects": ruckusRadioObjects,
       "ruckusRadioInfo": ruckusRadioInfo,
       "ruckusRadioNumber": ruckusRadioNumber,
       "ruckusRadioTable": ruckusRadioTable,
       "ruckusRadioEntry": ruckusRadioEntry,
       "ruckusRadioMode": ruckusRadioMode,
       "ruckusRadioCountry": ruckusRadioCountry,
       "ruckusRadioBSSType": ruckusRadioBSSType,
       "ruckusRadioChannel": ruckusRadioChannel,
       "ruckusRadioDataRate": ruckusRadioDataRate,
       "ruckusRadioTxPower": ruckusRadioTxPower,
       "ruckusRadioProtectionMode": ruckusRadioProtectionMode,
       "ruckusRadioStatsTable": ruckusRadioStatsTable,
       "ruckusRadioStatsEntry": ruckusRadioStatsEntry,
       "ruckusRadioStatsMaxSta": ruckusRadioStatsMaxSta,
       "ruckusRadioStatsNumSta": ruckusRadioStatsNumSta,
       "ruckusRadioStatsNumAuthSta": ruckusRadioStatsNumAuthSta,
       "ruckusRadioStatsNumAuthReq": ruckusRadioStatsNumAuthReq,
       "ruckusRadioStatsNumAuthResp": ruckusRadioStatsNumAuthResp,
       "ruckusRadioStatsNumAuthSuccess": ruckusRadioStatsNumAuthSuccess,
       "ruckusRadioStatsNumAuthFail": ruckusRadioStatsNumAuthFail,
       "ruckusRadioStatsNumAssocReq": ruckusRadioStatsNumAssocReq,
       "ruckusRadioStatsNumAssocResp": ruckusRadioStatsNumAssocResp,
       "ruckusRadioStatsNumAssocSuccess": ruckusRadioStatsNumAssocSuccess,
       "ruckusRadioStatsNumAssocFail": ruckusRadioStatsNumAssocFail,
       "ruckusRadioStatsAssocFailRate": ruckusRadioStatsAssocFailRate,
       "ruckusRadioStatsAuthFailRate": ruckusRadioStatsAuthFailRate,
       "ruckusRadioStatsAssocSuccessRate": ruckusRadioStatsAssocSuccessRate,
       "ruckusRadioStatsResourceUtil": ruckusRadioStatsResourceUtil,
       "ruckusRadioStatsRxBytes": ruckusRadioStatsRxBytes,
       "ruckusRadioStatsRxFrames": ruckusRadioStatsRxFrames,
       "ruckusRadioStatsRxWEPFail": ruckusRadioStatsRxWEPFail,
       "ruckusRadioStatsRxDecryptCRCError": ruckusRadioStatsRxDecryptCRCError,
       "ruckusRadioStatsRxMICError": ruckusRadioStatsRxMICError,
       "ruckusRadioStatsRxErrors": ruckusRadioStatsRxErrors,
       "ruckusRadioStatsTxBytes": ruckusRadioStatsTxBytes,
       "ruckusRadioStatsTxFrames": ruckusRadioStatsTxFrames}
)
