# SNMP MIB module (IEEE8021-SECY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-SECY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:04 2024
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
 ifCounterDiscontinuityGroup) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifCounterDiscontinuityGroup")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ieee8021SecyMIB = ModuleIdentity(
    (1, 0, 8802, 1, 1, 3)
)
ieee8021SecyMIB.setRevisions(
        ("2017-12-07 18:16",
         "2016-05-10 20:49",
         "2006-01-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SecySCI(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class SecyAN(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )



# MIB Managed Objects in the order of their OIDs

_SecyMIBNotifications_ObjectIdentity = ObjectIdentity
secyMIBNotifications = _SecyMIBNotifications_ObjectIdentity(
    (1, 0, 8802, 1, 1, 3, 0)
)
_SecyMIBObjects_ObjectIdentity = ObjectIdentity
secyMIBObjects = _SecyMIBObjects_ObjectIdentity(
    (1, 0, 8802, 1, 1, 3, 1)
)
_SecyMgmtMIBObjects_ObjectIdentity = ObjectIdentity
secyMgmtMIBObjects = _SecyMgmtMIBObjects_ObjectIdentity(
    (1, 0, 8802, 1, 1, 3, 1, 1)
)
_SecyIfTable_Object = MibTable
secyIfTable = _SecyIfTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    secyIfTable.setStatus("current")
_SecyIfEntry_Object = MibTableRow
secyIfEntry = _SecyIfEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1)
)
secyIfEntry.setIndexNames(
    (0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"),
)
if mibBuilder.loadTexts:
    secyIfEntry.setStatus("current")
_SecyIfInterfaceIndex_Type = InterfaceIndex
_SecyIfInterfaceIndex_Object = MibTableColumn
secyIfInterfaceIndex = _SecyIfInterfaceIndex_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 1),
    _SecyIfInterfaceIndex_Type()
)
secyIfInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    secyIfInterfaceIndex.setStatus("current")
_SecyIfMaxPeerSCs_Type = Unsigned32
_SecyIfMaxPeerSCs_Object = MibTableColumn
secyIfMaxPeerSCs = _SecyIfMaxPeerSCs_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 2),
    _SecyIfMaxPeerSCs_Type()
)
secyIfMaxPeerSCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyIfMaxPeerSCs.setStatus("current")
if mibBuilder.loadTexts:
    secyIfMaxPeerSCs.setUnits("security connections")
_SecyIfRxMaxKeys_Type = Unsigned32
_SecyIfRxMaxKeys_Object = MibTableColumn
secyIfRxMaxKeys = _SecyIfRxMaxKeys_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 3),
    _SecyIfRxMaxKeys_Type()
)
secyIfRxMaxKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyIfRxMaxKeys.setStatus("current")
if mibBuilder.loadTexts:
    secyIfRxMaxKeys.setUnits("keys")
_SecyIfTxMaxKeys_Type = Unsigned32
_SecyIfTxMaxKeys_Object = MibTableColumn
secyIfTxMaxKeys = _SecyIfTxMaxKeys_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 4),
    _SecyIfTxMaxKeys_Type()
)
secyIfTxMaxKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyIfTxMaxKeys.setStatus("current")
if mibBuilder.loadTexts:
    secyIfTxMaxKeys.setUnits("keys")


class _SecyIfProtectFramesEnable_Type(TruthValue):
    """Custom type secyIfProtectFramesEnable based on TruthValue"""


_SecyIfProtectFramesEnable_Object = MibTableColumn
secyIfProtectFramesEnable = _SecyIfProtectFramesEnable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 5),
    _SecyIfProtectFramesEnable_Type()
)
secyIfProtectFramesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secyIfProtectFramesEnable.setStatus("current")


class _SecyIfValidateFrames_Type(Integer32):
    """Custom type secyIfValidateFrames based on Integer32"""
    defaultValue = 3

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
        *(("check", 2),
          ("disabled", 1),
          ("null", 4),
          ("strict", 3))
    )


_SecyIfValidateFrames_Type.__name__ = "Integer32"
_SecyIfValidateFrames_Object = MibTableColumn
secyIfValidateFrames = _SecyIfValidateFrames_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 6),
    _SecyIfValidateFrames_Type()
)
secyIfValidateFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secyIfValidateFrames.setStatus("current")


class _SecyIfReplayProtectEnable_Type(TruthValue):
    """Custom type secyIfReplayProtectEnable based on TruthValue"""


_SecyIfReplayProtectEnable_Object = MibTableColumn
secyIfReplayProtectEnable = _SecyIfReplayProtectEnable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 7),
    _SecyIfReplayProtectEnable_Type()
)
secyIfReplayProtectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secyIfReplayProtectEnable.setStatus("current")


class _SecyIfReplayProtectWindow_Type(Unsigned32):
    """Custom type secyIfReplayProtectWindow based on Unsigned32"""
    defaultValue = 0


_SecyIfReplayProtectWindow_Object = MibTableColumn
secyIfReplayProtectWindow = _SecyIfReplayProtectWindow_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 8),
    _SecyIfReplayProtectWindow_Type()
)
secyIfReplayProtectWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secyIfReplayProtectWindow.setStatus("current")
if mibBuilder.loadTexts:
    secyIfReplayProtectWindow.setUnits("Packets")
_SecyIfCurrentCipherSuite_Type = Unsigned32
_SecyIfCurrentCipherSuite_Object = MibTableColumn
secyIfCurrentCipherSuite = _SecyIfCurrentCipherSuite_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 9),
    _SecyIfCurrentCipherSuite_Type()
)
secyIfCurrentCipherSuite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secyIfCurrentCipherSuite.setStatus("current")


class _SecyIfAdminPt2PtMAC_Type(Integer32):
    """Custom type secyIfAdminPt2PtMAC based on Integer32"""
    defaultValue = 3

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
          ("forceFalse", 2),
          ("forceTrue", 1))
    )


_SecyIfAdminPt2PtMAC_Type.__name__ = "Integer32"
_SecyIfAdminPt2PtMAC_Object = MibTableColumn
secyIfAdminPt2PtMAC = _SecyIfAdminPt2PtMAC_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 10),
    _SecyIfAdminPt2PtMAC_Type()
)
secyIfAdminPt2PtMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secyIfAdminPt2PtMAC.setStatus("current")
_SecyIfOperPt2PtMAC_Type = TruthValue
_SecyIfOperPt2PtMAC_Object = MibTableColumn
secyIfOperPt2PtMAC = _SecyIfOperPt2PtMAC_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 11),
    _SecyIfOperPt2PtMAC_Type()
)
secyIfOperPt2PtMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyIfOperPt2PtMAC.setStatus("current")


class _SecyIfIncludeSCIEnable_Type(TruthValue):
    """Custom type secyIfIncludeSCIEnable based on TruthValue"""


_SecyIfIncludeSCIEnable_Object = MibTableColumn
secyIfIncludeSCIEnable = _SecyIfIncludeSCIEnable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 12),
    _SecyIfIncludeSCIEnable_Type()
)
secyIfIncludeSCIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secyIfIncludeSCIEnable.setStatus("current")


class _SecyIfUseESEnable_Type(TruthValue):
    """Custom type secyIfUseESEnable based on TruthValue"""


_SecyIfUseESEnable_Object = MibTableColumn
secyIfUseESEnable = _SecyIfUseESEnable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 13),
    _SecyIfUseESEnable_Type()
)
secyIfUseESEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secyIfUseESEnable.setStatus("current")


class _SecyIfUseSCBEnable_Type(TruthValue):
    """Custom type secyIfUseSCBEnable based on TruthValue"""


_SecyIfUseSCBEnable_Object = MibTableColumn
secyIfUseSCBEnable = _SecyIfUseSCBEnable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 14),
    _SecyIfUseSCBEnable_Type()
)
secyIfUseSCBEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secyIfUseSCBEnable.setStatus("current")
_SecyIfSCI_Type = SecySCI
_SecyIfSCI_Object = MibTableColumn
secyIfSCI = _SecyIfSCI_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 15),
    _SecyIfSCI_Type()
)
secyIfSCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyIfSCI.setStatus("current")


class _SecyIfIncludingSCI_Type(TruthValue):
    """Custom type secyIfIncludingSCI based on TruthValue"""


_SecyIfIncludingSCI_Object = MibTableColumn
secyIfIncludingSCI = _SecyIfIncludingSCI_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 16),
    _SecyIfIncludingSCI_Type()
)
secyIfIncludingSCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyIfIncludingSCI.setStatus("current")
_SecyIfMaxTSCs_Type = Unsigned32
_SecyIfMaxTSCs_Object = MibTableColumn
secyIfMaxTSCs = _SecyIfMaxTSCs_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 17),
    _SecyIfMaxTSCs_Type()
)
secyIfMaxTSCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyIfMaxTSCs.setStatus("current")
if mibBuilder.loadTexts:
    secyIfMaxTSCs.setUnits("security connections")
_SecyTxSCTable_Object = MibTable
secyTxSCTable = _SecyTxSCTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    secyTxSCTable.setStatus("current")
_SecyTxSCEntry_Object = MibTableRow
secyTxSCEntry = _SecyTxSCEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 2, 1)
)
secyTxSCEntry.setIndexNames(
    (0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"),
)
if mibBuilder.loadTexts:
    secyTxSCEntry.setStatus("current")
_SecyTxSCI_Type = SecySCI
_SecyTxSCI_Object = MibTableColumn
secyTxSCI = _SecyTxSCI_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 2, 1, 1),
    _SecyTxSCI_Type()
)
secyTxSCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTxSCI.setStatus("current")


class _SecyTxSCState_Type(Integer32):
    """Custom type secyTxSCState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inUse", 1),
          ("notInUse", 2))
    )


_SecyTxSCState_Type.__name__ = "Integer32"
_SecyTxSCState_Object = MibTableColumn
secyTxSCState = _SecyTxSCState_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 2, 1, 2),
    _SecyTxSCState_Type()
)
secyTxSCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTxSCState.setStatus("current")
_SecyTxSCEncodingSA_Type = RowPointer
_SecyTxSCEncodingSA_Object = MibTableColumn
secyTxSCEncodingSA = _SecyTxSCEncodingSA_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 2, 1, 3),
    _SecyTxSCEncodingSA_Type()
)
secyTxSCEncodingSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTxSCEncodingSA.setStatus("current")
_SecyTxSCEncipheringSA_Type = RowPointer
_SecyTxSCEncipheringSA_Object = MibTableColumn
secyTxSCEncipheringSA = _SecyTxSCEncipheringSA_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 2, 1, 4),
    _SecyTxSCEncipheringSA_Type()
)
secyTxSCEncipheringSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTxSCEncipheringSA.setStatus("deprecated")
_SecyTxSCCreatedTime_Type = TimeStamp
_SecyTxSCCreatedTime_Object = MibTableColumn
secyTxSCCreatedTime = _SecyTxSCCreatedTime_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 2, 1, 5),
    _SecyTxSCCreatedTime_Type()
)
secyTxSCCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTxSCCreatedTime.setStatus("current")
_SecyTxSCStartedTime_Type = TimeStamp
_SecyTxSCStartedTime_Object = MibTableColumn
secyTxSCStartedTime = _SecyTxSCStartedTime_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 2, 1, 6),
    _SecyTxSCStartedTime_Type()
)
secyTxSCStartedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTxSCStartedTime.setStatus("current")
_SecyTxSCStoppedTime_Type = TimeStamp
_SecyTxSCStoppedTime_Object = MibTableColumn
secyTxSCStoppedTime = _SecyTxSCStoppedTime_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 2, 1, 7),
    _SecyTxSCStoppedTime_Type()
)
secyTxSCStoppedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTxSCStoppedTime.setStatus("current")
_SecyTxSATable_Object = MibTable
secyTxSATable = _SecyTxSATable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    secyTxSATable.setStatus("current")
_SecyTxSAEntry_Object = MibTableRow
secyTxSAEntry = _SecyTxSAEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 3, 1)
)
secyTxSAEntry.setIndexNames(
    (0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"),
    (0, "IEEE8021-SECY-MIB", "secyTxSA"),
)
if mibBuilder.loadTexts:
    secyTxSAEntry.setStatus("current")
_SecyTxSA_Type = SecyAN
_SecyTxSA_Object = MibTableColumn
secyTxSA = _SecyTxSA_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 3, 1, 1),
    _SecyTxSA_Type()
)
secyTxSA.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    secyTxSA.setStatus("current")


class _SecyTxSAState_Type(Integer32):
    """Custom type secyTxSAState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inUse", 1),
          ("notInUse", 2))
    )


_SecyTxSAState_Type.__name__ = "Integer32"
_SecyTxSAState_Object = MibTableColumn
secyTxSAState = _SecyTxSAState_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 3, 1, 2),
    _SecyTxSAState_Type()
)
secyTxSAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTxSAState.setStatus("current")
_SecyTxSANextPN_Type = Unsigned32
_SecyTxSANextPN_Object = MibTableColumn
secyTxSANextPN = _SecyTxSANextPN_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 3, 1, 3),
    _SecyTxSANextPN_Type()
)
secyTxSANextPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTxSANextPN.setStatus("current")
_SecyTxSAConfidentiality_Type = TruthValue
_SecyTxSAConfidentiality_Object = MibTableColumn
secyTxSAConfidentiality = _SecyTxSAConfidentiality_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 3, 1, 4),
    _SecyTxSAConfidentiality_Type()
)
secyTxSAConfidentiality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTxSAConfidentiality.setStatus("current")
_SecyTxSASAKUnchanged_Type = TruthValue
_SecyTxSASAKUnchanged_Object = MibTableColumn
secyTxSASAKUnchanged = _SecyTxSASAKUnchanged_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 3, 1, 5),
    _SecyTxSASAKUnchanged_Type()
)
secyTxSASAKUnchanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTxSASAKUnchanged.setStatus("deprecated")
_SecyTxSACreatedTime_Type = TimeStamp
_SecyTxSACreatedTime_Object = MibTableColumn
secyTxSACreatedTime = _SecyTxSACreatedTime_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 3, 1, 6),
    _SecyTxSACreatedTime_Type()
)
secyTxSACreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTxSACreatedTime.setStatus("current")
_SecyTxSAStartedTime_Type = TimeStamp
_SecyTxSAStartedTime_Object = MibTableColumn
secyTxSAStartedTime = _SecyTxSAStartedTime_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 3, 1, 7),
    _SecyTxSAStartedTime_Type()
)
secyTxSAStartedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTxSAStartedTime.setStatus("current")
_SecyTxSAStoppedTime_Type = TimeStamp
_SecyTxSAStoppedTime_Object = MibTableColumn
secyTxSAStoppedTime = _SecyTxSAStoppedTime_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 3, 1, 8),
    _SecyTxSAStoppedTime_Type()
)
secyTxSAStoppedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTxSAStoppedTime.setStatus("current")
_SecyRxSCTable_Object = MibTable
secyRxSCTable = _SecyRxSCTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    secyRxSCTable.setStatus("current")
_SecyRxSCEntry_Object = MibTableRow
secyRxSCEntry = _SecyRxSCEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 4, 1)
)
secyRxSCEntry.setIndexNames(
    (0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"),
    (0, "IEEE8021-SECY-MIB", "secyRxSCI"),
)
if mibBuilder.loadTexts:
    secyRxSCEntry.setStatus("current")
_SecyRxSCI_Type = SecySCI
_SecyRxSCI_Object = MibTableColumn
secyRxSCI = _SecyRxSCI_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 4, 1, 1),
    _SecyRxSCI_Type()
)
secyRxSCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    secyRxSCI.setStatus("current")


class _SecyRxSCState_Type(Integer32):
    """Custom type secyRxSCState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inUse", 1),
          ("notInUse", 2))
    )


_SecyRxSCState_Type.__name__ = "Integer32"
_SecyRxSCState_Object = MibTableColumn
secyRxSCState = _SecyRxSCState_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 4, 1, 2),
    _SecyRxSCState_Type()
)
secyRxSCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSCState.setStatus("current")
_SecyRxSCCurrentSA_Type = RowPointer
_SecyRxSCCurrentSA_Object = MibTableColumn
secyRxSCCurrentSA = _SecyRxSCCurrentSA_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 4, 1, 3),
    _SecyRxSCCurrentSA_Type()
)
secyRxSCCurrentSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSCCurrentSA.setStatus("deprecated")
_SecyRxSCCreatedTime_Type = TimeStamp
_SecyRxSCCreatedTime_Object = MibTableColumn
secyRxSCCreatedTime = _SecyRxSCCreatedTime_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 4, 1, 4),
    _SecyRxSCCreatedTime_Type()
)
secyRxSCCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSCCreatedTime.setStatus("current")
_SecyRxSCStartedTime_Type = TimeStamp
_SecyRxSCStartedTime_Object = MibTableColumn
secyRxSCStartedTime = _SecyRxSCStartedTime_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 4, 1, 5),
    _SecyRxSCStartedTime_Type()
)
secyRxSCStartedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSCStartedTime.setStatus("current")
_SecyRxSCStoppedTime_Type = TimeStamp
_SecyRxSCStoppedTime_Object = MibTableColumn
secyRxSCStoppedTime = _SecyRxSCStoppedTime_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 4, 1, 6),
    _SecyRxSCStoppedTime_Type()
)
secyRxSCStoppedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSCStoppedTime.setStatus("current")
_SecyRxSATable_Object = MibTable
secyRxSATable = _SecyRxSATable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    secyRxSATable.setStatus("current")
_SecyRxSAEntry_Object = MibTableRow
secyRxSAEntry = _SecyRxSAEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 5, 1)
)
secyRxSAEntry.setIndexNames(
    (0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"),
    (0, "IEEE8021-SECY-MIB", "secyRxSCI"),
    (0, "IEEE8021-SECY-MIB", "secyRxSA"),
)
if mibBuilder.loadTexts:
    secyRxSAEntry.setStatus("current")
_SecyRxSA_Type = SecyAN
_SecyRxSA_Object = MibTableColumn
secyRxSA = _SecyRxSA_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 5, 1, 1),
    _SecyRxSA_Type()
)
secyRxSA.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    secyRxSA.setStatus("current")


class _SecyRxSAState_Type(Integer32):
    """Custom type secyRxSAState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inUse", 1),
          ("notInUse", 2))
    )


_SecyRxSAState_Type.__name__ = "Integer32"
_SecyRxSAState_Object = MibTableColumn
secyRxSAState = _SecyRxSAState_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 5, 1, 2),
    _SecyRxSAState_Type()
)
secyRxSAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSAState.setStatus("current")
_SecyRxSANextPN_Type = Unsigned32
_SecyRxSANextPN_Object = MibTableColumn
secyRxSANextPN = _SecyRxSANextPN_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 5, 1, 3),
    _SecyRxSANextPN_Type()
)
secyRxSANextPN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secyRxSANextPN.setStatus("deprecated")
_SecyRxSASAKUnchanged_Type = TruthValue
_SecyRxSASAKUnchanged_Object = MibTableColumn
secyRxSASAKUnchanged = _SecyRxSASAKUnchanged_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 5, 1, 4),
    _SecyRxSASAKUnchanged_Type()
)
secyRxSASAKUnchanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSASAKUnchanged.setStatus("deprecated")
_SecyRxSACreatedTime_Type = TimeStamp
_SecyRxSACreatedTime_Object = MibTableColumn
secyRxSACreatedTime = _SecyRxSACreatedTime_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 5, 1, 5),
    _SecyRxSACreatedTime_Type()
)
secyRxSACreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSACreatedTime.setStatus("current")
_SecyRxSAStartedTime_Type = TimeStamp
_SecyRxSAStartedTime_Object = MibTableColumn
secyRxSAStartedTime = _SecyRxSAStartedTime_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 5, 1, 6),
    _SecyRxSAStartedTime_Type()
)
secyRxSAStartedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSAStartedTime.setStatus("current")
_SecyRxSAStoppedTime_Type = TimeStamp
_SecyRxSAStoppedTime_Object = MibTableColumn
secyRxSAStoppedTime = _SecyRxSAStoppedTime_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 5, 1, 7),
    _SecyRxSAStoppedTime_Type()
)
secyRxSAStoppedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSAStoppedTime.setStatus("current")
_SecyRxSANextXPN_Type = Counter64
_SecyRxSANextXPN_Object = MibTableColumn
secyRxSANextXPN = _SecyRxSANextXPN_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 5, 1, 8),
    _SecyRxSANextXPN_Type()
)
secyRxSANextXPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSANextXPN.setStatus("current")
_SecyRxSALowestXPN_Type = Counter64
_SecyRxSALowestXPN_Object = MibTableColumn
secyRxSALowestXPN = _SecyRxSALowestXPN_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 5, 1, 9),
    _SecyRxSALowestXPN_Type()
)
secyRxSALowestXPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSALowestXPN.setStatus("current")


class _SecyRxSAKeyIdentifier_Type(SnmpAdminString):
    """Custom type secyRxSAKeyIdentifier based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SecyRxSAKeyIdentifier_Type.__name__ = "SnmpAdminString"
_SecyRxSAKeyIdentifier_Object = MibTableColumn
secyRxSAKeyIdentifier = _SecyRxSAKeyIdentifier_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 5, 1, 10),
    _SecyRxSAKeyIdentifier_Type()
)
secyRxSAKeyIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSAKeyIdentifier.setStatus("current")
_SecyRxSASSCI_Type = Integer32
_SecyRxSASSCI_Object = MibTableColumn
secyRxSASSCI = _SecyRxSASSCI_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 5, 1, 11),
    _SecyRxSASSCI_Type()
)
secyRxSASSCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSASSCI.setStatus("current")
_SecyCipherSuiteTable_Object = MibTable
secyCipherSuiteTable = _SecyCipherSuiteTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    secyCipherSuiteTable.setStatus("current")
_SecyCipherSuiteEntry_Object = MibTableRow
secyCipherSuiteEntry = _SecyCipherSuiteEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 6, 1)
)
secyCipherSuiteEntry.setIndexNames(
    (0, "IEEE8021-SECY-MIB", "secyCipherSuiteIndex"),
)
if mibBuilder.loadTexts:
    secyCipherSuiteEntry.setStatus("current")


class _SecyCipherSuiteIndex_Type(Unsigned32):
    """Custom type secyCipherSuiteIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SecyCipherSuiteIndex_Type.__name__ = "Unsigned32"
_SecyCipherSuiteIndex_Object = MibTableColumn
secyCipherSuiteIndex = _SecyCipherSuiteIndex_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 6, 1, 1),
    _SecyCipherSuiteIndex_Type()
)
secyCipherSuiteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    secyCipherSuiteIndex.setStatus("current")


class _SecyCipherSuiteId_Type(OctetString):
    """Custom type secyCipherSuiteId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SecyCipherSuiteId_Type.__name__ = "OctetString"
_SecyCipherSuiteId_Object = MibTableColumn
secyCipherSuiteId = _SecyCipherSuiteId_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 6, 1, 2),
    _SecyCipherSuiteId_Type()
)
secyCipherSuiteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secyCipherSuiteId.setStatus("current")


class _SecyCipherSuiteName_Type(SnmpAdminString):
    """Custom type secyCipherSuiteName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SecyCipherSuiteName_Type.__name__ = "SnmpAdminString"
_SecyCipherSuiteName_Object = MibTableColumn
secyCipherSuiteName = _SecyCipherSuiteName_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 6, 1, 3),
    _SecyCipherSuiteName_Type()
)
secyCipherSuiteName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secyCipherSuiteName.setStatus("current")


class _SecyCipherSuiteCapability_Type(Bits):
    """Custom type secyCipherSuiteCapability based on Bits"""
    namedValues = NamedValues(
        *(("confidentiality", 1),
          ("integrity", 0),
          ("offsetConfidentiality", 2))
    )

_SecyCipherSuiteCapability_Type.__name__ = "Bits"
_SecyCipherSuiteCapability_Object = MibTableColumn
secyCipherSuiteCapability = _SecyCipherSuiteCapability_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 6, 1, 4),
    _SecyCipherSuiteCapability_Type()
)
secyCipherSuiteCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secyCipherSuiteCapability.setStatus("current")


class _SecyCipherSuiteProtection_Type(Bits):
    """Custom type secyCipherSuiteProtection based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("confidentiality", 1),
          ("integrity", 0),
          ("offsetConfidentiality", 2))
    )

_SecyCipherSuiteProtection_Type.__name__ = "Bits"
_SecyCipherSuiteProtection_Object = MibTableColumn
secyCipherSuiteProtection = _SecyCipherSuiteProtection_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 6, 1, 5),
    _SecyCipherSuiteProtection_Type()
)
secyCipherSuiteProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secyCipherSuiteProtection.setStatus("deprecated")


class _SecyCipherSuiteProtectionOffset_Type(Integer32):
    """Custom type secyCipherSuiteProtectionOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(50, 50),
    )


_SecyCipherSuiteProtectionOffset_Type.__name__ = "Integer32"
_SecyCipherSuiteProtectionOffset_Object = MibTableColumn
secyCipherSuiteProtectionOffset = _SecyCipherSuiteProtectionOffset_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 6, 1, 6),
    _SecyCipherSuiteProtectionOffset_Type()
)
secyCipherSuiteProtectionOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secyCipherSuiteProtectionOffset.setStatus("deprecated")
if mibBuilder.loadTexts:
    secyCipherSuiteProtectionOffset.setUnits("bytes")
_SecyCipherSuiteDataLengthChange_Type = TruthValue
_SecyCipherSuiteDataLengthChange_Object = MibTableColumn
secyCipherSuiteDataLengthChange = _SecyCipherSuiteDataLengthChange_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 6, 1, 7),
    _SecyCipherSuiteDataLengthChange_Type()
)
secyCipherSuiteDataLengthChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secyCipherSuiteDataLengthChange.setStatus("current")


class _SecyCipherSuiteICVLength_Type(Unsigned32):
    """Custom type secyCipherSuiteICVLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 16),
    )


_SecyCipherSuiteICVLength_Type.__name__ = "Unsigned32"
_SecyCipherSuiteICVLength_Object = MibTableColumn
secyCipherSuiteICVLength = _SecyCipherSuiteICVLength_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 6, 1, 8),
    _SecyCipherSuiteICVLength_Type()
)
secyCipherSuiteICVLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secyCipherSuiteICVLength.setStatus("current")
if mibBuilder.loadTexts:
    secyCipherSuiteICVLength.setUnits("octets")
_SecyCipherSuiteRowStatus_Type = RowStatus
_SecyCipherSuiteRowStatus_Object = MibTableColumn
secyCipherSuiteRowStatus = _SecyCipherSuiteRowStatus_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 6, 1, 9),
    _SecyCipherSuiteRowStatus_Type()
)
secyCipherSuiteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secyCipherSuiteRowStatus.setStatus("current")
_SecyIfCipherTable_Object = MibTable
secyIfCipherTable = _SecyIfCipherTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 7)
)
if mibBuilder.loadTexts:
    secyIfCipherTable.setStatus("current")
_SecyIfCipherEntry_Object = MibTableRow
secyIfCipherEntry = _SecyIfCipherEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 7, 1)
)
secyIfCipherEntry.setIndexNames(
    (0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"),
    (0, "IEEE8021-SECY-MIB", "secyCipherSuiteIndex"),
)
if mibBuilder.loadTexts:
    secyIfCipherEntry.setStatus("current")


class _SecyIfCipherImplemented_Type(TruthValue):
    """Custom type secyIfCipherImplemented based on TruthValue"""


_SecyIfCipherImplemented_Object = MibTableColumn
secyIfCipherImplemented = _SecyIfCipherImplemented_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 7, 1, 1),
    _SecyIfCipherImplemented_Type()
)
secyIfCipherImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyIfCipherImplemented.setStatus("current")


class _SecyIfCipherEnableUse_Type(TruthValue):
    """Custom type secyIfCipherEnableUse based on TruthValue"""


_SecyIfCipherEnableUse_Object = MibTableColumn
secyIfCipherEnableUse = _SecyIfCipherEnableUse_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 7, 1, 2),
    _SecyIfCipherEnableUse_Type()
)
secyIfCipherEnableUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secyIfCipherEnableUse.setStatus("current")


class _SecyIfCipherRqConfidentiality_Type(TruthValue):
    """Custom type secyIfCipherRqConfidentiality based on TruthValue"""


_SecyIfCipherRqConfidentiality_Object = MibTableColumn
secyIfCipherRqConfidentiality = _SecyIfCipherRqConfidentiality_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 7, 1, 3),
    _SecyIfCipherRqConfidentiality_Type()
)
secyIfCipherRqConfidentiality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secyIfCipherRqConfidentiality.setStatus("current")
_SecyIfTCTable_Object = MibTable
secyIfTCTable = _SecyIfTCTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 8)
)
if mibBuilder.loadTexts:
    secyIfTCTable.setStatus("current")
_SecyIfTCEntry_Object = MibTableRow
secyIfTCEntry = _SecyIfTCEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 8, 1)
)
secyIfTCEntry.setIndexNames(
    (0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"),
    (0, "IEEE8021-SECY-MIB", "secyIfTCUserPriority"),
)
if mibBuilder.loadTexts:
    secyIfTCEntry.setStatus("current")


class _SecyIfTCUserPriority_Type(Integer32):
    """Custom type secyIfTCUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SecyIfTCUserPriority_Type.__name__ = "Integer32"
_SecyIfTCUserPriority_Object = MibTableColumn
secyIfTCUserPriority = _SecyIfTCUserPriority_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 8, 1, 1),
    _SecyIfTCUserPriority_Type()
)
secyIfTCUserPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    secyIfTCUserPriority.setStatus("current")


class _SecyIfTCTrafficClass_Type(Integer32):
    """Custom type secyIfTCTrafficClass based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SecyIfTCTrafficClass_Type.__name__ = "Integer32"
_SecyIfTCTrafficClass_Object = MibTableColumn
secyIfTCTrafficClass = _SecyIfTCTrafficClass_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 8, 1, 2),
    _SecyIfTCTrafficClass_Type()
)
secyIfTCTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secyIfTCTrafficClass.setStatus("current")
_SecyIfAPTable_Object = MibTable
secyIfAPTable = _SecyIfAPTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 9)
)
if mibBuilder.loadTexts:
    secyIfAPTable.setStatus("current")
_SecyIfAPEntry_Object = MibTableRow
secyIfAPEntry = _SecyIfAPEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 9, 1)
)
secyIfAPEntry.setIndexNames(
    (0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"),
    (0, "IEEE8021-SECY-MIB", "secyIfAPUserPCP"),
)
if mibBuilder.loadTexts:
    secyIfAPEntry.setStatus("current")


class _SecyIfAPUserPCP_Type(Integer32):
    """Custom type secyIfAPUserPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SecyIfAPUserPCP_Type.__name__ = "Integer32"
_SecyIfAPUserPCP_Object = MibTableColumn
secyIfAPUserPCP = _SecyIfAPUserPCP_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 9, 1, 1),
    _SecyIfAPUserPCP_Type()
)
secyIfAPUserPCP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    secyIfAPUserPCP.setStatus("current")


class _SecyIfAPAccessPCP_Type(Integer32):
    """Custom type secyIfAPAccessPCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SecyIfAPAccessPCP_Type.__name__ = "Integer32"
_SecyIfAPAccessPCP_Object = MibTableColumn
secyIfAPAccessPCP = _SecyIfAPAccessPCP_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 9, 1, 2),
    _SecyIfAPAccessPCP_Type()
)
secyIfAPAccessPCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secyIfAPAccessPCP.setStatus("current")
_SecyTSCTable_Object = MibTable
secyTSCTable = _SecyTSCTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 10)
)
if mibBuilder.loadTexts:
    secyTSCTable.setStatus("current")
_SecyTSCEntry_Object = MibTableRow
secyTSCEntry = _SecyTSCEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 10, 1)
)
secyTSCEntry.setIndexNames(
    (0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"),
    (0, "IEEE8021-SECY-MIB", "secyTSCI"),
)
if mibBuilder.loadTexts:
    secyTSCEntry.setStatus("current")
_SecyTSCI_Type = SecySCI
_SecyTSCI_Object = MibTableColumn
secyTSCI = _SecyTSCI_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 10, 1, 1),
    _SecyTSCI_Type()
)
secyTSCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    secyTSCI.setStatus("current")


class _SecyTSCState_Type(Integer32):
    """Custom type secyTSCState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inUse", 1),
          ("notInUse", 2))
    )


_SecyTSCState_Type.__name__ = "Integer32"
_SecyTSCState_Object = MibTableColumn
secyTSCState = _SecyTSCState_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 10, 1, 2),
    _SecyTSCState_Type()
)
secyTSCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTSCState.setStatus("current")
_SecyTSCEncodingSA_Type = RowPointer
_SecyTSCEncodingSA_Object = MibTableColumn
secyTSCEncodingSA = _SecyTSCEncodingSA_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 10, 1, 3),
    _SecyTSCEncodingSA_Type()
)
secyTSCEncodingSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTSCEncodingSA.setStatus("current")
_SecyTSCCreatedTime_Type = TimeStamp
_SecyTSCCreatedTime_Object = MibTableColumn
secyTSCCreatedTime = _SecyTSCCreatedTime_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 10, 1, 4),
    _SecyTSCCreatedTime_Type()
)
secyTSCCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTSCCreatedTime.setStatus("current")
_SecyTSCStartedTime_Type = TimeStamp
_SecyTSCStartedTime_Object = MibTableColumn
secyTSCStartedTime = _SecyTSCStartedTime_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 10, 1, 5),
    _SecyTSCStartedTime_Type()
)
secyTSCStartedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTSCStartedTime.setStatus("current")
_SecyTSCStoppedTime_Type = TimeStamp
_SecyTSCStoppedTime_Object = MibTableColumn
secyTSCStoppedTime = _SecyTSCStoppedTime_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 10, 1, 6),
    _SecyTSCStoppedTime_Type()
)
secyTSCStoppedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTSCStoppedTime.setStatus("current")
_SecyTSATable_Object = MibTable
secyTSATable = _SecyTSATable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 11)
)
if mibBuilder.loadTexts:
    secyTSATable.setStatus("current")
_SecyTSAEntry_Object = MibTableRow
secyTSAEntry = _SecyTSAEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 11, 1)
)
secyTSAEntry.setIndexNames(
    (0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"),
    (0, "IEEE8021-SECY-MIB", "secyTSCI"),
    (0, "IEEE8021-SECY-MIB", "secyTSA"),
)
if mibBuilder.loadTexts:
    secyTSAEntry.setStatus("current")
_SecyTSA_Type = SecyAN
_SecyTSA_Object = MibTableColumn
secyTSA = _SecyTSA_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 11, 1, 1),
    _SecyTSA_Type()
)
secyTSA.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    secyTSA.setStatus("current")


class _SecyTSAState_Type(Integer32):
    """Custom type secyTSAState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inUse", 1),
          ("notInUse", 2))
    )


_SecyTSAState_Type.__name__ = "Integer32"
_SecyTSAState_Object = MibTableColumn
secyTSAState = _SecyTSAState_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 11, 1, 2),
    _SecyTSAState_Type()
)
secyTSAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTSAState.setStatus("current")
_SecyTSANextXPN_Type = Counter64
_SecyTSANextXPN_Object = MibTableColumn
secyTSANextXPN = _SecyTSANextXPN_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 11, 1, 3),
    _SecyTSANextXPN_Type()
)
secyTSANextXPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTSANextXPN.setStatus("current")
_SecyTSAConfidentiality_Type = TruthValue
_SecyTSAConfidentiality_Object = MibTableColumn
secyTSAConfidentiality = _SecyTSAConfidentiality_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 11, 1, 4),
    _SecyTSAConfidentiality_Type()
)
secyTSAConfidentiality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTSAConfidentiality.setStatus("current")


class _SecyTSAKeyIdentifier_Type(SnmpAdminString):
    """Custom type secyTSAKeyIdentifier based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SecyTSAKeyIdentifier_Type.__name__ = "SnmpAdminString"
_SecyTSAKeyIdentifier_Object = MibTableColumn
secyTSAKeyIdentifier = _SecyTSAKeyIdentifier_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 11, 1, 5),
    _SecyTSAKeyIdentifier_Type()
)
secyTSAKeyIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTSAKeyIdentifier.setStatus("current")
_SecyTSASSCI_Type = Integer32
_SecyTSASSCI_Object = MibTableColumn
secyTSASSCI = _SecyTSASSCI_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 11, 1, 6),
    _SecyTSASSCI_Type()
)
secyTSASSCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTSASSCI.setStatus("current")
_SecyTSACreatedTime_Type = TimeStamp
_SecyTSACreatedTime_Object = MibTableColumn
secyTSACreatedTime = _SecyTSACreatedTime_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 11, 1, 7),
    _SecyTSACreatedTime_Type()
)
secyTSACreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTSACreatedTime.setStatus("current")
_SecyTSAStartedTime_Type = TimeStamp
_SecyTSAStartedTime_Object = MibTableColumn
secyTSAStartedTime = _SecyTSAStartedTime_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 11, 1, 8),
    _SecyTSAStartedTime_Type()
)
secyTSAStartedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTSAStartedTime.setStatus("current")
_SecyTSAStoppedTime_Type = TimeStamp
_SecyTSAStoppedTime_Object = MibTableColumn
secyTSAStoppedTime = _SecyTSAStoppedTime_Object(
    (1, 0, 8802, 1, 1, 3, 1, 1, 11, 1, 9),
    _SecyTSAStoppedTime_Type()
)
secyTSAStoppedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTSAStoppedTime.setStatus("current")
_SecyStatsMIBObjects_ObjectIdentity = ObjectIdentity
secyStatsMIBObjects = _SecyStatsMIBObjects_ObjectIdentity(
    (1, 0, 8802, 1, 1, 3, 1, 2)
)
_SecyTxSAStatsTable_Object = MibTable
secyTxSAStatsTable = _SecyTxSAStatsTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    secyTxSAStatsTable.setStatus("deprecated")
_SecyTxSAStatsEntry_Object = MibTableRow
secyTxSAStatsEntry = _SecyTxSAStatsEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    secyTxSAStatsEntry.setStatus("deprecated")
_SecyTxSAStatsProtectedPkts_Type = Counter32
_SecyTxSAStatsProtectedPkts_Object = MibTableColumn
secyTxSAStatsProtectedPkts = _SecyTxSAStatsProtectedPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 1, 1, 1),
    _SecyTxSAStatsProtectedPkts_Type()
)
secyTxSAStatsProtectedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTxSAStatsProtectedPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    secyTxSAStatsProtectedPkts.setUnits("Packets")
_SecyTxSAStatsEncryptedPkts_Type = Counter32
_SecyTxSAStatsEncryptedPkts_Object = MibTableColumn
secyTxSAStatsEncryptedPkts = _SecyTxSAStatsEncryptedPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 1, 1, 2),
    _SecyTxSAStatsEncryptedPkts_Type()
)
secyTxSAStatsEncryptedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTxSAStatsEncryptedPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    secyTxSAStatsEncryptedPkts.setUnits("Packets")
_SecyTxSCStatsTable_Object = MibTable
secyTxSCStatsTable = _SecyTxSCStatsTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    secyTxSCStatsTable.setStatus("current")
_SecyTxSCStatsEntry_Object = MibTableRow
secyTxSCStatsEntry = _SecyTxSCStatsEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    secyTxSCStatsEntry.setStatus("current")
_SecyTxSCStatsProtectedPkts_Type = Counter64
_SecyTxSCStatsProtectedPkts_Object = MibTableColumn
secyTxSCStatsProtectedPkts = _SecyTxSCStatsProtectedPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 2, 1, 1),
    _SecyTxSCStatsProtectedPkts_Type()
)
secyTxSCStatsProtectedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTxSCStatsProtectedPkts.setStatus("current")
if mibBuilder.loadTexts:
    secyTxSCStatsProtectedPkts.setUnits("Packets")
_SecyTxSCStatsEncryptedPkts_Type = Counter64
_SecyTxSCStatsEncryptedPkts_Object = MibTableColumn
secyTxSCStatsEncryptedPkts = _SecyTxSCStatsEncryptedPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 2, 1, 4),
    _SecyTxSCStatsEncryptedPkts_Type()
)
secyTxSCStatsEncryptedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTxSCStatsEncryptedPkts.setStatus("current")
if mibBuilder.loadTexts:
    secyTxSCStatsEncryptedPkts.setUnits("Packets")
_SecyTxSCStatsOctetsProtected_Type = Counter64
_SecyTxSCStatsOctetsProtected_Object = MibTableColumn
secyTxSCStatsOctetsProtected = _SecyTxSCStatsOctetsProtected_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 2, 1, 10),
    _SecyTxSCStatsOctetsProtected_Type()
)
secyTxSCStatsOctetsProtected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTxSCStatsOctetsProtected.setStatus("deprecated")
if mibBuilder.loadTexts:
    secyTxSCStatsOctetsProtected.setUnits("Octets")
_SecyTxSCStatsOctetsEncrypted_Type = Counter64
_SecyTxSCStatsOctetsEncrypted_Object = MibTableColumn
secyTxSCStatsOctetsEncrypted = _SecyTxSCStatsOctetsEncrypted_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 2, 1, 11),
    _SecyTxSCStatsOctetsEncrypted_Type()
)
secyTxSCStatsOctetsEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTxSCStatsOctetsEncrypted.setStatus("deprecated")
if mibBuilder.loadTexts:
    secyTxSCStatsOctetsEncrypted.setUnits("Octets")
_SecyRxSAStatsTable_Object = MibTable
secyRxSAStatsTable = _SecyRxSAStatsTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    secyRxSAStatsTable.setStatus("deprecated")
_SecyRxSAStatsEntry_Object = MibTableRow
secyRxSAStatsEntry = _SecyRxSAStatsEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    secyRxSAStatsEntry.setStatus("deprecated")
_SecyRxSAStatsUnusedSAPkts_Type = Counter32
_SecyRxSAStatsUnusedSAPkts_Object = MibTableColumn
secyRxSAStatsUnusedSAPkts = _SecyRxSAStatsUnusedSAPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 3, 1, 1),
    _SecyRxSAStatsUnusedSAPkts_Type()
)
secyRxSAStatsUnusedSAPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSAStatsUnusedSAPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    secyRxSAStatsUnusedSAPkts.setUnits("Packets")
_SecyRxSAStatsNoUsingSAPkts_Type = Counter32
_SecyRxSAStatsNoUsingSAPkts_Object = MibTableColumn
secyRxSAStatsNoUsingSAPkts = _SecyRxSAStatsNoUsingSAPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 3, 1, 4),
    _SecyRxSAStatsNoUsingSAPkts_Type()
)
secyRxSAStatsNoUsingSAPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSAStatsNoUsingSAPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    secyRxSAStatsNoUsingSAPkts.setUnits("Packets")
_SecyRxSAStatsNotValidPkts_Type = Counter32
_SecyRxSAStatsNotValidPkts_Object = MibTableColumn
secyRxSAStatsNotValidPkts = _SecyRxSAStatsNotValidPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 3, 1, 13),
    _SecyRxSAStatsNotValidPkts_Type()
)
secyRxSAStatsNotValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSAStatsNotValidPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    secyRxSAStatsNotValidPkts.setUnits("Packets")
_SecyRxSAStatsInvalidPkts_Type = Counter32
_SecyRxSAStatsInvalidPkts_Object = MibTableColumn
secyRxSAStatsInvalidPkts = _SecyRxSAStatsInvalidPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 3, 1, 16),
    _SecyRxSAStatsInvalidPkts_Type()
)
secyRxSAStatsInvalidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSAStatsInvalidPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    secyRxSAStatsInvalidPkts.setUnits("Packets")
_SecyRxSAStatsOKPkts_Type = Counter32
_SecyRxSAStatsOKPkts_Object = MibTableColumn
secyRxSAStatsOKPkts = _SecyRxSAStatsOKPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 3, 1, 25),
    _SecyRxSAStatsOKPkts_Type()
)
secyRxSAStatsOKPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSAStatsOKPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    secyRxSAStatsOKPkts.setUnits("Packets")
_SecyRxSCStatsTable_Object = MibTable
secyRxSCStatsTable = _SecyRxSCStatsTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    secyRxSCStatsTable.setStatus("current")
_SecyRxSCStatsEntry_Object = MibTableRow
secyRxSCStatsEntry = _SecyRxSCStatsEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    secyRxSCStatsEntry.setStatus("current")
_SecyRxSCStatsUnusedSAPkts_Type = Counter64
_SecyRxSCStatsUnusedSAPkts_Object = MibTableColumn
secyRxSCStatsUnusedSAPkts = _SecyRxSCStatsUnusedSAPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 4, 1, 1),
    _SecyRxSCStatsUnusedSAPkts_Type()
)
secyRxSCStatsUnusedSAPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSCStatsUnusedSAPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    secyRxSCStatsUnusedSAPkts.setUnits("Packets")
_SecyRxSCStatsNoUsingSAPkts_Type = Counter64
_SecyRxSCStatsNoUsingSAPkts_Object = MibTableColumn
secyRxSCStatsNoUsingSAPkts = _SecyRxSCStatsNoUsingSAPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 4, 1, 2),
    _SecyRxSCStatsNoUsingSAPkts_Type()
)
secyRxSCStatsNoUsingSAPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSCStatsNoUsingSAPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    secyRxSCStatsNoUsingSAPkts.setUnits("Packets")
_SecyRxSCStatsLatePkts_Type = Counter64
_SecyRxSCStatsLatePkts_Object = MibTableColumn
secyRxSCStatsLatePkts = _SecyRxSCStatsLatePkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 4, 1, 3),
    _SecyRxSCStatsLatePkts_Type()
)
secyRxSCStatsLatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSCStatsLatePkts.setStatus("current")
if mibBuilder.loadTexts:
    secyRxSCStatsLatePkts.setUnits("Packets")
_SecyRxSCStatsNotValidPkts_Type = Counter64
_SecyRxSCStatsNotValidPkts_Object = MibTableColumn
secyRxSCStatsNotValidPkts = _SecyRxSCStatsNotValidPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 4, 1, 4),
    _SecyRxSCStatsNotValidPkts_Type()
)
secyRxSCStatsNotValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSCStatsNotValidPkts.setStatus("current")
if mibBuilder.loadTexts:
    secyRxSCStatsNotValidPkts.setUnits("Packets")
_SecyRxSCStatsInvalidPkts_Type = Counter64
_SecyRxSCStatsInvalidPkts_Object = MibTableColumn
secyRxSCStatsInvalidPkts = _SecyRxSCStatsInvalidPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 4, 1, 5),
    _SecyRxSCStatsInvalidPkts_Type()
)
secyRxSCStatsInvalidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSCStatsInvalidPkts.setStatus("current")
if mibBuilder.loadTexts:
    secyRxSCStatsInvalidPkts.setUnits("Packets")
_SecyRxSCStatsDelayedPkts_Type = Counter64
_SecyRxSCStatsDelayedPkts_Object = MibTableColumn
secyRxSCStatsDelayedPkts = _SecyRxSCStatsDelayedPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 4, 1, 6),
    _SecyRxSCStatsDelayedPkts_Type()
)
secyRxSCStatsDelayedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSCStatsDelayedPkts.setStatus("current")
if mibBuilder.loadTexts:
    secyRxSCStatsDelayedPkts.setUnits("Packets")
_SecyRxSCStatsUncheckedPkts_Type = Counter64
_SecyRxSCStatsUncheckedPkts_Object = MibTableColumn
secyRxSCStatsUncheckedPkts = _SecyRxSCStatsUncheckedPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 4, 1, 7),
    _SecyRxSCStatsUncheckedPkts_Type()
)
secyRxSCStatsUncheckedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSCStatsUncheckedPkts.setStatus("current")
if mibBuilder.loadTexts:
    secyRxSCStatsUncheckedPkts.setUnits("Packets")
_SecyRxSCStatsOKPkts_Type = Counter64
_SecyRxSCStatsOKPkts_Object = MibTableColumn
secyRxSCStatsOKPkts = _SecyRxSCStatsOKPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 4, 1, 8),
    _SecyRxSCStatsOKPkts_Type()
)
secyRxSCStatsOKPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSCStatsOKPkts.setStatus("current")
if mibBuilder.loadTexts:
    secyRxSCStatsOKPkts.setUnits("Packets")
_SecyRxSCStatsOctetsValidated_Type = Counter64
_SecyRxSCStatsOctetsValidated_Object = MibTableColumn
secyRxSCStatsOctetsValidated = _SecyRxSCStatsOctetsValidated_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 4, 1, 9),
    _SecyRxSCStatsOctetsValidated_Type()
)
secyRxSCStatsOctetsValidated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSCStatsOctetsValidated.setStatus("deprecated")
if mibBuilder.loadTexts:
    secyRxSCStatsOctetsValidated.setUnits("Octets")
_SecyRxSCStatsOctetsDecrypted_Type = Counter64
_SecyRxSCStatsOctetsDecrypted_Object = MibTableColumn
secyRxSCStatsOctetsDecrypted = _SecyRxSCStatsOctetsDecrypted_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 4, 1, 10),
    _SecyRxSCStatsOctetsDecrypted_Type()
)
secyRxSCStatsOctetsDecrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyRxSCStatsOctetsDecrypted.setStatus("deprecated")
if mibBuilder.loadTexts:
    secyRxSCStatsOctetsDecrypted.setUnits("Octets")
_SecyStatsTable_Object = MibTable
secyStatsTable = _SecyStatsTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 5)
)
if mibBuilder.loadTexts:
    secyStatsTable.setStatus("current")
_SecyStatsEntry_Object = MibTableRow
secyStatsEntry = _SecyStatsEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    secyStatsEntry.setStatus("current")
_SecyStatsTxUntaggedPkts_Type = Counter64
_SecyStatsTxUntaggedPkts_Object = MibTableColumn
secyStatsTxUntaggedPkts = _SecyStatsTxUntaggedPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 5, 1, 1),
    _SecyStatsTxUntaggedPkts_Type()
)
secyStatsTxUntaggedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyStatsTxUntaggedPkts.setStatus("current")
if mibBuilder.loadTexts:
    secyStatsTxUntaggedPkts.setUnits("Packets")
_SecyStatsTxTooLongPkts_Type = Counter64
_SecyStatsTxTooLongPkts_Object = MibTableColumn
secyStatsTxTooLongPkts = _SecyStatsTxTooLongPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 5, 1, 2),
    _SecyStatsTxTooLongPkts_Type()
)
secyStatsTxTooLongPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyStatsTxTooLongPkts.setStatus("current")
if mibBuilder.loadTexts:
    secyStatsTxTooLongPkts.setUnits("Packets")
_SecyStatsRxUntaggedPkts_Type = Counter64
_SecyStatsRxUntaggedPkts_Object = MibTableColumn
secyStatsRxUntaggedPkts = _SecyStatsRxUntaggedPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 5, 1, 3),
    _SecyStatsRxUntaggedPkts_Type()
)
secyStatsRxUntaggedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyStatsRxUntaggedPkts.setStatus("current")
if mibBuilder.loadTexts:
    secyStatsRxUntaggedPkts.setUnits("Packets")
_SecyStatsRxNoTagPkts_Type = Counter64
_SecyStatsRxNoTagPkts_Object = MibTableColumn
secyStatsRxNoTagPkts = _SecyStatsRxNoTagPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 5, 1, 4),
    _SecyStatsRxNoTagPkts_Type()
)
secyStatsRxNoTagPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyStatsRxNoTagPkts.setStatus("current")
if mibBuilder.loadTexts:
    secyStatsRxNoTagPkts.setUnits("Packets")
_SecyStatsRxBadTagPkts_Type = Counter64
_SecyStatsRxBadTagPkts_Object = MibTableColumn
secyStatsRxBadTagPkts = _SecyStatsRxBadTagPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 5, 1, 5),
    _SecyStatsRxBadTagPkts_Type()
)
secyStatsRxBadTagPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyStatsRxBadTagPkts.setStatus("current")
if mibBuilder.loadTexts:
    secyStatsRxBadTagPkts.setUnits("Packets")
_SecyStatsRxUnknownSCIPkts_Type = Counter64
_SecyStatsRxUnknownSCIPkts_Object = MibTableColumn
secyStatsRxUnknownSCIPkts = _SecyStatsRxUnknownSCIPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 5, 1, 6),
    _SecyStatsRxUnknownSCIPkts_Type()
)
secyStatsRxUnknownSCIPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyStatsRxUnknownSCIPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    secyStatsRxUnknownSCIPkts.setUnits("Packets")
_SecyStatsRxNoSCIPkts_Type = Counter64
_SecyStatsRxNoSCIPkts_Object = MibTableColumn
secyStatsRxNoSCIPkts = _SecyStatsRxNoSCIPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 5, 1, 7),
    _SecyStatsRxNoSCIPkts_Type()
)
secyStatsRxNoSCIPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyStatsRxNoSCIPkts.setStatus("deprecated")
if mibBuilder.loadTexts:
    secyStatsRxNoSCIPkts.setUnits("Packets")
_SecyStatsRxOverrunPkts_Type = Counter64
_SecyStatsRxOverrunPkts_Object = MibTableColumn
secyStatsRxOverrunPkts = _SecyStatsRxOverrunPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 5, 1, 8),
    _SecyStatsRxOverrunPkts_Type()
)
secyStatsRxOverrunPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyStatsRxOverrunPkts.setStatus("current")
if mibBuilder.loadTexts:
    secyStatsRxOverrunPkts.setUnits("Packets")
_SecyStatsRxNoSAPkts_Type = Counter64
_SecyStatsRxNoSAPkts_Object = MibTableColumn
secyStatsRxNoSAPkts = _SecyStatsRxNoSAPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 5, 1, 9),
    _SecyStatsRxNoSAPkts_Type()
)
secyStatsRxNoSAPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyStatsRxNoSAPkts.setStatus("current")
if mibBuilder.loadTexts:
    secyStatsRxNoSAPkts.setUnits("Packets")
_SecyStatsRxNoSAErrorPkts_Type = Counter64
_SecyStatsRxNoSAErrorPkts_Object = MibTableColumn
secyStatsRxNoSAErrorPkts = _SecyStatsRxNoSAErrorPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 5, 1, 10),
    _SecyStatsRxNoSAErrorPkts_Type()
)
secyStatsRxNoSAErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyStatsRxNoSAErrorPkts.setStatus("current")
if mibBuilder.loadTexts:
    secyStatsRxNoSAErrorPkts.setUnits("Packets")
_SecyStatsTxOctetsProtected_Type = Counter64
_SecyStatsTxOctetsProtected_Object = MibTableColumn
secyStatsTxOctetsProtected = _SecyStatsTxOctetsProtected_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 5, 1, 11),
    _SecyStatsTxOctetsProtected_Type()
)
secyStatsTxOctetsProtected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyStatsTxOctetsProtected.setStatus("current")
if mibBuilder.loadTexts:
    secyStatsTxOctetsProtected.setUnits("Octets")
_SecyStatsTxOctetsEncrypted_Type = Counter64
_SecyStatsTxOctetsEncrypted_Object = MibTableColumn
secyStatsTxOctetsEncrypted = _SecyStatsTxOctetsEncrypted_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 5, 1, 12),
    _SecyStatsTxOctetsEncrypted_Type()
)
secyStatsTxOctetsEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyStatsTxOctetsEncrypted.setStatus("current")
if mibBuilder.loadTexts:
    secyStatsTxOctetsEncrypted.setUnits("Octets")
_SecyStatsRxOctetsValidated_Type = Counter64
_SecyStatsRxOctetsValidated_Object = MibTableColumn
secyStatsRxOctetsValidated = _SecyStatsRxOctetsValidated_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 5, 1, 13),
    _SecyStatsRxOctetsValidated_Type()
)
secyStatsRxOctetsValidated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyStatsRxOctetsValidated.setStatus("current")
if mibBuilder.loadTexts:
    secyStatsRxOctetsValidated.setUnits("Octets")
_SecyStatsRxOctetsDecrypted_Type = Counter64
_SecyStatsRxOctetsDecrypted_Object = MibTableColumn
secyStatsRxOctetsDecrypted = _SecyStatsRxOctetsDecrypted_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 5, 1, 14),
    _SecyStatsRxOctetsDecrypted_Type()
)
secyStatsRxOctetsDecrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyStatsRxOctetsDecrypted.setStatus("current")
if mibBuilder.loadTexts:
    secyStatsRxOctetsDecrypted.setUnits("Octets")
_SecyTSCStatsTable_Object = MibTable
secyTSCStatsTable = _SecyTSCStatsTable_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 12)
)
if mibBuilder.loadTexts:
    secyTSCStatsTable.setStatus("current")
_SecyTSCStatsEntry_Object = MibTableRow
secyTSCStatsEntry = _SecyTSCStatsEntry_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 12, 1)
)
if mibBuilder.loadTexts:
    secyTSCStatsEntry.setStatus("current")
_SecyTSCStatsProtectedPkts_Type = Counter64
_SecyTSCStatsProtectedPkts_Object = MibTableColumn
secyTSCStatsProtectedPkts = _SecyTSCStatsProtectedPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 12, 1, 1),
    _SecyTSCStatsProtectedPkts_Type()
)
secyTSCStatsProtectedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTSCStatsProtectedPkts.setStatus("current")
if mibBuilder.loadTexts:
    secyTSCStatsProtectedPkts.setUnits("Packets")
_SecyTSCStatsEncryptedPkts_Type = Counter64
_SecyTSCStatsEncryptedPkts_Object = MibTableColumn
secyTSCStatsEncryptedPkts = _SecyTSCStatsEncryptedPkts_Object(
    (1, 0, 8802, 1, 1, 3, 1, 2, 12, 1, 2),
    _SecyTSCStatsEncryptedPkts_Type()
)
secyTSCStatsEncryptedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secyTSCStatsEncryptedPkts.setStatus("current")
if mibBuilder.loadTexts:
    secyTSCStatsEncryptedPkts.setUnits("Packets")
_SecyMIBConformance_ObjectIdentity = ObjectIdentity
secyMIBConformance = _SecyMIBConformance_ObjectIdentity(
    (1, 0, 8802, 1, 1, 3, 2)
)
_SecyMIBCompliances_ObjectIdentity = ObjectIdentity
secyMIBCompliances = _SecyMIBCompliances_ObjectIdentity(
    (1, 0, 8802, 1, 1, 3, 2, 1)
)
_SecyMIBGroups_ObjectIdentity = ObjectIdentity
secyMIBGroups = _SecyMIBGroups_ObjectIdentity(
    (1, 0, 8802, 1, 1, 3, 2, 2)
)
secyTxSAEntry.registerAugmentions(
    ("IEEE8021-SECY-MIB",
     "secyTxSAStatsEntry")
)
secyTxSAStatsEntry.setIndexNames(*secyTxSAEntry.getIndexNames())
secyTxSCEntry.registerAugmentions(
    ("IEEE8021-SECY-MIB",
     "secyTxSCStatsEntry")
)
secyTxSCStatsEntry.setIndexNames(*secyTxSCEntry.getIndexNames())
secyRxSAEntry.registerAugmentions(
    ("IEEE8021-SECY-MIB",
     "secyRxSAStatsEntry")
)
secyRxSAStatsEntry.setIndexNames(*secyRxSAEntry.getIndexNames())
secyRxSCEntry.registerAugmentions(
    ("IEEE8021-SECY-MIB",
     "secyRxSCStatsEntry")
)
secyRxSCStatsEntry.setIndexNames(*secyRxSCEntry.getIndexNames())
secyIfEntry.registerAugmentions(
    ("IEEE8021-SECY-MIB",
     "secyStatsEntry")
)
secyStatsEntry.setIndexNames(*secyIfEntry.getIndexNames())
secyTSCEntry.registerAugmentions(
    ("IEEE8021-SECY-MIB",
     "secyTSCStatsEntry")
)
secyTSCStatsEntry.setIndexNames(*secyTSCEntry.getIndexNames())

# Managed Objects groups

secyIfCtrlGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 1)
)
secyIfCtrlGroup.setObjects(
      *(("IEEE8021-SECY-MIB", "secyIfMaxPeerSCs"),
        ("IEEE8021-SECY-MIB", "secyIfRxMaxKeys"),
        ("IEEE8021-SECY-MIB", "secyIfTxMaxKeys"),
        ("IEEE8021-SECY-MIB", "secyIfProtectFramesEnable"),
        ("IEEE8021-SECY-MIB", "secyIfValidateFrames"),
        ("IEEE8021-SECY-MIB", "secyIfReplayProtectEnable"),
        ("IEEE8021-SECY-MIB", "secyIfReplayProtectWindow"),
        ("IEEE8021-SECY-MIB", "secyIfCurrentCipherSuite"),
        ("IEEE8021-SECY-MIB", "secyIfAdminPt2PtMAC"),
        ("IEEE8021-SECY-MIB", "secyIfOperPt2PtMAC"),
        ("IEEE8021-SECY-MIB", "secyIfIncludeSCIEnable"),
        ("IEEE8021-SECY-MIB", "secyIfUseESEnable"),
        ("IEEE8021-SECY-MIB", "secyIfUseSCBEnable"))
)
if mibBuilder.loadTexts:
    secyIfCtrlGroup.setStatus("deprecated")

secyTxSCGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 2)
)
secyTxSCGroup.setObjects(
      *(("IEEE8021-SECY-MIB", "secyTxSCI"),
        ("IEEE8021-SECY-MIB", "secyTxSCState"),
        ("IEEE8021-SECY-MIB", "secyTxSCEncodingSA"),
        ("IEEE8021-SECY-MIB", "secyTxSCEncipheringSA"),
        ("IEEE8021-SECY-MIB", "secyTxSCCreatedTime"),
        ("IEEE8021-SECY-MIB", "secyTxSCStartedTime"),
        ("IEEE8021-SECY-MIB", "secyTxSCStoppedTime"))
)
if mibBuilder.loadTexts:
    secyTxSCGroup.setStatus("deprecated")

secyTxSAGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 3)
)
secyTxSAGroup.setObjects(
      *(("IEEE8021-SECY-MIB", "secyTxSAState"),
        ("IEEE8021-SECY-MIB", "secyTxSANextPN"),
        ("IEEE8021-SECY-MIB", "secyTxSAConfidentiality"),
        ("IEEE8021-SECY-MIB", "secyTxSASAKUnchanged"),
        ("IEEE8021-SECY-MIB", "secyTxSACreatedTime"),
        ("IEEE8021-SECY-MIB", "secyTxSAStartedTime"),
        ("IEEE8021-SECY-MIB", "secyTxSAStoppedTime"))
)
if mibBuilder.loadTexts:
    secyTxSAGroup.setStatus("deprecated")

secyRxSCGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 4)
)
secyRxSCGroup.setObjects(
      *(("IEEE8021-SECY-MIB", "secyRxSCState"),
        ("IEEE8021-SECY-MIB", "secyRxSCCurrentSA"),
        ("IEEE8021-SECY-MIB", "secyRxSCCreatedTime"),
        ("IEEE8021-SECY-MIB", "secyRxSCStartedTime"),
        ("IEEE8021-SECY-MIB", "secyRxSCStoppedTime"))
)
if mibBuilder.loadTexts:
    secyRxSCGroup.setStatus("deprecated")

secyRxSAGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 5)
)
secyRxSAGroup.setObjects(
      *(("IEEE8021-SECY-MIB", "secyRxSAState"),
        ("IEEE8021-SECY-MIB", "secyRxSANextPN"),
        ("IEEE8021-SECY-MIB", "secyRxSASAKUnchanged"),
        ("IEEE8021-SECY-MIB", "secyRxSACreatedTime"),
        ("IEEE8021-SECY-MIB", "secyRxSAStartedTime"),
        ("IEEE8021-SECY-MIB", "secyRxSAStoppedTime"))
)
if mibBuilder.loadTexts:
    secyRxSAGroup.setStatus("deprecated")

secyCipherSuiteGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 6)
)
secyCipherSuiteGroup.setObjects(
      *(("IEEE8021-SECY-MIB", "secyCipherSuiteId"),
        ("IEEE8021-SECY-MIB", "secyCipherSuiteName"),
        ("IEEE8021-SECY-MIB", "secyCipherSuiteCapability"),
        ("IEEE8021-SECY-MIB", "secyCipherSuiteProtection"),
        ("IEEE8021-SECY-MIB", "secyCipherSuiteProtectionOffset"),
        ("IEEE8021-SECY-MIB", "secyCipherSuiteDataLengthChange"),
        ("IEEE8021-SECY-MIB", "secyCipherSuiteICVLength"),
        ("IEEE8021-SECY-MIB", "secyCipherSuiteRowStatus"))
)
if mibBuilder.loadTexts:
    secyCipherSuiteGroup.setStatus("deprecated")

secyTxSAStatsGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 7)
)
secyTxSAStatsGroup.setObjects(
      *(("IEEE8021-SECY-MIB", "secyTxSAStatsProtectedPkts"),
        ("IEEE8021-SECY-MIB", "secyTxSAStatsEncryptedPkts"))
)
if mibBuilder.loadTexts:
    secyTxSAStatsGroup.setStatus("deprecated")

secyRxSAStatsGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 8)
)
secyRxSAStatsGroup.setObjects(
      *(("IEEE8021-SECY-MIB", "secyRxSAStatsUnusedSAPkts"),
        ("IEEE8021-SECY-MIB", "secyRxSAStatsNoUsingSAPkts"),
        ("IEEE8021-SECY-MIB", "secyRxSAStatsNotValidPkts"),
        ("IEEE8021-SECY-MIB", "secyRxSAStatsInvalidPkts"),
        ("IEEE8021-SECY-MIB", "secyRxSAStatsOKPkts"))
)
if mibBuilder.loadTexts:
    secyRxSAStatsGroup.setStatus("deprecated")

secyTxSCStatsGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 9)
)
secyTxSCStatsGroup.setObjects(
      *(("IEEE8021-SECY-MIB", "secyTxSCStatsProtectedPkts"),
        ("IEEE8021-SECY-MIB", "secyTxSCStatsEncryptedPkts"),
        ("IEEE8021-SECY-MIB", "secyTxSCStatsOctetsProtected"),
        ("IEEE8021-SECY-MIB", "secyTxSCStatsOctetsEncrypted"))
)
if mibBuilder.loadTexts:
    secyTxSCStatsGroup.setStatus("deprecated")

secyRxSCStatsGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 10)
)
secyRxSCStatsGroup.setObjects(
      *(("IEEE8021-SECY-MIB", "secyRxSCStatsUnusedSAPkts"),
        ("IEEE8021-SECY-MIB", "secyRxSCStatsNoUsingSAPkts"),
        ("IEEE8021-SECY-MIB", "secyRxSCStatsLatePkts"),
        ("IEEE8021-SECY-MIB", "secyRxSCStatsNotValidPkts"),
        ("IEEE8021-SECY-MIB", "secyRxSCStatsInvalidPkts"),
        ("IEEE8021-SECY-MIB", "secyRxSCStatsDelayedPkts"),
        ("IEEE8021-SECY-MIB", "secyRxSCStatsUncheckedPkts"),
        ("IEEE8021-SECY-MIB", "secyRxSCStatsOKPkts"),
        ("IEEE8021-SECY-MIB", "secyRxSCStatsOctetsValidated"),
        ("IEEE8021-SECY-MIB", "secyRxSCStatsOctetsDecrypted"))
)
if mibBuilder.loadTexts:
    secyRxSCStatsGroup.setStatus("deprecated")

secyStatsGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 11)
)
secyStatsGroup.setObjects(
      *(("IEEE8021-SECY-MIB", "secyStatsTxUntaggedPkts"),
        ("IEEE8021-SECY-MIB", "secyStatsTxTooLongPkts"),
        ("IEEE8021-SECY-MIB", "secyStatsRxUntaggedPkts"),
        ("IEEE8021-SECY-MIB", "secyStatsRxNoTagPkts"),
        ("IEEE8021-SECY-MIB", "secyStatsRxBadTagPkts"),
        ("IEEE8021-SECY-MIB", "secyStatsRxUnknownSCIPkts"),
        ("IEEE8021-SECY-MIB", "secyStatsRxNoSCIPkts"),
        ("IEEE8021-SECY-MIB", "secyStatsRxOverrunPkts"))
)
if mibBuilder.loadTexts:
    secyStatsGroup.setStatus("deprecated")

secyIfGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 12)
)
secyIfGroup.setObjects(
      *(("IEEE8021-SECY-MIB", "secyIfMaxPeerSCs"),
        ("IEEE8021-SECY-MIB", "secyIfRxMaxKeys"),
        ("IEEE8021-SECY-MIB", "secyIfTxMaxKeys"),
        ("IEEE8021-SECY-MIB", "secyIfProtectFramesEnable"),
        ("IEEE8021-SECY-MIB", "secyIfValidateFrames"),
        ("IEEE8021-SECY-MIB", "secyIfReplayProtectEnable"),
        ("IEEE8021-SECY-MIB", "secyIfReplayProtectWindow"),
        ("IEEE8021-SECY-MIB", "secyIfCurrentCipherSuite"),
        ("IEEE8021-SECY-MIB", "secyIfAdminPt2PtMAC"),
        ("IEEE8021-SECY-MIB", "secyIfOperPt2PtMAC"),
        ("IEEE8021-SECY-MIB", "secyIfIncludeSCIEnable"),
        ("IEEE8021-SECY-MIB", "secyIfUseESEnable"),
        ("IEEE8021-SECY-MIB", "secyIfUseSCBEnable"),
        ("IEEE8021-SECY-MIB", "secyIfSCI"),
        ("IEEE8021-SECY-MIB", "secyIfIncludingSCI"),
        ("IEEE8021-SECY-MIB", "secyIfMaxTSCs"))
)
if mibBuilder.loadTexts:
    secyIfGroup.setStatus("current")

secyIfCipherGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 13)
)
secyIfCipherGroup.setObjects(
      *(("IEEE8021-SECY-MIB", "secyIfCipherImplemented"),
        ("IEEE8021-SECY-MIB", "secyIfCipherEnableUse"),
        ("IEEE8021-SECY-MIB", "secyIfCipherRqConfidentiality"))
)
if mibBuilder.loadTexts:
    secyIfCipherGroup.setStatus("current")

secyIfTCGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 14)
)
secyIfTCGroup.setObjects(
    ("IEEE8021-SECY-MIB", "secyIfTCTrafficClass")
)
if mibBuilder.loadTexts:
    secyIfTCGroup.setStatus("current")

secyIfAPGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 15)
)
secyIfAPGroup.setObjects(
    ("IEEE8021-SECY-MIB", "secyIfAPAccessPCP")
)
if mibBuilder.loadTexts:
    secyIfAPGroup.setStatus("current")

secyTSCGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 16)
)
secyTSCGroup.setObjects(
      *(("IEEE8021-SECY-MIB", "secyTSCState"),
        ("IEEE8021-SECY-MIB", "secyTSCEncodingSA"),
        ("IEEE8021-SECY-MIB", "secyTSCCreatedTime"),
        ("IEEE8021-SECY-MIB", "secyTSCStartedTime"),
        ("IEEE8021-SECY-MIB", "secyTSCStoppedTime"))
)
if mibBuilder.loadTexts:
    secyTSCGroup.setStatus("current")

secyTSAGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 17)
)
secyTSAGroup.setObjects(
      *(("IEEE8021-SECY-MIB", "secyTSAState"),
        ("IEEE8021-SECY-MIB", "secyTSANextXPN"),
        ("IEEE8021-SECY-MIB", "secyTSAConfidentiality"),
        ("IEEE8021-SECY-MIB", "secyTSAKeyIdentifier"),
        ("IEEE8021-SECY-MIB", "secyTSASSCI"),
        ("IEEE8021-SECY-MIB", "secyTSACreatedTime"),
        ("IEEE8021-SECY-MIB", "secyTSAStartedTime"),
        ("IEEE8021-SECY-MIB", "secyTSAStoppedTime"))
)
if mibBuilder.loadTexts:
    secyTSAGroup.setStatus("current")

secyRSCGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 18)
)
secyRSCGroup.setObjects(
      *(("IEEE8021-SECY-MIB", "secyRxSCState"),
        ("IEEE8021-SECY-MIB", "secyRxSCCreatedTime"),
        ("IEEE8021-SECY-MIB", "secyRxSCStartedTime"),
        ("IEEE8021-SECY-MIB", "secyRxSCStoppedTime"))
)
if mibBuilder.loadTexts:
    secyRSCGroup.setStatus("current")

secyRSAGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 19)
)
secyRSAGroup.setObjects(
      *(("IEEE8021-SECY-MIB", "secyRxSAState"),
        ("IEEE8021-SECY-MIB", "secyRxSANextXPN"),
        ("IEEE8021-SECY-MIB", "secyRxSALowestXPN"),
        ("IEEE8021-SECY-MIB", "secyRxSAKeyIdentifier"),
        ("IEEE8021-SECY-MIB", "secyRxSASSCI"),
        ("IEEE8021-SECY-MIB", "secyRxSACreatedTime"),
        ("IEEE8021-SECY-MIB", "secyRxSAStartedTime"),
        ("IEEE8021-SECY-MIB", "secyRxSAStoppedTime"))
)
if mibBuilder.loadTexts:
    secyRSAGroup.setStatus("current")

secyIfStatsGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 20)
)
secyIfStatsGroup.setObjects(
      *(("IEEE8021-SECY-MIB", "secyStatsTxUntaggedPkts"),
        ("IEEE8021-SECY-MIB", "secyStatsTxTooLongPkts"),
        ("IEEE8021-SECY-MIB", "secyStatsRxUntaggedPkts"),
        ("IEEE8021-SECY-MIB", "secyStatsRxNoTagPkts"),
        ("IEEE8021-SECY-MIB", "secyStatsRxBadTagPkts"),
        ("IEEE8021-SECY-MIB", "secyStatsRxNoSAPkts"),
        ("IEEE8021-SECY-MIB", "secyStatsRxNoSAErrorPkts"),
        ("IEEE8021-SECY-MIB", "secyStatsRxOverrunPkts"))
)
if mibBuilder.loadTexts:
    secyIfStatsGroup.setStatus("current")

secyCipherInfoGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 21)
)
secyCipherInfoGroup.setObjects(
      *(("IEEE8021-SECY-MIB", "secyCipherSuiteId"),
        ("IEEE8021-SECY-MIB", "secyCipherSuiteName"),
        ("IEEE8021-SECY-MIB", "secyCipherSuiteCapability"),
        ("IEEE8021-SECY-MIB", "secyCipherSuiteDataLengthChange"),
        ("IEEE8021-SECY-MIB", "secyCipherSuiteICVLength"))
)
if mibBuilder.loadTexts:
    secyCipherInfoGroup.setStatus("current")

secyTSCStatsGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 22)
)
secyTSCStatsGroup.setObjects(
      *(("IEEE8021-SECY-MIB", "secyTSCStatsProtectedPkts"),
        ("IEEE8021-SECY-MIB", "secyTSCStatsEncryptedPkts"))
)
if mibBuilder.loadTexts:
    secyTSCStatsGroup.setStatus("current")

secyRSCStatsGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 23)
)
secyRSCStatsGroup.setObjects(
      *(("IEEE8021-SECY-MIB", "secyRxSCStatsLatePkts"),
        ("IEEE8021-SECY-MIB", "secyRxSCStatsNotValidPkts"),
        ("IEEE8021-SECY-MIB", "secyRxSCStatsInvalidPkts"),
        ("IEEE8021-SECY-MIB", "secyRxSCStatsDelayedPkts"),
        ("IEEE8021-SECY-MIB", "secyRxSCStatsUncheckedPkts"),
        ("IEEE8021-SECY-MIB", "secyRxSCStatsOKPkts"))
)
if mibBuilder.loadTexts:
    secyRSCStatsGroup.setStatus("current")

secyCipherStatsGroup = ObjectGroup(
    (1, 0, 8802, 1, 1, 3, 2, 2, 24)
)
secyCipherStatsGroup.setObjects(
      *(("IEEE8021-SECY-MIB", "secyStatsTxOctetsProtected"),
        ("IEEE8021-SECY-MIB", "secyStatsTxOctetsEncrypted"),
        ("IEEE8021-SECY-MIB", "secyStatsRxOctetsValidated"),
        ("IEEE8021-SECY-MIB", "secyStatsRxOctetsDecrypted"))
)
if mibBuilder.loadTexts:
    secyCipherStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

secyMIBCompliance = ModuleCompliance(
    (1, 0, 8802, 1, 1, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    secyMIBCompliance.setStatus(
        "deprecated"
    )

secyMIBTcCompliance = ModuleCompliance(
    (1, 0, 8802, 1, 1, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    secyMIBTcCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-SECY-MIB",
    **{"SecySCI": SecySCI,
       "SecyAN": SecyAN,
       "ieee8021SecyMIB": ieee8021SecyMIB,
       "secyMIBNotifications": secyMIBNotifications,
       "secyMIBObjects": secyMIBObjects,
       "secyMgmtMIBObjects": secyMgmtMIBObjects,
       "secyIfTable": secyIfTable,
       "secyIfEntry": secyIfEntry,
       "secyIfInterfaceIndex": secyIfInterfaceIndex,
       "secyIfMaxPeerSCs": secyIfMaxPeerSCs,
       "secyIfRxMaxKeys": secyIfRxMaxKeys,
       "secyIfTxMaxKeys": secyIfTxMaxKeys,
       "secyIfProtectFramesEnable": secyIfProtectFramesEnable,
       "secyIfValidateFrames": secyIfValidateFrames,
       "secyIfReplayProtectEnable": secyIfReplayProtectEnable,
       "secyIfReplayProtectWindow": secyIfReplayProtectWindow,
       "secyIfCurrentCipherSuite": secyIfCurrentCipherSuite,
       "secyIfAdminPt2PtMAC": secyIfAdminPt2PtMAC,
       "secyIfOperPt2PtMAC": secyIfOperPt2PtMAC,
       "secyIfIncludeSCIEnable": secyIfIncludeSCIEnable,
       "secyIfUseESEnable": secyIfUseESEnable,
       "secyIfUseSCBEnable": secyIfUseSCBEnable,
       "secyIfSCI": secyIfSCI,
       "secyIfIncludingSCI": secyIfIncludingSCI,
       "secyIfMaxTSCs": secyIfMaxTSCs,
       "secyTxSCTable": secyTxSCTable,
       "secyTxSCEntry": secyTxSCEntry,
       "secyTxSCI": secyTxSCI,
       "secyTxSCState": secyTxSCState,
       "secyTxSCEncodingSA": secyTxSCEncodingSA,
       "secyTxSCEncipheringSA": secyTxSCEncipheringSA,
       "secyTxSCCreatedTime": secyTxSCCreatedTime,
       "secyTxSCStartedTime": secyTxSCStartedTime,
       "secyTxSCStoppedTime": secyTxSCStoppedTime,
       "secyTxSATable": secyTxSATable,
       "secyTxSAEntry": secyTxSAEntry,
       "secyTxSA": secyTxSA,
       "secyTxSAState": secyTxSAState,
       "secyTxSANextPN": secyTxSANextPN,
       "secyTxSAConfidentiality": secyTxSAConfidentiality,
       "secyTxSASAKUnchanged": secyTxSASAKUnchanged,
       "secyTxSACreatedTime": secyTxSACreatedTime,
       "secyTxSAStartedTime": secyTxSAStartedTime,
       "secyTxSAStoppedTime": secyTxSAStoppedTime,
       "secyRxSCTable": secyRxSCTable,
       "secyRxSCEntry": secyRxSCEntry,
       "secyRxSCI": secyRxSCI,
       "secyRxSCState": secyRxSCState,
       "secyRxSCCurrentSA": secyRxSCCurrentSA,
       "secyRxSCCreatedTime": secyRxSCCreatedTime,
       "secyRxSCStartedTime": secyRxSCStartedTime,
       "secyRxSCStoppedTime": secyRxSCStoppedTime,
       "secyRxSATable": secyRxSATable,
       "secyRxSAEntry": secyRxSAEntry,
       "secyRxSA": secyRxSA,
       "secyRxSAState": secyRxSAState,
       "secyRxSANextPN": secyRxSANextPN,
       "secyRxSASAKUnchanged": secyRxSASAKUnchanged,
       "secyRxSACreatedTime": secyRxSACreatedTime,
       "secyRxSAStartedTime": secyRxSAStartedTime,
       "secyRxSAStoppedTime": secyRxSAStoppedTime,
       "secyRxSANextXPN": secyRxSANextXPN,
       "secyRxSALowestXPN": secyRxSALowestXPN,
       "secyRxSAKeyIdentifier": secyRxSAKeyIdentifier,
       "secyRxSASSCI": secyRxSASSCI,
       "secyCipherSuiteTable": secyCipherSuiteTable,
       "secyCipherSuiteEntry": secyCipherSuiteEntry,
       "secyCipherSuiteIndex": secyCipherSuiteIndex,
       "secyCipherSuiteId": secyCipherSuiteId,
       "secyCipherSuiteName": secyCipherSuiteName,
       "secyCipherSuiteCapability": secyCipherSuiteCapability,
       "secyCipherSuiteProtection": secyCipherSuiteProtection,
       "secyCipherSuiteProtectionOffset": secyCipherSuiteProtectionOffset,
       "secyCipherSuiteDataLengthChange": secyCipherSuiteDataLengthChange,
       "secyCipherSuiteICVLength": secyCipherSuiteICVLength,
       "secyCipherSuiteRowStatus": secyCipherSuiteRowStatus,
       "secyIfCipherTable": secyIfCipherTable,
       "secyIfCipherEntry": secyIfCipherEntry,
       "secyIfCipherImplemented": secyIfCipherImplemented,
       "secyIfCipherEnableUse": secyIfCipherEnableUse,
       "secyIfCipherRqConfidentiality": secyIfCipherRqConfidentiality,
       "secyIfTCTable": secyIfTCTable,
       "secyIfTCEntry": secyIfTCEntry,
       "secyIfTCUserPriority": secyIfTCUserPriority,
       "secyIfTCTrafficClass": secyIfTCTrafficClass,
       "secyIfAPTable": secyIfAPTable,
       "secyIfAPEntry": secyIfAPEntry,
       "secyIfAPUserPCP": secyIfAPUserPCP,
       "secyIfAPAccessPCP": secyIfAPAccessPCP,
       "secyTSCTable": secyTSCTable,
       "secyTSCEntry": secyTSCEntry,
       "secyTSCI": secyTSCI,
       "secyTSCState": secyTSCState,
       "secyTSCEncodingSA": secyTSCEncodingSA,
       "secyTSCCreatedTime": secyTSCCreatedTime,
       "secyTSCStartedTime": secyTSCStartedTime,
       "secyTSCStoppedTime": secyTSCStoppedTime,
       "secyTSATable": secyTSATable,
       "secyTSAEntry": secyTSAEntry,
       "secyTSA": secyTSA,
       "secyTSAState": secyTSAState,
       "secyTSANextXPN": secyTSANextXPN,
       "secyTSAConfidentiality": secyTSAConfidentiality,
       "secyTSAKeyIdentifier": secyTSAKeyIdentifier,
       "secyTSASSCI": secyTSASSCI,
       "secyTSACreatedTime": secyTSACreatedTime,
       "secyTSAStartedTime": secyTSAStartedTime,
       "secyTSAStoppedTime": secyTSAStoppedTime,
       "secyStatsMIBObjects": secyStatsMIBObjects,
       "secyTxSAStatsTable": secyTxSAStatsTable,
       "secyTxSAStatsEntry": secyTxSAStatsEntry,
       "secyTxSAStatsProtectedPkts": secyTxSAStatsProtectedPkts,
       "secyTxSAStatsEncryptedPkts": secyTxSAStatsEncryptedPkts,
       "secyTxSCStatsTable": secyTxSCStatsTable,
       "secyTxSCStatsEntry": secyTxSCStatsEntry,
       "secyTxSCStatsProtectedPkts": secyTxSCStatsProtectedPkts,
       "secyTxSCStatsEncryptedPkts": secyTxSCStatsEncryptedPkts,
       "secyTxSCStatsOctetsProtected": secyTxSCStatsOctetsProtected,
       "secyTxSCStatsOctetsEncrypted": secyTxSCStatsOctetsEncrypted,
       "secyRxSAStatsTable": secyRxSAStatsTable,
       "secyRxSAStatsEntry": secyRxSAStatsEntry,
       "secyRxSAStatsUnusedSAPkts": secyRxSAStatsUnusedSAPkts,
       "secyRxSAStatsNoUsingSAPkts": secyRxSAStatsNoUsingSAPkts,
       "secyRxSAStatsNotValidPkts": secyRxSAStatsNotValidPkts,
       "secyRxSAStatsInvalidPkts": secyRxSAStatsInvalidPkts,
       "secyRxSAStatsOKPkts": secyRxSAStatsOKPkts,
       "secyRxSCStatsTable": secyRxSCStatsTable,
       "secyRxSCStatsEntry": secyRxSCStatsEntry,
       "secyRxSCStatsUnusedSAPkts": secyRxSCStatsUnusedSAPkts,
       "secyRxSCStatsNoUsingSAPkts": secyRxSCStatsNoUsingSAPkts,
       "secyRxSCStatsLatePkts": secyRxSCStatsLatePkts,
       "secyRxSCStatsNotValidPkts": secyRxSCStatsNotValidPkts,
       "secyRxSCStatsInvalidPkts": secyRxSCStatsInvalidPkts,
       "secyRxSCStatsDelayedPkts": secyRxSCStatsDelayedPkts,
       "secyRxSCStatsUncheckedPkts": secyRxSCStatsUncheckedPkts,
       "secyRxSCStatsOKPkts": secyRxSCStatsOKPkts,
       "secyRxSCStatsOctetsValidated": secyRxSCStatsOctetsValidated,
       "secyRxSCStatsOctetsDecrypted": secyRxSCStatsOctetsDecrypted,
       "secyStatsTable": secyStatsTable,
       "secyStatsEntry": secyStatsEntry,
       "secyStatsTxUntaggedPkts": secyStatsTxUntaggedPkts,
       "secyStatsTxTooLongPkts": secyStatsTxTooLongPkts,
       "secyStatsRxUntaggedPkts": secyStatsRxUntaggedPkts,
       "secyStatsRxNoTagPkts": secyStatsRxNoTagPkts,
       "secyStatsRxBadTagPkts": secyStatsRxBadTagPkts,
       "secyStatsRxUnknownSCIPkts": secyStatsRxUnknownSCIPkts,
       "secyStatsRxNoSCIPkts": secyStatsRxNoSCIPkts,
       "secyStatsRxOverrunPkts": secyStatsRxOverrunPkts,
       "secyStatsRxNoSAPkts": secyStatsRxNoSAPkts,
       "secyStatsRxNoSAErrorPkts": secyStatsRxNoSAErrorPkts,
       "secyStatsTxOctetsProtected": secyStatsTxOctetsProtected,
       "secyStatsTxOctetsEncrypted": secyStatsTxOctetsEncrypted,
       "secyStatsRxOctetsValidated": secyStatsRxOctetsValidated,
       "secyStatsRxOctetsDecrypted": secyStatsRxOctetsDecrypted,
       "secyTSCStatsTable": secyTSCStatsTable,
       "secyTSCStatsEntry": secyTSCStatsEntry,
       "secyTSCStatsProtectedPkts": secyTSCStatsProtectedPkts,
       "secyTSCStatsEncryptedPkts": secyTSCStatsEncryptedPkts,
       "secyMIBConformance": secyMIBConformance,
       "secyMIBCompliances": secyMIBCompliances,
       "secyMIBCompliance": secyMIBCompliance,
       "secyMIBTcCompliance": secyMIBTcCompliance,
       "secyMIBGroups": secyMIBGroups,
       "secyIfCtrlGroup": secyIfCtrlGroup,
       "secyTxSCGroup": secyTxSCGroup,
       "secyTxSAGroup": secyTxSAGroup,
       "secyRxSCGroup": secyRxSCGroup,
       "secyRxSAGroup": secyRxSAGroup,
       "secyCipherSuiteGroup": secyCipherSuiteGroup,
       "secyTxSAStatsGroup": secyTxSAStatsGroup,
       "secyRxSAStatsGroup": secyRxSAStatsGroup,
       "secyTxSCStatsGroup": secyTxSCStatsGroup,
       "secyRxSCStatsGroup": secyRxSCStatsGroup,
       "secyStatsGroup": secyStatsGroup,
       "secyIfGroup": secyIfGroup,
       "secyIfCipherGroup": secyIfCipherGroup,
       "secyIfTCGroup": secyIfTCGroup,
       "secyIfAPGroup": secyIfAPGroup,
       "secyTSCGroup": secyTSCGroup,
       "secyTSAGroup": secyTSAGroup,
       "secyRSCGroup": secyRSCGroup,
       "secyRSAGroup": secyRSAGroup,
       "secyIfStatsGroup": secyIfStatsGroup,
       "secyCipherInfoGroup": secyCipherInfoGroup,
       "secyTSCStatsGroup": secyTSCStatsGroup,
       "secyRSCStatsGroup": secyRSCStatsGroup,
       "secyCipherStatsGroup": secyCipherStatsGroup}
)
