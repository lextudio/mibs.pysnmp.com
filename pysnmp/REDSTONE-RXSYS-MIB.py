# SNMP MIB module (REDSTONE-RXSYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-RXSYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:46 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(rsMgmt,) = mibBuilder.importSymbols(
    "REDSTONE-SMI",
    "rsMgmt")

(RsEnable,) = mibBuilder.importSymbols(
    "REDSTONE-TC",
    "RsEnable")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rsRXSysMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17)
)
rsRXSysMIB.setRevisions(
        ("1999-07-12 00:00",
         "1999-07-02 00:00",
         "1999-04-22 00:00",
         "1998-01-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RsSysCardType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ce1", 8),
          ("ct1", 9),
          ("ct3", 2),
          ("oc3", 3),
          ("srp", 1),
          ("ue3Atm", 6),
          ("ue3Frame", 7),
          ("unknown", 0),
          ("ut3Atm", 4),
          ("ut3Frame", 5))
    )



# MIB Managed Objects in the order of their OIDs

_RsRXSysTrap_ObjectIdentity = ObjectIdentity
rsRXSysTrap = _RsRXSysTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 0)
)
_RsRXSysObjects_ObjectIdentity = ObjectIdentity
rsRXSysObjects = _RsRXSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1)
)
_RsRXSysGeneral_ObjectIdentity = ObjectIdentity
rsRXSysGeneral = _RsRXSysGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 1)
)


class _RsRXSysChassisRev_Type(Integer32):
    """Custom type rsRXSysChassisRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsRXSysChassisRev_Type.__name__ = "Integer32"
_RsRXSysChassisRev_Object = MibScalar
rsRXSysChassisRev = _RsRXSysChassisRev_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 1, 1),
    _RsRXSysChassisRev_Type()
)
rsRXSysChassisRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysChassisRev.setStatus("current")
_RsRXSysSwVersion_Type = DisplayString
_RsRXSysSwVersion_Object = MibScalar
rsRXSysSwVersion = _RsRXSysSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 1, 2),
    _RsRXSysSwVersion_Type()
)
rsRXSysSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysSwVersion.setStatus("current")
_RsRXSysSwBuildDate_Type = DisplayString
_RsRXSysSwBuildDate_Object = MibScalar
rsRXSysSwBuildDate = _RsRXSysSwBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 1, 3),
    _RsRXSysSwBuildDate_Type()
)
rsRXSysSwBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysSwBuildDate.setStatus("current")
_RsRXSysFabric_ObjectIdentity = ObjectIdentity
rsRXSysFabric = _RsRXSysFabric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 2)
)
_RsRXSysFabricSpeed_Type = Integer32
_RsRXSysFabricSpeed_Object = MibScalar
rsRXSysFabricSpeed = _RsRXSysFabricSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 2, 1),
    _RsRXSysFabricSpeed_Type()
)
rsRXSysFabricSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysFabricSpeed.setStatus("current")
if mibBuilder.loadTexts:
    rsRXSysFabricSpeed.setUnits("gigabits per second")


class _RsRXSysFabricRev_Type(Integer32):
    """Custom type rsRXSysFabricRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsRXSysFabricRev_Type.__name__ = "Integer32"
_RsRXSysFabricRev_Object = MibScalar
rsRXSysFabricRev = _RsRXSysFabricRev_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 2, 2),
    _RsRXSysFabricRev_Type()
)
rsRXSysFabricRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysFabricRev.setStatus("current")
_RsRXSysNvs_ObjectIdentity = ObjectIdentity
rsRXSysNvs = _RsRXSysNvs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 3)
)


class _RsRXSysNvsStatus_Type(Integer32):
    """Custom type rsRXSysNvsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("nearCapacity", 3),
          ("notPresent", 0),
          ("ok", 4),
          ("volumeError", 2),
          ("writeProtected", 1))
    )


_RsRXSysNvsStatus_Type.__name__ = "Integer32"
_RsRXSysNvsStatus_Object = MibScalar
rsRXSysNvsStatus = _RsRXSysNvsStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 3, 1),
    _RsRXSysNvsStatus_Type()
)
rsRXSysNvsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysNvsStatus.setStatus("current")
_RsRXSysNvsCapacity_Type = Integer32
_RsRXSysNvsCapacity_Object = MibScalar
rsRXSysNvsCapacity = _RsRXSysNvsCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 3, 2),
    _RsRXSysNvsCapacity_Type()
)
rsRXSysNvsCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysNvsCapacity.setStatus("current")
if mibBuilder.loadTexts:
    rsRXSysNvsCapacity.setUnits("megabytes")


class _RsRXSysNvsUtilPct_Type(Integer32):
    """Custom type rsRXSysNvsUtilPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_RsRXSysNvsUtilPct_Type.__name__ = "Integer32"
_RsRXSysNvsUtilPct_Object = MibScalar
rsRXSysNvsUtilPct = _RsRXSysNvsUtilPct_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 3, 3),
    _RsRXSysNvsUtilPct_Type()
)
rsRXSysNvsUtilPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysNvsUtilPct.setStatus("current")
if mibBuilder.loadTexts:
    rsRXSysNvsUtilPct.setUnits("percent")
_RsRXSysSlot_ObjectIdentity = ObjectIdentity
rsRXSysSlot = _RsRXSysSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4)
)
_RsRXSysSlotCount_Type = Integer32
_RsRXSysSlotCount_Object = MibScalar
rsRXSysSlotCount = _RsRXSysSlotCount_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 1),
    _RsRXSysSlotCount_Type()
)
rsRXSysSlotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysSlotCount.setStatus("current")
_RsRXSysSlotTable_Object = MibTable
rsRXSysSlotTable = _RsRXSysSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2)
)
if mibBuilder.loadTexts:
    rsRXSysSlotTable.setStatus("current")
_RsRXSysSlotEntry_Object = MibTableRow
rsRXSysSlotEntry = _RsRXSysSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1)
)
rsRXSysSlotEntry.setIndexNames(
    (0, "REDSTONE-RXSYS-MIB", "rsRXSysSlotIndex"),
)
if mibBuilder.loadTexts:
    rsRXSysSlotEntry.setStatus("current")
_RsRXSysSlotIndex_Type = Integer32
_RsRXSysSlotIndex_Object = MibTableColumn
rsRXSysSlotIndex = _RsRXSysSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 1),
    _RsRXSysSlotIndex_Type()
)
rsRXSysSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsRXSysSlotIndex.setStatus("current")


class _RsRXSysSlotDescr_Type(DisplayString):
    """Custom type rsRXSysSlotDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RsRXSysSlotDescr_Type.__name__ = "DisplayString"
_RsRXSysSlotDescr_Object = MibTableColumn
rsRXSysSlotDescr = _RsRXSysSlotDescr_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 2),
    _RsRXSysSlotDescr_Type()
)
rsRXSysSlotDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysSlotDescr.setStatus("current")
_RsRXSysSlotCurrentCardType_Type = RsSysCardType
_RsRXSysSlotCurrentCardType_Object = MibTableColumn
rsRXSysSlotCurrentCardType = _RsRXSysSlotCurrentCardType_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 3),
    _RsRXSysSlotCurrentCardType_Type()
)
rsRXSysSlotCurrentCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysSlotCurrentCardType.setStatus("current")


class _RsRXSysSlotRev_Type(Integer32):
    """Custom type rsRXSysSlotRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsRXSysSlotRev_Type.__name__ = "Integer32"
_RsRXSysSlotRev_Object = MibTableColumn
rsRXSysSlotRev = _RsRXSysSlotRev_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 4),
    _RsRXSysSlotRev_Type()
)
rsRXSysSlotRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysSlotRev.setStatus("current")
_RsRXSysSlotAdminStatus_Type = RsEnable
_RsRXSysSlotAdminStatus_Object = MibTableColumn
rsRXSysSlotAdminStatus = _RsRXSysSlotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 5),
    _RsRXSysSlotAdminStatus_Type()
)
rsRXSysSlotAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRXSysSlotAdminStatus.setStatus("current")


class _RsRXSysSlotOperStatus_Type(Integer32):
    """Custom type rsRXSysSlotOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("booting", 4),
          ("disabled", 2),
          ("empty", 1),
          ("failed", 3),
          ("initializing", 5),
          ("online", 6),
          ("standby", 7),
          ("unknown", 0))
    )


_RsRXSysSlotOperStatus_Type.__name__ = "Integer32"
_RsRXSysSlotOperStatus_Object = MibTableColumn
rsRXSysSlotOperStatus = _RsRXSysSlotOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 6),
    _RsRXSysSlotOperStatus_Type()
)
rsRXSysSlotOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysSlotOperStatus.setStatus("current")


class _RsRXSysSlotDisableReason_Type(Integer32):
    """Custom type rsRXSysSlotDisableReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("admin", 3),
          ("assessing", 2),
          ("cardMismatch", 4),
          ("fabricLimit", 5),
          ("imageError", 6),
          ("none", 0),
          ("unknown", 1))
    )


_RsRXSysSlotDisableReason_Type.__name__ = "Integer32"
_RsRXSysSlotDisableReason_Object = MibTableColumn
rsRXSysSlotDisableReason = _RsRXSysSlotDisableReason_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 7),
    _RsRXSysSlotDisableReason_Type()
)
rsRXSysSlotDisableReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysSlotDisableReason.setStatus("current")
_RsRXSysSlotExpectedCardType_Type = RsSysCardType
_RsRXSysSlotExpectedCardType_Object = MibTableColumn
rsRXSysSlotExpectedCardType = _RsRXSysSlotExpectedCardType_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 8),
    _RsRXSysSlotExpectedCardType_Type()
)
rsRXSysSlotExpectedCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysSlotExpectedCardType.setStatus("current")


class _RsRXSysSlotControl_Type(Integer32):
    """Custom type rsRXSysSlotControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flush", 1),
          ("noOperation", 0),
          ("reset", 2))
    )


_RsRXSysSlotControl_Type.__name__ = "Integer32"
_RsRXSysSlotControl_Object = MibTableColumn
rsRXSysSlotControl = _RsRXSysSlotControl_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 9),
    _RsRXSysSlotControl_Type()
)
rsRXSysSlotControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRXSysSlotControl.setStatus("current")


class _RsRXSysSlotCpuUtilPct_Type(Integer32):
    """Custom type rsRXSysSlotCpuUtilPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_RsRXSysSlotCpuUtilPct_Type.__name__ = "Integer32"
_RsRXSysSlotCpuUtilPct_Object = MibTableColumn
rsRXSysSlotCpuUtilPct = _RsRXSysSlotCpuUtilPct_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 10),
    _RsRXSysSlotCpuUtilPct_Type()
)
rsRXSysSlotCpuUtilPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysSlotCpuUtilPct.setStatus("current")
if mibBuilder.loadTexts:
    rsRXSysSlotCpuUtilPct.setUnits("percent")


class _RsRXSysSlotMemUtilPct_Type(Integer32):
    """Custom type rsRXSysSlotMemUtilPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_RsRXSysSlotMemUtilPct_Type.__name__ = "Integer32"
_RsRXSysSlotMemUtilPct_Object = MibTableColumn
rsRXSysSlotMemUtilPct = _RsRXSysSlotMemUtilPct_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 11),
    _RsRXSysSlotMemUtilPct_Type()
)
rsRXSysSlotMemUtilPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysSlotMemUtilPct.setStatus("current")
if mibBuilder.loadTexts:
    rsRXSysSlotMemUtilPct.setUnits("percent")
_RsRXSysSlotIoaPresent_Type = TruthValue
_RsRXSysSlotIoaPresent_Object = MibTableColumn
rsRXSysSlotIoaPresent = _RsRXSysSlotIoaPresent_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 12),
    _RsRXSysSlotIoaPresent_Type()
)
rsRXSysSlotIoaPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysSlotIoaPresent.setStatus("current")
_RsRXSysSlotPortCount_Type = Integer32
_RsRXSysSlotPortCount_Object = MibTableColumn
rsRXSysSlotPortCount = _RsRXSysSlotPortCount_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 13),
    _RsRXSysSlotPortCount_Type()
)
rsRXSysSlotPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysSlotPortCount.setStatus("current")
_RsRXSysSlotLastChange_Type = TimeTicks
_RsRXSysSlotLastChange_Object = MibTableColumn
rsRXSysSlotLastChange = _RsRXSysSlotLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 4, 2, 1, 14),
    _RsRXSysSlotLastChange_Type()
)
rsRXSysSlotLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysSlotLastChange.setStatus("current")
_RsRXSysPort_ObjectIdentity = ObjectIdentity
rsRXSysPort = _RsRXSysPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 5)
)
_RsRXSysPortTable_Object = MibTable
rsRXSysPortTable = _RsRXSysPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 5, 1)
)
if mibBuilder.loadTexts:
    rsRXSysPortTable.setStatus("current")
_RsRXSysPortEntry_Object = MibTableRow
rsRXSysPortEntry = _RsRXSysPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 5, 1, 1)
)
rsRXSysPortEntry.setIndexNames(
    (0, "REDSTONE-RXSYS-MIB", "rsRXSysSlotIndex"),
    (0, "REDSTONE-RXSYS-MIB", "rsRXSysPortIndex"),
)
if mibBuilder.loadTexts:
    rsRXSysPortEntry.setStatus("current")
_RsRXSysPortIndex_Type = Integer32
_RsRXSysPortIndex_Object = MibTableColumn
rsRXSysPortIndex = _RsRXSysPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 5, 1, 1, 1),
    _RsRXSysPortIndex_Type()
)
rsRXSysPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsRXSysPortIndex.setStatus("current")


class _RsRXSysPortDescr_Type(DisplayString):
    """Custom type rsRXSysPortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RsRXSysPortDescr_Type.__name__ = "DisplayString"
_RsRXSysPortDescr_Object = MibTableColumn
rsRXSysPortDescr = _RsRXSysPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 5, 1, 1, 2),
    _RsRXSysPortDescr_Type()
)
rsRXSysPortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysPortDescr.setStatus("current")


class _RsRXSysPortType_Type(Integer32):
    """Custom type rsRXSysPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ce1", 8),
          ("ct1", 9),
          ("ct3", 2),
          ("eth", 1),
          ("oc3c", 3),
          ("ue3Atm", 6),
          ("ue3Frame", 7),
          ("unknown", 0),
          ("ut3Atm", 4),
          ("ut3Frame", 5))
    )


_RsRXSysPortType_Type.__name__ = "Integer32"
_RsRXSysPortType_Object = MibTableColumn
rsRXSysPortType = _RsRXSysPortType_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 5, 1, 1, 3),
    _RsRXSysPortType_Type()
)
rsRXSysPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysPortType.setStatus("current")
_RsRXSysPortIfIndex_Type = InterfaceIndexOrZero
_RsRXSysPortIfIndex_Object = MibTableColumn
rsRXSysPortIfIndex = _RsRXSysPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 5, 1, 1, 4),
    _RsRXSysPortIfIndex_Type()
)
rsRXSysPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysPortIfIndex.setStatus("current")
_RsRXSysPower_ObjectIdentity = ObjectIdentity
rsRXSysPower = _RsRXSysPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 6)
)
_RsRXSysPowerTable_Object = MibTable
rsRXSysPowerTable = _RsRXSysPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 6, 1)
)
if mibBuilder.loadTexts:
    rsRXSysPowerTable.setStatus("current")
_RsRXSysPowerEntry_Object = MibTableRow
rsRXSysPowerEntry = _RsRXSysPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 6, 1, 1)
)
rsRXSysPowerEntry.setIndexNames(
    (0, "REDSTONE-RXSYS-MIB", "rsRXSysPowerIndex"),
)
if mibBuilder.loadTexts:
    rsRXSysPowerEntry.setStatus("current")
_RsRXSysPowerIndex_Type = Integer32
_RsRXSysPowerIndex_Object = MibTableColumn
rsRXSysPowerIndex = _RsRXSysPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 6, 1, 1, 1),
    _RsRXSysPowerIndex_Type()
)
rsRXSysPowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsRXSysPowerIndex.setStatus("current")


class _RsRXSysPowerDescr_Type(DisplayString):
    """Custom type rsRXSysPowerDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RsRXSysPowerDescr_Type.__name__ = "DisplayString"
_RsRXSysPowerDescr_Object = MibTableColumn
rsRXSysPowerDescr = _RsRXSysPowerDescr_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 6, 1, 1, 2),
    _RsRXSysPowerDescr_Type()
)
rsRXSysPowerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysPowerDescr.setStatus("current")


class _RsRXSysPowerStatus_Type(Integer32):
    """Custom type rsRXSysPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_RsRXSysPowerStatus_Type.__name__ = "Integer32"
_RsRXSysPowerStatus_Object = MibTableColumn
rsRXSysPowerStatus = _RsRXSysPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 6, 1, 1, 3),
    _RsRXSysPowerStatus_Type()
)
rsRXSysPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysPowerStatus.setStatus("current")
_RsRXSysTemperature_ObjectIdentity = ObjectIdentity
rsRXSysTemperature = _RsRXSysTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 7)
)


class _RsRXSysTempFanStatus_Type(Integer32):
    """Custom type rsRXSysTempFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("ok", 1))
    )


_RsRXSysTempFanStatus_Type.__name__ = "Integer32"
_RsRXSysTempFanStatus_Object = MibScalar
rsRXSysTempFanStatus = _RsRXSysTempFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 7, 1),
    _RsRXSysTempFanStatus_Type()
)
rsRXSysTempFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysTempFanStatus.setStatus("current")
_RsRXSysTempTable_Object = MibTable
rsRXSysTempTable = _RsRXSysTempTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 7, 2)
)
if mibBuilder.loadTexts:
    rsRXSysTempTable.setStatus("current")
_RsRXSysTempEntry_Object = MibTableRow
rsRXSysTempEntry = _RsRXSysTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 7, 2, 1)
)
rsRXSysTempEntry.setIndexNames(
    (0, "REDSTONE-RXSYS-MIB", "rsRXSysSlotIndex"),
    (0, "REDSTONE-RXSYS-MIB", "rsRXSysTempIndex"),
)
if mibBuilder.loadTexts:
    rsRXSysTempEntry.setStatus("current")
_RsRXSysTempIndex_Type = Integer32
_RsRXSysTempIndex_Object = MibTableColumn
rsRXSysTempIndex = _RsRXSysTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 7, 2, 1, 1),
    _RsRXSysTempIndex_Type()
)
rsRXSysTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsRXSysTempIndex.setStatus("current")


class _RsRXSysTempDescr_Type(DisplayString):
    """Custom type rsRXSysTempDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RsRXSysTempDescr_Type.__name__ = "DisplayString"
_RsRXSysTempDescr_Object = MibTableColumn
rsRXSysTempDescr = _RsRXSysTempDescr_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 7, 2, 1, 2),
    _RsRXSysTempDescr_Type()
)
rsRXSysTempDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysTempDescr.setStatus("current")


class _RsRXSysTempStatus_Type(Integer32):
    """Custom type rsRXSysTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("nominal", 3),
          ("tooHigh", 4),
          ("tooLow", 2),
          ("unknown", 0))
    )


_RsRXSysTempStatus_Type.__name__ = "Integer32"
_RsRXSysTempStatus_Object = MibTableColumn
rsRXSysTempStatus = _RsRXSysTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 7, 2, 1, 3),
    _RsRXSysTempStatus_Type()
)
rsRXSysTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysTempStatus.setStatus("current")
_RsRXSysTempValue_Type = Integer32
_RsRXSysTempValue_Object = MibTableColumn
rsRXSysTempValue = _RsRXSysTempValue_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 1, 7, 2, 1, 4),
    _RsRXSysTempValue_Type()
)
rsRXSysTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRXSysTempValue.setStatus("current")
if mibBuilder.loadTexts:
    rsRXSysTempValue.setUnits("degrees Celsius")
_RsRXSysConformance_ObjectIdentity = ObjectIdentity
rsRXSysConformance = _RsRXSysConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 2)
)
_RsRXSysCompliances_ObjectIdentity = ObjectIdentity
rsRXSysCompliances = _RsRXSysCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 2, 1)
)
_RsRXSysGroups_ObjectIdentity = ObjectIdentity
rsRXSysGroups = _RsRXSysGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 2, 2)
)

# Managed Objects groups

rsRXSysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 2, 2, 1)
)
rsRXSysGroup.setObjects(
      *(("REDSTONE-RXSYS-MIB", "rsRXSysChassisRev"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysSwVersion"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysSwBuildDate"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysFabricSpeed"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysFabricRev"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysNvsStatus"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysNvsCapacity"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysNvsUtilPct"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysSlotCount"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysSlotDescr"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysSlotCurrentCardType"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysSlotRev"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysSlotAdminStatus"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysSlotOperStatus"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysSlotDisableReason"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysSlotExpectedCardType"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysSlotControl"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysSlotCpuUtilPct"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysSlotMemUtilPct"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysSlotIoaPresent"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysSlotPortCount"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysSlotLastChange"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysPortDescr"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysPortType"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysPortIfIndex"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysPowerDescr"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysPowerStatus"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysTempFanStatus"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysTempDescr"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysTempStatus"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysTempValue"))
)
if mibBuilder.loadTexts:
    rsRXSysGroup.setStatus("current")


# Notification objects

rsRXSysSlotOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 0, 1)
)
rsRXSysSlotOperStatusChange.setObjects(
      *(("REDSTONE-RXSYS-MIB", "rsRXSysSlotCurrentCardType"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysSlotAdminStatus"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysSlotOperStatus"),
        ("REDSTONE-RXSYS-MIB", "rsRXSysSlotDisableReason"))
)
if mibBuilder.loadTexts:
    rsRXSysSlotOperStatusChange.setStatus(
        "current"
    )

rsRXSysPowerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 0, 2)
)
rsRXSysPowerStatusChange.setObjects(
    ("REDSTONE-RXSYS-MIB", "rsRXSysPowerStatus")
)
if mibBuilder.loadTexts:
    rsRXSysPowerStatusChange.setStatus(
        "current"
    )

rsRXSysTempFanStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 0, 3)
)
rsRXSysTempFanStatusChange.setObjects(
    ("REDSTONE-RXSYS-MIB", "rsRXSysTempFanStatus")
)
if mibBuilder.loadTexts:
    rsRXSysTempFanStatusChange.setStatus(
        "current"
    )

rsRXSysTempStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 0, 4)
)
rsRXSysTempStatusChange.setObjects(
    ("REDSTONE-RXSYS-MIB", "rsRXSysTempStatus")
)
if mibBuilder.loadTexts:
    rsRXSysTempStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

rsRXSysCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 17, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rsRXSysCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-RXSYS-MIB",
    **{"RsSysCardType": RsSysCardType,
       "rsRXSysMIB": rsRXSysMIB,
       "rsRXSysTrap": rsRXSysTrap,
       "rsRXSysSlotOperStatusChange": rsRXSysSlotOperStatusChange,
       "rsRXSysPowerStatusChange": rsRXSysPowerStatusChange,
       "rsRXSysTempFanStatusChange": rsRXSysTempFanStatusChange,
       "rsRXSysTempStatusChange": rsRXSysTempStatusChange,
       "rsRXSysObjects": rsRXSysObjects,
       "rsRXSysGeneral": rsRXSysGeneral,
       "rsRXSysChassisRev": rsRXSysChassisRev,
       "rsRXSysSwVersion": rsRXSysSwVersion,
       "rsRXSysSwBuildDate": rsRXSysSwBuildDate,
       "rsRXSysFabric": rsRXSysFabric,
       "rsRXSysFabricSpeed": rsRXSysFabricSpeed,
       "rsRXSysFabricRev": rsRXSysFabricRev,
       "rsRXSysNvs": rsRXSysNvs,
       "rsRXSysNvsStatus": rsRXSysNvsStatus,
       "rsRXSysNvsCapacity": rsRXSysNvsCapacity,
       "rsRXSysNvsUtilPct": rsRXSysNvsUtilPct,
       "rsRXSysSlot": rsRXSysSlot,
       "rsRXSysSlotCount": rsRXSysSlotCount,
       "rsRXSysSlotTable": rsRXSysSlotTable,
       "rsRXSysSlotEntry": rsRXSysSlotEntry,
       "rsRXSysSlotIndex": rsRXSysSlotIndex,
       "rsRXSysSlotDescr": rsRXSysSlotDescr,
       "rsRXSysSlotCurrentCardType": rsRXSysSlotCurrentCardType,
       "rsRXSysSlotRev": rsRXSysSlotRev,
       "rsRXSysSlotAdminStatus": rsRXSysSlotAdminStatus,
       "rsRXSysSlotOperStatus": rsRXSysSlotOperStatus,
       "rsRXSysSlotDisableReason": rsRXSysSlotDisableReason,
       "rsRXSysSlotExpectedCardType": rsRXSysSlotExpectedCardType,
       "rsRXSysSlotControl": rsRXSysSlotControl,
       "rsRXSysSlotCpuUtilPct": rsRXSysSlotCpuUtilPct,
       "rsRXSysSlotMemUtilPct": rsRXSysSlotMemUtilPct,
       "rsRXSysSlotIoaPresent": rsRXSysSlotIoaPresent,
       "rsRXSysSlotPortCount": rsRXSysSlotPortCount,
       "rsRXSysSlotLastChange": rsRXSysSlotLastChange,
       "rsRXSysPort": rsRXSysPort,
       "rsRXSysPortTable": rsRXSysPortTable,
       "rsRXSysPortEntry": rsRXSysPortEntry,
       "rsRXSysPortIndex": rsRXSysPortIndex,
       "rsRXSysPortDescr": rsRXSysPortDescr,
       "rsRXSysPortType": rsRXSysPortType,
       "rsRXSysPortIfIndex": rsRXSysPortIfIndex,
       "rsRXSysPower": rsRXSysPower,
       "rsRXSysPowerTable": rsRXSysPowerTable,
       "rsRXSysPowerEntry": rsRXSysPowerEntry,
       "rsRXSysPowerIndex": rsRXSysPowerIndex,
       "rsRXSysPowerDescr": rsRXSysPowerDescr,
       "rsRXSysPowerStatus": rsRXSysPowerStatus,
       "rsRXSysTemperature": rsRXSysTemperature,
       "rsRXSysTempFanStatus": rsRXSysTempFanStatus,
       "rsRXSysTempTable": rsRXSysTempTable,
       "rsRXSysTempEntry": rsRXSysTempEntry,
       "rsRXSysTempIndex": rsRXSysTempIndex,
       "rsRXSysTempDescr": rsRXSysTempDescr,
       "rsRXSysTempStatus": rsRXSysTempStatus,
       "rsRXSysTempValue": rsRXSysTempValue,
       "rsRXSysConformance": rsRXSysConformance,
       "rsRXSysCompliances": rsRXSysCompliances,
       "rsRXSysCompliance": rsRXSysCompliance,
       "rsRXSysGroups": rsRXSysGroups,
       "rsRXSysGroup": rsRXSysGroup}
)
