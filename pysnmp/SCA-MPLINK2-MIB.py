# SNMP MIB module (SCA-MPLINK2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCA-MPLINK2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:55 2024
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

(scanet,) = mibBuilder.importSymbols(
    "SCANET-MIB",
    "scanet")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class OnOff(Integer32):
    """Custom type OnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )





class Attachment(Integer32):
    """Custom type Attachment based on Integer32"""
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
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("aui", 3),
          ("eia530-dce", 8),
          ("eia530-dte", 14),
          ("empty", 19),
          ("id0", 4),
          ("id1", 5),
          ("id2", 6),
          ("id3", 7),
          ("isdn", 20),
          ("isdn-e1-bnc", 23),
          ("isdn-e1-rj45", 22),
          ("isdn-t1-rj45", 24),
          ("none", 1),
          ("pcmcia-async", 21),
          ("tenbase-t", 2),
          ("test-plug", 9),
          ("v11-dce", 10),
          ("v11-dte", 15),
          ("v24-dce", 11),
          ("v24-dte", 16),
          ("v35-dce", 12),
          ("v35-dte", 17),
          ("v36-dce", 13),
          ("v36-dte", 18))
    )





class CompType(Integer32):
    """Custom type CompType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("proprietary", 1),
          ("stac", 2))
    )





class Direction(Integer32):
    """Custom type Direction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 2),
          ("outgoing", 3),
          ("unknown", 1))
    )





class DataState(Integer32):
    """Custom type DataState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("timeCut", 2),
          ("up", 3))
    )





class ConnectState(Integer32):
    """Custom type ConnectState based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("destroy", 9),
          ("down", 2),
          ("empty", 13),
          ("error", 8),
          ("idle", 11),
          ("incomingCall", 4),
          ("incomingDisconnect", 5),
          ("outgoingCall", 3),
          ("outgoingDisconnect", 6),
          ("timeCut", 10),
          ("up", 12),
          ("waitDisconnectConfirm", 7))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mplk2_ObjectIdentity = ObjectIdentity
mplk2 = _Mplk2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 44)
)
_Mpl2Service_ObjectIdentity = ObjectIdentity
mpl2Service = _Mpl2Service_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 44, 1)
)
_Mpl2ServiceTable_Object = MibTable
mpl2ServiceTable = _Mpl2ServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 1, 1)
)
if mibBuilder.loadTexts:
    mpl2ServiceTable.setStatus("mandatory")
_Mpl2ServiceEntry_Object = MibTableRow
mpl2ServiceEntry = _Mpl2ServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 1, 1, 1)
)
mpl2ServiceEntry.setIndexNames(
    (0, "SCA-MPLINK2-MIB", "mpl2ServiceNumber"),
)
if mibBuilder.loadTexts:
    mpl2ServiceEntry.setStatus("mandatory")
_Mpl2ServiceNumber_Type = Integer32
_Mpl2ServiceNumber_Object = MibTableColumn
mpl2ServiceNumber = _Mpl2ServiceNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 1, 1, 1, 1),
    _Mpl2ServiceNumber_Type()
)
mpl2ServiceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2ServiceNumber.setStatus("mandatory")
_Mpl2ServiceSlotNumber_Type = Integer32
_Mpl2ServiceSlotNumber_Object = MibTableColumn
mpl2ServiceSlotNumber = _Mpl2ServiceSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 1, 1, 1, 2),
    _Mpl2ServiceSlotNumber_Type()
)
mpl2ServiceSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2ServiceSlotNumber.setStatus("mandatory")
_Mpl2ServicePlugNumber_Type = Integer32
_Mpl2ServicePlugNumber_Object = MibTableColumn
mpl2ServicePlugNumber = _Mpl2ServicePlugNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 1, 1, 1, 3),
    _Mpl2ServicePlugNumber_Type()
)
mpl2ServicePlugNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2ServicePlugNumber.setStatus("mandatory")


class _Mpl2ServicePlugName_Type(DisplayString):
    """Custom type mpl2ServicePlugName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_Mpl2ServicePlugName_Type.__name__ = "DisplayString"
_Mpl2ServicePlugName_Object = MibTableColumn
mpl2ServicePlugName = _Mpl2ServicePlugName_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 1, 1, 1, 4),
    _Mpl2ServicePlugName_Type()
)
mpl2ServicePlugName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2ServicePlugName.setStatus("mandatory")
_Mpl2ServiceAttachment_Type = Attachment
_Mpl2ServiceAttachment_Object = MibTableColumn
mpl2ServiceAttachment = _Mpl2ServiceAttachment_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 1, 1, 1, 5),
    _Mpl2ServiceAttachment_Type()
)
mpl2ServiceAttachment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2ServiceAttachment.setStatus("mandatory")


class _Mpl2ServiceProvider_Type(Integer32):
    """Custom type mpl2ServiceProvider based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("frAttachment", 5),
          ("frHdlc", 4),
          ("isdnAttachment", 8),
          ("lan", 1),
          ("lapbHdlc", 2),
          ("lapbIsdn", 6),
          ("pppHdlc", 3),
          ("pppIsdn", 7),
          ("pppMultiMaster", 12),
          ("pppPcmciaModem", 16),
          ("slip", 11),
          ("x25Attachment", 10),
          ("x25Lapb", 9))
    )


_Mpl2ServiceProvider_Type.__name__ = "Integer32"
_Mpl2ServiceProvider_Object = MibTableColumn
mpl2ServiceProvider = _Mpl2ServiceProvider_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 1, 1, 1, 6),
    _Mpl2ServiceProvider_Type()
)
mpl2ServiceProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2ServiceProvider.setStatus("mandatory")
_Mpl2ServiceBytesSentUpper_Type = Counter32
_Mpl2ServiceBytesSentUpper_Object = MibTableColumn
mpl2ServiceBytesSentUpper = _Mpl2ServiceBytesSentUpper_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 1, 1, 1, 7),
    _Mpl2ServiceBytesSentUpper_Type()
)
mpl2ServiceBytesSentUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2ServiceBytesSentUpper.setStatus("mandatory")
_Mpl2ServiceBytesSentLower_Type = Counter32
_Mpl2ServiceBytesSentLower_Object = MibTableColumn
mpl2ServiceBytesSentLower = _Mpl2ServiceBytesSentLower_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 1, 1, 1, 8),
    _Mpl2ServiceBytesSentLower_Type()
)
mpl2ServiceBytesSentLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2ServiceBytesSentLower.setStatus("mandatory")
_Mpl2ServiceBytesReceivedUpper_Type = Counter32
_Mpl2ServiceBytesReceivedUpper_Object = MibTableColumn
mpl2ServiceBytesReceivedUpper = _Mpl2ServiceBytesReceivedUpper_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 1, 1, 1, 9),
    _Mpl2ServiceBytesReceivedUpper_Type()
)
mpl2ServiceBytesReceivedUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2ServiceBytesReceivedUpper.setStatus("mandatory")
_Mpl2ServiceBytesReceivedLower_Type = Counter32
_Mpl2ServiceBytesReceivedLower_Object = MibTableColumn
mpl2ServiceBytesReceivedLower = _Mpl2ServiceBytesReceivedLower_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 1, 1, 1, 10),
    _Mpl2ServiceBytesReceivedLower_Type()
)
mpl2ServiceBytesReceivedLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2ServiceBytesReceivedLower.setStatus("mandatory")
_Mpl2ServiceLock_Type = OnOff
_Mpl2ServiceLock_Object = MibTableColumn
mpl2ServiceLock = _Mpl2ServiceLock_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 1, 1, 1, 11),
    _Mpl2ServiceLock_Type()
)
mpl2ServiceLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpl2ServiceLock.setStatus("mandatory")
_Mpl2LanSpecific_ObjectIdentity = ObjectIdentity
mpl2LanSpecific = _Mpl2LanSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 44, 2)
)
_Mpl2LanTable_Object = MibTable
mpl2LanTable = _Mpl2LanTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 2, 1)
)
if mibBuilder.loadTexts:
    mpl2LanTable.setStatus("mandatory")
_Mpl2LanEntry_Object = MibTableRow
mpl2LanEntry = _Mpl2LanEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 2, 1, 1)
)
mpl2LanEntry.setIndexNames(
    (0, "SCA-MPLINK2-MIB", "mpl2LanNumber"),
)
if mibBuilder.loadTexts:
    mpl2LanEntry.setStatus("mandatory")
_Mpl2LanNumber_Type = Integer32
_Mpl2LanNumber_Object = MibTableColumn
mpl2LanNumber = _Mpl2LanNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 2, 1, 1, 1),
    _Mpl2LanNumber_Type()
)
mpl2LanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2LanNumber.setStatus("mandatory")
_Mpl2LanRxCRCErrors_Type = Counter32
_Mpl2LanRxCRCErrors_Object = MibTableColumn
mpl2LanRxCRCErrors = _Mpl2LanRxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 2, 1, 1, 2),
    _Mpl2LanRxCRCErrors_Type()
)
mpl2LanRxCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2LanRxCRCErrors.setStatus("mandatory")
_Mpl2LanRxOverrun_Type = Counter32
_Mpl2LanRxOverrun_Object = MibTableColumn
mpl2LanRxOverrun = _Mpl2LanRxOverrun_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 2, 1, 1, 3),
    _Mpl2LanRxOverrun_Type()
)
mpl2LanRxOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2LanRxOverrun.setStatus("mandatory")
_Mpl2LanRxLong_Type = Counter32
_Mpl2LanRxLong_Object = MibTableColumn
mpl2LanRxLong = _Mpl2LanRxLong_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 2, 1, 1, 4),
    _Mpl2LanRxLong_Type()
)
mpl2LanRxLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2LanRxLong.setStatus("mandatory")
_Mpl2LanRxOverflow_Type = Counter32
_Mpl2LanRxOverflow_Object = MibTableColumn
mpl2LanRxOverflow = _Mpl2LanRxOverflow_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 2, 1, 1, 5),
    _Mpl2LanRxOverflow_Type()
)
mpl2LanRxOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2LanRxOverflow.setStatus("mandatory")
_Mpl2LanRxAlnErrors_Type = Counter32
_Mpl2LanRxAlnErrors_Object = MibTableColumn
mpl2LanRxAlnErrors = _Mpl2LanRxAlnErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 2, 1, 1, 6),
    _Mpl2LanRxAlnErrors_Type()
)
mpl2LanRxAlnErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2LanRxAlnErrors.setStatus("mandatory")
_Mpl2LanRxOuts_Type = Counter32
_Mpl2LanRxOuts_Object = MibTableColumn
mpl2LanRxOuts = _Mpl2LanRxOuts_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 2, 1, 1, 7),
    _Mpl2LanRxOuts_Type()
)
mpl2LanRxOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2LanRxOuts.setStatus("mandatory")
_Mpl2LanRxShort_Type = Counter32
_Mpl2LanRxShort_Object = MibTableColumn
mpl2LanRxShort = _Mpl2LanRxShort_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 2, 1, 1, 8),
    _Mpl2LanRxShort_Type()
)
mpl2LanRxShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2LanRxShort.setStatus("mandatory")
_Mpl2LanTxDeferred_Type = Counter32
_Mpl2LanTxDeferred_Object = MibTableColumn
mpl2LanTxDeferred = _Mpl2LanTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 2, 1, 1, 9),
    _Mpl2LanTxDeferred_Type()
)
mpl2LanTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2LanTxDeferred.setStatus("mandatory")
_Mpl2LanTxUnderrun_Type = Counter32
_Mpl2LanTxUnderrun_Object = MibTableColumn
mpl2LanTxUnderrun = _Mpl2LanTxUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 2, 1, 1, 10),
    _Mpl2LanTxUnderrun_Type()
)
mpl2LanTxUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2LanTxUnderrun.setStatus("mandatory")
_Mpl2LanTxSQEFailure_Type = Counter32
_Mpl2LanTxSQEFailure_Object = MibTableColumn
mpl2LanTxSQEFailure = _Mpl2LanTxSQEFailure_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 2, 1, 1, 11),
    _Mpl2LanTxSQEFailure_Type()
)
mpl2LanTxSQEFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2LanTxSQEFailure.setStatus("mandatory")
_Mpl2LanTxExcDeferral_Type = Counter32
_Mpl2LanTxExcDeferral_Object = MibTableColumn
mpl2LanTxExcDeferral = _Mpl2LanTxExcDeferral_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 2, 1, 1, 12),
    _Mpl2LanTxExcDeferral_Type()
)
mpl2LanTxExcDeferral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2LanTxExcDeferral.setStatus("mandatory")
_Mpl2LanTxCollExceed_Type = Counter32
_Mpl2LanTxCollExceed_Object = MibTableColumn
mpl2LanTxCollExceed = _Mpl2LanTxCollExceed_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 2, 1, 1, 13),
    _Mpl2LanTxCollExceed_Type()
)
mpl2LanTxCollExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2LanTxCollExceed.setStatus("mandatory")
_Mpl2LanTxLateColl_Type = Counter32
_Mpl2LanTxLateColl_Object = MibTableColumn
mpl2LanTxLateColl = _Mpl2LanTxLateColl_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 2, 1, 1, 14),
    _Mpl2LanTxLateColl_Type()
)
mpl2LanTxLateColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2LanTxLateColl.setStatus("mandatory")
_Mpl2LanTxCollisions_Type = Counter32
_Mpl2LanTxCollisions_Object = MibTableColumn
mpl2LanTxCollisions = _Mpl2LanTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 2, 1, 1, 15),
    _Mpl2LanTxCollisions_Type()
)
mpl2LanTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2LanTxCollisions.setStatus("mandatory")
_Mpl2LanTxNoCarrier_Type = Counter32
_Mpl2LanTxNoCarrier_Object = MibTableColumn
mpl2LanTxNoCarrier = _Mpl2LanTxNoCarrier_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 2, 1, 1, 16),
    _Mpl2LanTxNoCarrier_Type()
)
mpl2LanTxNoCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2LanTxNoCarrier.setStatus("mandatory")
_Mpl2WanSpecific_ObjectIdentity = ObjectIdentity
mpl2WanSpecific = _Mpl2WanSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 44, 3)
)
_Mpl2WanTable_Object = MibTable
mpl2WanTable = _Mpl2WanTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1)
)
if mibBuilder.loadTexts:
    mpl2WanTable.setStatus("mandatory")
_Mpl2WanEntry_Object = MibTableRow
mpl2WanEntry = _Mpl2WanEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1)
)
mpl2WanEntry.setIndexNames(
    (0, "SCA-MPLINK2-MIB", "mpl2WanNumber"),
)
if mibBuilder.loadTexts:
    mpl2WanEntry.setStatus("mandatory")
_Mpl2WanNumber_Type = Integer32
_Mpl2WanNumber_Object = MibTableColumn
mpl2WanNumber = _Mpl2WanNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1, 1),
    _Mpl2WanNumber_Type()
)
mpl2WanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2WanNumber.setStatus("mandatory")
_Mpl2WanDataState_Type = DataState
_Mpl2WanDataState_Object = MibTableColumn
mpl2WanDataState = _Mpl2WanDataState_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1, 2),
    _Mpl2WanDataState_Type()
)
mpl2WanDataState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2WanDataState.setStatus("mandatory")
_Mpl2WanDataStateTimer_Type = Integer32
_Mpl2WanDataStateTimer_Object = MibTableColumn
mpl2WanDataStateTimer = _Mpl2WanDataStateTimer_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1, 3),
    _Mpl2WanDataStateTimer_Type()
)
mpl2WanDataStateTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2WanDataStateTimer.setStatus("mandatory")
_Mpl2WanConnectState_Type = ConnectState
_Mpl2WanConnectState_Object = MibTableColumn
mpl2WanConnectState = _Mpl2WanConnectState_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1, 4),
    _Mpl2WanConnectState_Type()
)
mpl2WanConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2WanConnectState.setStatus("mandatory")
_Mpl2WanConnectStateTimer_Type = Integer32
_Mpl2WanConnectStateTimer_Object = MibTableColumn
mpl2WanConnectStateTimer = _Mpl2WanConnectStateTimer_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1, 5),
    _Mpl2WanConnectStateTimer_Type()
)
mpl2WanConnectStateTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2WanConnectStateTimer.setStatus("mandatory")
_Mpl2WanCompression_Type = OnOff
_Mpl2WanCompression_Object = MibTableColumn
mpl2WanCompression = _Mpl2WanCompression_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1, 6),
    _Mpl2WanCompression_Type()
)
mpl2WanCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2WanCompression.setStatus("mandatory")
_Mpl2WanCompressionType_Type = CompType
_Mpl2WanCompressionType_Object = MibTableColumn
mpl2WanCompressionType = _Mpl2WanCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1, 7),
    _Mpl2WanCompressionType_Type()
)
mpl2WanCompressionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2WanCompressionType.setStatus("mandatory")
_Mpl2WanCallsSucceeded_Type = Counter32
_Mpl2WanCallsSucceeded_Object = MibTableColumn
mpl2WanCallsSucceeded = _Mpl2WanCallsSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1, 8),
    _Mpl2WanCallsSucceeded_Type()
)
mpl2WanCallsSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2WanCallsSucceeded.setStatus("mandatory")
_Mpl2WanCallsFailed_Type = Counter32
_Mpl2WanCallsFailed_Object = MibTableColumn
mpl2WanCallsFailed = _Mpl2WanCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1, 9),
    _Mpl2WanCallsFailed_Type()
)
mpl2WanCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2WanCallsFailed.setStatus("mandatory")
_Mpl2WanCallsAccepted_Type = Counter32
_Mpl2WanCallsAccepted_Object = MibTableColumn
mpl2WanCallsAccepted = _Mpl2WanCallsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1, 10),
    _Mpl2WanCallsAccepted_Type()
)
mpl2WanCallsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2WanCallsAccepted.setStatus("mandatory")
_Mpl2WanCallsRejected_Type = Counter32
_Mpl2WanCallsRejected_Object = MibTableColumn
mpl2WanCallsRejected = _Mpl2WanCallsRejected_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1, 11),
    _Mpl2WanCallsRejected_Type()
)
mpl2WanCallsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2WanCallsRejected.setStatus("mandatory")
_Mpl2WanRetries_Type = Integer32
_Mpl2WanRetries_Object = MibTableColumn
mpl2WanRetries = _Mpl2WanRetries_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1, 12),
    _Mpl2WanRetries_Type()
)
mpl2WanRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpl2WanRetries.setStatus("mandatory")
_Mpl2WanDirection_Type = Direction
_Mpl2WanDirection_Object = MibTableColumn
mpl2WanDirection = _Mpl2WanDirection_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1, 13),
    _Mpl2WanDirection_Type()
)
mpl2WanDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2WanDirection.setStatus("mandatory")
_Mpl2WanHasBackup_Type = OnOff
_Mpl2WanHasBackup_Object = MibTableColumn
mpl2WanHasBackup = _Mpl2WanHasBackup_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1, 14),
    _Mpl2WanHasBackup_Type()
)
mpl2WanHasBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2WanHasBackup.setStatus("mandatory")
_Mpl2WanBackupFor_Type = Integer32
_Mpl2WanBackupFor_Object = MibTableColumn
mpl2WanBackupFor = _Mpl2WanBackupFor_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1, 15),
    _Mpl2WanBackupFor_Type()
)
mpl2WanBackupFor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2WanBackupFor.setStatus("mandatory")
_Mpl2WanBackupForAttachment_Type = OnOff
_Mpl2WanBackupForAttachment_Object = MibTableColumn
mpl2WanBackupForAttachment = _Mpl2WanBackupForAttachment_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1, 16),
    _Mpl2WanBackupForAttachment_Type()
)
mpl2WanBackupForAttachment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2WanBackupForAttachment.setStatus("mandatory")
_Mpl2WanIsSlave_Type = OnOff
_Mpl2WanIsSlave_Object = MibTableColumn
mpl2WanIsSlave = _Mpl2WanIsSlave_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1, 17),
    _Mpl2WanIsSlave_Type()
)
mpl2WanIsSlave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2WanIsSlave.setStatus("mandatory")
_Mpl2WanPppMaster_Type = Integer32
_Mpl2WanPppMaster_Object = MibTableColumn
mpl2WanPppMaster = _Mpl2WanPppMaster_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1, 18),
    _Mpl2WanPppMaster_Type()
)
mpl2WanPppMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2WanPppMaster.setStatus("mandatory")
_Mpl2WanPppSlaveUpCount_Type = Integer32
_Mpl2WanPppSlaveUpCount_Object = MibTableColumn
mpl2WanPppSlaveUpCount = _Mpl2WanPppSlaveUpCount_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1, 19),
    _Mpl2WanPppSlaveUpCount_Type()
)
mpl2WanPppSlaveUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2WanPppSlaveUpCount.setStatus("mandatory")
_Mpl2WanActivityTimeLeft_Type = Integer32
_Mpl2WanActivityTimeLeft_Object = MibTableColumn
mpl2WanActivityTimeLeft = _Mpl2WanActivityTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1, 20),
    _Mpl2WanActivityTimeLeft_Type()
)
mpl2WanActivityTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2WanActivityTimeLeft.setStatus("mandatory")
_Mpl2WanActivity_Type = OnOff
_Mpl2WanActivity_Object = MibTableColumn
mpl2WanActivity = _Mpl2WanActivity_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1, 21),
    _Mpl2WanActivity_Type()
)
mpl2WanActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpl2WanActivity.setStatus("mandatory")
_Mpl2WanTimer_Type = OnOff
_Mpl2WanTimer_Object = MibTableColumn
mpl2WanTimer = _Mpl2WanTimer_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 3, 1, 1, 22),
    _Mpl2WanTimer_Type()
)
mpl2WanTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2WanTimer.setStatus("mandatory")
_Mpl2IfSpecific_ObjectIdentity = ObjectIdentity
mpl2IfSpecific = _Mpl2IfSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 44, 4)
)
_Mpl2IfStackTable_Object = MibTable
mpl2IfStackTable = _Mpl2IfStackTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 4, 1)
)
if mibBuilder.loadTexts:
    mpl2IfStackTable.setStatus("mandatory")
_Mpl2IfStackEntry_Object = MibTableRow
mpl2IfStackEntry = _Mpl2IfStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 4, 1, 1)
)
mpl2IfStackEntry.setIndexNames(
    (0, "SCA-MPLINK2-MIB", "mpl2IfStackNumber"),
)
if mibBuilder.loadTexts:
    mpl2IfStackEntry.setStatus("mandatory")
_Mpl2IfStackNumber_Type = Integer32
_Mpl2IfStackNumber_Object = MibTableColumn
mpl2IfStackNumber = _Mpl2IfStackNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 4, 1, 1, 1),
    _Mpl2IfStackNumber_Type()
)
mpl2IfStackNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2IfStackNumber.setStatus("mandatory")
_Mpl2IfStackLowerLayer_Type = Integer32
_Mpl2IfStackLowerLayer_Object = MibTableColumn
mpl2IfStackLowerLayer = _Mpl2IfStackLowerLayer_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 4, 1, 1, 2),
    _Mpl2IfStackLowerLayer_Type()
)
mpl2IfStackLowerLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2IfStackLowerLayer.setStatus("mandatory")
_Mpl2General_ObjectIdentity = ObjectIdentity
mpl2General = _Mpl2General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 44, 5)
)
_Mpl2GeneralOverviewChange_Type = TimeTicks
_Mpl2GeneralOverviewChange_Object = MibScalar
mpl2GeneralOverviewChange = _Mpl2GeneralOverviewChange_Object(
    (1, 3, 6, 1, 4, 1, 208, 44, 5, 1),
    _Mpl2GeneralOverviewChange_Type()
)
mpl2GeneralOverviewChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpl2GeneralOverviewChange.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mpl2LockEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 208, 44, 0, 1)
)
mpl2LockEvent.setObjects(
      *(("SCA-MPLINK2-MIB", "mpl2ServiceNumber"),
        ("SCA-MPLINK2-MIB", "mpl2ServiceLock"))
)
if mibBuilder.loadTexts:
    mpl2LockEvent.setStatus(
        ""
    )

mpl2WanRetriesEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 208, 44, 0, 2)
)
mpl2WanRetriesEvent.setObjects(
      *(("SCA-MPLINK2-MIB", "mpl2WanNumber"),
        ("SCA-MPLINK2-MIB", "mpl2WanRetries"))
)
if mibBuilder.loadTexts:
    mpl2WanRetriesEvent.setStatus(
        ""
    )

mpl2WanActivityEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 208, 44, 0, 3)
)
mpl2WanActivityEvent.setObjects(
      *(("SCA-MPLINK2-MIB", "mpl2WanNumber"),
        ("SCA-MPLINK2-MIB", "mpl2WanActivity"))
)
if mibBuilder.loadTexts:
    mpl2WanActivityEvent.setStatus(
        ""
    )

mpl2WanTimerEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 208, 44, 0, 4)
)
mpl2WanTimerEvent.setObjects(
      *(("SCA-MPLINK2-MIB", "mpl2WanNumber"),
        ("SCA-MPLINK2-MIB", "mpl2WanTimer"))
)
if mibBuilder.loadTexts:
    mpl2WanTimerEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCA-MPLINK2-MIB",
    **{"OnOff": OnOff,
       "Attachment": Attachment,
       "CompType": CompType,
       "Direction": Direction,
       "DataState": DataState,
       "ConnectState": ConnectState,
       "mplk2": mplk2,
       "mpl2LockEvent": mpl2LockEvent,
       "mpl2WanRetriesEvent": mpl2WanRetriesEvent,
       "mpl2WanActivityEvent": mpl2WanActivityEvent,
       "mpl2WanTimerEvent": mpl2WanTimerEvent,
       "mpl2Service": mpl2Service,
       "mpl2ServiceTable": mpl2ServiceTable,
       "mpl2ServiceEntry": mpl2ServiceEntry,
       "mpl2ServiceNumber": mpl2ServiceNumber,
       "mpl2ServiceSlotNumber": mpl2ServiceSlotNumber,
       "mpl2ServicePlugNumber": mpl2ServicePlugNumber,
       "mpl2ServicePlugName": mpl2ServicePlugName,
       "mpl2ServiceAttachment": mpl2ServiceAttachment,
       "mpl2ServiceProvider": mpl2ServiceProvider,
       "mpl2ServiceBytesSentUpper": mpl2ServiceBytesSentUpper,
       "mpl2ServiceBytesSentLower": mpl2ServiceBytesSentLower,
       "mpl2ServiceBytesReceivedUpper": mpl2ServiceBytesReceivedUpper,
       "mpl2ServiceBytesReceivedLower": mpl2ServiceBytesReceivedLower,
       "mpl2ServiceLock": mpl2ServiceLock,
       "mpl2LanSpecific": mpl2LanSpecific,
       "mpl2LanTable": mpl2LanTable,
       "mpl2LanEntry": mpl2LanEntry,
       "mpl2LanNumber": mpl2LanNumber,
       "mpl2LanRxCRCErrors": mpl2LanRxCRCErrors,
       "mpl2LanRxOverrun": mpl2LanRxOverrun,
       "mpl2LanRxLong": mpl2LanRxLong,
       "mpl2LanRxOverflow": mpl2LanRxOverflow,
       "mpl2LanRxAlnErrors": mpl2LanRxAlnErrors,
       "mpl2LanRxOuts": mpl2LanRxOuts,
       "mpl2LanRxShort": mpl2LanRxShort,
       "mpl2LanTxDeferred": mpl2LanTxDeferred,
       "mpl2LanTxUnderrun": mpl2LanTxUnderrun,
       "mpl2LanTxSQEFailure": mpl2LanTxSQEFailure,
       "mpl2LanTxExcDeferral": mpl2LanTxExcDeferral,
       "mpl2LanTxCollExceed": mpl2LanTxCollExceed,
       "mpl2LanTxLateColl": mpl2LanTxLateColl,
       "mpl2LanTxCollisions": mpl2LanTxCollisions,
       "mpl2LanTxNoCarrier": mpl2LanTxNoCarrier,
       "mpl2WanSpecific": mpl2WanSpecific,
       "mpl2WanTable": mpl2WanTable,
       "mpl2WanEntry": mpl2WanEntry,
       "mpl2WanNumber": mpl2WanNumber,
       "mpl2WanDataState": mpl2WanDataState,
       "mpl2WanDataStateTimer": mpl2WanDataStateTimer,
       "mpl2WanConnectState": mpl2WanConnectState,
       "mpl2WanConnectStateTimer": mpl2WanConnectStateTimer,
       "mpl2WanCompression": mpl2WanCompression,
       "mpl2WanCompressionType": mpl2WanCompressionType,
       "mpl2WanCallsSucceeded": mpl2WanCallsSucceeded,
       "mpl2WanCallsFailed": mpl2WanCallsFailed,
       "mpl2WanCallsAccepted": mpl2WanCallsAccepted,
       "mpl2WanCallsRejected": mpl2WanCallsRejected,
       "mpl2WanRetries": mpl2WanRetries,
       "mpl2WanDirection": mpl2WanDirection,
       "mpl2WanHasBackup": mpl2WanHasBackup,
       "mpl2WanBackupFor": mpl2WanBackupFor,
       "mpl2WanBackupForAttachment": mpl2WanBackupForAttachment,
       "mpl2WanIsSlave": mpl2WanIsSlave,
       "mpl2WanPppMaster": mpl2WanPppMaster,
       "mpl2WanPppSlaveUpCount": mpl2WanPppSlaveUpCount,
       "mpl2WanActivityTimeLeft": mpl2WanActivityTimeLeft,
       "mpl2WanActivity": mpl2WanActivity,
       "mpl2WanTimer": mpl2WanTimer,
       "mpl2IfSpecific": mpl2IfSpecific,
       "mpl2IfStackTable": mpl2IfStackTable,
       "mpl2IfStackEntry": mpl2IfStackEntry,
       "mpl2IfStackNumber": mpl2IfStackNumber,
       "mpl2IfStackLowerLayer": mpl2IfStackLowerLayer,
       "mpl2General": mpl2General,
       "mpl2GeneralOverviewChange": mpl2GeneralOverviewChange}
)
