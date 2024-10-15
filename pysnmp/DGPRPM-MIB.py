# SNMP MIB module (DGPRPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DGPRPM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:23 2024
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
 NotificationType,
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
    "NotificationType",
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

_Dgp_ObjectIdentity = ObjectIdentity
dgp = _Dgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1)
)
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1)
)


class _Protocol_Type(Integer32):
    """Custom type protocol based on Integer32"""
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
        *(("ats", 4),
          ("cps", 3),
          ("rpm", 2),
          ("ups01", 0),
          ("ups02", 1))
    )


_Protocol_Type.__name__ = "Integer32"
_Protocol_Object = MibScalar
protocol = _Protocol_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 1),
    _Protocol_Type()
)
protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocol.setStatus("mandatory")
_Rpm_ObjectIdentity = ObjectIdentity
rpm = _Rpm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3)
)
_RpmNumber_Type = Integer32
_RpmNumber_Object = MibScalar
rpmNumber = _RpmNumber_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 1),
    _RpmNumber_Type()
)
rpmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmNumber.setStatus("mandatory")
_RpmTable_Object = MibTable
rpmTable = _RpmTable_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    rpmTable.setStatus("mandatory")
_RpmEntry_Object = MibTableRow
rpmEntry = _RpmEntry_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1)
)
rpmEntry.setIndexNames(
    (0, "DGPRPM-MIB", "rpmID"),
)
if mibBuilder.loadTexts:
    rpmEntry.setStatus("mandatory")


class _RpmID_Type(Integer32):
    """Custom type rpmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_RpmID_Type.__name__ = "Integer32"
_RpmID_Object = MibTableColumn
rpmID = _RpmID_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 1),
    _RpmID_Type()
)
rpmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmID.setStatus("mandatory")
_RpmOutletNumber_Type = Integer32
_RpmOutletNumber_Object = MibTableColumn
rpmOutletNumber = _RpmOutletNumber_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 2),
    _RpmOutletNumber_Type()
)
rpmOutletNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmOutletNumber.setStatus("mandatory")
_RpmOutletState_Type = DisplayString
_RpmOutletState_Object = MibTableColumn
rpmOutletState = _RpmOutletState_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 3),
    _RpmOutletState_Type()
)
rpmOutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmOutletState.setStatus("mandatory")
_RpmControlType_Type = DisplayString
_RpmControlType_Object = MibTableColumn
rpmControlType = _RpmControlType_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 4),
    _RpmControlType_Type()
)
rpmControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmControlType.setStatus("mandatory")
_RpmInternetLocal_Type = DisplayString
_RpmInternetLocal_Object = MibTableColumn
rpmInternetLocal = _RpmInternetLocal_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 5),
    _RpmInternetLocal_Type()
)
rpmInternetLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmInternetLocal.setStatus("mandatory")
_RpmName_Type = DisplayString
_RpmName_Object = MibTableColumn
rpmName = _RpmName_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 6),
    _RpmName_Type()
)
rpmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmName.setStatus("mandatory")
_RpmOutletA_Type = DisplayString
_RpmOutletA_Object = MibTableColumn
rpmOutletA = _RpmOutletA_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 7),
    _RpmOutletA_Type()
)
rpmOutletA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmOutletA.setStatus("mandatory")
_RpmOutletB_Type = DisplayString
_RpmOutletB_Object = MibTableColumn
rpmOutletB = _RpmOutletB_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 8),
    _RpmOutletB_Type()
)
rpmOutletB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmOutletB.setStatus("mandatory")
_RpmOutletC_Type = DisplayString
_RpmOutletC_Object = MibTableColumn
rpmOutletC = _RpmOutletC_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 9),
    _RpmOutletC_Type()
)
rpmOutletC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmOutletC.setStatus("mandatory")
_RpmOutletD_Type = DisplayString
_RpmOutletD_Object = MibTableColumn
rpmOutletD = _RpmOutletD_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 10),
    _RpmOutletD_Type()
)
rpmOutletD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmOutletD.setStatus("mandatory")
_RpmOutletE_Type = DisplayString
_RpmOutletE_Object = MibTableColumn
rpmOutletE = _RpmOutletE_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 11),
    _RpmOutletE_Type()
)
rpmOutletE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmOutletE.setStatus("mandatory")
_RpmOutletF_Type = DisplayString
_RpmOutletF_Object = MibTableColumn
rpmOutletF = _RpmOutletF_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 12),
    _RpmOutletF_Type()
)
rpmOutletF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmOutletF.setStatus("mandatory")
_RpmOutletG_Type = DisplayString
_RpmOutletG_Object = MibTableColumn
rpmOutletG = _RpmOutletG_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 13),
    _RpmOutletG_Type()
)
rpmOutletG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmOutletG.setStatus("mandatory")
_RpmOutletH_Type = DisplayString
_RpmOutletH_Object = MibTableColumn
rpmOutletH = _RpmOutletH_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 14),
    _RpmOutletH_Type()
)
rpmOutletH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmOutletH.setStatus("mandatory")
_RpmDelayA_Type = Integer32
_RpmDelayA_Object = MibTableColumn
rpmDelayA = _RpmDelayA_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 15),
    _RpmDelayA_Type()
)
rpmDelayA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmDelayA.setStatus("mandatory")
_RpmDelayB_Type = Integer32
_RpmDelayB_Object = MibTableColumn
rpmDelayB = _RpmDelayB_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 16),
    _RpmDelayB_Type()
)
rpmDelayB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmDelayB.setStatus("mandatory")
_RpmDelayC_Type = Integer32
_RpmDelayC_Object = MibTableColumn
rpmDelayC = _RpmDelayC_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 17),
    _RpmDelayC_Type()
)
rpmDelayC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmDelayC.setStatus("mandatory")
_RpmDelayD_Type = Integer32
_RpmDelayD_Object = MibTableColumn
rpmDelayD = _RpmDelayD_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 18),
    _RpmDelayD_Type()
)
rpmDelayD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmDelayD.setStatus("mandatory")
_RpmDelayE_Type = Integer32
_RpmDelayE_Object = MibTableColumn
rpmDelayE = _RpmDelayE_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 19),
    _RpmDelayE_Type()
)
rpmDelayE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmDelayE.setStatus("mandatory")
_RpmDelayF_Type = Integer32
_RpmDelayF_Object = MibTableColumn
rpmDelayF = _RpmDelayF_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 20),
    _RpmDelayF_Type()
)
rpmDelayF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmDelayF.setStatus("mandatory")
_RpmDelayG_Type = Integer32
_RpmDelayG_Object = MibTableColumn
rpmDelayG = _RpmDelayG_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 21),
    _RpmDelayG_Type()
)
rpmDelayG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmDelayG.setStatus("mandatory")
_RpmDelayH_Type = Integer32
_RpmDelayH_Object = MibTableColumn
rpmDelayH = _RpmDelayH_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 22),
    _RpmDelayH_Type()
)
rpmDelayH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmDelayH.setStatus("mandatory")
_RpmResumeDelayA_Type = Integer32
_RpmResumeDelayA_Object = MibTableColumn
rpmResumeDelayA = _RpmResumeDelayA_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 23),
    _RpmResumeDelayA_Type()
)
rpmResumeDelayA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmResumeDelayA.setStatus("mandatory")
_RpmResumeDelayB_Type = Integer32
_RpmResumeDelayB_Object = MibTableColumn
rpmResumeDelayB = _RpmResumeDelayB_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 24),
    _RpmResumeDelayB_Type()
)
rpmResumeDelayB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmResumeDelayB.setStatus("mandatory")
_RpmResumeDelayC_Type = Integer32
_RpmResumeDelayC_Object = MibTableColumn
rpmResumeDelayC = _RpmResumeDelayC_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 25),
    _RpmResumeDelayC_Type()
)
rpmResumeDelayC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmResumeDelayC.setStatus("mandatory")
_RpmResumeDelayD_Type = Integer32
_RpmResumeDelayD_Object = MibTableColumn
rpmResumeDelayD = _RpmResumeDelayD_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 26),
    _RpmResumeDelayD_Type()
)
rpmResumeDelayD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmResumeDelayD.setStatus("mandatory")
_RpmResumeDelayE_Type = Integer32
_RpmResumeDelayE_Object = MibTableColumn
rpmResumeDelayE = _RpmResumeDelayE_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 27),
    _RpmResumeDelayE_Type()
)
rpmResumeDelayE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmResumeDelayE.setStatus("mandatory")
_RpmResumeDelayF_Type = Integer32
_RpmResumeDelayF_Object = MibTableColumn
rpmResumeDelayF = _RpmResumeDelayF_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 28),
    _RpmResumeDelayF_Type()
)
rpmResumeDelayF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmResumeDelayF.setStatus("mandatory")
_RpmResumeDelayG_Type = Integer32
_RpmResumeDelayG_Object = MibTableColumn
rpmResumeDelayG = _RpmResumeDelayG_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 29),
    _RpmResumeDelayG_Type()
)
rpmResumeDelayG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmResumeDelayG.setStatus("mandatory")
_RpmResumeDelayH_Type = Integer32
_RpmResumeDelayH_Object = MibTableColumn
rpmResumeDelayH = _RpmResumeDelayH_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 2, 1, 30),
    _RpmResumeDelayH_Type()
)
rpmResumeDelayH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmResumeDelayH.setStatus("mandatory")
_RpmSetEntry_ObjectIdentity = ObjectIdentity
rpmSetEntry = _RpmSetEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 3)
)


class _RpmSetID_Type(Integer32):
    """Custom type rpmSetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_RpmSetID_Type.__name__ = "Integer32"
_RpmSetID_Object = MibScalar
rpmSetID = _RpmSetID_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 3, 1),
    _RpmSetID_Type()
)
rpmSetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmSetID.setStatus("mandatory")


class _RpmOnNumber_Type(Integer32):
    """Custom type rpmOnNumber based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("outletA", 1),
          ("outletB", 2),
          ("outletC", 3),
          ("outletD", 4),
          ("outletE", 5),
          ("outletF", 6),
          ("outletG", 7),
          ("outletH", 8))
    )


_RpmOnNumber_Type.__name__ = "Integer32"
_RpmOnNumber_Object = MibScalar
rpmOnNumber = _RpmOnNumber_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 3, 2),
    _RpmOnNumber_Type()
)
rpmOnNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmOnNumber.setStatus("mandatory")


class _RpmOffNumber_Type(Integer32):
    """Custom type rpmOffNumber based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("outletA", 1),
          ("outletB", 2),
          ("outletC", 3),
          ("outletD", 4),
          ("outletE", 5),
          ("outletF", 6),
          ("outletG", 7),
          ("outletH", 8))
    )


_RpmOffNumber_Type.__name__ = "Integer32"
_RpmOffNumber_Object = MibScalar
rpmOffNumber = _RpmOffNumber_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 3, 3),
    _RpmOffNumber_Type()
)
rpmOffNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmOffNumber.setStatus("mandatory")


class _RpmAllOnOff_Type(Integer32):
    """Custom type rpmAllOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("off", 2),
          ("on", 1))
    )


_RpmAllOnOff_Type.__name__ = "Integer32"
_RpmAllOnOff_Object = MibScalar
rpmAllOnOff = _RpmAllOnOff_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 3, 4),
    _RpmAllOnOff_Type()
)
rpmAllOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmAllOnOff.setStatus("mandatory")
_RpmScheduleTable_Object = MibTable
rpmScheduleTable = _RpmScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    rpmScheduleTable.setStatus("mandatory")
_RpmScheduleEntry_Object = MibTableRow
rpmScheduleEntry = _RpmScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 4, 1)
)
rpmScheduleEntry.setIndexNames(
    (0, "DGPRPM-MIB", "rpmScheduleIndex"),
)
if mibBuilder.loadTexts:
    rpmScheduleEntry.setStatus("mandatory")
_RpmScheduleIndex_Type = Integer32
_RpmScheduleIndex_Object = MibTableColumn
rpmScheduleIndex = _RpmScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 4, 1, 1),
    _RpmScheduleIndex_Type()
)
rpmScheduleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmScheduleIndex.setStatus("mandatory")


class _RpmScheduleID_Type(Integer32):
    """Custom type rpmScheduleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_RpmScheduleID_Type.__name__ = "Integer32"
_RpmScheduleID_Object = MibTableColumn
rpmScheduleID = _RpmScheduleID_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 4, 1, 2),
    _RpmScheduleID_Type()
)
rpmScheduleID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmScheduleID.setStatus("mandatory")


class _RpmOutlet_Type(Integer32):
    """Custom type rpmOutlet based on Integer32"""
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
        *(("outletA", 1),
          ("outletB", 2),
          ("outletC", 3),
          ("outletD", 4),
          ("outletE", 5),
          ("outletF", 6),
          ("outletG", 7),
          ("outletH", 8))
    )


_RpmOutlet_Type.__name__ = "Integer32"
_RpmOutlet_Object = MibTableColumn
rpmOutlet = _RpmOutlet_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 4, 1, 3),
    _RpmOutlet_Type()
)
rpmOutlet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmOutlet.setStatus("mandatory")


class _RpmOutletAction_Type(Integer32):
    """Custom type rpmOutletAction based on Integer32"""
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


_RpmOutletAction_Type.__name__ = "Integer32"
_RpmOutletAction_Object = MibTableColumn
rpmOutletAction = _RpmOutletAction_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 4, 1, 4),
    _RpmOutletAction_Type()
)
rpmOutletAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmOutletAction.setStatus("mandatory")


class _RpmPeriod_Type(Integer32):
    """Custom type rpmPeriod based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("everyDay", 9),
          ("everyFriday", 7),
          ("everyMonday", 3),
          ("everySaturday", 8),
          ("everySunday", 2),
          ("everyThursday", 6),
          ("everyTuesday", 4),
          ("everyWednesday", 5),
          ("once", 1))
    )


_RpmPeriod_Type.__name__ = "Integer32"
_RpmPeriod_Object = MibTableColumn
rpmPeriod = _RpmPeriod_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 4, 1, 5),
    _RpmPeriod_Type()
)
rpmPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmPeriod.setStatus("mandatory")
_RpmDate_Type = DisplayString
_RpmDate_Object = MibTableColumn
rpmDate = _RpmDate_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 4, 1, 6),
    _RpmDate_Type()
)
rpmDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmDate.setStatus("mandatory")
_RpmTime_Type = DisplayString
_RpmTime_Object = MibTableColumn
rpmTime = _RpmTime_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 4, 1, 7),
    _RpmTime_Type()
)
rpmTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmTime.setStatus("mandatory")


class _RpmStatus_Type(Integer32):
    """Custom type rpmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("clear", 0))
    )


_RpmStatus_Type.__name__ = "Integer32"
_RpmStatus_Object = MibTableColumn
rpmStatus = _RpmStatus_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 3, 4, 1, 8),
    _RpmStatus_Type()
)
rpmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpmStatus.setStatus("mandatory")
_Cps_ObjectIdentity = ObjectIdentity
cps = _Cps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 4)
)
_CpsNumber_Type = Integer32
_CpsNumber_Object = MibScalar
cpsNumber = _CpsNumber_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 4, 1),
    _CpsNumber_Type()
)
cpsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsNumber.setStatus("mandatory")
_CpsTable_Object = MibTable
cpsTable = _CpsTable_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cpsTable.setStatus("mandatory")
_CpsEntry_Object = MibTableRow
cpsEntry = _CpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 4, 2, 1)
)
cpsEntry.setIndexNames(
    (0, "DGPRPM-MIB", "cpsID"),
)
if mibBuilder.loadTexts:
    cpsEntry.setStatus("mandatory")


class _CpsID_Type(Integer32):
    """Custom type cpsID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CpsID_Type.__name__ = "Integer32"
_CpsID_Object = MibTableColumn
cpsID = _CpsID_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 4, 2, 1, 1),
    _CpsID_Type()
)
cpsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsID.setStatus("mandatory")
_CpsValue_Type = Integer32
_CpsValue_Object = MibTableColumn
cpsValue = _CpsValue_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 4, 2, 1, 2),
    _CpsValue_Type()
)
cpsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsValue.setStatus("mandatory")


class _CpsThreshold1_Type(Integer32):
    """Custom type cpsThreshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_CpsThreshold1_Type.__name__ = "Integer32"
_CpsThreshold1_Object = MibTableColumn
cpsThreshold1 = _CpsThreshold1_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 4, 2, 1, 3),
    _CpsThreshold1_Type()
)
cpsThreshold1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsThreshold1.setStatus("mandatory")


class _CpsThreshold2_Type(Integer32):
    """Custom type cpsThreshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_CpsThreshold2_Type.__name__ = "Integer32"
_CpsThreshold2_Object = MibTableColumn
cpsThreshold2 = _CpsThreshold2_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 4, 2, 1, 4),
    _CpsThreshold2_Type()
)
cpsThreshold2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsThreshold2.setStatus("mandatory")
_CpsSetTable_Object = MibTable
cpsSetTable = _CpsSetTable_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cpsSetTable.setStatus("mandatory")
_CpsSetEntry_Object = MibTableRow
cpsSetEntry = _CpsSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 4, 3, 1)
)
cpsSetEntry.setIndexNames(
    (0, "DGPRPM-MIB", "cpsIDIndex"),
)
if mibBuilder.loadTexts:
    cpsSetEntry.setStatus("mandatory")


class _CpsIDIndex_Type(Integer32):
    """Custom type cpsIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CpsIDIndex_Type.__name__ = "Integer32"
_CpsIDIndex_Object = MibTableColumn
cpsIDIndex = _CpsIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 4, 3, 1, 1),
    _CpsIDIndex_Type()
)
cpsIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpsIDIndex.setStatus("mandatory")


class _CpsSetThreshold1_Type(Integer32):
    """Custom type cpsSetThreshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_CpsSetThreshold1_Type.__name__ = "Integer32"
_CpsSetThreshold1_Object = MibTableColumn
cpsSetThreshold1 = _CpsSetThreshold1_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 4, 3, 1, 2),
    _CpsSetThreshold1_Type()
)
cpsSetThreshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsSetThreshold1.setStatus("mandatory")


class _CpsSetThreshold2_Type(Integer32):
    """Custom type cpsSetThreshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_CpsSetThreshold2_Type.__name__ = "Integer32"
_CpsSetThreshold2_Object = MibTableColumn
cpsSetThreshold2 = _CpsSetThreshold2_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 4, 3, 1, 3),
    _CpsSetThreshold2_Type()
)
cpsSetThreshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpsSetThreshold2.setStatus("mandatory")
_Ats_ObjectIdentity = ObjectIdentity
ats = _Ats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 5)
)
_AtsIdentification_Type = DisplayString
_AtsIdentification_Object = MibScalar
atsIdentification = _AtsIdentification_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 5, 1),
    _AtsIdentification_Type()
)
atsIdentification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsIdentification.setStatus("mandatory")
_AtsInputPowerSourceA_Type = DisplayString
_AtsInputPowerSourceA_Object = MibScalar
atsInputPowerSourceA = _AtsInputPowerSourceA_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 5, 2),
    _AtsInputPowerSourceA_Type()
)
atsInputPowerSourceA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsInputPowerSourceA.setStatus("mandatory")
_AtsInputPowerSourceB_Type = DisplayString
_AtsInputPowerSourceB_Object = MibScalar
atsInputPowerSourceB = _AtsInputPowerSourceB_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 5, 3),
    _AtsInputPowerSourceB_Type()
)
atsInputPowerSourceB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsInputPowerSourceB.setStatus("mandatory")


class _AtsAutomaticTransferSwitch_Type(Integer32):
    """Custom type atsAutomaticTransferSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("transfer", 1))
    )


_AtsAutomaticTransferSwitch_Type.__name__ = "Integer32"
_AtsAutomaticTransferSwitch_Object = MibScalar
atsAutomaticTransferSwitch = _AtsAutomaticTransferSwitch_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 5, 4),
    _AtsAutomaticTransferSwitch_Type()
)
atsAutomaticTransferSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atsAutomaticTransferSwitch.setStatus("mandatory")


class _AtsStatus_Type(Integer32):
    """Custom type atsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2),
          ("none", 0))
    )


_AtsStatus_Type.__name__ = "Integer32"
_AtsStatus_Object = MibScalar
atsStatus = _AtsStatus_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 5, 5),
    _AtsStatus_Type()
)
atsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atsStatus.setStatus("mandatory")
_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 999)
)
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 999, 1)
)
_AccessTable_Object = MibTable
accessTable = _AccessTable_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 999, 1, 1)
)
if mibBuilder.loadTexts:
    accessTable.setStatus("mandatory")
_AccessEntry_Object = MibTableRow
accessEntry = _AccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 999, 1, 1, 1)
)
accessEntry.setIndexNames(
    (0, "DGPRPM-MIB", "accessNo"),
)
if mibBuilder.loadTexts:
    accessEntry.setStatus("mandatory")


class _AccessNo_Type(Integer32):
    """Custom type accessNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AccessNo_Type.__name__ = "Integer32"
_AccessNo_Object = MibTableColumn
accessNo = _AccessNo_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 999, 1, 1, 1, 1),
    _AccessNo_Type()
)
accessNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessNo.setStatus("mandatory")
_Community_Type = DisplayString
_Community_Object = MibTableColumn
community = _Community_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 999, 1, 1, 1, 2),
    _Community_Type()
)
community.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    community.setStatus("mandatory")


class _Permission_Type(Integer32):
    """Custom type permission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAccess", 0),
          ("read", 1),
          ("readWrite", 2))
    )


_Permission_Type.__name__ = "Integer32"
_Permission_Object = MibTableColumn
permission = _Permission_Object(
    (1, 3, 6, 1, 4, 1, 17420, 1, 1, 999, 1, 1, 1, 3),
    _Permission_Type()
)
permission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    permission.setStatus("mandatory")

# Managed Objects groups


# Notification objects

rpmOutletOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 17420, 0, 100)
)
if mibBuilder.loadTexts:
    rpmOutletOn.setStatus(
        ""
    )

rpmOutletOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 17420, 0, 101)
)
if mibBuilder.loadTexts:
    rpmOutletOff.setStatus(
        ""
    )

rpmOutletReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 17420, 0, 102)
)
if mibBuilder.loadTexts:
    rpmOutletReboot.setStatus(
        ""
    )

rpmOutletfault = NotificationType(
    (1, 3, 6, 1, 4, 1, 17420, 0, 103)
)
if mibBuilder.loadTexts:
    rpmOutletfault.setStatus(
        ""
    )

rpmCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 17420, 0, 104)
)
if mibBuilder.loadTexts:
    rpmCommunicationLost.setStatus(
        ""
    )

cpsOutOfThreshold1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 17420, 0, 105)
)
if mibBuilder.loadTexts:
    cpsOutOfThreshold1.setStatus(
        ""
    )

cpsOutOfThreshold2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 17420, 0, 106)
)
if mibBuilder.loadTexts:
    cpsOutOfThreshold2.setStatus(
        ""
    )

cpsCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 17420, 0, 107)
)
if mibBuilder.loadTexts:
    cpsCommunicationLost.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DGPRPM-MIB",
    **{"dgp": dgp,
       "rpmOutletOn": rpmOutletOn,
       "rpmOutletOff": rpmOutletOff,
       "rpmOutletReboot": rpmOutletReboot,
       "rpmOutletfault": rpmOutletfault,
       "rpmCommunicationLost": rpmCommunicationLost,
       "cpsOutOfThreshold1": cpsOutOfThreshold1,
       "cpsOutOfThreshold2": cpsOutOfThreshold2,
       "cpsCommunicationLost": cpsCommunicationLost,
       "products": products,
       "hardware": hardware,
       "protocol": protocol,
       "rpm": rpm,
       "rpmNumber": rpmNumber,
       "rpmTable": rpmTable,
       "rpmEntry": rpmEntry,
       "rpmID": rpmID,
       "rpmOutletNumber": rpmOutletNumber,
       "rpmOutletState": rpmOutletState,
       "rpmControlType": rpmControlType,
       "rpmInternetLocal": rpmInternetLocal,
       "rpmName": rpmName,
       "rpmOutletA": rpmOutletA,
       "rpmOutletB": rpmOutletB,
       "rpmOutletC": rpmOutletC,
       "rpmOutletD": rpmOutletD,
       "rpmOutletE": rpmOutletE,
       "rpmOutletF": rpmOutletF,
       "rpmOutletG": rpmOutletG,
       "rpmOutletH": rpmOutletH,
       "rpmDelayA": rpmDelayA,
       "rpmDelayB": rpmDelayB,
       "rpmDelayC": rpmDelayC,
       "rpmDelayD": rpmDelayD,
       "rpmDelayE": rpmDelayE,
       "rpmDelayF": rpmDelayF,
       "rpmDelayG": rpmDelayG,
       "rpmDelayH": rpmDelayH,
       "rpmResumeDelayA": rpmResumeDelayA,
       "rpmResumeDelayB": rpmResumeDelayB,
       "rpmResumeDelayC": rpmResumeDelayC,
       "rpmResumeDelayD": rpmResumeDelayD,
       "rpmResumeDelayE": rpmResumeDelayE,
       "rpmResumeDelayF": rpmResumeDelayF,
       "rpmResumeDelayG": rpmResumeDelayG,
       "rpmResumeDelayH": rpmResumeDelayH,
       "rpmSetEntry": rpmSetEntry,
       "rpmSetID": rpmSetID,
       "rpmOnNumber": rpmOnNumber,
       "rpmOffNumber": rpmOffNumber,
       "rpmAllOnOff": rpmAllOnOff,
       "rpmScheduleTable": rpmScheduleTable,
       "rpmScheduleEntry": rpmScheduleEntry,
       "rpmScheduleIndex": rpmScheduleIndex,
       "rpmScheduleID": rpmScheduleID,
       "rpmOutlet": rpmOutlet,
       "rpmOutletAction": rpmOutletAction,
       "rpmPeriod": rpmPeriod,
       "rpmDate": rpmDate,
       "rpmTime": rpmTime,
       "rpmStatus": rpmStatus,
       "cps": cps,
       "cpsNumber": cpsNumber,
       "cpsTable": cpsTable,
       "cpsEntry": cpsEntry,
       "cpsID": cpsID,
       "cpsValue": cpsValue,
       "cpsThreshold1": cpsThreshold1,
       "cpsThreshold2": cpsThreshold2,
       "cpsSetTable": cpsSetTable,
       "cpsSetEntry": cpsSetEntry,
       "cpsIDIndex": cpsIDIndex,
       "cpsSetThreshold1": cpsSetThreshold1,
       "cpsSetThreshold2": cpsSetThreshold2,
       "ats": ats,
       "atsIdentification": atsIdentification,
       "atsInputPowerSourceA": atsInputPowerSourceA,
       "atsInputPowerSourceB": atsInputPowerSourceB,
       "atsAutomaticTransferSwitch": atsAutomaticTransferSwitch,
       "atsStatus": atsStatus,
       "mgmt": mgmt,
       "snmp": snmp,
       "accessTable": accessTable,
       "accessEntry": accessEntry,
       "accessNo": accessNo,
       "community": community,
       "permission": permission}
)
