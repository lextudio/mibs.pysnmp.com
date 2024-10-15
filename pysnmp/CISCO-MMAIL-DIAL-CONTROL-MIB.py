# SNMP MIB module (CISCO-MMAIL-DIAL-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MMAIL-DIAL-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:44 2024
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

(cCallHistoryIndex,) = mibBuilder.importSymbols(
    "CISCO-DIAL-CONTROL-MIB",
    "cCallHistoryIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CvcGUid,) = mibBuilder.importSymbols(
    "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB",
    "CvcGUid")

(AbsoluteCounter32,
 callActiveIndex,
 callActiveSetupTime) = mibBuilder.importSymbols(
    "DIAL-CONTROL-MIB",
    "AbsoluteCounter32",
    "callActiveIndex",
    "callActiveSetupTime")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoMediaMailDialControlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 102)
)
ciscoMediaMailDialControlMIB.setRevisions(
        ("2002-02-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CmmImgResolution(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fine", 3),
          ("standard", 2),
          ("superFine", 4))
    )



class CmmImgResolutionOrTransparent(Integer32, TextualConvention):
    status = "current"
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
        *(("fine", 3),
          ("standard", 2),
          ("superFine", 4),
          ("transparent", 1))
    )



class CmmImgEncoding(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("modifiedHuffman", 2),
          ("modifiedMR", 4),
          ("modifiedREAD", 3))
    )



class CmmImgEncodingOrTransparent(Integer32, TextualConvention):
    status = "current"
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
        *(("modifiedHuffman", 2),
          ("modifiedMR", 4),
          ("modifiedREAD", 3),
          ("transparent", 1))
    )



class CmmFaxHeadingString(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )



# MIB Managed Objects in the order of their OIDs

_CmmdcMIBObjects_ObjectIdentity = ObjectIdentity
cmmdcMIBObjects = _CmmdcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1)
)
_CmmPeer_ObjectIdentity = ObjectIdentity
cmmPeer = _CmmPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 1)
)
_CmmIpPeerCfgTable_Object = MibTable
cmmIpPeerCfgTable = _CmmIpPeerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cmmIpPeerCfgTable.setStatus("current")
_CmmIpPeerCfgEntry_Object = MibTableRow
cmmIpPeerCfgEntry = _CmmIpPeerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 1, 1, 1)
)
cmmIpPeerCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cmmIpPeerCfgEntry.setStatus("current")


class _CmmIpPeerCfgSessionProtocol_Type(Integer32):
    """Custom type cmmIpPeerCfgSessionProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("smtp", 1)
    )


_CmmIpPeerCfgSessionProtocol_Type.__name__ = "Integer32"
_CmmIpPeerCfgSessionProtocol_Object = MibTableColumn
cmmIpPeerCfgSessionProtocol = _CmmIpPeerCfgSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 1, 1, 1, 1),
    _CmmIpPeerCfgSessionProtocol_Type()
)
cmmIpPeerCfgSessionProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmIpPeerCfgSessionProtocol.setStatus("current")
_CmmIpPeerCfgSessionTarget_Type = DisplayString
_CmmIpPeerCfgSessionTarget_Object = MibTableColumn
cmmIpPeerCfgSessionTarget = _CmmIpPeerCfgSessionTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 1, 1, 1, 2),
    _CmmIpPeerCfgSessionTarget_Type()
)
cmmIpPeerCfgSessionTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmIpPeerCfgSessionTarget.setStatus("current")


class _CmmIpPeerCfgImgEncodingType_Type(CmmImgEncodingOrTransparent):
    """Custom type cmmIpPeerCfgImgEncodingType based on CmmImgEncodingOrTransparent"""


_CmmIpPeerCfgImgEncodingType_Object = MibTableColumn
cmmIpPeerCfgImgEncodingType = _CmmIpPeerCfgImgEncodingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 1, 1, 1, 3),
    _CmmIpPeerCfgImgEncodingType_Type()
)
cmmIpPeerCfgImgEncodingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmIpPeerCfgImgEncodingType.setStatus("current")


class _CmmIpPeerCfgImgResolution_Type(CmmImgResolutionOrTransparent):
    """Custom type cmmIpPeerCfgImgResolution based on CmmImgResolutionOrTransparent"""


_CmmIpPeerCfgImgResolution_Object = MibTableColumn
cmmIpPeerCfgImgResolution = _CmmIpPeerCfgImgResolution_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 1, 1, 1, 4),
    _CmmIpPeerCfgImgResolution_Type()
)
cmmIpPeerCfgImgResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmIpPeerCfgImgResolution.setStatus("current")


class _CmmIpPeerCfgMsgDispoNotification_Type(TruthValue):
    """Custom type cmmIpPeerCfgMsgDispoNotification based on TruthValue"""


_CmmIpPeerCfgMsgDispoNotification_Object = MibTableColumn
cmmIpPeerCfgMsgDispoNotification = _CmmIpPeerCfgMsgDispoNotification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 1, 1, 1, 5),
    _CmmIpPeerCfgMsgDispoNotification_Type()
)
cmmIpPeerCfgMsgDispoNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmIpPeerCfgMsgDispoNotification.setStatus("current")


class _CmmIpPeerCfgDeliStatNotification_Type(Bits):
    """Custom type cmmIpPeerCfgDeliStatNotification based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("delayed", 2),
          ("failure", 1),
          ("success", 0))
    )

_CmmIpPeerCfgDeliStatNotification_Type.__name__ = "Bits"
_CmmIpPeerCfgDeliStatNotification_Object = MibTableColumn
cmmIpPeerCfgDeliStatNotification = _CmmIpPeerCfgDeliStatNotification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 1, 1, 1, 6),
    _CmmIpPeerCfgDeliStatNotification_Type()
)
cmmIpPeerCfgDeliStatNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmIpPeerCfgDeliStatNotification.setStatus("current")
_CmmCallActive_ObjectIdentity = ObjectIdentity
cmmCallActive = _CmmCallActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2)
)
_CmmIpCallActiveTable_Object = MibTable
cmmIpCallActiveTable = _CmmIpCallActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cmmIpCallActiveTable.setStatus("current")
_CmmIpCallActiveEntry_Object = MibTableRow
cmmIpCallActiveEntry = _CmmIpCallActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1)
)
cmmIpCallActiveEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    cmmIpCallActiveEntry.setStatus("current")
_CmmIpCallActiveConnectionId_Type = CvcGUid
_CmmIpCallActiveConnectionId_Object = MibTableColumn
cmmIpCallActiveConnectionId = _CmmIpCallActiveConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1, 1),
    _CmmIpCallActiveConnectionId_Type()
)
cmmIpCallActiveConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpCallActiveConnectionId.setStatus("current")
_CmmIpCallActiveRemoteIPAddress_Type = IpAddress
_CmmIpCallActiveRemoteIPAddress_Object = MibTableColumn
cmmIpCallActiveRemoteIPAddress = _CmmIpCallActiveRemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1, 2),
    _CmmIpCallActiveRemoteIPAddress_Type()
)
cmmIpCallActiveRemoteIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpCallActiveRemoteIPAddress.setStatus("current")


class _CmmIpCallActiveSessionProtocol_Type(Integer32):
    """Custom type cmmIpCallActiveSessionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("smtp", 1)
    )


_CmmIpCallActiveSessionProtocol_Type.__name__ = "Integer32"
_CmmIpCallActiveSessionProtocol_Object = MibTableColumn
cmmIpCallActiveSessionProtocol = _CmmIpCallActiveSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1, 3),
    _CmmIpCallActiveSessionProtocol_Type()
)
cmmIpCallActiveSessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpCallActiveSessionProtocol.setStatus("current")
_CmmIpCallActiveSessionTarget_Type = DisplayString
_CmmIpCallActiveSessionTarget_Object = MibTableColumn
cmmIpCallActiveSessionTarget = _CmmIpCallActiveSessionTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1, 4),
    _CmmIpCallActiveSessionTarget_Type()
)
cmmIpCallActiveSessionTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpCallActiveSessionTarget.setStatus("current")
_CmmIpCallActiveMessageId_Type = DisplayString
_CmmIpCallActiveMessageId_Object = MibTableColumn
cmmIpCallActiveMessageId = _CmmIpCallActiveMessageId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1, 5),
    _CmmIpCallActiveMessageId_Type()
)
cmmIpCallActiveMessageId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpCallActiveMessageId.setStatus("current")
_CmmIpCallActiveAccountId_Type = DisplayString
_CmmIpCallActiveAccountId_Object = MibTableColumn
cmmIpCallActiveAccountId = _CmmIpCallActiveAccountId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1, 6),
    _CmmIpCallActiveAccountId_Type()
)
cmmIpCallActiveAccountId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpCallActiveAccountId.setStatus("current")
_CmmIpCallActiveImgEncodingType_Type = CmmImgEncoding
_CmmIpCallActiveImgEncodingType_Object = MibTableColumn
cmmIpCallActiveImgEncodingType = _CmmIpCallActiveImgEncodingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1, 7),
    _CmmIpCallActiveImgEncodingType_Type()
)
cmmIpCallActiveImgEncodingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpCallActiveImgEncodingType.setStatus("current")
_CmmIpCallActiveImgResolution_Type = CmmImgResolution
_CmmIpCallActiveImgResolution_Object = MibTableColumn
cmmIpCallActiveImgResolution = _CmmIpCallActiveImgResolution_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1, 8),
    _CmmIpCallActiveImgResolution_Type()
)
cmmIpCallActiveImgResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpCallActiveImgResolution.setStatus("current")
_CmmIpCallActiveAcceptMimeTypes_Type = AbsoluteCounter32
_CmmIpCallActiveAcceptMimeTypes_Object = MibTableColumn
cmmIpCallActiveAcceptMimeTypes = _CmmIpCallActiveAcceptMimeTypes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1, 9),
    _CmmIpCallActiveAcceptMimeTypes_Type()
)
cmmIpCallActiveAcceptMimeTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpCallActiveAcceptMimeTypes.setStatus("current")
_CmmIpCallActiveDiscdMimeTypes_Type = AbsoluteCounter32
_CmmIpCallActiveDiscdMimeTypes_Object = MibTableColumn
cmmIpCallActiveDiscdMimeTypes = _CmmIpCallActiveDiscdMimeTypes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1, 10),
    _CmmIpCallActiveDiscdMimeTypes_Type()
)
cmmIpCallActiveDiscdMimeTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpCallActiveDiscdMimeTypes.setStatus("current")


class _CmmIpCallActiveNotification_Type(Integer32):
    """Custom type cmmIpCallActiveNotification based on Integer32"""
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
        *(("dsn", 3),
          ("dsnMdn", 4),
          ("mdn", 2),
          ("none", 1))
    )


_CmmIpCallActiveNotification_Type.__name__ = "Integer32"
_CmmIpCallActiveNotification_Object = MibTableColumn
cmmIpCallActiveNotification = _CmmIpCallActiveNotification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1, 11),
    _CmmIpCallActiveNotification_Type()
)
cmmIpCallActiveNotification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpCallActiveNotification.setStatus("current")
_CmmCallHistory_ObjectIdentity = ObjectIdentity
cmmCallHistory = _CmmCallHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3)
)
_CmmIpCallHistoryTable_Object = MibTable
cmmIpCallHistoryTable = _CmmIpCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cmmIpCallHistoryTable.setStatus("current")
_CmmIpCallHistoryEntry_Object = MibTableRow
cmmIpCallHistoryEntry = _CmmIpCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1)
)
cmmIpCallHistoryEntry.setIndexNames(
    (0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    cmmIpCallHistoryEntry.setStatus("current")
_CmmIpCallHistoryConnectionId_Type = CvcGUid
_CmmIpCallHistoryConnectionId_Object = MibTableColumn
cmmIpCallHistoryConnectionId = _CmmIpCallHistoryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1, 1),
    _CmmIpCallHistoryConnectionId_Type()
)
cmmIpCallHistoryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpCallHistoryConnectionId.setStatus("current")
_CmmIpCallHistoryRemoteIPAddress_Type = IpAddress
_CmmIpCallHistoryRemoteIPAddress_Object = MibTableColumn
cmmIpCallHistoryRemoteIPAddress = _CmmIpCallHistoryRemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1, 2),
    _CmmIpCallHistoryRemoteIPAddress_Type()
)
cmmIpCallHistoryRemoteIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpCallHistoryRemoteIPAddress.setStatus("current")


class _CmmIpCallHistorySessionProtocol_Type(Integer32):
    """Custom type cmmIpCallHistorySessionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("smtp", 1)
    )


_CmmIpCallHistorySessionProtocol_Type.__name__ = "Integer32"
_CmmIpCallHistorySessionProtocol_Object = MibTableColumn
cmmIpCallHistorySessionProtocol = _CmmIpCallHistorySessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1, 3),
    _CmmIpCallHistorySessionProtocol_Type()
)
cmmIpCallHistorySessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpCallHistorySessionProtocol.setStatus("current")
_CmmIpCallHistorySessionTarget_Type = DisplayString
_CmmIpCallHistorySessionTarget_Object = MibTableColumn
cmmIpCallHistorySessionTarget = _CmmIpCallHistorySessionTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1, 4),
    _CmmIpCallHistorySessionTarget_Type()
)
cmmIpCallHistorySessionTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpCallHistorySessionTarget.setStatus("current")
_CmmIpCallHistoryMessageId_Type = DisplayString
_CmmIpCallHistoryMessageId_Object = MibTableColumn
cmmIpCallHistoryMessageId = _CmmIpCallHistoryMessageId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1, 5),
    _CmmIpCallHistoryMessageId_Type()
)
cmmIpCallHistoryMessageId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpCallHistoryMessageId.setStatus("current")
_CmmIpCallHistoryAccountId_Type = DisplayString
_CmmIpCallHistoryAccountId_Object = MibTableColumn
cmmIpCallHistoryAccountId = _CmmIpCallHistoryAccountId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1, 6),
    _CmmIpCallHistoryAccountId_Type()
)
cmmIpCallHistoryAccountId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpCallHistoryAccountId.setStatus("current")
_CmmIpCallHistoryImgEncodingType_Type = CmmImgEncoding
_CmmIpCallHistoryImgEncodingType_Object = MibTableColumn
cmmIpCallHistoryImgEncodingType = _CmmIpCallHistoryImgEncodingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1, 7),
    _CmmIpCallHistoryImgEncodingType_Type()
)
cmmIpCallHistoryImgEncodingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpCallHistoryImgEncodingType.setStatus("current")
_CmmIpCallHistoryImgResolution_Type = CmmImgResolution
_CmmIpCallHistoryImgResolution_Object = MibTableColumn
cmmIpCallHistoryImgResolution = _CmmIpCallHistoryImgResolution_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1, 8),
    _CmmIpCallHistoryImgResolution_Type()
)
cmmIpCallHistoryImgResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpCallHistoryImgResolution.setStatus("current")
_CmmIpCallHistoryAcceptMimeTypes_Type = AbsoluteCounter32
_CmmIpCallHistoryAcceptMimeTypes_Object = MibTableColumn
cmmIpCallHistoryAcceptMimeTypes = _CmmIpCallHistoryAcceptMimeTypes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1, 9),
    _CmmIpCallHistoryAcceptMimeTypes_Type()
)
cmmIpCallHistoryAcceptMimeTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpCallHistoryAcceptMimeTypes.setStatus("current")
_CmmIpCallHistoryDiscdMimeTypes_Type = AbsoluteCounter32
_CmmIpCallHistoryDiscdMimeTypes_Object = MibTableColumn
cmmIpCallHistoryDiscdMimeTypes = _CmmIpCallHistoryDiscdMimeTypes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1, 10),
    _CmmIpCallHistoryDiscdMimeTypes_Type()
)
cmmIpCallHistoryDiscdMimeTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpCallHistoryDiscdMimeTypes.setStatus("current")


class _CmmIpCallHistoryNotification_Type(Integer32):
    """Custom type cmmIpCallHistoryNotification based on Integer32"""
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
        *(("dsn", 3),
          ("dsnMdn", 4),
          ("mdn", 2),
          ("none", 1))
    )


_CmmIpCallHistoryNotification_Type.__name__ = "Integer32"
_CmmIpCallHistoryNotification_Object = MibTableColumn
cmmIpCallHistoryNotification = _CmmIpCallHistoryNotification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1, 11),
    _CmmIpCallHistoryNotification_Type()
)
cmmIpCallHistoryNotification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIpCallHistoryNotification.setStatus("current")
_CmmFaxGeneralCfg_ObjectIdentity = ObjectIdentity
cmmFaxGeneralCfg = _CmmFaxGeneralCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 4)
)


class _CmmFaxCfgCalledSubscriberId_Type(DisplayString):
    """Custom type cmmFaxCfgCalledSubscriberId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CmmFaxCfgCalledSubscriberId_Type.__name__ = "DisplayString"
_CmmFaxCfgCalledSubscriberId_Object = MibScalar
cmmFaxCfgCalledSubscriberId = _CmmFaxCfgCalledSubscriberId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 4, 1),
    _CmmFaxCfgCalledSubscriberId_Type()
)
cmmFaxCfgCalledSubscriberId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmFaxCfgCalledSubscriberId.setStatus("current")


class _CmmFaxCfgXmitSubscriberId_Type(DisplayString):
    """Custom type cmmFaxCfgXmitSubscriberId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CmmFaxCfgXmitSubscriberId_Type.__name__ = "DisplayString"
_CmmFaxCfgXmitSubscriberId_Object = MibScalar
cmmFaxCfgXmitSubscriberId = _CmmFaxCfgXmitSubscriberId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 4, 2),
    _CmmFaxCfgXmitSubscriberId_Type()
)
cmmFaxCfgXmitSubscriberId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmFaxCfgXmitSubscriberId.setStatus("current")
_CmmFaxCfgRightHeadingString_Type = CmmFaxHeadingString
_CmmFaxCfgRightHeadingString_Object = MibScalar
cmmFaxCfgRightHeadingString = _CmmFaxCfgRightHeadingString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 4, 3),
    _CmmFaxCfgRightHeadingString_Type()
)
cmmFaxCfgRightHeadingString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmFaxCfgRightHeadingString.setStatus("current")
_CmmFaxCfgCenterHeadingString_Type = CmmFaxHeadingString
_CmmFaxCfgCenterHeadingString_Object = MibScalar
cmmFaxCfgCenterHeadingString = _CmmFaxCfgCenterHeadingString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 4, 4),
    _CmmFaxCfgCenterHeadingString_Type()
)
cmmFaxCfgCenterHeadingString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmFaxCfgCenterHeadingString.setStatus("current")
_CmmFaxCfgLeftHeadingString_Type = CmmFaxHeadingString
_CmmFaxCfgLeftHeadingString_Object = MibScalar
cmmFaxCfgLeftHeadingString = _CmmFaxCfgLeftHeadingString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 4, 5),
    _CmmFaxCfgLeftHeadingString_Type()
)
cmmFaxCfgLeftHeadingString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmFaxCfgLeftHeadingString.setStatus("current")


class _CmmFaxCfgCovergPageControl_Type(Bits):
    """Custom type cmmFaxCfgCovergPageControl based on Bits"""
    namedValues = NamedValues(
        *(("coverPageCtlByEmail", 1),
          ("coverPageDetailEnable", 2),
          ("coverPageEnable", 0))
    )

_CmmFaxCfgCovergPageControl_Type.__name__ = "Bits"
_CmmFaxCfgCovergPageControl_Object = MibScalar
cmmFaxCfgCovergPageControl = _CmmFaxCfgCovergPageControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 4, 6),
    _CmmFaxCfgCovergPageControl_Type()
)
cmmFaxCfgCovergPageControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmFaxCfgCovergPageControl.setStatus("current")
_CmmFaxCfgCovergPageComment_Type = DisplayString
_CmmFaxCfgCovergPageComment_Object = MibScalar
cmmFaxCfgCovergPageComment = _CmmFaxCfgCovergPageComment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 4, 7),
    _CmmFaxCfgCovergPageComment_Type()
)
cmmFaxCfgCovergPageComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmFaxCfgCovergPageComment.setStatus("current")


class _CmmFaxCfgFaxProfile_Type(Bits):
    """Custom type cmmFaxCfgFaxProfile based on Bits"""
    namedValues = NamedValues(
        *(("profileC", 3),
          ("profileF", 1),
          ("profileJ", 2),
          ("profileL", 4),
          ("profileM", 5),
          ("profileS", 0))
    )

_CmmFaxCfgFaxProfile_Type.__name__ = "Bits"
_CmmFaxCfgFaxProfile_Object = MibScalar
cmmFaxCfgFaxProfile = _CmmFaxCfgFaxProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 4, 8),
    _CmmFaxCfgFaxProfile_Type()
)
cmmFaxCfgFaxProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmFaxCfgFaxProfile.setStatus("current")
_CmmdcMIBConformance_ObjectIdentity = ObjectIdentity
cmmdcMIBConformance = _CmmdcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 3)
)
_CmmdcMIBCompliances_ObjectIdentity = ObjectIdentity
cmmdcMIBCompliances = _CmmdcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 3, 1)
)
_CmmdcMIBGroups_ObjectIdentity = ObjectIdentity
cmmdcMIBGroups = _CmmdcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 3, 2)
)

# Managed Objects groups

cmmdcPeerCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 3, 2, 1)
)
cmmdcPeerCfgGroup.setObjects(
      *(("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpPeerCfgSessionProtocol"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpPeerCfgSessionTarget"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpPeerCfgImgEncodingType"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpPeerCfgImgResolution"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpPeerCfgMsgDispoNotification"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpPeerCfgDeliStatNotification"))
)
if mibBuilder.loadTexts:
    cmmdcPeerCfgGroup.setStatus("current")

cmmIpCallGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 3, 2, 2)
)
cmmIpCallGeneralGroup.setObjects(
      *(("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallActiveConnectionId"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallActiveRemoteIPAddress"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallActiveSessionProtocol"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallActiveSessionTarget"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallActiveMessageId"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallActiveAccountId"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallActiveAcceptMimeTypes"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallActiveDiscdMimeTypes"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallActiveNotification"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallHistoryConnectionId"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallHistoryRemoteIPAddress"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallHistorySessionProtocol"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallHistorySessionTarget"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallHistoryMessageId"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallHistoryAccountId"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallHistoryAcceptMimeTypes"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallHistoryDiscdMimeTypes"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallHistoryNotification"))
)
if mibBuilder.loadTexts:
    cmmIpCallGeneralGroup.setStatus("current")

cmmIpCallImageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 3, 2, 3)
)
cmmIpCallImageGroup.setObjects(
      *(("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallActiveImgEncodingType"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallActiveImgResolution"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallHistoryImgEncodingType"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallHistoryImgResolution"))
)
if mibBuilder.loadTexts:
    cmmIpCallImageGroup.setStatus("current")

cmmFaxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 3, 2, 4)
)
cmmFaxGroup.setObjects(
      *(("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmFaxCfgCalledSubscriberId"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmFaxCfgXmitSubscriberId"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmFaxCfgRightHeadingString"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmFaxCfgCenterHeadingString"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmFaxCfgLeftHeadingString"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmFaxCfgCovergPageControl"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmFaxCfgCovergPageComment"),
        ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmFaxCfgFaxProfile"))
)
if mibBuilder.loadTexts:
    cmmFaxGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmmdcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 102, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cmmdcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MMAIL-DIAL-CONTROL-MIB",
    **{"CmmImgResolution": CmmImgResolution,
       "CmmImgResolutionOrTransparent": CmmImgResolutionOrTransparent,
       "CmmImgEncoding": CmmImgEncoding,
       "CmmImgEncodingOrTransparent": CmmImgEncodingOrTransparent,
       "CmmFaxHeadingString": CmmFaxHeadingString,
       "ciscoMediaMailDialControlMIB": ciscoMediaMailDialControlMIB,
       "cmmdcMIBObjects": cmmdcMIBObjects,
       "cmmPeer": cmmPeer,
       "cmmIpPeerCfgTable": cmmIpPeerCfgTable,
       "cmmIpPeerCfgEntry": cmmIpPeerCfgEntry,
       "cmmIpPeerCfgSessionProtocol": cmmIpPeerCfgSessionProtocol,
       "cmmIpPeerCfgSessionTarget": cmmIpPeerCfgSessionTarget,
       "cmmIpPeerCfgImgEncodingType": cmmIpPeerCfgImgEncodingType,
       "cmmIpPeerCfgImgResolution": cmmIpPeerCfgImgResolution,
       "cmmIpPeerCfgMsgDispoNotification": cmmIpPeerCfgMsgDispoNotification,
       "cmmIpPeerCfgDeliStatNotification": cmmIpPeerCfgDeliStatNotification,
       "cmmCallActive": cmmCallActive,
       "cmmIpCallActiveTable": cmmIpCallActiveTable,
       "cmmIpCallActiveEntry": cmmIpCallActiveEntry,
       "cmmIpCallActiveConnectionId": cmmIpCallActiveConnectionId,
       "cmmIpCallActiveRemoteIPAddress": cmmIpCallActiveRemoteIPAddress,
       "cmmIpCallActiveSessionProtocol": cmmIpCallActiveSessionProtocol,
       "cmmIpCallActiveSessionTarget": cmmIpCallActiveSessionTarget,
       "cmmIpCallActiveMessageId": cmmIpCallActiveMessageId,
       "cmmIpCallActiveAccountId": cmmIpCallActiveAccountId,
       "cmmIpCallActiveImgEncodingType": cmmIpCallActiveImgEncodingType,
       "cmmIpCallActiveImgResolution": cmmIpCallActiveImgResolution,
       "cmmIpCallActiveAcceptMimeTypes": cmmIpCallActiveAcceptMimeTypes,
       "cmmIpCallActiveDiscdMimeTypes": cmmIpCallActiveDiscdMimeTypes,
       "cmmIpCallActiveNotification": cmmIpCallActiveNotification,
       "cmmCallHistory": cmmCallHistory,
       "cmmIpCallHistoryTable": cmmIpCallHistoryTable,
       "cmmIpCallHistoryEntry": cmmIpCallHistoryEntry,
       "cmmIpCallHistoryConnectionId": cmmIpCallHistoryConnectionId,
       "cmmIpCallHistoryRemoteIPAddress": cmmIpCallHistoryRemoteIPAddress,
       "cmmIpCallHistorySessionProtocol": cmmIpCallHistorySessionProtocol,
       "cmmIpCallHistorySessionTarget": cmmIpCallHistorySessionTarget,
       "cmmIpCallHistoryMessageId": cmmIpCallHistoryMessageId,
       "cmmIpCallHistoryAccountId": cmmIpCallHistoryAccountId,
       "cmmIpCallHistoryImgEncodingType": cmmIpCallHistoryImgEncodingType,
       "cmmIpCallHistoryImgResolution": cmmIpCallHistoryImgResolution,
       "cmmIpCallHistoryAcceptMimeTypes": cmmIpCallHistoryAcceptMimeTypes,
       "cmmIpCallHistoryDiscdMimeTypes": cmmIpCallHistoryDiscdMimeTypes,
       "cmmIpCallHistoryNotification": cmmIpCallHistoryNotification,
       "cmmFaxGeneralCfg": cmmFaxGeneralCfg,
       "cmmFaxCfgCalledSubscriberId": cmmFaxCfgCalledSubscriberId,
       "cmmFaxCfgXmitSubscriberId": cmmFaxCfgXmitSubscriberId,
       "cmmFaxCfgRightHeadingString": cmmFaxCfgRightHeadingString,
       "cmmFaxCfgCenterHeadingString": cmmFaxCfgCenterHeadingString,
       "cmmFaxCfgLeftHeadingString": cmmFaxCfgLeftHeadingString,
       "cmmFaxCfgCovergPageControl": cmmFaxCfgCovergPageControl,
       "cmmFaxCfgCovergPageComment": cmmFaxCfgCovergPageComment,
       "cmmFaxCfgFaxProfile": cmmFaxCfgFaxProfile,
       "cmmdcMIBConformance": cmmdcMIBConformance,
       "cmmdcMIBCompliances": cmmdcMIBCompliances,
       "cmmdcMIBCompliance": cmmdcMIBCompliance,
       "cmmdcMIBGroups": cmmdcMIBGroups,
       "cmmdcPeerCfgGroup": cmmdcPeerCfgGroup,
       "cmmIpCallGeneralGroup": cmmIpCallGeneralGroup,
       "cmmIpCallImageGroup": cmmIpCallImageGroup,
       "cmmFaxGroup": cmmFaxGroup}
)
