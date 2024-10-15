# SNMP MIB module (INTEL-MPLINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-MPLINK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:55 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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





class UserEnum(Integer32):
    """Custom type UserEnum based on Integer32"""
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
        *(("all", 1),
          ("br", 4),
          ("ip", 2),
          ("ipx", 3))
    )





class ProtoEnum(Integer32):
    """Custom type ProtoEnum based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("br-all", 19),
          ("br-bpdu", 20),
          ("br-other", 21),
          ("ip-all", 1),
          ("ip-bootp", 6),
          ("ip-dns", 5),
          ("ip-ftp", 2),
          ("ip-http", 7),
          ("ip-other", 11),
          ("ip-rip", 9),
          ("ip-smtp", 4),
          ("ip-snmp", 8),
          ("ip-telnet", 3),
          ("ip-tunnel", 10),
          ("ipx-all", 12),
          ("ipx-ncp", 13),
          ("ipx-other", 18),
          ("ipx-rip", 15),
          ("ipx-sap", 16),
          ("ipx-spx", 14),
          ("ipx-type20", 17))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mpl_ObjectIdentity = ObjectIdentity
mpl = _Mpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 20)
)
_MplService_ObjectIdentity = ObjectIdentity
mplService = _MplService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 1)
)
_MplServiceTable_Object = MibTable
mplServiceTable = _MplServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 1, 1)
)
if mibBuilder.loadTexts:
    mplServiceTable.setStatus("mandatory")
_MplServiceEntry_Object = MibTableRow
mplServiceEntry = _MplServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 1, 1, 1)
)
mplServiceEntry.setIndexNames(
    (0, "INTEL-MPLINK-MIB", "mplServiceNumber"),
)
if mibBuilder.loadTexts:
    mplServiceEntry.setStatus("mandatory")
_MplServiceNumber_Type = Integer32
_MplServiceNumber_Object = MibTableColumn
mplServiceNumber = _MplServiceNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 1, 1, 1, 1),
    _MplServiceNumber_Type()
)
mplServiceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplServiceNumber.setStatus("mandatory")
_MplServiceSlotNumber_Type = Integer32
_MplServiceSlotNumber_Object = MibTableColumn
mplServiceSlotNumber = _MplServiceSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 1, 1, 1, 2),
    _MplServiceSlotNumber_Type()
)
mplServiceSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplServiceSlotNumber.setStatus("mandatory")
_MplServicePlugNumber_Type = Integer32
_MplServicePlugNumber_Object = MibTableColumn
mplServicePlugNumber = _MplServicePlugNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 1, 1, 1, 3),
    _MplServicePlugNumber_Type()
)
mplServicePlugNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplServicePlugNumber.setStatus("mandatory")


class _MplServicePlugName_Type(DisplayString):
    """Custom type mplServicePlugName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_MplServicePlugName_Type.__name__ = "DisplayString"
_MplServicePlugName_Object = MibTableColumn
mplServicePlugName = _MplServicePlugName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 1, 1, 1, 4),
    _MplServicePlugName_Type()
)
mplServicePlugName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplServicePlugName.setStatus("mandatory")
_MplServiceAttachment_Type = Attachment
_MplServiceAttachment_Object = MibTableColumn
mplServiceAttachment = _MplServiceAttachment_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 1, 1, 1, 5),
    _MplServiceAttachment_Type()
)
mplServiceAttachment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplServiceAttachment.setStatus("mandatory")


class _MplServiceProvider_Type(Integer32):
    """Custom type mplServiceProvider based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("asyncAttachment", 20),
          ("frAttachment", 5),
          ("frHdlc", 4),
          ("isdnAttachment", 8),
          ("lan", 1),
          ("lapbHdlc", 2),
          ("lapbIsdn", 6),
          ("padX25", 18),
          ("pppAodi", 13),
          ("pppAsync", 19),
          ("pppHdlc", 3),
          ("pppIsdn", 7),
          ("pppMultiMaster", 12),
          ("pppPcmcia", 15),
          ("pppPcmciaModem", 17),
          ("pppTcpTunnel", 16),
          ("pppX25", 14),
          ("pppX31", 21),
          ("slip", 11),
          ("x25Attachment", 10),
          ("x25Lapb", 9))
    )


_MplServiceProvider_Type.__name__ = "Integer32"
_MplServiceProvider_Object = MibTableColumn
mplServiceProvider = _MplServiceProvider_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 1, 1, 1, 6),
    _MplServiceProvider_Type()
)
mplServiceProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplServiceProvider.setStatus("mandatory")
_MplServiceBytesSentUpper_Type = Counter32
_MplServiceBytesSentUpper_Object = MibTableColumn
mplServiceBytesSentUpper = _MplServiceBytesSentUpper_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 1, 1, 1, 7),
    _MplServiceBytesSentUpper_Type()
)
mplServiceBytesSentUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplServiceBytesSentUpper.setStatus("mandatory")
_MplServiceBytesSentLower_Type = Counter32
_MplServiceBytesSentLower_Object = MibTableColumn
mplServiceBytesSentLower = _MplServiceBytesSentLower_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 1, 1, 1, 8),
    _MplServiceBytesSentLower_Type()
)
mplServiceBytesSentLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplServiceBytesSentLower.setStatus("mandatory")
_MplServiceBytesReceivedUpper_Type = Counter32
_MplServiceBytesReceivedUpper_Object = MibTableColumn
mplServiceBytesReceivedUpper = _MplServiceBytesReceivedUpper_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 1, 1, 1, 9),
    _MplServiceBytesReceivedUpper_Type()
)
mplServiceBytesReceivedUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplServiceBytesReceivedUpper.setStatus("mandatory")
_MplServiceBytesReceivedLower_Type = Counter32
_MplServiceBytesReceivedLower_Object = MibTableColumn
mplServiceBytesReceivedLower = _MplServiceBytesReceivedLower_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 1, 1, 1, 10),
    _MplServiceBytesReceivedLower_Type()
)
mplServiceBytesReceivedLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplServiceBytesReceivedLower.setStatus("mandatory")
_MplServiceLock_Type = OnOff
_MplServiceLock_Object = MibTableColumn
mplServiceLock = _MplServiceLock_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 1, 1, 1, 11),
    _MplServiceLock_Type()
)
mplServiceLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplServiceLock.setStatus("mandatory")
_MplLanSpecific_ObjectIdentity = ObjectIdentity
mplLanSpecific = _MplLanSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 2)
)
_MplLanTable_Object = MibTable
mplLanTable = _MplLanTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 2, 1)
)
if mibBuilder.loadTexts:
    mplLanTable.setStatus("mandatory")
_MplLanEntry_Object = MibTableRow
mplLanEntry = _MplLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 2, 1, 1)
)
mplLanEntry.setIndexNames(
    (0, "INTEL-MPLINK-MIB", "mplLanNumber"),
)
if mibBuilder.loadTexts:
    mplLanEntry.setStatus("mandatory")
_MplLanNumber_Type = Integer32
_MplLanNumber_Object = MibTableColumn
mplLanNumber = _MplLanNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 2, 1, 1, 1),
    _MplLanNumber_Type()
)
mplLanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplLanNumber.setStatus("mandatory")
_MplLanRxCRCErrors_Type = Counter32
_MplLanRxCRCErrors_Object = MibTableColumn
mplLanRxCRCErrors = _MplLanRxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 2, 1, 1, 2),
    _MplLanRxCRCErrors_Type()
)
mplLanRxCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplLanRxCRCErrors.setStatus("mandatory")
_MplLanRxOverrun_Type = Counter32
_MplLanRxOverrun_Object = MibTableColumn
mplLanRxOverrun = _MplLanRxOverrun_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 2, 1, 1, 3),
    _MplLanRxOverrun_Type()
)
mplLanRxOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplLanRxOverrun.setStatus("mandatory")
_MplLanRxLong_Type = Counter32
_MplLanRxLong_Object = MibTableColumn
mplLanRxLong = _MplLanRxLong_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 2, 1, 1, 4),
    _MplLanRxLong_Type()
)
mplLanRxLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplLanRxLong.setStatus("mandatory")
_MplLanRxOverflow_Type = Counter32
_MplLanRxOverflow_Object = MibTableColumn
mplLanRxOverflow = _MplLanRxOverflow_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 2, 1, 1, 5),
    _MplLanRxOverflow_Type()
)
mplLanRxOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplLanRxOverflow.setStatus("mandatory")
_MplLanRxAlnErrors_Type = Counter32
_MplLanRxAlnErrors_Object = MibTableColumn
mplLanRxAlnErrors = _MplLanRxAlnErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 2, 1, 1, 6),
    _MplLanRxAlnErrors_Type()
)
mplLanRxAlnErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplLanRxAlnErrors.setStatus("mandatory")
_MplLanRxOuts_Type = Counter32
_MplLanRxOuts_Object = MibTableColumn
mplLanRxOuts = _MplLanRxOuts_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 2, 1, 1, 7),
    _MplLanRxOuts_Type()
)
mplLanRxOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplLanRxOuts.setStatus("mandatory")
_MplLanRxShort_Type = Counter32
_MplLanRxShort_Object = MibTableColumn
mplLanRxShort = _MplLanRxShort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 2, 1, 1, 8),
    _MplLanRxShort_Type()
)
mplLanRxShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplLanRxShort.setStatus("mandatory")
_MplLanTxDeferred_Type = Counter32
_MplLanTxDeferred_Object = MibTableColumn
mplLanTxDeferred = _MplLanTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 2, 1, 1, 9),
    _MplLanTxDeferred_Type()
)
mplLanTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplLanTxDeferred.setStatus("mandatory")
_MplLanTxUnderrun_Type = Counter32
_MplLanTxUnderrun_Object = MibTableColumn
mplLanTxUnderrun = _MplLanTxUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 2, 1, 1, 10),
    _MplLanTxUnderrun_Type()
)
mplLanTxUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplLanTxUnderrun.setStatus("mandatory")
_MplLanTxSQEFailure_Type = Counter32
_MplLanTxSQEFailure_Object = MibTableColumn
mplLanTxSQEFailure = _MplLanTxSQEFailure_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 2, 1, 1, 11),
    _MplLanTxSQEFailure_Type()
)
mplLanTxSQEFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplLanTxSQEFailure.setStatus("mandatory")
_MplLanTxExcDeferral_Type = Counter32
_MplLanTxExcDeferral_Object = MibTableColumn
mplLanTxExcDeferral = _MplLanTxExcDeferral_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 2, 1, 1, 12),
    _MplLanTxExcDeferral_Type()
)
mplLanTxExcDeferral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplLanTxExcDeferral.setStatus("mandatory")
_MplLanTxCollExceed_Type = Counter32
_MplLanTxCollExceed_Object = MibTableColumn
mplLanTxCollExceed = _MplLanTxCollExceed_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 2, 1, 1, 13),
    _MplLanTxCollExceed_Type()
)
mplLanTxCollExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplLanTxCollExceed.setStatus("mandatory")
_MplLanTxLateColl_Type = Counter32
_MplLanTxLateColl_Object = MibTableColumn
mplLanTxLateColl = _MplLanTxLateColl_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 2, 1, 1, 14),
    _MplLanTxLateColl_Type()
)
mplLanTxLateColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplLanTxLateColl.setStatus("mandatory")
_MplLanTxCollisions_Type = Counter32
_MplLanTxCollisions_Object = MibTableColumn
mplLanTxCollisions = _MplLanTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 2, 1, 1, 15),
    _MplLanTxCollisions_Type()
)
mplLanTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplLanTxCollisions.setStatus("mandatory")
_MplLanTxNoCarrier_Type = Counter32
_MplLanTxNoCarrier_Object = MibTableColumn
mplLanTxNoCarrier = _MplLanTxNoCarrier_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 2, 1, 1, 16),
    _MplLanTxNoCarrier_Type()
)
mplLanTxNoCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplLanTxNoCarrier.setStatus("mandatory")
_MplWanSpecific_ObjectIdentity = ObjectIdentity
mplWanSpecific = _MplWanSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3)
)
_MplWanTable_Object = MibTable
mplWanTable = _MplWanTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1)
)
if mibBuilder.loadTexts:
    mplWanTable.setStatus("mandatory")
_MplWanEntry_Object = MibTableRow
mplWanEntry = _MplWanEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1)
)
mplWanEntry.setIndexNames(
    (0, "INTEL-MPLINK-MIB", "mplWanNumber"),
)
if mibBuilder.loadTexts:
    mplWanEntry.setStatus("mandatory")
_MplWanNumber_Type = Integer32
_MplWanNumber_Object = MibTableColumn
mplWanNumber = _MplWanNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 1),
    _MplWanNumber_Type()
)
mplWanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanNumber.setStatus("mandatory")
_MplWanDataState_Type = DataState
_MplWanDataState_Object = MibTableColumn
mplWanDataState = _MplWanDataState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 2),
    _MplWanDataState_Type()
)
mplWanDataState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanDataState.setStatus("mandatory")
_MplWanDataStateTimer_Type = Integer32
_MplWanDataStateTimer_Object = MibTableColumn
mplWanDataStateTimer = _MplWanDataStateTimer_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 3),
    _MplWanDataStateTimer_Type()
)
mplWanDataStateTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanDataStateTimer.setStatus("mandatory")
_MplWanConnectState_Type = ConnectState
_MplWanConnectState_Object = MibTableColumn
mplWanConnectState = _MplWanConnectState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 4),
    _MplWanConnectState_Type()
)
mplWanConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanConnectState.setStatus("mandatory")
_MplWanConnectStateTimer_Type = Integer32
_MplWanConnectStateTimer_Object = MibTableColumn
mplWanConnectStateTimer = _MplWanConnectStateTimer_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 5),
    _MplWanConnectStateTimer_Type()
)
mplWanConnectStateTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanConnectStateTimer.setStatus("mandatory")
_MplWanCompression_Type = OnOff
_MplWanCompression_Object = MibTableColumn
mplWanCompression = _MplWanCompression_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 6),
    _MplWanCompression_Type()
)
mplWanCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanCompression.setStatus("mandatory")
_MplWanCompressionType_Type = CompType
_MplWanCompressionType_Object = MibTableColumn
mplWanCompressionType = _MplWanCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 7),
    _MplWanCompressionType_Type()
)
mplWanCompressionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanCompressionType.setStatus("mandatory")
_MplWanCallsSucceeded_Type = Counter32
_MplWanCallsSucceeded_Object = MibTableColumn
mplWanCallsSucceeded = _MplWanCallsSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 8),
    _MplWanCallsSucceeded_Type()
)
mplWanCallsSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanCallsSucceeded.setStatus("mandatory")
_MplWanCallsFailed_Type = Counter32
_MplWanCallsFailed_Object = MibTableColumn
mplWanCallsFailed = _MplWanCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 9),
    _MplWanCallsFailed_Type()
)
mplWanCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanCallsFailed.setStatus("mandatory")
_MplWanCallsAccepted_Type = Counter32
_MplWanCallsAccepted_Object = MibTableColumn
mplWanCallsAccepted = _MplWanCallsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 10),
    _MplWanCallsAccepted_Type()
)
mplWanCallsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanCallsAccepted.setStatus("mandatory")
_MplWanCallsRejected_Type = Counter32
_MplWanCallsRejected_Object = MibTableColumn
mplWanCallsRejected = _MplWanCallsRejected_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 11),
    _MplWanCallsRejected_Type()
)
mplWanCallsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanCallsRejected.setStatus("mandatory")
_MplWanRetries_Type = Integer32
_MplWanRetries_Object = MibTableColumn
mplWanRetries = _MplWanRetries_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 12),
    _MplWanRetries_Type()
)
mplWanRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplWanRetries.setStatus("mandatory")
_MplWanDirection_Type = Direction
_MplWanDirection_Object = MibTableColumn
mplWanDirection = _MplWanDirection_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 13),
    _MplWanDirection_Type()
)
mplWanDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanDirection.setStatus("mandatory")
_MplWanHasBackup_Type = OnOff
_MplWanHasBackup_Object = MibTableColumn
mplWanHasBackup = _MplWanHasBackup_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 14),
    _MplWanHasBackup_Type()
)
mplWanHasBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanHasBackup.setStatus("mandatory")
_MplWanBackupFor_Type = Integer32
_MplWanBackupFor_Object = MibTableColumn
mplWanBackupFor = _MplWanBackupFor_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 15),
    _MplWanBackupFor_Type()
)
mplWanBackupFor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanBackupFor.setStatus("mandatory")
_MplWanBackupForAttachment_Type = OnOff
_MplWanBackupForAttachment_Object = MibTableColumn
mplWanBackupForAttachment = _MplWanBackupForAttachment_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 16),
    _MplWanBackupForAttachment_Type()
)
mplWanBackupForAttachment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanBackupForAttachment.setStatus("mandatory")
_MplWanFlags_Type = Integer32
_MplWanFlags_Object = MibTableColumn
mplWanFlags = _MplWanFlags_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 17),
    _MplWanFlags_Type()
)
mplWanFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanFlags.setStatus("mandatory")
_MplWanPppMaster_Type = Integer32
_MplWanPppMaster_Object = MibTableColumn
mplWanPppMaster = _MplWanPppMaster_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 18),
    _MplWanPppMaster_Type()
)
mplWanPppMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanPppMaster.setStatus("mandatory")
_MplWanPppSlaveUpCount_Type = Integer32
_MplWanPppSlaveUpCount_Object = MibTableColumn
mplWanPppSlaveUpCount = _MplWanPppSlaveUpCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 19),
    _MplWanPppSlaveUpCount_Type()
)
mplWanPppSlaveUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanPppSlaveUpCount.setStatus("mandatory")
_MplWanActivityTimeLeft_Type = Integer32
_MplWanActivityTimeLeft_Object = MibTableColumn
mplWanActivityTimeLeft = _MplWanActivityTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 20),
    _MplWanActivityTimeLeft_Type()
)
mplWanActivityTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanActivityTimeLeft.setStatus("mandatory")
_MplWanActivity_Type = OnOff
_MplWanActivity_Object = MibTableColumn
mplWanActivity = _MplWanActivity_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 21),
    _MplWanActivity_Type()
)
mplWanActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplWanActivity.setStatus("mandatory")
_MplWanTimer_Type = OnOff
_MplWanTimer_Object = MibTableColumn
mplWanTimer = _MplWanTimer_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 22),
    _MplWanTimer_Type()
)
mplWanTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanTimer.setStatus("mandatory")
_MplWanTimeTillTimecut_Type = Integer32
_MplWanTimeTillTimecut_Object = MibTableColumn
mplWanTimeTillTimecut = _MplWanTimeTillTimecut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 23),
    _MplWanTimeTillTimecut_Type()
)
mplWanTimeTillTimecut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanTimeTillTimecut.setStatus("mandatory")


class _MplWanLastPacket_Type(OctetString):
    """Custom type mplWanLastPacket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_MplWanLastPacket_Type.__name__ = "OctetString"
_MplWanLastPacket_Object = MibTableColumn
mplWanLastPacket = _MplWanLastPacket_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 24),
    _MplWanLastPacket_Type()
)
mplWanLastPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanLastPacket.setStatus("mandatory")
_MplWanInCallsPlaced_Type = Counter32
_MplWanInCallsPlaced_Object = MibTableColumn
mplWanInCallsPlaced = _MplWanInCallsPlaced_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 25),
    _MplWanInCallsPlaced_Type()
)
mplWanInCallsPlaced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanInCallsPlaced.setStatus("mandatory")
_MplWanOutCallsPlaced_Type = Counter32
_MplWanOutCallsPlaced_Object = MibTableColumn
mplWanOutCallsPlaced = _MplWanOutCallsPlaced_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 26),
    _MplWanOutCallsPlaced_Type()
)
mplWanOutCallsPlaced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanOutCallsPlaced.setStatus("mandatory")
_MplWanInTimeActive_Type = Integer32
_MplWanInTimeActive_Object = MibTableColumn
mplWanInTimeActive = _MplWanInTimeActive_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 27),
    _MplWanInTimeActive_Type()
)
mplWanInTimeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanInTimeActive.setStatus("mandatory")
_MplWanOutTimeActive_Type = Integer32
_MplWanOutTimeActive_Object = MibTableColumn
mplWanOutTimeActive = _MplWanOutTimeActive_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 28),
    _MplWanOutTimeActive_Type()
)
mplWanOutTimeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanOutTimeActive.setStatus("mandatory")
_MplWanTotalTime_Type = Integer32
_MplWanTotalTime_Object = MibTableColumn
mplWanTotalTime = _MplWanTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 1, 1, 29),
    _MplWanTotalTime_Type()
)
mplWanTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplWanTotalTime.setStatus("mandatory")
_MplCompTable_Object = MibTable
mplCompTable = _MplCompTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2)
)
if mibBuilder.loadTexts:
    mplCompTable.setStatus("mandatory")
_MplCompEntry_Object = MibTableRow
mplCompEntry = _MplCompEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2, 1)
)
mplCompEntry.setIndexNames(
    (0, "INTEL-MPLINK-MIB", "mplCompNumber"),
)
if mibBuilder.loadTexts:
    mplCompEntry.setStatus("mandatory")
_MplCompNumber_Type = Integer32
_MplCompNumber_Object = MibTableColumn
mplCompNumber = _MplCompNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2, 1, 1),
    _MplCompNumber_Type()
)
mplCompNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplCompNumber.setStatus("mandatory")
_MplCompRxDecRxBytesTotalUpper_Type = Counter32
_MplCompRxDecRxBytesTotalUpper_Object = MibTableColumn
mplCompRxDecRxBytesTotalUpper = _MplCompRxDecRxBytesTotalUpper_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2, 1, 2),
    _MplCompRxDecRxBytesTotalUpper_Type()
)
mplCompRxDecRxBytesTotalUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplCompRxDecRxBytesTotalUpper.setStatus("mandatory")
_MplCompRxDecRxBytesTotalLower_Type = Counter32
_MplCompRxDecRxBytesTotalLower_Object = MibTableColumn
mplCompRxDecRxBytesTotalLower = _MplCompRxDecRxBytesTotalLower_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2, 1, 3),
    _MplCompRxDecRxBytesTotalLower_Type()
)
mplCompRxDecRxBytesTotalLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplCompRxDecRxBytesTotalLower.setStatus("mandatory")
_MplCompRxDecRxBytesDecompUpper_Type = Counter32
_MplCompRxDecRxBytesDecompUpper_Object = MibTableColumn
mplCompRxDecRxBytesDecompUpper = _MplCompRxDecRxBytesDecompUpper_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2, 1, 4),
    _MplCompRxDecRxBytesDecompUpper_Type()
)
mplCompRxDecRxBytesDecompUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplCompRxDecRxBytesDecompUpper.setStatus("mandatory")
_MplCompRxDecRxBytesDecompLower_Type = Counter32
_MplCompRxDecRxBytesDecompLower_Object = MibTableColumn
mplCompRxDecRxBytesDecompLower = _MplCompRxDecRxBytesDecompLower_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2, 1, 5),
    _MplCompRxDecRxBytesDecompLower_Type()
)
mplCompRxDecRxBytesDecompLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplCompRxDecRxBytesDecompLower.setStatus("mandatory")
_MplCompRxDecDecompressedUpper_Type = Counter32
_MplCompRxDecDecompressedUpper_Object = MibTableColumn
mplCompRxDecDecompressedUpper = _MplCompRxDecDecompressedUpper_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2, 1, 6),
    _MplCompRxDecDecompressedUpper_Type()
)
mplCompRxDecDecompressedUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplCompRxDecDecompressedUpper.setStatus("mandatory")
_MplCompRxDecDecompressedLower_Type = Counter32
_MplCompRxDecDecompressedLower_Object = MibTableColumn
mplCompRxDecDecompressedLower = _MplCompRxDecDecompressedLower_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2, 1, 7),
    _MplCompRxDecDecompressedLower_Type()
)
mplCompRxDecDecompressedLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplCompRxDecDecompressedLower.setStatus("mandatory")
_MplCompRxDecAllocErrorsUpper_Type = Counter32
_MplCompRxDecAllocErrorsUpper_Object = MibTableColumn
mplCompRxDecAllocErrorsUpper = _MplCompRxDecAllocErrorsUpper_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2, 1, 8),
    _MplCompRxDecAllocErrorsUpper_Type()
)
mplCompRxDecAllocErrorsUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplCompRxDecAllocErrorsUpper.setStatus("mandatory")
_MplCompRxDecAllocErrorsLower_Type = Counter32
_MplCompRxDecAllocErrorsLower_Object = MibTableColumn
mplCompRxDecAllocErrorsLower = _MplCompRxDecAllocErrorsLower_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2, 1, 9),
    _MplCompRxDecAllocErrorsLower_Type()
)
mplCompRxDecAllocErrorsLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplCompRxDecAllocErrorsLower.setStatus("mandatory")
_MplCompRxDecRemoteInits_Type = Counter32
_MplCompRxDecRemoteInits_Object = MibTableColumn
mplCompRxDecRemoteInits = _MplCompRxDecRemoteInits_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2, 1, 10),
    _MplCompRxDecRemoteInits_Type()
)
mplCompRxDecRemoteInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplCompRxDecRemoteInits.setStatus("mandatory")
_MplCompTxEncInBytesTotalUpper_Type = Counter32
_MplCompTxEncInBytesTotalUpper_Object = MibTableColumn
mplCompTxEncInBytesTotalUpper = _MplCompTxEncInBytesTotalUpper_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2, 1, 11),
    _MplCompTxEncInBytesTotalUpper_Type()
)
mplCompTxEncInBytesTotalUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplCompTxEncInBytesTotalUpper.setStatus("mandatory")
_MplCompTxEncInBytesTotalLower_Type = Counter32
_MplCompTxEncInBytesTotalLower_Object = MibTableColumn
mplCompTxEncInBytesTotalLower = _MplCompTxEncInBytesTotalLower_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2, 1, 12),
    _MplCompTxEncInBytesTotalLower_Type()
)
mplCompTxEncInBytesTotalLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplCompTxEncInBytesTotalLower.setStatus("mandatory")
_MplCompTxEncTxBytesCompUpper_Type = Counter32
_MplCompTxEncTxBytesCompUpper_Object = MibTableColumn
mplCompTxEncTxBytesCompUpper = _MplCompTxEncTxBytesCompUpper_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2, 1, 13),
    _MplCompTxEncTxBytesCompUpper_Type()
)
mplCompTxEncTxBytesCompUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplCompTxEncTxBytesCompUpper.setStatus("mandatory")
_MplCompTxEncTxBytesCompLower_Type = Counter32
_MplCompTxEncTxBytesCompLower_Object = MibTableColumn
mplCompTxEncTxBytesCompLower = _MplCompTxEncTxBytesCompLower_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2, 1, 14),
    _MplCompTxEncTxBytesCompLower_Type()
)
mplCompTxEncTxBytesCompLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplCompTxEncTxBytesCompLower.setStatus("mandatory")
_MplCompTxEncCompressedUpper_Type = Counter32
_MplCompTxEncCompressedUpper_Object = MibTableColumn
mplCompTxEncCompressedUpper = _MplCompTxEncCompressedUpper_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2, 1, 15),
    _MplCompTxEncCompressedUpper_Type()
)
mplCompTxEncCompressedUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplCompTxEncCompressedUpper.setStatus("mandatory")
_MplCompTxEncCompressedLower_Type = Counter32
_MplCompTxEncCompressedLower_Object = MibTableColumn
mplCompTxEncCompressedLower = _MplCompTxEncCompressedLower_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2, 1, 16),
    _MplCompTxEncCompressedLower_Type()
)
mplCompTxEncCompressedLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplCompTxEncCompressedLower.setStatus("mandatory")
_MplCompTxEncAllocErrorsUpper_Type = Counter32
_MplCompTxEncAllocErrorsUpper_Object = MibTableColumn
mplCompTxEncAllocErrorsUpper = _MplCompTxEncAllocErrorsUpper_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2, 1, 17),
    _MplCompTxEncAllocErrorsUpper_Type()
)
mplCompTxEncAllocErrorsUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplCompTxEncAllocErrorsUpper.setStatus("mandatory")
_MplCompTxEncAllocErrorsLower_Type = Counter32
_MplCompTxEncAllocErrorsLower_Object = MibTableColumn
mplCompTxEncAllocErrorsLower = _MplCompTxEncAllocErrorsLower_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2, 1, 18),
    _MplCompTxEncAllocErrorsLower_Type()
)
mplCompTxEncAllocErrorsLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplCompTxEncAllocErrorsLower.setStatus("mandatory")
_MplCompTxEncLocalInits_Type = Counter32
_MplCompTxEncLocalInits_Object = MibTableColumn
mplCompTxEncLocalInits = _MplCompTxEncLocalInits_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2, 1, 19),
    _MplCompTxEncLocalInits_Type()
)
mplCompTxEncLocalInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplCompTxEncLocalInits.setStatus("mandatory")
_MplCompTxEncTransmitErrors_Type = Integer32
_MplCompTxEncTransmitErrors_Object = MibTableColumn
mplCompTxEncTransmitErrors = _MplCompTxEncTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2, 1, 20),
    _MplCompTxEncTransmitErrors_Type()
)
mplCompTxEncTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplCompTxEncTransmitErrors.setStatus("mandatory")
_MplCompTxEncQueueLength_Type = Integer32
_MplCompTxEncQueueLength_Object = MibTableColumn
mplCompTxEncQueueLength = _MplCompTxEncQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 3, 2, 1, 21),
    _MplCompTxEncQueueLength_Type()
)
mplCompTxEncQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplCompTxEncQueueLength.setStatus("mandatory")
_MplIfSpecific_ObjectIdentity = ObjectIdentity
mplIfSpecific = _MplIfSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 4)
)
_MplIfStackTable_Object = MibTable
mplIfStackTable = _MplIfStackTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 4, 1)
)
if mibBuilder.loadTexts:
    mplIfStackTable.setStatus("mandatory")
_MplIfStackEntry_Object = MibTableRow
mplIfStackEntry = _MplIfStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 4, 1, 1)
)
mplIfStackEntry.setIndexNames(
    (0, "INTEL-MPLINK-MIB", "mplIfStackNumber"),
)
if mibBuilder.loadTexts:
    mplIfStackEntry.setStatus("mandatory")
_MplIfStackNumber_Type = Integer32
_MplIfStackNumber_Object = MibTableColumn
mplIfStackNumber = _MplIfStackNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 4, 1, 1, 1),
    _MplIfStackNumber_Type()
)
mplIfStackNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplIfStackNumber.setStatus("mandatory")
_MplIfStackLowerLayer_Type = Integer32
_MplIfStackLowerLayer_Object = MibTableColumn
mplIfStackLowerLayer = _MplIfStackLowerLayer_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 4, 1, 1, 2),
    _MplIfStackLowerLayer_Type()
)
mplIfStackLowerLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplIfStackLowerLayer.setStatus("mandatory")
_MplGeneral_ObjectIdentity = ObjectIdentity
mplGeneral = _MplGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 5)
)
_MplGeneralOverviewChange_Type = TimeTicks
_MplGeneralOverviewChange_Object = MibScalar
mplGeneralOverviewChange = _MplGeneralOverviewChange_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 5, 1),
    _MplGeneralOverviewChange_Type()
)
mplGeneralOverviewChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplGeneralOverviewChange.setStatus("mandatory")


class _MplGeneralIfgroupStatus_Type(OctetString):
    """Custom type mplGeneralIfgroupStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_MplGeneralIfgroupStatus_Type.__name__ = "OctetString"
_MplGeneralIfgroupStatus_Object = MibScalar
mplGeneralIfgroupStatus = _MplGeneralIfgroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 5, 2),
    _MplGeneralIfgroupStatus_Type()
)
mplGeneralIfgroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplGeneralIfgroupStatus.setStatus("mandatory")
_MplUtilization_ObjectIdentity = ObjectIdentity
mplUtilization = _MplUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 6)
)
_MplUtilizationTable_Object = MibTable
mplUtilizationTable = _MplUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 6, 1)
)
if mibBuilder.loadTexts:
    mplUtilizationTable.setStatus("mandatory")
_MplUtilizationEntry_Object = MibTableRow
mplUtilizationEntry = _MplUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 6, 1, 1)
)
mplUtilizationEntry.setIndexNames(
    (0, "INTEL-MPLINK-MIB", "mplUtilizationPlugNumber"),
    (0, "INTEL-MPLINK-MIB", "mplUtilizationMplink"),
    (0, "INTEL-MPLINK-MIB", "mplUtilizationUser"),
    (0, "INTEL-MPLINK-MIB", "mplUtilizationProtocol"),
)
if mibBuilder.loadTexts:
    mplUtilizationEntry.setStatus("mandatory")
_MplUtilizationPlugNumber_Type = Integer32
_MplUtilizationPlugNumber_Object = MibTableColumn
mplUtilizationPlugNumber = _MplUtilizationPlugNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 6, 1, 1, 1),
    _MplUtilizationPlugNumber_Type()
)
mplUtilizationPlugNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplUtilizationPlugNumber.setStatus("mandatory")
_MplUtilizationMplink_Type = Integer32
_MplUtilizationMplink_Object = MibTableColumn
mplUtilizationMplink = _MplUtilizationMplink_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 6, 1, 1, 2),
    _MplUtilizationMplink_Type()
)
mplUtilizationMplink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplUtilizationMplink.setStatus("mandatory")
_MplUtilizationUser_Type = UserEnum
_MplUtilizationUser_Object = MibTableColumn
mplUtilizationUser = _MplUtilizationUser_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 6, 1, 1, 3),
    _MplUtilizationUser_Type()
)
mplUtilizationUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplUtilizationUser.setStatus("mandatory")
_MplUtilizationProtocol_Type = ProtoEnum
_MplUtilizationProtocol_Object = MibTableColumn
mplUtilizationProtocol = _MplUtilizationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 6, 1, 1, 4),
    _MplUtilizationProtocol_Type()
)
mplUtilizationProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplUtilizationProtocol.setStatus("mandatory")
_MplUtilizationRxUtil_Type = Counter32
_MplUtilizationRxUtil_Object = MibTableColumn
mplUtilizationRxUtil = _MplUtilizationRxUtil_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 6, 1, 1, 5),
    _MplUtilizationRxUtil_Type()
)
mplUtilizationRxUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplUtilizationRxUtil.setStatus("mandatory")
_MplUtilizationTxUtil_Type = Counter32
_MplUtilizationTxUtil_Object = MibTableColumn
mplUtilizationTxUtil = _MplUtilizationTxUtil_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 6, 1, 1, 6),
    _MplUtilizationTxUtil_Type()
)
mplUtilizationTxUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplUtilizationTxUtil.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mplLockEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 0, 1)
)
mplLockEvent.setObjects(
      *(("INTEL-MPLINK-MIB", "mplServiceNumber"),
        ("INTEL-MPLINK-MIB", "mplServiceLock"))
)
if mibBuilder.loadTexts:
    mplLockEvent.setStatus(
        ""
    )

mplWanRetriesEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 0, 2)
)
mplWanRetriesEvent.setObjects(
      *(("INTEL-MPLINK-MIB", "mplWanNumber"),
        ("INTEL-MPLINK-MIB", "mplWanRetries"))
)
if mibBuilder.loadTexts:
    mplWanRetriesEvent.setStatus(
        ""
    )

mplWanActivityEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 0, 3)
)
mplWanActivityEvent.setObjects(
      *(("INTEL-MPLINK-MIB", "mplWanNumber"),
        ("INTEL-MPLINK-MIB", "mplWanActivity"))
)
if mibBuilder.loadTexts:
    mplWanActivityEvent.setStatus(
        ""
    )

mplWanTimerEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 20, 0, 4)
)
mplWanTimerEvent.setObjects(
      *(("INTEL-MPLINK-MIB", "mplWanNumber"),
        ("INTEL-MPLINK-MIB", "mplWanTimer"))
)
if mibBuilder.loadTexts:
    mplWanTimerEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-MPLINK-MIB",
    **{"OnOff": OnOff,
       "Attachment": Attachment,
       "CompType": CompType,
       "Direction": Direction,
       "DataState": DataState,
       "ConnectState": ConnectState,
       "UserEnum": UserEnum,
       "ProtoEnum": ProtoEnum,
       "mpl": mpl,
       "mplLockEvent": mplLockEvent,
       "mplWanRetriesEvent": mplWanRetriesEvent,
       "mplWanActivityEvent": mplWanActivityEvent,
       "mplWanTimerEvent": mplWanTimerEvent,
       "mplService": mplService,
       "mplServiceTable": mplServiceTable,
       "mplServiceEntry": mplServiceEntry,
       "mplServiceNumber": mplServiceNumber,
       "mplServiceSlotNumber": mplServiceSlotNumber,
       "mplServicePlugNumber": mplServicePlugNumber,
       "mplServicePlugName": mplServicePlugName,
       "mplServiceAttachment": mplServiceAttachment,
       "mplServiceProvider": mplServiceProvider,
       "mplServiceBytesSentUpper": mplServiceBytesSentUpper,
       "mplServiceBytesSentLower": mplServiceBytesSentLower,
       "mplServiceBytesReceivedUpper": mplServiceBytesReceivedUpper,
       "mplServiceBytesReceivedLower": mplServiceBytesReceivedLower,
       "mplServiceLock": mplServiceLock,
       "mplLanSpecific": mplLanSpecific,
       "mplLanTable": mplLanTable,
       "mplLanEntry": mplLanEntry,
       "mplLanNumber": mplLanNumber,
       "mplLanRxCRCErrors": mplLanRxCRCErrors,
       "mplLanRxOverrun": mplLanRxOverrun,
       "mplLanRxLong": mplLanRxLong,
       "mplLanRxOverflow": mplLanRxOverflow,
       "mplLanRxAlnErrors": mplLanRxAlnErrors,
       "mplLanRxOuts": mplLanRxOuts,
       "mplLanRxShort": mplLanRxShort,
       "mplLanTxDeferred": mplLanTxDeferred,
       "mplLanTxUnderrun": mplLanTxUnderrun,
       "mplLanTxSQEFailure": mplLanTxSQEFailure,
       "mplLanTxExcDeferral": mplLanTxExcDeferral,
       "mplLanTxCollExceed": mplLanTxCollExceed,
       "mplLanTxLateColl": mplLanTxLateColl,
       "mplLanTxCollisions": mplLanTxCollisions,
       "mplLanTxNoCarrier": mplLanTxNoCarrier,
       "mplWanSpecific": mplWanSpecific,
       "mplWanTable": mplWanTable,
       "mplWanEntry": mplWanEntry,
       "mplWanNumber": mplWanNumber,
       "mplWanDataState": mplWanDataState,
       "mplWanDataStateTimer": mplWanDataStateTimer,
       "mplWanConnectState": mplWanConnectState,
       "mplWanConnectStateTimer": mplWanConnectStateTimer,
       "mplWanCompression": mplWanCompression,
       "mplWanCompressionType": mplWanCompressionType,
       "mplWanCallsSucceeded": mplWanCallsSucceeded,
       "mplWanCallsFailed": mplWanCallsFailed,
       "mplWanCallsAccepted": mplWanCallsAccepted,
       "mplWanCallsRejected": mplWanCallsRejected,
       "mplWanRetries": mplWanRetries,
       "mplWanDirection": mplWanDirection,
       "mplWanHasBackup": mplWanHasBackup,
       "mplWanBackupFor": mplWanBackupFor,
       "mplWanBackupForAttachment": mplWanBackupForAttachment,
       "mplWanFlags": mplWanFlags,
       "mplWanPppMaster": mplWanPppMaster,
       "mplWanPppSlaveUpCount": mplWanPppSlaveUpCount,
       "mplWanActivityTimeLeft": mplWanActivityTimeLeft,
       "mplWanActivity": mplWanActivity,
       "mplWanTimer": mplWanTimer,
       "mplWanTimeTillTimecut": mplWanTimeTillTimecut,
       "mplWanLastPacket": mplWanLastPacket,
       "mplWanInCallsPlaced": mplWanInCallsPlaced,
       "mplWanOutCallsPlaced": mplWanOutCallsPlaced,
       "mplWanInTimeActive": mplWanInTimeActive,
       "mplWanOutTimeActive": mplWanOutTimeActive,
       "mplWanTotalTime": mplWanTotalTime,
       "mplCompTable": mplCompTable,
       "mplCompEntry": mplCompEntry,
       "mplCompNumber": mplCompNumber,
       "mplCompRxDecRxBytesTotalUpper": mplCompRxDecRxBytesTotalUpper,
       "mplCompRxDecRxBytesTotalLower": mplCompRxDecRxBytesTotalLower,
       "mplCompRxDecRxBytesDecompUpper": mplCompRxDecRxBytesDecompUpper,
       "mplCompRxDecRxBytesDecompLower": mplCompRxDecRxBytesDecompLower,
       "mplCompRxDecDecompressedUpper": mplCompRxDecDecompressedUpper,
       "mplCompRxDecDecompressedLower": mplCompRxDecDecompressedLower,
       "mplCompRxDecAllocErrorsUpper": mplCompRxDecAllocErrorsUpper,
       "mplCompRxDecAllocErrorsLower": mplCompRxDecAllocErrorsLower,
       "mplCompRxDecRemoteInits": mplCompRxDecRemoteInits,
       "mplCompTxEncInBytesTotalUpper": mplCompTxEncInBytesTotalUpper,
       "mplCompTxEncInBytesTotalLower": mplCompTxEncInBytesTotalLower,
       "mplCompTxEncTxBytesCompUpper": mplCompTxEncTxBytesCompUpper,
       "mplCompTxEncTxBytesCompLower": mplCompTxEncTxBytesCompLower,
       "mplCompTxEncCompressedUpper": mplCompTxEncCompressedUpper,
       "mplCompTxEncCompressedLower": mplCompTxEncCompressedLower,
       "mplCompTxEncAllocErrorsUpper": mplCompTxEncAllocErrorsUpper,
       "mplCompTxEncAllocErrorsLower": mplCompTxEncAllocErrorsLower,
       "mplCompTxEncLocalInits": mplCompTxEncLocalInits,
       "mplCompTxEncTransmitErrors": mplCompTxEncTransmitErrors,
       "mplCompTxEncQueueLength": mplCompTxEncQueueLength,
       "mplIfSpecific": mplIfSpecific,
       "mplIfStackTable": mplIfStackTable,
       "mplIfStackEntry": mplIfStackEntry,
       "mplIfStackNumber": mplIfStackNumber,
       "mplIfStackLowerLayer": mplIfStackLowerLayer,
       "mplGeneral": mplGeneral,
       "mplGeneralOverviewChange": mplGeneralOverviewChange,
       "mplGeneralIfgroupStatus": mplGeneralIfgroupStatus,
       "mplUtilization": mplUtilization,
       "mplUtilizationTable": mplUtilizationTable,
       "mplUtilizationEntry": mplUtilizationEntry,
       "mplUtilizationPlugNumber": mplUtilizationPlugNumber,
       "mplUtilizationMplink": mplUtilizationMplink,
       "mplUtilizationUser": mplUtilizationUser,
       "mplUtilizationProtocol": mplUtilizationProtocol,
       "mplUtilizationRxUtil": mplUtilizationRxUtil,
       "mplUtilizationTxUtil": mplUtilizationTxUtil}
)
