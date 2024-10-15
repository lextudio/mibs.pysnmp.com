# SNMP MIB module (PROPLANE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PROPLANE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:50 2024
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

(lannet,) = mibBuilder.importSymbols(
    "GEN-MIB",
    "lannet")

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





class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PropLane_ObjectIdentity = ObjectIdentity
propLane = _PropLane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 34)
)
_PropLaneMgmtLEC_ObjectIdentity = ObjectIdentity
propLaneMgmtLEC = _PropLaneMgmtLEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 34, 1)
)
_PropLaneMgmtLECCurrentAddress_Type = MacAddress
_PropLaneMgmtLECCurrentAddress_Object = MibScalar
propLaneMgmtLECCurrentAddress = _PropLaneMgmtLECCurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 1, 1),
    _PropLaneMgmtLECCurrentAddress_Type()
)
propLaneMgmtLECCurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneMgmtLECCurrentAddress.setStatus("mandatory")
_PropLaneMgmtLECIfIndexMap_Type = Integer32
_PropLaneMgmtLECIfIndexMap_Object = MibScalar
propLaneMgmtLECIfIndexMap = _PropLaneMgmtLECIfIndexMap_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 1, 2),
    _PropLaneMgmtLECIfIndexMap_Type()
)
propLaneMgmtLECIfIndexMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneMgmtLECIfIndexMap.setStatus("mandatory")
_PropLaneMgmtLECLecIndexMap_Type = Integer32
_PropLaneMgmtLECLecIndexMap_Object = MibScalar
propLaneMgmtLECLecIndexMap = _PropLaneMgmtLECLecIndexMap_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 1, 3),
    _PropLaneMgmtLECLecIndexMap_Type()
)
propLaneMgmtLECLecIndexMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneMgmtLECLecIndexMap.setStatus("mandatory")
_PropLaneElan_ObjectIdentity = ObjectIdentity
propLaneElan = _PropLaneElan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 34, 2)
)
_PropLaneElanConfTable_Object = MibTable
propLaneElanConfTable = _PropLaneElanConfTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 2, 1)
)
if mibBuilder.loadTexts:
    propLaneElanConfTable.setStatus("mandatory")
_PropLaneElanConfEntry_Object = MibTableRow
propLaneElanConfEntry = _PropLaneElanConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 2, 1, 1)
)
propLaneElanConfEntry.setIndexNames(
    (0, "PROPLANE-MIB", "propLaneElanConfIndex"),
)
if mibBuilder.loadTexts:
    propLaneElanConfEntry.setStatus("mandatory")
_PropLaneElanConfIndex_Type = Integer32
_PropLaneElanConfIndex_Object = MibTableColumn
propLaneElanConfIndex = _PropLaneElanConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 2, 1, 1, 1),
    _PropLaneElanConfIndex_Type()
)
propLaneElanConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneElanConfIndex.setStatus("mandatory")


class _PropLaneElanSecurity_Type(Integer32):
    """Custom type propLaneElanSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_PropLaneElanSecurity_Type.__name__ = "Integer32"
_PropLaneElanSecurity_Object = MibTableColumn
propLaneElanSecurity = _PropLaneElanSecurity_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 2, 1, 1, 2),
    _PropLaneElanSecurity_Type()
)
propLaneElanSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    propLaneElanSecurity.setStatus("mandatory")


class _PropLaneElanLesDiscovery_Type(Integer32):
    """Custom type propLaneElanLesDiscovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_PropLaneElanLesDiscovery_Type.__name__ = "Integer32"
_PropLaneElanLesDiscovery_Object = MibTableColumn
propLaneElanLesDiscovery = _PropLaneElanLesDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 2, 1, 1, 3),
    _PropLaneElanLesDiscovery_Type()
)
propLaneElanLesDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    propLaneElanLesDiscovery.setStatus("mandatory")


class _PropLaneElanLesRgstrType_Type(Integer32):
    """Custom type propLaneElanLesRgstrType based on Integer32"""
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
        *(("autosense", 1),
          ("distributed", 4),
          ("resilient", 3),
          ("single", 2))
    )


_PropLaneElanLesRgstrType_Type.__name__ = "Integer32"
_PropLaneElanLesRgstrType_Object = MibTableColumn
propLaneElanLesRgstrType = _PropLaneElanLesRgstrType_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 2, 1, 1, 4),
    _PropLaneElanLesRgstrType_Type()
)
propLaneElanLesRgstrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    propLaneElanLesRgstrType.setStatus("mandatory")


class _PropLaneElanLesActualRgstrType_Type(Integer32):
    """Custom type propLaneElanLesActualRgstrType based on Integer32"""
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
        *(("distrib", 4),
          ("none", 1),
          ("resilient", 3),
          ("single", 2))
    )


_PropLaneElanLesActualRgstrType_Type.__name__ = "Integer32"
_PropLaneElanLesActualRgstrType_Object = MibTableColumn
propLaneElanLesActualRgstrType = _PropLaneElanLesActualRgstrType_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 2, 1, 1, 5),
    _PropLaneElanLesActualRgstrType_Type()
)
propLaneElanLesActualRgstrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneElanLesActualRgstrType.setStatus("mandatory")


class _PropLaneElanMaximumActiveLes_Type(Integer32):
    """Custom type propLaneElanMaximumActiveLes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_PropLaneElanMaximumActiveLes_Type.__name__ = "Integer32"
_PropLaneElanMaximumActiveLes_Object = MibTableColumn
propLaneElanMaximumActiveLes = _PropLaneElanMaximumActiveLes_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 2, 1, 1, 6),
    _PropLaneElanMaximumActiveLes_Type()
)
propLaneElanMaximumActiveLes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    propLaneElanMaximumActiveLes.setStatus("mandatory")


class _PropLaneElanLesAddrForm_Type(Integer32):
    """Custom type propLaneElanLesAddrForm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("groupAddr", 1),
          ("longMatch", 3),
          ("roundRobin", 2))
    )


_PropLaneElanLesAddrForm_Type.__name__ = "Integer32"
_PropLaneElanLesAddrForm_Object = MibTableColumn
propLaneElanLesAddrForm = _PropLaneElanLesAddrForm_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 2, 1, 1, 7),
    _PropLaneElanLesAddrForm_Type()
)
propLaneElanLesAddrForm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    propLaneElanLesAddrForm.setStatus("mandatory")
_PropLaneElanGroupLesAddress_Type = AtmAddress
_PropLaneElanGroupLesAddress_Object = MibTableColumn
propLaneElanGroupLesAddress = _PropLaneElanGroupLesAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 2, 1, 1, 8),
    _PropLaneElanGroupLesAddress_Type()
)
propLaneElanGroupLesAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    propLaneElanGroupLesAddress.setStatus("mandatory")


class _PropLaneElanLuni2capability_Type(Integer32):
    """Custom type propLaneElanLuni2capability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("no", 2),
          ("yes", 1))
    )


_PropLaneElanLuni2capability_Type.__name__ = "Integer32"
_PropLaneElanLuni2capability_Object = MibTableColumn
propLaneElanLuni2capability = _PropLaneElanLuni2capability_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 2, 1, 1, 9),
    _PropLaneElanLuni2capability_Type()
)
propLaneElanLuni2capability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    propLaneElanLuni2capability.setStatus("mandatory")


class _PropLaneElanLuni2capabilityOper_Type(Integer32):
    """Custom type propLaneElanLuni2capabilityOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("no", 2),
          ("yes", 1))
    )


_PropLaneElanLuni2capabilityOper_Type.__name__ = "Integer32"
_PropLaneElanLuni2capabilityOper_Object = MibTableColumn
propLaneElanLuni2capabilityOper = _PropLaneElanLuni2capabilityOper_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 2, 1, 1, 10),
    _PropLaneElanLuni2capabilityOper_Type()
)
propLaneElanLuni2capabilityOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneElanLuni2capabilityOper.setStatus("mandatory")
_PropLaneElanLesTable_Object = MibTable
propLaneElanLesTable = _PropLaneElanLesTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 2, 2)
)
if mibBuilder.loadTexts:
    propLaneElanLesTable.setStatus("mandatory")
_PropLaneElanLesTableEntry_Object = MibTableRow
propLaneElanLesTableEntry = _PropLaneElanLesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 2, 2, 1)
)
propLaneElanLesTableEntry.setIndexNames(
    (0, "PROPLANE-MIB", "propLaneElanConfIndex"),
    (0, "PROPLANE-MIB", "propLaneElanLesIndex"),
)
if mibBuilder.loadTexts:
    propLaneElanLesTableEntry.setStatus("mandatory")
_PropLaneElanLesIndex_Type = Integer32
_PropLaneElanLesIndex_Object = MibTableColumn
propLaneElanLesIndex = _PropLaneElanLesIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 2, 2, 1, 1),
    _PropLaneElanLesIndex_Type()
)
propLaneElanLesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneElanLesIndex.setStatus("mandatory")
_PropLaneElanLesLecIdLow_Type = Integer32
_PropLaneElanLesLecIdLow_Object = MibTableColumn
propLaneElanLesLecIdLow = _PropLaneElanLesLecIdLow_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 2, 2, 1, 2),
    _PropLaneElanLesLecIdLow_Type()
)
propLaneElanLesLecIdLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneElanLesLecIdLow.setStatus("mandatory")
_PropLaneElanLesLecIdHigh_Type = Integer32
_PropLaneElanLesLecIdHigh_Object = MibTableColumn
propLaneElanLesLecIdHigh = _PropLaneElanLesLecIdHigh_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 2, 2, 1, 3),
    _PropLaneElanLesLecIdHigh_Type()
)
propLaneElanLesLecIdHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneElanLesLecIdHigh.setStatus("mandatory")
_PropLaneLes_ObjectIdentity = ObjectIdentity
propLaneLes = _PropLaneLes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 34, 3)
)
_PropLaneLesConfTable_Object = MibTable
propLaneLesConfTable = _PropLaneLesConfTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 3, 1)
)
if mibBuilder.loadTexts:
    propLaneLesConfTable.setStatus("mandatory")
_PropLaneLesConfEntry_Object = MibTableRow
propLaneLesConfEntry = _PropLaneLesConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 3, 1, 1)
)
propLaneLesConfEntry.setIndexNames(
    (0, "PROPLANE-MIB", "propLaneLesConfIndex"),
)
if mibBuilder.loadTexts:
    propLaneLesConfEntry.setStatus("mandatory")
_PropLaneLesConfIndex_Type = Integer32
_PropLaneLesConfIndex_Object = MibTableColumn
propLaneLesConfIndex = _PropLaneLesConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 3, 1, 1, 1),
    _PropLaneLesConfIndex_Type()
)
propLaneLesConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneLesConfIndex.setStatus("mandatory")


class _PropLaneLesMode_Type(Integer32):
    """Custom type propLaneLesMode based on Integer32"""
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
        *(("distrib", 4),
          ("manual", 1),
          ("resilient", 3),
          ("single", 2))
    )


_PropLaneLesMode_Type.__name__ = "Integer32"
_PropLaneLesMode_Object = MibTableColumn
propLaneLesMode = _PropLaneLesMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 3, 1, 1, 2),
    _PropLaneLesMode_Type()
)
propLaneLesMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    propLaneLesMode.setStatus("mandatory")


class _PropLaneLesActiveStatus_Type(Integer32):
    """Custom type propLaneLesActiveStatus based on Integer32"""
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
        *(("active", 1),
          ("none", 4),
          ("not-registered", 3),
          ("standby", 2))
    )


_PropLaneLesActiveStatus_Type.__name__ = "Integer32"
_PropLaneLesActiveStatus_Object = MibTableColumn
propLaneLesActiveStatus = _PropLaneLesActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 3, 1, 1, 3),
    _PropLaneLesActiveStatus_Type()
)
propLaneLesActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneLesActiveStatus.setStatus("mandatory")
_PropLaneLesLecIdLow_Type = Integer32
_PropLaneLesLecIdLow_Object = MibTableColumn
propLaneLesLecIdLow = _PropLaneLesLecIdLow_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 3, 1, 1, 4),
    _PropLaneLesLecIdLow_Type()
)
propLaneLesLecIdLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneLesLecIdLow.setStatus("mandatory")
_PropLaneLesLecIdHigh_Type = Integer32
_PropLaneLesLecIdHigh_Object = MibTableColumn
propLaneLesLecIdHigh = _PropLaneLesLecIdHigh_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 3, 1, 1, 5),
    _PropLaneLesLecIdHigh_Type()
)
propLaneLesLecIdHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneLesLecIdHigh.setStatus("mandatory")


class _PropLaneLesBusUnicastFilter_Type(Integer32):
    """Custom type propLaneLesBusUnicastFilter based on Integer32"""
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


_PropLaneLesBusUnicastFilter_Type.__name__ = "Integer32"
_PropLaneLesBusUnicastFilter_Object = MibTableColumn
propLaneLesBusUnicastFilter = _PropLaneLesBusUnicastFilter_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 3, 1, 1, 6),
    _PropLaneLesBusUnicastFilter_Type()
)
propLaneLesBusUnicastFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    propLaneLesBusUnicastFilter.setStatus("mandatory")


class _PropLaneLesLuni2capability_Type(Integer32):
    """Custom type propLaneLesLuni2capability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PropLaneLesLuni2capability_Type.__name__ = "Integer32"
_PropLaneLesLuni2capability_Object = MibTableColumn
propLaneLesLuni2capability = _PropLaneLesLuni2capability_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 3, 1, 1, 7),
    _PropLaneLesLuni2capability_Type()
)
propLaneLesLuni2capability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    propLaneLesLuni2capability.setStatus("mandatory")
_PropLaneLesLecTable_Object = MibTable
propLaneLesLecTable = _PropLaneLesLecTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 3, 2)
)
if mibBuilder.loadTexts:
    propLaneLesLecTable.setStatus("mandatory")
_PropLaneLesLecEntry_Object = MibTableRow
propLaneLesLecEntry = _PropLaneLesLecEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 3, 2, 1)
)
propLaneLesLecEntry.setIndexNames(
    (0, "PROPLANE-MIB", "propLaneLesConfIndex"),
    (0, "PROPLANE-MIB", "propLaneLesLecIndex"),
)
if mibBuilder.loadTexts:
    propLaneLesLecEntry.setStatus("mandatory")
_PropLaneLesLecIndex_Type = Integer32
_PropLaneLesLecIndex_Object = MibTableColumn
propLaneLesLecIndex = _PropLaneLesLecIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 3, 2, 1, 1),
    _PropLaneLesLecIndex_Type()
)
propLaneLesLecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneLesLecIndex.setStatus("mandatory")


class _PropLaneLesLecLuni2granted_Type(Integer32):
    """Custom type propLaneLesLecLuni2granted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PropLaneLesLecLuni2granted_Type.__name__ = "Integer32"
_PropLaneLesLecLuni2granted_Object = MibTableColumn
propLaneLesLecLuni2granted = _PropLaneLesLecLuni2granted_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 3, 2, 1, 2),
    _PropLaneLesLecLuni2granted_Type()
)
propLaneLesLecLuni2granted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneLesLecLuni2granted.setStatus("mandatory")


class _PropLaneLesLecSelectiveMulticast_Type(Integer32):
    """Custom type propLaneLesLecSelectiveMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PropLaneLesLecSelectiveMulticast_Type.__name__ = "Integer32"
_PropLaneLesLecSelectiveMulticast_Object = MibTableColumn
propLaneLesLecSelectiveMulticast = _PropLaneLesLecSelectiveMulticast_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 3, 2, 1, 3),
    _PropLaneLesLecSelectiveMulticast_Type()
)
propLaneLesLecSelectiveMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneLesLecSelectiveMulticast.setStatus("mandatory")
_PropLaneLecs_ObjectIdentity = ObjectIdentity
propLaneLecs = _PropLaneLecs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 34, 4)
)
_PropLaneLecsTable_Object = MibTable
propLaneLecsTable = _PropLaneLecsTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 4, 1)
)
if mibBuilder.loadTexts:
    propLaneLecsTable.setStatus("mandatory")
_PropLaneLecsEntry_Object = MibTableRow
propLaneLecsEntry = _PropLaneLecsEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 4, 1, 1)
)
propLaneLecsEntry.setIndexNames(
    (0, "PROPLANE-MIB", "propLaneLecsSlotIndex"),
)
if mibBuilder.loadTexts:
    propLaneLecsEntry.setStatus("mandatory")
_PropLaneLecsSlotIndex_Type = Integer32
_PropLaneLecsSlotIndex_Object = MibTableColumn
propLaneLecsSlotIndex = _PropLaneLecsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 4, 1, 1, 1),
    _PropLaneLecsSlotIndex_Type()
)
propLaneLecsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneLecsSlotIndex.setStatus("mandatory")


class _PropLaneLecsLocation_Type(Integer32):
    """Custom type propLaneLecsLocation based on Integer32"""
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
        *(("local-selector", 2),
          ("local-wka", 1),
          ("remote-atm-addr", 4),
          ("remote-res-lecs", 5),
          ("remote-wka", 3))
    )


_PropLaneLecsLocation_Type.__name__ = "Integer32"
_PropLaneLecsLocation_Object = MibTableColumn
propLaneLecsLocation = _PropLaneLecsLocation_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 4, 1, 1, 2),
    _PropLaneLecsLocation_Type()
)
propLaneLecsLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    propLaneLecsLocation.setStatus("mandatory")
_PropLaneLecsRemoteAddress_Type = AtmAddress
_PropLaneLecsRemoteAddress_Object = MibTableColumn
propLaneLecsRemoteAddress = _PropLaneLecsRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 4, 1, 1, 3),
    _PropLaneLecsRemoteAddress_Type()
)
propLaneLecsRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    propLaneLecsRemoteAddress.setStatus("mandatory")
_PropLaneLecsLocalSelector_Type = Integer32
_PropLaneLecsLocalSelector_Object = MibTableColumn
propLaneLecsLocalSelector = _PropLaneLecsLocalSelector_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 4, 1, 1, 4),
    _PropLaneLecsLocalSelector_Type()
)
propLaneLecsLocalSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    propLaneLecsLocalSelector.setStatus("mandatory")


class _PropLaneLecsDefTRElan_Type(DisplayString):
    """Custom type propLaneLecsDefTRElan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PropLaneLecsDefTRElan_Type.__name__ = "DisplayString"
_PropLaneLecsDefTRElan_Object = MibTableColumn
propLaneLecsDefTRElan = _PropLaneLecsDefTRElan_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 4, 1, 1, 5),
    _PropLaneLecsDefTRElan_Type()
)
propLaneLecsDefTRElan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    propLaneLecsDefTRElan.setStatus("mandatory")


class _PropLaneLecsDefEthElan_Type(DisplayString):
    """Custom type propLaneLecsDefEthElan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PropLaneLecsDefEthElan_Type.__name__ = "DisplayString"
_PropLaneLecsDefEthElan_Object = MibTableColumn
propLaneLecsDefEthElan = _PropLaneLecsDefEthElan_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 4, 1, 1, 6),
    _PropLaneLecsDefEthElan_Type()
)
propLaneLecsDefEthElan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    propLaneLecsDefEthElan.setStatus("mandatory")


class _PropLaneLecsDefUnspecElan_Type(DisplayString):
    """Custom type propLaneLecsDefUnspecElan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PropLaneLecsDefUnspecElan_Type.__name__ = "DisplayString"
_PropLaneLecsDefUnspecElan_Object = MibTableColumn
propLaneLecsDefUnspecElan = _PropLaneLecsDefUnspecElan_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 4, 1, 1, 7),
    _PropLaneLecsDefUnspecElan_Type()
)
propLaneLecsDefUnspecElan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    propLaneLecsDefUnspecElan.setStatus("mandatory")


class _PropLaneLecsResilientNetStatus_Type(Integer32):
    """Custom type propLaneLecsResilientNetStatus based on Integer32"""
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
        *(("discovering", 1),
          ("forming", 2),
          ("not-resilient", 5),
          ("running", 4),
          ("synchronising", 3))
    )


_PropLaneLecsResilientNetStatus_Type.__name__ = "Integer32"
_PropLaneLecsResilientNetStatus_Object = MibTableColumn
propLaneLecsResilientNetStatus = _PropLaneLecsResilientNetStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 4, 1, 1, 8),
    _PropLaneLecsResilientNetStatus_Type()
)
propLaneLecsResilientNetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneLecsResilientNetStatus.setStatus("mandatory")


class _PropLaneLecsResilientMode_Type(Integer32):
    """Custom type propLaneLecsResilientMode based on Integer32"""
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


_PropLaneLecsResilientMode_Type.__name__ = "Integer32"
_PropLaneLecsResilientMode_Object = MibTableColumn
propLaneLecsResilientMode = _PropLaneLecsResilientMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 4, 1, 1, 9),
    _PropLaneLecsResilientMode_Type()
)
propLaneLecsResilientMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    propLaneLecsResilientMode.setStatus("mandatory")


class _PropLaneLecsResilientStatus_Type(Integer32):
    """Custom type propLaneLecsResilientStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("not-resilient", 3),
          ("standby", 2))
    )


_PropLaneLecsResilientStatus_Type.__name__ = "Integer32"
_PropLaneLecsResilientStatus_Object = MibTableColumn
propLaneLecsResilientStatus = _PropLaneLecsResilientStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 4, 1, 1, 10),
    _PropLaneLecsResilientStatus_Type()
)
propLaneLecsResilientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneLecsResilientStatus.setStatus("mandatory")


class _PropLaneLecsResilientPriority_Type(Integer32):
    """Custom type propLaneLecsResilientPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PropLaneLecsResilientPriority_Type.__name__ = "Integer32"
_PropLaneLecsResilientPriority_Object = MibTableColumn
propLaneLecsResilientPriority = _PropLaneLecsResilientPriority_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 4, 1, 1, 11),
    _PropLaneLecsResilientPriority_Type()
)
propLaneLecsResilientPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    propLaneLecsResilientPriority.setStatus("mandatory")
_PropLaneResLecs_ObjectIdentity = ObjectIdentity
propLaneResLecs = _PropLaneResLecs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 34, 5)
)
_PropLaneLecsResTable_Object = MibTable
propLaneLecsResTable = _PropLaneLecsResTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 5, 1)
)
if mibBuilder.loadTexts:
    propLaneLecsResTable.setStatus("mandatory")
_PropLaneLecsResEntry_Object = MibTableRow
propLaneLecsResEntry = _PropLaneLecsResEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 5, 1, 1)
)
propLaneLecsResEntry.setIndexNames(
    (0, "PROPLANE-MIB", "propLaneLecsSlotIndex"),
    (0, "PROPLANE-MIB", "propLaneLecsResIndex"),
)
if mibBuilder.loadTexts:
    propLaneLecsResEntry.setStatus("mandatory")
_PropLaneLecsResIndex_Type = Integer32
_PropLaneLecsResIndex_Object = MibTableColumn
propLaneLecsResIndex = _PropLaneLecsResIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 5, 1, 1, 1),
    _PropLaneLecsResIndex_Type()
)
propLaneLecsResIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneLecsResIndex.setStatus("mandatory")
_PropLaneLecsResAddress_Type = AtmAddress
_PropLaneLecsResAddress_Object = MibTableColumn
propLaneLecsResAddress = _PropLaneLecsResAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 5, 1, 1, 2),
    _PropLaneLecsResAddress_Type()
)
propLaneLecsResAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneLecsResAddress.setStatus("mandatory")


class _PropLaneLecsResPriority_Type(Integer32):
    """Custom type propLaneLecsResPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PropLaneLecsResPriority_Type.__name__ = "Integer32"
_PropLaneLecsResPriority_Object = MibTableColumn
propLaneLecsResPriority = _PropLaneLecsResPriority_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 5, 1, 1, 3),
    _PropLaneLecsResPriority_Type()
)
propLaneLecsResPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneLecsResPriority.setStatus("mandatory")


class _PropLaneLecsResStatus_Type(Integer32):
    """Custom type propLaneLecsResStatus based on Integer32"""
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
        *(("active", 1),
          ("not-found", 4),
          ("standby", 2),
          ("timing-out", 3))
    )


_PropLaneLecsResStatus_Type.__name__ = "Integer32"
_PropLaneLecsResStatus_Object = MibTableColumn
propLaneLecsResStatus = _PropLaneLecsResStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 5, 1, 1, 4),
    _PropLaneLecsResStatus_Type()
)
propLaneLecsResStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneLecsResStatus.setStatus("mandatory")


class _PropLaneLecsResOrigin_Type(Integer32):
    """Custom type propLaneLecsResOrigin based on Integer32"""
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
        *(("local", 4),
          ("manual", 1),
          ("pvc", 3),
          ("pvc-svc", 2),
          ("snmp", 5))
    )


_PropLaneLecsResOrigin_Type.__name__ = "Integer32"
_PropLaneLecsResOrigin_Object = MibTableColumn
propLaneLecsResOrigin = _PropLaneLecsResOrigin_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 5, 1, 1, 5),
    _PropLaneLecsResOrigin_Type()
)
propLaneLecsResOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneLecsResOrigin.setStatus("mandatory")


class _PropLaneLecsResRowStatus_Type(Integer32):
    """Custom type propLaneLecsResRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("undercreation", 2),
          ("valid", 3))
    )


_PropLaneLecsResRowStatus_Type.__name__ = "Integer32"
_PropLaneLecsResRowStatus_Object = MibTableColumn
propLaneLecsResRowStatus = _PropLaneLecsResRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 5, 1, 1, 6),
    _PropLaneLecsResRowStatus_Type()
)
propLaneLecsResRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneLecsResRowStatus.setStatus("mandatory")
_PropLaneLecsResActiveTime_Type = TimeTicks
_PropLaneLecsResActiveTime_Object = MibTableColumn
propLaneLecsResActiveTime = _PropLaneLecsResActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 5, 1, 1, 7),
    _PropLaneLecsResActiveTime_Type()
)
propLaneLecsResActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneLecsResActiveTime.setStatus("mandatory")


class _PropLaneLecsResAddrForm_Type(Integer32):
    """Custom type propLaneLecsResAddrForm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("selector", 2),
          ("unknown", 3),
          ("wka", 1))
    )


_PropLaneLecsResAddrForm_Type.__name__ = "Integer32"
_PropLaneLecsResAddrForm_Object = MibTableColumn
propLaneLecsResAddrForm = _PropLaneLecsResAddrForm_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 5, 1, 1, 8),
    _PropLaneLecsResAddrForm_Type()
)
propLaneLecsResAddrForm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneLecsResAddrForm.setStatus("mandatory")


class _PropLaneLecsResSelector_Type(Integer32):
    """Custom type propLaneLecsResSelector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PropLaneLecsResSelector_Type.__name__ = "Integer32"
_PropLaneLecsResSelector_Object = MibTableColumn
propLaneLecsResSelector = _PropLaneLecsResSelector_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 5, 1, 1, 9),
    _PropLaneLecsResSelector_Type()
)
propLaneLecsResSelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneLecsResSelector.setStatus("mandatory")
_PropLaneSlot_ObjectIdentity = ObjectIdentity
propLaneSlot = _PropLaneSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 34, 6)
)
_PropLaneSlotTable_Object = MibTable
propLaneSlotTable = _PropLaneSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 6, 1)
)
if mibBuilder.loadTexts:
    propLaneSlotTable.setStatus("mandatory")
_PropLaneSlotEntry_Object = MibTableRow
propLaneSlotEntry = _PropLaneSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 6, 1, 1)
)
propLaneSlotEntry.setIndexNames(
    (0, "PROPLANE-MIB", "propLaneSlotIndex"),
)
if mibBuilder.loadTexts:
    propLaneSlotEntry.setStatus("mandatory")
_PropLaneSlotIndex_Type = Integer32
_PropLaneSlotIndex_Object = MibTableColumn
propLaneSlotIndex = _PropLaneSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 6, 1, 1, 1),
    _PropLaneSlotIndex_Type()
)
propLaneSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneSlotIndex.setStatus("mandatory")
_PropLaneSlotElanConfNextId_Type = Integer32
_PropLaneSlotElanConfNextId_Object = MibTableColumn
propLaneSlotElanConfNextId = _PropLaneSlotElanConfNextId_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 6, 1, 1, 2),
    _PropLaneSlotElanConfNextId_Type()
)
propLaneSlotElanConfNextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneSlotElanConfNextId.setStatus("mandatory")
_PropLaneSlotLecsConfNextId_Type = Integer32
_PropLaneSlotLecsConfNextId_Object = MibTableColumn
propLaneSlotLecsConfNextId = _PropLaneSlotLecsConfNextId_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 6, 1, 1, 3),
    _PropLaneSlotLecsConfNextId_Type()
)
propLaneSlotLecsConfNextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneSlotLecsConfNextId.setStatus("mandatory")
_PropLaneSlotLesConfNextId_Type = Integer32
_PropLaneSlotLesConfNextId_Object = MibTableColumn
propLaneSlotLesConfNextId = _PropLaneSlotLesConfNextId_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 6, 1, 1, 4),
    _PropLaneSlotLesConfNextId_Type()
)
propLaneSlotLesConfNextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneSlotLesConfNextId.setStatus("mandatory")
_PropLaneSlotBusConfNextId_Type = Integer32
_PropLaneSlotBusConfNextId_Object = MibTableColumn
propLaneSlotBusConfNextId = _PropLaneSlotBusConfNextId_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 6, 1, 1, 5),
    _PropLaneSlotBusConfNextId_Type()
)
propLaneSlotBusConfNextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneSlotBusConfNextId.setStatus("mandatory")
_PropLaneSlotNextLesSelector_Type = Integer32
_PropLaneSlotNextLesSelector_Object = MibTableColumn
propLaneSlotNextLesSelector = _PropLaneSlotNextLesSelector_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 6, 1, 1, 6),
    _PropLaneSlotNextLesSelector_Type()
)
propLaneSlotNextLesSelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneSlotNextLesSelector.setStatus("mandatory")
_PropLaneSlotNextBusSelector_Type = Integer32
_PropLaneSlotNextBusSelector_Object = MibTableColumn
propLaneSlotNextBusSelector = _PropLaneSlotNextBusSelector_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 6, 1, 1, 7),
    _PropLaneSlotNextBusSelector_Type()
)
propLaneSlotNextBusSelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneSlotNextBusSelector.setStatus("mandatory")
_PropLaneSlotNextLecsSelector_Type = Integer32
_PropLaneSlotNextLecsSelector_Object = MibTableColumn
propLaneSlotNextLecsSelector = _PropLaneSlotNextLecsSelector_Object(
    (1, 3, 6, 1, 4, 1, 81, 34, 6, 1, 1, 8),
    _PropLaneSlotNextLecsSelector_Type()
)
propLaneSlotNextLecsSelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propLaneSlotNextLecsSelector.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PROPLANE-MIB",
    **{"AtmAddress": AtmAddress,
       "MacAddress": MacAddress,
       "propLane": propLane,
       "propLaneMgmtLEC": propLaneMgmtLEC,
       "propLaneMgmtLECCurrentAddress": propLaneMgmtLECCurrentAddress,
       "propLaneMgmtLECIfIndexMap": propLaneMgmtLECIfIndexMap,
       "propLaneMgmtLECLecIndexMap": propLaneMgmtLECLecIndexMap,
       "propLaneElan": propLaneElan,
       "propLaneElanConfTable": propLaneElanConfTable,
       "propLaneElanConfEntry": propLaneElanConfEntry,
       "propLaneElanConfIndex": propLaneElanConfIndex,
       "propLaneElanSecurity": propLaneElanSecurity,
       "propLaneElanLesDiscovery": propLaneElanLesDiscovery,
       "propLaneElanLesRgstrType": propLaneElanLesRgstrType,
       "propLaneElanLesActualRgstrType": propLaneElanLesActualRgstrType,
       "propLaneElanMaximumActiveLes": propLaneElanMaximumActiveLes,
       "propLaneElanLesAddrForm": propLaneElanLesAddrForm,
       "propLaneElanGroupLesAddress": propLaneElanGroupLesAddress,
       "propLaneElanLuni2capability": propLaneElanLuni2capability,
       "propLaneElanLuni2capabilityOper": propLaneElanLuni2capabilityOper,
       "propLaneElanLesTable": propLaneElanLesTable,
       "propLaneElanLesTableEntry": propLaneElanLesTableEntry,
       "propLaneElanLesIndex": propLaneElanLesIndex,
       "propLaneElanLesLecIdLow": propLaneElanLesLecIdLow,
       "propLaneElanLesLecIdHigh": propLaneElanLesLecIdHigh,
       "propLaneLes": propLaneLes,
       "propLaneLesConfTable": propLaneLesConfTable,
       "propLaneLesConfEntry": propLaneLesConfEntry,
       "propLaneLesConfIndex": propLaneLesConfIndex,
       "propLaneLesMode": propLaneLesMode,
       "propLaneLesActiveStatus": propLaneLesActiveStatus,
       "propLaneLesLecIdLow": propLaneLesLecIdLow,
       "propLaneLesLecIdHigh": propLaneLesLecIdHigh,
       "propLaneLesBusUnicastFilter": propLaneLesBusUnicastFilter,
       "propLaneLesLuni2capability": propLaneLesLuni2capability,
       "propLaneLesLecTable": propLaneLesLecTable,
       "propLaneLesLecEntry": propLaneLesLecEntry,
       "propLaneLesLecIndex": propLaneLesLecIndex,
       "propLaneLesLecLuni2granted": propLaneLesLecLuni2granted,
       "propLaneLesLecSelectiveMulticast": propLaneLesLecSelectiveMulticast,
       "propLaneLecs": propLaneLecs,
       "propLaneLecsTable": propLaneLecsTable,
       "propLaneLecsEntry": propLaneLecsEntry,
       "propLaneLecsSlotIndex": propLaneLecsSlotIndex,
       "propLaneLecsLocation": propLaneLecsLocation,
       "propLaneLecsRemoteAddress": propLaneLecsRemoteAddress,
       "propLaneLecsLocalSelector": propLaneLecsLocalSelector,
       "propLaneLecsDefTRElan": propLaneLecsDefTRElan,
       "propLaneLecsDefEthElan": propLaneLecsDefEthElan,
       "propLaneLecsDefUnspecElan": propLaneLecsDefUnspecElan,
       "propLaneLecsResilientNetStatus": propLaneLecsResilientNetStatus,
       "propLaneLecsResilientMode": propLaneLecsResilientMode,
       "propLaneLecsResilientStatus": propLaneLecsResilientStatus,
       "propLaneLecsResilientPriority": propLaneLecsResilientPriority,
       "propLaneResLecs": propLaneResLecs,
       "propLaneLecsResTable": propLaneLecsResTable,
       "propLaneLecsResEntry": propLaneLecsResEntry,
       "propLaneLecsResIndex": propLaneLecsResIndex,
       "propLaneLecsResAddress": propLaneLecsResAddress,
       "propLaneLecsResPriority": propLaneLecsResPriority,
       "propLaneLecsResStatus": propLaneLecsResStatus,
       "propLaneLecsResOrigin": propLaneLecsResOrigin,
       "propLaneLecsResRowStatus": propLaneLecsResRowStatus,
       "propLaneLecsResActiveTime": propLaneLecsResActiveTime,
       "propLaneLecsResAddrForm": propLaneLecsResAddrForm,
       "propLaneLecsResSelector": propLaneLecsResSelector,
       "propLaneSlot": propLaneSlot,
       "propLaneSlotTable": propLaneSlotTable,
       "propLaneSlotEntry": propLaneSlotEntry,
       "propLaneSlotIndex": propLaneSlotIndex,
       "propLaneSlotElanConfNextId": propLaneSlotElanConfNextId,
       "propLaneSlotLecsConfNextId": propLaneSlotLecsConfNextId,
       "propLaneSlotLesConfNextId": propLaneSlotLesConfNextId,
       "propLaneSlotBusConfNextId": propLaneSlotBusConfNextId,
       "propLaneSlotNextLesSelector": propLaneSlotNextLesSelector,
       "propLaneSlotNextBusSelector": propLaneSlotNextBusSelector,
       "propLaneSlotNextLecsSelector": propLaneSlotNextLecsSelector}
)
