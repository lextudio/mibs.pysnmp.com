# SNMP MIB module (IDS0-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IDS0-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:08 2024
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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_Nas_ObjectIdentity = ObjectIdentity
nas = _Nas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1)
)
_Ids0_ObjectIdentity = ObjectIdentity
ids0 = _Ids0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 16)
)
_Ids0CfgTable_Object = MibTable
ids0CfgTable = _Ids0CfgTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 1)
)
if mibBuilder.loadTexts:
    ids0CfgTable.setStatus("mandatory")
_Ids0CfgEntry_Object = MibTableRow
ids0CfgEntry = _Ids0CfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 1, 1)
)
ids0CfgEntry.setIndexNames(
    (0, "IDS0-MIB", "ids0CfgDs1Index"),
    (0, "IDS0-MIB", "ids0CfgDs0Index"),
)
if mibBuilder.loadTexts:
    ids0CfgEntry.setStatus("mandatory")
_Ids0CfgDs1Index_Type = Integer32
_Ids0CfgDs1Index_Object = MibTableColumn
ids0CfgDs1Index = _Ids0CfgDs1Index_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 1, 1, 1),
    _Ids0CfgDs1Index_Type()
)
ids0CfgDs1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ids0CfgDs1Index.setStatus("mandatory")
_Ids0CfgDs0Index_Type = Integer32
_Ids0CfgDs0Index_Object = MibTableColumn
ids0CfgDs0Index = _Ids0CfgDs0Index_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 1, 1, 2),
    _Ids0CfgDs0Index_Type()
)
ids0CfgDs0Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ids0CfgDs0Index.setStatus("mandatory")


class _Ids0CfgDs0Id_Type(DisplayString):
    """Custom type ids0CfgDs0Id based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Ids0CfgDs0Id_Type.__name__ = "DisplayString"
_Ids0CfgDs0Id_Object = MibTableColumn
ids0CfgDs0Id = _Ids0CfgDs0Id_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 1, 1, 3),
    _Ids0CfgDs0Id_Type()
)
ids0CfgDs0Id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ids0CfgDs0Id.setStatus("mandatory")


class _Ids0CfgBlockCallType_Type(Integer32):
    """Custom type ids0CfgBlockCallType based on Integer32"""
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
        *(("blockAll", 5),
          ("blockAnalog", 3),
          ("blockDigital", 4),
          ("blockNone", 2),
          ("notSupported", 1))
    )


_Ids0CfgBlockCallType_Type.__name__ = "Integer32"
_Ids0CfgBlockCallType_Object = MibTableColumn
ids0CfgBlockCallType = _Ids0CfgBlockCallType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 1, 1, 4),
    _Ids0CfgBlockCallType_Type()
)
ids0CfgBlockCallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ids0CfgBlockCallType.setStatus("mandatory")


class _Ids0CfgDs0AssignedSlot_Type(Integer32):
    """Custom type ids0CfgDs0AssignedSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 17),
    )


_Ids0CfgDs0AssignedSlot_Type.__name__ = "Integer32"
_Ids0CfgDs0AssignedSlot_Object = MibTableColumn
ids0CfgDs0AssignedSlot = _Ids0CfgDs0AssignedSlot_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 1, 1, 5),
    _Ids0CfgDs0AssignedSlot_Type()
)
ids0CfgDs0AssignedSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ids0CfgDs0AssignedSlot.setStatus("mandatory")


class _Ids0CfgDs0AssignedChannel_Type(Integer32):
    """Custom type ids0CfgDs0AssignedChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33),
    )


_Ids0CfgDs0AssignedChannel_Type.__name__ = "Integer32"
_Ids0CfgDs0AssignedChannel_Object = MibTableColumn
ids0CfgDs0AssignedChannel = _Ids0CfgDs0AssignedChannel_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 1, 1, 6),
    _Ids0CfgDs0AssignedChannel_Type()
)
ids0CfgDs0AssignedChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ids0CfgDs0AssignedChannel.setStatus("mandatory")


class _Ids0CfgDs0SrvcState_Type(Integer32):
    """Custom type ids0CfgDs0SrvcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 2),
          ("localOutOfService", 3),
          ("notSupported", 1))
    )


_Ids0CfgDs0SrvcState_Type.__name__ = "Integer32"
_Ids0CfgDs0SrvcState_Object = MibTableColumn
ids0CfgDs0SrvcState = _Ids0CfgDs0SrvcState_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 1, 1, 7),
    _Ids0CfgDs0SrvcState_Type()
)
ids0CfgDs0SrvcState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ids0CfgDs0SrvcState.setStatus("mandatory")


class _Ids0CfgNailUpDs0_Type(Integer32):
    """Custom type ids0CfgNailUpDs0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("transparent", 2))
    )


_Ids0CfgNailUpDs0_Type.__name__ = "Integer32"
_Ids0CfgNailUpDs0_Object = MibTableColumn
ids0CfgNailUpDs0 = _Ids0CfgNailUpDs0_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 1, 1, 8),
    _Ids0CfgNailUpDs0_Type()
)
ids0CfgNailUpDs0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ids0CfgNailUpDs0.setStatus("mandatory")
_Ids0StatTable_Object = MibTable
ids0StatTable = _Ids0StatTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 2)
)
if mibBuilder.loadTexts:
    ids0StatTable.setStatus("mandatory")
_Ids0StatEntry_Object = MibTableRow
ids0StatEntry = _Ids0StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 2, 1)
)
ids0StatEntry.setIndexNames(
    (0, "IDS0-MIB", "ids0StatDs1Index"),
    (0, "IDS0-MIB", "ids0StatDs0Index"),
)
if mibBuilder.loadTexts:
    ids0StatEntry.setStatus("mandatory")
_Ids0StatDs1Index_Type = Integer32
_Ids0StatDs1Index_Object = MibTableColumn
ids0StatDs1Index = _Ids0StatDs1Index_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 2, 1, 1),
    _Ids0StatDs1Index_Type()
)
ids0StatDs1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ids0StatDs1Index.setStatus("mandatory")
_Ids0StatDs0Index_Type = Integer32
_Ids0StatDs0Index_Object = MibTableColumn
ids0StatDs0Index = _Ids0StatDs0Index_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 2, 1, 2),
    _Ids0StatDs0Index_Type()
)
ids0StatDs0Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ids0StatDs0Index.setStatus("mandatory")


class _Ids0StatDs0_Type(Integer32):
    """Custom type ids0StatDs0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("connectedIn", 5),
          ("connectedOut", 6),
          ("dialingIn", 3),
          ("dialingOut", 4),
          ("ds0CallDisc", 22),
          ("ds0InMaint", 25),
          ("ds0IsDchan", 23),
          ("ds0IsFchan", 26),
          ("ds0LclOutOfService", 27),
          ("ds0OutOfServ", 24),
          ("idle", 2),
          ("other", 1))
    )


_Ids0StatDs0_Type.__name__ = "Integer32"
_Ids0StatDs0_Object = MibTableColumn
ids0StatDs0 = _Ids0StatDs0_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 2, 1, 3),
    _Ids0StatDs0_Type()
)
ids0StatDs0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ids0StatDs0.setStatus("mandatory")


class _Ids0StatDevConnTo_Type(Integer32):
    """Custom type ids0StatDevConnTo based on Integer32"""
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
        *(("isdnGateway", 2),
          ("none", 1),
          ("quadIModem", 4),
          ("quadModem", 3))
    )


_Ids0StatDevConnTo_Type.__name__ = "Integer32"
_Ids0StatDevConnTo_Object = MibTableColumn
ids0StatDevConnTo = _Ids0StatDevConnTo_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 2, 1, 4),
    _Ids0StatDevConnTo_Type()
)
ids0StatDevConnTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ids0StatDevConnTo.setStatus("mandatory")


class _Ids0StatSlotConnTo_Type(Integer32):
    """Custom type ids0StatSlotConnTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Ids0StatSlotConnTo_Type.__name__ = "Integer32"
_Ids0StatSlotConnTo_Object = MibTableColumn
ids0StatSlotConnTo = _Ids0StatSlotConnTo_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 2, 1, 5),
    _Ids0StatSlotConnTo_Type()
)
ids0StatSlotConnTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ids0StatSlotConnTo.setStatus("mandatory")


class _Ids0StatChanConnTo_Type(Integer32):
    """Custom type ids0StatChanConnTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ids0StatChanConnTo_Type.__name__ = "Integer32"
_Ids0StatChanConnTo_Object = MibTableColumn
ids0StatChanConnTo = _Ids0StatChanConnTo_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 2, 1, 6),
    _Ids0StatChanConnTo_Type()
)
ids0StatChanConnTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ids0StatChanConnTo.setStatus("mandatory")


class _Ids0StatDs0SrvcState_Type(Integer32):
    """Custom type ids0StatDs0SrvcState based on Integer32"""
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
        *(("inService", 2),
          ("localOutOfService", 3),
          ("maintenance", 4),
          ("notSupported", 1),
          ("remoteOutOfService", 5))
    )


_Ids0StatDs0SrvcState_Type.__name__ = "Integer32"
_Ids0StatDs0SrvcState_Object = MibTableColumn
ids0StatDs0SrvcState = _Ids0StatDs0SrvcState_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 2, 1, 7),
    _Ids0StatDs0SrvcState_Type()
)
ids0StatDs0SrvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ids0StatDs0SrvcState.setStatus("mandatory")
_Ids0StatCallArrivalTime_Type = Integer32
_Ids0StatCallArrivalTime_Object = MibTableColumn
ids0StatCallArrivalTime = _Ids0StatCallArrivalTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 2, 1, 8),
    _Ids0StatCallArrivalTime_Type()
)
ids0StatCallArrivalTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ids0StatCallArrivalTime.setStatus("mandatory")
_Ids0StatCallConnectTime_Type = Integer32
_Ids0StatCallConnectTime_Object = MibTableColumn
ids0StatCallConnectTime = _Ids0StatCallConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 2, 1, 9),
    _Ids0StatCallConnectTime_Type()
)
ids0StatCallConnectTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ids0StatCallConnectTime.setStatus("mandatory")
_Ids0StatCallTerminateTime_Type = Integer32
_Ids0StatCallTerminateTime_Object = MibTableColumn
ids0StatCallTerminateTime = _Ids0StatCallTerminateTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 2, 1, 10),
    _Ids0StatCallTerminateTime_Type()
)
ids0StatCallTerminateTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ids0StatCallTerminateTime.setStatus("mandatory")


class _Ids0StatCallType_Type(Integer32):
    """Custom type ids0StatCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("analog", 1),
          ("digital", 2))
    )


_Ids0StatCallType_Type.__name__ = "Integer32"
_Ids0StatCallType_Object = MibTableColumn
ids0StatCallType = _Ids0StatCallType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 2, 1, 11),
    _Ids0StatCallType_Type()
)
ids0StatCallType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ids0StatCallType.setStatus("mandatory")


class _Ids0StatCallBlockState_Type(Integer32):
    """Custom type ids0StatCallBlockState based on Integer32"""
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
        *(("blockAll", 5),
          ("blockAnalog", 3),
          ("blockDigital", 4),
          ("blockNone", 2),
          ("notSupported", 1))
    )


_Ids0StatCallBlockState_Type.__name__ = "Integer32"
_Ids0StatCallBlockState_Object = MibTableColumn
ids0StatCallBlockState = _Ids0StatCallBlockState_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 2, 1, 12),
    _Ids0StatCallBlockState_Type()
)
ids0StatCallBlockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ids0StatCallBlockState.setStatus("mandatory")


class _Ids0StatCallDirn_Type(Integer32):
    """Custom type ids0StatCallDirn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_Ids0StatCallDirn_Type.__name__ = "Integer32"
_Ids0StatCallDirn_Object = MibTableColumn
ids0StatCallDirn = _Ids0StatCallDirn_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 2, 1, 13),
    _Ids0StatCallDirn_Type()
)
ids0StatCallDirn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ids0StatCallDirn.setStatus("mandatory")
_Ids0CmdTable_Object = MibTable
ids0CmdTable = _Ids0CmdTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 3)
)
if mibBuilder.loadTexts:
    ids0CmdTable.setStatus("mandatory")
_Ids0CmdEntry_Object = MibTableRow
ids0CmdEntry = _Ids0CmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 3, 1)
)
ids0CmdEntry.setIndexNames(
    (0, "IDS0-MIB", "ids0CmdDs1Index"),
    (0, "IDS0-MIB", "ids0CmdDs0Index"),
)
if mibBuilder.loadTexts:
    ids0CmdEntry.setStatus("mandatory")
_Ids0CmdDs1Index_Type = Integer32
_Ids0CmdDs1Index_Object = MibTableColumn
ids0CmdDs1Index = _Ids0CmdDs1Index_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 3, 1, 1),
    _Ids0CmdDs1Index_Type()
)
ids0CmdDs1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ids0CmdDs1Index.setStatus("mandatory")
_Ids0CmdDs0Index_Type = Integer32
_Ids0CmdDs0Index_Object = MibTableColumn
ids0CmdDs0Index = _Ids0CmdDs0Index_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 3, 1, 2),
    _Ids0CmdDs0Index_Type()
)
ids0CmdDs0Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ids0CmdDs0Index.setStatus("mandatory")


class _Ids0CmdMgtStationId_Type(OctetString):
    """Custom type ids0CmdMgtStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ids0CmdMgtStationId_Type.__name__ = "OctetString"
_Ids0CmdMgtStationId_Object = MibTableColumn
ids0CmdMgtStationId = _Ids0CmdMgtStationId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 3, 1, 3),
    _Ids0CmdMgtStationId_Type()
)
ids0CmdMgtStationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ids0CmdMgtStationId.setStatus("mandatory")
_Ids0CmdReqId_Type = Integer32
_Ids0CmdReqId_Object = MibTableColumn
ids0CmdReqId = _Ids0CmdReqId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 3, 1, 4),
    _Ids0CmdReqId_Type()
)
ids0CmdReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ids0CmdReqId.setStatus("mandatory")


class _Ids0CmdFunction_Type(Integer32):
    """Custom type ids0CmdFunction based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("blockAllCalls", 7),
          ("blockAnalogCalls", 5),
          ("blockDigitalCalls", 6),
          ("blockNoCalls", 8),
          ("disconnect", 2),
          ("inService", 3),
          ("localOutofService", 4),
          ("noCommand", 1))
    )


_Ids0CmdFunction_Type.__name__ = "Integer32"
_Ids0CmdFunction_Object = MibTableColumn
ids0CmdFunction = _Ids0CmdFunction_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 3, 1, 5),
    _Ids0CmdFunction_Type()
)
ids0CmdFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ids0CmdFunction.setStatus("mandatory")


class _Ids0CmdForce_Type(Integer32):
    """Custom type ids0CmdForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("force", 1),
          ("noForce", 2))
    )


_Ids0CmdForce_Type.__name__ = "Integer32"
_Ids0CmdForce_Object = MibTableColumn
ids0CmdForce = _Ids0CmdForce_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 3, 1, 6),
    _Ids0CmdForce_Type()
)
ids0CmdForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ids0CmdForce.setStatus("mandatory")


class _Ids0CmdParam_Type(OctetString):
    """Custom type ids0CmdParam based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Ids0CmdParam_Type.__name__ = "OctetString"
_Ids0CmdParam_Object = MibTableColumn
ids0CmdParam = _Ids0CmdParam_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 3, 1, 7),
    _Ids0CmdParam_Type()
)
ids0CmdParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ids0CmdParam.setStatus("mandatory")


class _Ids0CmdResult_Type(Integer32):
    """Custom type ids0CmdResult based on Integer32"""
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


_Ids0CmdResult_Type.__name__ = "Integer32"
_Ids0CmdResult_Object = MibTableColumn
ids0CmdResult = _Ids0CmdResult_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 3, 1, 8),
    _Ids0CmdResult_Type()
)
ids0CmdResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ids0CmdResult.setStatus("mandatory")


class _Ids0CmdCode_Type(Integer32):
    """Custom type ids0CmdCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              8,
              12,
              20,
              22,
              73)
        )
    )
    namedValues = NamedValues(
        *(("deviceDisabled", 22),
          ("noError", 1),
          ("noResponse", 12),
          ("pendingSoftwareDownload", 73),
          ("slotEmpty", 8),
          ("unable", 2),
          ("unrecognizedCommand", 6),
          ("unsupportedCommand", 20))
    )


_Ids0CmdCode_Type.__name__ = "Integer32"
_Ids0CmdCode_Object = MibTableColumn
ids0CmdCode = _Ids0CmdCode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 3, 1, 9),
    _Ids0CmdCode_Type()
)
ids0CmdCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ids0CmdCode.setStatus("mandatory")
_Ids0BulkAccessTable_Object = MibTable
ids0BulkAccessTable = _Ids0BulkAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 4)
)
if mibBuilder.loadTexts:
    ids0BulkAccessTable.setStatus("mandatory")
_Ids0BulkAccessEntry_Object = MibTableRow
ids0BulkAccessEntry = _Ids0BulkAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 4, 1)
)
ids0BulkAccessEntry.setIndexNames(
    (0, "IDS0-MIB", "ids0BulkAccessDs1Index"),
)
if mibBuilder.loadTexts:
    ids0BulkAccessEntry.setStatus("mandatory")
_Ids0BulkAccessDs1Index_Type = Integer32
_Ids0BulkAccessDs1Index_Object = MibTableColumn
ids0BulkAccessDs1Index = _Ids0BulkAccessDs1Index_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 4, 1, 1),
    _Ids0BulkAccessDs1Index_Type()
)
ids0BulkAccessDs1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ids0BulkAccessDs1Index.setStatus("mandatory")


class _Ids0BulkAccessStatDs0Mdm_Type(OctetString):
    """Custom type ids0BulkAccessStatDs0Mdm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ids0BulkAccessStatDs0Mdm_Type.__name__ = "OctetString"
_Ids0BulkAccessStatDs0Mdm_Object = MibTableColumn
ids0BulkAccessStatDs0Mdm = _Ids0BulkAccessStatDs0Mdm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 16, 4, 1, 2),
    _Ids0BulkAccessStatDs0Mdm_Type()
)
ids0BulkAccessStatDs0Mdm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ids0BulkAccessStatDs0Mdm.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IDS0-MIB",
    **{"usr": usr,
       "nas": nas,
       "ids0": ids0,
       "ids0CfgTable": ids0CfgTable,
       "ids0CfgEntry": ids0CfgEntry,
       "ids0CfgDs1Index": ids0CfgDs1Index,
       "ids0CfgDs0Index": ids0CfgDs0Index,
       "ids0CfgDs0Id": ids0CfgDs0Id,
       "ids0CfgBlockCallType": ids0CfgBlockCallType,
       "ids0CfgDs0AssignedSlot": ids0CfgDs0AssignedSlot,
       "ids0CfgDs0AssignedChannel": ids0CfgDs0AssignedChannel,
       "ids0CfgDs0SrvcState": ids0CfgDs0SrvcState,
       "ids0CfgNailUpDs0": ids0CfgNailUpDs0,
       "ids0StatTable": ids0StatTable,
       "ids0StatEntry": ids0StatEntry,
       "ids0StatDs1Index": ids0StatDs1Index,
       "ids0StatDs0Index": ids0StatDs0Index,
       "ids0StatDs0": ids0StatDs0,
       "ids0StatDevConnTo": ids0StatDevConnTo,
       "ids0StatSlotConnTo": ids0StatSlotConnTo,
       "ids0StatChanConnTo": ids0StatChanConnTo,
       "ids0StatDs0SrvcState": ids0StatDs0SrvcState,
       "ids0StatCallArrivalTime": ids0StatCallArrivalTime,
       "ids0StatCallConnectTime": ids0StatCallConnectTime,
       "ids0StatCallTerminateTime": ids0StatCallTerminateTime,
       "ids0StatCallType": ids0StatCallType,
       "ids0StatCallBlockState": ids0StatCallBlockState,
       "ids0StatCallDirn": ids0StatCallDirn,
       "ids0CmdTable": ids0CmdTable,
       "ids0CmdEntry": ids0CmdEntry,
       "ids0CmdDs1Index": ids0CmdDs1Index,
       "ids0CmdDs0Index": ids0CmdDs0Index,
       "ids0CmdMgtStationId": ids0CmdMgtStationId,
       "ids0CmdReqId": ids0CmdReqId,
       "ids0CmdFunction": ids0CmdFunction,
       "ids0CmdForce": ids0CmdForce,
       "ids0CmdParam": ids0CmdParam,
       "ids0CmdResult": ids0CmdResult,
       "ids0CmdCode": ids0CmdCode,
       "ids0BulkAccessTable": ids0BulkAccessTable,
       "ids0BulkAccessEntry": ids0BulkAccessEntry,
       "ids0BulkAccessDs1Index": ids0BulkAccessDs1Index,
       "ids0BulkAccessStatDs0Mdm": ids0BulkAccessStatDs0Mdm}
)
