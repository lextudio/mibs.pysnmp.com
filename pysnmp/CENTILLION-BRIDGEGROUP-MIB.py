# SNMP MIB module (CENTILLION-BRIDGEGROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CENTILLION-BRIDGEGROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:06 2024
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

(EnableIndicator,
 StatusIndicator,
 sysConfig) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "EnableIndicator",
    "StatusIndicator",
    "sysConfig")

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


# Types definitions



class BridgeGroupId(Integer32):
    """Custom type BridgeGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BridgeGroup_ObjectIdentity = ObjectIdentity
bridgeGroup = _BridgeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 24)
)
_Dot1dBaseGroupIdentifier_Type = BridgeGroupId
_Dot1dBaseGroupIdentifier_Object = MibScalar
dot1dBaseGroupIdentifier = _Dot1dBaseGroupIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 24, 1),
    _Dot1dBaseGroupIdentifier_Type()
)
dot1dBaseGroupIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dBaseGroupIdentifier.setStatus("mandatory")
_BridgeGroupTable_Object = MibTable
bridgeGroupTable = _BridgeGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 24, 2)
)
if mibBuilder.loadTexts:
    bridgeGroupTable.setStatus("mandatory")
_BridgeGroupEntry_Object = MibTableRow
bridgeGroupEntry = _BridgeGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 24, 2, 1)
)
bridgeGroupEntry.setIndexNames(
    (0, "CENTILLION-BRIDGEGROUP-MIB", "bridgeGroupIdentifier"),
)
if mibBuilder.loadTexts:
    bridgeGroupEntry.setStatus("mandatory")
_BridgeGroupIdentifier_Type = BridgeGroupId
_BridgeGroupIdentifier_Object = MibTableColumn
bridgeGroupIdentifier = _BridgeGroupIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 24, 2, 1, 1),
    _BridgeGroupIdentifier_Type()
)
bridgeGroupIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupIdentifier.setStatus("mandatory")
_BridgeGroupStatus_Type = StatusIndicator
_BridgeGroupStatus_Object = MibTableColumn
bridgeGroupStatus = _BridgeGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 24, 2, 1, 2),
    _BridgeGroupStatus_Type()
)
bridgeGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupStatus.setStatus("mandatory")


class _BridgeGroupBaseType_Type(Integer32):
    """Custom type bridgeGroupBaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("sourceroute-only", 4),
          ("srt", 5),
          ("translation", 6),
          ("transparent-only", 3),
          ("unknown", 2))
    )


_BridgeGroupBaseType_Type.__name__ = "Integer32"
_BridgeGroupBaseType_Object = MibTableColumn
bridgeGroupBaseType = _BridgeGroupBaseType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 24, 2, 1, 3),
    _BridgeGroupBaseType_Type()
)
bridgeGroupBaseType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupBaseType.setStatus("mandatory")


class _BridgeGroupStpProtocol_Type(Integer32):
    """Custom type bridgeGroupStpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("decLb100", 3),
          ("ibm", 5),
          ("ieee8021d", 4),
          ("none", 1),
          ("unknown", 2))
    )


_BridgeGroupStpProtocol_Type.__name__ = "Integer32"
_BridgeGroupStpProtocol_Object = MibTableColumn
bridgeGroupStpProtocol = _BridgeGroupStpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 24, 2, 1, 4),
    _BridgeGroupStpProtocol_Type()
)
bridgeGroupStpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupStpProtocol.setStatus("mandatory")


class _BridgeGroupPortType_Type(Integer32):
    """Custom type bridgeGroupPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 3),
          ("token-ring", 2),
          ("unknown", 1))
    )


_BridgeGroupPortType_Type.__name__ = "Integer32"
_BridgeGroupPortType_Object = MibTableColumn
bridgeGroupPortType = _BridgeGroupPortType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 24, 2, 1, 5),
    _BridgeGroupPortType_Type()
)
bridgeGroupPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupPortType.setStatus("mandatory")
_BridgeGroupNextPortIndex_Type = Integer32
_BridgeGroupNextPortIndex_Object = MibTableColumn
bridgeGroupNextPortIndex = _BridgeGroupNextPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 24, 2, 1, 6),
    _BridgeGroupNextPortIndex_Type()
)
bridgeGroupNextPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeGroupNextPortIndex.setStatus("mandatory")
_BridgeGroupTbRifEnable_Type = EnableIndicator
_BridgeGroupTbRifEnable_Object = MibTableColumn
bridgeGroupTbRifEnable = _BridgeGroupTbRifEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 24, 2, 1, 7),
    _BridgeGroupTbRifEnable_Type()
)
bridgeGroupTbRifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupTbRifEnable.setStatus("mandatory")


class _BridgeGroupTbRifRing_Type(Integer32):
    """Custom type bridgeGroupTbRifRing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_BridgeGroupTbRifRing_Type.__name__ = "Integer32"
_BridgeGroupTbRifRing_Object = MibTableColumn
bridgeGroupTbRifRing = _BridgeGroupTbRifRing_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 24, 2, 1, 8),
    _BridgeGroupTbRifRing_Type()
)
bridgeGroupTbRifRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupTbRifRing.setStatus("mandatory")
_BridgeGroupPortTable_Object = MibTable
bridgeGroupPortTable = _BridgeGroupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 24, 3)
)
if mibBuilder.loadTexts:
    bridgeGroupPortTable.setStatus("mandatory")
_BridgeGroupPortEntry_Object = MibTableRow
bridgeGroupPortEntry = _BridgeGroupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 24, 3, 1)
)
bridgeGroupPortEntry.setIndexNames(
    (0, "CENTILLION-BRIDGEGROUP-MIB", "bridgeGroupPortGroupId"),
    (0, "CENTILLION-BRIDGEGROUP-MIB", "bridgeGroupPortIndex"),
)
if mibBuilder.loadTexts:
    bridgeGroupPortEntry.setStatus("mandatory")
_BridgeGroupPortGroupId_Type = BridgeGroupId
_BridgeGroupPortGroupId_Object = MibTableColumn
bridgeGroupPortGroupId = _BridgeGroupPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 24, 3, 1, 1),
    _BridgeGroupPortGroupId_Type()
)
bridgeGroupPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeGroupPortGroupId.setStatus("mandatory")
_BridgeGroupPortIndex_Type = Integer32
_BridgeGroupPortIndex_Object = MibTableColumn
bridgeGroupPortIndex = _BridgeGroupPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 24, 3, 1, 2),
    _BridgeGroupPortIndex_Type()
)
bridgeGroupPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeGroupPortIndex.setStatus("mandatory")
_BridgeGroupPortStatus_Type = StatusIndicator
_BridgeGroupPortStatus_Object = MibTableColumn
bridgeGroupPortStatus = _BridgeGroupPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 24, 3, 1, 3),
    _BridgeGroupPortStatus_Type()
)
bridgeGroupPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeGroupPortStatus.setStatus("mandatory")
_BridgeGroupPortIfIndex_Type = Integer32
_BridgeGroupPortIfIndex_Object = MibTableColumn
bridgeGroupPortIfIndex = _BridgeGroupPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 24, 3, 1, 4),
    _BridgeGroupPortIfIndex_Type()
)
bridgeGroupPortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupPortIfIndex.setStatus("mandatory")


class _BridgeGroupPortSpanMode_Type(Integer32):
    """Custom type bridgeGroupPortSpanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-span", 1),
          ("disabled", 2),
          ("forced", 3))
    )


_BridgeGroupPortSpanMode_Type.__name__ = "Integer32"
_BridgeGroupPortSpanMode_Object = MibTableColumn
bridgeGroupPortSpanMode = _BridgeGroupPortSpanMode_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 24, 3, 1, 5),
    _BridgeGroupPortSpanMode_Type()
)
bridgeGroupPortSpanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupPortSpanMode.setStatus("mandatory")
_BridgeGroupPortFastStart_Type = EnableIndicator
_BridgeGroupPortFastStart_Object = MibTableColumn
bridgeGroupPortFastStart = _BridgeGroupPortFastStart_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 24, 3, 1, 6),
    _BridgeGroupPortFastStart_Type()
)
bridgeGroupPortFastStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeGroupPortFastStart.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILLION-BRIDGEGROUP-MIB",
    **{"BridgeGroupId": BridgeGroupId,
       "bridgeGroup": bridgeGroup,
       "dot1dBaseGroupIdentifier": dot1dBaseGroupIdentifier,
       "bridgeGroupTable": bridgeGroupTable,
       "bridgeGroupEntry": bridgeGroupEntry,
       "bridgeGroupIdentifier": bridgeGroupIdentifier,
       "bridgeGroupStatus": bridgeGroupStatus,
       "bridgeGroupBaseType": bridgeGroupBaseType,
       "bridgeGroupStpProtocol": bridgeGroupStpProtocol,
       "bridgeGroupPortType": bridgeGroupPortType,
       "bridgeGroupNextPortIndex": bridgeGroupNextPortIndex,
       "bridgeGroupTbRifEnable": bridgeGroupTbRifEnable,
       "bridgeGroupTbRifRing": bridgeGroupTbRifRing,
       "bridgeGroupPortTable": bridgeGroupPortTable,
       "bridgeGroupPortEntry": bridgeGroupPortEntry,
       "bridgeGroupPortGroupId": bridgeGroupPortGroupId,
       "bridgeGroupPortIndex": bridgeGroupPortIndex,
       "bridgeGroupPortStatus": bridgeGroupPortStatus,
       "bridgeGroupPortIfIndex": bridgeGroupPortIfIndex,
       "bridgeGroupPortSpanMode": bridgeGroupPortSpanMode,
       "bridgeGroupPortFastStart": bridgeGroupPortFastStart}
)
