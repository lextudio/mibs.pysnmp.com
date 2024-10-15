# SNMP MIB module (CISCO-OPTICAL-IF-EXTN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-OPTICAL-IF-EXTN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:22 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoOpticalIfExtnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 66)
)
ciscoOpticalIfExtnMIB.setRevisions(
        ("2004-11-19 00:00",
         "2003-12-29 00:00",
         "2002-05-23 00:00",
         "2001-04-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CoDwdmFrequency(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )



class CoDwdmFrequencyOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )



# MIB Managed Objects in the order of their OIDs

_CoIfExtnMIBObjects_ObjectIdentity = ObjectIdentity
coIfExtnMIBObjects = _CoIfExtnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1)
)
_CoIfTypeExtnGroup_ObjectIdentity = ObjectIdentity
coIfTypeExtnGroup = _CoIfTypeExtnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 1)
)
_CoIfTypeExtnTable_Object = MibTable
coIfTypeExtnTable = _CoIfTypeExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 1, 1)
)
if mibBuilder.loadTexts:
    coIfTypeExtnTable.setStatus("current")
_CoIfTypeExtnEntry_Object = MibTableRow
coIfTypeExtnEntry = _CoIfTypeExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 1, 1, 1)
)
coIfTypeExtnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    coIfTypeExtnEntry.setStatus("current")


class _CoIfTypeExtn_Type(Integer32):
    """Custom type coIfTypeExtn based on Integer32"""
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
        *(("esconPhy", 7),
          ("ethernetPhy", 6),
          ("gigabitPhy", 8),
          ("multiRate", 11),
          ("opticalTransponder", 1),
          ("sonetPhy", 10),
          ("twoGigabitPhy", 9),
          ("wavelengthTransport", 5),
          ("wdmChannel", 3),
          ("wdmChannelGroup", 4),
          ("wdmTransport", 2))
    )


_CoIfTypeExtn_Type.__name__ = "Integer32"
_CoIfTypeExtn_Object = MibTableColumn
coIfTypeExtn = _CoIfTypeExtn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 1, 1, 1, 1),
    _CoIfTypeExtn_Type()
)
coIfTypeExtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coIfTypeExtn.setStatus("current")
_CoIfWavelengthGroup_ObjectIdentity = ObjectIdentity
coIfWavelengthGroup = _CoIfWavelengthGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 2)
)
_CoIfWavelengthTable_Object = MibTable
coIfWavelengthTable = _CoIfWavelengthTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 2, 1)
)
if mibBuilder.loadTexts:
    coIfWavelengthTable.setStatus("current")
_CoIfWavelengthEntry_Object = MibTableRow
coIfWavelengthEntry = _CoIfWavelengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 2, 1, 1)
)
coIfWavelengthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    coIfWavelengthEntry.setStatus("current")
_CoIfDwdmFrequency_Type = CoDwdmFrequency
_CoIfDwdmFrequency_Object = MibTableColumn
coIfDwdmFrequency = _CoIfDwdmFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 2, 1, 1, 1),
    _CoIfDwdmFrequency_Type()
)
coIfDwdmFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coIfDwdmFrequency.setStatus("current")
if mibBuilder.loadTexts:
    coIfDwdmFrequency.setUnits("GHz")
_CoIfDwdmChannelGroup_ObjectIdentity = ObjectIdentity
coIfDwdmChannelGroup = _CoIfDwdmChannelGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 3)
)
_CoIfDwdmChannelGroupTable_Object = MibTable
coIfDwdmChannelGroupTable = _CoIfDwdmChannelGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 3, 3)
)
if mibBuilder.loadTexts:
    coIfDwdmChannelGroupTable.setStatus("current")
_CoIfDwdmChannelGroupEntry_Object = MibTableRow
coIfDwdmChannelGroupEntry = _CoIfDwdmChannelGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 3, 3, 1)
)
coIfDwdmChannelGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    coIfDwdmChannelGroupEntry.setStatus("current")
_CoIfDwdmChannelGroupMinFrequency_Type = CoDwdmFrequency
_CoIfDwdmChannelGroupMinFrequency_Object = MibTableColumn
coIfDwdmChannelGroupMinFrequency = _CoIfDwdmChannelGroupMinFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 3, 3, 1, 1),
    _CoIfDwdmChannelGroupMinFrequency_Type()
)
coIfDwdmChannelGroupMinFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coIfDwdmChannelGroupMinFrequency.setStatus("current")
if mibBuilder.loadTexts:
    coIfDwdmChannelGroupMinFrequency.setUnits("GHz")


class _CoIfDwdmChannelGroupSpacing_Type(Unsigned32):
    """Custom type coIfDwdmChannelGroupSpacing based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CoIfDwdmChannelGroupSpacing_Type.__name__ = "Unsigned32"
_CoIfDwdmChannelGroupSpacing_Object = MibTableColumn
coIfDwdmChannelGroupSpacing = _CoIfDwdmChannelGroupSpacing_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 3, 3, 1, 2),
    _CoIfDwdmChannelGroupSpacing_Type()
)
coIfDwdmChannelGroupSpacing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coIfDwdmChannelGroupSpacing.setStatus("current")
if mibBuilder.loadTexts:
    coIfDwdmChannelGroupSpacing.setUnits("GHz")


class _CoIfDwdmChannelGroupBitmapLogic_Type(Integer32):
    """Custom type coIfDwdmChannelGroupBitmapLogic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 2),
          ("carried", 1))
    )


_CoIfDwdmChannelGroupBitmapLogic_Type.__name__ = "Integer32"
_CoIfDwdmChannelGroupBitmapLogic_Object = MibTableColumn
coIfDwdmChannelGroupBitmapLogic = _CoIfDwdmChannelGroupBitmapLogic_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 3, 3, 1, 3),
    _CoIfDwdmChannelGroupBitmapLogic_Type()
)
coIfDwdmChannelGroupBitmapLogic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coIfDwdmChannelGroupBitmapLogic.setStatus("current")


class _CoIfDwdmChannelGroupBitmap_Type(OctetString):
    """Custom type coIfDwdmChannelGroupBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CoIfDwdmChannelGroupBitmap_Type.__name__ = "OctetString"
_CoIfDwdmChannelGroupBitmap_Object = MibTableColumn
coIfDwdmChannelGroupBitmap = _CoIfDwdmChannelGroupBitmap_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 3, 3, 1, 4),
    _CoIfDwdmChannelGroupBitmap_Type()
)
coIfDwdmChannelGroupBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coIfDwdmChannelGroupBitmap.setStatus("current")
_CoIfXcvrGroup_ObjectIdentity = ObjectIdentity
coIfXcvrGroup = _CoIfXcvrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 4)
)
_CoIfXcvrTable_Object = MibTable
coIfXcvrTable = _CoIfXcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 4, 1)
)
if mibBuilder.loadTexts:
    coIfXcvrTable.setStatus("current")
_CoIfXcvrEntry_Object = MibTableRow
coIfXcvrEntry = _CoIfXcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 4, 1, 1)
)
coIfXcvrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    coIfXcvrEntry.setStatus("current")


class _CoIfXcvrLaserAdminStatus_Type(Integer32):
    """Custom type coIfXcvrLaserAdminStatus based on Integer32"""
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


_CoIfXcvrLaserAdminStatus_Type.__name__ = "Integer32"
_CoIfXcvrLaserAdminStatus_Object = MibTableColumn
coIfXcvrLaserAdminStatus = _CoIfXcvrLaserAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 4, 1, 1, 1),
    _CoIfXcvrLaserAdminStatus_Type()
)
coIfXcvrLaserAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coIfXcvrLaserAdminStatus.setStatus("current")


class _CoIfXcvrLaserOperStatus_Type(Integer32):
    """Custom type coIfXcvrLaserOperStatus based on Integer32"""
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
        *(("degraded", 2),
          ("down", 3),
          ("flcDown", 5),
          ("lscDown", 4),
          ("transmitting", 1),
          ("unknown", 6))
    )


_CoIfXcvrLaserOperStatus_Type.__name__ = "Integer32"
_CoIfXcvrLaserOperStatus_Object = MibTableColumn
coIfXcvrLaserOperStatus = _CoIfXcvrLaserOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 4, 1, 1, 2),
    _CoIfXcvrLaserOperStatus_Type()
)
coIfXcvrLaserOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coIfXcvrLaserOperStatus.setStatus("current")
_CoIfXcvrMinLaserFrequency_Type = CoDwdmFrequencyOrZero
_CoIfXcvrMinLaserFrequency_Object = MibTableColumn
coIfXcvrMinLaserFrequency = _CoIfXcvrMinLaserFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 4, 1, 1, 3),
    _CoIfXcvrMinLaserFrequency_Type()
)
coIfXcvrMinLaserFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coIfXcvrMinLaserFrequency.setStatus("current")
if mibBuilder.loadTexts:
    coIfXcvrMinLaserFrequency.setUnits("GHz")


class _CoIfXcvrLaserFrequencySpacing_Type(Unsigned32):
    """Custom type coIfXcvrLaserFrequencySpacing based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CoIfXcvrLaserFrequencySpacing_Type.__name__ = "Unsigned32"
_CoIfXcvrLaserFrequencySpacing_Object = MibTableColumn
coIfXcvrLaserFrequencySpacing = _CoIfXcvrLaserFrequencySpacing_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 4, 1, 1, 4),
    _CoIfXcvrLaserFrequencySpacing_Type()
)
coIfXcvrLaserFrequencySpacing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coIfXcvrLaserFrequencySpacing.setStatus("current")
if mibBuilder.loadTexts:
    coIfXcvrLaserFrequencySpacing.setUnits("GHz")


class _CoIfXcvrLaserFrequencyBitmap_Type(OctetString):
    """Custom type coIfXcvrLaserFrequencyBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CoIfXcvrLaserFrequencyBitmap_Type.__name__ = "OctetString"
_CoIfXcvrLaserFrequencyBitmap_Object = MibTableColumn
coIfXcvrLaserFrequencyBitmap = _CoIfXcvrLaserFrequencyBitmap_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 4, 1, 1, 5),
    _CoIfXcvrLaserFrequencyBitmap_Type()
)
coIfXcvrLaserFrequencyBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coIfXcvrLaserFrequencyBitmap.setStatus("current")


class _CoIfXcvrForwardLaserControl_Type(Integer32):
    """Custom type coIfXcvrForwardLaserControl based on Integer32"""
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


_CoIfXcvrForwardLaserControl_Type.__name__ = "Integer32"
_CoIfXcvrForwardLaserControl_Object = MibTableColumn
coIfXcvrForwardLaserControl = _CoIfXcvrForwardLaserControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 4, 1, 1, 6),
    _CoIfXcvrForwardLaserControl_Type()
)
coIfXcvrForwardLaserControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coIfXcvrForwardLaserControl.setStatus("current")


class _CoIfXcvrLaserSafetyControl_Type(Integer32):
    """Custom type coIfXcvrLaserSafetyControl based on Integer32"""
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


_CoIfXcvrLaserSafetyControl_Type.__name__ = "Integer32"
_CoIfXcvrLaserSafetyControl_Object = MibTableColumn
coIfXcvrLaserSafetyControl = _CoIfXcvrLaserSafetyControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 4, 1, 1, 7),
    _CoIfXcvrLaserSafetyControl_Type()
)
coIfXcvrLaserSafetyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coIfXcvrLaserSafetyControl.setStatus("current")


class _CoIfXcvrLSCProtocol_Type(Integer32):
    """Custom type coIfXcvrLSCProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("g664", 2),
          ("proprietary", 1))
    )


_CoIfXcvrLSCProtocol_Type.__name__ = "Integer32"
_CoIfXcvrLSCProtocol_Object = MibTableColumn
coIfXcvrLSCProtocol = _CoIfXcvrLSCProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 4, 1, 1, 8),
    _CoIfXcvrLSCProtocol_Type()
)
coIfXcvrLSCProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coIfXcvrLSCProtocol.setStatus("current")


class _CoIfXcvrLSCRestartMode_Type(Integer32):
    """Custom type coIfXcvrLSCRestartMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automaticRestart", 1),
          ("manualRestart", 2))
    )


_CoIfXcvrLSCRestartMode_Type.__name__ = "Integer32"
_CoIfXcvrLSCRestartMode_Object = MibTableColumn
coIfXcvrLSCRestartMode = _CoIfXcvrLSCRestartMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 4, 1, 1, 9),
    _CoIfXcvrLSCRestartMode_Type()
)
coIfXcvrLSCRestartMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coIfXcvrLSCRestartMode.setStatus("current")


class _CoIfXcvrLSCManualRestart_Type(Integer32):
    """Custom type coIfXcvrLSCManualRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("restart", 2),
          ("restartForTest", 3))
    )


_CoIfXcvrLSCManualRestart_Type.__name__ = "Integer32"
_CoIfXcvrLSCManualRestart_Object = MibTableColumn
coIfXcvrLSCManualRestart = _CoIfXcvrLSCManualRestart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 4, 1, 1, 10),
    _CoIfXcvrLSCManualRestart_Type()
)
coIfXcvrLSCManualRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coIfXcvrLSCManualRestart.setStatus("current")


class _CoIfXcvrLSCPulseLength_Type(Unsigned32):
    """Custom type coIfXcvrLSCPulseLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 20000),
    )


_CoIfXcvrLSCPulseLength_Type.__name__ = "Unsigned32"
_CoIfXcvrLSCPulseLength_Object = MibTableColumn
coIfXcvrLSCPulseLength = _CoIfXcvrLSCPulseLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 4, 1, 1, 11),
    _CoIfXcvrLSCPulseLength_Type()
)
coIfXcvrLSCPulseLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coIfXcvrLSCPulseLength.setStatus("current")
if mibBuilder.loadTexts:
    coIfXcvrLSCPulseLength.setUnits("milliseconds")


class _CoIfXcvrLSCTestPulseLength_Type(Unsigned32):
    """Custom type coIfXcvrLSCTestPulseLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CoIfXcvrLSCTestPulseLength_Type.__name__ = "Unsigned32"
_CoIfXcvrLSCTestPulseLength_Object = MibTableColumn
coIfXcvrLSCTestPulseLength = _CoIfXcvrLSCTestPulseLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 4, 1, 1, 12),
    _CoIfXcvrLSCTestPulseLength_Type()
)
coIfXcvrLSCTestPulseLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coIfXcvrLSCTestPulseLength.setStatus("current")
if mibBuilder.loadTexts:
    coIfXcvrLSCTestPulseLength.setUnits("seconds")


class _CoIfXcvrLSCPulseRepetitionTime_Type(Unsigned32):
    """Custom type coIfXcvrLSCPulseRepetitionTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CoIfXcvrLSCPulseRepetitionTime_Type.__name__ = "Unsigned32"
_CoIfXcvrLSCPulseRepetitionTime_Object = MibTableColumn
coIfXcvrLSCPulseRepetitionTime = _CoIfXcvrLSCPulseRepetitionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 1, 4, 1, 1, 13),
    _CoIfXcvrLSCPulseRepetitionTime_Type()
)
coIfXcvrLSCPulseRepetitionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coIfXcvrLSCPulseRepetitionTime.setStatus("current")
if mibBuilder.loadTexts:
    coIfXcvrLSCPulseRepetitionTime.setUnits("seconds")
_CoIfExtnMIBConformance_ObjectIdentity = ObjectIdentity
coIfExtnMIBConformance = _CoIfExtnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 3)
)
_CoIfExtnMIBCompliances_ObjectIdentity = ObjectIdentity
coIfExtnMIBCompliances = _CoIfExtnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 3, 1)
)
_CoIfExtnMIBGroups_ObjectIdentity = ObjectIdentity
coIfExtnMIBGroups = _CoIfExtnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 3, 2)
)

# Managed Objects groups

coIfTypeExtnMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 3, 2, 1)
)
coIfTypeExtnMIBGroup.setObjects(
    ("CISCO-OPTICAL-IF-EXTN-MIB", "coIfTypeExtn")
)
if mibBuilder.loadTexts:
    coIfTypeExtnMIBGroup.setStatus("current")

coIfWavelengthMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 3, 2, 2)
)
coIfWavelengthMIBGroup.setObjects(
    ("CISCO-OPTICAL-IF-EXTN-MIB", "coIfDwdmFrequency")
)
if mibBuilder.loadTexts:
    coIfWavelengthMIBGroup.setStatus("current")

coIfDwdmChannelGroupMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 3, 2, 3)
)
coIfDwdmChannelGroupMIBGroup.setObjects(
      *(("CISCO-OPTICAL-IF-EXTN-MIB", "coIfDwdmChannelGroupMinFrequency"),
        ("CISCO-OPTICAL-IF-EXTN-MIB", "coIfDwdmChannelGroupSpacing"),
        ("CISCO-OPTICAL-IF-EXTN-MIB", "coIfDwdmChannelGroupBitmapLogic"),
        ("CISCO-OPTICAL-IF-EXTN-MIB", "coIfDwdmChannelGroupBitmap"))
)
if mibBuilder.loadTexts:
    coIfDwdmChannelGroupMIBGroup.setStatus("current")

coIfXcvrBaseMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 3, 2, 4)
)
coIfXcvrBaseMIBGroup.setObjects(
      *(("CISCO-OPTICAL-IF-EXTN-MIB", "coIfXcvrLaserAdminStatus"),
        ("CISCO-OPTICAL-IF-EXTN-MIB", "coIfXcvrLaserOperStatus"),
        ("CISCO-OPTICAL-IF-EXTN-MIB", "coIfXcvrForwardLaserControl"))
)
if mibBuilder.loadTexts:
    coIfXcvrBaseMIBGroup.setStatus("current")

coIfXcvrTunableLaserMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 3, 2, 5)
)
coIfXcvrTunableLaserMIBGroup.setObjects(
      *(("CISCO-OPTICAL-IF-EXTN-MIB", "coIfXcvrMinLaserFrequency"),
        ("CISCO-OPTICAL-IF-EXTN-MIB", "coIfXcvrLaserFrequencySpacing"),
        ("CISCO-OPTICAL-IF-EXTN-MIB", "coIfXcvrLaserFrequencyBitmap"))
)
if mibBuilder.loadTexts:
    coIfXcvrTunableLaserMIBGroup.setStatus("current")

coIfXcvrLSCMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 3, 2, 6)
)
coIfXcvrLSCMIBGroup.setObjects(
      *(("CISCO-OPTICAL-IF-EXTN-MIB", "coIfXcvrLaserSafetyControl"),
        ("CISCO-OPTICAL-IF-EXTN-MIB", "coIfXcvrLSCProtocol"),
        ("CISCO-OPTICAL-IF-EXTN-MIB", "coIfXcvrLSCRestartMode"),
        ("CISCO-OPTICAL-IF-EXTN-MIB", "coIfXcvrLSCManualRestart"),
        ("CISCO-OPTICAL-IF-EXTN-MIB", "coIfXcvrLSCPulseLength"),
        ("CISCO-OPTICAL-IF-EXTN-MIB", "coIfXcvrLSCTestPulseLength"),
        ("CISCO-OPTICAL-IF-EXTN-MIB", "coIfXcvrLSCPulseRepetitionTime"))
)
if mibBuilder.loadTexts:
    coIfXcvrLSCMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

coIfExtnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 3, 1, 1)
)
if mibBuilder.loadTexts:
    coIfExtnMIBCompliance.setStatus(
        "deprecated"
    )

coIfExtnMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 66, 3, 1, 2)
)
if mibBuilder.loadTexts:
    coIfExtnMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-OPTICAL-IF-EXTN-MIB",
    **{"CoDwdmFrequency": CoDwdmFrequency,
       "CoDwdmFrequencyOrZero": CoDwdmFrequencyOrZero,
       "ciscoOpticalIfExtnMIB": ciscoOpticalIfExtnMIB,
       "coIfExtnMIBObjects": coIfExtnMIBObjects,
       "coIfTypeExtnGroup": coIfTypeExtnGroup,
       "coIfTypeExtnTable": coIfTypeExtnTable,
       "coIfTypeExtnEntry": coIfTypeExtnEntry,
       "coIfTypeExtn": coIfTypeExtn,
       "coIfWavelengthGroup": coIfWavelengthGroup,
       "coIfWavelengthTable": coIfWavelengthTable,
       "coIfWavelengthEntry": coIfWavelengthEntry,
       "coIfDwdmFrequency": coIfDwdmFrequency,
       "coIfDwdmChannelGroup": coIfDwdmChannelGroup,
       "coIfDwdmChannelGroupTable": coIfDwdmChannelGroupTable,
       "coIfDwdmChannelGroupEntry": coIfDwdmChannelGroupEntry,
       "coIfDwdmChannelGroupMinFrequency": coIfDwdmChannelGroupMinFrequency,
       "coIfDwdmChannelGroupSpacing": coIfDwdmChannelGroupSpacing,
       "coIfDwdmChannelGroupBitmapLogic": coIfDwdmChannelGroupBitmapLogic,
       "coIfDwdmChannelGroupBitmap": coIfDwdmChannelGroupBitmap,
       "coIfXcvrGroup": coIfXcvrGroup,
       "coIfXcvrTable": coIfXcvrTable,
       "coIfXcvrEntry": coIfXcvrEntry,
       "coIfXcvrLaserAdminStatus": coIfXcvrLaserAdminStatus,
       "coIfXcvrLaserOperStatus": coIfXcvrLaserOperStatus,
       "coIfXcvrMinLaserFrequency": coIfXcvrMinLaserFrequency,
       "coIfXcvrLaserFrequencySpacing": coIfXcvrLaserFrequencySpacing,
       "coIfXcvrLaserFrequencyBitmap": coIfXcvrLaserFrequencyBitmap,
       "coIfXcvrForwardLaserControl": coIfXcvrForwardLaserControl,
       "coIfXcvrLaserSafetyControl": coIfXcvrLaserSafetyControl,
       "coIfXcvrLSCProtocol": coIfXcvrLSCProtocol,
       "coIfXcvrLSCRestartMode": coIfXcvrLSCRestartMode,
       "coIfXcvrLSCManualRestart": coIfXcvrLSCManualRestart,
       "coIfXcvrLSCPulseLength": coIfXcvrLSCPulseLength,
       "coIfXcvrLSCTestPulseLength": coIfXcvrLSCTestPulseLength,
       "coIfXcvrLSCPulseRepetitionTime": coIfXcvrLSCPulseRepetitionTime,
       "coIfExtnMIBConformance": coIfExtnMIBConformance,
       "coIfExtnMIBCompliances": coIfExtnMIBCompliances,
       "coIfExtnMIBCompliance": coIfExtnMIBCompliance,
       "coIfExtnMIBCompliance2": coIfExtnMIBCompliance2,
       "coIfExtnMIBGroups": coIfExtnMIBGroups,
       "coIfTypeExtnMIBGroup": coIfTypeExtnMIBGroup,
       "coIfWavelengthMIBGroup": coIfWavelengthMIBGroup,
       "coIfDwdmChannelGroupMIBGroup": coIfDwdmChannelGroupMIBGroup,
       "coIfXcvrBaseMIBGroup": coIfXcvrBaseMIBGroup,
       "coIfXcvrTunableLaserMIBGroup": coIfXcvrTunableLaserMIBGroup,
       "coIfXcvrLSCMIBGroup": coIfXcvrLSCMIBGroup}
)
