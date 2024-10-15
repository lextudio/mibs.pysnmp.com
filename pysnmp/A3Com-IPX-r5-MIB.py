# SNMP MIB module (A3COM-IPX-R5-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-IPX-R5-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:35 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "RFC1286-MIB",
    "MacAddress")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class SMDSAddress(OctetString):
    """Custom type SMDSAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )





class IPXNET(OctetString):
    """Custom type IPXNET based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_BrouterMIB_ObjectIdentity = ObjectIdentity
brouterMIB = _BrouterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2)
)
_A3ComIPX_ObjectIdentity = ObjectIdentity
a3ComIPX = _A3ComIPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 7)
)
_A3ipxGeneral_ObjectIdentity = ObjectIdentity
a3ipxGeneral = _A3ipxGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 1)
)


class _A3ipxRouteControl_Type(Integer32):
    """Custom type a3ipxRouteControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3ipxRouteControl_Type.__name__ = "Integer32"
_A3ipxRouteControl_Object = MibScalar
a3ipxRouteControl = _A3ipxRouteControl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 1),
    _A3ipxRouteControl_Type()
)
a3ipxRouteControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxRouteControl.setStatus("deprecated")


class _A3ipxWanBcastControl_Type(Integer32):
    """Custom type a3ipxWanBcastControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3ipxWanBcastControl_Type.__name__ = "Integer32"
_A3ipxWanBcastControl_Object = MibScalar
a3ipxWanBcastControl = _A3ipxWanBcastControl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 2),
    _A3ipxWanBcastControl_Type()
)
a3ipxWanBcastControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxWanBcastControl.setStatus("deprecated")


class _A3ipxUpdateTime_Type(Integer32):
    """Custom type a3ipxUpdateTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_A3ipxUpdateTime_Type.__name__ = "Integer32"
_A3ipxUpdateTime_Object = MibScalar
a3ipxUpdateTime = _A3ipxUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 3),
    _A3ipxUpdateTime_Type()
)
a3ipxUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxUpdateTime.setStatus("deprecated")


class _A3ipxFlushRipSap_Type(Integer32):
    """Custom type a3ipxFlushRipSap based on Integer32"""
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
        *(("both", 4),
          ("other", 1),
          ("rip", 2),
          ("sap", 3))
    )


_A3ipxFlushRipSap_Type.__name__ = "Integer32"
_A3ipxFlushRipSap_Object = MibScalar
a3ipxFlushRipSap = _A3ipxFlushRipSap_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 4),
    _A3ipxFlushRipSap_Type()
)
a3ipxFlushRipSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxFlushRipSap.setStatus("mandatory")
_A3ipxInternalNet_Type = IPXNET
_A3ipxInternalNet_Object = MibScalar
a3ipxInternalNet = _A3ipxInternalNet_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 5),
    _A3ipxInternalNet_Type()
)
a3ipxInternalNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxInternalNet.setStatus("mandatory")


class _A3ipxRouterName_Type(DisplayString):
    """Custom type a3ipxRouterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_A3ipxRouterName_Type.__name__ = "DisplayString"
_A3ipxRouterName_Object = MibScalar
a3ipxRouterName = _A3ipxRouterName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 6),
    _A3ipxRouterName_Type()
)
a3ipxRouterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxRouterName.setStatus("mandatory")
_A3ipxControl_ObjectIdentity = ObjectIdentity
a3ipxControl = _A3ipxControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 7)
)
_A3ipxControlTable_Object = MibTable
a3ipxControlTable = _A3ipxControlTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 7, 1)
)
if mibBuilder.loadTexts:
    a3ipxControlTable.setStatus("mandatory")
_A3ipxControlEntry_Object = MibTableRow
a3ipxControlEntry = _A3ipxControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 7, 1, 1)
)
a3ipxControlEntry.setIndexNames(
    (0, "A3COM-IPX-R5-MIB", "a3ipxControlPort"),
)
if mibBuilder.loadTexts:
    a3ipxControlEntry.setStatus("mandatory")
_A3ipxControlPort_Type = Integer32
_A3ipxControlPort_Object = MibTableColumn
a3ipxControlPort = _A3ipxControlPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 7, 1, 1, 1),
    _A3ipxControlPort_Type()
)
a3ipxControlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxControlPort.setStatus("mandatory")


class _A3ipxControlRoute_Type(Integer32):
    """Custom type a3ipxControlRoute based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3ipxControlRoute_Type.__name__ = "Integer32"
_A3ipxControlRoute_Object = MibTableColumn
a3ipxControlRoute = _A3ipxControlRoute_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 7, 1, 1, 2),
    _A3ipxControlRoute_Type()
)
a3ipxControlRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxControlRoute.setStatus("mandatory")


class _A3ipxControlWanBcast_Type(Integer32):
    """Custom type a3ipxControlWanBcast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3ipxControlWanBcast_Type.__name__ = "Integer32"
_A3ipxControlWanBcast_Object = MibTableColumn
a3ipxControlWanBcast = _A3ipxControlWanBcast_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 7, 1, 1, 3),
    _A3ipxControlWanBcast_Type()
)
a3ipxControlWanBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxControlWanBcast.setStatus("mandatory")


class _A3ipxControlChecksum_Type(Integer32):
    """Custom type a3ipxControlChecksum based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3ipxControlChecksum_Type.__name__ = "Integer32"
_A3ipxControlChecksum_Object = MibTableColumn
a3ipxControlChecksum = _A3ipxControlChecksum_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 7, 1, 1, 4),
    _A3ipxControlChecksum_Type()
)
a3ipxControlChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxControlChecksum.setStatus("mandatory")


class _A3ipxControlWanOpt_Type(Integer32):
    """Custom type a3ipxControlWanOpt based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noWan", 2),
          ("wan", 1))
    )


_A3ipxControlWanOpt_Type.__name__ = "Integer32"
_A3ipxControlWanOpt_Object = MibTableColumn
a3ipxControlWanOpt = _A3ipxControlWanOpt_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 7, 1, 1, 5),
    _A3ipxControlWanOpt_Type()
)
a3ipxControlWanOpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxControlWanOpt.setStatus("mandatory")


class _A3ipxRipHoldTimeFactor_Type(Integer32):
    """Custom type a3ipxRipHoldTimeFactor based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_A3ipxRipHoldTimeFactor_Type.__name__ = "Integer32"
_A3ipxRipHoldTimeFactor_Object = MibScalar
a3ipxRipHoldTimeFactor = _A3ipxRipHoldTimeFactor_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 8),
    _A3ipxRipHoldTimeFactor_Type()
)
a3ipxRipHoldTimeFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxRipHoldTimeFactor.setStatus("mandatory")


class _A3ipxSapHoldTimeFactor_Type(Integer32):
    """Custom type a3ipxSapHoldTimeFactor based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_A3ipxSapHoldTimeFactor_Type.__name__ = "Integer32"
_A3ipxSapHoldTimeFactor_Object = MibScalar
a3ipxSapHoldTimeFactor = _A3ipxSapHoldTimeFactor_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 1, 9),
    _A3ipxSapHoldTimeFactor_Type()
)
a3ipxSapHoldTimeFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxSapHoldTimeFactor.setStatus("mandatory")
_A3ipxRipControlTable_Object = MibTable
a3ipxRipControlTable = _A3ipxRipControlTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 2)
)
if mibBuilder.loadTexts:
    a3ipxRipControlTable.setStatus("mandatory")
_A3ipxRipControlEntry_Object = MibTableRow
a3ipxRipControlEntry = _A3ipxRipControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1)
)
a3ipxRipControlEntry.setIndexNames(
    (0, "A3COM-IPX-R5-MIB", "a3ipxRipControlPort"),
)
if mibBuilder.loadTexts:
    a3ipxRipControlEntry.setStatus("mandatory")
_A3ipxRipControlPort_Type = Integer32
_A3ipxRipControlPort_Object = MibTableColumn
a3ipxRipControlPort = _A3ipxRipControlPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 1),
    _A3ipxRipControlPort_Type()
)
a3ipxRipControlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxRipControlPort.setStatus("mandatory")


class _A3ipxRipControlSwitch_Type(Integer32):
    """Custom type a3ipxRipControlSwitch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3ipxRipControlSwitch_Type.__name__ = "Integer32"
_A3ipxRipControlSwitch_Object = MibTableColumn
a3ipxRipControlSwitch = _A3ipxRipControlSwitch_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 2),
    _A3ipxRipControlSwitch_Type()
)
a3ipxRipControlSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxRipControlSwitch.setStatus("deprecated")


class _A3ipxRipControlTrigger_Type(Integer32):
    """Custom type a3ipxRipControlTrigger based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3ipxRipControlTrigger_Type.__name__ = "Integer32"
_A3ipxRipControlTrigger_Object = MibTableColumn
a3ipxRipControlTrigger = _A3ipxRipControlTrigger_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 3),
    _A3ipxRipControlTrigger_Type()
)
a3ipxRipControlTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxRipControlTrigger.setStatus("mandatory")


class _A3ipxRipControlPoison_Type(Integer32):
    """Custom type a3ipxRipControlPoison based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3ipxRipControlPoison_Type.__name__ = "Integer32"
_A3ipxRipControlPoison_Object = MibTableColumn
a3ipxRipControlPoison = _A3ipxRipControlPoison_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 4),
    _A3ipxRipControlPoison_Type()
)
a3ipxRipControlPoison.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxRipControlPoison.setStatus("mandatory")


class _A3ipxRipControlMapOpt_Type(Integer32):
    """Custom type a3ipxRipControlMapOpt based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("newNbrMap", 2),
          ("oldNbrMap", 1))
    )


_A3ipxRipControlMapOpt_Type.__name__ = "Integer32"
_A3ipxRipControlMapOpt_Object = MibTableColumn
a3ipxRipControlMapOpt = _A3ipxRipControlMapOpt_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 5),
    _A3ipxRipControlMapOpt_Type()
)
a3ipxRipControlMapOpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxRipControlMapOpt.setStatus("mandatory")


class _A3ipxRipControlWanOpt_Type(Integer32):
    """Custom type a3ipxRipControlWanOpt based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noWan", 2),
          ("wan", 1))
    )


_A3ipxRipControlWanOpt_Type.__name__ = "Integer32"
_A3ipxRipControlWanOpt_Object = MibTableColumn
a3ipxRipControlWanOpt = _A3ipxRipControlWanOpt_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 6),
    _A3ipxRipControlWanOpt_Type()
)
a3ipxRipControlWanOpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxRipControlWanOpt.setStatus("deprecated")


class _A3ipxRipControlPerRip_Type(Integer32):
    """Custom type a3ipxRipControlPerRip based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonPeriodicRip", 2),
          ("periodicRip", 1))
    )


_A3ipxRipControlPerRip_Type.__name__ = "Integer32"
_A3ipxRipControlPerRip_Object = MibTableColumn
a3ipxRipControlPerRip = _A3ipxRipControlPerRip_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 7),
    _A3ipxRipControlPerRip_Type()
)
a3ipxRipControlPerRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxRipControlPerRip.setStatus("mandatory")


class _A3ipxRipControlPerSap_Type(Integer32):
    """Custom type a3ipxRipControlPerSap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonPeriodicSap", 2),
          ("periodicSap", 1))
    )


_A3ipxRipControlPerSap_Type.__name__ = "Integer32"
_A3ipxRipControlPerSap_Object = MibTableColumn
a3ipxRipControlPerSap = _A3ipxRipControlPerSap_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 8),
    _A3ipxRipControlPerSap_Type()
)
a3ipxRipControlPerSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxRipControlPerSap.setStatus("mandatory")


class _A3ipxRipControlTalk_Type(Integer32):
    """Custom type a3ipxRipControlTalk based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3ipxRipControlTalk_Type.__name__ = "Integer32"
_A3ipxRipControlTalk_Object = MibTableColumn
a3ipxRipControlTalk = _A3ipxRipControlTalk_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 9),
    _A3ipxRipControlTalk_Type()
)
a3ipxRipControlTalk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxRipControlTalk.setStatus("deprecated")


class _A3ipxRipControlListen_Type(Integer32):
    """Custom type a3ipxRipControlListen based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3ipxRipControlListen_Type.__name__ = "Integer32"
_A3ipxRipControlListen_Object = MibTableColumn
a3ipxRipControlListen = _A3ipxRipControlListen_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 10),
    _A3ipxRipControlListen_Type()
)
a3ipxRipControlListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxRipControlListen.setStatus("deprecated")


class _A3ipxSapControlTalk_Type(Integer32):
    """Custom type a3ipxSapControlTalk based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3ipxSapControlTalk_Type.__name__ = "Integer32"
_A3ipxSapControlTalk_Object = MibTableColumn
a3ipxSapControlTalk = _A3ipxSapControlTalk_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 11),
    _A3ipxSapControlTalk_Type()
)
a3ipxSapControlTalk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxSapControlTalk.setStatus("deprecated")


class _A3ipxSapControlListen_Type(Integer32):
    """Custom type a3ipxSapControlListen based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3ipxSapControlListen_Type.__name__ = "Integer32"
_A3ipxSapControlListen_Object = MibTableColumn
a3ipxSapControlListen = _A3ipxSapControlListen_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 12),
    _A3ipxSapControlListen_Type()
)
a3ipxSapControlListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxSapControlListen.setStatus("deprecated")


class _A3ipxRipCtl_Type(Integer32):
    """Custom type a3ipxRipCtl based on Integer32"""
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
        *(("auto", 5),
          ("noTalkListen", 3),
          ("noTalkNoListen", 4),
          ("talkListen", 1),
          ("talkNoListen", 2))
    )


_A3ipxRipCtl_Type.__name__ = "Integer32"
_A3ipxRipCtl_Object = MibTableColumn
a3ipxRipCtl = _A3ipxRipCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 13),
    _A3ipxRipCtl_Type()
)
a3ipxRipCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxRipCtl.setStatus("mandatory")


class _A3ipxSapCtl_Type(Integer32):
    """Custom type a3ipxSapCtl based on Integer32"""
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
        *(("auto", 5),
          ("noTalkListen", 3),
          ("noTalkNoListen", 4),
          ("talkListen", 1),
          ("talkNoListen", 2))
    )


_A3ipxSapCtl_Type.__name__ = "Integer32"
_A3ipxSapCtl_Object = MibTableColumn
a3ipxSapCtl = _A3ipxSapCtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 2, 1, 14),
    _A3ipxSapCtl_Type()
)
a3ipxSapCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxSapCtl.setStatus("mandatory")
_A3ipxWaAddrTable_Object = MibTable
a3ipxWaAddrTable = _A3ipxWaAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 3)
)
if mibBuilder.loadTexts:
    a3ipxWaAddrTable.setStatus("mandatory")
_A3ipxWaAddrEntry_Object = MibTableRow
a3ipxWaAddrEntry = _A3ipxWaAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 3, 1)
)
a3ipxWaAddrEntry.setIndexNames(
    (0, "A3COM-IPX-R5-MIB", "a3ipxWaAddrEthAddress"),
)
if mibBuilder.loadTexts:
    a3ipxWaAddrEntry.setStatus("mandatory")
_A3ipxWaAddrEthAddress_Type = MacAddress
_A3ipxWaAddrEthAddress_Object = MibTableColumn
a3ipxWaAddrEthAddress = _A3ipxWaAddrEthAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 3, 1, 1),
    _A3ipxWaAddrEthAddress_Type()
)
a3ipxWaAddrEthAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxWaAddrEthAddress.setStatus("mandatory")
_A3ipxWaAddrPort_Type = Integer32
_A3ipxWaAddrPort_Object = MibTableColumn
a3ipxWaAddrPort = _A3ipxWaAddrPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 3, 1, 2),
    _A3ipxWaAddrPort_Type()
)
a3ipxWaAddrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxWaAddrPort.setStatus("mandatory")


class _A3ipxWaAddrDLType_Type(Integer32):
    """Custom type a3ipxWaAddrDLType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("frameRelay", 2),
          ("smds", 3),
          ("x25", 1))
    )


_A3ipxWaAddrDLType_Type.__name__ = "Integer32"
_A3ipxWaAddrDLType_Object = MibTableColumn
a3ipxWaAddrDLType = _A3ipxWaAddrDLType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 3, 1, 3),
    _A3ipxWaAddrDLType_Type()
)
a3ipxWaAddrDLType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxWaAddrDLType.setStatus("mandatory")
_A3ipxWaAddrDLAddress_Type = PhysAddress
_A3ipxWaAddrDLAddress_Object = MibTableColumn
a3ipxWaAddrDLAddress = _A3ipxWaAddrDLAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 3, 1, 4),
    _A3ipxWaAddrDLAddress_Type()
)
a3ipxWaAddrDLAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxWaAddrDLAddress.setStatus("mandatory")
_A3ipxWaAddrStatus_Type = RowStatus
_A3ipxWaAddrStatus_Object = MibTableColumn
a3ipxWaAddrStatus = _A3ipxWaAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 3, 1, 5),
    _A3ipxWaAddrStatus_Type()
)
a3ipxWaAddrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxWaAddrStatus.setStatus("mandatory")
_A3ipxAttachedNetTable_Object = MibTable
a3ipxAttachedNetTable = _A3ipxAttachedNetTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 4)
)
if mibBuilder.loadTexts:
    a3ipxAttachedNetTable.setStatus("mandatory")
_A3ipxAttachedNetEntry_Object = MibTableRow
a3ipxAttachedNetEntry = _A3ipxAttachedNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 4, 1)
)
a3ipxAttachedNetEntry.setIndexNames(
    (0, "A3COM-IPX-R5-MIB", "a3ipxAttachedNetNumber"),
)
if mibBuilder.loadTexts:
    a3ipxAttachedNetEntry.setStatus("mandatory")
_A3ipxAttachedNetNumber_Type = IPXNET
_A3ipxAttachedNetNumber_Object = MibTableColumn
a3ipxAttachedNetNumber = _A3ipxAttachedNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 4, 1, 1),
    _A3ipxAttachedNetNumber_Type()
)
a3ipxAttachedNetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxAttachedNetNumber.setStatus("mandatory")
_A3ipxAttachedNetPort_Type = Integer32
_A3ipxAttachedNetPort_Object = MibTableColumn
a3ipxAttachedNetPort = _A3ipxAttachedNetPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 4, 1, 2),
    _A3ipxAttachedNetPort_Type()
)
a3ipxAttachedNetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxAttachedNetPort.setStatus("mandatory")


class _A3ipxAttachedNetFormat_Type(Integer32):
    """Custom type a3ipxAttachedNetFormat based on Integer32"""
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
        *(("ethernet", 1),
          ("fr", 7),
          ("ieee", 2),
          ("llc", 3),
          ("ppp", 5),
          ("smds", 8),
          ("snap", 4),
          ("x25", 6))
    )


_A3ipxAttachedNetFormat_Type.__name__ = "Integer32"
_A3ipxAttachedNetFormat_Object = MibTableColumn
a3ipxAttachedNetFormat = _A3ipxAttachedNetFormat_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 4, 1, 3),
    _A3ipxAttachedNetFormat_Type()
)
a3ipxAttachedNetFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxAttachedNetFormat.setStatus("mandatory")


class _A3ipxAttachedNetType_Type(Integer32):
    """Custom type a3ipxAttachedNetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_A3ipxAttachedNetType_Type.__name__ = "Integer32"
_A3ipxAttachedNetType_Object = MibTableColumn
a3ipxAttachedNetType = _A3ipxAttachedNetType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 4, 1, 4),
    _A3ipxAttachedNetType_Type()
)
a3ipxAttachedNetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxAttachedNetType.setStatus("mandatory")


class _A3ipxAttachedNetOperState_Type(Integer32):
    """Custom type a3ipxAttachedNetOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_A3ipxAttachedNetOperState_Type.__name__ = "Integer32"
_A3ipxAttachedNetOperState_Object = MibTableColumn
a3ipxAttachedNetOperState = _A3ipxAttachedNetOperState_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 4, 1, 5),
    _A3ipxAttachedNetOperState_Type()
)
a3ipxAttachedNetOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxAttachedNetOperState.setStatus("mandatory")
_A3ipxAttachedNetStatus_Type = RowStatus
_A3ipxAttachedNetStatus_Object = MibTableColumn
a3ipxAttachedNetStatus = _A3ipxAttachedNetStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 4, 1, 6),
    _A3ipxAttachedNetStatus_Type()
)
a3ipxAttachedNetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxAttachedNetStatus.setStatus("mandatory")
_A3ipxRouteTable_Object = MibTable
a3ipxRouteTable = _A3ipxRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 5)
)
if mibBuilder.loadTexts:
    a3ipxRouteTable.setStatus("mandatory")
_A3ipxRouteEntry_Object = MibTableRow
a3ipxRouteEntry = _A3ipxRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 5, 1)
)
a3ipxRouteEntry.setIndexNames(
    (0, "A3COM-IPX-R5-MIB", "a3ipxRouteDestNet"),
    (0, "A3COM-IPX-R5-MIB", "a3ipxRouteType"),
)
if mibBuilder.loadTexts:
    a3ipxRouteEntry.setStatus("mandatory")
_A3ipxRouteDestNet_Type = IPXNET
_A3ipxRouteDestNet_Object = MibTableColumn
a3ipxRouteDestNet = _A3ipxRouteDestNet_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 5, 1, 1),
    _A3ipxRouteDestNet_Type()
)
a3ipxRouteDestNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxRouteDestNet.setStatus("mandatory")
_A3ipxRouteAttachedNet_Type = IPXNET
_A3ipxRouteAttachedNet_Object = MibTableColumn
a3ipxRouteAttachedNet = _A3ipxRouteAttachedNet_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 5, 1, 2),
    _A3ipxRouteAttachedNet_Type()
)
a3ipxRouteAttachedNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxRouteAttachedNet.setStatus("mandatory")


class _A3ipxRouteDLType_Type(Integer32):
    """Custom type a3ipxRouteDLType based on Integer32"""
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
        *(("ethernet", 1),
          ("frameRelay", 3),
          ("smds", 4),
          ("x25", 2))
    )


_A3ipxRouteDLType_Type.__name__ = "Integer32"
_A3ipxRouteDLType_Object = MibTableColumn
a3ipxRouteDLType = _A3ipxRouteDLType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 5, 1, 3),
    _A3ipxRouteDLType_Type()
)
a3ipxRouteDLType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxRouteDLType.setStatus("mandatory")
_A3ipxRouteDLAddress_Type = PhysAddress
_A3ipxRouteDLAddress_Object = MibTableColumn
a3ipxRouteDLAddress = _A3ipxRouteDLAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 5, 1, 4),
    _A3ipxRouteDLAddress_Type()
)
a3ipxRouteDLAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxRouteDLAddress.setStatus("mandatory")


class _A3ipxRouteHops_Type(Integer32):
    """Custom type a3ipxRouteHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_A3ipxRouteHops_Type.__name__ = "Integer32"
_A3ipxRouteHops_Object = MibTableColumn
a3ipxRouteHops = _A3ipxRouteHops_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 5, 1, 5),
    _A3ipxRouteHops_Type()
)
a3ipxRouteHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxRouteHops.setStatus("mandatory")


class _A3ipxRouteType_Type(Integer32):
    """Custom type a3ipxRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_A3ipxRouteType_Type.__name__ = "Integer32"
_A3ipxRouteType_Object = MibTableColumn
a3ipxRouteType = _A3ipxRouteType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 5, 1, 6),
    _A3ipxRouteType_Type()
)
a3ipxRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxRouteType.setStatus("mandatory")


class _A3ipxRouteProto_Type(Integer32):
    """Custom type a3ipxRouteProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("rip", 3),
          ("static", 2))
    )


_A3ipxRouteProto_Type.__name__ = "Integer32"
_A3ipxRouteProto_Object = MibTableColumn
a3ipxRouteProto = _A3ipxRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 5, 1, 7),
    _A3ipxRouteProto_Type()
)
a3ipxRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxRouteProto.setStatus("mandatory")
_A3ipxRouteDelay_Type = Integer32
_A3ipxRouteDelay_Object = MibTableColumn
a3ipxRouteDelay = _A3ipxRouteDelay_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 5, 1, 8),
    _A3ipxRouteDelay_Type()
)
a3ipxRouteDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxRouteDelay.setStatus("mandatory")
_A3ipxRouteStatus_Type = RowStatus
_A3ipxRouteStatus_Object = MibTableColumn
a3ipxRouteStatus = _A3ipxRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 5, 1, 9),
    _A3ipxRouteStatus_Type()
)
a3ipxRouteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxRouteStatus.setStatus("mandatory")
_A3ipxServerTable_Object = MibTable
a3ipxServerTable = _A3ipxServerTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 6)
)
if mibBuilder.loadTexts:
    a3ipxServerTable.setStatus("mandatory")
_A3ipxServerEntry_Object = MibTableRow
a3ipxServerEntry = _A3ipxServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 6, 1)
)
a3ipxServerEntry.setIndexNames(
    (0, "A3COM-IPX-R5-MIB", "a3ipxServerName"),
    (0, "A3COM-IPX-R5-MIB", "a3ipxServerType"),
)
if mibBuilder.loadTexts:
    a3ipxServerEntry.setStatus("mandatory")


class _A3ipxServerName_Type(DisplayString):
    """Custom type a3ipxServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_A3ipxServerName_Type.__name__ = "DisplayString"
_A3ipxServerName_Object = MibTableColumn
a3ipxServerName = _A3ipxServerName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 6, 1, 1),
    _A3ipxServerName_Type()
)
a3ipxServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxServerName.setStatus("mandatory")


class _A3ipxServerType_Type(OctetString):
    """Custom type a3ipxServerType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_A3ipxServerType_Type.__name__ = "OctetString"
_A3ipxServerType_Object = MibTableColumn
a3ipxServerType = _A3ipxServerType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 6, 1, 2),
    _A3ipxServerType_Type()
)
a3ipxServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxServerType.setStatus("mandatory")
_A3ipxServerNet_Type = IPXNET
_A3ipxServerNet_Object = MibTableColumn
a3ipxServerNet = _A3ipxServerNet_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 6, 1, 3),
    _A3ipxServerNet_Type()
)
a3ipxServerNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxServerNet.setStatus("mandatory")
_A3ipxServerDLAddress_Type = MacAddress
_A3ipxServerDLAddress_Object = MibTableColumn
a3ipxServerDLAddress = _A3ipxServerDLAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 6, 1, 4),
    _A3ipxServerDLAddress_Type()
)
a3ipxServerDLAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxServerDLAddress.setStatus("mandatory")


class _A3ipxServerSocket_Type(OctetString):
    """Custom type a3ipxServerSocket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_A3ipxServerSocket_Type.__name__ = "OctetString"
_A3ipxServerSocket_Object = MibTableColumn
a3ipxServerSocket = _A3ipxServerSocket_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 6, 1, 5),
    _A3ipxServerSocket_Type()
)
a3ipxServerSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxServerSocket.setStatus("mandatory")


class _A3ipxServerProto_Type(Integer32):
    """Custom type a3ipxServerProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("sap", 3),
          ("static", 2))
    )


_A3ipxServerProto_Type.__name__ = "Integer32"
_A3ipxServerProto_Object = MibTableColumn
a3ipxServerProto = _A3ipxServerProto_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 6, 1, 6),
    _A3ipxServerProto_Type()
)
a3ipxServerProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxServerProto.setStatus("mandatory")
_A3ipxServerStatus_Type = RowStatus
_A3ipxServerStatus_Object = MibTableColumn
a3ipxServerStatus = _A3ipxServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 6, 1, 7),
    _A3ipxServerStatus_Type()
)
a3ipxServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxServerStatus.setStatus("mandatory")
_A3ipxX25configTable_Object = MibTable
a3ipxX25configTable = _A3ipxX25configTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 7)
)
if mibBuilder.loadTexts:
    a3ipxX25configTable.setStatus("mandatory")
_A3ipxX25configEntry_Object = MibTableRow
a3ipxX25configEntry = _A3ipxX25configEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 7, 1)
)
a3ipxX25configEntry.setIndexNames(
    (0, "A3COM-IPX-R5-MIB", "a3ipxX25configPort"),
)
if mibBuilder.loadTexts:
    a3ipxX25configEntry.setStatus("mandatory")
_A3ipxX25configPort_Type = Integer32
_A3ipxX25configPort_Object = MibTableColumn
a3ipxX25configPort = _A3ipxX25configPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 7, 1, 1),
    _A3ipxX25configPort_Type()
)
a3ipxX25configPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxX25configPort.setStatus("mandatory")


class _A3ipxX25configPID_Type(Integer32):
    """Custom type a3ipxX25configPID based on Integer32"""
    defaultHexValue = 238

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_A3ipxX25configPID_Type.__name__ = "Integer32"
_A3ipxX25configPID_Object = MibTableColumn
a3ipxX25configPID = _A3ipxX25configPID_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 7, 1, 2),
    _A3ipxX25configPID_Type()
)
a3ipxX25configPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxX25configPID.setStatus("mandatory")


class _A3ipxX25configQueueSize_Type(Integer32):
    """Custom type a3ipxX25configQueueSize based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_A3ipxX25configQueueSize_Type.__name__ = "Integer32"
_A3ipxX25configQueueSize_Object = MibTableColumn
a3ipxX25configQueueSize = _A3ipxX25configQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 7, 1, 3),
    _A3ipxX25configQueueSize_Type()
)
a3ipxX25configQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxX25configQueueSize.setStatus("deprecated")


class _A3ipxX25configVClimit_Type(Integer32):
    """Custom type a3ipxX25configVClimit based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_A3ipxX25configVClimit_Type.__name__ = "Integer32"
_A3ipxX25configVClimit_Object = MibTableColumn
a3ipxX25configVClimit = _A3ipxX25configVClimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 7, 1, 4),
    _A3ipxX25configVClimit_Type()
)
a3ipxX25configVClimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxX25configVClimit.setStatus("deprecated")


class _A3ipxX25configVCtimer_Type(Integer32):
    """Custom type a3ipxX25configVCtimer based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_A3ipxX25configVCtimer_Type.__name__ = "Integer32"
_A3ipxX25configVCtimer_Object = MibTableColumn
a3ipxX25configVCtimer = _A3ipxX25configVCtimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 7, 1, 5),
    _A3ipxX25configVCtimer_Type()
)
a3ipxX25configVCtimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxX25configVCtimer.setStatus("deprecated")


class _A3ipxX25configProfId_Type(Integer32):
    """Custom type a3ipxX25configProfId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_A3ipxX25configProfId_Type.__name__ = "Integer32"
_A3ipxX25configProfId_Object = MibTableColumn
a3ipxX25configProfId = _A3ipxX25configProfId_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 7, 1, 6),
    _A3ipxX25configProfId_Type()
)
a3ipxX25configProfId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxX25configProfId.setStatus("mandatory")
_A3ipxSmdsGroupAddressTable_Object = MibTable
a3ipxSmdsGroupAddressTable = _A3ipxSmdsGroupAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 8)
)
if mibBuilder.loadTexts:
    a3ipxSmdsGroupAddressTable.setStatus("mandatory")
_A3ipxSmdsGroupAddressEntry_Object = MibTableRow
a3ipxSmdsGroupAddressEntry = _A3ipxSmdsGroupAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 8, 1)
)
a3ipxSmdsGroupAddressEntry.setIndexNames(
    (0, "A3COM-IPX-R5-MIB", "a3ipxSmdsGaIpxPort"),
)
if mibBuilder.loadTexts:
    a3ipxSmdsGroupAddressEntry.setStatus("mandatory")
_A3ipxSmdsGaIpxPort_Type = Integer32
_A3ipxSmdsGaIpxPort_Object = MibTableColumn
a3ipxSmdsGaIpxPort = _A3ipxSmdsGaIpxPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 8, 1, 1),
    _A3ipxSmdsGaIpxPort_Type()
)
a3ipxSmdsGaIpxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxSmdsGaIpxPort.setStatus("mandatory")
_A3ipxSmdsGaAddress_Type = SMDSAddress
_A3ipxSmdsGaAddress_Object = MibTableColumn
a3ipxSmdsGaAddress = _A3ipxSmdsGaAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 8, 1, 2),
    _A3ipxSmdsGaAddress_Type()
)
a3ipxSmdsGaAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxSmdsGaAddress.setStatus("mandatory")
_A3ipxPreferredSvrTable_Object = MibTable
a3ipxPreferredSvrTable = _A3ipxPreferredSvrTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 9)
)
if mibBuilder.loadTexts:
    a3ipxPreferredSvrTable.setStatus("mandatory")
_A3ipxPreferredSvrEntry_Object = MibTableRow
a3ipxPreferredSvrEntry = _A3ipxPreferredSvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 9, 1)
)
a3ipxPreferredSvrEntry.setIndexNames(
    (0, "A3COM-IPX-R5-MIB", "a3ipxPrefSvrPort"),
    (0, "A3COM-IPX-R5-MIB", "a3ipxPrefSvrName"),
)
if mibBuilder.loadTexts:
    a3ipxPreferredSvrEntry.setStatus("mandatory")
_A3ipxPrefSvrPort_Type = Integer32
_A3ipxPrefSvrPort_Object = MibTableColumn
a3ipxPrefSvrPort = _A3ipxPrefSvrPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 9, 1, 1),
    _A3ipxPrefSvrPort_Type()
)
a3ipxPrefSvrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxPrefSvrPort.setStatus("mandatory")


class _A3ipxPrefSvrName_Type(DisplayString):
    """Custom type a3ipxPrefSvrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_A3ipxPrefSvrName_Type.__name__ = "DisplayString"
_A3ipxPrefSvrName_Object = MibTableColumn
a3ipxPrefSvrName = _A3ipxPrefSvrName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 9, 1, 2),
    _A3ipxPrefSvrName_Type()
)
a3ipxPrefSvrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxPrefSvrName.setStatus("mandatory")
_A3ipxPrefSvrStatus_Type = RowStatus
_A3ipxPrefSvrStatus_Object = MibTableColumn
a3ipxPrefSvrStatus = _A3ipxPrefSvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 9, 1, 3),
    _A3ipxPrefSvrStatus_Type()
)
a3ipxPrefSvrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxPrefSvrStatus.setStatus("mandatory")
_A3ipxPortconfigTable_Object = MibTable
a3ipxPortconfigTable = _A3ipxPortconfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 10)
)
if mibBuilder.loadTexts:
    a3ipxPortconfigTable.setStatus("mandatory")
_A3ipxPortconfigEntry_Object = MibTableRow
a3ipxPortconfigEntry = _A3ipxPortconfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 10, 1)
)
a3ipxPortconfigEntry.setIndexNames(
    (0, "A3COM-IPX-R5-MIB", "a3ipxPortconfigPort"),
)
if mibBuilder.loadTexts:
    a3ipxPortconfigEntry.setStatus("mandatory")
_A3ipxPortconfigPort_Type = Integer32
_A3ipxPortconfigPort_Object = MibTableColumn
a3ipxPortconfigPort = _A3ipxPortconfigPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 10, 1, 1),
    _A3ipxPortconfigPort_Type()
)
a3ipxPortconfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxPortconfigPort.setStatus("mandatory")


class _A3ipxRipUpdateTime_Type(Integer32):
    """Custom type a3ipxRipUpdateTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_A3ipxRipUpdateTime_Type.__name__ = "Integer32"
_A3ipxRipUpdateTime_Object = MibTableColumn
a3ipxRipUpdateTime = _A3ipxRipUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 10, 1, 2),
    _A3ipxRipUpdateTime_Type()
)
a3ipxRipUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxRipUpdateTime.setStatus("mandatory")


class _A3ipxSapUpdateTime_Type(Integer32):
    """Custom type a3ipxSapUpdateTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_A3ipxSapUpdateTime_Type.__name__ = "Integer32"
_A3ipxSapUpdateTime_Object = MibTableColumn
a3ipxSapUpdateTime = _A3ipxSapUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 10, 1, 3),
    _A3ipxSapUpdateTime_Type()
)
a3ipxSapUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxSapUpdateTime.setStatus("mandatory")


class _A3ipxDefMetricHops_Type(Integer32):
    """Custom type a3ipxDefMetricHops based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_A3ipxDefMetricHops_Type.__name__ = "Integer32"
_A3ipxDefMetricHops_Object = MibTableColumn
a3ipxDefMetricHops = _A3ipxDefMetricHops_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 10, 1, 4),
    _A3ipxDefMetricHops_Type()
)
a3ipxDefMetricHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxDefMetricHops.setStatus("mandatory")


class _A3ipxDefMetricTicks_Type(Integer32):
    """Custom type a3ipxDefMetricTicks based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ipxDefMetricTicks_Type.__name__ = "Integer32"
_A3ipxDefMetricTicks_Object = MibTableColumn
a3ipxDefMetricTicks = _A3ipxDefMetricTicks_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 10, 1, 5),
    _A3ipxDefMetricTicks_Type()
)
a3ipxDefMetricTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxDefMetricTicks.setStatus("mandatory")
_A3ipxSpoofCtlTable_Object = MibTable
a3ipxSpoofCtlTable = _A3ipxSpoofCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 11)
)
if mibBuilder.loadTexts:
    a3ipxSpoofCtlTable.setStatus("mandatory")
_A3ipxSpoofCtlEntry_Object = MibTableRow
a3ipxSpoofCtlEntry = _A3ipxSpoofCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 11, 1)
)
a3ipxSpoofCtlEntry.setIndexNames(
    (0, "A3COM-IPX-R5-MIB", "a3ipxSpoofCtlPort"),
)
if mibBuilder.loadTexts:
    a3ipxSpoofCtlEntry.setStatus("mandatory")
_A3ipxSpoofCtlPort_Type = Integer32
_A3ipxSpoofCtlPort_Object = MibTableColumn
a3ipxSpoofCtlPort = _A3ipxSpoofCtlPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 11, 1, 1),
    _A3ipxSpoofCtlPort_Type()
)
a3ipxSpoofCtlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ipxSpoofCtlPort.setStatus("mandatory")


class _A3ipxSpoofCtlWatchdog_Type(Integer32):
    """Custom type a3ipxSpoofCtlWatchdog based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3ipxSpoofCtlWatchdog_Type.__name__ = "Integer32"
_A3ipxSpoofCtlWatchdog_Object = MibTableColumn
a3ipxSpoofCtlWatchdog = _A3ipxSpoofCtlWatchdog_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 7, 11, 1, 2),
    _A3ipxSpoofCtlWatchdog_Type()
)
a3ipxSpoofCtlWatchdog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ipxSpoofCtlWatchdog.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-IPX-R5-MIB",
    **{"SMDSAddress": SMDSAddress,
       "RowStatus": RowStatus,
       "IPXNET": IPXNET,
       "a3Com": a3Com,
       "brouterMIB": brouterMIB,
       "a3ComIPX": a3ComIPX,
       "a3ipxGeneral": a3ipxGeneral,
       "a3ipxRouteControl": a3ipxRouteControl,
       "a3ipxWanBcastControl": a3ipxWanBcastControl,
       "a3ipxUpdateTime": a3ipxUpdateTime,
       "a3ipxFlushRipSap": a3ipxFlushRipSap,
       "a3ipxInternalNet": a3ipxInternalNet,
       "a3ipxRouterName": a3ipxRouterName,
       "a3ipxControl": a3ipxControl,
       "a3ipxControlTable": a3ipxControlTable,
       "a3ipxControlEntry": a3ipxControlEntry,
       "a3ipxControlPort": a3ipxControlPort,
       "a3ipxControlRoute": a3ipxControlRoute,
       "a3ipxControlWanBcast": a3ipxControlWanBcast,
       "a3ipxControlChecksum": a3ipxControlChecksum,
       "a3ipxControlWanOpt": a3ipxControlWanOpt,
       "a3ipxRipHoldTimeFactor": a3ipxRipHoldTimeFactor,
       "a3ipxSapHoldTimeFactor": a3ipxSapHoldTimeFactor,
       "a3ipxRipControlTable": a3ipxRipControlTable,
       "a3ipxRipControlEntry": a3ipxRipControlEntry,
       "a3ipxRipControlPort": a3ipxRipControlPort,
       "a3ipxRipControlSwitch": a3ipxRipControlSwitch,
       "a3ipxRipControlTrigger": a3ipxRipControlTrigger,
       "a3ipxRipControlPoison": a3ipxRipControlPoison,
       "a3ipxRipControlMapOpt": a3ipxRipControlMapOpt,
       "a3ipxRipControlWanOpt": a3ipxRipControlWanOpt,
       "a3ipxRipControlPerRip": a3ipxRipControlPerRip,
       "a3ipxRipControlPerSap": a3ipxRipControlPerSap,
       "a3ipxRipControlTalk": a3ipxRipControlTalk,
       "a3ipxRipControlListen": a3ipxRipControlListen,
       "a3ipxSapControlTalk": a3ipxSapControlTalk,
       "a3ipxSapControlListen": a3ipxSapControlListen,
       "a3ipxRipCtl": a3ipxRipCtl,
       "a3ipxSapCtl": a3ipxSapCtl,
       "a3ipxWaAddrTable": a3ipxWaAddrTable,
       "a3ipxWaAddrEntry": a3ipxWaAddrEntry,
       "a3ipxWaAddrEthAddress": a3ipxWaAddrEthAddress,
       "a3ipxWaAddrPort": a3ipxWaAddrPort,
       "a3ipxWaAddrDLType": a3ipxWaAddrDLType,
       "a3ipxWaAddrDLAddress": a3ipxWaAddrDLAddress,
       "a3ipxWaAddrStatus": a3ipxWaAddrStatus,
       "a3ipxAttachedNetTable": a3ipxAttachedNetTable,
       "a3ipxAttachedNetEntry": a3ipxAttachedNetEntry,
       "a3ipxAttachedNetNumber": a3ipxAttachedNetNumber,
       "a3ipxAttachedNetPort": a3ipxAttachedNetPort,
       "a3ipxAttachedNetFormat": a3ipxAttachedNetFormat,
       "a3ipxAttachedNetType": a3ipxAttachedNetType,
       "a3ipxAttachedNetOperState": a3ipxAttachedNetOperState,
       "a3ipxAttachedNetStatus": a3ipxAttachedNetStatus,
       "a3ipxRouteTable": a3ipxRouteTable,
       "a3ipxRouteEntry": a3ipxRouteEntry,
       "a3ipxRouteDestNet": a3ipxRouteDestNet,
       "a3ipxRouteAttachedNet": a3ipxRouteAttachedNet,
       "a3ipxRouteDLType": a3ipxRouteDLType,
       "a3ipxRouteDLAddress": a3ipxRouteDLAddress,
       "a3ipxRouteHops": a3ipxRouteHops,
       "a3ipxRouteType": a3ipxRouteType,
       "a3ipxRouteProto": a3ipxRouteProto,
       "a3ipxRouteDelay": a3ipxRouteDelay,
       "a3ipxRouteStatus": a3ipxRouteStatus,
       "a3ipxServerTable": a3ipxServerTable,
       "a3ipxServerEntry": a3ipxServerEntry,
       "a3ipxServerName": a3ipxServerName,
       "a3ipxServerType": a3ipxServerType,
       "a3ipxServerNet": a3ipxServerNet,
       "a3ipxServerDLAddress": a3ipxServerDLAddress,
       "a3ipxServerSocket": a3ipxServerSocket,
       "a3ipxServerProto": a3ipxServerProto,
       "a3ipxServerStatus": a3ipxServerStatus,
       "a3ipxX25configTable": a3ipxX25configTable,
       "a3ipxX25configEntry": a3ipxX25configEntry,
       "a3ipxX25configPort": a3ipxX25configPort,
       "a3ipxX25configPID": a3ipxX25configPID,
       "a3ipxX25configQueueSize": a3ipxX25configQueueSize,
       "a3ipxX25configVClimit": a3ipxX25configVClimit,
       "a3ipxX25configVCtimer": a3ipxX25configVCtimer,
       "a3ipxX25configProfId": a3ipxX25configProfId,
       "a3ipxSmdsGroupAddressTable": a3ipxSmdsGroupAddressTable,
       "a3ipxSmdsGroupAddressEntry": a3ipxSmdsGroupAddressEntry,
       "a3ipxSmdsGaIpxPort": a3ipxSmdsGaIpxPort,
       "a3ipxSmdsGaAddress": a3ipxSmdsGaAddress,
       "a3ipxPreferredSvrTable": a3ipxPreferredSvrTable,
       "a3ipxPreferredSvrEntry": a3ipxPreferredSvrEntry,
       "a3ipxPrefSvrPort": a3ipxPrefSvrPort,
       "a3ipxPrefSvrName": a3ipxPrefSvrName,
       "a3ipxPrefSvrStatus": a3ipxPrefSvrStatus,
       "a3ipxPortconfigTable": a3ipxPortconfigTable,
       "a3ipxPortconfigEntry": a3ipxPortconfigEntry,
       "a3ipxPortconfigPort": a3ipxPortconfigPort,
       "a3ipxRipUpdateTime": a3ipxRipUpdateTime,
       "a3ipxSapUpdateTime": a3ipxSapUpdateTime,
       "a3ipxDefMetricHops": a3ipxDefMetricHops,
       "a3ipxDefMetricTicks": a3ipxDefMetricTicks,
       "a3ipxSpoofCtlTable": a3ipxSpoofCtlTable,
       "a3ipxSpoofCtlEntry": a3ipxSpoofCtlEntry,
       "a3ipxSpoofCtlPort": a3ipxSpoofCtlPort,
       "a3ipxSpoofCtlWatchdog": a3ipxSpoofCtlWatchdog}
)
