# SNMP MIB module (T1E1-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/T1E1-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:43 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysicalPortNumber(Integer32):
    """Custom type PhysicalPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(49, 50),
    )





class VirtualPortNumber(Integer32):
    """Custom type VirtualPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 255),
    )




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
_Cdx6500CfgProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgProtocolGroup = _Cdx6500CfgProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1)
)
_Cdx6500PCTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTPortProtocolGroup = _Cdx6500PCTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1)
)
_Cdx6500PCTT1E1PortTable_ObjectIdentity = ObjectIdentity
cdx6500PCTT1E1PortTable = _Cdx6500PCTT1E1PortTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24)
)
_Cdx6500VPCTT1E1PortTable_Object = MibTable
cdx6500VPCTT1E1PortTable = _Cdx6500VPCTT1E1PortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3)
)
if mibBuilder.loadTexts:
    cdx6500VPCTT1E1PortTable.setStatus("mandatory")
_Cdx6500VPCTT1E1PortEntry_Object = MibTableRow
cdx6500VPCTT1E1PortEntry = _Cdx6500VPCTT1E1PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1)
)
cdx6500VPCTT1E1PortEntry.setIndexNames(
    (0, "T1E1-OPT-MIB", "cdx6500VPCTT1E1CfgIndex"),
)
if mibBuilder.loadTexts:
    cdx6500VPCTT1E1PortEntry.setStatus("mandatory")
_Cdx6500VPCTT1E1CfgPortNumber_Type = Integer32
_Cdx6500VPCTT1E1CfgPortNumber_Object = MibTableColumn
cdx6500VPCTT1E1CfgPortNumber = _Cdx6500VPCTT1E1CfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 1),
    _Cdx6500VPCTT1E1CfgPortNumber_Type()
)
cdx6500VPCTT1E1CfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPCTT1E1CfgPortNumber.setStatus("mandatory")


class _Cdx6500VPCTT1E1CfgPortType_Type(Integer32):
    """Custom type cdx6500VPCTT1E1CfgPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              100)
        )
    )
    namedValues = NamedValues(
        *(("bypassData", 6),
          ("bypassVoice", 5),
          ("data", 2),
          ("nc", 100),
          ("switchedData", 4),
          ("switchedVoice", 3),
          ("voice", 1))
    )


_Cdx6500VPCTT1E1CfgPortType_Type.__name__ = "Integer32"
_Cdx6500VPCTT1E1CfgPortType_Object = MibTableColumn
cdx6500VPCTT1E1CfgPortType = _Cdx6500VPCTT1E1CfgPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 2),
    _Cdx6500VPCTT1E1CfgPortType_Type()
)
cdx6500VPCTT1E1CfgPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPCTT1E1CfgPortType.setStatus("mandatory")
_Cdx6500VPCTT1E1CfgPhyPortNumber_Type = Integer32
_Cdx6500VPCTT1E1CfgPhyPortNumber_Object = MibTableColumn
cdx6500VPCTT1E1CfgPhyPortNumber = _Cdx6500VPCTT1E1CfgPhyPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 3),
    _Cdx6500VPCTT1E1CfgPhyPortNumber_Type()
)
cdx6500VPCTT1E1CfgPhyPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPCTT1E1CfgPhyPortNumber.setStatus("mandatory")
_Cdx6500VPCTT1E1CfgTimeSlotNumber_Type = Integer32
_Cdx6500VPCTT1E1CfgTimeSlotNumber_Object = MibTableColumn
cdx6500VPCTT1E1CfgTimeSlotNumber = _Cdx6500VPCTT1E1CfgTimeSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 4),
    _Cdx6500VPCTT1E1CfgTimeSlotNumber_Type()
)
cdx6500VPCTT1E1CfgTimeSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPCTT1E1CfgTimeSlotNumber.setStatus("mandatory")


class _Cdx6500VPCTT1E1CfgDS0Rate_Type(Integer32):
    """Custom type cdx6500VPCTT1E1CfgDS0Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("ds056k", 1),
          ("ds064k", 2),
          ("nc", 100))
    )


_Cdx6500VPCTT1E1CfgDS0Rate_Type.__name__ = "Integer32"
_Cdx6500VPCTT1E1CfgDS0Rate_Object = MibTableColumn
cdx6500VPCTT1E1CfgDS0Rate = _Cdx6500VPCTT1E1CfgDS0Rate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 5),
    _Cdx6500VPCTT1E1CfgDS0Rate_Type()
)
cdx6500VPCTT1E1CfgDS0Rate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPCTT1E1CfgDS0Rate.setStatus("mandatory")


class _Cdx6500VPCTT1E1CfgAggregateType_Type(Integer32):
    """Custom type cdx6500VPCTT1E1CfgAggregateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("so", 2),
          ("t1e1", 1))
    )


_Cdx6500VPCTT1E1CfgAggregateType_Type.__name__ = "Integer32"
_Cdx6500VPCTT1E1CfgAggregateType_Object = MibTableColumn
cdx6500VPCTT1E1CfgAggregateType = _Cdx6500VPCTT1E1CfgAggregateType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 6),
    _Cdx6500VPCTT1E1CfgAggregateType_Type()
)
cdx6500VPCTT1E1CfgAggregateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPCTT1E1CfgAggregateType.setStatus("mandatory")
_Cdx6500VPCTT1E1CfgSOPortNumber_Type = Integer32
_Cdx6500VPCTT1E1CfgSOPortNumber_Object = MibTableColumn
cdx6500VPCTT1E1CfgSOPortNumber = _Cdx6500VPCTT1E1CfgSOPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 7),
    _Cdx6500VPCTT1E1CfgSOPortNumber_Type()
)
cdx6500VPCTT1E1CfgSOPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPCTT1E1CfgSOPortNumber.setStatus("mandatory")
_Cdx6500VPCTT1E1CfgBChannel_Type = Integer32
_Cdx6500VPCTT1E1CfgBChannel_Object = MibTableColumn
cdx6500VPCTT1E1CfgBChannel = _Cdx6500VPCTT1E1CfgBChannel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 8),
    _Cdx6500VPCTT1E1CfgBChannel_Type()
)
cdx6500VPCTT1E1CfgBChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPCTT1E1CfgBChannel.setStatus("mandatory")


class _Cdx6500VPCTT1E1CfgLocalSubscriberAddress_Type(DisplayString):
    """Custom type cdx6500VPCTT1E1CfgLocalSubscriberAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Cdx6500VPCTT1E1CfgLocalSubscriberAddress_Type.__name__ = "DisplayString"
_Cdx6500VPCTT1E1CfgLocalSubscriberAddress_Object = MibTableColumn
cdx6500VPCTT1E1CfgLocalSubscriberAddress = _Cdx6500VPCTT1E1CfgLocalSubscriberAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 9),
    _Cdx6500VPCTT1E1CfgLocalSubscriberAddress_Type()
)
cdx6500VPCTT1E1CfgLocalSubscriberAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPCTT1E1CfgLocalSubscriberAddress.setStatus("mandatory")


class _Cdx6500VPCTT1E1CfgNetSpecCall_Type(Integer32):
    """Custom type cdx6500VPCTT1E1CfgNetSpecCall based on Integer32"""
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
              9,
              17,
              100)
        )
    )
    namedValues = NamedValues(
        *(("attAccunet", 7),
          ("attInt800", 9),
          ("attMc", 4),
          ("attMc800", 3),
          ("attMq", 17),
          ("attSdn", 2),
          ("nc", 100),
          ("none", 1),
          ("ntFx", 5),
          ("ntTieTrunk", 6))
    )


_Cdx6500VPCTT1E1CfgNetSpecCall_Type.__name__ = "Integer32"
_Cdx6500VPCTT1E1CfgNetSpecCall_Object = MibTableColumn
cdx6500VPCTT1E1CfgNetSpecCall = _Cdx6500VPCTT1E1CfgNetSpecCall_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 10),
    _Cdx6500VPCTT1E1CfgNetSpecCall_Type()
)
cdx6500VPCTT1E1CfgNetSpecCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPCTT1E1CfgNetSpecCall.setStatus("mandatory")


class _Cdx6500VPCTT1E1CfgPartyNumberType_Type(Integer32):
    """Custom type cdx6500VPCTT1E1CfgPartyNumberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              7,
              100)
        )
    )
    namedValues = NamedValues(
        *(("abbreviated", 7),
          ("international", 2),
          ("national", 3),
          ("nc", 100),
          ("subscriber", 5),
          ("unknown", 1))
    )


_Cdx6500VPCTT1E1CfgPartyNumberType_Type.__name__ = "Integer32"
_Cdx6500VPCTT1E1CfgPartyNumberType_Object = MibTableColumn
cdx6500VPCTT1E1CfgPartyNumberType = _Cdx6500VPCTT1E1CfgPartyNumberType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 11),
    _Cdx6500VPCTT1E1CfgPartyNumberType_Type()
)
cdx6500VPCTT1E1CfgPartyNumberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPCTT1E1CfgPartyNumberType.setStatus("mandatory")


class _Cdx6500VPCTT1E1CfgPartyNumberPlan_Type(Integer32):
    """Custom type cdx6500VPCTT1E1CfgPartyNumberPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              100)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 2),
          ("nc", 100),
          ("private", 10),
          ("telephony", 3),
          ("unknown", 1))
    )


_Cdx6500VPCTT1E1CfgPartyNumberPlan_Type.__name__ = "Integer32"
_Cdx6500VPCTT1E1CfgPartyNumberPlan_Object = MibTableColumn
cdx6500VPCTT1E1CfgPartyNumberPlan = _Cdx6500VPCTT1E1CfgPartyNumberPlan_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 12),
    _Cdx6500VPCTT1E1CfgPartyNumberPlan_Type()
)
cdx6500VPCTT1E1CfgPartyNumberPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPCTT1E1CfgPartyNumberPlan.setStatus("mandatory")
_Cdx6500VPCTT1E1CfgIndex_Type = Integer32
_Cdx6500VPCTT1E1CfgIndex_Object = MibTableColumn
cdx6500VPCTT1E1CfgIndex = _Cdx6500VPCTT1E1CfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 24, 3, 1, 13),
    _Cdx6500VPCTT1E1CfgIndex_Type()
)
cdx6500VPCTT1E1CfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VPCTT1E1CfgIndex.setStatus("mandatory")
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500StatProtocolGroup = _Cdx6500StatProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1)
)
_Cdx6500PSTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTPortProtocolGroup = _Cdx6500PSTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1)
)
_Cdx6500PSTT1E1PortTable_ObjectIdentity = ObjectIdentity
cdx6500PSTT1E1PortTable = _Cdx6500PSTT1E1PortTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 25)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T1E1-OPT-MIB",
    **{"DisplayString": DisplayString,
       "PhysicalPortNumber": PhysicalPortNumber,
       "VirtualPortNumber": VirtualPortNumber,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PCTT1E1PortTable": cdx6500PCTT1E1PortTable,
       "cdx6500VPCTT1E1PortTable": cdx6500VPCTT1E1PortTable,
       "cdx6500VPCTT1E1PortEntry": cdx6500VPCTT1E1PortEntry,
       "cdx6500VPCTT1E1CfgPortNumber": cdx6500VPCTT1E1CfgPortNumber,
       "cdx6500VPCTT1E1CfgPortType": cdx6500VPCTT1E1CfgPortType,
       "cdx6500VPCTT1E1CfgPhyPortNumber": cdx6500VPCTT1E1CfgPhyPortNumber,
       "cdx6500VPCTT1E1CfgTimeSlotNumber": cdx6500VPCTT1E1CfgTimeSlotNumber,
       "cdx6500VPCTT1E1CfgDS0Rate": cdx6500VPCTT1E1CfgDS0Rate,
       "cdx6500VPCTT1E1CfgAggregateType": cdx6500VPCTT1E1CfgAggregateType,
       "cdx6500VPCTT1E1CfgSOPortNumber": cdx6500VPCTT1E1CfgSOPortNumber,
       "cdx6500VPCTT1E1CfgBChannel": cdx6500VPCTT1E1CfgBChannel,
       "cdx6500VPCTT1E1CfgLocalSubscriberAddress": cdx6500VPCTT1E1CfgLocalSubscriberAddress,
       "cdx6500VPCTT1E1CfgNetSpecCall": cdx6500VPCTT1E1CfgNetSpecCall,
       "cdx6500VPCTT1E1CfgPartyNumberType": cdx6500VPCTT1E1CfgPartyNumberType,
       "cdx6500VPCTT1E1CfgPartyNumberPlan": cdx6500VPCTT1E1CfgPartyNumberPlan,
       "cdx6500VPCTT1E1CfgIndex": cdx6500VPCTT1E1CfgIndex,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PSTT1E1PortTable": cdx6500PSTT1E1PortTable}
)
