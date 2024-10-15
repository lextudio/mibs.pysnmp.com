# SNMP MIB module (BIANCA-BRICK-PPPOE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-PPPOE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:40 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Pppoe_ObjectIdentity = ObjectIdentity
pppoe = _Pppoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 24)
)
_PppoeCallTable_Object = MibTable
pppoeCallTable = _PppoeCallTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 1)
)
if mibBuilder.loadTexts:
    pppoeCallTable.setStatus("mandatory")
_PppoeCallEntry_Object = MibTableRow
pppoeCallEntry = _PppoeCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 1, 1)
)
pppoeCallEntry.setIndexNames(
    (0, "BIANCA-BRICK-PPPOE-MIB", "pppoeCallId"),
)
if mibBuilder.loadTexts:
    pppoeCallEntry.setStatus("mandatory")
_PppoeCallId_Type = Integer32
_PppoeCallId_Object = MibTableColumn
pppoeCallId = _PppoeCallId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 1, 1, 1),
    _PppoeCallId_Type()
)
pppoeCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeCallId.setStatus("mandatory")


class _PppoeCallDirection_Type(Integer32):
    """Custom type pppoeCallDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_PppoeCallDirection_Type.__name__ = "Integer32"
_PppoeCallDirection_Object = MibTableColumn
pppoeCallDirection = _PppoeCallDirection_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 1, 1, 2),
    _PppoeCallDirection_Type()
)
pppoeCallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeCallDirection.setStatus("mandatory")
_PppoeCallAge_Type = TimeTicks
_PppoeCallAge_Object = MibTableColumn
pppoeCallAge = _PppoeCallAge_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 1, 1, 3),
    _PppoeCallAge_Type()
)
pppoeCallAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeCallAge.setStatus("mandatory")


class _PppoeCallState_Type(Integer32):
    """Custom type pppoeCallState based on Integer32"""
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
        *(("established", 5),
          ("idle", 1),
          ("terminated", 6),
          ("wait-pado", 2),
          ("wait-padr", 3),
          ("wait-pads", 4))
    )


_PppoeCallState_Type.__name__ = "Integer32"
_PppoeCallState_Object = MibTableColumn
pppoeCallState = _PppoeCallState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 1, 1, 4),
    _PppoeCallState_Type()
)
pppoeCallState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeCallState.setStatus("mandatory")
_PppoeCallRemotePhysAddress_Type = PhysAddress
_PppoeCallRemotePhysAddress_Object = MibTableColumn
pppoeCallRemotePhysAddress = _PppoeCallRemotePhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 1, 1, 5),
    _PppoeCallRemotePhysAddress_Type()
)
pppoeCallRemotePhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeCallRemotePhysAddress.setStatus("mandatory")
_PppoeCallLocalPhysAddress_Type = PhysAddress
_PppoeCallLocalPhysAddress_Object = MibTableColumn
pppoeCallLocalPhysAddress = _PppoeCallLocalPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 1, 1, 6),
    _PppoeCallLocalPhysAddress_Type()
)
pppoeCallLocalPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeCallLocalPhysAddress.setStatus("mandatory")
_PppoeCallAcName_Type = DisplayString
_PppoeCallAcName_Object = MibTableColumn
pppoeCallAcName = _PppoeCallAcName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 1, 1, 7),
    _PppoeCallAcName_Type()
)
pppoeCallAcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeCallAcName.setStatus("mandatory")
_PppoeCallService_Type = DisplayString
_PppoeCallService_Object = MibTableColumn
pppoeCallService = _PppoeCallService_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 1, 1, 8),
    _PppoeCallService_Type()
)
pppoeCallService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeCallService.setStatus("mandatory")
_PppoeCallReceivedPackets_Type = Counter32
_PppoeCallReceivedPackets_Object = MibTableColumn
pppoeCallReceivedPackets = _PppoeCallReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 1, 1, 9),
    _PppoeCallReceivedPackets_Type()
)
pppoeCallReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeCallReceivedPackets.setStatus("mandatory")
_PppoeCallReceivedOctets_Type = Counter32
_PppoeCallReceivedOctets_Object = MibTableColumn
pppoeCallReceivedOctets = _PppoeCallReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 1, 1, 10),
    _PppoeCallReceivedOctets_Type()
)
pppoeCallReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeCallReceivedOctets.setStatus("mandatory")
_PppoeCallReceivedErrors_Type = Counter32
_PppoeCallReceivedErrors_Object = MibTableColumn
pppoeCallReceivedErrors = _PppoeCallReceivedErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 1, 1, 11),
    _PppoeCallReceivedErrors_Type()
)
pppoeCallReceivedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeCallReceivedErrors.setStatus("mandatory")
_PppoeCallTransmitPackets_Type = Counter32
_PppoeCallTransmitPackets_Object = MibTableColumn
pppoeCallTransmitPackets = _PppoeCallTransmitPackets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 1, 1, 12),
    _PppoeCallTransmitPackets_Type()
)
pppoeCallTransmitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeCallTransmitPackets.setStatus("mandatory")
_PppoeCallTransmitOctets_Type = Counter32
_PppoeCallTransmitOctets_Object = MibTableColumn
pppoeCallTransmitOctets = _PppoeCallTransmitOctets_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 1, 1, 13),
    _PppoeCallTransmitOctets_Type()
)
pppoeCallTransmitOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeCallTransmitOctets.setStatus("mandatory")
_PppoeCallTransmitErrors_Type = Counter32
_PppoeCallTransmitErrors_Object = MibTableColumn
pppoeCallTransmitErrors = _PppoeCallTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 1, 1, 14),
    _PppoeCallTransmitErrors_Type()
)
pppoeCallTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeCallTransmitErrors.setStatus("mandatory")
_PppoeCallInfo_Type = DisplayString
_PppoeCallInfo_Object = MibTableColumn
pppoeCallInfo = _PppoeCallInfo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 1, 1, 15),
    _PppoeCallInfo_Type()
)
pppoeCallInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeCallInfo.setStatus("mandatory")
_PppoeCreditsTable_Object = MibTable
pppoeCreditsTable = _PppoeCreditsTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 2)
)
if mibBuilder.loadTexts:
    pppoeCreditsTable.setStatus("mandatory")
_PppoeCreditsEntry_Object = MibTableRow
pppoeCreditsEntry = _PppoeCreditsEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 2, 1)
)
pppoeCreditsEntry.setIndexNames(
    (0, "BIANCA-BRICK-PPPOE-MIB", "pppoeCreditsService"),
)
if mibBuilder.loadTexts:
    pppoeCreditsEntry.setStatus("mandatory")
_PppoeCreditsService_Type = DisplayString
_PppoeCreditsService_Object = MibTableColumn
pppoeCreditsService = _PppoeCreditsService_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 2, 1, 1),
    _PppoeCreditsService_Type()
)
pppoeCreditsService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeCreditsService.setStatus("mandatory")


class _PppoeCreditsSurveillance_Type(Integer32):
    """Custom type pppoeCreditsSurveillance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("off", 1),
          ("on", 2))
    )


_PppoeCreditsSurveillance_Type.__name__ = "Integer32"
_PppoeCreditsSurveillance_Object = MibTableColumn
pppoeCreditsSurveillance = _PppoeCreditsSurveillance_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 2, 1, 2),
    _PppoeCreditsSurveillance_Type()
)
pppoeCreditsSurveillance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeCreditsSurveillance.setStatus("mandatory")
_PppoeCreditsMeasuretime_Type = Integer32
_PppoeCreditsMeasuretime_Object = MibTableColumn
pppoeCreditsMeasuretime = _PppoeCreditsMeasuretime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 2, 1, 3),
    _PppoeCreditsMeasuretime_Type()
)
pppoeCreditsMeasuretime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeCreditsMeasuretime.setStatus("mandatory")
_PppoeCreditsMaxInCon_Type = Integer32
_PppoeCreditsMaxInCon_Object = MibTableColumn
pppoeCreditsMaxInCon = _PppoeCreditsMaxInCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 2, 1, 4),
    _PppoeCreditsMaxInCon_Type()
)
pppoeCreditsMaxInCon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeCreditsMaxInCon.setStatus("mandatory")
_PppoeCreditsMaxOutCon_Type = Integer32
_PppoeCreditsMaxOutCon_Object = MibTableColumn
pppoeCreditsMaxOutCon = _PppoeCreditsMaxOutCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 2, 1, 5),
    _PppoeCreditsMaxOutCon_Type()
)
pppoeCreditsMaxOutCon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeCreditsMaxOutCon.setStatus("mandatory")
_PppoeCreditsMaxInDuration_Type = Integer32
_PppoeCreditsMaxInDuration_Object = MibTableColumn
pppoeCreditsMaxInDuration = _PppoeCreditsMaxInDuration_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 2, 1, 6),
    _PppoeCreditsMaxInDuration_Type()
)
pppoeCreditsMaxInDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeCreditsMaxInDuration.setStatus("mandatory")
_PppoeCreditsMaxOutDuration_Type = Integer32
_PppoeCreditsMaxOutDuration_Object = MibTableColumn
pppoeCreditsMaxOutDuration = _PppoeCreditsMaxOutDuration_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 2, 1, 7),
    _PppoeCreditsMaxOutDuration_Type()
)
pppoeCreditsMaxOutDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeCreditsMaxOutDuration.setStatus("mandatory")
_PppoeCreditsTimeleft_Type = Integer32
_PppoeCreditsTimeleft_Object = MibTableColumn
pppoeCreditsTimeleft = _PppoeCreditsTimeleft_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 2, 1, 8),
    _PppoeCreditsTimeleft_Type()
)
pppoeCreditsTimeleft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeCreditsTimeleft.setStatus("mandatory")
_PppoeCreditsCurrentInCon_Type = Integer32
_PppoeCreditsCurrentInCon_Object = MibTableColumn
pppoeCreditsCurrentInCon = _PppoeCreditsCurrentInCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 2, 1, 9),
    _PppoeCreditsCurrentInCon_Type()
)
pppoeCreditsCurrentInCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeCreditsCurrentInCon.setStatus("mandatory")
_PppoeCreditsCurrentOutCon_Type = Integer32
_PppoeCreditsCurrentOutCon_Object = MibTableColumn
pppoeCreditsCurrentOutCon = _PppoeCreditsCurrentOutCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 2, 1, 10),
    _PppoeCreditsCurrentOutCon_Type()
)
pppoeCreditsCurrentOutCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeCreditsCurrentOutCon.setStatus("mandatory")
_PppoeCreditsTotalInCon_Type = Integer32
_PppoeCreditsTotalInCon_Object = MibTableColumn
pppoeCreditsTotalInCon = _PppoeCreditsTotalInCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 2, 1, 11),
    _PppoeCreditsTotalInCon_Type()
)
pppoeCreditsTotalInCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeCreditsTotalInCon.setStatus("mandatory")
_PppoeCreditsTotalOutCon_Type = Integer32
_PppoeCreditsTotalOutCon_Object = MibTableColumn
pppoeCreditsTotalOutCon = _PppoeCreditsTotalOutCon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 2, 1, 12),
    _PppoeCreditsTotalOutCon_Type()
)
pppoeCreditsTotalOutCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeCreditsTotalOutCon.setStatus("mandatory")
_PppoeCreditsTotalInDuration_Type = Integer32
_PppoeCreditsTotalInDuration_Object = MibTableColumn
pppoeCreditsTotalInDuration = _PppoeCreditsTotalInDuration_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 2, 1, 13),
    _PppoeCreditsTotalInDuration_Type()
)
pppoeCreditsTotalInDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeCreditsTotalInDuration.setStatus("mandatory")
_PppoeCreditsTotalOutDuration_Type = Integer32
_PppoeCreditsTotalOutDuration_Object = MibTableColumn
pppoeCreditsTotalOutDuration = _PppoeCreditsTotalOutDuration_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 2, 1, 14),
    _PppoeCreditsTotalOutDuration_Type()
)
pppoeCreditsTotalOutDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeCreditsTotalOutDuration.setStatus("mandatory")


class _PppoeCreditsCurrentAccount_Type(Integer32):
    """Custom type pppoeCreditsCurrentAccount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PppoeCreditsCurrentAccount_Type.__name__ = "Integer32"
_PppoeCreditsCurrentAccount_Object = MibTableColumn
pppoeCreditsCurrentAccount = _PppoeCreditsCurrentAccount_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 2, 1, 15),
    _PppoeCreditsCurrentAccount_Type()
)
pppoeCreditsCurrentAccount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeCreditsCurrentAccount.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-PPPOE-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "pppoe": pppoe,
       "pppoeCallTable": pppoeCallTable,
       "pppoeCallEntry": pppoeCallEntry,
       "pppoeCallId": pppoeCallId,
       "pppoeCallDirection": pppoeCallDirection,
       "pppoeCallAge": pppoeCallAge,
       "pppoeCallState": pppoeCallState,
       "pppoeCallRemotePhysAddress": pppoeCallRemotePhysAddress,
       "pppoeCallLocalPhysAddress": pppoeCallLocalPhysAddress,
       "pppoeCallAcName": pppoeCallAcName,
       "pppoeCallService": pppoeCallService,
       "pppoeCallReceivedPackets": pppoeCallReceivedPackets,
       "pppoeCallReceivedOctets": pppoeCallReceivedOctets,
       "pppoeCallReceivedErrors": pppoeCallReceivedErrors,
       "pppoeCallTransmitPackets": pppoeCallTransmitPackets,
       "pppoeCallTransmitOctets": pppoeCallTransmitOctets,
       "pppoeCallTransmitErrors": pppoeCallTransmitErrors,
       "pppoeCallInfo": pppoeCallInfo,
       "pppoeCreditsTable": pppoeCreditsTable,
       "pppoeCreditsEntry": pppoeCreditsEntry,
       "pppoeCreditsService": pppoeCreditsService,
       "pppoeCreditsSurveillance": pppoeCreditsSurveillance,
       "pppoeCreditsMeasuretime": pppoeCreditsMeasuretime,
       "pppoeCreditsMaxInCon": pppoeCreditsMaxInCon,
       "pppoeCreditsMaxOutCon": pppoeCreditsMaxOutCon,
       "pppoeCreditsMaxInDuration": pppoeCreditsMaxInDuration,
       "pppoeCreditsMaxOutDuration": pppoeCreditsMaxOutDuration,
       "pppoeCreditsTimeleft": pppoeCreditsTimeleft,
       "pppoeCreditsCurrentInCon": pppoeCreditsCurrentInCon,
       "pppoeCreditsCurrentOutCon": pppoeCreditsCurrentOutCon,
       "pppoeCreditsTotalInCon": pppoeCreditsTotalInCon,
       "pppoeCreditsTotalOutCon": pppoeCreditsTotalOutCon,
       "pppoeCreditsTotalInDuration": pppoeCreditsTotalInDuration,
       "pppoeCreditsTotalOutDuration": pppoeCreditsTotalOutDuration,
       "pppoeCreditsCurrentAccount": pppoeCreditsCurrentAccount}
)
