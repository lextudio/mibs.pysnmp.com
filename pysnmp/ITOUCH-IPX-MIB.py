# SNMP MIB module (ITOUCH-IPX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ITOUCH-IPX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:14 2024
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

(iTouch,) = mibBuilder.importSymbols(
    "ITOUCH-MIB",
    "iTouch")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XIpx_ObjectIdentity = ObjectIdentity
xIpx = _XIpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 15)
)
_XIpxSystem_ObjectIdentity = ObjectIdentity
xIpxSystem = _XIpxSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 15, 1)
)


class _IpxRouting_Type(Integer32):
    """Custom type ipxRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxRouting_Type.__name__ = "Integer32"
_IpxRouting_Object = MibScalar
ipxRouting = _IpxRouting_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 1, 1),
    _IpxRouting_Type()
)
ipxRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouting.setStatus("mandatory")


class _IpxInternalNetwork_Type(Integer32):
    """Custom type ipxInternalNetwork based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967294),
    )


_IpxInternalNetwork_Type.__name__ = "Integer32"
_IpxInternalNetwork_Object = MibScalar
ipxInternalNetwork = _IpxInternalNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 1, 2),
    _IpxInternalNetwork_Type()
)
ipxInternalNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInternalNetwork.setStatus("mandatory")
_XIpxIf_ObjectIdentity = ObjectIdentity
xIpxIf = _XIpxIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 15, 2)
)
_IpxIfTable_Object = MibTable
ipxIfTable = _IpxIfTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 2, 1)
)
if mibBuilder.loadTexts:
    ipxIfTable.setStatus("mandatory")
_IpxIfEntry_Object = MibTableRow
ipxIfEntry = _IpxIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1)
)
ipxIfEntry.setIndexNames(
    (0, "ITOUCH-IPX-MIB", "ipxIfIndex"),
)
if mibBuilder.loadTexts:
    ipxIfEntry.setStatus("mandatory")
_IpxIfIndex_Type = Integer32
_IpxIfIndex_Object = MibTableColumn
ipxIfIndex = _IpxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 1),
    _IpxIfIndex_Type()
)
ipxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfIndex.setStatus("mandatory")


class _IpxIfState_Type(Integer32):
    """Custom type ipxIfState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxIfState_Type.__name__ = "Integer32"
_IpxIfState_Object = MibTableColumn
ipxIfState = _IpxIfState_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 2),
    _IpxIfState_Type()
)
ipxIfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfState.setStatus("mandatory")


class _IpxIfNetwork_Type(Integer32):
    """Custom type ipxIfNetwork based on Integer32"""
    defaultValue = 0


_IpxIfNetwork_Object = MibTableColumn
ipxIfNetwork = _IpxIfNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 3),
    _IpxIfNetwork_Type()
)
ipxIfNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfNetwork.setStatus("mandatory")


class _IpxIfFrameStyle_Type(Integer32):
    """Custom type ipxIfFrameStyle based on Integer32"""
    defaultValue = 2

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
          ("ieee8022", 3),
          ("ieee8023", 2),
          ("ieee802Snap", 4))
    )


_IpxIfFrameStyle_Type.__name__ = "Integer32"
_IpxIfFrameStyle_Object = MibTableColumn
ipxIfFrameStyle = _IpxIfFrameStyle_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 4),
    _IpxIfFrameStyle_Type()
)
ipxIfFrameStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfFrameStyle.setStatus("mandatory")
_IpxIfFramesIn_Type = Counter32
_IpxIfFramesIn_Object = MibTableColumn
ipxIfFramesIn = _IpxIfFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 5),
    _IpxIfFramesIn_Type()
)
ipxIfFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfFramesIn.setStatus("mandatory")
_IpxIfFramesOut_Type = Counter32
_IpxIfFramesOut_Object = MibTableColumn
ipxIfFramesOut = _IpxIfFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 6),
    _IpxIfFramesOut_Type()
)
ipxIfFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfFramesOut.setStatus("mandatory")
_IpxIfErrors_Type = Counter32
_IpxIfErrors_Object = MibTableColumn
ipxIfErrors = _IpxIfErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 7),
    _IpxIfErrors_Type()
)
ipxIfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfErrors.setStatus("mandatory")
_IpxIfTransitDelay_Type = Integer32
_IpxIfTransitDelay_Object = MibTableColumn
ipxIfTransitDelay = _IpxIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 8),
    _IpxIfTransitDelay_Type()
)
ipxIfTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfTransitDelay.setStatus("mandatory")
_IpxIfTransitDelayActual_Type = Integer32
_IpxIfTransitDelayActual_Object = MibTableColumn
ipxIfTransitDelayActual = _IpxIfTransitDelayActual_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 9),
    _IpxIfTransitDelayActual_Type()
)
ipxIfTransitDelayActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfTransitDelayActual.setStatus("mandatory")


class _IpxIfProtocolPriority_Type(Integer32):
    """Custom type ipxIfProtocolPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("high", 5),
          ("low", 1),
          ("medium", 3))
    )


_IpxIfProtocolPriority_Type.__name__ = "Integer32"
_IpxIfProtocolPriority_Object = MibTableColumn
ipxIfProtocolPriority = _IpxIfProtocolPriority_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 10),
    _IpxIfProtocolPriority_Type()
)
ipxIfProtocolPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfProtocolPriority.setStatus("mandatory")


class _IpxIfWatchdogSpoof_Type(Integer32):
    """Custom type ipxIfWatchdogSpoof based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxIfWatchdogSpoof_Type.__name__ = "Integer32"
_IpxIfWatchdogSpoof_Object = MibTableColumn
ipxIfWatchdogSpoof = _IpxIfWatchdogSpoof_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 11),
    _IpxIfWatchdogSpoof_Type()
)
ipxIfWatchdogSpoof.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfWatchdogSpoof.setStatus("mandatory")


class _IpxIfStatusNetwork_Type(Integer32):
    """Custom type ipxIfStatusNetwork based on Integer32"""
    defaultValue = 0


_IpxIfStatusNetwork_Object = MibTableColumn
ipxIfStatusNetwork = _IpxIfStatusNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 2, 1, 1, 12),
    _IpxIfStatusNetwork_Type()
)
ipxIfStatusNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfStatusNetwork.setStatus("mandatory")
_XIpxNetbios_ObjectIdentity = ObjectIdentity
xIpxNetbios = _XIpxNetbios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 15, 3)
)


class _IpxNetbiosHopLimit_Type(Integer32):
    """Custom type ipxNetbiosHopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpxNetbiosHopLimit_Type.__name__ = "Integer32"
_IpxNetbiosHopLimit_Object = MibScalar
ipxNetbiosHopLimit = _IpxNetbiosHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 3, 1),
    _IpxNetbiosHopLimit_Type()
)
ipxNetbiosHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxNetbiosHopLimit.setStatus("mandatory")
_IpxNetbiosIfTable_Object = MibTable
ipxNetbiosIfTable = _IpxNetbiosIfTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 3, 2)
)
if mibBuilder.loadTexts:
    ipxNetbiosIfTable.setStatus("mandatory")
_IpxNetbiosIfEntry_Object = MibTableRow
ipxNetbiosIfEntry = _IpxNetbiosIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 3, 2, 1)
)
ipxNetbiosIfEntry.setIndexNames(
    (0, "ITOUCH-IPX-MIB", "ipxNetbiosIfIndex"),
)
if mibBuilder.loadTexts:
    ipxNetbiosIfEntry.setStatus("mandatory")
_IpxNetbiosIfIndex_Type = Integer32
_IpxNetbiosIfIndex_Object = MibTableColumn
ipxNetbiosIfIndex = _IpxNetbiosIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 3, 2, 1, 1),
    _IpxNetbiosIfIndex_Type()
)
ipxNetbiosIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxNetbiosIfIndex.setStatus("mandatory")


class _IpxIfNetbiosForwarding_Type(Integer32):
    """Custom type ipxIfNetbiosForwarding based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxIfNetbiosForwarding_Type.__name__ = "Integer32"
_IpxIfNetbiosForwarding_Object = MibTableColumn
ipxIfNetbiosForwarding = _IpxIfNetbiosForwarding_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 3, 2, 1, 2),
    _IpxIfNetbiosForwarding_Type()
)
ipxIfNetbiosForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfNetbiosForwarding.setStatus("mandatory")
_IpxIfNetbiosIn_Type = Counter32
_IpxIfNetbiosIn_Object = MibTableColumn
ipxIfNetbiosIn = _IpxIfNetbiosIn_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 3, 2, 1, 3),
    _IpxIfNetbiosIn_Type()
)
ipxIfNetbiosIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfNetbiosIn.setStatus("mandatory")
_IpxIfNetbiosOut_Type = Counter32
_IpxIfNetbiosOut_Object = MibTableColumn
ipxIfNetbiosOut = _IpxIfNetbiosOut_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 3, 2, 1, 4),
    _IpxIfNetbiosOut_Type()
)
ipxIfNetbiosOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfNetbiosOut.setStatus("mandatory")
_XIpxRip_ObjectIdentity = ObjectIdentity
xIpxRip = _XIpxRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 15, 4)
)
_IpxRipIfTable_Object = MibTable
ipxRipIfTable = _IpxRipIfTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 1)
)
if mibBuilder.loadTexts:
    ipxRipIfTable.setStatus("mandatory")
_IpxRipIfEntry_Object = MibTableRow
ipxRipIfEntry = _IpxRipIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1)
)
ipxRipIfEntry.setIndexNames(
    (0, "ITOUCH-IPX-MIB", "ipxRipIfIndex"),
)
if mibBuilder.loadTexts:
    ipxRipIfEntry.setStatus("mandatory")
_IpxRipIfIndex_Type = Integer32
_IpxRipIfIndex_Object = MibTableColumn
ipxRipIfIndex = _IpxRipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 1),
    _IpxRipIfIndex_Type()
)
ipxRipIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipIfIndex.setStatus("mandatory")


class _IpxIfRipBcst_Type(Integer32):
    """Custom type ipxIfRipBcst based on Integer32"""
    defaultValue = 2

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
        *(("demandCircuit", 4),
          ("disabled", 1),
          ("enabled", 2),
          ("propUpdateOnly", 3))
    )


_IpxIfRipBcst_Type.__name__ = "Integer32"
_IpxIfRipBcst_Object = MibTableColumn
ipxIfRipBcst = _IpxIfRipBcst_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 2),
    _IpxIfRipBcst_Type()
)
ipxIfRipBcst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfRipBcst.setStatus("mandatory")


class _IpxIfRipBcstDiscardTimeout_Type(Integer32):
    """Custom type ipxIfRipBcstDiscardTimeout based on Integer32"""
    defaultValue = 180


_IpxIfRipBcstDiscardTimeout_Object = MibTableColumn
ipxIfRipBcstDiscardTimeout = _IpxIfRipBcstDiscardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 3),
    _IpxIfRipBcstDiscardTimeout_Type()
)
ipxIfRipBcstDiscardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfRipBcstDiscardTimeout.setStatus("mandatory")


class _IpxIfRipBcstTimer_Type(Integer32):
    """Custom type ipxIfRipBcstTimer based on Integer32"""
    defaultValue = 60


_IpxIfRipBcstTimer_Object = MibTableColumn
ipxIfRipBcstTimer = _IpxIfRipBcstTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 4),
    _IpxIfRipBcstTimer_Type()
)
ipxIfRipBcstTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfRipBcstTimer.setStatus("mandatory")
_IpxIfRipIn_Type = Counter32
_IpxIfRipIn_Object = MibTableColumn
ipxIfRipIn = _IpxIfRipIn_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 5),
    _IpxIfRipIn_Type()
)
ipxIfRipIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfRipIn.setStatus("mandatory")
_IpxIfRipOut_Type = Counter32
_IpxIfRipOut_Object = MibTableColumn
ipxIfRipOut = _IpxIfRipOut_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 6),
    _IpxIfRipOut_Type()
)
ipxIfRipOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfRipOut.setStatus("mandatory")
_IpxIfRipAgedOut_Type = Counter32
_IpxIfRipAgedOut_Object = MibTableColumn
ipxIfRipAgedOut = _IpxIfRipAgedOut_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 1, 1, 7),
    _IpxIfRipAgedOut_Type()
)
ipxIfRipAgedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfRipAgedOut.setStatus("mandatory")
_IpxRipTable_Object = MibTable
ipxRipTable = _IpxRipTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 2)
)
if mibBuilder.loadTexts:
    ipxRipTable.setStatus("mandatory")
_IpxRipEntry_Object = MibTableRow
ipxRipEntry = _IpxRipEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1)
)
ipxRipEntry.setIndexNames(
    (0, "ITOUCH-IPX-MIB", "ipxRipNetwork"),
)
if mibBuilder.loadTexts:
    ipxRipEntry.setStatus("mandatory")
_IpxRipNetwork_Type = Integer32
_IpxRipNetwork_Object = MibTableColumn
ipxRipNetwork = _IpxRipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 1),
    _IpxRipNetwork_Type()
)
ipxRipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipNetwork.setStatus("mandatory")


class _IpxRipRouter_Type(OctetString):
    """Custom type ipxRipRouter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxRipRouter_Type.__name__ = "OctetString"
_IpxRipRouter_Object = MibTableColumn
ipxRipRouter = _IpxRipRouter_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 2),
    _IpxRipRouter_Type()
)
ipxRipRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipRouter.setStatus("mandatory")
_IpxRipInterface_Type = Integer32
_IpxRipInterface_Object = MibTableColumn
ipxRipInterface = _IpxRipInterface_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 3),
    _IpxRipInterface_Type()
)
ipxRipInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipInterface.setStatus("mandatory")
_IpxRipHops_Type = Integer32
_IpxRipHops_Object = MibTableColumn
ipxRipHops = _IpxRipHops_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 4),
    _IpxRipHops_Type()
)
ipxRipHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipHops.setStatus("mandatory")
_IpxRipTransTime_Type = Integer32
_IpxRipTransTime_Object = MibTableColumn
ipxRipTransTime = _IpxRipTransTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 5),
    _IpxRipTransTime_Type()
)
ipxRipTransTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipTransTime.setStatus("mandatory")
_IpxRipAge_Type = Integer32
_IpxRipAge_Object = MibTableColumn
ipxRipAge = _IpxRipAge_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 2, 1, 6),
    _IpxRipAge_Type()
)
ipxRipAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipAge.setStatus("mandatory")
_IpxRipRtTable_Object = MibTable
ipxRipRtTable = _IpxRipRtTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 3)
)
if mibBuilder.loadTexts:
    ipxRipRtTable.setStatus("mandatory")
_IpxRipRtEntry_Object = MibTableRow
ipxRipRtEntry = _IpxRipRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 3, 1)
)
ipxRipRtEntry.setIndexNames(
    (0, "ITOUCH-IPX-MIB", "ipxRipRtNetwork"),
    (0, "ITOUCH-IPX-MIB", "ipxRipRtInterface"),
    (0, "ITOUCH-IPX-MIB", "ipxRipRtOrigin"),
    (0, "ITOUCH-IPX-MIB", "ipxRipRtRouter"),
)
if mibBuilder.loadTexts:
    ipxRipRtEntry.setStatus("mandatory")
_IpxRipRtNetwork_Type = Integer32
_IpxRipRtNetwork_Object = MibTableColumn
ipxRipRtNetwork = _IpxRipRtNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 3, 1, 1),
    _IpxRipRtNetwork_Type()
)
ipxRipRtNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipRtNetwork.setStatus("mandatory")


class _IpxRipRtRouter_Type(OctetString):
    """Custom type ipxRipRtRouter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxRipRtRouter_Type.__name__ = "OctetString"
_IpxRipRtRouter_Object = MibTableColumn
ipxRipRtRouter = _IpxRipRtRouter_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 3, 1, 2),
    _IpxRipRtRouter_Type()
)
ipxRipRtRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipRtRouter.setStatus("mandatory")
_IpxRipRtInterface_Type = Integer32
_IpxRipRtInterface_Object = MibTableColumn
ipxRipRtInterface = _IpxRipRtInterface_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 3, 1, 3),
    _IpxRipRtInterface_Type()
)
ipxRipRtInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipRtInterface.setStatus("mandatory")


class _IpxRipRtHops_Type(Integer32):
    """Custom type ipxRipRtHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_IpxRipRtHops_Type.__name__ = "Integer32"
_IpxRipRtHops_Object = MibTableColumn
ipxRipRtHops = _IpxRipRtHops_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 3, 1, 4),
    _IpxRipRtHops_Type()
)
ipxRipRtHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRipRtHops.setStatus("mandatory")


class _IpxRipRtTransTime_Type(Integer32):
    """Custom type ipxRipRtTransTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpxRipRtTransTime_Type.__name__ = "Integer32"
_IpxRipRtTransTime_Object = MibTableColumn
ipxRipRtTransTime = _IpxRipRtTransTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 3, 1, 5),
    _IpxRipRtTransTime_Type()
)
ipxRipRtTransTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRipRtTransTime.setStatus("mandatory")


class _IpxRipRtOrigin_Type(Integer32):
    """Custom type ipxRipRtOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nlspLearned", 3),
          ("ripLearned", 1),
          ("static", 2))
    )


_IpxRipRtOrigin_Type.__name__ = "Integer32"
_IpxRipRtOrigin_Object = MibTableColumn
ipxRipRtOrigin = _IpxRipRtOrigin_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 3, 1, 6),
    _IpxRipRtOrigin_Type()
)
ipxRipRtOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRipRtOrigin.setStatus("mandatory")


class _IpxRipRtRowStatus_Type(Integer32):
    """Custom type ipxRipRtRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_IpxRipRtRowStatus_Type.__name__ = "Integer32"
_IpxRipRtRowStatus_Object = MibTableColumn
ipxRipRtRowStatus = _IpxRipRtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 4, 3, 1, 7),
    _IpxRipRtRowStatus_Type()
)
ipxRipRtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRipRtRowStatus.setStatus("mandatory")
_XIpxSap_ObjectIdentity = ObjectIdentity
xIpxSap = _XIpxSap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 15, 5)
)
_IpxSapIfTable_Object = MibTable
ipxSapIfTable = _IpxSapIfTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 1)
)
if mibBuilder.loadTexts:
    ipxSapIfTable.setStatus("mandatory")
_IpxSapIfEntry_Object = MibTableRow
ipxSapIfEntry = _IpxSapIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1)
)
ipxSapIfEntry.setIndexNames(
    (0, "ITOUCH-IPX-MIB", "ipxSapIfIndex"),
)
if mibBuilder.loadTexts:
    ipxSapIfEntry.setStatus("mandatory")
_IpxSapIfIndex_Type = Integer32
_IpxSapIfIndex_Object = MibTableColumn
ipxSapIfIndex = _IpxSapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 1),
    _IpxSapIfIndex_Type()
)
ipxSapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapIfIndex.setStatus("mandatory")


class _IpxIfSapBcst_Type(Integer32):
    """Custom type ipxIfSapBcst based on Integer32"""
    defaultValue = 2

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
        *(("demandCircuit", 4),
          ("disabled", 1),
          ("enabled", 2),
          ("propUpdateOnly", 3))
    )


_IpxIfSapBcst_Type.__name__ = "Integer32"
_IpxIfSapBcst_Object = MibTableColumn
ipxIfSapBcst = _IpxIfSapBcst_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 2),
    _IpxIfSapBcst_Type()
)
ipxIfSapBcst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfSapBcst.setStatus("mandatory")


class _IpxIfSapBcstDiscardTimeout_Type(Integer32):
    """Custom type ipxIfSapBcstDiscardTimeout based on Integer32"""
    defaultValue = 180


_IpxIfSapBcstDiscardTimeout_Object = MibTableColumn
ipxIfSapBcstDiscardTimeout = _IpxIfSapBcstDiscardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 3),
    _IpxIfSapBcstDiscardTimeout_Type()
)
ipxIfSapBcstDiscardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfSapBcstDiscardTimeout.setStatus("mandatory")


class _IpxIfSapBcstTimer_Type(Integer32):
    """Custom type ipxIfSapBcstTimer based on Integer32"""
    defaultValue = 60


_IpxIfSapBcstTimer_Object = MibTableColumn
ipxIfSapBcstTimer = _IpxIfSapBcstTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 4),
    _IpxIfSapBcstTimer_Type()
)
ipxIfSapBcstTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfSapBcstTimer.setStatus("mandatory")
_IpxIfSapIn_Type = Counter32
_IpxIfSapIn_Object = MibTableColumn
ipxIfSapIn = _IpxIfSapIn_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 5),
    _IpxIfSapIn_Type()
)
ipxIfSapIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfSapIn.setStatus("mandatory")
_IpxIfSapOut_Type = Counter32
_IpxIfSapOut_Object = MibTableColumn
ipxIfSapOut = _IpxIfSapOut_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 6),
    _IpxIfSapOut_Type()
)
ipxIfSapOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfSapOut.setStatus("mandatory")
_IpxIfSapAgedOut_Type = Counter32
_IpxIfSapAgedOut_Object = MibTableColumn
ipxIfSapAgedOut = _IpxIfSapAgedOut_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 1, 1, 7),
    _IpxIfSapAgedOut_Type()
)
ipxIfSapAgedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfSapAgedOut.setStatus("mandatory")
_IpxSapTable_Object = MibTable
ipxSapTable = _IpxSapTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 2)
)
if mibBuilder.loadTexts:
    ipxSapTable.setStatus("mandatory")
_IpxSapEntry_Object = MibTableRow
ipxSapEntry = _IpxSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1)
)
ipxSapEntry.setIndexNames(
    (0, "ITOUCH-IPX-MIB", "ipxSapName"),
    (0, "ITOUCH-IPX-MIB", "ipxSapType"),
)
if mibBuilder.loadTexts:
    ipxSapEntry.setStatus("mandatory")


class _IpxSapName_Type(DisplayString):
    """Custom type ipxSapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(48, 48),
    )


_IpxSapName_Type.__name__ = "DisplayString"
_IpxSapName_Object = MibTableColumn
ipxSapName = _IpxSapName_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 1),
    _IpxSapName_Type()
)
ipxSapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapName.setStatus("mandatory")
_IpxSapNetwork_Type = Integer32
_IpxSapNetwork_Object = MibTableColumn
ipxSapNetwork = _IpxSapNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 2),
    _IpxSapNetwork_Type()
)
ipxSapNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapNetwork.setStatus("mandatory")


class _IpxSapHost_Type(OctetString):
    """Custom type ipxSapHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxSapHost_Type.__name__ = "OctetString"
_IpxSapHost_Object = MibTableColumn
ipxSapHost = _IpxSapHost_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 3),
    _IpxSapHost_Type()
)
ipxSapHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapHost.setStatus("mandatory")
_IpxSapSocket_Type = Integer32
_IpxSapSocket_Object = MibTableColumn
ipxSapSocket = _IpxSapSocket_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 4),
    _IpxSapSocket_Type()
)
ipxSapSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapSocket.setStatus("mandatory")
_IpxSapInterface_Type = Integer32
_IpxSapInterface_Object = MibTableColumn
ipxSapInterface = _IpxSapInterface_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 5),
    _IpxSapInterface_Type()
)
ipxSapInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapInterface.setStatus("mandatory")


class _IpxSapType_Type(Integer32):
    """Custom type ipxSapType based on Integer32"""
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("administration", 11),
          ("archiveQueue", 8),
          ("archiveServer", 9),
          ("gateway1", 6),
          ("jobQueue", 10),
          ("jobServer", 5),
          ("novellFileServer", 4),
          ("printQueue", 3),
          ("printServer", 7),
          ("user", 1),
          ("userGroup", 2))
    )


_IpxSapType_Type.__name__ = "Integer32"
_IpxSapType_Object = MibTableColumn
ipxSapType = _IpxSapType_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 6),
    _IpxSapType_Type()
)
ipxSapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapType.setStatus("mandatory")
_IpxSapAge_Type = Integer32
_IpxSapAge_Object = MibTableColumn
ipxSapAge = _IpxSapAge_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 2, 1, 7),
    _IpxSapAge_Type()
)
ipxSapAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapAge.setStatus("mandatory")
_IpxSapSvTable_Object = MibTable
ipxSapSvTable = _IpxSapSvTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 3)
)
if mibBuilder.loadTexts:
    ipxSapSvTable.setStatus("mandatory")
_IpxSapSvEntry_Object = MibTableRow
ipxSapSvEntry = _IpxSapSvEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 3, 1)
)
ipxSapSvEntry.setIndexNames(
    (0, "ITOUCH-IPX-MIB", "ipxSapSvName"),
    (0, "ITOUCH-IPX-MIB", "ipxSapSvType"),
    (0, "ITOUCH-IPX-MIB", "ipxSapSvOrigin"),
    (0, "ITOUCH-IPX-MIB", "ipxSapSvNetwork"),
    (0, "ITOUCH-IPX-MIB", "ipxSapSvSocket"),
    (0, "ITOUCH-IPX-MIB", "ipxSapSvHost"),
)
if mibBuilder.loadTexts:
    ipxSapSvEntry.setStatus("mandatory")


class _IpxSapSvName_Type(DisplayString):
    """Custom type ipxSapSvName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_IpxSapSvName_Type.__name__ = "DisplayString"
_IpxSapSvName_Object = MibTableColumn
ipxSapSvName = _IpxSapSvName_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 3, 1, 1),
    _IpxSapSvName_Type()
)
ipxSapSvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapSvName.setStatus("mandatory")
_IpxSapSvNetwork_Type = Integer32
_IpxSapSvNetwork_Object = MibTableColumn
ipxSapSvNetwork = _IpxSapSvNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 3, 1, 2),
    _IpxSapSvNetwork_Type()
)
ipxSapSvNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapSvNetwork.setStatus("mandatory")


class _IpxSapSvHost_Type(OctetString):
    """Custom type ipxSapSvHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxSapSvHost_Type.__name__ = "OctetString"
_IpxSapSvHost_Object = MibTableColumn
ipxSapSvHost = _IpxSapSvHost_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 3, 1, 3),
    _IpxSapSvHost_Type()
)
ipxSapSvHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapSvHost.setStatus("mandatory")


class _IpxSapSvSocket_Type(Integer32):
    """Custom type ipxSapSvSocket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpxSapSvSocket_Type.__name__ = "Integer32"
_IpxSapSvSocket_Object = MibTableColumn
ipxSapSvSocket = _IpxSapSvSocket_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 3, 1, 4),
    _IpxSapSvSocket_Type()
)
ipxSapSvSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapSvSocket.setStatus("mandatory")
_IpxSapSvInterface_Type = Integer32
_IpxSapSvInterface_Object = MibTableColumn
ipxSapSvInterface = _IpxSapSvInterface_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 3, 1, 5),
    _IpxSapSvInterface_Type()
)
ipxSapSvInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapSvInterface.setStatus("mandatory")


class _IpxSapSvOrigin_Type(Integer32):
    """Custom type ipxSapSvOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipxSapLearned", 1),
          ("ipxStatic", 2))
    )


_IpxSapSvOrigin_Type.__name__ = "Integer32"
_IpxSapSvOrigin_Object = MibTableColumn
ipxSapSvOrigin = _IpxSapSvOrigin_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 3, 1, 6),
    _IpxSapSvOrigin_Type()
)
ipxSapSvOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapSvOrigin.setStatus("mandatory")


class _IpxSapSvType_Type(Integer32):
    """Custom type ipxSapSvType based on Integer32"""
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("administration", 11),
          ("archiveQueue", 8),
          ("archiveServer", 9),
          ("gateway1", 6),
          ("jobQueue", 10),
          ("jobServer", 5),
          ("novellFileServer", 4),
          ("printQueue", 3),
          ("printServer", 7),
          ("user", 1),
          ("userGroup", 2))
    )


_IpxSapSvType_Type.__name__ = "Integer32"
_IpxSapSvType_Object = MibTableColumn
ipxSapSvType = _IpxSapSvType_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 3, 1, 7),
    _IpxSapSvType_Type()
)
ipxSapSvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapSvType.setStatus("mandatory")


class _IpxSapSvHops_Type(Integer32):
    """Custom type ipxSapSvHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_IpxSapSvHops_Type.__name__ = "Integer32"
_IpxSapSvHops_Object = MibTableColumn
ipxSapSvHops = _IpxSapSvHops_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 3, 1, 8),
    _IpxSapSvHops_Type()
)
ipxSapSvHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSapSvHops.setStatus("mandatory")


class _IpxSapSvRowStatus_Type(Integer32):
    """Custom type ipxSapSvRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxSapSvRowStatus_Type.__name__ = "Integer32"
_IpxSapSvRowStatus_Object = MibTableColumn
ipxSapSvRowStatus = _IpxSapSvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 3, 1, 9),
    _IpxSapSvRowStatus_Type()
)
ipxSapSvRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSapSvRowStatus.setStatus("mandatory")
_IpxSapSvAge_Type = Integer32
_IpxSapSvAge_Object = MibTableColumn
ipxSapSvAge = _IpxSapSvAge_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 5, 3, 1, 10),
    _IpxSapSvAge_Type()
)
ipxSapSvAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapSvAge.setStatus("mandatory")
_XIpxFilter_ObjectIdentity = ObjectIdentity
xIpxFilter = _XIpxFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 15, 6)
)
_IpxIfFilterTable_Object = MibTable
ipxIfFilterTable = _IpxIfFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 1)
)
if mibBuilder.loadTexts:
    ipxIfFilterTable.setStatus("mandatory")
_IpxIfFilterEntry_Object = MibTableRow
ipxIfFilterEntry = _IpxIfFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1)
)
ipxIfFilterEntry.setIndexNames(
    (0, "ITOUCH-IPX-MIB", "ipxIfIndex"),
    (0, "ITOUCH-IPX-MIB", "ipxIfFilterDestNetwork"),
    (0, "ITOUCH-IPX-MIB", "ipxIfFilterDestNode"),
    (0, "ITOUCH-IPX-MIB", "ipxIfFilterSourceNetwork"),
    (0, "ITOUCH-IPX-MIB", "ipxIfFilterSourceNode"),
    (0, "ITOUCH-IPX-MIB", "ipxIfFilterPacketType"),
    (0, "ITOUCH-IPX-MIB", "ipxIfFilterStatusDestNetworkAll"),
    (0, "ITOUCH-IPX-MIB", "ipxIfFilterStatusDestNodeAll"),
    (0, "ITOUCH-IPX-MIB", "ipxIfFilterStatusSourceNetworkAll"),
    (0, "ITOUCH-IPX-MIB", "ipxIfFilterStatusSourceNodeAll"),
    (0, "ITOUCH-IPX-MIB", "ipxIfFilterStatusPacketTypeAll"),
)
if mibBuilder.loadTexts:
    ipxIfFilterEntry.setStatus("mandatory")
_IpxIfFilterIndex_Type = Integer32
_IpxIfFilterIndex_Object = MibTableColumn
ipxIfFilterIndex = _IpxIfFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 1),
    _IpxIfFilterIndex_Type()
)
ipxIfFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfFilterIndex.setStatus("mandatory")
_IpxIfFilterDestNetwork_Type = Integer32
_IpxIfFilterDestNetwork_Object = MibTableColumn
ipxIfFilterDestNetwork = _IpxIfFilterDestNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 2),
    _IpxIfFilterDestNetwork_Type()
)
ipxIfFilterDestNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfFilterDestNetwork.setStatus("mandatory")


class _IpxIfFilterDestNode_Type(OctetString):
    """Custom type ipxIfFilterDestNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxIfFilterDestNode_Type.__name__ = "OctetString"
_IpxIfFilterDestNode_Object = MibTableColumn
ipxIfFilterDestNode = _IpxIfFilterDestNode_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 3),
    _IpxIfFilterDestNode_Type()
)
ipxIfFilterDestNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfFilterDestNode.setStatus("mandatory")
_IpxIfFilterSourceNetwork_Type = Integer32
_IpxIfFilterSourceNetwork_Object = MibTableColumn
ipxIfFilterSourceNetwork = _IpxIfFilterSourceNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 4),
    _IpxIfFilterSourceNetwork_Type()
)
ipxIfFilterSourceNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfFilterSourceNetwork.setStatus("mandatory")


class _IpxIfFilterSourceNode_Type(OctetString):
    """Custom type ipxIfFilterSourceNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxIfFilterSourceNode_Type.__name__ = "OctetString"
_IpxIfFilterSourceNode_Object = MibTableColumn
ipxIfFilterSourceNode = _IpxIfFilterSourceNode_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 5),
    _IpxIfFilterSourceNode_Type()
)
ipxIfFilterSourceNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfFilterSourceNode.setStatus("mandatory")


class _IpxIfFilterPacketType_Type(Integer32):
    """Custom type ipxIfFilterPacketType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpxIfFilterPacketType_Type.__name__ = "Integer32"
_IpxIfFilterPacketType_Object = MibTableColumn
ipxIfFilterPacketType = _IpxIfFilterPacketType_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 6),
    _IpxIfFilterPacketType_Type()
)
ipxIfFilterPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfFilterPacketType.setStatus("mandatory")


class _IpxIfFilterAction_Type(Integer32):
    """Custom type ipxIfFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_IpxIfFilterAction_Type.__name__ = "Integer32"
_IpxIfFilterAction_Object = MibTableColumn
ipxIfFilterAction = _IpxIfFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 7),
    _IpxIfFilterAction_Type()
)
ipxIfFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfFilterAction.setStatus("mandatory")


class _IpxIfFilterRowStatus_Type(Integer32):
    """Custom type ipxIfFilterRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_IpxIfFilterRowStatus_Type.__name__ = "Integer32"
_IpxIfFilterRowStatus_Object = MibTableColumn
ipxIfFilterRowStatus = _IpxIfFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 8),
    _IpxIfFilterRowStatus_Type()
)
ipxIfFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfFilterRowStatus.setStatus("mandatory")


class _IpxIfFilterStatusDestNetworkAll_Type(Integer32):
    """Custom type ipxIfFilterStatusDestNetworkAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxIfFilterStatusDestNetworkAll_Type.__name__ = "Integer32"
_IpxIfFilterStatusDestNetworkAll_Object = MibTableColumn
ipxIfFilterStatusDestNetworkAll = _IpxIfFilterStatusDestNetworkAll_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 9),
    _IpxIfFilterStatusDestNetworkAll_Type()
)
ipxIfFilterStatusDestNetworkAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfFilterStatusDestNetworkAll.setStatus("mandatory")


class _IpxIfFilterStatusDestNodeAll_Type(Integer32):
    """Custom type ipxIfFilterStatusDestNodeAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxIfFilterStatusDestNodeAll_Type.__name__ = "Integer32"
_IpxIfFilterStatusDestNodeAll_Object = MibTableColumn
ipxIfFilterStatusDestNodeAll = _IpxIfFilterStatusDestNodeAll_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 10),
    _IpxIfFilterStatusDestNodeAll_Type()
)
ipxIfFilterStatusDestNodeAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfFilterStatusDestNodeAll.setStatus("mandatory")


class _IpxIfFilterStatusSourceNetworkAll_Type(Integer32):
    """Custom type ipxIfFilterStatusSourceNetworkAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxIfFilterStatusSourceNetworkAll_Type.__name__ = "Integer32"
_IpxIfFilterStatusSourceNetworkAll_Object = MibTableColumn
ipxIfFilterStatusSourceNetworkAll = _IpxIfFilterStatusSourceNetworkAll_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 11),
    _IpxIfFilterStatusSourceNetworkAll_Type()
)
ipxIfFilterStatusSourceNetworkAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfFilterStatusSourceNetworkAll.setStatus("mandatory")


class _IpxIfFilterStatusSourceNodeAll_Type(Integer32):
    """Custom type ipxIfFilterStatusSourceNodeAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxIfFilterStatusSourceNodeAll_Type.__name__ = "Integer32"
_IpxIfFilterStatusSourceNodeAll_Object = MibTableColumn
ipxIfFilterStatusSourceNodeAll = _IpxIfFilterStatusSourceNodeAll_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 12),
    _IpxIfFilterStatusSourceNodeAll_Type()
)
ipxIfFilterStatusSourceNodeAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfFilterStatusSourceNodeAll.setStatus("mandatory")


class _IpxIfFilterStatusPacketTypeAll_Type(Integer32):
    """Custom type ipxIfFilterStatusPacketTypeAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxIfFilterStatusPacketTypeAll_Type.__name__ = "Integer32"
_IpxIfFilterStatusPacketTypeAll_Object = MibTableColumn
ipxIfFilterStatusPacketTypeAll = _IpxIfFilterStatusPacketTypeAll_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 1, 1, 13),
    _IpxIfFilterStatusPacketTypeAll_Type()
)
ipxIfFilterStatusPacketTypeAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfFilterStatusPacketTypeAll.setStatus("mandatory")
_IpxIfRipFilterTable_Object = MibTable
ipxIfRipFilterTable = _IpxIfRipFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 2)
)
if mibBuilder.loadTexts:
    ipxIfRipFilterTable.setStatus("mandatory")
_IpxIfRipFilterEntry_Object = MibTableRow
ipxIfRipFilterEntry = _IpxIfRipFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 2, 1)
)
ipxIfRipFilterEntry.setIndexNames(
    (0, "ITOUCH-IPX-MIB", "ipxIfIndex"),
    (0, "ITOUCH-IPX-MIB", "ipxIfRipFilterType"),
    (0, "ITOUCH-IPX-MIB", "ipxIfRipFilterNetwork"),
    (0, "ITOUCH-IPX-MIB", "ipxIfRipFilterNetworkAll"),
    (0, "ITOUCH-IPX-MIB", "ipxIfRipFilterHost"),
)
if mibBuilder.loadTexts:
    ipxIfRipFilterEntry.setStatus("mandatory")
_IpxIfRipFilterNetwork_Type = Integer32
_IpxIfRipFilterNetwork_Object = MibTableColumn
ipxIfRipFilterNetwork = _IpxIfRipFilterNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 2, 1, 1),
    _IpxIfRipFilterNetwork_Type()
)
ipxIfRipFilterNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfRipFilterNetwork.setStatus("mandatory")


class _IpxIfRipFilterType_Type(Integer32):
    """Custom type ipxIfRipFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("export", 2),
          ("import", 1))
    )


_IpxIfRipFilterType_Type.__name__ = "Integer32"
_IpxIfRipFilterType_Object = MibTableColumn
ipxIfRipFilterType = _IpxIfRipFilterType_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 2, 1, 2),
    _IpxIfRipFilterType_Type()
)
ipxIfRipFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfRipFilterType.setStatus("mandatory")


class _IpxIfRipFilterAction_Type(Integer32):
    """Custom type ipxIfRipFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_IpxIfRipFilterAction_Type.__name__ = "Integer32"
_IpxIfRipFilterAction_Object = MibTableColumn
ipxIfRipFilterAction = _IpxIfRipFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 2, 1, 3),
    _IpxIfRipFilterAction_Type()
)
ipxIfRipFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfRipFilterAction.setStatus("mandatory")


class _IpxIfRipFilterRowStatus_Type(Integer32):
    """Custom type ipxIfRipFilterRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_IpxIfRipFilterRowStatus_Type.__name__ = "Integer32"
_IpxIfRipFilterRowStatus_Object = MibTableColumn
ipxIfRipFilterRowStatus = _IpxIfRipFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 2, 1, 4),
    _IpxIfRipFilterRowStatus_Type()
)
ipxIfRipFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfRipFilterRowStatus.setStatus("mandatory")


class _IpxIfRipFilterNetworkAll_Type(Integer32):
    """Custom type ipxIfRipFilterNetworkAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxIfRipFilterNetworkAll_Type.__name__ = "Integer32"
_IpxIfRipFilterNetworkAll_Object = MibTableColumn
ipxIfRipFilterNetworkAll = _IpxIfRipFilterNetworkAll_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 2, 1, 5),
    _IpxIfRipFilterNetworkAll_Type()
)
ipxIfRipFilterNetworkAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfRipFilterNetworkAll.setStatus("mandatory")


class _IpxIfRipFilterHost_Type(OctetString):
    """Custom type ipxIfRipFilterHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxIfRipFilterHost_Type.__name__ = "OctetString"
_IpxIfRipFilterHost_Object = MibTableColumn
ipxIfRipFilterHost = _IpxIfRipFilterHost_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 2, 1, 6),
    _IpxIfRipFilterHost_Type()
)
ipxIfRipFilterHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfRipFilterHost.setStatus("mandatory")
_IpxIfSapFilterTable_Object = MibTable
ipxIfSapFilterTable = _IpxIfSapFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 3)
)
if mibBuilder.loadTexts:
    ipxIfSapFilterTable.setStatus("mandatory")
_IpxIfSapFilterEntry_Object = MibTableRow
ipxIfSapFilterEntry = _IpxIfSapFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 3, 1)
)
ipxIfSapFilterEntry.setIndexNames(
    (0, "ITOUCH-IPX-MIB", "ipxIfIndex"),
    (0, "ITOUCH-IPX-MIB", "ipxIfSapFilterType"),
    (0, "ITOUCH-IPX-MIB", "ipxIfSapFilterName"),
    (0, "ITOUCH-IPX-MIB", "ipxIfSapFilterServiceType"),
    (0, "ITOUCH-IPX-MIB", "ipxIfSapFilterServiceTypeAll"),
    (0, "ITOUCH-IPX-MIB", "ipxIfSapFilterNetwork"),
    (0, "ITOUCH-IPX-MIB", "ipxIfSapFilterNetworkAll"),
    (0, "ITOUCH-IPX-MIB", "ipxIfSapFilterHost"),
)
if mibBuilder.loadTexts:
    ipxIfSapFilterEntry.setStatus("mandatory")
_IpxIfSapFilterNetwork_Type = Integer32
_IpxIfSapFilterNetwork_Object = MibTableColumn
ipxIfSapFilterNetwork = _IpxIfSapFilterNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 3, 1, 1),
    _IpxIfSapFilterNetwork_Type()
)
ipxIfSapFilterNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfSapFilterNetwork.setStatus("mandatory")


class _IpxIfSapFilterType_Type(Integer32):
    """Custom type ipxIfSapFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("export", 2),
          ("import", 1))
    )


_IpxIfSapFilterType_Type.__name__ = "Integer32"
_IpxIfSapFilterType_Object = MibTableColumn
ipxIfSapFilterType = _IpxIfSapFilterType_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 3, 1, 2),
    _IpxIfSapFilterType_Type()
)
ipxIfSapFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfSapFilterType.setStatus("mandatory")


class _IpxIfSapFilterServiceType_Type(Integer32):
    """Custom type ipxIfSapFilterServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpxIfSapFilterServiceType_Type.__name__ = "Integer32"
_IpxIfSapFilterServiceType_Object = MibTableColumn
ipxIfSapFilterServiceType = _IpxIfSapFilterServiceType_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 3, 1, 3),
    _IpxIfSapFilterServiceType_Type()
)
ipxIfSapFilterServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfSapFilterServiceType.setStatus("mandatory")


class _IpxIfSapFilterAction_Type(Integer32):
    """Custom type ipxIfSapFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_IpxIfSapFilterAction_Type.__name__ = "Integer32"
_IpxIfSapFilterAction_Object = MibTableColumn
ipxIfSapFilterAction = _IpxIfSapFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 3, 1, 4),
    _IpxIfSapFilterAction_Type()
)
ipxIfSapFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfSapFilterAction.setStatus("mandatory")


class _IpxIfSapFilterRowStatus_Type(Integer32):
    """Custom type ipxIfSapFilterRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_IpxIfSapFilterRowStatus_Type.__name__ = "Integer32"
_IpxIfSapFilterRowStatus_Object = MibTableColumn
ipxIfSapFilterRowStatus = _IpxIfSapFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 3, 1, 5),
    _IpxIfSapFilterRowStatus_Type()
)
ipxIfSapFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxIfSapFilterRowStatus.setStatus("mandatory")


class _IpxIfSapFilterNetworkAll_Type(Integer32):
    """Custom type ipxIfSapFilterNetworkAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxIfSapFilterNetworkAll_Type.__name__ = "Integer32"
_IpxIfSapFilterNetworkAll_Object = MibTableColumn
ipxIfSapFilterNetworkAll = _IpxIfSapFilterNetworkAll_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 3, 1, 6),
    _IpxIfSapFilterNetworkAll_Type()
)
ipxIfSapFilterNetworkAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfSapFilterNetworkAll.setStatus("mandatory")


class _IpxIfSapFilterServiceTypeAll_Type(Integer32):
    """Custom type ipxIfSapFilterServiceTypeAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxIfSapFilterServiceTypeAll_Type.__name__ = "Integer32"
_IpxIfSapFilterServiceTypeAll_Object = MibTableColumn
ipxIfSapFilterServiceTypeAll = _IpxIfSapFilterServiceTypeAll_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 3, 1, 7),
    _IpxIfSapFilterServiceTypeAll_Type()
)
ipxIfSapFilterServiceTypeAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfSapFilterServiceTypeAll.setStatus("mandatory")


class _IpxIfSapFilterName_Type(DisplayString):
    """Custom type ipxIfSapFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_IpxIfSapFilterName_Type.__name__ = "DisplayString"
_IpxIfSapFilterName_Object = MibTableColumn
ipxIfSapFilterName = _IpxIfSapFilterName_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 3, 1, 8),
    _IpxIfSapFilterName_Type()
)
ipxIfSapFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfSapFilterName.setStatus("mandatory")


class _IpxIfSapFilterHost_Type(OctetString):
    """Custom type ipxIfSapFilterHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxIfSapFilterHost_Type.__name__ = "OctetString"
_IpxIfSapFilterHost_Object = MibTableColumn
ipxIfSapFilterHost = _IpxIfSapFilterHost_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 6, 3, 1, 9),
    _IpxIfSapFilterHost_Type()
)
ipxIfSapFilterHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxIfSapFilterHost.setStatus("mandatory")
_XIpxPrinter_ObjectIdentity = ObjectIdentity
xIpxPrinter = _XIpxPrinter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 15, 8)
)
_IpxPrinterPortTable_Object = MibTable
ipxPrinterPortTable = _IpxPrinterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 8, 1)
)
if mibBuilder.loadTexts:
    ipxPrinterPortTable.setStatus("mandatory")
_IpxPrinterPortEntry_Object = MibTableRow
ipxPrinterPortEntry = _IpxPrinterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 8, 1, 1)
)
ipxPrinterPortEntry.setIndexNames(
    (0, "ITOUCH-IPX-MIB", "ipxPrinterPortIndex"),
)
if mibBuilder.loadTexts:
    ipxPrinterPortEntry.setStatus("mandatory")
_IpxPrinterPortIndex_Type = Integer32
_IpxPrinterPortIndex_Object = MibTableColumn
ipxPrinterPortIndex = _IpxPrinterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 8, 1, 1, 1),
    _IpxPrinterPortIndex_Type()
)
ipxPrinterPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxPrinterPortIndex.setStatus("mandatory")


class _IpxPrinterPortStatus_Type(Integer32):
    """Custom type ipxPrinterPortStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_IpxPrinterPortStatus_Type.__name__ = "Integer32"
_IpxPrinterPortStatus_Object = MibTableColumn
ipxPrinterPortStatus = _IpxPrinterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 8, 1, 1, 2),
    _IpxPrinterPortStatus_Type()
)
ipxPrinterPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxPrinterPortStatus.setStatus("mandatory")


class _IpxPrinterPortServer_Type(DisplayString):
    """Custom type ipxPrinterPortServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_IpxPrinterPortServer_Type.__name__ = "DisplayString"
_IpxPrinterPortServer_Object = MibTableColumn
ipxPrinterPortServer = _IpxPrinterPortServer_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 8, 1, 1, 3),
    _IpxPrinterPortServer_Type()
)
ipxPrinterPortServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxPrinterPortServer.setStatus("mandatory")


class _IpxPrinterPortPrinter_Type(Integer32):
    """Custom type ipxPrinterPortPrinter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpxPrinterPortPrinter_Type.__name__ = "Integer32"
_IpxPrinterPortPrinter_Object = MibTableColumn
ipxPrinterPortPrinter = _IpxPrinterPortPrinter_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 8, 1, 1, 4),
    _IpxPrinterPortPrinter_Type()
)
ipxPrinterPortPrinter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxPrinterPortPrinter.setStatus("mandatory")


class _IpxTimeout_Type(Integer32):
    """Custom type ipxTimeout based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 300),
    )


_IpxTimeout_Type.__name__ = "Integer32"
_IpxTimeout_Object = MibTableColumn
ipxTimeout = _IpxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 8, 1, 1, 5),
    _IpxTimeout_Type()
)
ipxTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxTimeout.setStatus("mandatory")


class _IpxPrinterEthernet_Type(Integer32):
    """Custom type ipxPrinterEthernet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxPrinterEthernet_Type.__name__ = "Integer32"
_IpxPrinterEthernet_Object = MibScalar
ipxPrinterEthernet = _IpxPrinterEthernet_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 8, 2),
    _IpxPrinterEthernet_Type()
)
ipxPrinterEthernet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxPrinterEthernet.setStatus("mandatory")


class _IpxPrinterMac_Type(Integer32):
    """Custom type ipxPrinterMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxPrinterMac_Type.__name__ = "Integer32"
_IpxPrinterMac_Object = MibScalar
ipxPrinterMac = _IpxPrinterMac_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 8, 3),
    _IpxPrinterMac_Type()
)
ipxPrinterMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxPrinterMac.setStatus("mandatory")


class _IpxPrinterMac802_2_Type(Integer32):
    """Custom type ipxPrinterMac802_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxPrinterMac802_2_Type.__name__ = "Integer32"
_IpxPrinterMac802_2_Object = MibScalar
ipxPrinterMac802_2 = _IpxPrinterMac802_2_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 8, 4),
    _IpxPrinterMac802_2_Type()
)
ipxPrinterMac802_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxPrinterMac802_2.setStatus("mandatory")


class _IpxPrinterMac802_2_Snap_Type(Integer32):
    """Custom type ipxPrinterMac802_2_Snap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpxPrinterMac802_2_Snap_Type.__name__ = "Integer32"
_IpxPrinterMac802_2_Snap_Object = MibScalar
ipxPrinterMac802_2_Snap = _IpxPrinterMac802_2_Snap_Object(
    (1, 3, 6, 1, 4, 1, 33, 15, 8, 5),
    _IpxPrinterMac802_2_Snap_Type()
)
ipxPrinterMac802_2_Snap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxPrinterMac802_2_Snap.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ITOUCH-IPX-MIB",
    **{"xIpx": xIpx,
       "xIpxSystem": xIpxSystem,
       "ipxRouting": ipxRouting,
       "ipxInternalNetwork": ipxInternalNetwork,
       "xIpxIf": xIpxIf,
       "ipxIfTable": ipxIfTable,
       "ipxIfEntry": ipxIfEntry,
       "ipxIfIndex": ipxIfIndex,
       "ipxIfState": ipxIfState,
       "ipxIfNetwork": ipxIfNetwork,
       "ipxIfFrameStyle": ipxIfFrameStyle,
       "ipxIfFramesIn": ipxIfFramesIn,
       "ipxIfFramesOut": ipxIfFramesOut,
       "ipxIfErrors": ipxIfErrors,
       "ipxIfTransitDelay": ipxIfTransitDelay,
       "ipxIfTransitDelayActual": ipxIfTransitDelayActual,
       "ipxIfProtocolPriority": ipxIfProtocolPriority,
       "ipxIfWatchdogSpoof": ipxIfWatchdogSpoof,
       "ipxIfStatusNetwork": ipxIfStatusNetwork,
       "xIpxNetbios": xIpxNetbios,
       "ipxNetbiosHopLimit": ipxNetbiosHopLimit,
       "ipxNetbiosIfTable": ipxNetbiosIfTable,
       "ipxNetbiosIfEntry": ipxNetbiosIfEntry,
       "ipxNetbiosIfIndex": ipxNetbiosIfIndex,
       "ipxIfNetbiosForwarding": ipxIfNetbiosForwarding,
       "ipxIfNetbiosIn": ipxIfNetbiosIn,
       "ipxIfNetbiosOut": ipxIfNetbiosOut,
       "xIpxRip": xIpxRip,
       "ipxRipIfTable": ipxRipIfTable,
       "ipxRipIfEntry": ipxRipIfEntry,
       "ipxRipIfIndex": ipxRipIfIndex,
       "ipxIfRipBcst": ipxIfRipBcst,
       "ipxIfRipBcstDiscardTimeout": ipxIfRipBcstDiscardTimeout,
       "ipxIfRipBcstTimer": ipxIfRipBcstTimer,
       "ipxIfRipIn": ipxIfRipIn,
       "ipxIfRipOut": ipxIfRipOut,
       "ipxIfRipAgedOut": ipxIfRipAgedOut,
       "ipxRipTable": ipxRipTable,
       "ipxRipEntry": ipxRipEntry,
       "ipxRipNetwork": ipxRipNetwork,
       "ipxRipRouter": ipxRipRouter,
       "ipxRipInterface": ipxRipInterface,
       "ipxRipHops": ipxRipHops,
       "ipxRipTransTime": ipxRipTransTime,
       "ipxRipAge": ipxRipAge,
       "ipxRipRtTable": ipxRipRtTable,
       "ipxRipRtEntry": ipxRipRtEntry,
       "ipxRipRtNetwork": ipxRipRtNetwork,
       "ipxRipRtRouter": ipxRipRtRouter,
       "ipxRipRtInterface": ipxRipRtInterface,
       "ipxRipRtHops": ipxRipRtHops,
       "ipxRipRtTransTime": ipxRipRtTransTime,
       "ipxRipRtOrigin": ipxRipRtOrigin,
       "ipxRipRtRowStatus": ipxRipRtRowStatus,
       "xIpxSap": xIpxSap,
       "ipxSapIfTable": ipxSapIfTable,
       "ipxSapIfEntry": ipxSapIfEntry,
       "ipxSapIfIndex": ipxSapIfIndex,
       "ipxIfSapBcst": ipxIfSapBcst,
       "ipxIfSapBcstDiscardTimeout": ipxIfSapBcstDiscardTimeout,
       "ipxIfSapBcstTimer": ipxIfSapBcstTimer,
       "ipxIfSapIn": ipxIfSapIn,
       "ipxIfSapOut": ipxIfSapOut,
       "ipxIfSapAgedOut": ipxIfSapAgedOut,
       "ipxSapTable": ipxSapTable,
       "ipxSapEntry": ipxSapEntry,
       "ipxSapName": ipxSapName,
       "ipxSapNetwork": ipxSapNetwork,
       "ipxSapHost": ipxSapHost,
       "ipxSapSocket": ipxSapSocket,
       "ipxSapInterface": ipxSapInterface,
       "ipxSapType": ipxSapType,
       "ipxSapAge": ipxSapAge,
       "ipxSapSvTable": ipxSapSvTable,
       "ipxSapSvEntry": ipxSapSvEntry,
       "ipxSapSvName": ipxSapSvName,
       "ipxSapSvNetwork": ipxSapSvNetwork,
       "ipxSapSvHost": ipxSapSvHost,
       "ipxSapSvSocket": ipxSapSvSocket,
       "ipxSapSvInterface": ipxSapSvInterface,
       "ipxSapSvOrigin": ipxSapSvOrigin,
       "ipxSapSvType": ipxSapSvType,
       "ipxSapSvHops": ipxSapSvHops,
       "ipxSapSvRowStatus": ipxSapSvRowStatus,
       "ipxSapSvAge": ipxSapSvAge,
       "xIpxFilter": xIpxFilter,
       "ipxIfFilterTable": ipxIfFilterTable,
       "ipxIfFilterEntry": ipxIfFilterEntry,
       "ipxIfFilterIndex": ipxIfFilterIndex,
       "ipxIfFilterDestNetwork": ipxIfFilterDestNetwork,
       "ipxIfFilterDestNode": ipxIfFilterDestNode,
       "ipxIfFilterSourceNetwork": ipxIfFilterSourceNetwork,
       "ipxIfFilterSourceNode": ipxIfFilterSourceNode,
       "ipxIfFilterPacketType": ipxIfFilterPacketType,
       "ipxIfFilterAction": ipxIfFilterAction,
       "ipxIfFilterRowStatus": ipxIfFilterRowStatus,
       "ipxIfFilterStatusDestNetworkAll": ipxIfFilterStatusDestNetworkAll,
       "ipxIfFilterStatusDestNodeAll": ipxIfFilterStatusDestNodeAll,
       "ipxIfFilterStatusSourceNetworkAll": ipxIfFilterStatusSourceNetworkAll,
       "ipxIfFilterStatusSourceNodeAll": ipxIfFilterStatusSourceNodeAll,
       "ipxIfFilterStatusPacketTypeAll": ipxIfFilterStatusPacketTypeAll,
       "ipxIfRipFilterTable": ipxIfRipFilterTable,
       "ipxIfRipFilterEntry": ipxIfRipFilterEntry,
       "ipxIfRipFilterNetwork": ipxIfRipFilterNetwork,
       "ipxIfRipFilterType": ipxIfRipFilterType,
       "ipxIfRipFilterAction": ipxIfRipFilterAction,
       "ipxIfRipFilterRowStatus": ipxIfRipFilterRowStatus,
       "ipxIfRipFilterNetworkAll": ipxIfRipFilterNetworkAll,
       "ipxIfRipFilterHost": ipxIfRipFilterHost,
       "ipxIfSapFilterTable": ipxIfSapFilterTable,
       "ipxIfSapFilterEntry": ipxIfSapFilterEntry,
       "ipxIfSapFilterNetwork": ipxIfSapFilterNetwork,
       "ipxIfSapFilterType": ipxIfSapFilterType,
       "ipxIfSapFilterServiceType": ipxIfSapFilterServiceType,
       "ipxIfSapFilterAction": ipxIfSapFilterAction,
       "ipxIfSapFilterRowStatus": ipxIfSapFilterRowStatus,
       "ipxIfSapFilterNetworkAll": ipxIfSapFilterNetworkAll,
       "ipxIfSapFilterServiceTypeAll": ipxIfSapFilterServiceTypeAll,
       "ipxIfSapFilterName": ipxIfSapFilterName,
       "ipxIfSapFilterHost": ipxIfSapFilterHost,
       "xIpxPrinter": xIpxPrinter,
       "ipxPrinterPortTable": ipxPrinterPortTable,
       "ipxPrinterPortEntry": ipxPrinterPortEntry,
       "ipxPrinterPortIndex": ipxPrinterPortIndex,
       "ipxPrinterPortStatus": ipxPrinterPortStatus,
       "ipxPrinterPortServer": ipxPrinterPortServer,
       "ipxPrinterPortPrinter": ipxPrinterPortPrinter,
       "ipxTimeout": ipxTimeout,
       "ipxPrinterEthernet": ipxPrinterEthernet,
       "ipxPrinterMac": ipxPrinterMac,
       "ipxPrinterMac802-2": ipxPrinterMac802_2,
       "ipxPrinterMac802-2-Snap": ipxPrinterMac802_2_Snap}
)
