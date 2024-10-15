# SNMP MIB module (CTATM-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTATM-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:21 2024
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

(atmTrafficDescrParamIndex,
 atmVclVci,
 atmVclVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmTrafficDescrParamIndex",
    "atmVclVci",
    "atmVclVpi")

(AtmTrafficDescrParamIndex,) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmTrafficDescrParamIndex")

(ctATMConfig,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctATMConfig")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(leArpMacAddress,
 lecIndex) = mibBuilder.importSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    "leArpMacAddress",
    "lecIndex")

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



class AtmAddress(OctetString):
    """Custom type AtmAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtATMBaseConfig_ObjectIdentity = ObjectIdentity
ctATMBaseConfig = _CtATMBaseConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1)
)


class _CtATMPvcIfDef_Type(Integer32):
    """Custom type ctATMPvcIfDef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_CtATMPvcIfDef_Type.__name__ = "Integer32"
_CtATMPvcIfDef_Object = MibScalar
ctATMPvcIfDef = _CtATMPvcIfDef_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 1),
    _CtATMPvcIfDef_Type()
)
ctATMPvcIfDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMPvcIfDef.setStatus("deprecated")


class _CtATMLecIfDef_Type(Integer32):
    """Custom type ctATMLecIfDef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_CtATMLecIfDef_Type.__name__ = "Integer32"
_CtATMLecIfDef_Object = MibScalar
ctATMLecIfDef = _CtATMLecIfDef_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 2),
    _CtATMLecIfDef_Type()
)
ctATMLecIfDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMLecIfDef.setStatus("obsolete")
_CtATMDefApplicationTable_Object = MibTable
ctATMDefApplicationTable = _CtATMDefApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ctATMDefApplicationTable.setStatus("obsolete")
_CtATMDefApplicationEntry_Object = MibTableRow
ctATMDefApplicationEntry = _CtATMDefApplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 3, 1)
)
ctATMDefApplicationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctATMDefApplicationEntry.setStatus("obsolete")


class _CtATMDefApplicationIfIndex_Type(Integer32):
    """Custom type ctATMDefApplicationIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_CtATMDefApplicationIfIndex_Type.__name__ = "Integer32"
_CtATMDefApplicationIfIndex_Object = MibTableColumn
ctATMDefApplicationIfIndex = _CtATMDefApplicationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 3, 1, 1),
    _CtATMDefApplicationIfIndex_Type()
)
ctATMDefApplicationIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMDefApplicationIfIndex.setStatus("obsolete")


class _CtATMDefApplication_Type(Integer32):
    """Custom type ctATMDefApplication based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lane", 2),
          ("lane04", 1))
    )


_CtATMDefApplication_Type.__name__ = "Integer32"
_CtATMDefApplication_Object = MibTableColumn
ctATMDefApplication = _CtATMDefApplication_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 3, 1, 2),
    _CtATMDefApplication_Type()
)
ctATMDefApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMDefApplication.setStatus("obsolete")
_CtATMFramerStatusTable_Object = MibTable
ctATMFramerStatusTable = _CtATMFramerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ctATMFramerStatusTable.setStatus("obsolete")
_CtATMFramerStatusEntry_Object = MibTableRow
ctATMFramerStatusEntry = _CtATMFramerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 4, 1)
)
ctATMFramerStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctATMFramerStatusEntry.setStatus("obsolete")


class _CtATMFramerStatusIfIndex_Type(Integer32):
    """Custom type ctATMFramerStatusIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_CtATMFramerStatusIfIndex_Type.__name__ = "Integer32"
_CtATMFramerStatusIfIndex_Object = MibTableColumn
ctATMFramerStatusIfIndex = _CtATMFramerStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 4, 1, 1),
    _CtATMFramerStatusIfIndex_Type()
)
ctATMFramerStatusIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMFramerStatusIfIndex.setStatus("obsolete")


class _CtATMFramerStatus_Type(Integer32):
    """Custom type ctATMFramerStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CtATMFramerStatus_Type.__name__ = "Integer32"
_CtATMFramerStatus_Object = MibTableColumn
ctATMFramerStatus = _CtATMFramerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 4, 1, 2),
    _CtATMFramerStatus_Type()
)
ctATMFramerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMFramerStatus.setStatus("obsolete")
_CtATMLecArpMacTable_Object = MibTable
ctATMLecArpMacTable = _CtATMLecArpMacTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ctATMLecArpMacTable.setStatus("current")
_CtATMLecArpMacEntry_Object = MibTableRow
ctATMLecArpMacEntry = _CtATMLecArpMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 5, 1)
)
ctATMLecArpMacEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
    (0, "LAN-EMULATION-CLIENT-MIB", "leArpMacAddress"),
)
if mibBuilder.loadTexts:
    ctATMLecArpMacEntry.setStatus("current")


class _CtATMLecArpMacLecIndex_Type(Integer32):
    """Custom type ctATMLecArpMacLecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtATMLecArpMacLecIndex_Type.__name__ = "Integer32"
_CtATMLecArpMacLecIndex_Object = MibTableColumn
ctATMLecArpMacLecIndex = _CtATMLecArpMacLecIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 5, 1, 1),
    _CtATMLecArpMacLecIndex_Type()
)
ctATMLecArpMacLecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMLecArpMacLecIndex.setStatus("obsolete")


class _CtATMLecArpMacAddress_Type(OctetString):
    """Custom type ctATMLecArpMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CtATMLecArpMacAddress_Type.__name__ = "OctetString"
_CtATMLecArpMacAddress_Object = MibTableColumn
ctATMLecArpMacAddress = _CtATMLecArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 5, 1, 2),
    _CtATMLecArpMacAddress_Type()
)
ctATMLecArpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMLecArpMacAddress.setStatus("obsolete")
_CtATMLecArpMacElanName_Type = DisplayString
_CtATMLecArpMacElanName_Object = MibTableColumn
ctATMLecArpMacElanName = _CtATMLecArpMacElanName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 5, 1, 3),
    _CtATMLecArpMacElanName_Type()
)
ctATMLecArpMacElanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMLecArpMacElanName.setStatus("current")


class _CtATMLecArpMacVpi_Type(Integer32):
    """Custom type ctATMLecArpMacVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CtATMLecArpMacVpi_Type.__name__ = "Integer32"
_CtATMLecArpMacVpi_Object = MibTableColumn
ctATMLecArpMacVpi = _CtATMLecArpMacVpi_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 5, 1, 4),
    _CtATMLecArpMacVpi_Type()
)
ctATMLecArpMacVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMLecArpMacVpi.setStatus("current")


class _CtATMLecArpMacVci_Type(Integer32):
    """Custom type ctATMLecArpMacVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtATMLecArpMacVci_Type.__name__ = "Integer32"
_CtATMLecArpMacVci_Object = MibTableColumn
ctATMLecArpMacVci = _CtATMLecArpMacVci_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 5, 1, 5),
    _CtATMLecArpMacVci_Type()
)
ctATMLecArpMacVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMLecArpMacVci.setStatus("current")


class _CtATMLecArpMacATMAddress_Type(DisplayString):
    """Custom type ctATMLecArpMacATMAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_CtATMLecArpMacATMAddress_Type.__name__ = "DisplayString"
_CtATMLecArpMacATMAddress_Object = MibTableColumn
ctATMLecArpMacATMAddress = _CtATMLecArpMacATMAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 5, 1, 6),
    _CtATMLecArpMacATMAddress_Type()
)
ctATMLecArpMacATMAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMLecArpMacATMAddress.setStatus("current")
_CtATMPvcBwAllocTable_Object = MibTable
ctATMPvcBwAllocTable = _CtATMPvcBwAllocTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ctATMPvcBwAllocTable.setStatus("current")
_CtATMPvcBwAllocEntry_Object = MibTableRow
ctATMPvcBwAllocEntry = _CtATMPvcBwAllocEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 6, 1)
)
ctATMPvcBwAllocEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctATMPvcBwAllocEntry.setStatus("current")


class _CtATMPvcBwAllocPhysIface_Type(Integer32):
    """Custom type ctATMPvcBwAllocPhysIface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_CtATMPvcBwAllocPhysIface_Type.__name__ = "Integer32"
_CtATMPvcBwAllocPhysIface_Object = MibTableColumn
ctATMPvcBwAllocPhysIface = _CtATMPvcBwAllocPhysIface_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 6, 1, 1),
    _CtATMPvcBwAllocPhysIface_Type()
)
ctATMPvcBwAllocPhysIface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMPvcBwAllocPhysIface.setStatus("obsolete")


class _CtATMPvcBwAllocStatus_Type(Integer32):
    """Custom type ctATMPvcBwAllocStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 3),
          ("off", 2),
          ("on", 1))
    )


_CtATMPvcBwAllocStatus_Type.__name__ = "Integer32"
_CtATMPvcBwAllocStatus_Object = MibTableColumn
ctATMPvcBwAllocStatus = _CtATMPvcBwAllocStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 6, 1, 2),
    _CtATMPvcBwAllocStatus_Type()
)
ctATMPvcBwAllocStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMPvcBwAllocStatus.setStatus("current")


class _CtATMPvcBwAllocBandwidth_Type(Integer32):
    """Custom type ctATMPvcBwAllocBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtATMPvcBwAllocBandwidth_Type.__name__ = "Integer32"
_CtATMPvcBwAllocBandwidth_Object = MibTableColumn
ctATMPvcBwAllocBandwidth = _CtATMPvcBwAllocBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 6, 1, 3),
    _CtATMPvcBwAllocBandwidth_Type()
)
ctATMPvcBwAllocBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMPvcBwAllocBandwidth.setStatus("obsolete")
_CtATMDiscoveryElanTable_Object = MibTable
ctATMDiscoveryElanTable = _CtATMDiscoveryElanTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 7)
)
if mibBuilder.loadTexts:
    ctATMDiscoveryElanTable.setStatus("current")
_CtATMDiscoveryElanEntry_Object = MibTableRow
ctATMDiscoveryElanEntry = _CtATMDiscoveryElanEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 7, 1)
)
ctATMDiscoveryElanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CTATM-CONFIG-MIB", "ctATMDiscoveryElanIndex"),
)
if mibBuilder.loadTexts:
    ctATMDiscoveryElanEntry.setStatus("current")


class _CtATMDiscoveryElanIndex_Type(Integer32):
    """Custom type ctATMDiscoveryElanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CtATMDiscoveryElanIndex_Type.__name__ = "Integer32"
_CtATMDiscoveryElanIndex_Object = MibTableColumn
ctATMDiscoveryElanIndex = _CtATMDiscoveryElanIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 7, 1, 1),
    _CtATMDiscoveryElanIndex_Type()
)
ctATMDiscoveryElanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMDiscoveryElanIndex.setStatus("current")


class _CtATMDiscoveryElanName_Type(DisplayString):
    """Custom type ctATMDiscoveryElanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_CtATMDiscoveryElanName_Type.__name__ = "DisplayString"
_CtATMDiscoveryElanName_Object = MibTableColumn
ctATMDiscoveryElanName = _CtATMDiscoveryElanName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 7, 1, 2),
    _CtATMDiscoveryElanName_Type()
)
ctATMDiscoveryElanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMDiscoveryElanName.setStatus("current")


class _CtATMDiscoveryElanMode_Type(Integer32):
    """Custom type ctATMDiscoveryElanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ctATMDiscoveryElanMaster", 1),
          ("ctATMDiscoveryElanSlave", 2))
    )


_CtATMDiscoveryElanMode_Type.__name__ = "Integer32"
_CtATMDiscoveryElanMode_Object = MibTableColumn
ctATMDiscoveryElanMode = _CtATMDiscoveryElanMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 7, 1, 3),
    _CtATMDiscoveryElanMode_Type()
)
ctATMDiscoveryElanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMDiscoveryElanMode.setStatus("current")


class _CtATMDiscoveryElanStatus_Type(Integer32):
    """Custom type ctATMDiscoveryElanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ctATMDiscoveryElanEnabled", 1),
          ("ctATmDiscoveryElanDisabled", 2))
    )


_CtATMDiscoveryElanStatus_Type.__name__ = "Integer32"
_CtATMDiscoveryElanStatus_Object = MibTableColumn
ctATMDiscoveryElanStatus = _CtATMDiscoveryElanStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 7, 1, 4),
    _CtATMDiscoveryElanStatus_Type()
)
ctATMDiscoveryElanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMDiscoveryElanStatus.setStatus("current")


class _CtATMDiscoveryElanPhysIface_Type(Integer32):
    """Custom type ctATMDiscoveryElanPhysIface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_CtATMDiscoveryElanPhysIface_Type.__name__ = "Integer32"
_CtATMDiscoveryElanPhysIface_Object = MibTableColumn
ctATMDiscoveryElanPhysIface = _CtATMDiscoveryElanPhysIface_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 7, 1, 5),
    _CtATMDiscoveryElanPhysIface_Type()
)
ctATMDiscoveryElanPhysIface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMDiscoveryElanPhysIface.setStatus("obsolete")
_CtATMVclTable_Object = MibTable
ctATMVclTable = _CtATMVclTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 8)
)
if mibBuilder.loadTexts:
    ctATMVclTable.setStatus("current")
_CtATMVclEntry_Object = MibTableRow
ctATMVclEntry = _CtATMVclEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 8, 1)
)
ctATMVclEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    ctATMVclEntry.setStatus("current")


class _CtATMVclIfIndex_Type(Integer32):
    """Custom type ctATMVclIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_CtATMVclIfIndex_Type.__name__ = "Integer32"
_CtATMVclIfIndex_Object = MibTableColumn
ctATMVclIfIndex = _CtATMVclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 8, 1, 1),
    _CtATMVclIfIndex_Type()
)
ctATMVclIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMVclIfIndex.setStatus("obsolete")


class _CtATMVclVpi_Type(Integer32):
    """Custom type ctATMVclVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CtATMVclVpi_Type.__name__ = "Integer32"
_CtATMVclVpi_Object = MibTableColumn
ctATMVclVpi = _CtATMVclVpi_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 8, 1, 2),
    _CtATMVclVpi_Type()
)
ctATMVclVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMVclVpi.setStatus("obsolete")


class _CtATMVclVci_Type(Integer32):
    """Custom type ctATMVclVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtATMVclVci_Type.__name__ = "Integer32"
_CtATMVclVci_Object = MibTableColumn
ctATMVclVci = _CtATMVclVci_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 8, 1, 3),
    _CtATMVclVci_Type()
)
ctATMVclVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMVclVci.setStatus("obsolete")


class _CtATMVclVirtualIfIndex_Type(Integer32):
    """Custom type ctATMVclVirtualIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_CtATMVclVirtualIfIndex_Type.__name__ = "Integer32"
_CtATMVclVirtualIfIndex_Object = MibTableColumn
ctATMVclVirtualIfIndex = _CtATMVclVirtualIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 8, 1, 4),
    _CtATMVclVirtualIfIndex_Type()
)
ctATMVclVirtualIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMVclVirtualIfIndex.setStatus("current")


class _CtATMVclApplicationPort_Type(Integer32):
    """Custom type ctATMVclApplicationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_CtATMVclApplicationPort_Type.__name__ = "Integer32"
_CtATMVclApplicationPort_Object = MibTableColumn
ctATMVclApplicationPort = _CtATMVclApplicationPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 8, 1, 5),
    _CtATMVclApplicationPort_Type()
)
ctATMVclApplicationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMVclApplicationPort.setStatus("current")
_CtATMVclATMAddress_Type = AtmAddress
_CtATMVclATMAddress_Object = MibTableColumn
ctATMVclATMAddress = _CtATMVclATMAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 8, 1, 6),
    _CtATMVclATMAddress_Type()
)
ctATMVclATMAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMVclATMAddress.setStatus("current")


class _CtATMVclEncapsulationType_Type(Integer32):
    """Custom type ctATMVclEncapsulationType based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("atmVcSvcApp", 15),
          ("ilmi", 11),
          ("lanEmulationControl", 14),
          ("lanEmulationData", 13),
          ("llcEncapsulation", 7),
          ("multiProtocolOverATMControl", 17),
          ("multiProtocolOverATMData", 16),
          ("multiprotocolFrameRelaySscs", 8),
          ("other", 9),
          ("uni", 12),
          ("unknown", 10),
          ("vcMultiplexBridgedProtocol8023", 2),
          ("vcMultiplexBridgedProtocol8025", 3),
          ("vcMultiplexBridgedProtocol8026", 4),
          ("vcMultiplexLANemulation8023", 5),
          ("vcMultiplexLANemulation8025", 6),
          ("vcMultiplexRoutedProtocol", 1))
    )


_CtATMVclEncapsulationType_Type.__name__ = "Integer32"
_CtATMVclEncapsulationType_Object = MibTableColumn
ctATMVclEncapsulationType = _CtATMVclEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 1, 8, 1, 7),
    _CtATMVclEncapsulationType_Type()
)
ctATMVclEncapsulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMVclEncapsulationType.setStatus("current")
_CtATMPhysicalRedundancy_ObjectIdentity = ObjectIdentity
ctATMPhysicalRedundancy = _CtATMPhysicalRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 2)
)
_CtATMPhysicalRedundancyInterface_ObjectIdentity = ObjectIdentity
ctATMPhysicalRedundancyInterface = _CtATMPhysicalRedundancyInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 2, 1)
)
_CtATMPhyRedundTable_Object = MibTable
ctATMPhyRedundTable = _CtATMPhyRedundTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ctATMPhyRedundTable.setStatus("current")
_CtATMPhyRedundEntry_Object = MibTableRow
ctATMPhyRedundEntry = _CtATMPhyRedundEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 2, 1, 1, 1)
)
ctATMPhyRedundEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctATMPhyRedundEntry.setStatus("current")


class _CtATMPhyRedundIfIndex_Type(Integer32):
    """Custom type ctATMPhyRedundIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_CtATMPhyRedundIfIndex_Type.__name__ = "Integer32"
_CtATMPhyRedundIfIndex_Object = MibTableColumn
ctATMPhyRedundIfIndex = _CtATMPhyRedundIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 2, 1, 1, 1, 1),
    _CtATMPhyRedundIfIndex_Type()
)
ctATMPhyRedundIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMPhyRedundIfIndex.setStatus("obsolete")


class _CtATMPhyRedundPrimaryPort_Type(Integer32):
    """Custom type ctATMPhyRedundPrimaryPort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CtATMPhyRedundPrimaryPort_Type.__name__ = "Integer32"
_CtATMPhyRedundPrimaryPort_Object = MibTableColumn
ctATMPhyRedundPrimaryPort = _CtATMPhyRedundPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 2, 1, 1, 1, 2),
    _CtATMPhyRedundPrimaryPort_Type()
)
ctATMPhyRedundPrimaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMPhyRedundPrimaryPort.setStatus("current")


class _CtATMPhyRedundActivePort_Type(Integer32):
    """Custom type ctATMPhyRedundActivePort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CtATMPhyRedundActivePort_Type.__name__ = "Integer32"
_CtATMPhyRedundActivePort_Object = MibTableColumn
ctATMPhyRedundActivePort = _CtATMPhyRedundActivePort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 2, 1, 1, 1, 3),
    _CtATMPhyRedundActivePort_Type()
)
ctATMPhyRedundActivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMPhyRedundActivePort.setStatus("current")


class _CtATMPhyRedundStatus_Type(Integer32):
    """Custom type ctATMPhyRedundStatus based on Integer32"""
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


_CtATMPhyRedundStatus_Type.__name__ = "Integer32"
_CtATMPhyRedundStatus_Object = MibTableColumn
ctATMPhyRedundStatus = _CtATMPhyRedundStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 2, 1, 1, 1, 4),
    _CtATMPhyRedundStatus_Type()
)
ctATMPhyRedundStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMPhyRedundStatus.setStatus("current")


class _CtATMPhyRedundActivation_Type(Integer32):
    """Custom type ctATMPhyRedundActivation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_CtATMPhyRedundActivation_Type.__name__ = "Integer32"
_CtATMPhyRedundActivation_Object = MibTableColumn
ctATMPhyRedundActivation = _CtATMPhyRedundActivation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 2, 1, 1, 1, 5),
    _CtATMPhyRedundActivation_Type()
)
ctATMPhyRedundActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMPhyRedundActivation.setStatus("current")


class _CtATMPhyRedundPrimaryRevert_Type(Integer32):
    """Custom type ctATMPhyRedundPrimaryRevert based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_CtATMPhyRedundPrimaryRevert_Type.__name__ = "Integer32"
_CtATMPhyRedundPrimaryRevert_Object = MibTableColumn
ctATMPhyRedundPrimaryRevert = _CtATMPhyRedundPrimaryRevert_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 2, 1, 1, 1, 6),
    _CtATMPhyRedundPrimaryRevert_Type()
)
ctATMPhyRedundPrimaryRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMPhyRedundPrimaryRevert.setStatus("current")


class _CtATMPhyRedundPerformTest_Type(Integer32):
    """Custom type ctATMPhyRedundPerformTest based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("immediate", 3))
    )


_CtATMPhyRedundPerformTest_Type.__name__ = "Integer32"
_CtATMPhyRedundPerformTest_Object = MibTableColumn
ctATMPhyRedundPerformTest = _CtATMPhyRedundPerformTest_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 2, 1, 1, 1, 7),
    _CtATMPhyRedundPerformTest_Type()
)
ctATMPhyRedundPerformTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMPhyRedundPerformTest.setStatus("current")


class _CtATMPhyRedundTestTOD_Type(DisplayString):
    """Custom type ctATMPhyRedundTestTOD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_CtATMPhyRedundTestTOD_Type.__name__ = "DisplayString"
_CtATMPhyRedundTestTOD_Object = MibTableColumn
ctATMPhyRedundTestTOD = _CtATMPhyRedundTestTOD_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 2, 1, 1, 1, 8),
    _CtATMPhyRedundTestTOD_Type()
)
ctATMPhyRedundTestTOD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMPhyRedundTestTOD.setStatus("current")


class _CtATMPhyRedundTestResult_Type(Integer32):
    """Custom type ctATMPhyRedundTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              101,
              102,
              103,
              200,
              201,
              202,
              203)
        )
    )
    namedValues = NamedValues(
        *(("automaticAllPortsGood", 200),
          ("automaticPrimaryBadOthersBad", 203),
          ("automaticPrimaryBadOthersGood", 201),
          ("automaticPrimaryGoodOthersBad", 202),
          ("manualAllPortsGood", 100),
          ("manualPrimaryBadOthersBad", 103),
          ("manualPrimaryBadOthersGood", 101),
          ("manualPrimaryGoodOthersBad", 102))
    )


_CtATMPhyRedundTestResult_Type.__name__ = "Integer32"
_CtATMPhyRedundTestResult_Object = MibTableColumn
ctATMPhyRedundTestResult = _CtATMPhyRedundTestResult_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 2, 1, 1, 1, 9),
    _CtATMPhyRedundTestResult_Type()
)
ctATMPhyRedundTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMPhyRedundTestResult.setStatus("current")


class _CtATMPhyRedundReset_Type(Integer32):
    """Custom type ctATMPhyRedundReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_CtATMPhyRedundReset_Type.__name__ = "Integer32"
_CtATMPhyRedundReset_Object = MibTableColumn
ctATMPhyRedundReset = _CtATMPhyRedundReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 2, 1, 1, 1, 10),
    _CtATMPhyRedundReset_Type()
)
ctATMPhyRedundReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMPhyRedundReset.setStatus("current")
_CtATMIlmi_ObjectIdentity = ObjectIdentity
ctATMIlmi = _CtATMIlmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 3)
)
_CtATMIlmiTable_Object = MibTable
ctATMIlmiTable = _CtATMIlmiTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ctATMIlmiTable.setStatus("current")
_CtATMIlmiEntry_Object = MibTableRow
ctATMIlmiEntry = _CtATMIlmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 3, 1, 1)
)
ctATMIlmiEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctATMIlmiEntry.setStatus("current")


class _CtATMIlmiIfIndex_Type(Integer32):
    """Custom type ctATMIlmiIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_CtATMIlmiIfIndex_Type.__name__ = "Integer32"
_CtATMIlmiIfIndex_Object = MibTableColumn
ctATMIlmiIfIndex = _CtATMIlmiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 3, 1, 1, 1),
    _CtATMIlmiIfIndex_Type()
)
ctATMIlmiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMIlmiIfIndex.setStatus("obsolete")


class _CtATMIlmiStatus_Type(Integer32):
    """Custom type ctATMIlmiStatus based on Integer32"""
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
        *(("disable", 3),
          ("enable", 2),
          ("enableAutoConfigure", 1))
    )


_CtATMIlmiStatus_Type.__name__ = "Integer32"
_CtATMIlmiStatus_Object = MibTableColumn
ctATMIlmiStatus = _CtATMIlmiStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 3, 1, 1, 2),
    _CtATMIlmiStatus_Type()
)
ctATMIlmiStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMIlmiStatus.setStatus("current")
_CtATMIlmiAtmAddress_Type = AtmAddress
_CtATMIlmiAtmAddress_Object = MibTableColumn
ctATMIlmiAtmAddress = _CtATMIlmiAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 3, 1, 1, 3),
    _CtATMIlmiAtmAddress_Type()
)
ctATMIlmiAtmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMIlmiAtmAddress.setStatus("current")


class _CtATMIlmiState_Type(Integer32):
    """Custom type ctATMIlmiState based on Integer32"""
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
        *(("addressRegistration", 3),
          ("autoconfigure", 4),
          ("down", 5),
          ("estabConnectivity", 6),
          ("noLink", 7),
          ("obtainLECS", 8),
          ("unknown", 1),
          ("up", 2))
    )


_CtATMIlmiState_Type.__name__ = "Integer32"
_CtATMIlmiState_Object = MibTableColumn
ctATMIlmiState = _CtATMIlmiState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 3, 1, 1, 4),
    _CtATMIlmiState_Type()
)
ctATMIlmiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMIlmiState.setStatus("current")


class _CtATMIlmiRestart_Type(Integer32):
    """Custom type ctATMIlmiRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_CtATMIlmiRestart_Type.__name__ = "Integer32"
_CtATMIlmiRestart_Object = MibTableColumn
ctATMIlmiRestart = _CtATMIlmiRestart_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 3, 1, 1, 5),
    _CtATMIlmiRestart_Type()
)
ctATMIlmiRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMIlmiRestart.setStatus("current")
_CtATMSignalConfig_ObjectIdentity = ObjectIdentity
ctATMSignalConfig = _CtATMSignalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 4)
)
_CtATMSignalTable_Object = MibTable
ctATMSignalTable = _CtATMSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ctATMSignalTable.setStatus("current")
_CtATMSignalEntry_Object = MibTableRow
ctATMSignalEntry = _CtATMSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 4, 1, 1)
)
ctATMSignalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctATMSignalEntry.setStatus("current")


class _CtATMSignalIfIndex_Type(Integer32):
    """Custom type ctATMSignalIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_CtATMSignalIfIndex_Type.__name__ = "Integer32"
_CtATMSignalIfIndex_Object = MibTableColumn
ctATMSignalIfIndex = _CtATMSignalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 4, 1, 1, 1),
    _CtATMSignalIfIndex_Type()
)
ctATMSignalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMSignalIfIndex.setStatus("obsolete")


class _CtATMSignalStatus_Type(Integer32):
    """Custom type ctATMSignalStatus based on Integer32"""
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


_CtATMSignalStatus_Type.__name__ = "Integer32"
_CtATMSignalStatus_Object = MibTableColumn
ctATMSignalStatus = _CtATMSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 4, 1, 1, 2),
    _CtATMSignalStatus_Type()
)
ctATMSignalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMSignalStatus.setStatus("current")


class _CtATMSignalType_Type(Integer32):
    """Custom type ctATMSignalType based on Integer32"""
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
        *(("spans", 2),
          ("uni30", 3),
          ("uni31", 4),
          ("uni40", 5),
          ("unknown", 1))
    )


_CtATMSignalType_Type.__name__ = "Integer32"
_CtATMSignalType_Object = MibTableColumn
ctATMSignalType = _CtATMSignalType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 4, 1, 1, 3),
    _CtATMSignalType_Type()
)
ctATMSignalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMSignalType.setStatus("current")


class _CtATMSignalQ93Status_Type(Integer32):
    """Custom type ctATMSignalQ93Status based on Integer32"""
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


_CtATMSignalQ93Status_Type.__name__ = "Integer32"
_CtATMSignalQ93Status_Object = MibTableColumn
ctATMSignalQ93Status = _CtATMSignalQ93Status_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 4, 1, 1, 4),
    _CtATMSignalQ93Status_Type()
)
ctATMSignalQ93Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMSignalQ93Status.setStatus("current")


class _CtATMSignalQsaalStatus_Type(Integer32):
    """Custom type ctATMSignalQsaalStatus based on Integer32"""
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


_CtATMSignalQsaalStatus_Type.__name__ = "Integer32"
_CtATMSignalQsaalStatus_Object = MibTableColumn
ctATMSignalQsaalStatus = _CtATMSignalQsaalStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 4, 1, 1, 5),
    _CtATMSignalQsaalStatus_Type()
)
ctATMSignalQsaalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMSignalQsaalStatus.setStatus("current")


class _CtATMSignalRestart_Type(Integer32):
    """Custom type ctATMSignalRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_CtATMSignalRestart_Type.__name__ = "Integer32"
_CtATMSignalRestart_Object = MibTableColumn
ctATMSignalRestart = _CtATMSignalRestart_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 4, 1, 1, 6),
    _CtATMSignalRestart_Type()
)
ctATMSignalRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMSignalRestart.setStatus("current")
_CtATMLANEServices_ObjectIdentity = ObjectIdentity
ctATMLANEServices = _CtATMLANEServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 5)
)
_CtATMLANEInfoExtGroup_ObjectIdentity = ObjectIdentity
ctATMLANEInfoExtGroup = _CtATMLANEInfoExtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 6)
)
_CtATMLANEInfoExtStatusTable_Object = MibTable
ctATMLANEInfoExtStatusTable = _CtATMLANEInfoExtStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ctATMLANEInfoExtStatusTable.setStatus("current")
_CtATMLANEInfoExtStatusEntry_Object = MibTableRow
ctATMLANEInfoExtStatusEntry = _CtATMLANEInfoExtStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 6, 1, 1)
)
ctATMLANEInfoExtStatusEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
)
if mibBuilder.loadTexts:
    ctATMLANEInfoExtStatusEntry.setStatus("current")


class _CtATMLANEInfoExtStatusUpTime_Type(Integer32):
    """Custom type ctATMLANEInfoExtStatusUpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtATMLANEInfoExtStatusUpTime_Type.__name__ = "Integer32"
_CtATMLANEInfoExtStatusUpTime_Object = MibTableColumn
ctATMLANEInfoExtStatusUpTime = _CtATMLANEInfoExtStatusUpTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 6, 1, 1, 1),
    _CtATMLANEInfoExtStatusUpTime_Type()
)
ctATMLANEInfoExtStatusUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMLANEInfoExtStatusUpTime.setStatus("current")


class _CtATMLANEInfoExtStatus_Type(Integer32):
    """Custom type ctATMLANEInfoExtStatus based on Integer32"""
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
        *(("lecactive", 1),
          ("lecmemError", 7),
          ("lecnoATMaddr", 5),
          ("lecnoATMaddrnoUNI", 4),
          ("lecnoLink", 3),
          ("lecnoUNI", 6),
          ("lecnotInService", 2))
    )


_CtATMLANEInfoExtStatus_Type.__name__ = "Integer32"
_CtATMLANEInfoExtStatus_Object = MibTableColumn
ctATMLANEInfoExtStatus = _CtATMLANEInfoExtStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 6, 1, 1, 2),
    _CtATMLANEInfoExtStatus_Type()
)
ctATMLANEInfoExtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMLANEInfoExtStatus.setStatus("current")


class _CtATMLANEInfoExtStatusSendTopo_Type(Integer32):
    """Custom type ctATMLANEInfoExtStatusSendTopo based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CtATMLANEInfoExtStatusSendTopo_Type.__name__ = "Integer32"
_CtATMLANEInfoExtStatusSendTopo_Object = MibTableColumn
ctATMLANEInfoExtStatusSendTopo = _CtATMLANEInfoExtStatusSendTopo_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 6, 1, 1, 3),
    _CtATMLANEInfoExtStatusSendTopo_Type()
)
ctATMLANEInfoExtStatusSendTopo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMLANEInfoExtStatusSendTopo.setStatus("current")


class _CtATMLANEInfoExtStatusTimeLeft_Type(DisplayString):
    """Custom type ctATMLANEInfoExtStatusTimeLeft based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_CtATMLANEInfoExtStatusTimeLeft_Type.__name__ = "DisplayString"
_CtATMLANEInfoExtStatusTimeLeft_Object = MibTableColumn
ctATMLANEInfoExtStatusTimeLeft = _CtATMLANEInfoExtStatusTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 6, 1, 1, 4),
    _CtATMLANEInfoExtStatusTimeLeft_Type()
)
ctATMLANEInfoExtStatusTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMLANEInfoExtStatusTimeLeft.setStatus("current")


class _CtATMLANEInfoExtStatusNumQueues_Type(Integer32):
    """Custom type ctATMLANEInfoExtStatusNumQueues based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CtATMLANEInfoExtStatusNumQueues_Type.__name__ = "Integer32"
_CtATMLANEInfoExtStatusNumQueues_Object = MibTableColumn
ctATMLANEInfoExtStatusNumQueues = _CtATMLANEInfoExtStatusNumQueues_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 6, 1, 1, 5),
    _CtATMLANEInfoExtStatusNumQueues_Type()
)
ctATMLANEInfoExtStatusNumQueues.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMLANEInfoExtStatusNumQueues.setStatus("current")


class _CtATMLANEInfoExtStatusMaxNumQueues_Type(Integer32):
    """Custom type ctATMLANEInfoExtStatusMaxNumQueues based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CtATMLANEInfoExtStatusMaxNumQueues_Type.__name__ = "Integer32"
_CtATMLANEInfoExtStatusMaxNumQueues_Object = MibTableColumn
ctATMLANEInfoExtStatusMaxNumQueues = _CtATMLANEInfoExtStatusMaxNumQueues_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 6, 1, 1, 6),
    _CtATMLANEInfoExtStatusMaxNumQueues_Type()
)
ctATMLANEInfoExtStatusMaxNumQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMLANEInfoExtStatusMaxNumQueues.setStatus("current")
_CtATMLANEInfoExtTMTable_Object = MibTable
ctATMLANEInfoExtTMTable = _CtATMLANEInfoExtTMTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 6, 2)
)
if mibBuilder.loadTexts:
    ctATMLANEInfoExtTMTable.setStatus("current")
_CtATMLANEInfoExtTMEntry_Object = MibTableRow
ctATMLANEInfoExtTMEntry = _CtATMLANEInfoExtTMEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 6, 2, 1)
)
ctATMLANEInfoExtTMEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
    (0, "CTATM-CONFIG-MIB", "ctATMLANEInfoExtTMIndex"),
)
if mibBuilder.loadTexts:
    ctATMLANEInfoExtTMEntry.setStatus("current")
_CtATMLANEInfoExtTMIndex_Type = Integer32
_CtATMLANEInfoExtTMIndex_Object = MibTableColumn
ctATMLANEInfoExtTMIndex = _CtATMLANEInfoExtTMIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 6, 2, 1, 1),
    _CtATMLANEInfoExtTMIndex_Type()
)
ctATMLANEInfoExtTMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMLANEInfoExtTMIndex.setStatus("current")
_CtATMLANEInfoExtTMTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_CtATMLANEInfoExtTMTrafficDescrIndex_Object = MibTableColumn
ctATMLANEInfoExtTMTrafficDescrIndex = _CtATMLANEInfoExtTMTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 6, 2, 1, 2),
    _CtATMLANEInfoExtTMTrafficDescrIndex_Type()
)
ctATMLANEInfoExtTMTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMLANEInfoExtTMTrafficDescrIndex.setStatus("current")
_CtATMTrafficManagementGroup_ObjectIdentity = ObjectIdentity
ctATMTrafficManagementGroup = _CtATMTrafficManagementGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 7)
)
_CtATMTrafficDescrNameTable_Object = MibTable
ctATMTrafficDescrNameTable = _CtATMTrafficDescrNameTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ctATMTrafficDescrNameTable.setStatus("current")
_CtATMTrafficDescrNameEntry_Object = MibTableRow
ctATMTrafficDescrNameEntry = _CtATMTrafficDescrNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 7, 1, 1)
)
ctATMTrafficDescrNameEntry.setIndexNames(
    (0, "ATM-MIB", "atmTrafficDescrParamIndex"),
)
if mibBuilder.loadTexts:
    ctATMTrafficDescrNameEntry.setStatus("current")


class _CtATMTrafficDescrName_Type(DisplayString):
    """Custom type ctATMTrafficDescrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_CtATMTrafficDescrName_Type.__name__ = "DisplayString"
_CtATMTrafficDescrName_Object = MibTableColumn
ctATMTrafficDescrName = _CtATMTrafficDescrName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 7, 1, 1, 1),
    _CtATMTrafficDescrName_Type()
)
ctATMTrafficDescrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctATMTrafficDescrName.setStatus("current")
_CtATMTrafficServiceCategoriesSupportedTable_Object = MibTable
ctATMTrafficServiceCategoriesSupportedTable = _CtATMTrafficServiceCategoriesSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 7, 2)
)
if mibBuilder.loadTexts:
    ctATMTrafficServiceCategoriesSupportedTable.setStatus("current")
_CtATMTrafficServiceCategoriesSupportedEntry_Object = MibTableRow
ctATMTrafficServiceCategoriesSupportedEntry = _CtATMTrafficServiceCategoriesSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 7, 2, 1)
)
ctATMTrafficServiceCategoriesSupportedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctATMTrafficServiceCategoriesSupportedEntry.setStatus("current")


class _CtATMTrafficServiceCategoriesSupportedBitMask_Type(Bits):
    """Custom type ctATMTrafficServiceCategoriesSupportedBitMask based on Bits"""
    namedValues = NamedValues(
        *(("abr", 5),
          ("cbr", 2),
          ("other", 0),
          ("pvcBandwidthAllocation", 1),
          ("ubr", 4),
          ("vbrnrt", 3),
          ("vbrrt", 6))
    )

_CtATMTrafficServiceCategoriesSupportedBitMask_Type.__name__ = "Bits"
_CtATMTrafficServiceCategoriesSupportedBitMask_Object = MibTableColumn
ctATMTrafficServiceCategoriesSupportedBitMask = _CtATMTrafficServiceCategoriesSupportedBitMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 7, 2, 1, 1),
    _CtATMTrafficServiceCategoriesSupportedBitMask_Type()
)
ctATMTrafficServiceCategoriesSupportedBitMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMTrafficServiceCategoriesSupportedBitMask.setStatus("current")


class _CtATMTrafficManagementAllocBandwidth_Type(Integer32):
    """Custom type ctATMTrafficManagementAllocBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CtATMTrafficManagementAllocBandwidth_Type.__name__ = "Integer32"
_CtATMTrafficManagementAllocBandwidth_Object = MibTableColumn
ctATMTrafficManagementAllocBandwidth = _CtATMTrafficManagementAllocBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1, 7, 2, 1, 2),
    _CtATMTrafficManagementAllocBandwidth_Type()
)
ctATMTrafficManagementAllocBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctATMTrafficManagementAllocBandwidth.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTATM-CONFIG-MIB",
    **{"AtmAddress": AtmAddress,
       "ctATMBaseConfig": ctATMBaseConfig,
       "ctATMPvcIfDef": ctATMPvcIfDef,
       "ctATMLecIfDef": ctATMLecIfDef,
       "ctATMDefApplicationTable": ctATMDefApplicationTable,
       "ctATMDefApplicationEntry": ctATMDefApplicationEntry,
       "ctATMDefApplicationIfIndex": ctATMDefApplicationIfIndex,
       "ctATMDefApplication": ctATMDefApplication,
       "ctATMFramerStatusTable": ctATMFramerStatusTable,
       "ctATMFramerStatusEntry": ctATMFramerStatusEntry,
       "ctATMFramerStatusIfIndex": ctATMFramerStatusIfIndex,
       "ctATMFramerStatus": ctATMFramerStatus,
       "ctATMLecArpMacTable": ctATMLecArpMacTable,
       "ctATMLecArpMacEntry": ctATMLecArpMacEntry,
       "ctATMLecArpMacLecIndex": ctATMLecArpMacLecIndex,
       "ctATMLecArpMacAddress": ctATMLecArpMacAddress,
       "ctATMLecArpMacElanName": ctATMLecArpMacElanName,
       "ctATMLecArpMacVpi": ctATMLecArpMacVpi,
       "ctATMLecArpMacVci": ctATMLecArpMacVci,
       "ctATMLecArpMacATMAddress": ctATMLecArpMacATMAddress,
       "ctATMPvcBwAllocTable": ctATMPvcBwAllocTable,
       "ctATMPvcBwAllocEntry": ctATMPvcBwAllocEntry,
       "ctATMPvcBwAllocPhysIface": ctATMPvcBwAllocPhysIface,
       "ctATMPvcBwAllocStatus": ctATMPvcBwAllocStatus,
       "ctATMPvcBwAllocBandwidth": ctATMPvcBwAllocBandwidth,
       "ctATMDiscoveryElanTable": ctATMDiscoveryElanTable,
       "ctATMDiscoveryElanEntry": ctATMDiscoveryElanEntry,
       "ctATMDiscoveryElanIndex": ctATMDiscoveryElanIndex,
       "ctATMDiscoveryElanName": ctATMDiscoveryElanName,
       "ctATMDiscoveryElanMode": ctATMDiscoveryElanMode,
       "ctATMDiscoveryElanStatus": ctATMDiscoveryElanStatus,
       "ctATMDiscoveryElanPhysIface": ctATMDiscoveryElanPhysIface,
       "ctATMVclTable": ctATMVclTable,
       "ctATMVclEntry": ctATMVclEntry,
       "ctATMVclIfIndex": ctATMVclIfIndex,
       "ctATMVclVpi": ctATMVclVpi,
       "ctATMVclVci": ctATMVclVci,
       "ctATMVclVirtualIfIndex": ctATMVclVirtualIfIndex,
       "ctATMVclApplicationPort": ctATMVclApplicationPort,
       "ctATMVclATMAddress": ctATMVclATMAddress,
       "ctATMVclEncapsulationType": ctATMVclEncapsulationType,
       "ctATMPhysicalRedundancy": ctATMPhysicalRedundancy,
       "ctATMPhysicalRedundancyInterface": ctATMPhysicalRedundancyInterface,
       "ctATMPhyRedundTable": ctATMPhyRedundTable,
       "ctATMPhyRedundEntry": ctATMPhyRedundEntry,
       "ctATMPhyRedundIfIndex": ctATMPhyRedundIfIndex,
       "ctATMPhyRedundPrimaryPort": ctATMPhyRedundPrimaryPort,
       "ctATMPhyRedundActivePort": ctATMPhyRedundActivePort,
       "ctATMPhyRedundStatus": ctATMPhyRedundStatus,
       "ctATMPhyRedundActivation": ctATMPhyRedundActivation,
       "ctATMPhyRedundPrimaryRevert": ctATMPhyRedundPrimaryRevert,
       "ctATMPhyRedundPerformTest": ctATMPhyRedundPerformTest,
       "ctATMPhyRedundTestTOD": ctATMPhyRedundTestTOD,
       "ctATMPhyRedundTestResult": ctATMPhyRedundTestResult,
       "ctATMPhyRedundReset": ctATMPhyRedundReset,
       "ctATMIlmi": ctATMIlmi,
       "ctATMIlmiTable": ctATMIlmiTable,
       "ctATMIlmiEntry": ctATMIlmiEntry,
       "ctATMIlmiIfIndex": ctATMIlmiIfIndex,
       "ctATMIlmiStatus": ctATMIlmiStatus,
       "ctATMIlmiAtmAddress": ctATMIlmiAtmAddress,
       "ctATMIlmiState": ctATMIlmiState,
       "ctATMIlmiRestart": ctATMIlmiRestart,
       "ctATMSignalConfig": ctATMSignalConfig,
       "ctATMSignalTable": ctATMSignalTable,
       "ctATMSignalEntry": ctATMSignalEntry,
       "ctATMSignalIfIndex": ctATMSignalIfIndex,
       "ctATMSignalStatus": ctATMSignalStatus,
       "ctATMSignalType": ctATMSignalType,
       "ctATMSignalQ93Status": ctATMSignalQ93Status,
       "ctATMSignalQsaalStatus": ctATMSignalQsaalStatus,
       "ctATMSignalRestart": ctATMSignalRestart,
       "ctATMLANEServices": ctATMLANEServices,
       "ctATMLANEInfoExtGroup": ctATMLANEInfoExtGroup,
       "ctATMLANEInfoExtStatusTable": ctATMLANEInfoExtStatusTable,
       "ctATMLANEInfoExtStatusEntry": ctATMLANEInfoExtStatusEntry,
       "ctATMLANEInfoExtStatusUpTime": ctATMLANEInfoExtStatusUpTime,
       "ctATMLANEInfoExtStatus": ctATMLANEInfoExtStatus,
       "ctATMLANEInfoExtStatusSendTopo": ctATMLANEInfoExtStatusSendTopo,
       "ctATMLANEInfoExtStatusTimeLeft": ctATMLANEInfoExtStatusTimeLeft,
       "ctATMLANEInfoExtStatusNumQueues": ctATMLANEInfoExtStatusNumQueues,
       "ctATMLANEInfoExtStatusMaxNumQueues": ctATMLANEInfoExtStatusMaxNumQueues,
       "ctATMLANEInfoExtTMTable": ctATMLANEInfoExtTMTable,
       "ctATMLANEInfoExtTMEntry": ctATMLANEInfoExtTMEntry,
       "ctATMLANEInfoExtTMIndex": ctATMLANEInfoExtTMIndex,
       "ctATMLANEInfoExtTMTrafficDescrIndex": ctATMLANEInfoExtTMTrafficDescrIndex,
       "ctATMTrafficManagementGroup": ctATMTrafficManagementGroup,
       "ctATMTrafficDescrNameTable": ctATMTrafficDescrNameTable,
       "ctATMTrafficDescrNameEntry": ctATMTrafficDescrNameEntry,
       "ctATMTrafficDescrName": ctATMTrafficDescrName,
       "ctATMTrafficServiceCategoriesSupportedTable": ctATMTrafficServiceCategoriesSupportedTable,
       "ctATMTrafficServiceCategoriesSupportedEntry": ctATMTrafficServiceCategoriesSupportedEntry,
       "ctATMTrafficServiceCategoriesSupportedBitMask": ctATMTrafficServiceCategoriesSupportedBitMask,
       "ctATMTrafficManagementAllocBandwidth": ctATMTrafficManagementAllocBandwidth}
)
