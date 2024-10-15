# SNMP MIB module (RFC1229-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC1229-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:10 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IfExtensions_ObjectIdentity = ObjectIdentity
ifExtensions = _IfExtensions_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 12)
)
_IfExtnsTable_Object = MibTable
ifExtnsTable = _IfExtnsTable_Object(
    (1, 3, 6, 1, 2, 1, 12, 1)
)
if mibBuilder.loadTexts:
    ifExtnsTable.setStatus("mandatory")
_IfExtnsEntry_Object = MibTableRow
ifExtnsEntry = _IfExtnsEntry_Object(
    (1, 3, 6, 1, 2, 1, 12, 1, 1)
)
ifExtnsEntry.setIndexNames(
    (0, "RFC1229-MIB", "ifExtnsIfIndex"),
)
if mibBuilder.loadTexts:
    ifExtnsEntry.setStatus("mandatory")
_IfExtnsIfIndex_Type = Integer32
_IfExtnsIfIndex_Object = MibTableColumn
ifExtnsIfIndex = _IfExtnsIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 12, 1, 1, 1),
    _IfExtnsIfIndex_Type()
)
ifExtnsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsIfIndex.setStatus("mandatory")
_IfExtnsChipSet_Type = ObjectIdentifier
_IfExtnsChipSet_Object = MibTableColumn
ifExtnsChipSet = _IfExtnsChipSet_Object(
    (1, 3, 6, 1, 2, 1, 12, 1, 1, 2),
    _IfExtnsChipSet_Type()
)
ifExtnsChipSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsChipSet.setStatus("mandatory")


class _IfExtnsRevWare_Type(DisplayString):
    """Custom type ifExtnsRevWare based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IfExtnsRevWare_Type.__name__ = "DisplayString"
_IfExtnsRevWare_Object = MibTableColumn
ifExtnsRevWare = _IfExtnsRevWare_Object(
    (1, 3, 6, 1, 2, 1, 12, 1, 1, 3),
    _IfExtnsRevWare_Type()
)
ifExtnsRevWare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsRevWare.setStatus("mandatory")
_IfExtnsMulticastsTransmittedOks_Type = Counter32
_IfExtnsMulticastsTransmittedOks_Object = MibTableColumn
ifExtnsMulticastsTransmittedOks = _IfExtnsMulticastsTransmittedOks_Object(
    (1, 3, 6, 1, 2, 1, 12, 1, 1, 4),
    _IfExtnsMulticastsTransmittedOks_Type()
)
ifExtnsMulticastsTransmittedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsMulticastsTransmittedOks.setStatus("mandatory")
_IfExtnsBroadcastsTransmittedOks_Type = Counter32
_IfExtnsBroadcastsTransmittedOks_Object = MibTableColumn
ifExtnsBroadcastsTransmittedOks = _IfExtnsBroadcastsTransmittedOks_Object(
    (1, 3, 6, 1, 2, 1, 12, 1, 1, 5),
    _IfExtnsBroadcastsTransmittedOks_Type()
)
ifExtnsBroadcastsTransmittedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsBroadcastsTransmittedOks.setStatus("mandatory")
_IfExtnsMulticastsReceivedOks_Type = Counter32
_IfExtnsMulticastsReceivedOks_Object = MibTableColumn
ifExtnsMulticastsReceivedOks = _IfExtnsMulticastsReceivedOks_Object(
    (1, 3, 6, 1, 2, 1, 12, 1, 1, 6),
    _IfExtnsMulticastsReceivedOks_Type()
)
ifExtnsMulticastsReceivedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsMulticastsReceivedOks.setStatus("mandatory")
_IfExtnsBroadcastsReceivedOks_Type = Counter32
_IfExtnsBroadcastsReceivedOks_Object = MibTableColumn
ifExtnsBroadcastsReceivedOks = _IfExtnsBroadcastsReceivedOks_Object(
    (1, 3, 6, 1, 2, 1, 12, 1, 1, 7),
    _IfExtnsBroadcastsReceivedOks_Type()
)
ifExtnsBroadcastsReceivedOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsBroadcastsReceivedOks.setStatus("mandatory")


class _IfExtnsPromiscuous_Type(Integer32):
    """Custom type ifExtnsPromiscuous based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_IfExtnsPromiscuous_Type.__name__ = "Integer32"
_IfExtnsPromiscuous_Object = MibTableColumn
ifExtnsPromiscuous = _IfExtnsPromiscuous_Object(
    (1, 3, 6, 1, 2, 1, 12, 1, 1, 8),
    _IfExtnsPromiscuous_Type()
)
ifExtnsPromiscuous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsPromiscuous.setStatus("mandatory")
_IfExtnsTestTable_Object = MibTable
ifExtnsTestTable = _IfExtnsTestTable_Object(
    (1, 3, 6, 1, 2, 1, 12, 2)
)
if mibBuilder.loadTexts:
    ifExtnsTestTable.setStatus("mandatory")
_IfExtnsTestEntry_Object = MibTableRow
ifExtnsTestEntry = _IfExtnsTestEntry_Object(
    (1, 3, 6, 1, 2, 1, 12, 2, 1)
)
ifExtnsTestEntry.setIndexNames(
    (0, "RFC1229-MIB", "ifExtnsTestIfIndex"),
)
if mibBuilder.loadTexts:
    ifExtnsTestEntry.setStatus("mandatory")
_IfExtnsTestIfIndex_Type = Integer32
_IfExtnsTestIfIndex_Object = MibTableColumn
ifExtnsTestIfIndex = _IfExtnsTestIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 12, 2, 1, 1),
    _IfExtnsTestIfIndex_Type()
)
ifExtnsTestIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsTestIfIndex.setStatus("mandatory")
_IfExtnsTestCommunity_Type = OctetString
_IfExtnsTestCommunity_Object = MibTableColumn
ifExtnsTestCommunity = _IfExtnsTestCommunity_Object(
    (1, 3, 6, 1, 2, 1, 12, 2, 1, 2),
    _IfExtnsTestCommunity_Type()
)
ifExtnsTestCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsTestCommunity.setStatus("mandatory")
_IfExtnsTestRequestId_Type = Integer32
_IfExtnsTestRequestId_Object = MibTableColumn
ifExtnsTestRequestId = _IfExtnsTestRequestId_Object(
    (1, 3, 6, 1, 2, 1, 12, 2, 1, 3),
    _IfExtnsTestRequestId_Type()
)
ifExtnsTestRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsTestRequestId.setStatus("mandatory")
_IfExtnsTestType_Type = ObjectIdentifier
_IfExtnsTestType_Object = MibTableColumn
ifExtnsTestType = _IfExtnsTestType_Object(
    (1, 3, 6, 1, 2, 1, 12, 2, 1, 4),
    _IfExtnsTestType_Type()
)
ifExtnsTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtnsTestType.setStatus("mandatory")


class _IfExtnsTestResult_Type(Integer32):
    """Custom type ifExtnsTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 6),
          ("failed", 7),
          ("inProgress", 3),
          ("none", 1),
          ("notSupported", 4),
          ("success", 2),
          ("unAbleToRun", 5))
    )


_IfExtnsTestResult_Type.__name__ = "Integer32"
_IfExtnsTestResult_Object = MibTableColumn
ifExtnsTestResult = _IfExtnsTestResult_Object(
    (1, 3, 6, 1, 2, 1, 12, 2, 1, 5),
    _IfExtnsTestResult_Type()
)
ifExtnsTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsTestResult.setStatus("mandatory")
_IfExtnsTestCode_Type = ObjectIdentifier
_IfExtnsTestCode_Object = MibTableColumn
ifExtnsTestCode = _IfExtnsTestCode_Object(
    (1, 3, 6, 1, 2, 1, 12, 2, 1, 6),
    _IfExtnsTestCode_Type()
)
ifExtnsTestCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsTestCode.setStatus("mandatory")
_IfExtnsRcvAddrTable_Object = MibTable
ifExtnsRcvAddrTable = _IfExtnsRcvAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 12, 3)
)
if mibBuilder.loadTexts:
    ifExtnsRcvAddrTable.setStatus("mandatory")
_IfExtnsRcvAddrEntry_Object = MibTableRow
ifExtnsRcvAddrEntry = _IfExtnsRcvAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 12, 3, 1)
)
ifExtnsRcvAddrEntry.setIndexNames(
    (0, "RFC1229-MIB", "ifExtnsRcvAddrIfIndex"),
    (0, "RFC1229-MIB", "ifExtnsRcvAddress"),
)
if mibBuilder.loadTexts:
    ifExtnsRcvAddrEntry.setStatus("mandatory")
_IfExtnsRcvAddrIfIndex_Type = Integer32
_IfExtnsRcvAddrIfIndex_Object = MibTableColumn
ifExtnsRcvAddrIfIndex = _IfExtnsRcvAddrIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 12, 3, 1, 1),
    _IfExtnsRcvAddrIfIndex_Type()
)
ifExtnsRcvAddrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsRcvAddrIfIndex.setStatus("mandatory")
_IfExtnsRcvAddress_Type = PhysAddress
_IfExtnsRcvAddress_Object = MibTableColumn
ifExtnsRcvAddress = _IfExtnsRcvAddress_Object(
    (1, 3, 6, 1, 2, 1, 12, 3, 1, 2),
    _IfExtnsRcvAddress_Type()
)
ifExtnsRcvAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtnsRcvAddress.setStatus("mandatory")


class _IfExtnsRcvAddrStatus_Type(Integer32):
    """Custom type ifExtnsRcvAddrStatus based on Integer32"""
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
        *(("invalid", 2),
          ("nonVolatile", 4),
          ("other", 1),
          ("volatile", 3))
    )


_IfExtnsRcvAddrStatus_Type.__name__ = "Integer32"
_IfExtnsRcvAddrStatus_Object = MibTableColumn
ifExtnsRcvAddrStatus = _IfExtnsRcvAddrStatus_Object(
    (1, 3, 6, 1, 2, 1, 12, 3, 1, 3),
    _IfExtnsRcvAddrStatus_Type()
)
ifExtnsRcvAddrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifExtnsRcvAddrStatus.setStatus("mandatory")
_WellKnownTests_ObjectIdentity = ObjectIdentity
wellKnownTests = _WellKnownTests_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 12, 4)
)
_TestFullDuplexLoopBack_ObjectIdentity = ObjectIdentity
testFullDuplexLoopBack = _TestFullDuplexLoopBack_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 12, 4, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1229-MIB",
    **{"ifExtensions": ifExtensions,
       "ifExtnsTable": ifExtnsTable,
       "ifExtnsEntry": ifExtnsEntry,
       "ifExtnsIfIndex": ifExtnsIfIndex,
       "ifExtnsChipSet": ifExtnsChipSet,
       "ifExtnsRevWare": ifExtnsRevWare,
       "ifExtnsMulticastsTransmittedOks": ifExtnsMulticastsTransmittedOks,
       "ifExtnsBroadcastsTransmittedOks": ifExtnsBroadcastsTransmittedOks,
       "ifExtnsMulticastsReceivedOks": ifExtnsMulticastsReceivedOks,
       "ifExtnsBroadcastsReceivedOks": ifExtnsBroadcastsReceivedOks,
       "ifExtnsPromiscuous": ifExtnsPromiscuous,
       "ifExtnsTestTable": ifExtnsTestTable,
       "ifExtnsTestEntry": ifExtnsTestEntry,
       "ifExtnsTestIfIndex": ifExtnsTestIfIndex,
       "ifExtnsTestCommunity": ifExtnsTestCommunity,
       "ifExtnsTestRequestId": ifExtnsTestRequestId,
       "ifExtnsTestType": ifExtnsTestType,
       "ifExtnsTestResult": ifExtnsTestResult,
       "ifExtnsTestCode": ifExtnsTestCode,
       "ifExtnsRcvAddrTable": ifExtnsRcvAddrTable,
       "ifExtnsRcvAddrEntry": ifExtnsRcvAddrEntry,
       "ifExtnsRcvAddrIfIndex": ifExtnsRcvAddrIfIndex,
       "ifExtnsRcvAddress": ifExtnsRcvAddress,
       "ifExtnsRcvAddrStatus": ifExtnsRcvAddrStatus,
       "wellKnownTests": wellKnownTests,
       "testFullDuplexLoopBack": testFullDuplexLoopBack}
)
