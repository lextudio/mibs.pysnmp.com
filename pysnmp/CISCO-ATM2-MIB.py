# SNMP MIB module (CISCO-ATM2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:10 2024
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

(atmInterfaceConfEntry,) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmInterfaceConfEntry")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoAtm2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 23)
)
ciscoAtm2MIB.setRevisions(
        ("1998-03-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ciscoatm2MIBObjects_ObjectIdentity = ObjectIdentity
ciscoatm2MIBObjects = _Ciscoatm2MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1)
)
_CiscoatmSigStatTable_Object = MibTable
ciscoatmSigStatTable = _CiscoatmSigStatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoatmSigStatTable.setStatus("current")
_CiscoatmSigStatEntry_Object = MibTableRow
ciscoatmSigStatEntry = _CiscoatmSigStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1)
)
ciscoatmSigStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ciscoatmSigStatEntry.setStatus("current")
_CiscoatmSigSSCOPConEvents_Type = Counter32
_CiscoatmSigSSCOPConEvents_Object = MibTableColumn
ciscoatmSigSSCOPConEvents = _CiscoatmSigSSCOPConEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 5),
    _CiscoatmSigSSCOPConEvents_Type()
)
ciscoatmSigSSCOPConEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmSigSSCOPConEvents.setStatus("current")
_CiscoatmSigSSCOPErrdPdus_Type = Counter32
_CiscoatmSigSSCOPErrdPdus_Object = MibTableColumn
ciscoatmSigSSCOPErrdPdus = _CiscoatmSigSSCOPErrdPdus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 6),
    _CiscoatmSigSSCOPErrdPdus_Type()
)
ciscoatmSigSSCOPErrdPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmSigSSCOPErrdPdus.setStatus("current")
_CiscoatmSigDetectSetupAttempts_Type = Counter32
_CiscoatmSigDetectSetupAttempts_Object = MibTableColumn
ciscoatmSigDetectSetupAttempts = _CiscoatmSigDetectSetupAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 7),
    _CiscoatmSigDetectSetupAttempts_Type()
)
ciscoatmSigDetectSetupAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmSigDetectSetupAttempts.setStatus("current")
_CiscoatmSigEmitSetupAttempts_Type = Counter32
_CiscoatmSigEmitSetupAttempts_Object = MibTableColumn
ciscoatmSigEmitSetupAttempts = _CiscoatmSigEmitSetupAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 8),
    _CiscoatmSigEmitSetupAttempts_Type()
)
ciscoatmSigEmitSetupAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmSigEmitSetupAttempts.setStatus("current")
_CiscoatmSigDetectUnavailRoutes_Type = Counter32
_CiscoatmSigDetectUnavailRoutes_Object = MibTableColumn
ciscoatmSigDetectUnavailRoutes = _CiscoatmSigDetectUnavailRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 9),
    _CiscoatmSigDetectUnavailRoutes_Type()
)
ciscoatmSigDetectUnavailRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmSigDetectUnavailRoutes.setStatus("current")
_CiscoatmSigEmitUnavailRoutes_Type = Counter32
_CiscoatmSigEmitUnavailRoutes_Object = MibTableColumn
ciscoatmSigEmitUnavailRoutes = _CiscoatmSigEmitUnavailRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 10),
    _CiscoatmSigEmitUnavailRoutes_Type()
)
ciscoatmSigEmitUnavailRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmSigEmitUnavailRoutes.setStatus("current")
_CiscoatmSigDetectUnavailResrcs_Type = Counter32
_CiscoatmSigDetectUnavailResrcs_Object = MibTableColumn
ciscoatmSigDetectUnavailResrcs = _CiscoatmSigDetectUnavailResrcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 11),
    _CiscoatmSigDetectUnavailResrcs_Type()
)
ciscoatmSigDetectUnavailResrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmSigDetectUnavailResrcs.setStatus("current")
_CiscoatmSigEmitUnavailResrcs_Type = Counter32
_CiscoatmSigEmitUnavailResrcs_Object = MibTableColumn
ciscoatmSigEmitUnavailResrcs = _CiscoatmSigEmitUnavailResrcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 12),
    _CiscoatmSigEmitUnavailResrcs_Type()
)
ciscoatmSigEmitUnavailResrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmSigEmitUnavailResrcs.setStatus("current")
_CiscoatmSigDetectCldPtyEvents_Type = Counter32
_CiscoatmSigDetectCldPtyEvents_Object = MibTableColumn
ciscoatmSigDetectCldPtyEvents = _CiscoatmSigDetectCldPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 13),
    _CiscoatmSigDetectCldPtyEvents_Type()
)
ciscoatmSigDetectCldPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmSigDetectCldPtyEvents.setStatus("current")
_CiscoatmSigEmitCldPtyEvents_Type = Counter32
_CiscoatmSigEmitCldPtyEvents_Object = MibTableColumn
ciscoatmSigEmitCldPtyEvents = _CiscoatmSigEmitCldPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 14),
    _CiscoatmSigEmitCldPtyEvents_Type()
)
ciscoatmSigEmitCldPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmSigEmitCldPtyEvents.setStatus("current")
_CiscoatmSigDetectMsgErrors_Type = Counter32
_CiscoatmSigDetectMsgErrors_Object = MibTableColumn
ciscoatmSigDetectMsgErrors = _CiscoatmSigDetectMsgErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 15),
    _CiscoatmSigDetectMsgErrors_Type()
)
ciscoatmSigDetectMsgErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmSigDetectMsgErrors.setStatus("current")
_CiscoatmSigEmitMsgErrors_Type = Counter32
_CiscoatmSigEmitMsgErrors_Object = MibTableColumn
ciscoatmSigEmitMsgErrors = _CiscoatmSigEmitMsgErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 16),
    _CiscoatmSigEmitMsgErrors_Type()
)
ciscoatmSigEmitMsgErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmSigEmitMsgErrors.setStatus("current")
_CiscoatmSigDetectClgPtyEvents_Type = Counter32
_CiscoatmSigDetectClgPtyEvents_Object = MibTableColumn
ciscoatmSigDetectClgPtyEvents = _CiscoatmSigDetectClgPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 17),
    _CiscoatmSigDetectClgPtyEvents_Type()
)
ciscoatmSigDetectClgPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmSigDetectClgPtyEvents.setStatus("current")
_CiscoatmSigEmitClgPtyEvents_Type = Counter32
_CiscoatmSigEmitClgPtyEvents_Object = MibTableColumn
ciscoatmSigEmitClgPtyEvents = _CiscoatmSigEmitClgPtyEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 18),
    _CiscoatmSigEmitClgPtyEvents_Type()
)
ciscoatmSigEmitClgPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmSigEmitClgPtyEvents.setStatus("current")
_CiscoatmSigDetectTimerExpireds_Type = Counter32
_CiscoatmSigDetectTimerExpireds_Object = MibTableColumn
ciscoatmSigDetectTimerExpireds = _CiscoatmSigDetectTimerExpireds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 19),
    _CiscoatmSigDetectTimerExpireds_Type()
)
ciscoatmSigDetectTimerExpireds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmSigDetectTimerExpireds.setStatus("current")
_CiscoatmSigEmitTimerExpireds_Type = Counter32
_CiscoatmSigEmitTimerExpireds_Object = MibTableColumn
ciscoatmSigEmitTimerExpireds = _CiscoatmSigEmitTimerExpireds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 20),
    _CiscoatmSigEmitTimerExpireds_Type()
)
ciscoatmSigEmitTimerExpireds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmSigEmitTimerExpireds.setStatus("current")
_CiscoatmSigDetectRestarts_Type = Counter32
_CiscoatmSigDetectRestarts_Object = MibTableColumn
ciscoatmSigDetectRestarts = _CiscoatmSigDetectRestarts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 21),
    _CiscoatmSigDetectRestarts_Type()
)
ciscoatmSigDetectRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmSigDetectRestarts.setStatus("current")
_CiscoatmSigEmitRestarts_Type = Counter32
_CiscoatmSigEmitRestarts_Object = MibTableColumn
ciscoatmSigEmitRestarts = _CiscoatmSigEmitRestarts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 22),
    _CiscoatmSigEmitRestarts_Type()
)
ciscoatmSigEmitRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmSigEmitRestarts.setStatus("current")
_CiscoatmSigInEstabls_Type = Counter32
_CiscoatmSigInEstabls_Object = MibTableColumn
ciscoatmSigInEstabls = _CiscoatmSigInEstabls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 23),
    _CiscoatmSigInEstabls_Type()
)
ciscoatmSigInEstabls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmSigInEstabls.setStatus("current")
_CiscoatmSigOutEstabls_Type = Counter32
_CiscoatmSigOutEstabls_Object = MibTableColumn
ciscoatmSigOutEstabls = _CiscoatmSigOutEstabls_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 1, 1, 24),
    _CiscoatmSigOutEstabls_Type()
)
ciscoatmSigOutEstabls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmSigOutEstabls.setStatus("current")
_CiscoatmSigSupportTable_Object = MibTable
ciscoatmSigSupportTable = _CiscoatmSigSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoatmSigSupportTable.setStatus("current")
_CiscoatmSigSupportEntry_Object = MibTableRow
ciscoatmSigSupportEntry = _CiscoatmSigSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 2, 1)
)
ciscoatmSigSupportEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ciscoatmSigSupportEntry.setStatus("current")


class _CiscoatmSigSupportClgPtyNumDel_Type(Integer32):
    """Custom type ciscoatmSigSupportClgPtyNumDel based on Integer32"""
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


_CiscoatmSigSupportClgPtyNumDel_Type.__name__ = "Integer32"
_CiscoatmSigSupportClgPtyNumDel_Object = MibTableColumn
ciscoatmSigSupportClgPtyNumDel = _CiscoatmSigSupportClgPtyNumDel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 2, 1, 1),
    _CiscoatmSigSupportClgPtyNumDel_Type()
)
ciscoatmSigSupportClgPtyNumDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoatmSigSupportClgPtyNumDel.setStatus("current")


class _CiscoatmSigSupportClgPtySubAddr_Type(Integer32):
    """Custom type ciscoatmSigSupportClgPtySubAddr based on Integer32"""
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


_CiscoatmSigSupportClgPtySubAddr_Type.__name__ = "Integer32"
_CiscoatmSigSupportClgPtySubAddr_Object = MibTableColumn
ciscoatmSigSupportClgPtySubAddr = _CiscoatmSigSupportClgPtySubAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 2, 1, 2),
    _CiscoatmSigSupportClgPtySubAddr_Type()
)
ciscoatmSigSupportClgPtySubAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoatmSigSupportClgPtySubAddr.setStatus("current")


class _CiscoatmSigSupportCldPtySubAddr_Type(Integer32):
    """Custom type ciscoatmSigSupportCldPtySubAddr based on Integer32"""
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


_CiscoatmSigSupportCldPtySubAddr_Type.__name__ = "Integer32"
_CiscoatmSigSupportCldPtySubAddr_Object = MibTableColumn
ciscoatmSigSupportCldPtySubAddr = _CiscoatmSigSupportCldPtySubAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 2, 1, 3),
    _CiscoatmSigSupportCldPtySubAddr_Type()
)
ciscoatmSigSupportCldPtySubAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoatmSigSupportCldPtySubAddr.setStatus("current")


class _CiscoatmSigSupportHiLyrInfo_Type(Integer32):
    """Custom type ciscoatmSigSupportHiLyrInfo based on Integer32"""
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


_CiscoatmSigSupportHiLyrInfo_Type.__name__ = "Integer32"
_CiscoatmSigSupportHiLyrInfo_Object = MibTableColumn
ciscoatmSigSupportHiLyrInfo = _CiscoatmSigSupportHiLyrInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 2, 1, 4),
    _CiscoatmSigSupportHiLyrInfo_Type()
)
ciscoatmSigSupportHiLyrInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoatmSigSupportHiLyrInfo.setStatus("current")


class _CiscoatmSigSupportLoLyrInfo_Type(Integer32):
    """Custom type ciscoatmSigSupportLoLyrInfo based on Integer32"""
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


_CiscoatmSigSupportLoLyrInfo_Type.__name__ = "Integer32"
_CiscoatmSigSupportLoLyrInfo_Object = MibTableColumn
ciscoatmSigSupportLoLyrInfo = _CiscoatmSigSupportLoLyrInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 2, 1, 5),
    _CiscoatmSigSupportLoLyrInfo_Type()
)
ciscoatmSigSupportLoLyrInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoatmSigSupportLoLyrInfo.setStatus("current")


class _CiscoatmSigSupportBlliRepeatInd_Type(Integer32):
    """Custom type ciscoatmSigSupportBlliRepeatInd based on Integer32"""
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


_CiscoatmSigSupportBlliRepeatInd_Type.__name__ = "Integer32"
_CiscoatmSigSupportBlliRepeatInd_Object = MibTableColumn
ciscoatmSigSupportBlliRepeatInd = _CiscoatmSigSupportBlliRepeatInd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 2, 1, 6),
    _CiscoatmSigSupportBlliRepeatInd_Type()
)
ciscoatmSigSupportBlliRepeatInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoatmSigSupportBlliRepeatInd.setStatus("current")


class _CiscoatmSigSupportAALInfo_Type(Integer32):
    """Custom type ciscoatmSigSupportAALInfo based on Integer32"""
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


_CiscoatmSigSupportAALInfo_Type.__name__ = "Integer32"
_CiscoatmSigSupportAALInfo_Object = MibTableColumn
ciscoatmSigSupportAALInfo = _CiscoatmSigSupportAALInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 2, 1, 7),
    _CiscoatmSigSupportAALInfo_Type()
)
ciscoatmSigSupportAALInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoatmSigSupportAALInfo.setStatus("current")


class _CiscoatmSigSupportUnknownIe_Type(Integer32):
    """Custom type ciscoatmSigSupportUnknownIe based on Integer32"""
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


_CiscoatmSigSupportUnknownIe_Type.__name__ = "Integer32"
_CiscoatmSigSupportUnknownIe_Object = MibTableColumn
ciscoatmSigSupportUnknownIe = _CiscoatmSigSupportUnknownIe_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 2, 1, 8),
    _CiscoatmSigSupportUnknownIe_Type()
)
ciscoatmSigSupportUnknownIe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoatmSigSupportUnknownIe.setStatus("current")
_CiscoatmInterfaceExtTable_Object = MibTable
ciscoatmInterfaceExtTable = _CiscoatmInterfaceExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoatmInterfaceExtTable.setStatus("current")
_CiscoatmInterfaceExtEntry_Object = MibTableRow
ciscoatmInterfaceExtEntry = _CiscoatmInterfaceExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ciscoatmInterfaceExtEntry.setStatus("current")


class _CiscoatmInterfaceConfMaxSvpcVpi_Type(Integer32):
    """Custom type ciscoatmInterfaceConfMaxSvpcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiscoatmInterfaceConfMaxSvpcVpi_Type.__name__ = "Integer32"
_CiscoatmInterfaceConfMaxSvpcVpi_Object = MibTableColumn
ciscoatmInterfaceConfMaxSvpcVpi = _CiscoatmInterfaceConfMaxSvpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 3, 1, 16),
    _CiscoatmInterfaceConfMaxSvpcVpi_Type()
)
ciscoatmInterfaceConfMaxSvpcVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoatmInterfaceConfMaxSvpcVpi.setStatus("current")


class _CiscoatmInterfaceCurrentMaxSvpcVpi_Type(Integer32):
    """Custom type ciscoatmInterfaceCurrentMaxSvpcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiscoatmInterfaceCurrentMaxSvpcVpi_Type.__name__ = "Integer32"
_CiscoatmInterfaceCurrentMaxSvpcVpi_Object = MibTableColumn
ciscoatmInterfaceCurrentMaxSvpcVpi = _CiscoatmInterfaceCurrentMaxSvpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 3, 1, 17),
    _CiscoatmInterfaceCurrentMaxSvpcVpi_Type()
)
ciscoatmInterfaceCurrentMaxSvpcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmInterfaceCurrentMaxSvpcVpi.setStatus("current")


class _CiscoatmInterfaceConfMaxSvccVpi_Type(Integer32):
    """Custom type ciscoatmInterfaceConfMaxSvccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiscoatmInterfaceConfMaxSvccVpi_Type.__name__ = "Integer32"
_CiscoatmInterfaceConfMaxSvccVpi_Object = MibTableColumn
ciscoatmInterfaceConfMaxSvccVpi = _CiscoatmInterfaceConfMaxSvccVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 3, 1, 18),
    _CiscoatmInterfaceConfMaxSvccVpi_Type()
)
ciscoatmInterfaceConfMaxSvccVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoatmInterfaceConfMaxSvccVpi.setStatus("current")


class _CiscoatmInterfaceCurrentMaxSvccVpi_Type(Integer32):
    """Custom type ciscoatmInterfaceCurrentMaxSvccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiscoatmInterfaceCurrentMaxSvccVpi_Type.__name__ = "Integer32"
_CiscoatmInterfaceCurrentMaxSvccVpi_Object = MibTableColumn
ciscoatmInterfaceCurrentMaxSvccVpi = _CiscoatmInterfaceCurrentMaxSvccVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 3, 1, 19),
    _CiscoatmInterfaceCurrentMaxSvccVpi_Type()
)
ciscoatmInterfaceCurrentMaxSvccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmInterfaceCurrentMaxSvccVpi.setStatus("current")


class _CiscoatmInterfaceConfMinSvccVci_Type(Integer32):
    """Custom type ciscoatmInterfaceConfMinSvccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 4095),
    )


_CiscoatmInterfaceConfMinSvccVci_Type.__name__ = "Integer32"
_CiscoatmInterfaceConfMinSvccVci_Object = MibTableColumn
ciscoatmInterfaceConfMinSvccVci = _CiscoatmInterfaceConfMinSvccVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 3, 1, 20),
    _CiscoatmInterfaceConfMinSvccVci_Type()
)
ciscoatmInterfaceConfMinSvccVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoatmInterfaceConfMinSvccVci.setStatus("current")


class _CiscoatmInterfaceCurrentMinSvccVci_Type(Integer32):
    """Custom type ciscoatmInterfaceCurrentMinSvccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 4095),
    )


_CiscoatmInterfaceCurrentMinSvccVci_Type.__name__ = "Integer32"
_CiscoatmInterfaceCurrentMinSvccVci_Object = MibTableColumn
ciscoatmInterfaceCurrentMinSvccVci = _CiscoatmInterfaceCurrentMinSvccVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 1, 3, 1, 21),
    _CiscoatmInterfaceCurrentMinSvccVci_Type()
)
ciscoatmInterfaceCurrentMinSvccVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoatmInterfaceCurrentMinSvccVci.setStatus("current")
_Ciscoatm2MIBConformance_ObjectIdentity = ObjectIdentity
ciscoatm2MIBConformance = _Ciscoatm2MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 3)
)
_Ciscoatm2MIBGroups_ObjectIdentity = ObjectIdentity
ciscoatm2MIBGroups = _Ciscoatm2MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 3, 1)
)
_Ciscoatm2MIBCompliances_ObjectIdentity = ObjectIdentity
ciscoatm2MIBCompliances = _Ciscoatm2MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 3, 2)
)
atmInterfaceConfEntry.registerAugmentions(
    ("CISCO-ATM2-MIB",
     "ciscoatmInterfaceExtEntry")
)
ciscoatmInterfaceExtEntry.setIndexNames(*atmInterfaceConfEntry.getIndexNames())

# Managed Objects groups

ciscoAtmSwitchServcHostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 3, 1, 1)
)
ciscoAtmSwitchServcHostGroup.setObjects(
      *(("CISCO-ATM2-MIB", "ciscoatmSigSSCOPConEvents"),
        ("CISCO-ATM2-MIB", "ciscoatmSigSSCOPErrdPdus"),
        ("CISCO-ATM2-MIB", "ciscoatmSigDetectSetupAttempts"),
        ("CISCO-ATM2-MIB", "ciscoatmSigEmitSetupAttempts"),
        ("CISCO-ATM2-MIB", "ciscoatmSigDetectUnavailRoutes"),
        ("CISCO-ATM2-MIB", "ciscoatmSigEmitUnavailRoutes"),
        ("CISCO-ATM2-MIB", "ciscoatmSigDetectUnavailResrcs"),
        ("CISCO-ATM2-MIB", "ciscoatmSigEmitUnavailResrcs"),
        ("CISCO-ATM2-MIB", "ciscoatmSigDetectCldPtyEvents"),
        ("CISCO-ATM2-MIB", "ciscoatmSigEmitCldPtyEvents"),
        ("CISCO-ATM2-MIB", "ciscoatmSigDetectMsgErrors"),
        ("CISCO-ATM2-MIB", "ciscoatmSigEmitMsgErrors"),
        ("CISCO-ATM2-MIB", "ciscoatmSigDetectClgPtyEvents"),
        ("CISCO-ATM2-MIB", "ciscoatmSigEmitClgPtyEvents"),
        ("CISCO-ATM2-MIB", "ciscoatmSigDetectTimerExpireds"),
        ("CISCO-ATM2-MIB", "ciscoatmSigEmitTimerExpireds"),
        ("CISCO-ATM2-MIB", "ciscoatmSigDetectRestarts"),
        ("CISCO-ATM2-MIB", "ciscoatmSigEmitRestarts"),
        ("CISCO-ATM2-MIB", "ciscoatmSigInEstabls"),
        ("CISCO-ATM2-MIB", "ciscoatmSigOutEstabls"))
)
if mibBuilder.loadTexts:
    ciscoAtmSwitchServcHostGroup.setStatus("current")

ciscoAtmSwitchServcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 3, 1, 3)
)
ciscoAtmSwitchServcGroup.setObjects(
      *(("CISCO-ATM2-MIB", "ciscoatmSigSupportClgPtyNumDel"),
        ("CISCO-ATM2-MIB", "ciscoatmSigSupportClgPtySubAddr"),
        ("CISCO-ATM2-MIB", "ciscoatmSigSupportCldPtySubAddr"),
        ("CISCO-ATM2-MIB", "ciscoatmSigSupportHiLyrInfo"),
        ("CISCO-ATM2-MIB", "ciscoatmSigSupportLoLyrInfo"),
        ("CISCO-ATM2-MIB", "ciscoatmSigSupportBlliRepeatInd"),
        ("CISCO-ATM2-MIB", "ciscoatmSigSupportAALInfo"),
        ("CISCO-ATM2-MIB", "ciscoatmSigSupportUnknownIe"))
)
if mibBuilder.loadTexts:
    ciscoAtmSwitchServcGroup.setStatus("current")

ciscoAtmSwitchServcHostGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 3, 1, 4)
)
ciscoAtmSwitchServcHostGroup2.setObjects(
      *(("CISCO-ATM2-MIB", "ciscoatmInterfaceConfMaxSvpcVpi"),
        ("CISCO-ATM2-MIB", "ciscoatmInterfaceCurrentMaxSvpcVpi"),
        ("CISCO-ATM2-MIB", "ciscoatmInterfaceConfMaxSvccVpi"),
        ("CISCO-ATM2-MIB", "ciscoatmInterfaceCurrentMaxSvccVpi"),
        ("CISCO-ATM2-MIB", "ciscoatmInterfaceConfMinSvccVci"),
        ("CISCO-ATM2-MIB", "ciscoatmInterfaceCurrentMinSvccVci"))
)
if mibBuilder.loadTexts:
    ciscoAtmSwitchServcHostGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoatm2MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoatm2MIBCompliance.setStatus(
        "obsolete"
    )

ciscoatm2MIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 23, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ciscoatm2MIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM2-MIB",
    **{"ciscoAtm2MIB": ciscoAtm2MIB,
       "ciscoatm2MIBObjects": ciscoatm2MIBObjects,
       "ciscoatmSigStatTable": ciscoatmSigStatTable,
       "ciscoatmSigStatEntry": ciscoatmSigStatEntry,
       "ciscoatmSigSSCOPConEvents": ciscoatmSigSSCOPConEvents,
       "ciscoatmSigSSCOPErrdPdus": ciscoatmSigSSCOPErrdPdus,
       "ciscoatmSigDetectSetupAttempts": ciscoatmSigDetectSetupAttempts,
       "ciscoatmSigEmitSetupAttempts": ciscoatmSigEmitSetupAttempts,
       "ciscoatmSigDetectUnavailRoutes": ciscoatmSigDetectUnavailRoutes,
       "ciscoatmSigEmitUnavailRoutes": ciscoatmSigEmitUnavailRoutes,
       "ciscoatmSigDetectUnavailResrcs": ciscoatmSigDetectUnavailResrcs,
       "ciscoatmSigEmitUnavailResrcs": ciscoatmSigEmitUnavailResrcs,
       "ciscoatmSigDetectCldPtyEvents": ciscoatmSigDetectCldPtyEvents,
       "ciscoatmSigEmitCldPtyEvents": ciscoatmSigEmitCldPtyEvents,
       "ciscoatmSigDetectMsgErrors": ciscoatmSigDetectMsgErrors,
       "ciscoatmSigEmitMsgErrors": ciscoatmSigEmitMsgErrors,
       "ciscoatmSigDetectClgPtyEvents": ciscoatmSigDetectClgPtyEvents,
       "ciscoatmSigEmitClgPtyEvents": ciscoatmSigEmitClgPtyEvents,
       "ciscoatmSigDetectTimerExpireds": ciscoatmSigDetectTimerExpireds,
       "ciscoatmSigEmitTimerExpireds": ciscoatmSigEmitTimerExpireds,
       "ciscoatmSigDetectRestarts": ciscoatmSigDetectRestarts,
       "ciscoatmSigEmitRestarts": ciscoatmSigEmitRestarts,
       "ciscoatmSigInEstabls": ciscoatmSigInEstabls,
       "ciscoatmSigOutEstabls": ciscoatmSigOutEstabls,
       "ciscoatmSigSupportTable": ciscoatmSigSupportTable,
       "ciscoatmSigSupportEntry": ciscoatmSigSupportEntry,
       "ciscoatmSigSupportClgPtyNumDel": ciscoatmSigSupportClgPtyNumDel,
       "ciscoatmSigSupportClgPtySubAddr": ciscoatmSigSupportClgPtySubAddr,
       "ciscoatmSigSupportCldPtySubAddr": ciscoatmSigSupportCldPtySubAddr,
       "ciscoatmSigSupportHiLyrInfo": ciscoatmSigSupportHiLyrInfo,
       "ciscoatmSigSupportLoLyrInfo": ciscoatmSigSupportLoLyrInfo,
       "ciscoatmSigSupportBlliRepeatInd": ciscoatmSigSupportBlliRepeatInd,
       "ciscoatmSigSupportAALInfo": ciscoatmSigSupportAALInfo,
       "ciscoatmSigSupportUnknownIe": ciscoatmSigSupportUnknownIe,
       "ciscoatmInterfaceExtTable": ciscoatmInterfaceExtTable,
       "ciscoatmInterfaceExtEntry": ciscoatmInterfaceExtEntry,
       "ciscoatmInterfaceConfMaxSvpcVpi": ciscoatmInterfaceConfMaxSvpcVpi,
       "ciscoatmInterfaceCurrentMaxSvpcVpi": ciscoatmInterfaceCurrentMaxSvpcVpi,
       "ciscoatmInterfaceConfMaxSvccVpi": ciscoatmInterfaceConfMaxSvccVpi,
       "ciscoatmInterfaceCurrentMaxSvccVpi": ciscoatmInterfaceCurrentMaxSvccVpi,
       "ciscoatmInterfaceConfMinSvccVci": ciscoatmInterfaceConfMinSvccVci,
       "ciscoatmInterfaceCurrentMinSvccVci": ciscoatmInterfaceCurrentMinSvccVci,
       "ciscoatm2MIBConformance": ciscoatm2MIBConformance,
       "ciscoatm2MIBGroups": ciscoatm2MIBGroups,
       "ciscoAtmSwitchServcHostGroup": ciscoAtmSwitchServcHostGroup,
       "ciscoAtmSwitchServcGroup": ciscoAtmSwitchServcGroup,
       "ciscoAtmSwitchServcHostGroup2": ciscoAtmSwitchServcHostGroup2,
       "ciscoatm2MIBCompliances": ciscoatm2MIBCompliances,
       "ciscoatm2MIBCompliance": ciscoatm2MIBCompliance,
       "ciscoatm2MIBCompliance2": ciscoatm2MIBCompliance2}
)
