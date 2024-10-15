# SNMP MIB module (WAN-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WAN-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:27 2024
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



class Counter8(Integer32):
    """Custom type Counter8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class Counter16(Integer32):
    """Custom type Counter16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Codex_ObjectIdentity = ObjectIdentity
codex = _Codex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449)
)
_CdxProductSpecific_ObjectIdentity = ObjectIdentity
cdxProductSpecific = _CdxProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2)
)
_Cdx6500_ObjectIdentity = ObjectIdentity
cdx6500 = _Cdx6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1)
)
_Cdx6500Configuration_ObjectIdentity = ObjectIdentity
cdx6500Configuration = _Cdx6500Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2)
)
_Cdx6500CfgGeneralGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgGeneralGroup = _Cdx6500CfgGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2)
)
_Cdx6500GCTLANConnectionTable_Object = MibTable
cdx6500GCTLANConnectionTable = _Cdx6500GCTLANConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16)
)
if mibBuilder.loadTexts:
    cdx6500GCTLANConnectionTable.setStatus("mandatory")
_Cdx6500GCTLANConnectionEntry_Object = MibTableRow
cdx6500GCTLANConnectionEntry = _Cdx6500GCTLANConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1)
)
cdx6500GCTLANConnectionEntry.setIndexNames(
    (0, "WAN-OPT-MIB", "cdx6500WAEntryNumber"),
)
if mibBuilder.loadTexts:
    cdx6500GCTLANConnectionEntry.setStatus("mandatory")


class _Cdx6500WAEntryNumber_Type(Integer32):
    """Custom type cdx6500WAEntryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500WAEntryNumber_Type.__name__ = "Integer32"
_Cdx6500WAEntryNumber_Object = MibTableColumn
cdx6500WAEntryNumber = _Cdx6500WAEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1, 1),
    _Cdx6500WAEntryNumber_Type()
)
cdx6500WAEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAEntryNumber.setStatus("mandatory")


class _Cdx6500WALanForwarderType_Type(Integer32):
    """Custom type cdx6500WALanForwarderType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("brid", 0),
          ("brout", 2),
          ("nc", 100),
          ("newvalBrid", 50),
          ("rout", 1))
    )


_Cdx6500WALanForwarderType_Type.__name__ = "Integer32"
_Cdx6500WALanForwarderType_Object = MibTableColumn
cdx6500WALanForwarderType = _Cdx6500WALanForwarderType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1, 2),
    _Cdx6500WALanForwarderType_Type()
)
cdx6500WALanForwarderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WALanForwarderType.setStatus("mandatory")


class _Cdx6500WABridgeLinkNumber_Type(Integer32):
    """Custom type cdx6500WABridgeLinkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 36),
    )


_Cdx6500WABridgeLinkNumber_Type.__name__ = "Integer32"
_Cdx6500WABridgeLinkNumber_Object = MibTableColumn
cdx6500WABridgeLinkNumber = _Cdx6500WABridgeLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1, 3),
    _Cdx6500WABridgeLinkNumber_Type()
)
cdx6500WABridgeLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WABridgeLinkNumber.setStatus("mandatory")


class _Cdx6500WARouterInterfaceNum_Type(Integer32):
    """Custom type cdx6500WARouterInterfaceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 36),
    )


_Cdx6500WARouterInterfaceNum_Type.__name__ = "Integer32"
_Cdx6500WARouterInterfaceNum_Object = MibTableColumn
cdx6500WARouterInterfaceNum = _Cdx6500WARouterInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1, 4),
    _Cdx6500WARouterInterfaceNum_Type()
)
cdx6500WARouterInterfaceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WARouterInterfaceNum.setStatus("mandatory")


class _Cdx6500WACfgEncapsulationType_Type(Integer32):
    """Custom type cdx6500WACfgEncapsulationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("deprecatedObj", 1)
    )


_Cdx6500WACfgEncapsulationType_Type.__name__ = "Integer32"
_Cdx6500WACfgEncapsulationType_Object = MibTableColumn
cdx6500WACfgEncapsulationType = _Cdx6500WACfgEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1, 5),
    _Cdx6500WACfgEncapsulationType_Type()
)
cdx6500WACfgEncapsulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WACfgEncapsulationType.setStatus("deprecated")
_Cdx6500WAAutocallMnemonic_Type = DisplayString
_Cdx6500WAAutocallMnemonic_Object = MibTableColumn
cdx6500WAAutocallMnemonic = _Cdx6500WAAutocallMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1, 6),
    _Cdx6500WAAutocallMnemonic_Type()
)
cdx6500WAAutocallMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAAutocallMnemonic.setStatus("mandatory")


class _Cdx6500WAAutocallTimeout_Type(Integer32):
    """Custom type cdx6500WAAutocallTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500WAAutocallTimeout_Type.__name__ = "Integer32"
_Cdx6500WAAutocallTimeout_Object = MibTableColumn
cdx6500WAAutocallTimeout = _Cdx6500WAAutocallTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1, 7),
    _Cdx6500WAAutocallTimeout_Type()
)
cdx6500WAAutocallTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAAutocallTimeout.setStatus("mandatory")


class _Cdx6500WAMaxAutocallAttempts_Type(Integer32):
    """Custom type cdx6500WAMaxAutocallAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500WAMaxAutocallAttempts_Type.__name__ = "Integer32"
_Cdx6500WAMaxAutocallAttempts_Object = MibTableColumn
cdx6500WAMaxAutocallAttempts = _Cdx6500WAMaxAutocallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1, 8),
    _Cdx6500WAMaxAutocallAttempts_Type()
)
cdx6500WAMaxAutocallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAMaxAutocallAttempts.setStatus("mandatory")


class _Cdx6500WARemoteConnectionId_Type(Integer32):
    """Custom type cdx6500WARemoteConnectionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500WARemoteConnectionId_Type.__name__ = "Integer32"
_Cdx6500WARemoteConnectionId_Object = MibTableColumn
cdx6500WARemoteConnectionId = _Cdx6500WARemoteConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1, 9),
    _Cdx6500WARemoteConnectionId_Type()
)
cdx6500WARemoteConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WARemoteConnectionId.setStatus("mandatory")


class _Cdx6500WABillingRecords_Type(Integer32):
    """Custom type cdx6500WABillingRecords based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("newvalOff", 50),
          ("off", 0),
          ("on", 1))
    )


_Cdx6500WABillingRecords_Type.__name__ = "Integer32"
_Cdx6500WABillingRecords_Object = MibTableColumn
cdx6500WABillingRecords = _Cdx6500WABillingRecords_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1, 10),
    _Cdx6500WABillingRecords_Type()
)
cdx6500WABillingRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WABillingRecords.setStatus("mandatory")


class _Cdx6500WADataPassingPriority_Type(Integer32):
    """Custom type cdx6500WADataPassingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("exp", 3),
          ("high", 2),
          ("low", 0),
          ("med", 1),
          ("nc", 100),
          ("newvalLow", 50))
    )


_Cdx6500WADataPassingPriority_Type.__name__ = "Integer32"
_Cdx6500WADataPassingPriority_Object = MibTableColumn
cdx6500WADataPassingPriority = _Cdx6500WADataPassingPriority_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1, 11),
    _Cdx6500WADataPassingPriority_Type()
)
cdx6500WADataPassingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WADataPassingPriority.setStatus("mandatory")


class _Cdx6500WALCONQueueLimit_Type(Integer32):
    """Custom type cdx6500WALCONQueueLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500WALCONQueueLimit_Type.__name__ = "Integer32"
_Cdx6500WALCONQueueLimit_Object = MibTableColumn
cdx6500WALCONQueueLimit = _Cdx6500WALCONQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1, 12),
    _Cdx6500WALCONQueueLimit_Type()
)
cdx6500WALCONQueueLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WALCONQueueLimit.setStatus("mandatory")


class _Cdx6500WACfgEncapType_Type(Integer32):
    """Custom type cdx6500WACfgEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("codex", 0),
          ("nc", 100),
          ("newvalCodex", 50),
          ("rfc1294", 1),
          ("rfc877", 2))
    )


_Cdx6500WACfgEncapType_Type.__name__ = "Integer32"
_Cdx6500WACfgEncapType_Object = MibTableColumn
cdx6500WACfgEncapType = _Cdx6500WACfgEncapType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1, 13),
    _Cdx6500WACfgEncapType_Type()
)
cdx6500WACfgEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WACfgEncapType.setStatus("mandatory")


class _Cdx6500WACfgOnDemand_Type(Integer32):
    """Custom type cdx6500WACfgOnDemand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("nc", 100),
          ("newvalDisabled", 50))
    )


_Cdx6500WACfgOnDemand_Type.__name__ = "Integer32"
_Cdx6500WACfgOnDemand_Object = MibTableColumn
cdx6500WACfgOnDemand = _Cdx6500WACfgOnDemand_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1, 14),
    _Cdx6500WACfgOnDemand_Type()
)
cdx6500WACfgOnDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WACfgOnDemand.setStatus("mandatory")


class _Cdx6500WACfgIdleTimeout_Type(Integer32):
    """Custom type cdx6500WACfgIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500WACfgIdleTimeout_Type.__name__ = "Integer32"
_Cdx6500WACfgIdleTimeout_Object = MibTableColumn
cdx6500WACfgIdleTimeout = _Cdx6500WACfgIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1, 15),
    _Cdx6500WACfgIdleTimeout_Type()
)
cdx6500WACfgIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WACfgIdleTimeout.setStatus("mandatory")


class _Cdx6500WACfgLanConnectionType_Type(Integer32):
    """Custom type cdx6500WACfgLanConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("group", 1),
          ("nc", 100),
          ("newvalPtToPt", 50),
          ("ptToPt", 0))
    )


_Cdx6500WACfgLanConnectionType_Type.__name__ = "Integer32"
_Cdx6500WACfgLanConnectionType_Object = MibTableColumn
cdx6500WACfgLanConnectionType = _Cdx6500WACfgLanConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1, 16),
    _Cdx6500WACfgLanConnectionType_Type()
)
cdx6500WACfgLanConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WACfgLanConnectionType.setStatus("mandatory")
_Cdx6500WACfgNexthopIpAddress_Type = IpAddress
_Cdx6500WACfgNexthopIpAddress_Object = MibTableColumn
cdx6500WACfgNexthopIpAddress = _Cdx6500WACfgNexthopIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1, 17),
    _Cdx6500WACfgNexthopIpAddress_Type()
)
cdx6500WACfgNexthopIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WACfgNexthopIpAddress.setStatus("mandatory")


class _Cdx6500WACfgNexthopIpxNodeNumber_Type(Integer32):
    """Custom type cdx6500WACfgNexthopIpxNodeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Cdx6500WACfgNexthopIpxNodeNumber_Type.__name__ = "Integer32"
_Cdx6500WACfgNexthopIpxNodeNumber_Object = MibTableColumn
cdx6500WACfgNexthopIpxNodeNumber = _Cdx6500WACfgNexthopIpxNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1, 18),
    _Cdx6500WACfgNexthopIpxNodeNumber_Type()
)
cdx6500WACfgNexthopIpxNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WACfgNexthopIpxNodeNumber.setStatus("mandatory")


class _Cdx6500WACfgParallelSvc_Type(Integer32):
    """Custom type cdx6500WACfgParallelSvc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Cdx6500WACfgParallelSvc_Type.__name__ = "Integer32"
_Cdx6500WACfgParallelSvc_Object = MibTableColumn
cdx6500WACfgParallelSvc = _Cdx6500WACfgParallelSvc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1, 19),
    _Cdx6500WACfgParallelSvc_Type()
)
cdx6500WACfgParallelSvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WACfgParallelSvc.setStatus("mandatory")


class _Cdx6500WACfgParallelThreshold_Type(Integer32):
    """Custom type cdx6500WACfgParallelThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500WACfgParallelThreshold_Type.__name__ = "Integer32"
_Cdx6500WACfgParallelThreshold_Object = MibTableColumn
cdx6500WACfgParallelThreshold = _Cdx6500WACfgParallelThreshold_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1, 20),
    _Cdx6500WACfgParallelThreshold_Type()
)
cdx6500WACfgParallelThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WACfgParallelThreshold.setStatus("mandatory")
_Cdx6500WACfgParallelPort_Type = DisplayString
_Cdx6500WACfgParallelPort_Object = MibTableColumn
cdx6500WACfgParallelPort = _Cdx6500WACfgParallelPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1, 21),
    _Cdx6500WACfgParallelPort_Type()
)
cdx6500WACfgParallelPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WACfgParallelPort.setStatus("mandatory")


class _Cdx6500WACfgBroadcast_Type(Integer32):
    """Custom type cdx6500WACfgBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("nc", 100),
          ("newvalDisabled", 50))
    )


_Cdx6500WACfgBroadcast_Type.__name__ = "Integer32"
_Cdx6500WACfgBroadcast_Object = MibTableColumn
cdx6500WACfgBroadcast = _Cdx6500WACfgBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 16, 1, 22),
    _Cdx6500WACfgBroadcast_Type()
)
cdx6500WACfgBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WACfgBroadcast.setStatus("mandatory")
_Cdx6500GCTWanAdaptorGroup_ObjectIdentity = ObjectIdentity
cdx6500GCTWanAdaptorGroup = _Cdx6500GCTWanAdaptorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 17)
)
_Cdx6500GCMaxLCON_Type = Integer32
_Cdx6500GCMaxLCON_Object = MibScalar
cdx6500GCMaxLCON = _Cdx6500GCMaxLCON_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 17, 1),
    _Cdx6500GCMaxLCON_Type()
)
cdx6500GCMaxLCON.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500GCMaxLCON.setStatus("mandatory")
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500StatProtocolGroup = _Cdx6500StatProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1)
)
_Cdx6500PSTLANConnectionGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTLANConnectionGroup = _Cdx6500PSTLANConnectionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6)
)
_Cdx6500LCTDataSummaryStats_Object = MibTable
cdx6500LCTDataSummaryStats = _Cdx6500LCTDataSummaryStats_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cdx6500LCTDataSummaryStats.setStatus("mandatory")
_Cdx6500WADataStatEntry_Object = MibTableRow
cdx6500WADataStatEntry = _Cdx6500WADataStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 1, 1)
)
cdx6500WADataStatEntry.setIndexNames(
    (0, "WAN-OPT-MIB", "cdx6500WALanConnNumberData"),
)
if mibBuilder.loadTexts:
    cdx6500WADataStatEntry.setStatus("mandatory")


class _Cdx6500WALanConnNumberData_Type(Integer32):
    """Custom type cdx6500WALanConnNumberData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500WALanConnNumberData_Type.__name__ = "Integer32"
_Cdx6500WALanConnNumberData_Object = MibTableColumn
cdx6500WALanConnNumberData = _Cdx6500WALanConnNumberData_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 1, 1, 1),
    _Cdx6500WALanConnNumberData_Type()
)
cdx6500WALanConnNumberData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WALanConnNumberData.setStatus("mandatory")
_Cdx6500WALastStatResetTime_Type = DisplayString
_Cdx6500WALastStatResetTime_Object = MibTableColumn
cdx6500WALastStatResetTime = _Cdx6500WALastStatResetTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 1, 1, 2),
    _Cdx6500WALastStatResetTime_Type()
)
cdx6500WALastStatResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WALastStatResetTime.setStatus("mandatory")
_Cdx6500WAAvgPktSizeTx_Type = Counter16
_Cdx6500WAAvgPktSizeTx_Object = MibTableColumn
cdx6500WAAvgPktSizeTx = _Cdx6500WAAvgPktSizeTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 1, 1, 3),
    _Cdx6500WAAvgPktSizeTx_Type()
)
cdx6500WAAvgPktSizeTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAAvgPktSizeTx.setStatus("mandatory")
_Cdx6500WACurTxQueueDepth_Type = Counter32
_Cdx6500WACurTxQueueDepth_Object = MibTableColumn
cdx6500WACurTxQueueDepth = _Cdx6500WACurTxQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 1, 1, 4),
    _Cdx6500WACurTxQueueDepth_Type()
)
cdx6500WACurTxQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WACurTxQueueDepth.setStatus("mandatory")
_Cdx6500WAMaxTxQueueDepth_Type = Counter32
_Cdx6500WAMaxTxQueueDepth_Object = MibTableColumn
cdx6500WAMaxTxQueueDepth = _Cdx6500WAMaxTxQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 1, 1, 5),
    _Cdx6500WAMaxTxQueueDepth_Type()
)
cdx6500WAMaxTxQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAMaxTxQueueDepth.setStatus("mandatory")
_Cdx6500WAMaxTxQDepthTime_Type = DisplayString
_Cdx6500WAMaxTxQDepthTime_Object = MibTableColumn
cdx6500WAMaxTxQDepthTime = _Cdx6500WAMaxTxQDepthTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 1, 1, 6),
    _Cdx6500WAMaxTxQDepthTime_Type()
)
cdx6500WAMaxTxQDepthTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAMaxTxQDepthTime.setStatus("mandatory")
_Cdx6500WAAvgPktSizeRcv_Type = Counter16
_Cdx6500WAAvgPktSizeRcv_Object = MibTableColumn
cdx6500WAAvgPktSizeRcv = _Cdx6500WAAvgPktSizeRcv_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 1, 1, 7),
    _Cdx6500WAAvgPktSizeRcv_Type()
)
cdx6500WAAvgPktSizeRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAAvgPktSizeRcv.setStatus("mandatory")
_Cdx6500WATxPktDiscardFrwdReq_Type = Counter32
_Cdx6500WATxPktDiscardFrwdReq_Object = MibTableColumn
cdx6500WATxPktDiscardFrwdReq = _Cdx6500WATxPktDiscardFrwdReq_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 1, 1, 8),
    _Cdx6500WATxPktDiscardFrwdReq_Type()
)
cdx6500WATxPktDiscardFrwdReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WATxPktDiscardFrwdReq.setStatus("deprecated")
_Cdx6500WATxPktDiscardTransDelay_Type = Counter32
_Cdx6500WATxPktDiscardTransDelay_Object = MibTableColumn
cdx6500WATxPktDiscardTransDelay = _Cdx6500WATxPktDiscardTransDelay_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 1, 1, 9),
    _Cdx6500WATxPktDiscardTransDelay_Type()
)
cdx6500WATxPktDiscardTransDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WATxPktDiscardTransDelay.setStatus("mandatory")
_Cdx6500WATxPktDiscardCong_Type = Counter32
_Cdx6500WATxPktDiscardCong_Object = MibTableColumn
cdx6500WATxPktDiscardCong = _Cdx6500WATxPktDiscardCong_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 1, 1, 10),
    _Cdx6500WATxPktDiscardCong_Type()
)
cdx6500WATxPktDiscardCong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WATxPktDiscardCong.setStatus("mandatory")
_Cdx6500WATxPktDiscardMaxFrame_Type = Counter32
_Cdx6500WATxPktDiscardMaxFrame_Object = MibTableColumn
cdx6500WATxPktDiscardMaxFrame = _Cdx6500WATxPktDiscardMaxFrame_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 1, 1, 11),
    _Cdx6500WATxPktDiscardMaxFrame_Type()
)
cdx6500WATxPktDiscardMaxFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WATxPktDiscardMaxFrame.setStatus("mandatory")
_Cdx6500WATxPktDiscardCLrReq_Type = Counter32
_Cdx6500WATxPktDiscardCLrReq_Object = MibTableColumn
cdx6500WATxPktDiscardCLrReq = _Cdx6500WATxPktDiscardCLrReq_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 1, 1, 12),
    _Cdx6500WATxPktDiscardCLrReq_Type()
)
cdx6500WATxPktDiscardCLrReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WATxPktDiscardCLrReq.setStatus("mandatory")
_Cdx6500WATxPktDiscardCallEstab_Type = Counter32
_Cdx6500WATxPktDiscardCallEstab_Object = MibTableColumn
cdx6500WATxPktDiscardCallEstab = _Cdx6500WATxPktDiscardCallEstab_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 1, 1, 13),
    _Cdx6500WATxPktDiscardCallEstab_Type()
)
cdx6500WATxPktDiscardCallEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WATxPktDiscardCallEstab.setStatus("mandatory")
_Cdx6500WABytesOutstanding_Type = Counter32
_Cdx6500WABytesOutstanding_Object = MibTableColumn
cdx6500WABytesOutstanding = _Cdx6500WABytesOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 1, 1, 14),
    _Cdx6500WABytesOutstanding_Type()
)
cdx6500WABytesOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WABytesOutstanding.setStatus("mandatory")
_Cdx6500LCTCallSummaryStats_Object = MibTable
cdx6500LCTCallSummaryStats = _Cdx6500LCTCallSummaryStats_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cdx6500LCTCallSummaryStats.setStatus("mandatory")
_Cdx6500WACallStatEntry_Object = MibTableRow
cdx6500WACallStatEntry = _Cdx6500WACallStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 2, 1)
)
cdx6500WACallStatEntry.setIndexNames(
    (0, "WAN-OPT-MIB", "cdx6500WALanConnNumberCall"),
)
if mibBuilder.loadTexts:
    cdx6500WACallStatEntry.setStatus("mandatory")


class _Cdx6500WALanConnNumberCall_Type(Integer32):
    """Custom type cdx6500WALanConnNumberCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500WALanConnNumberCall_Type.__name__ = "Integer32"
_Cdx6500WALanConnNumberCall_Object = MibTableColumn
cdx6500WALanConnNumberCall = _Cdx6500WALanConnNumberCall_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 2, 1, 1),
    _Cdx6500WALanConnNumberCall_Type()
)
cdx6500WALanConnNumberCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WALanConnNumberCall.setStatus("mandatory")
_Cdx6500WAConnectionType_Type = DisplayString
_Cdx6500WAConnectionType_Object = MibTableColumn
cdx6500WAConnectionType = _Cdx6500WAConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 2, 1, 2),
    _Cdx6500WAConnectionType_Type()
)
cdx6500WAConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAConnectionType.setStatus("mandatory")


class _Cdx6500WAStatEncapsulationType_Type(Integer32):
    """Custom type cdx6500WAStatEncapsulationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("codex", 0),
          ("newvalCodex", 50),
          ("rfc1294", 1),
          ("rfc877", 2))
    )


_Cdx6500WAStatEncapsulationType_Type.__name__ = "Integer32"
_Cdx6500WAStatEncapsulationType_Object = MibTableColumn
cdx6500WAStatEncapsulationType = _Cdx6500WAStatEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 2, 1, 3),
    _Cdx6500WAStatEncapsulationType_Type()
)
cdx6500WAStatEncapsulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAStatEncapsulationType.setStatus("mandatory")


class _Cdx6500WAConnectionState_Type(Integer32):
    """Custom type cdx6500WAConnectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6,
              7,
              8,
              9,
              11,
              17,
              18,
              50)
        )
    )
    namedValues = NamedValues(
        *(("backinHeap", 1),
          ("calling", 11),
          ("connected", 17),
          ("connectedCongested", 18),
          ("disabled", 3),
          ("handshaking", 4),
          ("newvalUnconfigured", 50),
          ("notConnected", 2),
          ("unconfigured", 0),
          ("waitForCall", 6),
          ("wfccDisabled", 9),
          ("wfccRecall", 7),
          ("wfccWaitForCall", 8))
    )


_Cdx6500WAConnectionState_Type.__name__ = "Integer32"
_Cdx6500WAConnectionState_Object = MibTableColumn
cdx6500WAConnectionState = _Cdx6500WAConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 2, 1, 4),
    _Cdx6500WAConnectionState_Type()
)
cdx6500WAConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAConnectionState.setStatus("mandatory")
_Cdx6500WAForwardersConnected_Type = DisplayString
_Cdx6500WAForwardersConnected_Object = MibTableColumn
cdx6500WAForwardersConnected = _Cdx6500WAForwardersConnected_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 2, 1, 5),
    _Cdx6500WAForwardersConnected_Type()
)
cdx6500WAForwardersConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAForwardersConnected.setStatus("mandatory")
_Cdx6500WARemoteAddress_Type = DisplayString
_Cdx6500WARemoteAddress_Object = MibTableColumn
cdx6500WARemoteAddress = _Cdx6500WARemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 2, 1, 6),
    _Cdx6500WARemoteAddress_Type()
)
cdx6500WARemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WARemoteAddress.setStatus("mandatory")
_Cdx6500WANumAutocallAttempts_Type = Counter8
_Cdx6500WANumAutocallAttempts_Object = MibTableColumn
cdx6500WANumAutocallAttempts = _Cdx6500WANumAutocallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 2, 1, 7),
    _Cdx6500WANumAutocallAttempts_Type()
)
cdx6500WANumAutocallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WANumAutocallAttempts.setStatus("mandatory")
_Cdx6500WALastClearCauseCode_Type = Integer32
_Cdx6500WALastClearCauseCode_Object = MibTableColumn
cdx6500WALastClearCauseCode = _Cdx6500WALastClearCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 2, 1, 8),
    _Cdx6500WALastClearCauseCode_Type()
)
cdx6500WALastClearCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WALastClearCauseCode.setStatus("mandatory")
_Cdx6500WALastClearDiagCode_Type = Integer32
_Cdx6500WALastClearDiagCode_Object = MibTableColumn
cdx6500WALastClearDiagCode = _Cdx6500WALastClearDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 2, 1, 9),
    _Cdx6500WALastClearDiagCode_Type()
)
cdx6500WALastClearDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WALastClearDiagCode.setStatus("mandatory")
_Cdx6500WAParallelSvcsEstab_Type = Counter16
_Cdx6500WAParallelSvcsEstab_Object = MibTableColumn
cdx6500WAParallelSvcsEstab = _Cdx6500WAParallelSvcsEstab_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 2, 1, 10),
    _Cdx6500WAParallelSvcsEstab_Type()
)
cdx6500WAParallelSvcsEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAParallelSvcsEstab.setStatus("mandatory")
_Cdx6500WAParallelSvcsConfigured_Type = Counter8
_Cdx6500WAParallelSvcsConfigured_Object = MibTableColumn
cdx6500WAParallelSvcsConfigured = _Cdx6500WAParallelSvcsConfigured_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 2, 1, 11),
    _Cdx6500WAParallelSvcsConfigured_Type()
)
cdx6500WAParallelSvcsConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAParallelSvcsConfigured.setStatus("mandatory")
_Cdx6500LCTPacketSummaryStats_Object = MibTable
cdx6500LCTPacketSummaryStats = _Cdx6500LCTPacketSummaryStats_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 3)
)
if mibBuilder.loadTexts:
    cdx6500LCTPacketSummaryStats.setStatus("mandatory")
_Cdx6500WAPktStatEntry_Object = MibTableRow
cdx6500WAPktStatEntry = _Cdx6500WAPktStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 3, 1)
)
cdx6500WAPktStatEntry.setIndexNames(
    (0, "WAN-OPT-MIB", "cdx6500WALanConnNumberPkt"),
)
if mibBuilder.loadTexts:
    cdx6500WAPktStatEntry.setStatus("mandatory")


class _Cdx6500WALanConnNumberPkt_Type(Integer32):
    """Custom type cdx6500WALanConnNumberPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500WALanConnNumberPkt_Type.__name__ = "Integer32"
_Cdx6500WALanConnNumberPkt_Object = MibTableColumn
cdx6500WALanConnNumberPkt = _Cdx6500WALanConnNumberPkt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 3, 1, 1),
    _Cdx6500WALanConnNumberPkt_Type()
)
cdx6500WALanConnNumberPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WALanConnNumberPkt.setStatus("mandatory")
_Cdx6500WADataPktTx_Type = Counter32
_Cdx6500WADataPktTx_Object = MibTableColumn
cdx6500WADataPktTx = _Cdx6500WADataPktTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 3, 1, 2),
    _Cdx6500WADataPktTx_Type()
)
cdx6500WADataPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WADataPktTx.setStatus("mandatory")
_Cdx6500WADataPktRcv_Type = Counter32
_Cdx6500WADataPktRcv_Object = MibTableColumn
cdx6500WADataPktRcv = _Cdx6500WADataPktRcv_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 3, 1, 3),
    _Cdx6500WADataPktRcv_Type()
)
cdx6500WADataPktRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WADataPktRcv.setStatus("mandatory")
_Cdx6500WACallReqPktsTx_Type = Counter32
_Cdx6500WACallReqPktsTx_Object = MibTableColumn
cdx6500WACallReqPktsTx = _Cdx6500WACallReqPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 3, 1, 4),
    _Cdx6500WACallReqPktsTx_Type()
)
cdx6500WACallReqPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WACallReqPktsTx.setStatus("mandatory")
_Cdx6500WACallReqPktsRcv_Type = Counter32
_Cdx6500WACallReqPktsRcv_Object = MibTableColumn
cdx6500WACallReqPktsRcv = _Cdx6500WACallReqPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 3, 1, 5),
    _Cdx6500WACallReqPktsRcv_Type()
)
cdx6500WACallReqPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WACallReqPktsRcv.setStatus("mandatory")
_Cdx6500WACallAcceptPktsTx_Type = Counter32
_Cdx6500WACallAcceptPktsTx_Object = MibTableColumn
cdx6500WACallAcceptPktsTx = _Cdx6500WACallAcceptPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 3, 1, 6),
    _Cdx6500WACallAcceptPktsTx_Type()
)
cdx6500WACallAcceptPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WACallAcceptPktsTx.setStatus("mandatory")
_Cdx6500WACallAcceptPktsRcv_Type = Counter32
_Cdx6500WACallAcceptPktsRcv_Object = MibTableColumn
cdx6500WACallAcceptPktsRcv = _Cdx6500WACallAcceptPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 3, 1, 7),
    _Cdx6500WACallAcceptPktsRcv_Type()
)
cdx6500WACallAcceptPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WACallAcceptPktsRcv.setStatus("mandatory")
_Cdx6500WAClearReqPktsTx_Type = Counter32
_Cdx6500WAClearReqPktsTx_Object = MibTableColumn
cdx6500WAClearReqPktsTx = _Cdx6500WAClearReqPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 3, 1, 8),
    _Cdx6500WAClearReqPktsTx_Type()
)
cdx6500WAClearReqPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAClearReqPktsTx.setStatus("mandatory")
_Cdx6500WAClearReqPktsRcv_Type = Counter32
_Cdx6500WAClearReqPktsRcv_Object = MibTableColumn
cdx6500WAClearReqPktsRcv = _Cdx6500WAClearReqPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 3, 1, 9),
    _Cdx6500WAClearReqPktsRcv_Type()
)
cdx6500WAClearReqPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAClearReqPktsRcv.setStatus("mandatory")
_Cdx6500WAClearConfPktsTx_Type = Counter32
_Cdx6500WAClearConfPktsTx_Object = MibTableColumn
cdx6500WAClearConfPktsTx = _Cdx6500WAClearConfPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 3, 1, 10),
    _Cdx6500WAClearConfPktsTx_Type()
)
cdx6500WAClearConfPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAClearConfPktsTx.setStatus("mandatory")
_Cdx6500WAClearConfPktsRcv_Type = Counter32
_Cdx6500WAClearConfPktsRcv_Object = MibTableColumn
cdx6500WAClearConfPktsRcv = _Cdx6500WAClearConfPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 3, 1, 11),
    _Cdx6500WAClearConfPktsRcv_Type()
)
cdx6500WAClearConfPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAClearConfPktsRcv.setStatus("mandatory")
_Cdx6500WAResetReqPktsTx_Type = Counter32
_Cdx6500WAResetReqPktsTx_Object = MibTableColumn
cdx6500WAResetReqPktsTx = _Cdx6500WAResetReqPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 3, 1, 12),
    _Cdx6500WAResetReqPktsTx_Type()
)
cdx6500WAResetReqPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAResetReqPktsTx.setStatus("mandatory")
_Cdx6500WAResetReqPktsRcv_Type = Counter32
_Cdx6500WAResetReqPktsRcv_Object = MibTableColumn
cdx6500WAResetReqPktsRcv = _Cdx6500WAResetReqPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 3, 1, 13),
    _Cdx6500WAResetReqPktsRcv_Type()
)
cdx6500WAResetReqPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAResetReqPktsRcv.setStatus("mandatory")
_Cdx6500WAResetConfPktsTx_Type = Counter32
_Cdx6500WAResetConfPktsTx_Object = MibTableColumn
cdx6500WAResetConfPktsTx = _Cdx6500WAResetConfPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 3, 1, 14),
    _Cdx6500WAResetConfPktsTx_Type()
)
cdx6500WAResetConfPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAResetConfPktsTx.setStatus("mandatory")
_Cdx6500WAResetConfPktsRcv_Type = Counter32
_Cdx6500WAResetConfPktsRcv_Object = MibTableColumn
cdx6500WAResetConfPktsRcv = _Cdx6500WAResetConfPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6, 3, 1, 15),
    _Cdx6500WAResetConfPktsRcv_Type()
)
cdx6500WAResetConfPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAResetConfPktsRcv.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)
_Cdx6500ContWANAdaptor_ObjectIdentity = ObjectIdentity
cdx6500ContWANAdaptor = _Cdx6500ContWANAdaptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 1)
)
_Cdx6500ContWANAdaptorTable_Object = MibTable
cdx6500ContWANAdaptorTable = _Cdx6500ContWANAdaptorTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cdx6500ContWANAdaptorTable.setStatus("mandatory")
_Cdx6500ContWANAdaptorEntry_Object = MibTableRow
cdx6500ContWANAdaptorEntry = _Cdx6500ContWANAdaptorEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 1, 1, 1)
)
cdx6500ContWANAdaptorEntry.setIndexNames(
    (0, "WAN-OPT-MIB", "cdx6500WAControlLanConnNumber"),
)
if mibBuilder.loadTexts:
    cdx6500ContWANAdaptorEntry.setStatus("mandatory")


class _Cdx6500WAControlLanConnNumber_Type(Integer32):
    """Custom type cdx6500WAControlLanConnNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500WAControlLanConnNumber_Type.__name__ = "Integer32"
_Cdx6500WAControlLanConnNumber_Object = MibTableColumn
cdx6500WAControlLanConnNumber = _Cdx6500WAControlLanConnNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 1, 1, 1, 1),
    _Cdx6500WAControlLanConnNumber_Type()
)
cdx6500WAControlLanConnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500WAControlLanConnNumber.setStatus("mandatory")


class _Cdx6500WALanConnEnableDisable_Type(Integer32):
    """Custom type cdx6500WALanConnEnableDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0),
          ("newvalEnable", 50))
    )


_Cdx6500WALanConnEnableDisable_Type.__name__ = "Integer32"
_Cdx6500WALanConnEnableDisable_Object = MibTableColumn
cdx6500WALanConnEnableDisable = _Cdx6500WALanConnEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 1, 1, 1, 2),
    _Cdx6500WALanConnEnableDisable_Type()
)
cdx6500WALanConnEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500WALanConnEnableDisable.setStatus("mandatory")


class _Cdx6500WALanConnBoot_Type(Integer32):
    """Custom type cdx6500WALanConnBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("boot", 1)
    )


_Cdx6500WALanConnBoot_Type.__name__ = "Integer32"
_Cdx6500WALanConnBoot_Object = MibTableColumn
cdx6500WALanConnBoot = _Cdx6500WALanConnBoot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 1, 1, 1, 3),
    _Cdx6500WALanConnBoot_Type()
)
cdx6500WALanConnBoot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500WALanConnBoot.setStatus("mandatory")


class _Cdx6500WALanConnResetStat_Type(Integer32):
    """Custom type cdx6500WALanConnResetStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetStats", 1)
    )


_Cdx6500WALanConnResetStat_Type.__name__ = "Integer32"
_Cdx6500WALanConnResetStat_Object = MibTableColumn
cdx6500WALanConnResetStat = _Cdx6500WALanConnResetStat_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 1, 1, 1, 4),
    _Cdx6500WALanConnResetStat_Type()
)
cdx6500WALanConnResetStat.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500WALanConnResetStat.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WAN-OPT-MIB",
    **{"Counter8": Counter8,
       "Counter16": Counter16,
       "DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgGeneralGroup": cdx6500CfgGeneralGroup,
       "cdx6500GCTLANConnectionTable": cdx6500GCTLANConnectionTable,
       "cdx6500GCTLANConnectionEntry": cdx6500GCTLANConnectionEntry,
       "cdx6500WAEntryNumber": cdx6500WAEntryNumber,
       "cdx6500WALanForwarderType": cdx6500WALanForwarderType,
       "cdx6500WABridgeLinkNumber": cdx6500WABridgeLinkNumber,
       "cdx6500WARouterInterfaceNum": cdx6500WARouterInterfaceNum,
       "cdx6500WACfgEncapsulationType": cdx6500WACfgEncapsulationType,
       "cdx6500WAAutocallMnemonic": cdx6500WAAutocallMnemonic,
       "cdx6500WAAutocallTimeout": cdx6500WAAutocallTimeout,
       "cdx6500WAMaxAutocallAttempts": cdx6500WAMaxAutocallAttempts,
       "cdx6500WARemoteConnectionId": cdx6500WARemoteConnectionId,
       "cdx6500WABillingRecords": cdx6500WABillingRecords,
       "cdx6500WADataPassingPriority": cdx6500WADataPassingPriority,
       "cdx6500WALCONQueueLimit": cdx6500WALCONQueueLimit,
       "cdx6500WACfgEncapType": cdx6500WACfgEncapType,
       "cdx6500WACfgOnDemand": cdx6500WACfgOnDemand,
       "cdx6500WACfgIdleTimeout": cdx6500WACfgIdleTimeout,
       "cdx6500WACfgLanConnectionType": cdx6500WACfgLanConnectionType,
       "cdx6500WACfgNexthopIpAddress": cdx6500WACfgNexthopIpAddress,
       "cdx6500WACfgNexthopIpxNodeNumber": cdx6500WACfgNexthopIpxNodeNumber,
       "cdx6500WACfgParallelSvc": cdx6500WACfgParallelSvc,
       "cdx6500WACfgParallelThreshold": cdx6500WACfgParallelThreshold,
       "cdx6500WACfgParallelPort": cdx6500WACfgParallelPort,
       "cdx6500WACfgBroadcast": cdx6500WACfgBroadcast,
       "cdx6500GCTWanAdaptorGroup": cdx6500GCTWanAdaptorGroup,
       "cdx6500GCMaxLCON": cdx6500GCMaxLCON,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTLANConnectionGroup": cdx6500PSTLANConnectionGroup,
       "cdx6500LCTDataSummaryStats": cdx6500LCTDataSummaryStats,
       "cdx6500WADataStatEntry": cdx6500WADataStatEntry,
       "cdx6500WALanConnNumberData": cdx6500WALanConnNumberData,
       "cdx6500WALastStatResetTime": cdx6500WALastStatResetTime,
       "cdx6500WAAvgPktSizeTx": cdx6500WAAvgPktSizeTx,
       "cdx6500WACurTxQueueDepth": cdx6500WACurTxQueueDepth,
       "cdx6500WAMaxTxQueueDepth": cdx6500WAMaxTxQueueDepth,
       "cdx6500WAMaxTxQDepthTime": cdx6500WAMaxTxQDepthTime,
       "cdx6500WAAvgPktSizeRcv": cdx6500WAAvgPktSizeRcv,
       "cdx6500WATxPktDiscardFrwdReq": cdx6500WATxPktDiscardFrwdReq,
       "cdx6500WATxPktDiscardTransDelay": cdx6500WATxPktDiscardTransDelay,
       "cdx6500WATxPktDiscardCong": cdx6500WATxPktDiscardCong,
       "cdx6500WATxPktDiscardMaxFrame": cdx6500WATxPktDiscardMaxFrame,
       "cdx6500WATxPktDiscardCLrReq": cdx6500WATxPktDiscardCLrReq,
       "cdx6500WATxPktDiscardCallEstab": cdx6500WATxPktDiscardCallEstab,
       "cdx6500WABytesOutstanding": cdx6500WABytesOutstanding,
       "cdx6500LCTCallSummaryStats": cdx6500LCTCallSummaryStats,
       "cdx6500WACallStatEntry": cdx6500WACallStatEntry,
       "cdx6500WALanConnNumberCall": cdx6500WALanConnNumberCall,
       "cdx6500WAConnectionType": cdx6500WAConnectionType,
       "cdx6500WAStatEncapsulationType": cdx6500WAStatEncapsulationType,
       "cdx6500WAConnectionState": cdx6500WAConnectionState,
       "cdx6500WAForwardersConnected": cdx6500WAForwardersConnected,
       "cdx6500WARemoteAddress": cdx6500WARemoteAddress,
       "cdx6500WANumAutocallAttempts": cdx6500WANumAutocallAttempts,
       "cdx6500WALastClearCauseCode": cdx6500WALastClearCauseCode,
       "cdx6500WALastClearDiagCode": cdx6500WALastClearDiagCode,
       "cdx6500WAParallelSvcsEstab": cdx6500WAParallelSvcsEstab,
       "cdx6500WAParallelSvcsConfigured": cdx6500WAParallelSvcsConfigured,
       "cdx6500LCTPacketSummaryStats": cdx6500LCTPacketSummaryStats,
       "cdx6500WAPktStatEntry": cdx6500WAPktStatEntry,
       "cdx6500WALanConnNumberPkt": cdx6500WALanConnNumberPkt,
       "cdx6500WADataPktTx": cdx6500WADataPktTx,
       "cdx6500WADataPktRcv": cdx6500WADataPktRcv,
       "cdx6500WACallReqPktsTx": cdx6500WACallReqPktsTx,
       "cdx6500WACallReqPktsRcv": cdx6500WACallReqPktsRcv,
       "cdx6500WACallAcceptPktsTx": cdx6500WACallAcceptPktsTx,
       "cdx6500WACallAcceptPktsRcv": cdx6500WACallAcceptPktsRcv,
       "cdx6500WAClearReqPktsTx": cdx6500WAClearReqPktsTx,
       "cdx6500WAClearReqPktsRcv": cdx6500WAClearReqPktsRcv,
       "cdx6500WAClearConfPktsTx": cdx6500WAClearConfPktsTx,
       "cdx6500WAClearConfPktsRcv": cdx6500WAClearConfPktsRcv,
       "cdx6500WAResetReqPktsTx": cdx6500WAResetReqPktsTx,
       "cdx6500WAResetReqPktsRcv": cdx6500WAResetReqPktsRcv,
       "cdx6500WAResetConfPktsTx": cdx6500WAResetConfPktsTx,
       "cdx6500WAResetConfPktsRcv": cdx6500WAResetConfPktsRcv,
       "cdx6500Controls": cdx6500Controls,
       "cdx6500ContWANAdaptor": cdx6500ContWANAdaptor,
       "cdx6500ContWANAdaptorTable": cdx6500ContWANAdaptorTable,
       "cdx6500ContWANAdaptorEntry": cdx6500ContWANAdaptorEntry,
       "cdx6500WAControlLanConnNumber": cdx6500WAControlLanConnNumber,
       "cdx6500WALanConnEnableDisable": cdx6500WALanConnEnableDisable,
       "cdx6500WALanConnBoot": cdx6500WALanConnBoot,
       "cdx6500WALanConnResetStat": cdx6500WALanConnResetStat}
)
