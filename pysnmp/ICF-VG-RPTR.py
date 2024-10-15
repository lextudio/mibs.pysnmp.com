# SNMP MIB module (ICF-VG-RPTR) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ICF-VG-RPTR
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:26 2024
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

(hpicfObjectModules,
 icfVgRepeater) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfObjectModules",
    "icfVgRepeater")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 MacAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

icfVgRepeaterMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10)
)
icfVgRepeaterMib.setRevisions(
        ("2000-11-03 22:25",
         "1997-03-06 03:47",
         "1996-09-10 02:03",
         "1996-01-25 03:56",
         "1995-01-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IcfVgBasic_ObjectIdentity = ObjectIdentity
icfVgBasic = _IcfVgBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1)
)
_IcfVgBasicRptr_ObjectIdentity = ObjectIdentity
icfVgBasicRptr = _IcfVgBasicRptr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1)
)
_IcfVgMACAddress_Type = MacAddress
_IcfVgMACAddress_Object = MibScalar
icfVgMACAddress = _IcfVgMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 1),
    _IcfVgMACAddress_Type()
)
icfVgMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgMACAddress.setStatus("current")


class _IcfVgCurrentFramingType_Type(Integer32):
    """Custom type icfVgCurrentFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frameType88023", 1),
          ("frameType88025", 2))
    )


_IcfVgCurrentFramingType_Type.__name__ = "Integer32"
_IcfVgCurrentFramingType_Object = MibScalar
icfVgCurrentFramingType = _IcfVgCurrentFramingType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 2),
    _IcfVgCurrentFramingType_Type()
)
icfVgCurrentFramingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgCurrentFramingType.setStatus("current")


class _IcfVgDesiredFramingType_Type(Integer32):
    """Custom type icfVgDesiredFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frameType88023", 1),
          ("frameType88025", 2))
    )


_IcfVgDesiredFramingType_Type.__name__ = "Integer32"
_IcfVgDesiredFramingType_Object = MibScalar
icfVgDesiredFramingType = _IcfVgDesiredFramingType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 3),
    _IcfVgDesiredFramingType_Type()
)
icfVgDesiredFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfVgDesiredFramingType.setStatus("current")


class _IcfVgFramingCapability_Type(Integer32):
    """Custom type icfVgFramingCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("frameType88023", 1),
          ("frameType88025", 2),
          ("frameTypeEither", 3))
    )


_IcfVgFramingCapability_Type.__name__ = "Integer32"
_IcfVgFramingCapability_Object = MibScalar
icfVgFramingCapability = _IcfVgFramingCapability_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 4),
    _IcfVgFramingCapability_Type()
)
icfVgFramingCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgFramingCapability.setStatus("current")


class _IcfVgTrainingVersion_Type(Integer32):
    """Custom type icfVgTrainingVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IcfVgTrainingVersion_Type.__name__ = "Integer32"
_IcfVgTrainingVersion_Object = MibScalar
icfVgTrainingVersion = _IcfVgTrainingVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 5),
    _IcfVgTrainingVersion_Type()
)
icfVgTrainingVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgTrainingVersion.setStatus("current")


class _IcfVgRepeaterGroupCapacity_Type(Integer32):
    """Custom type icfVgRepeaterGroupCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IcfVgRepeaterGroupCapacity_Type.__name__ = "Integer32"
_IcfVgRepeaterGroupCapacity_Object = MibScalar
icfVgRepeaterGroupCapacity = _IcfVgRepeaterGroupCapacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 6),
    _IcfVgRepeaterGroupCapacity_Type()
)
icfVgRepeaterGroupCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgRepeaterGroupCapacity.setStatus("current")


class _IcfVgRepeaterHealthState_Type(Integer32):
    """Custom type icfVgRepeaterHealthState based on Integer32"""
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
        *(("generalFailure", 6),
          ("groupFailure", 4),
          ("ok", 2),
          ("other", 1),
          ("portFailure", 5),
          ("rptrFailure", 3))
    )


_IcfVgRepeaterHealthState_Type.__name__ = "Integer32"
_IcfVgRepeaterHealthState_Object = MibScalar
icfVgRepeaterHealthState = _IcfVgRepeaterHealthState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 7),
    _IcfVgRepeaterHealthState_Type()
)
icfVgRepeaterHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgRepeaterHealthState.setStatus("current")


class _IcfVgRepeaterHealthText_Type(DisplayString):
    """Custom type icfVgRepeaterHealthText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IcfVgRepeaterHealthText_Type.__name__ = "DisplayString"
_IcfVgRepeaterHealthText_Object = MibScalar
icfVgRepeaterHealthText = _IcfVgRepeaterHealthText_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 8),
    _IcfVgRepeaterHealthText_Type()
)
icfVgRepeaterHealthText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgRepeaterHealthText.setStatus("current")


class _IcfVgRepeaterReset_Type(Integer32):
    """Custom type icfVgRepeaterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_IcfVgRepeaterReset_Type.__name__ = "Integer32"
_IcfVgRepeaterReset_Object = MibScalar
icfVgRepeaterReset = _IcfVgRepeaterReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 9),
    _IcfVgRepeaterReset_Type()
)
icfVgRepeaterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfVgRepeaterReset.setStatus("current")


class _IcfVgRepeaterNonDisruptTest_Type(Integer32):
    """Custom type icfVgRepeaterNonDisruptTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSelfTest", 1),
          ("selfTest", 2))
    )


_IcfVgRepeaterNonDisruptTest_Type.__name__ = "Integer32"
_IcfVgRepeaterNonDisruptTest_Object = MibScalar
icfVgRepeaterNonDisruptTest = _IcfVgRepeaterNonDisruptTest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 10),
    _IcfVgRepeaterNonDisruptTest_Type()
)
icfVgRepeaterNonDisruptTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfVgRepeaterNonDisruptTest.setStatus("current")
_IcfVgBasicGroup_ObjectIdentity = ObjectIdentity
icfVgBasicGroup = _IcfVgBasicGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2)
)
_IcfVgBasicGroupTable_Object = MibTable
icfVgBasicGroupTable = _IcfVgBasicGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    icfVgBasicGroupTable.setStatus("current")
_IcfVgBasicGroupEntry_Object = MibTableRow
icfVgBasicGroupEntry = _IcfVgBasicGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1)
)
icfVgBasicGroupEntry.setIndexNames(
    (0, "ICF-VG-RPTR", "icfVgGroupIndex"),
)
if mibBuilder.loadTexts:
    icfVgBasicGroupEntry.setStatus("current")


class _IcfVgGroupIndex_Type(Integer32):
    """Custom type icfVgGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IcfVgGroupIndex_Type.__name__ = "Integer32"
_IcfVgGroupIndex_Object = MibTableColumn
icfVgGroupIndex = _IcfVgGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1, 1),
    _IcfVgGroupIndex_Type()
)
icfVgGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icfVgGroupIndex.setStatus("current")


class _IcfVgGroupDescr_Type(DisplayString):
    """Custom type icfVgGroupDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IcfVgGroupDescr_Type.__name__ = "DisplayString"
_IcfVgGroupDescr_Object = MibTableColumn
icfVgGroupDescr = _IcfVgGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1, 2),
    _IcfVgGroupDescr_Type()
)
icfVgGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgGroupDescr.setStatus("current")
_IcfVgGroupObjectID_Type = ObjectIdentifier
_IcfVgGroupObjectID_Object = MibTableColumn
icfVgGroupObjectID = _IcfVgGroupObjectID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1, 3),
    _IcfVgGroupObjectID_Type()
)
icfVgGroupObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgGroupObjectID.setStatus("current")


class _IcfVgGroupOperStatus_Type(Integer32):
    """Custom type icfVgGroupOperStatus based on Integer32"""
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
        *(("malfunctioning", 3),
          ("notPresent", 4),
          ("operational", 2),
          ("other", 1),
          ("resetInProgress", 6),
          ("underTest", 5))
    )


_IcfVgGroupOperStatus_Type.__name__ = "Integer32"
_IcfVgGroupOperStatus_Object = MibTableColumn
icfVgGroupOperStatus = _IcfVgGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1, 4),
    _IcfVgGroupOperStatus_Type()
)
icfVgGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgGroupOperStatus.setStatus("current")
_IcfVgGroupLastOperStatusChange_Type = TimeStamp
_IcfVgGroupLastOperStatusChange_Object = MibTableColumn
icfVgGroupLastOperStatusChange = _IcfVgGroupLastOperStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1, 5),
    _IcfVgGroupLastOperStatusChange_Type()
)
icfVgGroupLastOperStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgGroupLastOperStatusChange.setStatus("current")


class _IcfVgGroupPortCapacity_Type(Integer32):
    """Custom type icfVgGroupPortCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IcfVgGroupPortCapacity_Type.__name__ = "Integer32"
_IcfVgGroupPortCapacity_Object = MibTableColumn
icfVgGroupPortCapacity = _IcfVgGroupPortCapacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1, 6),
    _IcfVgGroupPortCapacity_Type()
)
icfVgGroupPortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgGroupPortCapacity.setStatus("current")


class _IcfVgGroupCablesBundled_Type(Integer32):
    """Custom type icfVgGroupCablesBundled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCablesBundled", 2),
          ("someCablesBundled", 1))
    )


_IcfVgGroupCablesBundled_Type.__name__ = "Integer32"
_IcfVgGroupCablesBundled_Object = MibTableColumn
icfVgGroupCablesBundled = _IcfVgGroupCablesBundled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1, 7),
    _IcfVgGroupCablesBundled_Type()
)
icfVgGroupCablesBundled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfVgGroupCablesBundled.setStatus("current")
_IcfVgBasicPort_ObjectIdentity = ObjectIdentity
icfVgBasicPort = _IcfVgBasicPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3)
)
_IcfVgBasicPortTable_Object = MibTable
icfVgBasicPortTable = _IcfVgBasicPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    icfVgBasicPortTable.setStatus("current")
_IcfVgBasicPortEntry_Object = MibTableRow
icfVgBasicPortEntry = _IcfVgBasicPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1)
)
icfVgBasicPortEntry.setIndexNames(
    (0, "ICF-VG-RPTR", "icfVgPortGroupIndex"),
    (0, "ICF-VG-RPTR", "icfVgPortIndex"),
)
if mibBuilder.loadTexts:
    icfVgBasicPortEntry.setStatus("current")


class _IcfVgPortGroupIndex_Type(Integer32):
    """Custom type icfVgPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IcfVgPortGroupIndex_Type.__name__ = "Integer32"
_IcfVgPortGroupIndex_Object = MibTableColumn
icfVgPortGroupIndex = _IcfVgPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 1),
    _IcfVgPortGroupIndex_Type()
)
icfVgPortGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icfVgPortGroupIndex.setStatus("current")


class _IcfVgPortIndex_Type(Integer32):
    """Custom type icfVgPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IcfVgPortIndex_Type.__name__ = "Integer32"
_IcfVgPortIndex_Object = MibTableColumn
icfVgPortIndex = _IcfVgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 2),
    _IcfVgPortIndex_Type()
)
icfVgPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icfVgPortIndex.setStatus("current")


class _IcfVgPortType_Type(Integer32):
    """Custom type icfVgPortType based on Integer32"""
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
        *(("cascadeExternal", 1),
          ("cascadeInternal", 2),
          ("localExternal", 3),
          ("localInternal", 4))
    )


_IcfVgPortType_Type.__name__ = "Integer32"
_IcfVgPortType_Object = MibTableColumn
icfVgPortType = _IcfVgPortType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 3),
    _IcfVgPortType_Type()
)
icfVgPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortType.setStatus("current")


class _IcfVgPortAdminStatus_Type(Integer32):
    """Custom type icfVgPortAdminStatus based on Integer32"""
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


_IcfVgPortAdminStatus_Type.__name__ = "Integer32"
_IcfVgPortAdminStatus_Object = MibTableColumn
icfVgPortAdminStatus = _IcfVgPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 4),
    _IcfVgPortAdminStatus_Type()
)
icfVgPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfVgPortAdminStatus.setStatus("current")


class _IcfVgPortStatus_Type(Integer32):
    """Custom type icfVgPortStatus based on Integer32"""
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
          ("inactive", 2),
          ("training", 3))
    )


_IcfVgPortStatus_Type.__name__ = "Integer32"
_IcfVgPortStatus_Object = MibTableColumn
icfVgPortStatus = _IcfVgPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 5),
    _IcfVgPortStatus_Type()
)
icfVgPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortStatus.setStatus("current")


class _IcfVgPortSupportedPromiscMode_Type(Integer32):
    """Custom type icfVgPortSupportedPromiscMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("promiscModeOnly", 3),
          ("singleModeOnly", 1),
          ("singleOrPromiscMode", 2))
    )


_IcfVgPortSupportedPromiscMode_Type.__name__ = "Integer32"
_IcfVgPortSupportedPromiscMode_Object = MibTableColumn
icfVgPortSupportedPromiscMode = _IcfVgPortSupportedPromiscMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 6),
    _IcfVgPortSupportedPromiscMode_Type()
)
icfVgPortSupportedPromiscMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortSupportedPromiscMode.setStatus("current")


class _IcfVgPortSupportedCascadeMode_Type(Integer32):
    """Custom type icfVgPortSupportedCascadeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cascadePort", 3),
          ("endNodesOnly", 1),
          ("endNodesOrRepeaters", 2))
    )


_IcfVgPortSupportedCascadeMode_Type.__name__ = "Integer32"
_IcfVgPortSupportedCascadeMode_Object = MibTableColumn
icfVgPortSupportedCascadeMode = _IcfVgPortSupportedCascadeMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 7),
    _IcfVgPortSupportedCascadeMode_Type()
)
icfVgPortSupportedCascadeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortSupportedCascadeMode.setStatus("current")


class _IcfVgPortAllowedTrainType_Type(Integer32):
    """Custom type icfVgPortAllowedTrainType based on Integer32"""
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
        *(("allowAnything", 4),
          ("allowEndNodesOnly", 1),
          ("allowEndNodesOrRepeaters", 3),
          ("allowPromiscuousEndNodes", 2))
    )


_IcfVgPortAllowedTrainType_Type.__name__ = "Integer32"
_IcfVgPortAllowedTrainType_Object = MibTableColumn
icfVgPortAllowedTrainType = _IcfVgPortAllowedTrainType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 8),
    _IcfVgPortAllowedTrainType_Type()
)
icfVgPortAllowedTrainType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfVgPortAllowedTrainType.setStatus("current")


class _IcfVgPortLastTrainConfig_Type(OctetString):
    """Custom type icfVgPortLastTrainConfig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IcfVgPortLastTrainConfig_Type.__name__ = "OctetString"
_IcfVgPortLastTrainConfig_Object = MibTableColumn
icfVgPortLastTrainConfig = _IcfVgPortLastTrainConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 9),
    _IcfVgPortLastTrainConfig_Type()
)
icfVgPortLastTrainConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortLastTrainConfig.setStatus("current")


class _IcfVgPortTrainingResult_Type(OctetString):
    """Custom type icfVgPortTrainingResult based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_IcfVgPortTrainingResult_Type.__name__ = "OctetString"
_IcfVgPortTrainingResult_Object = MibTableColumn
icfVgPortTrainingResult = _IcfVgPortTrainingResult_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 10),
    _IcfVgPortTrainingResult_Type()
)
icfVgPortTrainingResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortTrainingResult.setStatus("current")
_IcfVgPortPriorityEnable_Type = TruthValue
_IcfVgPortPriorityEnable_Object = MibTableColumn
icfVgPortPriorityEnable = _IcfVgPortPriorityEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 11),
    _IcfVgPortPriorityEnable_Type()
)
icfVgPortPriorityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfVgPortPriorityEnable.setStatus("current")


class _IcfVgPortMediaType_Type(Integer32):
    """Custom type icfVgPortMediaType based on Integer32"""
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
        *(("fibre", 6),
          ("other", 1),
          ("pmdMissing", 3),
          ("stp2", 5),
          ("unknown", 2),
          ("utp4", 4))
    )


_IcfVgPortMediaType_Type.__name__ = "Integer32"
_IcfVgPortMediaType_Object = MibTableColumn
icfVgPortMediaType = _IcfVgPortMediaType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 12),
    _IcfVgPortMediaType_Type()
)
icfVgPortMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortMediaType.setStatus("current")
_IcfVgMonitor_ObjectIdentity = ObjectIdentity
icfVgMonitor = _IcfVgMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2)
)
_IcfVgMonRptr_ObjectIdentity = ObjectIdentity
icfVgMonRptr = _IcfVgMonRptr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 1)
)
_IcfVgMonGroup_ObjectIdentity = ObjectIdentity
icfVgMonGroup = _IcfVgMonGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 2)
)
_IcfVgMonPort_ObjectIdentity = ObjectIdentity
icfVgMonPort = _IcfVgMonPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3)
)
_IcfVgMonPortTable_Object = MibTable
icfVgMonPortTable = _IcfVgMonPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    icfVgMonPortTable.setStatus("current")
_IcfVgMonPortEntry_Object = MibTableRow
icfVgMonPortEntry = _IcfVgMonPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1)
)
icfVgMonPortEntry.setIndexNames(
    (0, "ICF-VG-RPTR", "icfVgPortGroupIndex"),
    (0, "ICF-VG-RPTR", "icfVgPortIndex"),
)
if mibBuilder.loadTexts:
    icfVgMonPortEntry.setStatus("current")
_IcfVgPortReadableFrames_Type = Counter32
_IcfVgPortReadableFrames_Object = MibTableColumn
icfVgPortReadableFrames = _IcfVgPortReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 1),
    _IcfVgPortReadableFrames_Type()
)
icfVgPortReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortReadableFrames.setStatus("current")
_IcfVgPortReadableOctets_Type = Counter32
_IcfVgPortReadableOctets_Object = MibTableColumn
icfVgPortReadableOctets = _IcfVgPortReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 2),
    _IcfVgPortReadableOctets_Type()
)
icfVgPortReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortReadableOctets.setStatus("current")
_IcfVgPortUnreadableOctets_Type = Counter32
_IcfVgPortUnreadableOctets_Object = MibTableColumn
icfVgPortUnreadableOctets = _IcfVgPortUnreadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 3),
    _IcfVgPortUnreadableOctets_Type()
)
icfVgPortUnreadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortUnreadableOctets.setStatus("current")
_IcfVgPortHighPriorityFrames_Type = Counter32
_IcfVgPortHighPriorityFrames_Object = MibTableColumn
icfVgPortHighPriorityFrames = _IcfVgPortHighPriorityFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 4),
    _IcfVgPortHighPriorityFrames_Type()
)
icfVgPortHighPriorityFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortHighPriorityFrames.setStatus("current")
_IcfVgPortHighPriorityOctets_Type = Counter32
_IcfVgPortHighPriorityOctets_Object = MibTableColumn
icfVgPortHighPriorityOctets = _IcfVgPortHighPriorityOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 5),
    _IcfVgPortHighPriorityOctets_Type()
)
icfVgPortHighPriorityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortHighPriorityOctets.setStatus("current")
_IcfVgPortBroadcastFrames_Type = Counter32
_IcfVgPortBroadcastFrames_Object = MibTableColumn
icfVgPortBroadcastFrames = _IcfVgPortBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 6),
    _IcfVgPortBroadcastFrames_Type()
)
icfVgPortBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortBroadcastFrames.setStatus("current")
_IcfVgPortMulticastFrames_Type = Counter32
_IcfVgPortMulticastFrames_Object = MibTableColumn
icfVgPortMulticastFrames = _IcfVgPortMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 7),
    _IcfVgPortMulticastFrames_Type()
)
icfVgPortMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortMulticastFrames.setStatus("current")
_IcfVgPortIPMFrames_Type = Counter32
_IcfVgPortIPMFrames_Object = MibTableColumn
icfVgPortIPMFrames = _IcfVgPortIPMFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 8),
    _IcfVgPortIPMFrames_Type()
)
icfVgPortIPMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortIPMFrames.setStatus("current")
_IcfVgPortDataErrorFrames_Type = Counter32
_IcfVgPortDataErrorFrames_Object = MibTableColumn
icfVgPortDataErrorFrames = _IcfVgPortDataErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 9),
    _IcfVgPortDataErrorFrames_Type()
)
icfVgPortDataErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortDataErrorFrames.setStatus("current")
_IcfVgPortPriorityPromotions_Type = Counter32
_IcfVgPortPriorityPromotions_Object = MibTableColumn
icfVgPortPriorityPromotions = _IcfVgPortPriorityPromotions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 10),
    _IcfVgPortPriorityPromotions_Type()
)
icfVgPortPriorityPromotions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortPriorityPromotions.setStatus("current")
_IcfVgPortHCReadableOctets_Type = Counter64
_IcfVgPortHCReadableOctets_Object = MibTableColumn
icfVgPortHCReadableOctets = _IcfVgPortHCReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 11),
    _IcfVgPortHCReadableOctets_Type()
)
icfVgPortHCReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortHCReadableOctets.setStatus("current")
_IcfVgPortHCUnreadableOctets_Type = Counter64
_IcfVgPortHCUnreadableOctets_Object = MibTableColumn
icfVgPortHCUnreadableOctets = _IcfVgPortHCUnreadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 12),
    _IcfVgPortHCUnreadableOctets_Type()
)
icfVgPortHCUnreadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortHCUnreadableOctets.setStatus("current")
_IcfVgPortHCHighPriorityOctets_Type = Counter64
_IcfVgPortHCHighPriorityOctets_Object = MibTableColumn
icfVgPortHCHighPriorityOctets = _IcfVgPortHCHighPriorityOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 13),
    _IcfVgPortHCHighPriorityOctets_Type()
)
icfVgPortHCHighPriorityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortHCHighPriorityOctets.setStatus("current")
_IcfVgPortHCNormPriorityOctets_Type = Counter64
_IcfVgPortHCNormPriorityOctets_Object = MibTableColumn
icfVgPortHCNormPriorityOctets = _IcfVgPortHCNormPriorityOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 14),
    _IcfVgPortHCNormPriorityOctets_Type()
)
icfVgPortHCNormPriorityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortHCNormPriorityOctets.setStatus("current")
_IcfVgPortNormPriorityFrames_Type = Counter32
_IcfVgPortNormPriorityFrames_Object = MibTableColumn
icfVgPortNormPriorityFrames = _IcfVgPortNormPriorityFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 15),
    _IcfVgPortNormPriorityFrames_Type()
)
icfVgPortNormPriorityFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortNormPriorityFrames.setStatus("current")
_IcfVgPortNormPriorityOctets_Type = Counter32
_IcfVgPortNormPriorityOctets_Object = MibTableColumn
icfVgPortNormPriorityOctets = _IcfVgPortNormPriorityOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 16),
    _IcfVgPortNormPriorityOctets_Type()
)
icfVgPortNormPriorityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortNormPriorityOctets.setStatus("current")
_IcfVgPortNullAddressedFrames_Type = Counter32
_IcfVgPortNullAddressedFrames_Object = MibTableColumn
icfVgPortNullAddressedFrames = _IcfVgPortNullAddressedFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 17),
    _IcfVgPortNullAddressedFrames_Type()
)
icfVgPortNullAddressedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortNullAddressedFrames.setStatus("current")
_IcfVgPortOversizeFrames_Type = Counter32
_IcfVgPortOversizeFrames_Object = MibTableColumn
icfVgPortOversizeFrames = _IcfVgPortOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 18),
    _IcfVgPortOversizeFrames_Type()
)
icfVgPortOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortOversizeFrames.setStatus("current")
_IcfVgPortTransitionToTrainings_Type = Counter32
_IcfVgPortTransitionToTrainings_Object = MibTableColumn
icfVgPortTransitionToTrainings = _IcfVgPortTransitionToTrainings_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 19),
    _IcfVgPortTransitionToTrainings_Type()
)
icfVgPortTransitionToTrainings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortTransitionToTrainings.setStatus("current")
_IcfVgAddrTrack_ObjectIdentity = ObjectIdentity
icfVgAddrTrack = _IcfVgAddrTrack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3)
)
_IcfVgAddrTrackRptr_ObjectIdentity = ObjectIdentity
icfVgAddrTrackRptr = _IcfVgAddrTrackRptr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 1)
)
_IcfVgAddrTrackGroup_ObjectIdentity = ObjectIdentity
icfVgAddrTrackGroup = _IcfVgAddrTrackGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 2)
)
_IcfVgAddrTrackPort_ObjectIdentity = ObjectIdentity
icfVgAddrTrackPort = _IcfVgAddrTrackPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 3)
)
_IcfVgAddrTrackTable_Object = MibTable
icfVgAddrTrackTable = _IcfVgAddrTrackTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    icfVgAddrTrackTable.setStatus("current")
_IcfVgAddrTrackEntry_Object = MibTableRow
icfVgAddrTrackEntry = _IcfVgAddrTrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 3, 1, 1)
)
icfVgAddrTrackEntry.setIndexNames(
    (0, "ICF-VG-RPTR", "icfVgPortGroupIndex"),
    (0, "ICF-VG-RPTR", "icfVgPortIndex"),
)
if mibBuilder.loadTexts:
    icfVgAddrTrackEntry.setStatus("current")


class _IcfVgAddrLastTrainedAddress_Type(OctetString):
    """Custom type icfVgAddrLastTrainedAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
    )


_IcfVgAddrLastTrainedAddress_Type.__name__ = "OctetString"
_IcfVgAddrLastTrainedAddress_Object = MibTableColumn
icfVgAddrLastTrainedAddress = _IcfVgAddrLastTrainedAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 3, 1, 1, 1),
    _IcfVgAddrLastTrainedAddress_Type()
)
icfVgAddrLastTrainedAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgAddrLastTrainedAddress.setStatus("current")
_IcfVgAddrTrainedAddrChanges_Type = Counter32
_IcfVgAddrTrainedAddrChanges_Object = MibTableColumn
icfVgAddrTrainedAddrChanges = _IcfVgAddrTrainedAddrChanges_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 3, 1, 1, 2),
    _IcfVgAddrTrainedAddrChanges_Type()
)
icfVgAddrTrainedAddrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgAddrTrainedAddrChanges.setStatus("current")
_IcfVgRptrDetectedDupAddress_Type = TruthValue
_IcfVgRptrDetectedDupAddress_Object = MibTableColumn
icfVgRptrDetectedDupAddress = _IcfVgRptrDetectedDupAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 3, 1, 1, 3),
    _IcfVgRptrDetectedDupAddress_Type()
)
icfVgRptrDetectedDupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgRptrDetectedDupAddress.setStatus("current")
_IcfVgMgrDetectedDupAddress_Type = TruthValue
_IcfVgMgrDetectedDupAddress_Object = MibTableColumn
icfVgMgrDetectedDupAddress = _IcfVgMgrDetectedDupAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 3, 1, 1, 4),
    _IcfVgMgrDetectedDupAddress_Type()
)
icfVgMgrDetectedDupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfVgMgrDetectedDupAddress.setStatus("current")
_IcfVgRptrTraps_ObjectIdentity = ObjectIdentity
icfVgRptrTraps = _IcfVgRptrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 4)
)
_IcfVgRptrTrapsPrefix_ObjectIdentity = ObjectIdentity
icfVgRptrTrapsPrefix = _IcfVgRptrTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 4, 0)
)
_IcfVgRepeaterConformance_ObjectIdentity = ObjectIdentity
icfVgRepeaterConformance = _IcfVgRepeaterConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10, 1)
)
_IcfVgRepeaterCompliances_ObjectIdentity = ObjectIdentity
icfVgRepeaterCompliances = _IcfVgRepeaterCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10, 1, 1)
)
_IcfVgRepeaterGroups_ObjectIdentity = ObjectIdentity
icfVgRepeaterGroups = _IcfVgRepeaterGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10, 1, 2)
)

# Managed Objects groups

icfVgRptrBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10, 1, 2, 1)
)
icfVgRptrBasicGroup.setObjects(
      *(("ICF-VG-RPTR", "icfVgMACAddress"),
        ("ICF-VG-RPTR", "icfVgCurrentFramingType"),
        ("ICF-VG-RPTR", "icfVgDesiredFramingType"),
        ("ICF-VG-RPTR", "icfVgFramingCapability"),
        ("ICF-VG-RPTR", "icfVgTrainingVersion"),
        ("ICF-VG-RPTR", "icfVgRepeaterGroupCapacity"),
        ("ICF-VG-RPTR", "icfVgRepeaterHealthState"),
        ("ICF-VG-RPTR", "icfVgRepeaterHealthText"),
        ("ICF-VG-RPTR", "icfVgRepeaterReset"),
        ("ICF-VG-RPTR", "icfVgRepeaterNonDisruptTest"),
        ("ICF-VG-RPTR", "icfVgGroupDescr"),
        ("ICF-VG-RPTR", "icfVgGroupObjectID"),
        ("ICF-VG-RPTR", "icfVgGroupOperStatus"),
        ("ICF-VG-RPTR", "icfVgGroupLastOperStatusChange"),
        ("ICF-VG-RPTR", "icfVgGroupPortCapacity"),
        ("ICF-VG-RPTR", "icfVgGroupCablesBundled"),
        ("ICF-VG-RPTR", "icfVgPortType"),
        ("ICF-VG-RPTR", "icfVgPortAdminStatus"),
        ("ICF-VG-RPTR", "icfVgPortStatus"),
        ("ICF-VG-RPTR", "icfVgPortSupportedPromiscMode"),
        ("ICF-VG-RPTR", "icfVgPortSupportedCascadeMode"),
        ("ICF-VG-RPTR", "icfVgPortAllowedTrainType"),
        ("ICF-VG-RPTR", "icfVgPortLastTrainConfig"),
        ("ICF-VG-RPTR", "icfVgPortTrainingResult"),
        ("ICF-VG-RPTR", "icfVgPortPriorityEnable"),
        ("ICF-VG-RPTR", "icfVgPortMediaType"))
)
if mibBuilder.loadTexts:
    icfVgRptrBasicGroup.setStatus("current")

icfVgRptrPreStdMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10, 1, 2, 2)
)
icfVgRptrPreStdMonitorGroup.setObjects(
      *(("ICF-VG-RPTR", "icfVgPortReadableFrames"),
        ("ICF-VG-RPTR", "icfVgPortReadableOctets"),
        ("ICF-VG-RPTR", "icfVgPortUnreadableOctets"),
        ("ICF-VG-RPTR", "icfVgPortHighPriorityFrames"),
        ("ICF-VG-RPTR", "icfVgPortHighPriorityOctets"),
        ("ICF-VG-RPTR", "icfVgPortBroadcastFrames"),
        ("ICF-VG-RPTR", "icfVgPortMulticastFrames"),
        ("ICF-VG-RPTR", "icfVgPortIPMFrames"),
        ("ICF-VG-RPTR", "icfVgPortDataErrorFrames"),
        ("ICF-VG-RPTR", "icfVgPortPriorityPromotions"),
        ("ICF-VG-RPTR", "icfVgPortHCReadableOctets"),
        ("ICF-VG-RPTR", "icfVgPortHCUnreadableOctets"),
        ("ICF-VG-RPTR", "icfVgPortHCHighPriorityOctets"))
)
if mibBuilder.loadTexts:
    icfVgRptrPreStdMonitorGroup.setStatus("obsolete")

icfVgRptrPreStdAddrTrackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10, 1, 2, 3)
)
icfVgRptrPreStdAddrTrackGroup.setObjects(
      *(("ICF-VG-RPTR", "icfVgAddrLastTrainedAddress"),
        ("ICF-VG-RPTR", "icfVgAddrTrainedAddrChanges"))
)
if mibBuilder.loadTexts:
    icfVgRptrPreStdAddrTrackGroup.setStatus("obsolete")

icfVgRptrMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10, 1, 2, 4)
)
icfVgRptrMonitorGroup.setObjects(
      *(("ICF-VG-RPTR", "icfVgPortReadableFrames"),
        ("ICF-VG-RPTR", "icfVgPortReadableOctets"),
        ("ICF-VG-RPTR", "icfVgPortUnreadableOctets"),
        ("ICF-VG-RPTR", "icfVgPortHighPriorityFrames"),
        ("ICF-VG-RPTR", "icfVgPortHighPriorityOctets"),
        ("ICF-VG-RPTR", "icfVgPortBroadcastFrames"),
        ("ICF-VG-RPTR", "icfVgPortMulticastFrames"),
        ("ICF-VG-RPTR", "icfVgPortIPMFrames"),
        ("ICF-VG-RPTR", "icfVgPortDataErrorFrames"),
        ("ICF-VG-RPTR", "icfVgPortPriorityPromotions"),
        ("ICF-VG-RPTR", "icfVgPortHCReadableOctets"),
        ("ICF-VG-RPTR", "icfVgPortHCUnreadableOctets"),
        ("ICF-VG-RPTR", "icfVgPortHCHighPriorityOctets"),
        ("ICF-VG-RPTR", "icfVgPortHCNormPriorityOctets"),
        ("ICF-VG-RPTR", "icfVgPortNormPriorityFrames"),
        ("ICF-VG-RPTR", "icfVgPortNormPriorityOctets"),
        ("ICF-VG-RPTR", "icfVgPortNullAddressedFrames"),
        ("ICF-VG-RPTR", "icfVgPortOversizeFrames"),
        ("ICF-VG-RPTR", "icfVgPortTransitionToTrainings"))
)
if mibBuilder.loadTexts:
    icfVgRptrMonitorGroup.setStatus("current")

icfVgRptrAddrTrackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10, 1, 2, 5)
)
icfVgRptrAddrTrackGroup.setObjects(
      *(("ICF-VG-RPTR", "icfVgAddrLastTrainedAddress"),
        ("ICF-VG-RPTR", "icfVgAddrTrainedAddrChanges"),
        ("ICF-VG-RPTR", "icfVgRptrDetectedDupAddress"),
        ("ICF-VG-RPTR", "icfVgMgrDetectedDupAddress"))
)
if mibBuilder.loadTexts:
    icfVgRptrAddrTrackGroup.setStatus("current")


# Notification objects

icfVgRptrHealth = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 4, 0, 1)
)
icfVgRptrHealth.setObjects(
    ("ICF-VG-RPTR", "icfVgRepeaterHealthState")
)
if mibBuilder.loadTexts:
    icfVgRptrHealth.setStatus(
        "current"
    )

icfVgRptrResetEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 4, 0, 3)
)
icfVgRptrResetEvent.setObjects(
    ("ICF-VG-RPTR", "icfVgRepeaterHealthState")
)
if mibBuilder.loadTexts:
    icfVgRptrResetEvent.setStatus(
        "current"
    )


# Notifications groups

icfVgRptrNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10, 1, 2, 6)
)
icfVgRptrNotificationsGroup.setObjects(
      *(("ICF-VG-RPTR", "icfVgRptrHealth"),
        ("ICF-VG-RPTR", "icfVgRptrResetEvent"))
)
if mibBuilder.loadTexts:
    icfVgRptrNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

icfVgRptrPreStdCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10, 1, 1, 1)
)
if mibBuilder.loadTexts:
    icfVgRptrPreStdCompliance.setStatus(
        "obsolete"
    )

icfVgRptrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10, 1, 1, 2)
)
if mibBuilder.loadTexts:
    icfVgRptrCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ICF-VG-RPTR",
    **{"icfVgBasic": icfVgBasic,
       "icfVgBasicRptr": icfVgBasicRptr,
       "icfVgMACAddress": icfVgMACAddress,
       "icfVgCurrentFramingType": icfVgCurrentFramingType,
       "icfVgDesiredFramingType": icfVgDesiredFramingType,
       "icfVgFramingCapability": icfVgFramingCapability,
       "icfVgTrainingVersion": icfVgTrainingVersion,
       "icfVgRepeaterGroupCapacity": icfVgRepeaterGroupCapacity,
       "icfVgRepeaterHealthState": icfVgRepeaterHealthState,
       "icfVgRepeaterHealthText": icfVgRepeaterHealthText,
       "icfVgRepeaterReset": icfVgRepeaterReset,
       "icfVgRepeaterNonDisruptTest": icfVgRepeaterNonDisruptTest,
       "icfVgBasicGroup": icfVgBasicGroup,
       "icfVgBasicGroupTable": icfVgBasicGroupTable,
       "icfVgBasicGroupEntry": icfVgBasicGroupEntry,
       "icfVgGroupIndex": icfVgGroupIndex,
       "icfVgGroupDescr": icfVgGroupDescr,
       "icfVgGroupObjectID": icfVgGroupObjectID,
       "icfVgGroupOperStatus": icfVgGroupOperStatus,
       "icfVgGroupLastOperStatusChange": icfVgGroupLastOperStatusChange,
       "icfVgGroupPortCapacity": icfVgGroupPortCapacity,
       "icfVgGroupCablesBundled": icfVgGroupCablesBundled,
       "icfVgBasicPort": icfVgBasicPort,
       "icfVgBasicPortTable": icfVgBasicPortTable,
       "icfVgBasicPortEntry": icfVgBasicPortEntry,
       "icfVgPortGroupIndex": icfVgPortGroupIndex,
       "icfVgPortIndex": icfVgPortIndex,
       "icfVgPortType": icfVgPortType,
       "icfVgPortAdminStatus": icfVgPortAdminStatus,
       "icfVgPortStatus": icfVgPortStatus,
       "icfVgPortSupportedPromiscMode": icfVgPortSupportedPromiscMode,
       "icfVgPortSupportedCascadeMode": icfVgPortSupportedCascadeMode,
       "icfVgPortAllowedTrainType": icfVgPortAllowedTrainType,
       "icfVgPortLastTrainConfig": icfVgPortLastTrainConfig,
       "icfVgPortTrainingResult": icfVgPortTrainingResult,
       "icfVgPortPriorityEnable": icfVgPortPriorityEnable,
       "icfVgPortMediaType": icfVgPortMediaType,
       "icfVgMonitor": icfVgMonitor,
       "icfVgMonRptr": icfVgMonRptr,
       "icfVgMonGroup": icfVgMonGroup,
       "icfVgMonPort": icfVgMonPort,
       "icfVgMonPortTable": icfVgMonPortTable,
       "icfVgMonPortEntry": icfVgMonPortEntry,
       "icfVgPortReadableFrames": icfVgPortReadableFrames,
       "icfVgPortReadableOctets": icfVgPortReadableOctets,
       "icfVgPortUnreadableOctets": icfVgPortUnreadableOctets,
       "icfVgPortHighPriorityFrames": icfVgPortHighPriorityFrames,
       "icfVgPortHighPriorityOctets": icfVgPortHighPriorityOctets,
       "icfVgPortBroadcastFrames": icfVgPortBroadcastFrames,
       "icfVgPortMulticastFrames": icfVgPortMulticastFrames,
       "icfVgPortIPMFrames": icfVgPortIPMFrames,
       "icfVgPortDataErrorFrames": icfVgPortDataErrorFrames,
       "icfVgPortPriorityPromotions": icfVgPortPriorityPromotions,
       "icfVgPortHCReadableOctets": icfVgPortHCReadableOctets,
       "icfVgPortHCUnreadableOctets": icfVgPortHCUnreadableOctets,
       "icfVgPortHCHighPriorityOctets": icfVgPortHCHighPriorityOctets,
       "icfVgPortHCNormPriorityOctets": icfVgPortHCNormPriorityOctets,
       "icfVgPortNormPriorityFrames": icfVgPortNormPriorityFrames,
       "icfVgPortNormPriorityOctets": icfVgPortNormPriorityOctets,
       "icfVgPortNullAddressedFrames": icfVgPortNullAddressedFrames,
       "icfVgPortOversizeFrames": icfVgPortOversizeFrames,
       "icfVgPortTransitionToTrainings": icfVgPortTransitionToTrainings,
       "icfVgAddrTrack": icfVgAddrTrack,
       "icfVgAddrTrackRptr": icfVgAddrTrackRptr,
       "icfVgAddrTrackGroup": icfVgAddrTrackGroup,
       "icfVgAddrTrackPort": icfVgAddrTrackPort,
       "icfVgAddrTrackTable": icfVgAddrTrackTable,
       "icfVgAddrTrackEntry": icfVgAddrTrackEntry,
       "icfVgAddrLastTrainedAddress": icfVgAddrLastTrainedAddress,
       "icfVgAddrTrainedAddrChanges": icfVgAddrTrainedAddrChanges,
       "icfVgRptrDetectedDupAddress": icfVgRptrDetectedDupAddress,
       "icfVgMgrDetectedDupAddress": icfVgMgrDetectedDupAddress,
       "icfVgRptrTraps": icfVgRptrTraps,
       "icfVgRptrTrapsPrefix": icfVgRptrTrapsPrefix,
       "icfVgRptrHealth": icfVgRptrHealth,
       "icfVgRptrResetEvent": icfVgRptrResetEvent,
       "icfVgRepeaterMib": icfVgRepeaterMib,
       "icfVgRepeaterConformance": icfVgRepeaterConformance,
       "icfVgRepeaterCompliances": icfVgRepeaterCompliances,
       "icfVgRptrPreStdCompliance": icfVgRptrPreStdCompliance,
       "icfVgRptrCompliance": icfVgRptrCompliance,
       "icfVgRepeaterGroups": icfVgRepeaterGroups,
       "icfVgRptrBasicGroup": icfVgRptrBasicGroup,
       "icfVgRptrPreStdMonitorGroup": icfVgRptrPreStdMonitorGroup,
       "icfVgRptrPreStdAddrTrackGroup": icfVgRptrPreStdAddrTrackGroup,
       "icfVgRptrMonitorGroup": icfVgRptrMonitorGroup,
       "icfVgRptrAddrTrackGroup": icfVgRptrAddrTrackGroup,
       "icfVgRptrNotificationsGroup": icfVgRptrNotificationsGroup}
)
