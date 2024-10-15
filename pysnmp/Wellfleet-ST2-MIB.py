# SNMP MIB module (Wellfleet-ST2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-ST2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:50 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfReservationProtocolGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfReservationProtocolGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfSt2Group_ObjectIdentity = ObjectIdentity
wfSt2Group = _WfSt2Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2)
)
_WfSt2BaseGroup_ObjectIdentity = ObjectIdentity
wfSt2BaseGroup = _WfSt2BaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 1)
)


class _WfSt2BaseDelete_Type(Integer32):
    """Custom type wfSt2BaseDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfSt2BaseDelete_Type.__name__ = "Integer32"
_WfSt2BaseDelete_Object = MibScalar
wfSt2BaseDelete = _WfSt2BaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 1, 1),
    _WfSt2BaseDelete_Type()
)
wfSt2BaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2BaseDelete.setStatus("mandatory")


class _WfSt2BaseDisable_Type(Integer32):
    """Custom type wfSt2BaseDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfSt2BaseDisable_Type.__name__ = "Integer32"
_WfSt2BaseDisable_Object = MibScalar
wfSt2BaseDisable = _WfSt2BaseDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 1, 2),
    _WfSt2BaseDisable_Type()
)
wfSt2BaseDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2BaseDisable.setStatus("mandatory")


class _WfSt2BaseState_Type(Integer32):
    """Custom type wfSt2BaseState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("initializing", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfSt2BaseState_Type.__name__ = "Integer32"
_WfSt2BaseState_Object = MibScalar
wfSt2BaseState = _WfSt2BaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 1, 3),
    _WfSt2BaseState_Type()
)
wfSt2BaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2BaseState.setStatus("mandatory")
_WfSt2BaseRoutingVers_Type = DisplayString
_WfSt2BaseRoutingVers_Object = MibScalar
wfSt2BaseRoutingVers = _WfSt2BaseRoutingVers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 1, 4),
    _WfSt2BaseRoutingVers_Type()
)
wfSt2BaseRoutingVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2BaseRoutingVers.setStatus("mandatory")


class _WfSt2BaseTunnelCapability_Type(Integer32):
    """Custom type wfSt2BaseTunnelCapability based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_WfSt2BaseTunnelCapability_Type.__name__ = "Integer32"
_WfSt2BaseTunnelCapability_Object = MibScalar
wfSt2BaseTunnelCapability = _WfSt2BaseTunnelCapability_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 1, 5),
    _WfSt2BaseTunnelCapability_Type()
)
wfSt2BaseTunnelCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2BaseTunnelCapability.setStatus("mandatory")


class _WfSt2BaseTunnelDisable_Type(Integer32):
    """Custom type wfSt2BaseTunnelDisable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfSt2BaseTunnelDisable_Type.__name__ = "Integer32"
_WfSt2BaseTunnelDisable_Object = MibScalar
wfSt2BaseTunnelDisable = _WfSt2BaseTunnelDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 1, 6),
    _WfSt2BaseTunnelDisable_Type()
)
wfSt2BaseTunnelDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2BaseTunnelDisable.setStatus("mandatory")
_WfSt2BaseAgentDBGMask_Type = Integer32
_WfSt2BaseAgentDBGMask_Object = MibScalar
wfSt2BaseAgentDBGMask = _WfSt2BaseAgentDBGMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 1, 7),
    _WfSt2BaseAgentDBGMask_Type()
)
wfSt2BaseAgentDBGMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2BaseAgentDBGMask.setStatus("mandatory")
_WfSt2BaseReservedParameter1_Type = Integer32
_WfSt2BaseReservedParameter1_Object = MibScalar
wfSt2BaseReservedParameter1 = _WfSt2BaseReservedParameter1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 1, 8),
    _WfSt2BaseReservedParameter1_Type()
)
wfSt2BaseReservedParameter1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2BaseReservedParameter1.setStatus("mandatory")
_WfSt2BaseReservedParameter2_Type = Integer32
_WfSt2BaseReservedParameter2_Object = MibScalar
wfSt2BaseReservedParameter2 = _WfSt2BaseReservedParameter2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 1, 9),
    _WfSt2BaseReservedParameter2_Type()
)
wfSt2BaseReservedParameter2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2BaseReservedParameter2.setStatus("mandatory")
_WfSt2CircuitTable_Object = MibTable
wfSt2CircuitTable = _WfSt2CircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wfSt2CircuitTable.setStatus("mandatory")
_WfSt2CircuitEntry_Object = MibTableRow
wfSt2CircuitEntry = _WfSt2CircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1)
)
wfSt2CircuitEntry.setIndexNames(
    (0, "Wellfleet-ST2-MIB", "wfSt2CircuitID"),
)
if mibBuilder.loadTexts:
    wfSt2CircuitEntry.setStatus("mandatory")


class _WfSt2CircuitDelete_Type(Integer32):
    """Custom type wfSt2CircuitDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfSt2CircuitDelete_Type.__name__ = "Integer32"
_WfSt2CircuitDelete_Object = MibTableColumn
wfSt2CircuitDelete = _WfSt2CircuitDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 1),
    _WfSt2CircuitDelete_Type()
)
wfSt2CircuitDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2CircuitDelete.setStatus("mandatory")


class _WfSt2CircuitDisable_Type(Integer32):
    """Custom type wfSt2CircuitDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfSt2CircuitDisable_Type.__name__ = "Integer32"
_WfSt2CircuitDisable_Object = MibTableColumn
wfSt2CircuitDisable = _WfSt2CircuitDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 2),
    _WfSt2CircuitDisable_Type()
)
wfSt2CircuitDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2CircuitDisable.setStatus("mandatory")


class _WfSt2CircuitCommonState_Type(Integer32):
    """Custom type wfSt2CircuitCommonState based on Integer32"""
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
        *(("down", 2),
          ("initializing", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfSt2CircuitCommonState_Type.__name__ = "Integer32"
_WfSt2CircuitCommonState_Object = MibTableColumn
wfSt2CircuitCommonState = _WfSt2CircuitCommonState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 3),
    _WfSt2CircuitCommonState_Type()
)
wfSt2CircuitCommonState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitCommonState.setStatus("mandatory")
_WfSt2CircuitID_Type = Integer32
_WfSt2CircuitID_Object = MibTableColumn
wfSt2CircuitID = _WfSt2CircuitID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 4),
    _WfSt2CircuitID_Type()
)
wfSt2CircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitID.setStatus("mandatory")


class _WfSt2CircuitCommonType_Type(Integer32):
    """Custom type wfSt2CircuitCommonType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              15,
              100,
              101,
              102,
              103,
              104)
        )
    )
    namedValues = NamedValues(
        *(("atm", 102),
          ("ethernet", 6),
          ("fddi", 15),
          ("fr", 101),
          ("ppp", 104),
          ("ring", 103),
          ("smds", 100),
          ("sync", 1))
    )


_WfSt2CircuitCommonType_Type.__name__ = "Integer32"
_WfSt2CircuitCommonType_Object = MibTableColumn
wfSt2CircuitCommonType = _WfSt2CircuitCommonType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 5),
    _WfSt2CircuitCommonType_Type()
)
wfSt2CircuitCommonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitCommonType.setStatus("mandatory")
_WfSt2CircuitIPAddress_Type = IpAddress
_WfSt2CircuitIPAddress_Object = MibTableColumn
wfSt2CircuitIPAddress = _WfSt2CircuitIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 6),
    _WfSt2CircuitIPAddress_Type()
)
wfSt2CircuitIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2CircuitIPAddress.setStatus("mandatory")


class _WfSt2CircuitTmoAccept_Type(Integer32):
    """Custom type wfSt2CircuitTmoAccept based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            10
        )
    )
    namedValues = NamedValues(
        ("taccdef", 10)
    )


_WfSt2CircuitTmoAccept_Type.__name__ = "Integer32"
_WfSt2CircuitTmoAccept_Object = MibTableColumn
wfSt2CircuitTmoAccept = _WfSt2CircuitTmoAccept_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 7),
    _WfSt2CircuitTmoAccept_Type()
)
wfSt2CircuitTmoAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2CircuitTmoAccept.setStatus("mandatory")


class _WfSt2CircuitRetryAccept_Type(Integer32):
    """Custom type wfSt2CircuitRetryAccept based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("raccdef", 3)
    )


_WfSt2CircuitRetryAccept_Type.__name__ = "Integer32"
_WfSt2CircuitRetryAccept_Object = MibTableColumn
wfSt2CircuitRetryAccept = _WfSt2CircuitRetryAccept_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 8),
    _WfSt2CircuitRetryAccept_Type()
)
wfSt2CircuitRetryAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2CircuitRetryAccept.setStatus("mandatory")


class _WfSt2CircuitTmoConnect_Type(Integer32):
    """Custom type wfSt2CircuitTmoConnect based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            10
        )
    )
    namedValues = NamedValues(
        ("tcondef", 10)
    )


_WfSt2CircuitTmoConnect_Type.__name__ = "Integer32"
_WfSt2CircuitTmoConnect_Object = MibTableColumn
wfSt2CircuitTmoConnect = _WfSt2CircuitTmoConnect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 9),
    _WfSt2CircuitTmoConnect_Type()
)
wfSt2CircuitTmoConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2CircuitTmoConnect.setStatus("mandatory")


class _WfSt2CircuitRetryConnect_Type(Integer32):
    """Custom type wfSt2CircuitRetryConnect based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("rcondef", 5)
    )


_WfSt2CircuitRetryConnect_Type.__name__ = "Integer32"
_WfSt2CircuitRetryConnect_Object = MibTableColumn
wfSt2CircuitRetryConnect = _WfSt2CircuitRetryConnect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 10),
    _WfSt2CircuitRetryConnect_Type()
)
wfSt2CircuitRetryConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2CircuitRetryConnect.setStatus("mandatory")


class _WfSt2CircuitTmoDisconnect_Type(Integer32):
    """Custom type wfSt2CircuitTmoDisconnect based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            10
        )
    )
    namedValues = NamedValues(
        ("tdiscondef", 10)
    )


_WfSt2CircuitTmoDisconnect_Type.__name__ = "Integer32"
_WfSt2CircuitTmoDisconnect_Object = MibTableColumn
wfSt2CircuitTmoDisconnect = _WfSt2CircuitTmoDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 11),
    _WfSt2CircuitTmoDisconnect_Type()
)
wfSt2CircuitTmoDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2CircuitTmoDisconnect.setStatus("mandatory")


class _WfSt2CircuitRetryDisconnect_Type(Integer32):
    """Custom type wfSt2CircuitRetryDisconnect based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("rdiscondef", 3)
    )


_WfSt2CircuitRetryDisconnect_Type.__name__ = "Integer32"
_WfSt2CircuitRetryDisconnect_Object = MibTableColumn
wfSt2CircuitRetryDisconnect = _WfSt2CircuitRetryDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 12),
    _WfSt2CircuitRetryDisconnect_Type()
)
wfSt2CircuitRetryDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2CircuitRetryDisconnect.setStatus("mandatory")


class _WfSt2CircuitTmoHidChange_Type(Integer32):
    """Custom type wfSt2CircuitTmoHidChange based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            10
        )
    )
    namedValues = NamedValues(
        ("thidchgdef", 10)
    )


_WfSt2CircuitTmoHidChange_Type.__name__ = "Integer32"
_WfSt2CircuitTmoHidChange_Object = MibTableColumn
wfSt2CircuitTmoHidChange = _WfSt2CircuitTmoHidChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 13),
    _WfSt2CircuitTmoHidChange_Type()
)
wfSt2CircuitTmoHidChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2CircuitTmoHidChange.setStatus("mandatory")


class _WfSt2CircuitRetryHidChange_Type(Integer32):
    """Custom type wfSt2CircuitRetryHidChange based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("rhidchgdef", 3)
    )


_WfSt2CircuitRetryHidChange_Type.__name__ = "Integer32"
_WfSt2CircuitRetryHidChange_Object = MibTableColumn
wfSt2CircuitRetryHidChange = _WfSt2CircuitRetryHidChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 14),
    _WfSt2CircuitRetryHidChange_Type()
)
wfSt2CircuitRetryHidChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2CircuitRetryHidChange.setStatus("mandatory")


class _WfSt2CircuitTmoRefuse_Type(Integer32):
    """Custom type wfSt2CircuitTmoRefuse based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            10
        )
    )
    namedValues = NamedValues(
        ("trefusedef", 10)
    )


_WfSt2CircuitTmoRefuse_Type.__name__ = "Integer32"
_WfSt2CircuitTmoRefuse_Object = MibTableColumn
wfSt2CircuitTmoRefuse = _WfSt2CircuitTmoRefuse_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 15),
    _WfSt2CircuitTmoRefuse_Type()
)
wfSt2CircuitTmoRefuse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2CircuitTmoRefuse.setStatus("mandatory")


class _WfSt2CircuitRetryRefuse_Type(Integer32):
    """Custom type wfSt2CircuitRetryRefuse based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("rrefusedef", 3)
    )


_WfSt2CircuitRetryRefuse_Type.__name__ = "Integer32"
_WfSt2CircuitRetryRefuse_Object = MibTableColumn
wfSt2CircuitRetryRefuse = _WfSt2CircuitRetryRefuse_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 16),
    _WfSt2CircuitRetryRefuse_Type()
)
wfSt2CircuitRetryRefuse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2CircuitRetryRefuse.setStatus("mandatory")


class _WfSt2CircuitTmoHello_Type(Integer32):
    """Custom type wfSt2CircuitTmoHello based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            10
        )
    )
    namedValues = NamedValues(
        ("thellodef", 10)
    )


_WfSt2CircuitTmoHello_Type.__name__ = "Integer32"
_WfSt2CircuitTmoHello_Object = MibTableColumn
wfSt2CircuitTmoHello = _WfSt2CircuitTmoHello_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 17),
    _WfSt2CircuitTmoHello_Type()
)
wfSt2CircuitTmoHello.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2CircuitTmoHello.setStatus("mandatory")


class _WfSt2CircuitRetryHello_Type(Integer32):
    """Custom type wfSt2CircuitRetryHello based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("rhellodef", 5)
    )


_WfSt2CircuitRetryHello_Type.__name__ = "Integer32"
_WfSt2CircuitRetryHello_Object = MibTableColumn
wfSt2CircuitRetryHello = _WfSt2CircuitRetryHello_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 18),
    _WfSt2CircuitRetryHello_Type()
)
wfSt2CircuitRetryHello.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2CircuitRetryHello.setStatus("mandatory")
_WfSt2CircuitMTU_Type = Integer32
_WfSt2CircuitMTU_Object = MibTableColumn
wfSt2CircuitMTU = _WfSt2CircuitMTU_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 19),
    _WfSt2CircuitMTU_Type()
)
wfSt2CircuitMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2CircuitMTU.setStatus("mandatory")
_WfSt2CircuitDBGMask_Type = Integer32
_WfSt2CircuitDBGMask_Object = MibTableColumn
wfSt2CircuitDBGMask = _WfSt2CircuitDBGMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 20),
    _WfSt2CircuitDBGMask_Type()
)
wfSt2CircuitDBGMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2CircuitDBGMask.setStatus("mandatory")


class _WfSt2CircuitHelloFailure_Type(Integer32):
    """Custom type wfSt2CircuitHelloFailure based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("preserve", 1))
    )


_WfSt2CircuitHelloFailure_Type.__name__ = "Integer32"
_WfSt2CircuitHelloFailure_Object = MibTableColumn
wfSt2CircuitHelloFailure = _WfSt2CircuitHelloFailure_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 21),
    _WfSt2CircuitHelloFailure_Type()
)
wfSt2CircuitHelloFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2CircuitHelloFailure.setStatus("mandatory")


class _WfSt2CircuitHidProposed_Type(Integer32):
    """Custom type wfSt2CircuitHidProposed based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locally", 1),
          ("remotely", 2))
    )


_WfSt2CircuitHidProposed_Type.__name__ = "Integer32"
_WfSt2CircuitHidProposed_Object = MibTableColumn
wfSt2CircuitHidProposed = _WfSt2CircuitHidProposed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 22),
    _WfSt2CircuitHidProposed_Type()
)
wfSt2CircuitHidProposed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2CircuitHidProposed.setStatus("mandatory")
_WfSt2CircuitBadStCksum_Type = Counter32
_WfSt2CircuitBadStCksum_Object = MibTableColumn
wfSt2CircuitBadStCksum = _WfSt2CircuitBadStCksum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 23),
    _WfSt2CircuitBadStCksum_Type()
)
wfSt2CircuitBadStCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitBadStCksum.setStatus("mandatory")
_WfSt2CircuitEncodeBadParm_Type = Counter32
_WfSt2CircuitEncodeBadParm_Object = MibTableColumn
wfSt2CircuitEncodeBadParm = _WfSt2CircuitEncodeBadParm_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 24),
    _WfSt2CircuitEncodeBadParm_Type()
)
wfSt2CircuitEncodeBadParm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitEncodeBadParm.setStatus("mandatory")
_WfSt2CircuitEncodeWrongParms_Type = Counter32
_WfSt2CircuitEncodeWrongParms_Object = MibTableColumn
wfSt2CircuitEncodeWrongParms = _WfSt2CircuitEncodeWrongParms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 25),
    _WfSt2CircuitEncodeWrongParms_Type()
)
wfSt2CircuitEncodeWrongParms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitEncodeWrongParms.setStatus("mandatory")
_WfSt2CircuitMsgInHidColl_Type = Counter32
_WfSt2CircuitMsgInHidColl_Object = MibTableColumn
wfSt2CircuitMsgInHidColl = _WfSt2CircuitMsgInHidColl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 26),
    _WfSt2CircuitMsgInHidColl_Type()
)
wfSt2CircuitMsgInHidColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitMsgInHidColl.setStatus("mandatory")
_WfSt2CircuitMsgInNoCon_Type = Counter32
_WfSt2CircuitMsgInNoCon_Object = MibTableColumn
wfSt2CircuitMsgInNoCon = _WfSt2CircuitMsgInNoCon_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 27),
    _WfSt2CircuitMsgInNoCon_Type()
)
wfSt2CircuitMsgInNoCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitMsgInNoCon.setStatus("mandatory")
_WfSt2CircuitNotSt2_Type = Counter32
_WfSt2CircuitNotSt2_Object = MibTableColumn
wfSt2CircuitNotSt2 = _WfSt2CircuitNotSt2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 28),
    _WfSt2CircuitNotSt2_Type()
)
wfSt2CircuitNotSt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitNotSt2.setStatus("mandatory")
_WfSt2CircuitParmMissing_Type = Counter32
_WfSt2CircuitParmMissing_Object = MibTableColumn
wfSt2CircuitParmMissing = _WfSt2CircuitParmMissing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 29),
    _WfSt2CircuitParmMissing_Type()
)
wfSt2CircuitParmMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitParmMissing.setStatus("mandatory")
_WfSt2CircuitScmpRefNum_Type = Counter32
_WfSt2CircuitScmpRefNum_Object = MibTableColumn
wfSt2CircuitScmpRefNum = _WfSt2CircuitScmpRefNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 30),
    _WfSt2CircuitScmpRefNum_Type()
)
wfSt2CircuitScmpRefNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitScmpRefNum.setStatus("mandatory")
_WfSt2CircuitScmp0rVlid_Type = Counter32
_WfSt2CircuitScmp0rVlid_Object = MibTableColumn
wfSt2CircuitScmp0rVlid = _WfSt2CircuitScmp0rVlid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 31),
    _WfSt2CircuitScmp0rVlid_Type()
)
wfSt2CircuitScmp0rVlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitScmp0rVlid.setStatus("mandatory")
_WfSt2CircuitScmp0sVlid_Type = Counter32
_WfSt2CircuitScmp0sVlid_Object = MibTableColumn
wfSt2CircuitScmp0sVlid = _WfSt2CircuitScmp0sVlid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 32),
    _WfSt2CircuitScmp0sVlid_Type()
)
wfSt2CircuitScmp0sVlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitScmp0sVlid.setStatus("mandatory")
_WfSt2CircuitScmpBadVlid_Type = Counter32
_WfSt2CircuitScmpBadVlid_Object = MibTableColumn
wfSt2CircuitScmpBadVlid = _WfSt2CircuitScmpBadVlid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 33),
    _WfSt2CircuitScmpBadVlid_Type()
)
wfSt2CircuitScmpBadVlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitScmpBadVlid.setStatus("mandatory")
_WfSt2CircuitScmpCksum_Type = Counter32
_WfSt2CircuitScmpCksum_Object = MibTableColumn
wfSt2CircuitScmpCksum = _WfSt2CircuitScmpCksum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 34),
    _WfSt2CircuitScmpCksum_Type()
)
wfSt2CircuitScmpCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitScmpCksum.setStatus("mandatory")
_WfSt2CircuitScmpFailedResources_Type = Counter32
_WfSt2CircuitScmpFailedResources_Object = MibTableColumn
wfSt2CircuitScmpFailedResources = _WfSt2CircuitScmpFailedResources_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 35),
    _WfSt2CircuitScmpFailedResources_Type()
)
wfSt2CircuitScmpFailedResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitScmpFailedResources.setStatus("mandatory")
_WfSt2CircuitScmpFailedRoute_Type = Counter32
_WfSt2CircuitScmpFailedRoute_Object = MibTableColumn
wfSt2CircuitScmpFailedRoute = _WfSt2CircuitScmpFailedRoute_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 36),
    _WfSt2CircuitScmpFailedRoute_Type()
)
wfSt2CircuitScmpFailedRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitScmpFailedRoute.setStatus("mandatory")
_WfSt2CircuitScmpLenInconsist_Type = Counter32
_WfSt2CircuitScmpLenInconsist_Object = MibTableColumn
wfSt2CircuitScmpLenInconsist = _WfSt2CircuitScmpLenInconsist_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 37),
    _WfSt2CircuitScmpLenInconsist_Type()
)
wfSt2CircuitScmpLenInconsist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitScmpLenInconsist.setStatus("mandatory")
_WfSt2CircuitScmpRxTimeOut_Type = Counter32
_WfSt2CircuitScmpRxTimeOut_Object = MibTableColumn
wfSt2CircuitScmpRxTimeOut = _WfSt2CircuitScmpRxTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 38),
    _WfSt2CircuitScmpRxTimeOut_Type()
)
wfSt2CircuitScmpRxTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitScmpRxTimeOut.setStatus("mandatory")
_WfSt2CircuitScmpXmtCnt_Type = Counter32
_WfSt2CircuitScmpXmtCnt_Object = MibTableColumn
wfSt2CircuitScmpXmtCnt = _WfSt2CircuitScmpXmtCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 39),
    _WfSt2CircuitScmpXmtCnt_Type()
)
wfSt2CircuitScmpXmtCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitScmpXmtCnt.setStatus("mandatory")
_WfSt2CircuitScmpRcvCnt_Type = Counter32
_WfSt2CircuitScmpRcvCnt_Object = MibTableColumn
wfSt2CircuitScmpRcvCnt = _WfSt2CircuitScmpRcvCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 40),
    _WfSt2CircuitScmpRcvCnt_Type()
)
wfSt2CircuitScmpRcvCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitScmpRcvCnt.setStatus("mandatory")
_WfSt2CircuitDataXmtCnt_Type = Counter32
_WfSt2CircuitDataXmtCnt_Object = MibTableColumn
wfSt2CircuitDataXmtCnt = _WfSt2CircuitDataXmtCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 41),
    _WfSt2CircuitDataXmtCnt_Type()
)
wfSt2CircuitDataXmtCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitDataXmtCnt.setStatus("mandatory")
_WfSt2CircuitDataRcvCnt_Type = Counter32
_WfSt2CircuitDataRcvCnt_Object = MibTableColumn
wfSt2CircuitDataRcvCnt = _WfSt2CircuitDataRcvCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 42),
    _WfSt2CircuitDataRcvCnt_Type()
)
wfSt2CircuitDataRcvCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitDataRcvCnt.setStatus("mandatory")
_WfSt2CircuitSt2StreamCnt_Type = Counter32
_WfSt2CircuitSt2StreamCnt_Object = MibTableColumn
wfSt2CircuitSt2StreamCnt = _WfSt2CircuitSt2StreamCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 43),
    _WfSt2CircuitSt2StreamCnt_Type()
)
wfSt2CircuitSt2StreamCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitSt2StreamCnt.setStatus("mandatory")
_WfSt2CircuitHelloXmtCnt_Type = Counter32
_WfSt2CircuitHelloXmtCnt_Object = MibTableColumn
wfSt2CircuitHelloXmtCnt = _WfSt2CircuitHelloXmtCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 44),
    _WfSt2CircuitHelloXmtCnt_Type()
)
wfSt2CircuitHelloXmtCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitHelloXmtCnt.setStatus("mandatory")
_WfSt2CircuitHelloRcvCnt_Type = Counter32
_WfSt2CircuitHelloRcvCnt_Object = MibTableColumn
wfSt2CircuitHelloRcvCnt = _WfSt2CircuitHelloRcvCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 45),
    _WfSt2CircuitHelloRcvCnt_Type()
)
wfSt2CircuitHelloRcvCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitHelloRcvCnt.setStatus("mandatory")
_WfSt2CircuitHelloRAckCnt_Type = Counter32
_WfSt2CircuitHelloRAckCnt_Object = MibTableColumn
wfSt2CircuitHelloRAckCnt = _WfSt2CircuitHelloRAckCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 46),
    _WfSt2CircuitHelloRAckCnt_Type()
)
wfSt2CircuitHelloRAckCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitHelloRAckCnt.setStatus("mandatory")
_WfSt2CircuitLbPoliceDrop_Type = Counter32
_WfSt2CircuitLbPoliceDrop_Object = MibTableColumn
wfSt2CircuitLbPoliceDrop = _WfSt2CircuitLbPoliceDrop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 47),
    _WfSt2CircuitLbPoliceDrop_Type()
)
wfSt2CircuitLbPoliceDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitLbPoliceDrop.setStatus("mandatory")
_WfSt2CircuitPbsDropCnt_Type = Counter32
_WfSt2CircuitPbsDropCnt_Object = MibTableColumn
wfSt2CircuitPbsDropCnt = _WfSt2CircuitPbsDropCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 48),
    _WfSt2CircuitPbsDropCnt_Type()
)
wfSt2CircuitPbsDropCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitPbsDropCnt.setStatus("mandatory")
_WfSt2CircuitOverDrop2Cnt_Type = Counter32
_WfSt2CircuitOverDrop2Cnt_Object = MibTableColumn
wfSt2CircuitOverDrop2Cnt = _WfSt2CircuitOverDrop2Cnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 49),
    _WfSt2CircuitOverDrop2Cnt_Type()
)
wfSt2CircuitOverDrop2Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitOverDrop2Cnt.setStatus("mandatory")
_WfSt2CircuitPktCnt_Type = Counter32
_WfSt2CircuitPktCnt_Object = MibTableColumn
wfSt2CircuitPktCnt = _WfSt2CircuitPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 50),
    _WfSt2CircuitPktCnt_Type()
)
wfSt2CircuitPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitPktCnt.setStatus("mandatory")
_WfSt2CircuitScmpXmt_Type = Counter32
_WfSt2CircuitScmpXmt_Object = MibTableColumn
wfSt2CircuitScmpXmt = _WfSt2CircuitScmpXmt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 51),
    _WfSt2CircuitScmpXmt_Type()
)
wfSt2CircuitScmpXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitScmpXmt.setStatus("mandatory")
_WfSt2CircuitScmpRcv_Type = Counter32
_WfSt2CircuitScmpRcv_Object = MibTableColumn
wfSt2CircuitScmpRcv = _WfSt2CircuitScmpRcv_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 52),
    _WfSt2CircuitScmpRcv_Type()
)
wfSt2CircuitScmpRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitScmpRcv.setStatus("mandatory")
_WfSt2CircuitBWAlloc_Type = Counter32
_WfSt2CircuitBWAlloc_Object = MibTableColumn
wfSt2CircuitBWAlloc = _WfSt2CircuitBWAlloc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 53),
    _WfSt2CircuitBWAlloc_Type()
)
wfSt2CircuitBWAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2CircuitBWAlloc.setStatus("mandatory")
_WfSt2CircuitRsvdParameter1_Type = Integer32
_WfSt2CircuitRsvdParameter1_Object = MibTableColumn
wfSt2CircuitRsvdParameter1 = _WfSt2CircuitRsvdParameter1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 54),
    _WfSt2CircuitRsvdParameter1_Type()
)
wfSt2CircuitRsvdParameter1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2CircuitRsvdParameter1.setStatus("mandatory")
_WfSt2CircuitRsvdParameter2_Type = Integer32
_WfSt2CircuitRsvdParameter2_Object = MibTableColumn
wfSt2CircuitRsvdParameter2 = _WfSt2CircuitRsvdParameter2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 2, 1, 55),
    _WfSt2CircuitRsvdParameter2_Type()
)
wfSt2CircuitRsvdParameter2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2CircuitRsvdParameter2.setStatus("mandatory")
_WfSt2NeighborTable_Object = MibTable
wfSt2NeighborTable = _WfSt2NeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3)
)
if mibBuilder.loadTexts:
    wfSt2NeighborTable.setStatus("mandatory")
_WfSt2NeighborEntry_Object = MibTableRow
wfSt2NeighborEntry = _WfSt2NeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1)
)
wfSt2NeighborEntry.setIndexNames(
    (0, "Wellfleet-ST2-MIB", "wfSt2NeighborNxtHopIPAddr"),
)
if mibBuilder.loadTexts:
    wfSt2NeighborEntry.setStatus("mandatory")


class _WfSt2NeighborDelete_Type(Integer32):
    """Custom type wfSt2NeighborDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfSt2NeighborDelete_Type.__name__ = "Integer32"
_WfSt2NeighborDelete_Object = MibTableColumn
wfSt2NeighborDelete = _WfSt2NeighborDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1, 1),
    _WfSt2NeighborDelete_Type()
)
wfSt2NeighborDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2NeighborDelete.setStatus("mandatory")


class _WfSt2NeighborDisable_Type(Integer32):
    """Custom type wfSt2NeighborDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfSt2NeighborDisable_Type.__name__ = "Integer32"
_WfSt2NeighborDisable_Object = MibTableColumn
wfSt2NeighborDisable = _WfSt2NeighborDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1, 2),
    _WfSt2NeighborDisable_Type()
)
wfSt2NeighborDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2NeighborDisable.setStatus("mandatory")
_WfSt2NeighborNxtHopIPAddr_Type = IpAddress
_WfSt2NeighborNxtHopIPAddr_Object = MibTableColumn
wfSt2NeighborNxtHopIPAddr = _WfSt2NeighborNxtHopIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1, 3),
    _WfSt2NeighborNxtHopIPAddr_Type()
)
wfSt2NeighborNxtHopIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSt2NeighborNxtHopIPAddr.setStatus("mandatory")


class _WfSt2NeighborRteExplr_Type(Integer32):
    """Custom type wfSt2NeighborRteExplr based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_WfSt2NeighborRteExplr_Type.__name__ = "Integer32"
_WfSt2NeighborRteExplr_Object = MibTableColumn
wfSt2NeighborRteExplr = _WfSt2NeighborRteExplr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1, 4),
    _WfSt2NeighborRteExplr_Type()
)
wfSt2NeighborRteExplr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2NeighborRteExplr.setStatus("mandatory")


class _WfSt2NeighborHelloProtocol_Type(Integer32):
    """Custom type wfSt2NeighborHelloProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("disable", 3),
          ("enable", 1))
    )


_WfSt2NeighborHelloProtocol_Type.__name__ = "Integer32"
_WfSt2NeighborHelloProtocol_Object = MibTableColumn
wfSt2NeighborHelloProtocol = _WfSt2NeighborHelloProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1, 5),
    _WfSt2NeighborHelloProtocol_Type()
)
wfSt2NeighborHelloProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2NeighborHelloProtocol.setStatus("mandatory")


class _WfSt2NeighborType_Type(Integer32):
    """Custom type wfSt2NeighborType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("tunnel", 2))
    )


_WfSt2NeighborType_Type.__name__ = "Integer32"
_WfSt2NeighborType_Object = MibTableColumn
wfSt2NeighborType = _WfSt2NeighborType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1, 6),
    _WfSt2NeighborType_Type()
)
wfSt2NeighborType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2NeighborType.setStatus("mandatory")


class _WfSt2NeighborPriorityLevel_Type(Integer32):
    """Custom type wfSt2NeighborPriorityLevel based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WfSt2NeighborPriorityLevel_Type.__name__ = "Integer32"
_WfSt2NeighborPriorityLevel_Object = MibTableColumn
wfSt2NeighborPriorityLevel = _WfSt2NeighborPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1, 7),
    _WfSt2NeighborPriorityLevel_Type()
)
wfSt2NeighborPriorityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2NeighborPriorityLevel.setStatus("mandatory")
_WfSt2NeighborRsvdParameter1_Type = Integer32
_WfSt2NeighborRsvdParameter1_Object = MibTableColumn
wfSt2NeighborRsvdParameter1 = _WfSt2NeighborRsvdParameter1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1, 8),
    _WfSt2NeighborRsvdParameter1_Type()
)
wfSt2NeighborRsvdParameter1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2NeighborRsvdParameter1.setStatus("mandatory")
_WfSt2NeighborRsvdParameter2_Type = Integer32
_WfSt2NeighborRsvdParameter2_Object = MibTableColumn
wfSt2NeighborRsvdParameter2 = _WfSt2NeighborRsvdParameter2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1, 9),
    _WfSt2NeighborRsvdParameter2_Type()
)
wfSt2NeighborRsvdParameter2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2NeighborRsvdParameter2.setStatus("mandatory")


class _WfSt2NeighborLocalIPAddress_Type(IpAddress):
    """Custom type wfSt2NeighborLocalIPAddress based on IpAddress"""
    defaultValue = 0


_WfSt2NeighborLocalIPAddress_Object = MibTableColumn
wfSt2NeighborLocalIPAddress = _WfSt2NeighborLocalIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1, 10),
    _WfSt2NeighborLocalIPAddress_Type()
)
wfSt2NeighborLocalIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2NeighborLocalIPAddress.setStatus("mandatory")


class _WfSt2NeighborTmoAccept_Type(Integer32):
    """Custom type wfSt2NeighborTmoAccept based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            10
        )
    )
    namedValues = NamedValues(
        ("taccdef", 10)
    )


_WfSt2NeighborTmoAccept_Type.__name__ = "Integer32"
_WfSt2NeighborTmoAccept_Object = MibTableColumn
wfSt2NeighborTmoAccept = _WfSt2NeighborTmoAccept_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1, 11),
    _WfSt2NeighborTmoAccept_Type()
)
wfSt2NeighborTmoAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2NeighborTmoAccept.setStatus("mandatory")


class _WfSt2NeighborRetryAccept_Type(Integer32):
    """Custom type wfSt2NeighborRetryAccept based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("raccdef", 3)
    )


_WfSt2NeighborRetryAccept_Type.__name__ = "Integer32"
_WfSt2NeighborRetryAccept_Object = MibTableColumn
wfSt2NeighborRetryAccept = _WfSt2NeighborRetryAccept_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1, 12),
    _WfSt2NeighborRetryAccept_Type()
)
wfSt2NeighborRetryAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2NeighborRetryAccept.setStatus("mandatory")


class _WfSt2NeighborTmoConnect_Type(Integer32):
    """Custom type wfSt2NeighborTmoConnect based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            10
        )
    )
    namedValues = NamedValues(
        ("tcondef", 10)
    )


_WfSt2NeighborTmoConnect_Type.__name__ = "Integer32"
_WfSt2NeighborTmoConnect_Object = MibTableColumn
wfSt2NeighborTmoConnect = _WfSt2NeighborTmoConnect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1, 13),
    _WfSt2NeighborTmoConnect_Type()
)
wfSt2NeighborTmoConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2NeighborTmoConnect.setStatus("mandatory")


class _WfSt2NeighborRetryConnect_Type(Integer32):
    """Custom type wfSt2NeighborRetryConnect based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("rcondef", 5)
    )


_WfSt2NeighborRetryConnect_Type.__name__ = "Integer32"
_WfSt2NeighborRetryConnect_Object = MibTableColumn
wfSt2NeighborRetryConnect = _WfSt2NeighborRetryConnect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1, 14),
    _WfSt2NeighborRetryConnect_Type()
)
wfSt2NeighborRetryConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2NeighborRetryConnect.setStatus("mandatory")


class _WfSt2NeighborTmoDisconnect_Type(Integer32):
    """Custom type wfSt2NeighborTmoDisconnect based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            10
        )
    )
    namedValues = NamedValues(
        ("tdiscondef", 10)
    )


_WfSt2NeighborTmoDisconnect_Type.__name__ = "Integer32"
_WfSt2NeighborTmoDisconnect_Object = MibTableColumn
wfSt2NeighborTmoDisconnect = _WfSt2NeighborTmoDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1, 15),
    _WfSt2NeighborTmoDisconnect_Type()
)
wfSt2NeighborTmoDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2NeighborTmoDisconnect.setStatus("mandatory")


class _WfSt2NeighborRetryDisconnect_Type(Integer32):
    """Custom type wfSt2NeighborRetryDisconnect based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("rdiscondef", 3)
    )


_WfSt2NeighborRetryDisconnect_Type.__name__ = "Integer32"
_WfSt2NeighborRetryDisconnect_Object = MibTableColumn
wfSt2NeighborRetryDisconnect = _WfSt2NeighborRetryDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1, 16),
    _WfSt2NeighborRetryDisconnect_Type()
)
wfSt2NeighborRetryDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2NeighborRetryDisconnect.setStatus("mandatory")


class _WfSt2NeighborTmoHidChange_Type(Integer32):
    """Custom type wfSt2NeighborTmoHidChange based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            10
        )
    )
    namedValues = NamedValues(
        ("thidchgdef", 10)
    )


_WfSt2NeighborTmoHidChange_Type.__name__ = "Integer32"
_WfSt2NeighborTmoHidChange_Object = MibTableColumn
wfSt2NeighborTmoHidChange = _WfSt2NeighborTmoHidChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1, 17),
    _WfSt2NeighborTmoHidChange_Type()
)
wfSt2NeighborTmoHidChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2NeighborTmoHidChange.setStatus("mandatory")


class _WfSt2NeighborRetryHidChange_Type(Integer32):
    """Custom type wfSt2NeighborRetryHidChange based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("rhidchgdef", 3)
    )


_WfSt2NeighborRetryHidChange_Type.__name__ = "Integer32"
_WfSt2NeighborRetryHidChange_Object = MibTableColumn
wfSt2NeighborRetryHidChange = _WfSt2NeighborRetryHidChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1, 18),
    _WfSt2NeighborRetryHidChange_Type()
)
wfSt2NeighborRetryHidChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2NeighborRetryHidChange.setStatus("mandatory")


class _WfSt2NeighborTmoRefuse_Type(Integer32):
    """Custom type wfSt2NeighborTmoRefuse based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            10
        )
    )
    namedValues = NamedValues(
        ("trefusedef", 10)
    )


_WfSt2NeighborTmoRefuse_Type.__name__ = "Integer32"
_WfSt2NeighborTmoRefuse_Object = MibTableColumn
wfSt2NeighborTmoRefuse = _WfSt2NeighborTmoRefuse_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1, 19),
    _WfSt2NeighborTmoRefuse_Type()
)
wfSt2NeighborTmoRefuse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2NeighborTmoRefuse.setStatus("mandatory")


class _WfSt2NeighborRetryRefuse_Type(Integer32):
    """Custom type wfSt2NeighborRetryRefuse based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("rrefusedef", 3)
    )


_WfSt2NeighborRetryRefuse_Type.__name__ = "Integer32"
_WfSt2NeighborRetryRefuse_Object = MibTableColumn
wfSt2NeighborRetryRefuse = _WfSt2NeighborRetryRefuse_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1, 20),
    _WfSt2NeighborRetryRefuse_Type()
)
wfSt2NeighborRetryRefuse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2NeighborRetryRefuse.setStatus("mandatory")


class _WfSt2NeighborTmoHello_Type(Integer32):
    """Custom type wfSt2NeighborTmoHello based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            10
        )
    )
    namedValues = NamedValues(
        ("thellodef", 10)
    )


_WfSt2NeighborTmoHello_Type.__name__ = "Integer32"
_WfSt2NeighborTmoHello_Object = MibTableColumn
wfSt2NeighborTmoHello = _WfSt2NeighborTmoHello_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1, 21),
    _WfSt2NeighborTmoHello_Type()
)
wfSt2NeighborTmoHello.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2NeighborTmoHello.setStatus("mandatory")


class _WfSt2NeighborRetryHello_Type(Integer32):
    """Custom type wfSt2NeighborRetryHello based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("rhellodef", 5)
    )


_WfSt2NeighborRetryHello_Type.__name__ = "Integer32"
_WfSt2NeighborRetryHello_Object = MibTableColumn
wfSt2NeighborRetryHello = _WfSt2NeighborRetryHello_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 1, 2, 3, 1, 22),
    _WfSt2NeighborRetryHello_Type()
)
wfSt2NeighborRetryHello.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSt2NeighborRetryHello.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-ST2-MIB",
    **{"wfSt2Group": wfSt2Group,
       "wfSt2BaseGroup": wfSt2BaseGroup,
       "wfSt2BaseDelete": wfSt2BaseDelete,
       "wfSt2BaseDisable": wfSt2BaseDisable,
       "wfSt2BaseState": wfSt2BaseState,
       "wfSt2BaseRoutingVers": wfSt2BaseRoutingVers,
       "wfSt2BaseTunnelCapability": wfSt2BaseTunnelCapability,
       "wfSt2BaseTunnelDisable": wfSt2BaseTunnelDisable,
       "wfSt2BaseAgentDBGMask": wfSt2BaseAgentDBGMask,
       "wfSt2BaseReservedParameter1": wfSt2BaseReservedParameter1,
       "wfSt2BaseReservedParameter2": wfSt2BaseReservedParameter2,
       "wfSt2CircuitTable": wfSt2CircuitTable,
       "wfSt2CircuitEntry": wfSt2CircuitEntry,
       "wfSt2CircuitDelete": wfSt2CircuitDelete,
       "wfSt2CircuitDisable": wfSt2CircuitDisable,
       "wfSt2CircuitCommonState": wfSt2CircuitCommonState,
       "wfSt2CircuitID": wfSt2CircuitID,
       "wfSt2CircuitCommonType": wfSt2CircuitCommonType,
       "wfSt2CircuitIPAddress": wfSt2CircuitIPAddress,
       "wfSt2CircuitTmoAccept": wfSt2CircuitTmoAccept,
       "wfSt2CircuitRetryAccept": wfSt2CircuitRetryAccept,
       "wfSt2CircuitTmoConnect": wfSt2CircuitTmoConnect,
       "wfSt2CircuitRetryConnect": wfSt2CircuitRetryConnect,
       "wfSt2CircuitTmoDisconnect": wfSt2CircuitTmoDisconnect,
       "wfSt2CircuitRetryDisconnect": wfSt2CircuitRetryDisconnect,
       "wfSt2CircuitTmoHidChange": wfSt2CircuitTmoHidChange,
       "wfSt2CircuitRetryHidChange": wfSt2CircuitRetryHidChange,
       "wfSt2CircuitTmoRefuse": wfSt2CircuitTmoRefuse,
       "wfSt2CircuitRetryRefuse": wfSt2CircuitRetryRefuse,
       "wfSt2CircuitTmoHello": wfSt2CircuitTmoHello,
       "wfSt2CircuitRetryHello": wfSt2CircuitRetryHello,
       "wfSt2CircuitMTU": wfSt2CircuitMTU,
       "wfSt2CircuitDBGMask": wfSt2CircuitDBGMask,
       "wfSt2CircuitHelloFailure": wfSt2CircuitHelloFailure,
       "wfSt2CircuitHidProposed": wfSt2CircuitHidProposed,
       "wfSt2CircuitBadStCksum": wfSt2CircuitBadStCksum,
       "wfSt2CircuitEncodeBadParm": wfSt2CircuitEncodeBadParm,
       "wfSt2CircuitEncodeWrongParms": wfSt2CircuitEncodeWrongParms,
       "wfSt2CircuitMsgInHidColl": wfSt2CircuitMsgInHidColl,
       "wfSt2CircuitMsgInNoCon": wfSt2CircuitMsgInNoCon,
       "wfSt2CircuitNotSt2": wfSt2CircuitNotSt2,
       "wfSt2CircuitParmMissing": wfSt2CircuitParmMissing,
       "wfSt2CircuitScmpRefNum": wfSt2CircuitScmpRefNum,
       "wfSt2CircuitScmp0rVlid": wfSt2CircuitScmp0rVlid,
       "wfSt2CircuitScmp0sVlid": wfSt2CircuitScmp0sVlid,
       "wfSt2CircuitScmpBadVlid": wfSt2CircuitScmpBadVlid,
       "wfSt2CircuitScmpCksum": wfSt2CircuitScmpCksum,
       "wfSt2CircuitScmpFailedResources": wfSt2CircuitScmpFailedResources,
       "wfSt2CircuitScmpFailedRoute": wfSt2CircuitScmpFailedRoute,
       "wfSt2CircuitScmpLenInconsist": wfSt2CircuitScmpLenInconsist,
       "wfSt2CircuitScmpRxTimeOut": wfSt2CircuitScmpRxTimeOut,
       "wfSt2CircuitScmpXmtCnt": wfSt2CircuitScmpXmtCnt,
       "wfSt2CircuitScmpRcvCnt": wfSt2CircuitScmpRcvCnt,
       "wfSt2CircuitDataXmtCnt": wfSt2CircuitDataXmtCnt,
       "wfSt2CircuitDataRcvCnt": wfSt2CircuitDataRcvCnt,
       "wfSt2CircuitSt2StreamCnt": wfSt2CircuitSt2StreamCnt,
       "wfSt2CircuitHelloXmtCnt": wfSt2CircuitHelloXmtCnt,
       "wfSt2CircuitHelloRcvCnt": wfSt2CircuitHelloRcvCnt,
       "wfSt2CircuitHelloRAckCnt": wfSt2CircuitHelloRAckCnt,
       "wfSt2CircuitLbPoliceDrop": wfSt2CircuitLbPoliceDrop,
       "wfSt2CircuitPbsDropCnt": wfSt2CircuitPbsDropCnt,
       "wfSt2CircuitOverDrop2Cnt": wfSt2CircuitOverDrop2Cnt,
       "wfSt2CircuitPktCnt": wfSt2CircuitPktCnt,
       "wfSt2CircuitScmpXmt": wfSt2CircuitScmpXmt,
       "wfSt2CircuitScmpRcv": wfSt2CircuitScmpRcv,
       "wfSt2CircuitBWAlloc": wfSt2CircuitBWAlloc,
       "wfSt2CircuitRsvdParameter1": wfSt2CircuitRsvdParameter1,
       "wfSt2CircuitRsvdParameter2": wfSt2CircuitRsvdParameter2,
       "wfSt2NeighborTable": wfSt2NeighborTable,
       "wfSt2NeighborEntry": wfSt2NeighborEntry,
       "wfSt2NeighborDelete": wfSt2NeighborDelete,
       "wfSt2NeighborDisable": wfSt2NeighborDisable,
       "wfSt2NeighborNxtHopIPAddr": wfSt2NeighborNxtHopIPAddr,
       "wfSt2NeighborRteExplr": wfSt2NeighborRteExplr,
       "wfSt2NeighborHelloProtocol": wfSt2NeighborHelloProtocol,
       "wfSt2NeighborType": wfSt2NeighborType,
       "wfSt2NeighborPriorityLevel": wfSt2NeighborPriorityLevel,
       "wfSt2NeighborRsvdParameter1": wfSt2NeighborRsvdParameter1,
       "wfSt2NeighborRsvdParameter2": wfSt2NeighborRsvdParameter2,
       "wfSt2NeighborLocalIPAddress": wfSt2NeighborLocalIPAddress,
       "wfSt2NeighborTmoAccept": wfSt2NeighborTmoAccept,
       "wfSt2NeighborRetryAccept": wfSt2NeighborRetryAccept,
       "wfSt2NeighborTmoConnect": wfSt2NeighborTmoConnect,
       "wfSt2NeighborRetryConnect": wfSt2NeighborRetryConnect,
       "wfSt2NeighborTmoDisconnect": wfSt2NeighborTmoDisconnect,
       "wfSt2NeighborRetryDisconnect": wfSt2NeighborRetryDisconnect,
       "wfSt2NeighborTmoHidChange": wfSt2NeighborTmoHidChange,
       "wfSt2NeighborRetryHidChange": wfSt2NeighborRetryHidChange,
       "wfSt2NeighborTmoRefuse": wfSt2NeighborTmoRefuse,
       "wfSt2NeighborRetryRefuse": wfSt2NeighborRetryRefuse,
       "wfSt2NeighborTmoHello": wfSt2NeighborTmoHello,
       "wfSt2NeighborRetryHello": wfSt2NeighborRetryHello}
)
