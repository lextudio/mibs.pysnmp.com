# SNMP MIB module (CTRON-LFAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-LFAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:01 2024
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

(ctSystem,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctSystem")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ctLFAP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11)
)
ctLFAP.setRevisions(
        ("1999-12-29 00:00",
         "1997-09-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FlowPolicy_ObjectIdentity = ObjectIdentity
flowPolicy = _FlowPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 1)
)


class _FlowPolicyControl_Type(Integer32):
    """Custom type flowPolicyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlowPolicyControl_Type.__name__ = "Integer32"
_FlowPolicyControl_Object = MibScalar
flowPolicyControl = _FlowPolicyControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 1, 1),
    _FlowPolicyControl_Type()
)
flowPolicyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowPolicyControl.setStatus("current")


class _FlowPolicyStatus_Type(Integer32):
    """Custom type flowPolicyStatus based on Integer32"""
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
        *(("active", 3),
          ("disabled", 1),
          ("enabled", 2),
          ("error", 4))
    )


_FlowPolicyStatus_Type.__name__ = "Integer32"
_FlowPolicyStatus_Object = MibScalar
flowPolicyStatus = _FlowPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 1, 2),
    _FlowPolicyStatus_Type()
)
flowPolicyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowPolicyStatus.setStatus("current")
_FlowPolicyActiveServer_Type = PhysAddress
_FlowPolicyActiveServer_Object = MibScalar
flowPolicyActiveServer = _FlowPolicyActiveServer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 1, 3),
    _FlowPolicyActiveServer_Type()
)
flowPolicyActiveServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowPolicyActiveServer.setStatus("current")
_FlowPolicyServerAddrTable_Object = MibTable
flowPolicyServerAddrTable = _FlowPolicyServerAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 1, 4)
)
if mibBuilder.loadTexts:
    flowPolicyServerAddrTable.setStatus("current")
_FlowPolicyServerAddrEntry_Object = MibTableRow
flowPolicyServerAddrEntry = _FlowPolicyServerAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 1, 4, 1)
)
flowPolicyServerAddrEntry.setIndexNames(
    (0, "CTRON-LFAP-MIB", "flowPolicyServerAddrIndex"),
)
if mibBuilder.loadTexts:
    flowPolicyServerAddrEntry.setStatus("current")


class _FlowPolicyServerAddrIndex_Type(Integer32):
    """Custom type flowPolicyServerAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FlowPolicyServerAddrIndex_Type.__name__ = "Integer32"
_FlowPolicyServerAddrIndex_Object = MibTableColumn
flowPolicyServerAddrIndex = _FlowPolicyServerAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 1, 4, 1, 1),
    _FlowPolicyServerAddrIndex_Type()
)
flowPolicyServerAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowPolicyServerAddrIndex.setStatus("current")
_FlowPolicyServerAddr_Type = PhysAddress
_FlowPolicyServerAddr_Object = MibTableColumn
flowPolicyServerAddr = _FlowPolicyServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 1, 4, 1, 2),
    _FlowPolicyServerAddr_Type()
)
flowPolicyServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowPolicyServerAddr.setStatus("current")
_FlowPolicyConfig_ObjectIdentity = ObjectIdentity
flowPolicyConfig = _FlowPolicyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 1, 6)
)


class _FlowPolicyConfigPolicy_Type(Integer32):
    """Custom type flowPolicyConfigPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2))
    )


_FlowPolicyConfigPolicy_Type.__name__ = "Integer32"
_FlowPolicyConfigPolicy_Object = MibScalar
flowPolicyConfigPolicy = _FlowPolicyConfigPolicy_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 1, 6, 1),
    _FlowPolicyConfigPolicy_Type()
)
flowPolicyConfigPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowPolicyConfigPolicy.setStatus("current")


class _FlowPolicyConfigStatistics_Type(Integer32):
    """Custom type flowPolicyConfigStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2))
    )


_FlowPolicyConfigStatistics_Type.__name__ = "Integer32"
_FlowPolicyConfigStatistics_Object = MibScalar
flowPolicyConfigStatistics = _FlowPolicyConfigStatistics_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 1, 6, 2),
    _FlowPolicyConfigStatistics_Type()
)
flowPolicyConfigStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowPolicyConfigStatistics.setStatus("current")
_MonLfap_ObjectIdentity = ObjectIdentity
monLfap = _MonLfap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2)
)
_MonLfapCounts_ObjectIdentity = ObjectIdentity
monLfapCounts = _MonLfapCounts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1)
)
_MonLfapFARsSent_Type = Counter32
_MonLfapFARsSent_Object = MibScalar
monLfapFARsSent = _MonLfapFARsSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 1),
    _MonLfapFARsSent_Type()
)
monLfapFARsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapFARsSent.setStatus("current")
_MonLfapFARsReceived_Type = Counter32
_MonLfapFARsReceived_Object = MibScalar
monLfapFARsReceived = _MonLfapFARsReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 2),
    _MonLfapFARsReceived_Type()
)
monLfapFARsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapFARsReceived.setStatus("current")
_MonLfapFAAsSent_Type = Counter32
_MonLfapFAAsSent_Object = MibScalar
monLfapFAAsSent = _MonLfapFAAsSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 3),
    _MonLfapFAAsSent_Type()
)
monLfapFAAsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapFAAsSent.setStatus("current")
_MonLfapFAAsReceived_Type = Counter32
_MonLfapFAAsReceived_Object = MibScalar
monLfapFAAsReceived = _MonLfapFAAsReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 4),
    _MonLfapFAAsReceived_Type()
)
monLfapFAAsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapFAAsReceived.setStatus("current")
_MonLfapFAUsSent_Type = Counter32
_MonLfapFAUsSent_Object = MibScalar
monLfapFAUsSent = _MonLfapFAUsSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 5),
    _MonLfapFAUsSent_Type()
)
monLfapFAUsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapFAUsSent.setStatus("current")
_MonLfapFAUsReceived_Type = Counter32
_MonLfapFAUsReceived_Object = MibScalar
monLfapFAUsReceived = _MonLfapFAUsReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 6),
    _MonLfapFAUsReceived_Type()
)
monLfapFAUsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapFAUsReceived.setStatus("current")
_MonLfapFUNsSent_Type = Counter32
_MonLfapFUNsSent_Object = MibScalar
monLfapFUNsSent = _MonLfapFUNsSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 7),
    _MonLfapFUNsSent_Type()
)
monLfapFUNsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapFUNsSent.setStatus("current")
_MonLfapFUNsReceived_Type = Counter32
_MonLfapFUNsReceived_Object = MibScalar
monLfapFUNsReceived = _MonLfapFUNsReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 8),
    _MonLfapFUNsReceived_Type()
)
monLfapFUNsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapFUNsReceived.setStatus("current")
_MonLfapFUAsSent_Type = Counter32
_MonLfapFUAsSent_Object = MibScalar
monLfapFUAsSent = _MonLfapFUAsSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 9),
    _MonLfapFUAsSent_Type()
)
monLfapFUAsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapFUAsSent.setStatus("current")
_MonLfapFUAsReceived_Type = Counter32
_MonLfapFUAsReceived_Object = MibScalar
monLfapFUAsReceived = _MonLfapFUAsReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 10),
    _MonLfapFUAsReceived_Type()
)
monLfapFUAsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapFUAsReceived.setStatus("current")
_MonLfapFCRsSent_Type = Counter32
_MonLfapFCRsSent_Object = MibScalar
monLfapFCRsSent = _MonLfapFCRsSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 11),
    _MonLfapFCRsSent_Type()
)
monLfapFCRsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapFCRsSent.setStatus("current")
_MonLfapFCRsReceived_Type = Counter32
_MonLfapFCRsReceived_Object = MibScalar
monLfapFCRsReceived = _MonLfapFCRsReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 12),
    _MonLfapFCRsReceived_Type()
)
monLfapFCRsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapFCRsReceived.setStatus("current")
_MonLfapFCAsSent_Type = Counter32
_MonLfapFCAsSent_Object = MibScalar
monLfapFCAsSent = _MonLfapFCAsSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 13),
    _MonLfapFCAsSent_Type()
)
monLfapFCAsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapFCAsSent.setStatus("current")
_MonLfapFCAsReceived_Type = Counter32
_MonLfapFCAsReceived_Object = MibScalar
monLfapFCAsReceived = _MonLfapFCAsReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 14),
    _MonLfapFCAsReceived_Type()
)
monLfapFCAsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapFCAsReceived.setStatus("current")
_MonLfapARsSent_Type = Counter32
_MonLfapARsSent_Object = MibScalar
monLfapARsSent = _MonLfapARsSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 15),
    _MonLfapARsSent_Type()
)
monLfapARsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapARsSent.setStatus("current")
_MonLfapARsReceived_Type = Counter32
_MonLfapARsReceived_Object = MibScalar
monLfapARsReceived = _MonLfapARsReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 16),
    _MonLfapARsReceived_Type()
)
monLfapARsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapARsReceived.setStatus("current")
_MonLfapARAsSent_Type = Counter32
_MonLfapARAsSent_Object = MibScalar
monLfapARAsSent = _MonLfapARAsSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 17),
    _MonLfapARAsSent_Type()
)
monLfapARAsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapARAsSent.setStatus("current")
_MonLfapARAsReceived_Type = Counter32
_MonLfapARAsReceived_Object = MibScalar
monLfapARAsReceived = _MonLfapARAsReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 18),
    _MonLfapARAsReceived_Type()
)
monLfapARAsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapARAsReceived.setStatus("current")
_MonLfapFSNsSent_Type = Counter32
_MonLfapFSNsSent_Object = MibScalar
monLfapFSNsSent = _MonLfapFSNsSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 19),
    _MonLfapFSNsSent_Type()
)
monLfapFSNsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapFSNsSent.setStatus("current")
_MonLfapFSNsReceived_Type = Counter32
_MonLfapFSNsReceived_Object = MibScalar
monLfapFSNsReceived = _MonLfapFSNsReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 20),
    _MonLfapFSNsReceived_Type()
)
monLfapFSNsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapFSNsReceived.setStatus("current")
_MonLfapFSAsSent_Type = Counter32
_MonLfapFSAsSent_Object = MibScalar
monLfapFSAsSent = _MonLfapFSAsSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 21),
    _MonLfapFSAsSent_Type()
)
monLfapFSAsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapFSAsSent.setStatus("current")
_MonLfapFSAsReceived_Type = Counter32
_MonLfapFSAsReceived_Object = MibScalar
monLfapFSAsReceived = _MonLfapFSAsReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 22),
    _MonLfapFSAsReceived_Type()
)
monLfapFSAsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapFSAsReceived.setStatus("current")
_MonLfapDroppedMessages_Type = Counter32
_MonLfapDroppedMessages_Object = MibScalar
monLfapDroppedMessages = _MonLfapDroppedMessages_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 23),
    _MonLfapDroppedMessages_Type()
)
monLfapDroppedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapDroppedMessages.setStatus("current")
_MonLfapVRsSent_Type = Counter32
_MonLfapVRsSent_Object = MibScalar
monLfapVRsSent = _MonLfapVRsSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 24),
    _MonLfapVRsSent_Type()
)
monLfapVRsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapVRsSent.setStatus("current")
_MonLfapVRAsReceived_Type = Counter32
_MonLfapVRAsReceived_Object = MibScalar
monLfapVRAsReceived = _MonLfapVRAsReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 25),
    _MonLfapVRAsReceived_Type()
)
monLfapVRAsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapVRAsReceived.setStatus("current")
_MonLfapConnSuccess_Type = Counter32
_MonLfapConnSuccess_Object = MibScalar
monLfapConnSuccess = _MonLfapConnSuccess_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 26),
    _MonLfapConnSuccess_Type()
)
monLfapConnSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapConnSuccess.setStatus("current")
_MonLfapConnFailure_Type = Counter32
_MonLfapConnFailure_Object = MibScalar
monLfapConnFailure = _MonLfapConnFailure_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 27),
    _MonLfapConnFailure_Type()
)
monLfapConnFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapConnFailure.setStatus("current")
_MonLfapBytesSent_Type = Counter32
_MonLfapBytesSent_Object = MibScalar
monLfapBytesSent = _MonLfapBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 28),
    _MonLfapBytesSent_Type()
)
monLfapBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapBytesSent.setStatus("current")
_MonLfapBytesReceived_Type = Counter32
_MonLfapBytesReceived_Object = MibScalar
monLfapBytesReceived = _MonLfapBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 29),
    _MonLfapBytesReceived_Type()
)
monLfapBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapBytesReceived.setStatus("current")
_MonLfapMsgsSent_Type = Counter32
_MonLfapMsgsSent_Object = MibScalar
monLfapMsgsSent = _MonLfapMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 30),
    _MonLfapMsgsSent_Type()
)
monLfapMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapMsgsSent.setStatus("current")
_MonLfapMsgsReceived_Type = Counter32
_MonLfapMsgsReceived_Object = MibScalar
monLfapMsgsReceived = _MonLfapMsgsReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 31),
    _MonLfapMsgsReceived_Type()
)
monLfapMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapMsgsReceived.setStatus("current")
_MonLfapMsgsReceivedError_Type = Counter32
_MonLfapMsgsReceivedError_Object = MibScalar
monLfapMsgsReceivedError = _MonLfapMsgsReceivedError_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 32),
    _MonLfapMsgsReceivedError_Type()
)
monLfapMsgsReceivedError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapMsgsReceivedError.setStatus("current")
_MonLfapMsgsSendQueue_Type = Integer32
_MonLfapMsgsSendQueue_Object = MibScalar
monLfapMsgsSendQueue = _MonLfapMsgsSendQueue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 33),
    _MonLfapMsgsSendQueue_Type()
)
monLfapMsgsSendQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapMsgsSendQueue.setStatus("current")
_MonLfapMsgsSendQueuePeak_Type = Gauge32
_MonLfapMsgsSendQueuePeak_Object = MibScalar
monLfapMsgsSendQueuePeak = _MonLfapMsgsSendQueuePeak_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 34),
    _MonLfapMsgsSendQueuePeak_Type()
)
monLfapMsgsSendQueuePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapMsgsSendQueuePeak.setStatus("current")
_MonLfapMsgsReceiveQueue_Type = Integer32
_MonLfapMsgsReceiveQueue_Object = MibScalar
monLfapMsgsReceiveQueue = _MonLfapMsgsReceiveQueue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 35),
    _MonLfapMsgsReceiveQueue_Type()
)
monLfapMsgsReceiveQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapMsgsReceiveQueue.setStatus("current")
_MonLfapDroppedMessagesConnected_Type = Counter32
_MonLfapDroppedMessagesConnected_Object = MibScalar
monLfapDroppedMessagesConnected = _MonLfapDroppedMessagesConnected_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 36),
    _MonLfapDroppedMessagesConnected_Type()
)
monLfapDroppedMessagesConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapDroppedMessagesConnected.setStatus("current")
_MonLfapDroppedFARs_Type = Counter32
_MonLfapDroppedFARs_Object = MibScalar
monLfapDroppedFARs = _MonLfapDroppedFARs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 37),
    _MonLfapDroppedFARs_Type()
)
monLfapDroppedFARs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapDroppedFARs.setStatus("current")
_MonLfapDroppedFUNIs_Type = Counter32
_MonLfapDroppedFUNIs_Object = MibScalar
monLfapDroppedFUNIs = _MonLfapDroppedFUNIs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 38),
    _MonLfapDroppedFUNIs_Type()
)
monLfapDroppedFUNIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapDroppedFUNIs.setStatus("current")
_MonLfapDroppedFUNs_Type = Counter32
_MonLfapDroppedFUNs_Object = MibScalar
monLfapDroppedFUNs = _MonLfapDroppedFUNs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 39),
    _MonLfapDroppedFUNs_Type()
)
monLfapDroppedFUNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapDroppedFUNs.setStatus("current")
_MonLfapDroppedARs_Type = Counter32
_MonLfapDroppedARs_Object = MibScalar
monLfapDroppedARs = _MonLfapDroppedARs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 40),
    _MonLfapDroppedARs_Type()
)
monLfapDroppedARs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapDroppedARs.setStatus("current")
_MonLfapDroppedARAs_Type = Counter32
_MonLfapDroppedARAs_Object = MibScalar
monLfapDroppedARAs = _MonLfapDroppedARAs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 41),
    _MonLfapDroppedARAs_Type()
)
monLfapDroppedARAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapDroppedARAs.setStatus("current")
_MonLfapDroppedVRs_Type = Counter32
_MonLfapDroppedVRs_Object = MibScalar
monLfapDroppedVRs = _MonLfapDroppedVRs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 42),
    _MonLfapDroppedVRs_Type()
)
monLfapDroppedVRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapDroppedVRs.setStatus("current")
_MonCxnCounts_ObjectIdentity = ObjectIdentity
monCxnCounts = _MonCxnCounts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 2)
)
_MonLfapYesRespCnt_Type = Counter32
_MonLfapYesRespCnt_Object = MibScalar
monLfapYesRespCnt = _MonLfapYesRespCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 2, 1),
    _MonLfapYesRespCnt_Type()
)
monLfapYesRespCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapYesRespCnt.setStatus("current")
_MonLfapNoRespCnt_Type = Counter32
_MonLfapNoRespCnt_Object = MibScalar
monLfapNoRespCnt = _MonLfapNoRespCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 2, 2),
    _MonLfapNoRespCnt_Type()
)
monLfapNoRespCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapNoRespCnt.setStatus("current")
_MonLfapFlowSetups_Type = Counter32
_MonLfapFlowSetups_Object = MibScalar
monLfapFlowSetups = _MonLfapFlowSetups_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 2, 3),
    _MonLfapFlowSetups_Type()
)
monLfapFlowSetups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapFlowSetups.setStatus("current")
_MonLfapFlowTeardowns_Type = Counter32
_MonLfapFlowTeardowns_Object = MibScalar
monLfapFlowTeardowns = _MonLfapFlowTeardowns_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 2, 4),
    _MonLfapFlowTeardowns_Type()
)
monLfapFlowTeardowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapFlowTeardowns.setStatus("current")
_MonLfapFlowActivePeak_Type = Gauge32
_MonLfapFlowActivePeak_Object = MibScalar
monLfapFlowActivePeak = _MonLfapFlowActivePeak_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 2, 5),
    _MonLfapFlowActivePeak_Type()
)
monLfapFlowActivePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monLfapFlowActivePeak.setStatus("current")
_MonActiveCxnCnt_Type = Counter32
_MonActiveCxnCnt_Object = MibScalar
monActiveCxnCnt = _MonActiveCxnCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 2, 8),
    _MonActiveCxnCnt_Type()
)
monActiveCxnCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monActiveCxnCnt.setStatus("current")
_FlowPolicyPolling_ObjectIdentity = ObjectIdentity
flowPolicyPolling = _FlowPolicyPolling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 3)
)


class _FlowPolicyPollingTimerInterval_Type(Integer32):
    """Custom type flowPolicyPollingTimerInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_FlowPolicyPollingTimerInterval_Type.__name__ = "Integer32"
_FlowPolicyPollingTimerInterval_Object = MibScalar
flowPolicyPollingTimerInterval = _FlowPolicyPollingTimerInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 3, 1),
    _FlowPolicyPollingTimerInterval_Type()
)
flowPolicyPollingTimerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowPolicyPollingTimerInterval.setStatus("current")


class _FlowPolicyPollingBatchSize_Type(Integer32):
    """Custom type flowPolicyPollingBatchSize based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_FlowPolicyPollingBatchSize_Type.__name__ = "Integer32"
_FlowPolicyPollingBatchSize_Object = MibScalar
flowPolicyPollingBatchSize = _FlowPolicyPollingBatchSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 3, 2),
    _FlowPolicyPollingBatchSize_Type()
)
flowPolicyPollingBatchSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowPolicyPollingBatchSize.setStatus("current")
_FlowPolicyPollingBatchInterval_Type = Integer32
_FlowPolicyPollingBatchInterval_Object = MibScalar
flowPolicyPollingBatchInterval = _FlowPolicyPollingBatchInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 3, 3),
    _FlowPolicyPollingBatchInterval_Type()
)
flowPolicyPollingBatchInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flowPolicyPollingBatchInterval.setStatus("current")


class _FlowPolicyPollingBatchUpdateInterval_Type(Integer32):
    """Custom type flowPolicyPollingBatchUpdateInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_FlowPolicyPollingBatchUpdateInterval_Type.__name__ = "Integer32"
_FlowPolicyPollingBatchUpdateInterval_Object = MibScalar
flowPolicyPollingBatchUpdateInterval = _FlowPolicyPollingBatchUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 3, 4),
    _FlowPolicyPollingBatchUpdateInterval_Type()
)
flowPolicyPollingBatchUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowPolicyPollingBatchUpdateInterval.setStatus("current")


class _FlowPolicyPollingLostContactInterval_Type(Integer32):
    """Custom type flowPolicyPollingLostContactInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_FlowPolicyPollingLostContactInterval_Type.__name__ = "Integer32"
_FlowPolicyPollingLostContactInterval_Object = MibScalar
flowPolicyPollingLostContactInterval = _FlowPolicyPollingLostContactInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 3, 5),
    _FlowPolicyPollingLostContactInterval_Type()
)
flowPolicyPollingLostContactInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowPolicyPollingLostContactInterval.setStatus("current")


class _FlowPolicyPollingServerRetryInterval_Type(Integer32):
    """Custom type flowPolicyPollingServerRetryInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_FlowPolicyPollingServerRetryInterval_Type.__name__ = "Integer32"
_FlowPolicyPollingServerRetryInterval_Object = MibScalar
flowPolicyPollingServerRetryInterval = _FlowPolicyPollingServerRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 3, 6),
    _FlowPolicyPollingServerRetryInterval_Type()
)
flowPolicyPollingServerRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowPolicyPollingServerRetryInterval.setStatus("current")


class _FlowPolicyPollingSendQueueMaxSize_Type(Integer32):
    """Custom type flowPolicyPollingSendQueueMaxSize based on Integer32"""
    defaultValue = 50000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 2000000),
    )


_FlowPolicyPollingSendQueueMaxSize_Type.__name__ = "Integer32"
_FlowPolicyPollingSendQueueMaxSize_Object = MibScalar
flowPolicyPollingSendQueueMaxSize = _FlowPolicyPollingSendQueueMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 3, 7),
    _FlowPolicyPollingSendQueueMaxSize_Type()
)
flowPolicyPollingSendQueueMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowPolicyPollingSendQueueMaxSize.setStatus("current")


class _FlowPolicyPollingTaskPriority_Type(Integer32):
    """Custom type flowPolicyPollingTaskPriority based on Integer32"""
    defaultValue = 230

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 250),
    )


_FlowPolicyPollingTaskPriority_Type.__name__ = "Integer32"
_FlowPolicyPollingTaskPriority_Object = MibScalar
flowPolicyPollingTaskPriority = _FlowPolicyPollingTaskPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 3, 8),
    _FlowPolicyPollingTaskPriority_Type()
)
flowPolicyPollingTaskPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flowPolicyPollingTaskPriority.setStatus("current")
_LfapConformance_ObjectIdentity = ObjectIdentity
lfapConformance = _LfapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 4)
)
_LfapCompliances_ObjectIdentity = ObjectIdentity
lfapCompliances = _LfapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 4, 1)
)
_LfapGroups_ObjectIdentity = ObjectIdentity
lfapGroups = _LfapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 4, 2)
)

# Managed Objects groups

lfapConfGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 4, 2, 3)
)
lfapConfGroupV10.setObjects(
      *(("CTRON-LFAP-MIB", "flowPolicyControl"),
        ("CTRON-LFAP-MIB", "flowPolicyStatus"),
        ("CTRON-LFAP-MIB", "flowPolicyActiveServer"),
        ("CTRON-LFAP-MIB", "flowPolicyServerAddrIndex"),
        ("CTRON-LFAP-MIB", "flowPolicyServerAddr"),
        ("CTRON-LFAP-MIB", "flowPolicyConfigPolicy"),
        ("CTRON-LFAP-MIB", "flowPolicyConfigStatistics"),
        ("CTRON-LFAP-MIB", "monLfapFARsSent"),
        ("CTRON-LFAP-MIB", "monLfapFARsReceived"),
        ("CTRON-LFAP-MIB", "monLfapFAAsSent"),
        ("CTRON-LFAP-MIB", "monLfapFAAsReceived"),
        ("CTRON-LFAP-MIB", "monLfapFAUsSent"),
        ("CTRON-LFAP-MIB", "monLfapFAUsReceived"),
        ("CTRON-LFAP-MIB", "monLfapFUNsSent"),
        ("CTRON-LFAP-MIB", "monLfapFUNsReceived"),
        ("CTRON-LFAP-MIB", "monLfapFUAsSent"),
        ("CTRON-LFAP-MIB", "monLfapFUAsReceived"),
        ("CTRON-LFAP-MIB", "monLfapFCRsSent"),
        ("CTRON-LFAP-MIB", "monLfapFCRsReceived"),
        ("CTRON-LFAP-MIB", "monLfapFCAsSent"),
        ("CTRON-LFAP-MIB", "monLfapFCAsReceived"),
        ("CTRON-LFAP-MIB", "monLfapARsSent"),
        ("CTRON-LFAP-MIB", "monLfapARsReceived"),
        ("CTRON-LFAP-MIB", "monLfapARAsSent"),
        ("CTRON-LFAP-MIB", "monLfapARAsReceived"),
        ("CTRON-LFAP-MIB", "monLfapFSNsSent"),
        ("CTRON-LFAP-MIB", "monLfapFSNsReceived"),
        ("CTRON-LFAP-MIB", "monLfapFSAsSent"),
        ("CTRON-LFAP-MIB", "monLfapFSAsReceived"),
        ("CTRON-LFAP-MIB", "monLfapDroppedMessages"),
        ("CTRON-LFAP-MIB", "monLfapYesRespCnt"),
        ("CTRON-LFAP-MIB", "monLfapNoRespCnt"),
        ("CTRON-LFAP-MIB", "monActiveCxnCnt"),
        ("CTRON-LFAP-MIB", "flowPolicyPollingTimerInterval"),
        ("CTRON-LFAP-MIB", "flowPolicyPollingBatchSize"),
        ("CTRON-LFAP-MIB", "flowPolicyPollingBatchInterval"))
)
if mibBuilder.loadTexts:
    lfapConfGroupV10.setStatus("deprecated")

lfapConfGroupV40 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 4, 2, 4)
)
lfapConfGroupV40.setObjects(
      *(("CTRON-LFAP-MIB", "flowPolicyControl"),
        ("CTRON-LFAP-MIB", "flowPolicyStatus"),
        ("CTRON-LFAP-MIB", "flowPolicyActiveServer"),
        ("CTRON-LFAP-MIB", "flowPolicyServerAddrIndex"),
        ("CTRON-LFAP-MIB", "flowPolicyServerAddr"),
        ("CTRON-LFAP-MIB", "flowPolicyConfigPolicy"),
        ("CTRON-LFAP-MIB", "flowPolicyConfigStatistics"),
        ("CTRON-LFAP-MIB", "monLfapFARsSent"),
        ("CTRON-LFAP-MIB", "monLfapFARsReceived"),
        ("CTRON-LFAP-MIB", "monLfapFAAsSent"),
        ("CTRON-LFAP-MIB", "monLfapFAAsReceived"),
        ("CTRON-LFAP-MIB", "monLfapFAUsSent"),
        ("CTRON-LFAP-MIB", "monLfapFAUsReceived"),
        ("CTRON-LFAP-MIB", "monLfapFUNsSent"),
        ("CTRON-LFAP-MIB", "monLfapFUNsReceived"),
        ("CTRON-LFAP-MIB", "monLfapFUAsSent"),
        ("CTRON-LFAP-MIB", "monLfapFUAsReceived"),
        ("CTRON-LFAP-MIB", "monLfapFCRsSent"),
        ("CTRON-LFAP-MIB", "monLfapFCRsReceived"),
        ("CTRON-LFAP-MIB", "monLfapFCAsSent"),
        ("CTRON-LFAP-MIB", "monLfapFCAsReceived"),
        ("CTRON-LFAP-MIB", "monLfapARsSent"),
        ("CTRON-LFAP-MIB", "monLfapARsReceived"),
        ("CTRON-LFAP-MIB", "monLfapARAsSent"),
        ("CTRON-LFAP-MIB", "monLfapARAsReceived"),
        ("CTRON-LFAP-MIB", "monLfapFSNsSent"),
        ("CTRON-LFAP-MIB", "monLfapFSNsReceived"),
        ("CTRON-LFAP-MIB", "monLfapFSAsSent"),
        ("CTRON-LFAP-MIB", "monLfapFSAsReceived"),
        ("CTRON-LFAP-MIB", "monLfapDroppedMessages"),
        ("CTRON-LFAP-MIB", "monLfapVRsSent"),
        ("CTRON-LFAP-MIB", "monLfapVRAsReceived"),
        ("CTRON-LFAP-MIB", "monLfapConnSuccess"),
        ("CTRON-LFAP-MIB", "monLfapConnFailure"),
        ("CTRON-LFAP-MIB", "monLfapBytesSent"),
        ("CTRON-LFAP-MIB", "monLfapBytesReceived"),
        ("CTRON-LFAP-MIB", "monLfapMsgsSent"),
        ("CTRON-LFAP-MIB", "monLfapMsgsReceived"),
        ("CTRON-LFAP-MIB", "monLfapMsgsReceivedError"),
        ("CTRON-LFAP-MIB", "monLfapMsgsSendQueue"),
        ("CTRON-LFAP-MIB", "monLfapMsgsSendQueuePeak"),
        ("CTRON-LFAP-MIB", "monLfapMsgsReceiveQueue"),
        ("CTRON-LFAP-MIB", "monLfapDroppedMessagesConnected"),
        ("CTRON-LFAP-MIB", "monLfapDroppedFARs"),
        ("CTRON-LFAP-MIB", "monLfapDroppedFUNIs"),
        ("CTRON-LFAP-MIB", "monLfapDroppedFUNs"),
        ("CTRON-LFAP-MIB", "monLfapDroppedARs"),
        ("CTRON-LFAP-MIB", "monLfapDroppedARAs"),
        ("CTRON-LFAP-MIB", "monLfapDroppedVRs"),
        ("CTRON-LFAP-MIB", "monLfapYesRespCnt"),
        ("CTRON-LFAP-MIB", "monLfapNoRespCnt"),
        ("CTRON-LFAP-MIB", "monLfapFlowSetups"),
        ("CTRON-LFAP-MIB", "monLfapFlowTeardowns"),
        ("CTRON-LFAP-MIB", "monLfapFlowActivePeak"),
        ("CTRON-LFAP-MIB", "monActiveCxnCnt"),
        ("CTRON-LFAP-MIB", "flowPolicyPollingTimerInterval"),
        ("CTRON-LFAP-MIB", "flowPolicyPollingBatchSize"),
        ("CTRON-LFAP-MIB", "flowPolicyPollingBatchInterval"),
        ("CTRON-LFAP-MIB", "flowPolicyPollingBatchUpdateInterval"),
        ("CTRON-LFAP-MIB", "flowPolicyPollingLostContactInterval"),
        ("CTRON-LFAP-MIB", "flowPolicyPollingServerRetryInterval"),
        ("CTRON-LFAP-MIB", "flowPolicyPollingSendQueueMaxSize"),
        ("CTRON-LFAP-MIB", "flowPolicyPollingTaskPriority"))
)
if mibBuilder.loadTexts:
    lfapConfGroupV40.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lfapComplianceV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    lfapComplianceV10.setStatus(
        "deprecated"
    )

lfapComplianceV40 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 4, 2, 4, 1)
)
if mibBuilder.loadTexts:
    lfapComplianceV40.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-LFAP-MIB",
    **{"ctLFAP": ctLFAP,
       "flowPolicy": flowPolicy,
       "flowPolicyControl": flowPolicyControl,
       "flowPolicyStatus": flowPolicyStatus,
       "flowPolicyActiveServer": flowPolicyActiveServer,
       "flowPolicyServerAddrTable": flowPolicyServerAddrTable,
       "flowPolicyServerAddrEntry": flowPolicyServerAddrEntry,
       "flowPolicyServerAddrIndex": flowPolicyServerAddrIndex,
       "flowPolicyServerAddr": flowPolicyServerAddr,
       "flowPolicyConfig": flowPolicyConfig,
       "flowPolicyConfigPolicy": flowPolicyConfigPolicy,
       "flowPolicyConfigStatistics": flowPolicyConfigStatistics,
       "monLfap": monLfap,
       "monLfapCounts": monLfapCounts,
       "monLfapFARsSent": monLfapFARsSent,
       "monLfapFARsReceived": monLfapFARsReceived,
       "monLfapFAAsSent": monLfapFAAsSent,
       "monLfapFAAsReceived": monLfapFAAsReceived,
       "monLfapFAUsSent": monLfapFAUsSent,
       "monLfapFAUsReceived": monLfapFAUsReceived,
       "monLfapFUNsSent": monLfapFUNsSent,
       "monLfapFUNsReceived": monLfapFUNsReceived,
       "monLfapFUAsSent": monLfapFUAsSent,
       "monLfapFUAsReceived": monLfapFUAsReceived,
       "monLfapFCRsSent": monLfapFCRsSent,
       "monLfapFCRsReceived": monLfapFCRsReceived,
       "monLfapFCAsSent": monLfapFCAsSent,
       "monLfapFCAsReceived": monLfapFCAsReceived,
       "monLfapARsSent": monLfapARsSent,
       "monLfapARsReceived": monLfapARsReceived,
       "monLfapARAsSent": monLfapARAsSent,
       "monLfapARAsReceived": monLfapARAsReceived,
       "monLfapFSNsSent": monLfapFSNsSent,
       "monLfapFSNsReceived": monLfapFSNsReceived,
       "monLfapFSAsSent": monLfapFSAsSent,
       "monLfapFSAsReceived": monLfapFSAsReceived,
       "monLfapDroppedMessages": monLfapDroppedMessages,
       "monLfapVRsSent": monLfapVRsSent,
       "monLfapVRAsReceived": monLfapVRAsReceived,
       "monLfapConnSuccess": monLfapConnSuccess,
       "monLfapConnFailure": monLfapConnFailure,
       "monLfapBytesSent": monLfapBytesSent,
       "monLfapBytesReceived": monLfapBytesReceived,
       "monLfapMsgsSent": monLfapMsgsSent,
       "monLfapMsgsReceived": monLfapMsgsReceived,
       "monLfapMsgsReceivedError": monLfapMsgsReceivedError,
       "monLfapMsgsSendQueue": monLfapMsgsSendQueue,
       "monLfapMsgsSendQueuePeak": monLfapMsgsSendQueuePeak,
       "monLfapMsgsReceiveQueue": monLfapMsgsReceiveQueue,
       "monLfapDroppedMessagesConnected": monLfapDroppedMessagesConnected,
       "monLfapDroppedFARs": monLfapDroppedFARs,
       "monLfapDroppedFUNIs": monLfapDroppedFUNIs,
       "monLfapDroppedFUNs": monLfapDroppedFUNs,
       "monLfapDroppedARs": monLfapDroppedARs,
       "monLfapDroppedARAs": monLfapDroppedARAs,
       "monLfapDroppedVRs": monLfapDroppedVRs,
       "monCxnCounts": monCxnCounts,
       "monLfapYesRespCnt": monLfapYesRespCnt,
       "monLfapNoRespCnt": monLfapNoRespCnt,
       "monLfapFlowSetups": monLfapFlowSetups,
       "monLfapFlowTeardowns": monLfapFlowTeardowns,
       "monLfapFlowActivePeak": monLfapFlowActivePeak,
       "monActiveCxnCnt": monActiveCxnCnt,
       "flowPolicyPolling": flowPolicyPolling,
       "flowPolicyPollingTimerInterval": flowPolicyPollingTimerInterval,
       "flowPolicyPollingBatchSize": flowPolicyPollingBatchSize,
       "flowPolicyPollingBatchInterval": flowPolicyPollingBatchInterval,
       "flowPolicyPollingBatchUpdateInterval": flowPolicyPollingBatchUpdateInterval,
       "flowPolicyPollingLostContactInterval": flowPolicyPollingLostContactInterval,
       "flowPolicyPollingServerRetryInterval": flowPolicyPollingServerRetryInterval,
       "flowPolicyPollingSendQueueMaxSize": flowPolicyPollingSendQueueMaxSize,
       "flowPolicyPollingTaskPriority": flowPolicyPollingTaskPriority,
       "lfapConformance": lfapConformance,
       "lfapCompliances": lfapCompliances,
       "lfapGroups": lfapGroups,
       "lfapConfGroupV10": lfapConfGroupV10,
       "lfapComplianceV10": lfapComplianceV10,
       "lfapConfGroupV40": lfapConfGroupV40,
       "lfapComplianceV40": lfapComplianceV40}
)
