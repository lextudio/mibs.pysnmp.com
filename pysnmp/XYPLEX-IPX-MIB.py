# SNMP MIB module (XYPLEX-IPX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYPLEX-IPX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:51 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Xyplex_ObjectIdentity = ObjectIdentity
xyplex = _Xyplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33)
)
_Ipx_ObjectIdentity = ObjectIdentity
ipx = _Ipx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 15)
)
_IpxSystem_ObjectIdentity = ObjectIdentity
ipxSystem = _IpxSystem_ObjectIdentity(
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
_IpxIf_ObjectIdentity = ObjectIdentity
ipxIf = _IpxIf_ObjectIdentity(
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
    (0, "XYPLEX-IPX-MIB", "ipxIfIndex"),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("ieee8022", 2))
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
_IpxNetbios_ObjectIdentity = ObjectIdentity
ipxNetbios = _IpxNetbios_ObjectIdentity(
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
    (0, "XYPLEX-IPX-MIB", "ipxNetbiosIfIndex"),
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
_IpxRip_ObjectIdentity = ObjectIdentity
ipxRip = _IpxRip_ObjectIdentity(
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
    (0, "XYPLEX-IPX-MIB", "ipxRipIfIndex"),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
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
    (0, "XYPLEX-IPX-MIB", "ipxRipNetwork"),
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
_IpxSap_ObjectIdentity = ObjectIdentity
ipxSap = _IpxSap_ObjectIdentity(
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
    (0, "XYPLEX-IPX-MIB", "ipxSapIfIndex"),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
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
    (0, "XYPLEX-IPX-MIB", "ipxSapName"),
    (0, "XYPLEX-IPX-MIB", "ipxSapType"),
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

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYPLEX-IPX-MIB",
    **{"xyplex": xyplex,
       "ipx": ipx,
       "ipxSystem": ipxSystem,
       "ipxRouting": ipxRouting,
       "ipxIf": ipxIf,
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
       "ipxNetbios": ipxNetbios,
       "ipxNetbiosHopLimit": ipxNetbiosHopLimit,
       "ipxNetbiosIfTable": ipxNetbiosIfTable,
       "ipxNetbiosIfEntry": ipxNetbiosIfEntry,
       "ipxNetbiosIfIndex": ipxNetbiosIfIndex,
       "ipxIfNetbiosForwarding": ipxIfNetbiosForwarding,
       "ipxIfNetbiosIn": ipxIfNetbiosIn,
       "ipxIfNetbiosOut": ipxIfNetbiosOut,
       "ipxRip": ipxRip,
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
       "ipxSap": ipxSap,
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
       "ipxSapAge": ipxSapAge}
)
