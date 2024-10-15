# SNMP MIB module (FIBRE-CHANNEL-FE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FIBRE-CHANNEL-FE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:51 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

fcFeMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 75)
)
fcFeMIB.setRevisions(
        ("2000-05-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MilliSeconds(Unsigned32, TextualConvention):
    status = "current"


class MicroSeconds(Unsigned32, TextualConvention):
    status = "current"


class FcNameId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class FcAddressId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class FcRxDataFieldSize(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 2112),
    )



class FcBbCredit(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )



class FcphVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class FcStackedConnMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lockedDown", 3),
          ("none", 1),
          ("transparent", 2))
    )



class FcCosCap(Bits, TextualConvention):
    status = "current"


class FcFeModuleCapacity(Unsigned32, TextualConvention):
    status = "current"


class FcFeFxPortCapacity(Unsigned32, TextualConvention):
    status = "current"


class FcFeModuleIndex(Unsigned32, TextualConvention):
    status = "current"


class FcFeFxPortIndex(Unsigned32, TextualConvention):
    status = "current"


class FcFeNxPortIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )



class FcBbCreditModel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("regular", 1))
    )



# MIB Managed Objects in the order of their OIDs

_FcFeMIBObjects_ObjectIdentity = ObjectIdentity
fcFeMIBObjects = _FcFeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 75, 1)
)
_FcFeConfig_ObjectIdentity = ObjectIdentity
fcFeConfig = _FcFeConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 75, 1, 1)
)
_FcFeFabricName_Type = FcNameId
_FcFeFabricName_Object = MibScalar
fcFeFabricName = _FcFeFabricName_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 1),
    _FcFeFabricName_Type()
)
fcFeFabricName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcFeFabricName.setStatus("current")
_FcFeElementName_Type = FcNameId
_FcFeElementName_Object = MibScalar
fcFeElementName = _FcFeElementName_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 2),
    _FcFeElementName_Type()
)
fcFeElementName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcFeElementName.setStatus("current")
_FcFeModuleCapacity_Type = FcFeModuleCapacity
_FcFeModuleCapacity_Object = MibScalar
fcFeModuleCapacity = _FcFeModuleCapacity_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 3),
    _FcFeModuleCapacity_Type()
)
fcFeModuleCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFeModuleCapacity.setStatus("current")
_FcFeModuleTable_Object = MibTable
fcFeModuleTable = _FcFeModuleTable_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 4)
)
if mibBuilder.loadTexts:
    fcFeModuleTable.setStatus("current")
_FcFeModuleEntry_Object = MibTableRow
fcFeModuleEntry = _FcFeModuleEntry_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 4, 1)
)
fcFeModuleEntry.setIndexNames(
    (0, "FIBRE-CHANNEL-FE-MIB", "fcFeModuleIndex"),
)
if mibBuilder.loadTexts:
    fcFeModuleEntry.setStatus("current")
_FcFeModuleIndex_Type = FcFeModuleIndex
_FcFeModuleIndex_Object = MibTableColumn
fcFeModuleIndex = _FcFeModuleIndex_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 4, 1, 1),
    _FcFeModuleIndex_Type()
)
fcFeModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcFeModuleIndex.setStatus("current")
_FcFeModuleDescr_Type = SnmpAdminString
_FcFeModuleDescr_Object = MibTableColumn
fcFeModuleDescr = _FcFeModuleDescr_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 4, 1, 2),
    _FcFeModuleDescr_Type()
)
fcFeModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFeModuleDescr.setStatus("current")
_FcFeModuleObjectID_Type = ObjectIdentifier
_FcFeModuleObjectID_Object = MibTableColumn
fcFeModuleObjectID = _FcFeModuleObjectID_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 4, 1, 3),
    _FcFeModuleObjectID_Type()
)
fcFeModuleObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFeModuleObjectID.setStatus("current")


class _FcFeModuleOperStatus_Type(Integer32):
    """Custom type fcFeModuleOperStatus based on Integer32"""
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
        *(("faulty", 4),
          ("offline", 2),
          ("online", 1),
          ("testing", 3))
    )


_FcFeModuleOperStatus_Type.__name__ = "Integer32"
_FcFeModuleOperStatus_Object = MibTableColumn
fcFeModuleOperStatus = _FcFeModuleOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 4, 1, 4),
    _FcFeModuleOperStatus_Type()
)
fcFeModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFeModuleOperStatus.setStatus("current")
_FcFeModuleLastChange_Type = TimeStamp
_FcFeModuleLastChange_Object = MibTableColumn
fcFeModuleLastChange = _FcFeModuleLastChange_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 4, 1, 5),
    _FcFeModuleLastChange_Type()
)
fcFeModuleLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFeModuleLastChange.setStatus("current")
_FcFeModuleFxPortCapacity_Type = FcFeFxPortCapacity
_FcFeModuleFxPortCapacity_Object = MibTableColumn
fcFeModuleFxPortCapacity = _FcFeModuleFxPortCapacity_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 4, 1, 6),
    _FcFeModuleFxPortCapacity_Type()
)
fcFeModuleFxPortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFeModuleFxPortCapacity.setStatus("current")
_FcFeModuleName_Type = FcNameId
_FcFeModuleName_Object = MibTableColumn
fcFeModuleName = _FcFeModuleName_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 4, 1, 7),
    _FcFeModuleName_Type()
)
fcFeModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcFeModuleName.setStatus("current")
_FcFxPortTable_Object = MibTable
fcFxPortTable = _FcFxPortTable_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 5)
)
if mibBuilder.loadTexts:
    fcFxPortTable.setStatus("current")
_FcFxPortEntry_Object = MibTableRow
fcFxPortEntry = _FcFxPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1)
)
fcFxPortEntry.setIndexNames(
    (0, "FIBRE-CHANNEL-FE-MIB", "fcFeModuleIndex"),
    (0, "FIBRE-CHANNEL-FE-MIB", "fcFxPortIndex"),
)
if mibBuilder.loadTexts:
    fcFxPortEntry.setStatus("current")
_FcFxPortIndex_Type = FcFeFxPortIndex
_FcFxPortIndex_Object = MibTableColumn
fcFxPortIndex = _FcFxPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 1),
    _FcFxPortIndex_Type()
)
fcFxPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcFxPortIndex.setStatus("current")
_FcFxPortName_Type = FcNameId
_FcFxPortName_Object = MibTableColumn
fcFxPortName = _FcFxPortName_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 2),
    _FcFxPortName_Type()
)
fcFxPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortName.setStatus("current")
_FcFxPortFcphVersionHigh_Type = FcphVersion
_FcFxPortFcphVersionHigh_Object = MibTableColumn
fcFxPortFcphVersionHigh = _FcFxPortFcphVersionHigh_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 3),
    _FcFxPortFcphVersionHigh_Type()
)
fcFxPortFcphVersionHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortFcphVersionHigh.setStatus("current")
_FcFxPortFcphVersionLow_Type = FcphVersion
_FcFxPortFcphVersionLow_Object = MibTableColumn
fcFxPortFcphVersionLow = _FcFxPortFcphVersionLow_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 4),
    _FcFxPortFcphVersionLow_Type()
)
fcFxPortFcphVersionLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortFcphVersionLow.setStatus("current")
_FcFxPortBbCredit_Type = FcBbCredit
_FcFxPortBbCredit_Object = MibTableColumn
fcFxPortBbCredit = _FcFxPortBbCredit_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 5),
    _FcFxPortBbCredit_Type()
)
fcFxPortBbCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortBbCredit.setStatus("current")
if mibBuilder.loadTexts:
    fcFxPortBbCredit.setUnits("buffers")
_FcFxPortRxBufSize_Type = FcRxDataFieldSize
_FcFxPortRxBufSize_Object = MibTableColumn
fcFxPortRxBufSize = _FcFxPortRxBufSize_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 6),
    _FcFxPortRxBufSize_Type()
)
fcFxPortRxBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortRxBufSize.setStatus("current")
if mibBuilder.loadTexts:
    fcFxPortRxBufSize.setUnits("bytes")
_FcFxPortRatov_Type = MilliSeconds
_FcFxPortRatov_Object = MibTableColumn
fcFxPortRatov = _FcFxPortRatov_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 7),
    _FcFxPortRatov_Type()
)
fcFxPortRatov.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortRatov.setStatus("current")
if mibBuilder.loadTexts:
    fcFxPortRatov.setUnits("milliseconds")
_FcFxPortEdtov_Type = MilliSeconds
_FcFxPortEdtov_Object = MibTableColumn
fcFxPortEdtov = _FcFxPortEdtov_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 8),
    _FcFxPortEdtov_Type()
)
fcFxPortEdtov.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortEdtov.setStatus("current")
if mibBuilder.loadTexts:
    fcFxPortEdtov.setUnits("milliseconds")
_FcFxPortCosSupported_Type = FcCosCap
_FcFxPortCosSupported_Object = MibTableColumn
fcFxPortCosSupported = _FcFxPortCosSupported_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 9),
    _FcFxPortCosSupported_Type()
)
fcFxPortCosSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCosSupported.setStatus("current")
_FcFxPortIntermixSupported_Type = TruthValue
_FcFxPortIntermixSupported_Object = MibTableColumn
fcFxPortIntermixSupported = _FcFxPortIntermixSupported_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 10),
    _FcFxPortIntermixSupported_Type()
)
fcFxPortIntermixSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortIntermixSupported.setStatus("current")
_FcFxPortStackedConnMode_Type = FcStackedConnMode
_FcFxPortStackedConnMode_Object = MibTableColumn
fcFxPortStackedConnMode = _FcFxPortStackedConnMode_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 11),
    _FcFxPortStackedConnMode_Type()
)
fcFxPortStackedConnMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortStackedConnMode.setStatus("current")
_FcFxPortClass2SeqDeliv_Type = TruthValue
_FcFxPortClass2SeqDeliv_Object = MibTableColumn
fcFxPortClass2SeqDeliv = _FcFxPortClass2SeqDeliv_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 12),
    _FcFxPortClass2SeqDeliv_Type()
)
fcFxPortClass2SeqDeliv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortClass2SeqDeliv.setStatus("current")
_FcFxPortClass3SeqDeliv_Type = TruthValue
_FcFxPortClass3SeqDeliv_Object = MibTableColumn
fcFxPortClass3SeqDeliv = _FcFxPortClass3SeqDeliv_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 13),
    _FcFxPortClass3SeqDeliv_Type()
)
fcFxPortClass3SeqDeliv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortClass3SeqDeliv.setStatus("current")
_FcFxPortHoldTime_Type = MicroSeconds
_FcFxPortHoldTime_Object = MibTableColumn
fcFxPortHoldTime = _FcFxPortHoldTime_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 1, 5, 1, 14),
    _FcFxPortHoldTime_Type()
)
fcFxPortHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    fcFxPortHoldTime.setUnits("microseconds")
_FcFeStatus_ObjectIdentity = ObjectIdentity
fcFeStatus = _FcFeStatus_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 75, 1, 2)
)
_FcFxPortStatusTable_Object = MibTable
fcFxPortStatusTable = _FcFxPortStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fcFxPortStatusTable.setStatus("current")
_FcFxPortStatusEntry_Object = MibTableRow
fcFxPortStatusEntry = _FcFxPortStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fcFxPortStatusEntry.setStatus("current")
_FcFxPortID_Type = FcAddressId
_FcFxPortID_Object = MibTableColumn
fcFxPortID = _FcFxPortID_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 1, 1, 1),
    _FcFxPortID_Type()
)
fcFxPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortID.setStatus("current")
_FcFxPortBbCreditAvailable_Type = Gauge32
_FcFxPortBbCreditAvailable_Object = MibTableColumn
fcFxPortBbCreditAvailable = _FcFxPortBbCreditAvailable_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 1, 1, 2),
    _FcFxPortBbCreditAvailable_Type()
)
fcFxPortBbCreditAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortBbCreditAvailable.setStatus("current")
if mibBuilder.loadTexts:
    fcFxPortBbCreditAvailable.setUnits("buffers")


class _FcFxPortOperMode_Type(Integer32):
    """Custom type fcFxPortOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fPort", 2),
          ("flPort", 3),
          ("unknown", 1))
    )


_FcFxPortOperMode_Type.__name__ = "Integer32"
_FcFxPortOperMode_Object = MibTableColumn
fcFxPortOperMode = _FcFxPortOperMode_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 1, 1, 3),
    _FcFxPortOperMode_Type()
)
fcFxPortOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortOperMode.setStatus("current")


class _FcFxPortAdminMode_Type(Integer32):
    """Custom type fcFxPortAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fPort", 2),
          ("flPort", 3))
    )


_FcFxPortAdminMode_Type.__name__ = "Integer32"
_FcFxPortAdminMode_Object = MibTableColumn
fcFxPortAdminMode = _FcFxPortAdminMode_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 1, 1, 4),
    _FcFxPortAdminMode_Type()
)
fcFxPortAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcFxPortAdminMode.setStatus("current")
_FcFxPortPhysTable_Object = MibTable
fcFxPortPhysTable = _FcFxPortPhysTable_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fcFxPortPhysTable.setStatus("current")
_FcFxPortPhysEntry_Object = MibTableRow
fcFxPortPhysEntry = _FcFxPortPhysEntry_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fcFxPortPhysEntry.setStatus("current")


class _FcFxPortPhysAdminStatus_Type(Integer32):
    """Custom type fcFxPortPhysAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1),
          ("testing", 3))
    )


_FcFxPortPhysAdminStatus_Type.__name__ = "Integer32"
_FcFxPortPhysAdminStatus_Object = MibTableColumn
fcFxPortPhysAdminStatus = _FcFxPortPhysAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 2, 1, 1),
    _FcFxPortPhysAdminStatus_Type()
)
fcFxPortPhysAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcFxPortPhysAdminStatus.setStatus("current")


class _FcFxPortPhysOperStatus_Type(Integer32):
    """Custom type fcFxPortPhysOperStatus based on Integer32"""
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
        *(("linkFailure", 4),
          ("offline", 2),
          ("online", 1),
          ("testing", 3))
    )


_FcFxPortPhysOperStatus_Type.__name__ = "Integer32"
_FcFxPortPhysOperStatus_Object = MibTableColumn
fcFxPortPhysOperStatus = _FcFxPortPhysOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 2, 1, 2),
    _FcFxPortPhysOperStatus_Type()
)
fcFxPortPhysOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortPhysOperStatus.setStatus("current")
_FcFxPortPhysLastChange_Type = TimeStamp
_FcFxPortPhysLastChange_Object = MibTableColumn
fcFxPortPhysLastChange = _FcFxPortPhysLastChange_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 2, 1, 3),
    _FcFxPortPhysLastChange_Type()
)
fcFxPortPhysLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortPhysLastChange.setStatus("current")
_FcFxPortPhysRttov_Type = MilliSeconds
_FcFxPortPhysRttov_Object = MibTableColumn
fcFxPortPhysRttov = _FcFxPortPhysRttov_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 2, 1, 4),
    _FcFxPortPhysRttov_Type()
)
fcFxPortPhysRttov.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcFxPortPhysRttov.setStatus("current")
if mibBuilder.loadTexts:
    fcFxPortPhysRttov.setUnits("milliseconds")
_FcFxLoginTable_Object = MibTable
fcFxLoginTable = _FcFxLoginTable_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fcFxLoginTable.setStatus("current")
_FcFxLoginEntry_Object = MibTableRow
fcFxLoginEntry = _FcFxLoginEntry_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1)
)
fcFxLoginEntry.setIndexNames(
    (0, "FIBRE-CHANNEL-FE-MIB", "fcFeModuleIndex"),
    (0, "FIBRE-CHANNEL-FE-MIB", "fcFxPortIndex"),
    (0, "FIBRE-CHANNEL-FE-MIB", "fcFxPortNxLoginIndex"),
)
if mibBuilder.loadTexts:
    fcFxLoginEntry.setStatus("current")
_FcFxPortNxLoginIndex_Type = FcFeNxPortIndex
_FcFxPortNxLoginIndex_Object = MibTableColumn
fcFxPortNxLoginIndex = _FcFxPortNxLoginIndex_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 1),
    _FcFxPortNxLoginIndex_Type()
)
fcFxPortNxLoginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcFxPortNxLoginIndex.setStatus("current")
_FcFxPortFcphVersionAgreed_Type = FcphVersion
_FcFxPortFcphVersionAgreed_Object = MibTableColumn
fcFxPortFcphVersionAgreed = _FcFxPortFcphVersionAgreed_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 2),
    _FcFxPortFcphVersionAgreed_Type()
)
fcFxPortFcphVersionAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortFcphVersionAgreed.setStatus("current")
_FcFxPortNxPortBbCredit_Type = FcBbCredit
_FcFxPortNxPortBbCredit_Object = MibTableColumn
fcFxPortNxPortBbCredit = _FcFxPortNxPortBbCredit_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 3),
    _FcFxPortNxPortBbCredit_Type()
)
fcFxPortNxPortBbCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortNxPortBbCredit.setStatus("current")
if mibBuilder.loadTexts:
    fcFxPortNxPortBbCredit.setUnits("buffers")
_FcFxPortNxPortRxDataFieldSize_Type = FcRxDataFieldSize
_FcFxPortNxPortRxDataFieldSize_Object = MibTableColumn
fcFxPortNxPortRxDataFieldSize = _FcFxPortNxPortRxDataFieldSize_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 4),
    _FcFxPortNxPortRxDataFieldSize_Type()
)
fcFxPortNxPortRxDataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortNxPortRxDataFieldSize.setStatus("current")
if mibBuilder.loadTexts:
    fcFxPortNxPortRxDataFieldSize.setUnits("bytes")
_FcFxPortCosSuppAgreed_Type = FcCosCap
_FcFxPortCosSuppAgreed_Object = MibTableColumn
fcFxPortCosSuppAgreed = _FcFxPortCosSuppAgreed_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 5),
    _FcFxPortCosSuppAgreed_Type()
)
fcFxPortCosSuppAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCosSuppAgreed.setStatus("current")
_FcFxPortIntermixSuppAgreed_Type = TruthValue
_FcFxPortIntermixSuppAgreed_Object = MibTableColumn
fcFxPortIntermixSuppAgreed = _FcFxPortIntermixSuppAgreed_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 6),
    _FcFxPortIntermixSuppAgreed_Type()
)
fcFxPortIntermixSuppAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortIntermixSuppAgreed.setStatus("current")
_FcFxPortStackedConnModeAgreed_Type = FcStackedConnMode
_FcFxPortStackedConnModeAgreed_Object = MibTableColumn
fcFxPortStackedConnModeAgreed = _FcFxPortStackedConnModeAgreed_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 7),
    _FcFxPortStackedConnModeAgreed_Type()
)
fcFxPortStackedConnModeAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortStackedConnModeAgreed.setStatus("current")
_FcFxPortClass2SeqDelivAgreed_Type = TruthValue
_FcFxPortClass2SeqDelivAgreed_Object = MibTableColumn
fcFxPortClass2SeqDelivAgreed = _FcFxPortClass2SeqDelivAgreed_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 8),
    _FcFxPortClass2SeqDelivAgreed_Type()
)
fcFxPortClass2SeqDelivAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortClass2SeqDelivAgreed.setStatus("current")
_FcFxPortClass3SeqDelivAgreed_Type = TruthValue
_FcFxPortClass3SeqDelivAgreed_Object = MibTableColumn
fcFxPortClass3SeqDelivAgreed = _FcFxPortClass3SeqDelivAgreed_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 9),
    _FcFxPortClass3SeqDelivAgreed_Type()
)
fcFxPortClass3SeqDelivAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortClass3SeqDelivAgreed.setStatus("current")
_FcFxPortNxPortName_Type = FcNameId
_FcFxPortNxPortName_Object = MibTableColumn
fcFxPortNxPortName = _FcFxPortNxPortName_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 10),
    _FcFxPortNxPortName_Type()
)
fcFxPortNxPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortNxPortName.setStatus("current")
_FcFxPortConnectedNxPort_Type = FcAddressId
_FcFxPortConnectedNxPort_Object = MibTableColumn
fcFxPortConnectedNxPort = _FcFxPortConnectedNxPort_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 11),
    _FcFxPortConnectedNxPort_Type()
)
fcFxPortConnectedNxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortConnectedNxPort.setStatus("current")
_FcFxPortBbCreditModel_Type = FcBbCreditModel
_FcFxPortBbCreditModel_Object = MibTableColumn
fcFxPortBbCreditModel = _FcFxPortBbCreditModel_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 2, 3, 1, 12),
    _FcFxPortBbCreditModel_Type()
)
fcFxPortBbCreditModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcFxPortBbCreditModel.setStatus("current")
_FcFeError_ObjectIdentity = ObjectIdentity
fcFeError = _FcFeError_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 75, 1, 3)
)
_FcFxPortErrorTable_Object = MibTable
fcFxPortErrorTable = _FcFxPortErrorTable_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fcFxPortErrorTable.setStatus("current")
_FcFxPortErrorEntry_Object = MibTableRow
fcFxPortErrorEntry = _FcFxPortErrorEntry_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    fcFxPortErrorEntry.setStatus("current")
_FcFxPortLinkFailures_Type = Counter32
_FcFxPortLinkFailures_Object = MibTableColumn
fcFxPortLinkFailures = _FcFxPortLinkFailures_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 1),
    _FcFxPortLinkFailures_Type()
)
fcFxPortLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortLinkFailures.setStatus("current")
_FcFxPortSyncLosses_Type = Counter32
_FcFxPortSyncLosses_Object = MibTableColumn
fcFxPortSyncLosses = _FcFxPortSyncLosses_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 2),
    _FcFxPortSyncLosses_Type()
)
fcFxPortSyncLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortSyncLosses.setStatus("current")
_FcFxPortSigLosses_Type = Counter32
_FcFxPortSigLosses_Object = MibTableColumn
fcFxPortSigLosses = _FcFxPortSigLosses_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 3),
    _FcFxPortSigLosses_Type()
)
fcFxPortSigLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortSigLosses.setStatus("current")
_FcFxPortPrimSeqProtoErrors_Type = Counter32
_FcFxPortPrimSeqProtoErrors_Object = MibTableColumn
fcFxPortPrimSeqProtoErrors = _FcFxPortPrimSeqProtoErrors_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 4),
    _FcFxPortPrimSeqProtoErrors_Type()
)
fcFxPortPrimSeqProtoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortPrimSeqProtoErrors.setStatus("current")
_FcFxPortInvalidTxWords_Type = Counter32
_FcFxPortInvalidTxWords_Object = MibTableColumn
fcFxPortInvalidTxWords = _FcFxPortInvalidTxWords_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 5),
    _FcFxPortInvalidTxWords_Type()
)
fcFxPortInvalidTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortInvalidTxWords.setStatus("current")
_FcFxPortInvalidCrcs_Type = Counter32
_FcFxPortInvalidCrcs_Object = MibTableColumn
fcFxPortInvalidCrcs = _FcFxPortInvalidCrcs_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 6),
    _FcFxPortInvalidCrcs_Type()
)
fcFxPortInvalidCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortInvalidCrcs.setStatus("current")
_FcFxPortDelimiterErrors_Type = Counter32
_FcFxPortDelimiterErrors_Object = MibTableColumn
fcFxPortDelimiterErrors = _FcFxPortDelimiterErrors_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 7),
    _FcFxPortDelimiterErrors_Type()
)
fcFxPortDelimiterErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortDelimiterErrors.setStatus("current")
_FcFxPortAddressIdErrors_Type = Counter32
_FcFxPortAddressIdErrors_Object = MibTableColumn
fcFxPortAddressIdErrors = _FcFxPortAddressIdErrors_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 8),
    _FcFxPortAddressIdErrors_Type()
)
fcFxPortAddressIdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortAddressIdErrors.setStatus("current")
_FcFxPortLinkResetIns_Type = Counter32
_FcFxPortLinkResetIns_Object = MibTableColumn
fcFxPortLinkResetIns = _FcFxPortLinkResetIns_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 9),
    _FcFxPortLinkResetIns_Type()
)
fcFxPortLinkResetIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortLinkResetIns.setStatus("current")
_FcFxPortLinkResetOuts_Type = Counter32
_FcFxPortLinkResetOuts_Object = MibTableColumn
fcFxPortLinkResetOuts = _FcFxPortLinkResetOuts_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 10),
    _FcFxPortLinkResetOuts_Type()
)
fcFxPortLinkResetOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortLinkResetOuts.setStatus("current")
_FcFxPortOlsIns_Type = Counter32
_FcFxPortOlsIns_Object = MibTableColumn
fcFxPortOlsIns = _FcFxPortOlsIns_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 11),
    _FcFxPortOlsIns_Type()
)
fcFxPortOlsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortOlsIns.setStatus("current")
_FcFxPortOlsOuts_Type = Counter32
_FcFxPortOlsOuts_Object = MibTableColumn
fcFxPortOlsOuts = _FcFxPortOlsOuts_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 3, 1, 1, 12),
    _FcFxPortOlsOuts_Type()
)
fcFxPortOlsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortOlsOuts.setStatus("current")
_FcFeAccounting_ObjectIdentity = ObjectIdentity
fcFeAccounting = _FcFeAccounting_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 75, 1, 4)
)
_FcFxPortC1AccountingTable_Object = MibTable
fcFxPortC1AccountingTable = _FcFxPortC1AccountingTable_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 1)
)
if mibBuilder.loadTexts:
    fcFxPortC1AccountingTable.setStatus("current")
_FcFxPortC1AccountingEntry_Object = MibTableRow
fcFxPortC1AccountingEntry = _FcFxPortC1AccountingEntry_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    fcFxPortC1AccountingEntry.setStatus("current")
_FcFxPortC1InFrames_Type = Counter32
_FcFxPortC1InFrames_Object = MibTableColumn
fcFxPortC1InFrames = _FcFxPortC1InFrames_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 1, 1, 1),
    _FcFxPortC1InFrames_Type()
)
fcFxPortC1InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC1InFrames.setStatus("current")
_FcFxPortC1OutFrames_Type = Counter32
_FcFxPortC1OutFrames_Object = MibTableColumn
fcFxPortC1OutFrames = _FcFxPortC1OutFrames_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 1, 1, 2),
    _FcFxPortC1OutFrames_Type()
)
fcFxPortC1OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC1OutFrames.setStatus("current")
_FcFxPortC1InOctets_Type = Counter32
_FcFxPortC1InOctets_Object = MibTableColumn
fcFxPortC1InOctets = _FcFxPortC1InOctets_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 1, 1, 3),
    _FcFxPortC1InOctets_Type()
)
fcFxPortC1InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC1InOctets.setStatus("current")
_FcFxPortC1OutOctets_Type = Counter32
_FcFxPortC1OutOctets_Object = MibTableColumn
fcFxPortC1OutOctets = _FcFxPortC1OutOctets_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 1, 1, 4),
    _FcFxPortC1OutOctets_Type()
)
fcFxPortC1OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC1OutOctets.setStatus("current")
_FcFxPortC1Discards_Type = Counter32
_FcFxPortC1Discards_Object = MibTableColumn
fcFxPortC1Discards = _FcFxPortC1Discards_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 1, 1, 5),
    _FcFxPortC1Discards_Type()
)
fcFxPortC1Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC1Discards.setStatus("current")
_FcFxPortC1FbsyFrames_Type = Counter32
_FcFxPortC1FbsyFrames_Object = MibTableColumn
fcFxPortC1FbsyFrames = _FcFxPortC1FbsyFrames_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 1, 1, 6),
    _FcFxPortC1FbsyFrames_Type()
)
fcFxPortC1FbsyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC1FbsyFrames.setStatus("current")
_FcFxPortC1FrjtFrames_Type = Counter32
_FcFxPortC1FrjtFrames_Object = MibTableColumn
fcFxPortC1FrjtFrames = _FcFxPortC1FrjtFrames_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 1, 1, 7),
    _FcFxPortC1FrjtFrames_Type()
)
fcFxPortC1FrjtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC1FrjtFrames.setStatus("current")
_FcFxPortC1InConnections_Type = Counter32
_FcFxPortC1InConnections_Object = MibTableColumn
fcFxPortC1InConnections = _FcFxPortC1InConnections_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 1, 1, 8),
    _FcFxPortC1InConnections_Type()
)
fcFxPortC1InConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC1InConnections.setStatus("current")
_FcFxPortC1OutConnections_Type = Counter32
_FcFxPortC1OutConnections_Object = MibTableColumn
fcFxPortC1OutConnections = _FcFxPortC1OutConnections_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 1, 1, 9),
    _FcFxPortC1OutConnections_Type()
)
fcFxPortC1OutConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC1OutConnections.setStatus("current")
_FcFxPortC1ConnTime_Type = MilliSeconds
_FcFxPortC1ConnTime_Object = MibTableColumn
fcFxPortC1ConnTime = _FcFxPortC1ConnTime_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 1, 1, 10),
    _FcFxPortC1ConnTime_Type()
)
fcFxPortC1ConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC1ConnTime.setStatus("current")
if mibBuilder.loadTexts:
    fcFxPortC1ConnTime.setUnits("milliseconds")
_FcFxPortC2AccountingTable_Object = MibTable
fcFxPortC2AccountingTable = _FcFxPortC2AccountingTable_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 2)
)
if mibBuilder.loadTexts:
    fcFxPortC2AccountingTable.setStatus("current")
_FcFxPortC2AccountingEntry_Object = MibTableRow
fcFxPortC2AccountingEntry = _FcFxPortC2AccountingEntry_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    fcFxPortC2AccountingEntry.setStatus("current")
_FcFxPortC2InFrames_Type = Counter32
_FcFxPortC2InFrames_Object = MibTableColumn
fcFxPortC2InFrames = _FcFxPortC2InFrames_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 2, 1, 1),
    _FcFxPortC2InFrames_Type()
)
fcFxPortC2InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC2InFrames.setStatus("current")
_FcFxPortC2OutFrames_Type = Counter32
_FcFxPortC2OutFrames_Object = MibTableColumn
fcFxPortC2OutFrames = _FcFxPortC2OutFrames_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 2, 1, 2),
    _FcFxPortC2OutFrames_Type()
)
fcFxPortC2OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC2OutFrames.setStatus("current")
_FcFxPortC2InOctets_Type = Counter32
_FcFxPortC2InOctets_Object = MibTableColumn
fcFxPortC2InOctets = _FcFxPortC2InOctets_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 2, 1, 3),
    _FcFxPortC2InOctets_Type()
)
fcFxPortC2InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC2InOctets.setStatus("current")
_FcFxPortC2OutOctets_Type = Counter32
_FcFxPortC2OutOctets_Object = MibTableColumn
fcFxPortC2OutOctets = _FcFxPortC2OutOctets_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 2, 1, 4),
    _FcFxPortC2OutOctets_Type()
)
fcFxPortC2OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC2OutOctets.setStatus("current")
_FcFxPortC2Discards_Type = Counter32
_FcFxPortC2Discards_Object = MibTableColumn
fcFxPortC2Discards = _FcFxPortC2Discards_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 2, 1, 5),
    _FcFxPortC2Discards_Type()
)
fcFxPortC2Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC2Discards.setStatus("current")
_FcFxPortC2FbsyFrames_Type = Counter32
_FcFxPortC2FbsyFrames_Object = MibTableColumn
fcFxPortC2FbsyFrames = _FcFxPortC2FbsyFrames_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 2, 1, 6),
    _FcFxPortC2FbsyFrames_Type()
)
fcFxPortC2FbsyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC2FbsyFrames.setStatus("current")
_FcFxPortC2FrjtFrames_Type = Counter32
_FcFxPortC2FrjtFrames_Object = MibTableColumn
fcFxPortC2FrjtFrames = _FcFxPortC2FrjtFrames_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 2, 1, 7),
    _FcFxPortC2FrjtFrames_Type()
)
fcFxPortC2FrjtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC2FrjtFrames.setStatus("current")
_FcFxPortC3AccountingTable_Object = MibTable
fcFxPortC3AccountingTable = _FcFxPortC3AccountingTable_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 3)
)
if mibBuilder.loadTexts:
    fcFxPortC3AccountingTable.setStatus("current")
_FcFxPortC3AccountingEntry_Object = MibTableRow
fcFxPortC3AccountingEntry = _FcFxPortC3AccountingEntry_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    fcFxPortC3AccountingEntry.setStatus("current")
_FcFxPortC3InFrames_Type = Counter32
_FcFxPortC3InFrames_Object = MibTableColumn
fcFxPortC3InFrames = _FcFxPortC3InFrames_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 3, 1, 1),
    _FcFxPortC3InFrames_Type()
)
fcFxPortC3InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC3InFrames.setStatus("current")
_FcFxPortC3OutFrames_Type = Counter32
_FcFxPortC3OutFrames_Object = MibTableColumn
fcFxPortC3OutFrames = _FcFxPortC3OutFrames_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 3, 1, 2),
    _FcFxPortC3OutFrames_Type()
)
fcFxPortC3OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC3OutFrames.setStatus("current")
_FcFxPortC3InOctets_Type = Counter32
_FcFxPortC3InOctets_Object = MibTableColumn
fcFxPortC3InOctets = _FcFxPortC3InOctets_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 3, 1, 3),
    _FcFxPortC3InOctets_Type()
)
fcFxPortC3InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC3InOctets.setStatus("current")
_FcFxPortC3OutOctets_Type = Counter32
_FcFxPortC3OutOctets_Object = MibTableColumn
fcFxPortC3OutOctets = _FcFxPortC3OutOctets_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 3, 1, 4),
    _FcFxPortC3OutOctets_Type()
)
fcFxPortC3OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC3OutOctets.setStatus("current")
_FcFxPortC3Discards_Type = Counter32
_FcFxPortC3Discards_Object = MibTableColumn
fcFxPortC3Discards = _FcFxPortC3Discards_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 4, 3, 1, 5),
    _FcFxPortC3Discards_Type()
)
fcFxPortC3Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortC3Discards.setStatus("current")
_FcFeCapabilities_ObjectIdentity = ObjectIdentity
fcFeCapabilities = _FcFeCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 75, 1, 5)
)
_FcFxPortCapTable_Object = MibTable
fcFxPortCapTable = _FcFxPortCapTable_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 5, 1)
)
if mibBuilder.loadTexts:
    fcFxPortCapTable.setStatus("current")
_FcFxPortCapEntry_Object = MibTableRow
fcFxPortCapEntry = _FcFxPortCapEntry_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    fcFxPortCapEntry.setStatus("current")
_FcFxPortCapFcphVersionHigh_Type = FcphVersion
_FcFxPortCapFcphVersionHigh_Object = MibTableColumn
fcFxPortCapFcphVersionHigh = _FcFxPortCapFcphVersionHigh_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 1),
    _FcFxPortCapFcphVersionHigh_Type()
)
fcFxPortCapFcphVersionHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapFcphVersionHigh.setStatus("current")
_FcFxPortCapFcphVersionLow_Type = FcphVersion
_FcFxPortCapFcphVersionLow_Object = MibTableColumn
fcFxPortCapFcphVersionLow = _FcFxPortCapFcphVersionLow_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 2),
    _FcFxPortCapFcphVersionLow_Type()
)
fcFxPortCapFcphVersionLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapFcphVersionLow.setStatus("current")
_FcFxPortCapBbCreditMax_Type = FcBbCredit
_FcFxPortCapBbCreditMax_Object = MibTableColumn
fcFxPortCapBbCreditMax = _FcFxPortCapBbCreditMax_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 3),
    _FcFxPortCapBbCreditMax_Type()
)
fcFxPortCapBbCreditMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapBbCreditMax.setStatus("current")
if mibBuilder.loadTexts:
    fcFxPortCapBbCreditMax.setUnits("buffers")
_FcFxPortCapBbCreditMin_Type = FcBbCredit
_FcFxPortCapBbCreditMin_Object = MibTableColumn
fcFxPortCapBbCreditMin = _FcFxPortCapBbCreditMin_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 4),
    _FcFxPortCapBbCreditMin_Type()
)
fcFxPortCapBbCreditMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapBbCreditMin.setStatus("current")
if mibBuilder.loadTexts:
    fcFxPortCapBbCreditMin.setUnits("buffers")
_FcFxPortCapRxDataFieldSizeMax_Type = FcRxDataFieldSize
_FcFxPortCapRxDataFieldSizeMax_Object = MibTableColumn
fcFxPortCapRxDataFieldSizeMax = _FcFxPortCapRxDataFieldSizeMax_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 5),
    _FcFxPortCapRxDataFieldSizeMax_Type()
)
fcFxPortCapRxDataFieldSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapRxDataFieldSizeMax.setStatus("current")
if mibBuilder.loadTexts:
    fcFxPortCapRxDataFieldSizeMax.setUnits("bytes")
_FcFxPortCapRxDataFieldSizeMin_Type = FcRxDataFieldSize
_FcFxPortCapRxDataFieldSizeMin_Object = MibTableColumn
fcFxPortCapRxDataFieldSizeMin = _FcFxPortCapRxDataFieldSizeMin_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 6),
    _FcFxPortCapRxDataFieldSizeMin_Type()
)
fcFxPortCapRxDataFieldSizeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapRxDataFieldSizeMin.setStatus("current")
if mibBuilder.loadTexts:
    fcFxPortCapRxDataFieldSizeMin.setUnits("bytes")
_FcFxPortCapCos_Type = FcCosCap
_FcFxPortCapCos_Object = MibTableColumn
fcFxPortCapCos = _FcFxPortCapCos_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 7),
    _FcFxPortCapCos_Type()
)
fcFxPortCapCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapCos.setStatus("current")
_FcFxPortCapIntermix_Type = TruthValue
_FcFxPortCapIntermix_Object = MibTableColumn
fcFxPortCapIntermix = _FcFxPortCapIntermix_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 8),
    _FcFxPortCapIntermix_Type()
)
fcFxPortCapIntermix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapIntermix.setStatus("current")
_FcFxPortCapStackedConnMode_Type = FcStackedConnMode
_FcFxPortCapStackedConnMode_Object = MibTableColumn
fcFxPortCapStackedConnMode = _FcFxPortCapStackedConnMode_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 9),
    _FcFxPortCapStackedConnMode_Type()
)
fcFxPortCapStackedConnMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapStackedConnMode.setStatus("current")
_FcFxPortCapClass2SeqDeliv_Type = TruthValue
_FcFxPortCapClass2SeqDeliv_Object = MibTableColumn
fcFxPortCapClass2SeqDeliv = _FcFxPortCapClass2SeqDeliv_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 10),
    _FcFxPortCapClass2SeqDeliv_Type()
)
fcFxPortCapClass2SeqDeliv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapClass2SeqDeliv.setStatus("current")
_FcFxPortCapClass3SeqDeliv_Type = TruthValue
_FcFxPortCapClass3SeqDeliv_Object = MibTableColumn
fcFxPortCapClass3SeqDeliv = _FcFxPortCapClass3SeqDeliv_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 11),
    _FcFxPortCapClass3SeqDeliv_Type()
)
fcFxPortCapClass3SeqDeliv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapClass3SeqDeliv.setStatus("current")
_FcFxPortCapHoldTimeMax_Type = MicroSeconds
_FcFxPortCapHoldTimeMax_Object = MibTableColumn
fcFxPortCapHoldTimeMax = _FcFxPortCapHoldTimeMax_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 12),
    _FcFxPortCapHoldTimeMax_Type()
)
fcFxPortCapHoldTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapHoldTimeMax.setStatus("current")
if mibBuilder.loadTexts:
    fcFxPortCapHoldTimeMax.setUnits("microseconds")
_FcFxPortCapHoldTimeMin_Type = MicroSeconds
_FcFxPortCapHoldTimeMin_Object = MibTableColumn
fcFxPortCapHoldTimeMin = _FcFxPortCapHoldTimeMin_Object(
    (1, 3, 6, 1, 2, 1, 75, 1, 5, 1, 1, 13),
    _FcFxPortCapHoldTimeMin_Type()
)
fcFxPortCapHoldTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcFxPortCapHoldTimeMin.setStatus("current")
if mibBuilder.loadTexts:
    fcFxPortCapHoldTimeMin.setUnits("microseconds")
_FcFeMIBConformance_ObjectIdentity = ObjectIdentity
fcFeMIBConformance = _FcFeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 75, 2)
)
_FcFeMIBCompliances_ObjectIdentity = ObjectIdentity
fcFeMIBCompliances = _FcFeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 75, 2, 1)
)
_FcFeMIBGroups_ObjectIdentity = ObjectIdentity
fcFeMIBGroups = _FcFeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 75, 2, 2)
)
fcFxPortEntry.registerAugmentions(
    ("FIBRE-CHANNEL-FE-MIB",
     "fcFxPortStatusEntry")
)
fcFxPortStatusEntry.setIndexNames(*fcFxPortEntry.getIndexNames())
fcFxPortEntry.registerAugmentions(
    ("FIBRE-CHANNEL-FE-MIB",
     "fcFxPortPhysEntry")
)
fcFxPortPhysEntry.setIndexNames(*fcFxPortEntry.getIndexNames())
fcFxPortEntry.registerAugmentions(
    ("FIBRE-CHANNEL-FE-MIB",
     "fcFxPortErrorEntry")
)
fcFxPortErrorEntry.setIndexNames(*fcFxPortEntry.getIndexNames())
fcFxPortEntry.registerAugmentions(
    ("FIBRE-CHANNEL-FE-MIB",
     "fcFxPortC1AccountingEntry")
)
fcFxPortC1AccountingEntry.setIndexNames(*fcFxPortEntry.getIndexNames())
fcFxPortEntry.registerAugmentions(
    ("FIBRE-CHANNEL-FE-MIB",
     "fcFxPortC2AccountingEntry")
)
fcFxPortC2AccountingEntry.setIndexNames(*fcFxPortEntry.getIndexNames())
fcFxPortEntry.registerAugmentions(
    ("FIBRE-CHANNEL-FE-MIB",
     "fcFxPortC3AccountingEntry")
)
fcFxPortC3AccountingEntry.setIndexNames(*fcFxPortEntry.getIndexNames())
fcFxPortEntry.registerAugmentions(
    ("FIBRE-CHANNEL-FE-MIB",
     "fcFxPortCapEntry")
)
fcFxPortCapEntry.setIndexNames(*fcFxPortEntry.getIndexNames())

# Managed Objects groups

fcFeConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 75, 2, 2, 1)
)
fcFeConfigGroup.setObjects(
      *(("FIBRE-CHANNEL-FE-MIB", "fcFeFabricName"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFeElementName"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFeModuleCapacity"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFeModuleDescr"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFeModuleObjectID"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFeModuleOperStatus"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFeModuleLastChange"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFeModuleFxPortCapacity"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFeModuleName"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortName"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortFcphVersionHigh"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortFcphVersionLow"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortBbCredit"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortRxBufSize"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortRatov"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortEdtov"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCosSupported"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortIntermixSupported"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortStackedConnMode"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortClass2SeqDeliv"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortClass3SeqDeliv"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortHoldTime"))
)
if mibBuilder.loadTexts:
    fcFeConfigGroup.setStatus("current")

fcFeStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 75, 2, 2, 2)
)
fcFeStatusGroup.setObjects(
      *(("FIBRE-CHANNEL-FE-MIB", "fcFxPortID"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortBbCreditAvailable"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortOperMode"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortAdminMode"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortPhysAdminStatus"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortPhysOperStatus"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortPhysLastChange"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortPhysRttov"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortFcphVersionAgreed"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortNxPortBbCredit"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortNxPortRxDataFieldSize"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCosSuppAgreed"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortIntermixSuppAgreed"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortStackedConnModeAgreed"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortClass2SeqDelivAgreed"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortClass3SeqDelivAgreed"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortNxPortName"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortConnectedNxPort"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortBbCreditModel"))
)
if mibBuilder.loadTexts:
    fcFeStatusGroup.setStatus("current")

fcFeErrorGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 75, 2, 2, 3)
)
fcFeErrorGroup.setObjects(
      *(("FIBRE-CHANNEL-FE-MIB", "fcFxPortLinkFailures"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortSyncLosses"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortSigLosses"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortPrimSeqProtoErrors"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortInvalidTxWords"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortInvalidCrcs"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortDelimiterErrors"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortAddressIdErrors"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortLinkResetIns"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortLinkResetOuts"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortOlsIns"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortOlsOuts"))
)
if mibBuilder.loadTexts:
    fcFeErrorGroup.setStatus("current")

fcFeClass1AccountingGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 75, 2, 2, 4)
)
fcFeClass1AccountingGroup.setObjects(
      *(("FIBRE-CHANNEL-FE-MIB", "fcFxPortC1InFrames"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC1OutFrames"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC1InOctets"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC1OutOctets"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC1Discards"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC1FbsyFrames"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC1FrjtFrames"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC1InConnections"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC1OutConnections"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC1ConnTime"))
)
if mibBuilder.loadTexts:
    fcFeClass1AccountingGroup.setStatus("current")

fcFeClass2AccountingGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 75, 2, 2, 5)
)
fcFeClass2AccountingGroup.setObjects(
      *(("FIBRE-CHANNEL-FE-MIB", "fcFxPortC2InFrames"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC2OutFrames"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC2InOctets"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC2OutOctets"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC2Discards"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC2FbsyFrames"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC2FrjtFrames"))
)
if mibBuilder.loadTexts:
    fcFeClass2AccountingGroup.setStatus("current")

fcFeClass3AccountingGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 75, 2, 2, 6)
)
fcFeClass3AccountingGroup.setObjects(
      *(("FIBRE-CHANNEL-FE-MIB", "fcFxPortC3InFrames"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC3OutFrames"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC3InOctets"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC3OutOctets"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortC3Discards"))
)
if mibBuilder.loadTexts:
    fcFeClass3AccountingGroup.setStatus("current")

fcFeCapabilitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 75, 2, 2, 7)
)
fcFeCapabilitiesGroup.setObjects(
      *(("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapFcphVersionHigh"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapFcphVersionLow"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapBbCreditMax"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapBbCreditMin"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapRxDataFieldSizeMax"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapRxDataFieldSizeMin"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapCos"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapIntermix"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapStackedConnMode"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapClass2SeqDeliv"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapClass3SeqDeliv"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapHoldTimeMax"),
        ("FIBRE-CHANNEL-FE-MIB", "fcFxPortCapHoldTimeMin"))
)
if mibBuilder.loadTexts:
    fcFeCapabilitiesGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fcFeMIBMinimumCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 75, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fcFeMIBMinimumCompliance.setStatus(
        "current"
    )

fcFeMIBFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 75, 2, 1, 2)
)
if mibBuilder.loadTexts:
    fcFeMIBFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBRE-CHANNEL-FE-MIB",
    **{"MilliSeconds": MilliSeconds,
       "MicroSeconds": MicroSeconds,
       "FcNameId": FcNameId,
       "FcAddressId": FcAddressId,
       "FcRxDataFieldSize": FcRxDataFieldSize,
       "FcBbCredit": FcBbCredit,
       "FcphVersion": FcphVersion,
       "FcStackedConnMode": FcStackedConnMode,
       "FcCosCap": FcCosCap,
       "FcFeModuleCapacity": FcFeModuleCapacity,
       "FcFeFxPortCapacity": FcFeFxPortCapacity,
       "FcFeModuleIndex": FcFeModuleIndex,
       "FcFeFxPortIndex": FcFeFxPortIndex,
       "FcFeNxPortIndex": FcFeNxPortIndex,
       "FcBbCreditModel": FcBbCreditModel,
       "fcFeMIB": fcFeMIB,
       "fcFeMIBObjects": fcFeMIBObjects,
       "fcFeConfig": fcFeConfig,
       "fcFeFabricName": fcFeFabricName,
       "fcFeElementName": fcFeElementName,
       "fcFeModuleCapacity": fcFeModuleCapacity,
       "fcFeModuleTable": fcFeModuleTable,
       "fcFeModuleEntry": fcFeModuleEntry,
       "fcFeModuleIndex": fcFeModuleIndex,
       "fcFeModuleDescr": fcFeModuleDescr,
       "fcFeModuleObjectID": fcFeModuleObjectID,
       "fcFeModuleOperStatus": fcFeModuleOperStatus,
       "fcFeModuleLastChange": fcFeModuleLastChange,
       "fcFeModuleFxPortCapacity": fcFeModuleFxPortCapacity,
       "fcFeModuleName": fcFeModuleName,
       "fcFxPortTable": fcFxPortTable,
       "fcFxPortEntry": fcFxPortEntry,
       "fcFxPortIndex": fcFxPortIndex,
       "fcFxPortName": fcFxPortName,
       "fcFxPortFcphVersionHigh": fcFxPortFcphVersionHigh,
       "fcFxPortFcphVersionLow": fcFxPortFcphVersionLow,
       "fcFxPortBbCredit": fcFxPortBbCredit,
       "fcFxPortRxBufSize": fcFxPortRxBufSize,
       "fcFxPortRatov": fcFxPortRatov,
       "fcFxPortEdtov": fcFxPortEdtov,
       "fcFxPortCosSupported": fcFxPortCosSupported,
       "fcFxPortIntermixSupported": fcFxPortIntermixSupported,
       "fcFxPortStackedConnMode": fcFxPortStackedConnMode,
       "fcFxPortClass2SeqDeliv": fcFxPortClass2SeqDeliv,
       "fcFxPortClass3SeqDeliv": fcFxPortClass3SeqDeliv,
       "fcFxPortHoldTime": fcFxPortHoldTime,
       "fcFeStatus": fcFeStatus,
       "fcFxPortStatusTable": fcFxPortStatusTable,
       "fcFxPortStatusEntry": fcFxPortStatusEntry,
       "fcFxPortID": fcFxPortID,
       "fcFxPortBbCreditAvailable": fcFxPortBbCreditAvailable,
       "fcFxPortOperMode": fcFxPortOperMode,
       "fcFxPortAdminMode": fcFxPortAdminMode,
       "fcFxPortPhysTable": fcFxPortPhysTable,
       "fcFxPortPhysEntry": fcFxPortPhysEntry,
       "fcFxPortPhysAdminStatus": fcFxPortPhysAdminStatus,
       "fcFxPortPhysOperStatus": fcFxPortPhysOperStatus,
       "fcFxPortPhysLastChange": fcFxPortPhysLastChange,
       "fcFxPortPhysRttov": fcFxPortPhysRttov,
       "fcFxLoginTable": fcFxLoginTable,
       "fcFxLoginEntry": fcFxLoginEntry,
       "fcFxPortNxLoginIndex": fcFxPortNxLoginIndex,
       "fcFxPortFcphVersionAgreed": fcFxPortFcphVersionAgreed,
       "fcFxPortNxPortBbCredit": fcFxPortNxPortBbCredit,
       "fcFxPortNxPortRxDataFieldSize": fcFxPortNxPortRxDataFieldSize,
       "fcFxPortCosSuppAgreed": fcFxPortCosSuppAgreed,
       "fcFxPortIntermixSuppAgreed": fcFxPortIntermixSuppAgreed,
       "fcFxPortStackedConnModeAgreed": fcFxPortStackedConnModeAgreed,
       "fcFxPortClass2SeqDelivAgreed": fcFxPortClass2SeqDelivAgreed,
       "fcFxPortClass3SeqDelivAgreed": fcFxPortClass3SeqDelivAgreed,
       "fcFxPortNxPortName": fcFxPortNxPortName,
       "fcFxPortConnectedNxPort": fcFxPortConnectedNxPort,
       "fcFxPortBbCreditModel": fcFxPortBbCreditModel,
       "fcFeError": fcFeError,
       "fcFxPortErrorTable": fcFxPortErrorTable,
       "fcFxPortErrorEntry": fcFxPortErrorEntry,
       "fcFxPortLinkFailures": fcFxPortLinkFailures,
       "fcFxPortSyncLosses": fcFxPortSyncLosses,
       "fcFxPortSigLosses": fcFxPortSigLosses,
       "fcFxPortPrimSeqProtoErrors": fcFxPortPrimSeqProtoErrors,
       "fcFxPortInvalidTxWords": fcFxPortInvalidTxWords,
       "fcFxPortInvalidCrcs": fcFxPortInvalidCrcs,
       "fcFxPortDelimiterErrors": fcFxPortDelimiterErrors,
       "fcFxPortAddressIdErrors": fcFxPortAddressIdErrors,
       "fcFxPortLinkResetIns": fcFxPortLinkResetIns,
       "fcFxPortLinkResetOuts": fcFxPortLinkResetOuts,
       "fcFxPortOlsIns": fcFxPortOlsIns,
       "fcFxPortOlsOuts": fcFxPortOlsOuts,
       "fcFeAccounting": fcFeAccounting,
       "fcFxPortC1AccountingTable": fcFxPortC1AccountingTable,
       "fcFxPortC1AccountingEntry": fcFxPortC1AccountingEntry,
       "fcFxPortC1InFrames": fcFxPortC1InFrames,
       "fcFxPortC1OutFrames": fcFxPortC1OutFrames,
       "fcFxPortC1InOctets": fcFxPortC1InOctets,
       "fcFxPortC1OutOctets": fcFxPortC1OutOctets,
       "fcFxPortC1Discards": fcFxPortC1Discards,
       "fcFxPortC1FbsyFrames": fcFxPortC1FbsyFrames,
       "fcFxPortC1FrjtFrames": fcFxPortC1FrjtFrames,
       "fcFxPortC1InConnections": fcFxPortC1InConnections,
       "fcFxPortC1OutConnections": fcFxPortC1OutConnections,
       "fcFxPortC1ConnTime": fcFxPortC1ConnTime,
       "fcFxPortC2AccountingTable": fcFxPortC2AccountingTable,
       "fcFxPortC2AccountingEntry": fcFxPortC2AccountingEntry,
       "fcFxPortC2InFrames": fcFxPortC2InFrames,
       "fcFxPortC2OutFrames": fcFxPortC2OutFrames,
       "fcFxPortC2InOctets": fcFxPortC2InOctets,
       "fcFxPortC2OutOctets": fcFxPortC2OutOctets,
       "fcFxPortC2Discards": fcFxPortC2Discards,
       "fcFxPortC2FbsyFrames": fcFxPortC2FbsyFrames,
       "fcFxPortC2FrjtFrames": fcFxPortC2FrjtFrames,
       "fcFxPortC3AccountingTable": fcFxPortC3AccountingTable,
       "fcFxPortC3AccountingEntry": fcFxPortC3AccountingEntry,
       "fcFxPortC3InFrames": fcFxPortC3InFrames,
       "fcFxPortC3OutFrames": fcFxPortC3OutFrames,
       "fcFxPortC3InOctets": fcFxPortC3InOctets,
       "fcFxPortC3OutOctets": fcFxPortC3OutOctets,
       "fcFxPortC3Discards": fcFxPortC3Discards,
       "fcFeCapabilities": fcFeCapabilities,
       "fcFxPortCapTable": fcFxPortCapTable,
       "fcFxPortCapEntry": fcFxPortCapEntry,
       "fcFxPortCapFcphVersionHigh": fcFxPortCapFcphVersionHigh,
       "fcFxPortCapFcphVersionLow": fcFxPortCapFcphVersionLow,
       "fcFxPortCapBbCreditMax": fcFxPortCapBbCreditMax,
       "fcFxPortCapBbCreditMin": fcFxPortCapBbCreditMin,
       "fcFxPortCapRxDataFieldSizeMax": fcFxPortCapRxDataFieldSizeMax,
       "fcFxPortCapRxDataFieldSizeMin": fcFxPortCapRxDataFieldSizeMin,
       "fcFxPortCapCos": fcFxPortCapCos,
       "fcFxPortCapIntermix": fcFxPortCapIntermix,
       "fcFxPortCapStackedConnMode": fcFxPortCapStackedConnMode,
       "fcFxPortCapClass2SeqDeliv": fcFxPortCapClass2SeqDeliv,
       "fcFxPortCapClass3SeqDeliv": fcFxPortCapClass3SeqDeliv,
       "fcFxPortCapHoldTimeMax": fcFxPortCapHoldTimeMax,
       "fcFxPortCapHoldTimeMin": fcFxPortCapHoldTimeMin,
       "fcFeMIBConformance": fcFeMIBConformance,
       "fcFeMIBCompliances": fcFeMIBCompliances,
       "fcFeMIBMinimumCompliance": fcFeMIBMinimumCompliance,
       "fcFeMIBFullCompliance": fcFeMIBFullCompliance,
       "fcFeMIBGroups": fcFeMIBGroups,
       "fcFeConfigGroup": fcFeConfigGroup,
       "fcFeStatusGroup": fcFeStatusGroup,
       "fcFeErrorGroup": fcFeErrorGroup,
       "fcFeClass1AccountingGroup": fcFeClass1AccountingGroup,
       "fcFeClass2AccountingGroup": fcFeClass2AccountingGroup,
       "fcFeClass3AccountingGroup": fcFeClass3AccountingGroup,
       "fcFeCapabilitiesGroup": fcFeCapabilitiesGroup}
)
