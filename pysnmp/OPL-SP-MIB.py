# SNMP MIB module (OPL-SP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPL-SP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:23 2024
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

oplSpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1)
)
oplSpMIB.setRevisions(
        ("2010-05-24 00:00",
         "2009-06-10 00:00",
         "2009-01-28 00:00",
         "2008-11-14 00:00",
         "2008-04-01 00:00",
         "2007-01-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ScfMonitorTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fanRotational", 3),
          ("humidity", 4),
          ("temperature", 1),
          ("unknown", 255),
          ("voltage", 2))
    )



class ScfComponentType(Integer32, TextualConvention):
    status = "current"
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              19,
              21,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              36,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              53,
              54,
              55,
              56,
              57,
              96,
              97,
              98,
              100,
              110,
              115,
              133,
              134,
              135,
              136,
              137,
              141,
              148,
              149,
              150,
              151,
              155,
              157,
              158,
              159,
              160,
              161,
              169,
              171,
              173,
              175,
              180,
              190,
              192,
              196,
              200,
              201,
              203,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("acInlet", 161),
          ("acsA", 40),
          ("acsB", 41),
          ("airA", 158),
          ("airB", 159),
          ("airC", 160),
          ("bank", 14),
          ("block", 15),
          ("bpA", 43),
          ("bpB", 44),
          ("bpuA", 133),
          ("bpuB", 136),
          ("bridge", 149),
          ("busbar", 137),
          ("cable", 180),
          ("clkuA", 34),
          ("clkuB", 36),
          ("cmu", 1),
          ("cpuChip", 4),
          ("cpuCore", 5),
          ("cpuStrand", 6),
          ("cpum", 3),
          ("ddc", 2),
          ("ddcA", 45),
          ("ddcB", 100),
          ("ddcr", 141),
          ("domain", 203),
          ("dvd", 55),
          ("dvdbpA", 173),
          ("dvdbpB", 175),
          ("environment", 200),
          ("fan", 50),
          ("fanA", 49),
          ("fanB", 51),
          ("fanbpA", 46),
          ("fanbpB", 47),
          ("fanbpC", 48),
          ("firm", 201),
          ("flp", 25),
          ("gbe", 150),
          ("half", 17),
          ("hdd", 28),
          ("hddbp", 169),
          ("iob", 134),
          ("ioc", 24),
          ("iocCh", 26),
          ("iocLeaf", 27),
          ("iou", 21),
          ("ioua", 190),
          ("mac", 13),
          ("mbuA", 96),
          ("mbuB", 115),
          ("medbp", 57),
          ("mem", 9),
          ("memb", 110),
          ("notApplicable", 254),
          ("opnl", 53),
          ("pci", 29),
          ("pcic", 30),
          ("pcir", 23),
          ("pcmu", 98),
          ("pdb", 135),
          ("psu", 42),
          ("psuFan", 157),
          ("psubpA", 38),
          ("psubpB", 39),
          ("riser", 97),
          ("sas", 151),
          ("sc", 10),
          ("snsu", 192),
          ("sw", 148),
          ("swbp", 56),
          ("tag", 11),
          ("tape", 54),
          ("tapebp", 171),
          ("unknown", 255),
          ("unspecified", 253),
          ("ups", 196),
          ("way", 7),
          ("xbuA", 16),
          ("xbuB", 19),
          ("xsb", 12),
          ("xscfA", 31),
          ("xscfB", 32),
          ("xscfC", 33),
          ("xscfu", 155))
    )



class ScfValidStatus(Integer32, TextualConvention):
    status = "current"
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



class ScfLEDState(Integer32, TextualConvention):
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
        *(("blinking", 3),
          ("off", 1),
          ("on", 2))
    )



class ScfModeSwitchState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("service", 2))
    )



class ScfStateTC(Integer32, TextualConvention):
    status = "current"
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
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("change", 254),
          ("deconfigured", 7),
          ("idle", 5),
          ("init", 3),
          ("notConfigured", 4),
          ("run", 6),
          ("stop", 2),
          ("unknown", 255),
          ("unmounted", 1))
    )



class ScfErrorStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("change", 254),
          ("degraded", 2),
          ("faulted", 3),
          ("normal", 1),
          ("unknown", 255))
    )



class ScfDomainStatusTC(Integer32, TextualConvention):
    status = "current"
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
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("boot", 5),
          ("change", 254),
          ("initialize", 4),
          ("panic", 2),
          ("powerOff", 1),
          ("prom", 7),
          ("running", 6),
          ("shutdown", 3),
          ("unknown", 255))
    )



class ScfDomainConfigPolicy(Integer32, TextualConvention):
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
        *(("fru", 1),
          ("system", 3),
          ("xsb", 2))
    )



class ScfIoBoxLEDState(Integer32, TextualConvention):
    status = "current"
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
        *(("blinkFast", 4),
          ("blinkSlow", 3),
          ("feedbackFlash", 5),
          ("off", 1),
          ("on", 6),
          ("standbyBlink", 2),
          ("unknown", 7))
    )



class ScfIoBoxComponentLocation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("left", 1),
          ("right", 2))
    )



class ScfIoBoxComponentType(Integer32, TextualConvention):
    status = "current"
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
        *(("boat", 4),
          ("cp", 2),
          ("dlc", 6),
          ("ps", 3),
          ("ulc", 5),
          ("unknown", 1))
    )



class ScfIoBoatTypeTC(Integer32, TextualConvention):
    status = "current"
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
        *(("max", 5),
          ("notPresent", 1),
          ("pcie", 3),
          ("pcix", 4),
          ("unknown", 2))
    )



class ScfIoBoxEnabledAlarms(Bits, TextualConvention):
    status = "current"


class ScfCodState(Integer32, TextualConvention):
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
        *(("disabled", 1),
          ("enabled", 2),
          ("notApplicable", 3))
    )



class ScfBoardSubTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 254),
          ("type1", 4),
          ("type2", 5),
          ("typeA", 1),
          ("typeB", 2),
          ("typeC", 3),
          ("unknown", 255))
    )



class ScfTrapEventTypeTC(Integer32, TextualConvention):
    status = "current"
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
        *(("acFail", 4),
          ("acRestore", 5),
          ("acRestoreComplete", 9),
          ("acRestoreFail", 8),
          ("acRestoreStart", 7),
          ("add", 2),
          ("changeComplete", 6),
          ("other", 1),
          ("remove", 3))
    )



class ScfTrapStatusEventTypeTC(Integer32, TextualConvention):
    status = "current"
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
        *(("degraded", 2),
          ("faulted", 3),
          ("information", 5),
          ("other", 1),
          ("recover", 4))
    )



class ScfDomainStatusAlarmType(Integer32, TextualConvention):
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
        *(("other", 1),
          ("panic", 3),
          ("status", 2))
    )



class ScfTrapIoBoxTempEventTypeTC(Integer32, TextualConvention):
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
        *(("other", 1),
          ("overTemp", 2),
          ("recover", 3))
    )



class ScfIoBoxLEDType(Integer32, TextualConvention):
    status = "current"
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("data", 10),
          ("locate", 2),
          ("mgmt", 9),
          ("overtemp", 8),
          ("powerAC", 5),
          ("powerDC", 4),
          ("rtr", 7),
          ("service", 6),
          ("unknown", 1))
    )



class ScfTrapModeSwitchEventTypeTC(Integer32, TextualConvention):
    status = "current"
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
        *(("modeToLocked", 4),
          ("modeToService", 5),
          ("other", 1),
          ("powerLong", 3),
          ("powerShort", 2))
    )



class ScfIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ScfIoBoxIndex(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )



class ScfXsbIndex(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class ScfDRState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("configured", 2),
          ("disconnected", 4),
          ("unconfigured", 1),
          ("unknown", 255),
          ("waiting", 3))
    )



class ScfUsageState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )



class ScfTestState(Integer32, TextualConvention):
    status = "current"
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
        *(("failed", 5),
          ("passed", 4),
          ("testing", 3),
          ("unknown", 2),
          ("unmounted", 1))
    )



class ScfAssignmentState(Integer32, TextualConvention):
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
        *(("assigned", 3),
          ("available", 2),
          ("unavailable", 1))
    )



class ScfConnectivityState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("disconnected", 1))
    )



class ScfConfigurationState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 2),
          ("unconfigured", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Fujitsu_ObjectIdentity = ObjectIdentity
fujitsu = _Fujitsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1)
)
_Solaris_ObjectIdentity = ObjectIdentity
solaris = _Solaris_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15)
)
_SparcEnterprise_ObjectIdentity = ObjectIdentity
sparcEnterprise = _SparcEnterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3)
)
_ScfObjects_ObjectIdentity = ObjectIdentity
scfObjects = _ScfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1)
)
_ScfInfo_ObjectIdentity = ObjectIdentity
scfInfo = _ScfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 1)
)
_ScfAgentId_Type = Integer32
_ScfAgentId_Object = MibScalar
scfAgentId = _ScfAgentId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 1, 1),
    _ScfAgentId_Type()
)
scfAgentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfAgentId.setStatus("current")
_ScfAgentNumber_Type = Integer32
_ScfAgentNumber_Object = MibScalar
scfAgentNumber = _ScfAgentNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 1, 2),
    _ScfAgentNumber_Type()
)
scfAgentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfAgentNumber.setStatus("current")
_ScfAgentTable_Object = MibTable
scfAgentTable = _ScfAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    scfAgentTable.setStatus("current")
_ScfAgentEntry_Object = MibTableRow
scfAgentEntry = _ScfAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 1, 3, 1)
)
scfAgentEntry.setIndexNames(
    (0, "OPL-SP-MIB", "scfAgentIndex"),
)
if mibBuilder.loadTexts:
    scfAgentEntry.setStatus("current")
_ScfAgentIndex_Type = ScfIndex
_ScfAgentIndex_Object = MibTableColumn
scfAgentIndex = _ScfAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 1, 3, 1, 1),
    _ScfAgentIndex_Type()
)
scfAgentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfAgentIndex.setStatus("current")
_ScfXcpVersion_Type = DisplayString
_ScfXcpVersion_Object = MibTableColumn
scfXcpVersion = _ScfXcpVersion_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 1, 3, 1, 2),
    _ScfXcpVersion_Type()
)
scfXcpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfXcpVersion.setStatus("current")
_ScfIpAddressPortNumber_Type = Integer32
_ScfIpAddressPortNumber_Object = MibScalar
scfIpAddressPortNumber = _ScfIpAddressPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 1, 4),
    _ScfIpAddressPortNumber_Type()
)
scfIpAddressPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIpAddressPortNumber.setStatus("current")
_ScfIpAddressNumber_Type = Integer32
_ScfIpAddressNumber_Object = MibScalar
scfIpAddressNumber = _ScfIpAddressNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 1, 5),
    _ScfIpAddressNumber_Type()
)
scfIpAddressNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIpAddressNumber.setStatus("current")
_ScfIpAddressTable_Object = MibTable
scfIpAddressTable = _ScfIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    scfIpAddressTable.setStatus("current")
_ScfIpAddressEntry_Object = MibTableRow
scfIpAddressEntry = _ScfIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 1, 6, 1)
)
scfIpAddressEntry.setIndexNames(
    (0, "OPL-SP-MIB", "scfIpAddressIndex"),
)
if mibBuilder.loadTexts:
    scfIpAddressEntry.setStatus("current")
_ScfIpAddressIndex_Type = ScfIndex
_ScfIpAddressIndex_Object = MibTableColumn
scfIpAddressIndex = _ScfIpAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 1, 6, 1, 1),
    _ScfIpAddressIndex_Type()
)
scfIpAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIpAddressIndex.setStatus("current")
_ScfIpAddress_Type = IpAddress
_ScfIpAddress_Object = MibTableColumn
scfIpAddress = _ScfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 1, 6, 1, 2),
    _ScfIpAddress_Type()
)
scfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIpAddress.setStatus("current")
_ScfState_ObjectIdentity = ObjectIdentity
scfState = _ScfState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 2)
)
_ScfSystemState_Type = ScfErrorStatus
_ScfSystemState_Object = MibScalar
scfSystemState = _ScfSystemState_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 2, 1),
    _ScfSystemState_Type()
)
scfSystemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfSystemState.setStatus("current")
_ScfFirmwareState_Type = ScfErrorStatus
_ScfFirmwareState_Object = MibScalar
scfFirmwareState = _ScfFirmwareState_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 2, 2),
    _ScfFirmwareState_Type()
)
scfFirmwareState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfFirmwareState.setStatus("current")
_ScfHardwareState_Type = ScfErrorStatus
_ScfHardwareState_Object = MibScalar
scfHardwareState = _ScfHardwareState_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 2, 3),
    _ScfHardwareState_Type()
)
scfHardwareState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfHardwareState.setStatus("current")
_ScfModeSwitch_Type = ScfModeSwitchState
_ScfModeSwitch_Object = MibScalar
scfModeSwitch = _ScfModeSwitch_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 2, 4),
    _ScfModeSwitch_Type()
)
scfModeSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfModeSwitch.setStatus("current")
_ScfMonitorInfo_ObjectIdentity = ObjectIdentity
scfMonitorInfo = _ScfMonitorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 3)
)
_ScfMonitorNumber_Type = Integer32
_ScfMonitorNumber_Object = MibScalar
scfMonitorNumber = _ScfMonitorNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 3, 1),
    _ScfMonitorNumber_Type()
)
scfMonitorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMonitorNumber.setStatus("current")
_ScfMonitorTable_Object = MibTable
scfMonitorTable = _ScfMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    scfMonitorTable.setStatus("current")
_ScfMonitorEntry_Object = MibTableRow
scfMonitorEntry = _ScfMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 3, 2, 1)
)
scfMonitorEntry.setIndexNames(
    (0, "OPL-SP-MIB", "scfMonitorBoardType"),
    (0, "OPL-SP-MIB", "scfMonitorBoardId"),
    (0, "OPL-SP-MIB", "scfMonitorModuleType"),
    (0, "OPL-SP-MIB", "scfMonitorModuleId"),
    (0, "OPL-SP-MIB", "scfMonitorType"),
    (0, "OPL-SP-MIB", "scfMonitorId"),
)
if mibBuilder.loadTexts:
    scfMonitorEntry.setStatus("current")
_ScfMonitorBoardType_Type = ScfComponentType
_ScfMonitorBoardType_Object = MibTableColumn
scfMonitorBoardType = _ScfMonitorBoardType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 3, 2, 1, 1),
    _ScfMonitorBoardType_Type()
)
scfMonitorBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMonitorBoardType.setStatus("current")
_ScfMonitorBoardId_Type = ScfIndex
_ScfMonitorBoardId_Object = MibTableColumn
scfMonitorBoardId = _ScfMonitorBoardId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 3, 2, 1, 2),
    _ScfMonitorBoardId_Type()
)
scfMonitorBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMonitorBoardId.setStatus("current")
_ScfMonitorModuleType_Type = ScfComponentType
_ScfMonitorModuleType_Object = MibTableColumn
scfMonitorModuleType = _ScfMonitorModuleType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 3, 2, 1, 3),
    _ScfMonitorModuleType_Type()
)
scfMonitorModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMonitorModuleType.setStatus("current")
_ScfMonitorModuleId_Type = ScfIndex
_ScfMonitorModuleId_Object = MibTableColumn
scfMonitorModuleId = _ScfMonitorModuleId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 3, 2, 1, 4),
    _ScfMonitorModuleId_Type()
)
scfMonitorModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMonitorModuleId.setStatus("current")
_ScfMonitorType_Type = ScfMonitorTypeTC
_ScfMonitorType_Object = MibTableColumn
scfMonitorType = _ScfMonitorType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 3, 2, 1, 5),
    _ScfMonitorType_Type()
)
scfMonitorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMonitorType.setStatus("current")
_ScfMonitorId_Type = ScfIndex
_ScfMonitorId_Object = MibTableColumn
scfMonitorId = _ScfMonitorId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 3, 2, 1, 6),
    _ScfMonitorId_Type()
)
scfMonitorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMonitorId.setStatus("current")
_ScfMonitorDescription_Type = DisplayString
_ScfMonitorDescription_Object = MibTableColumn
scfMonitorDescription = _ScfMonitorDescription_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 3, 2, 1, 7),
    _ScfMonitorDescription_Type()
)
scfMonitorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMonitorDescription.setStatus("current")
_ScfMonitorAdditionalInfo_Type = DisplayString
_ScfMonitorAdditionalInfo_Object = MibTableColumn
scfMonitorAdditionalInfo = _ScfMonitorAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 3, 2, 1, 8),
    _ScfMonitorAdditionalInfo_Type()
)
scfMonitorAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMonitorAdditionalInfo.setStatus("current")
_ScfMonitorUnits_Type = DisplayString
_ScfMonitorUnits_Object = MibTableColumn
scfMonitorUnits = _ScfMonitorUnits_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 3, 2, 1, 9),
    _ScfMonitorUnits_Type()
)
scfMonitorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMonitorUnits.setStatus("current")
_ScfMonitorStatus_Type = ScfValidStatus
_ScfMonitorStatus_Object = MibTableColumn
scfMonitorStatus = _ScfMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 3, 2, 1, 10),
    _ScfMonitorStatus_Type()
)
scfMonitorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMonitorStatus.setStatus("current")
_ScfMonitorValue_Type = Integer32
_ScfMonitorValue_Object = MibTableColumn
scfMonitorValue = _ScfMonitorValue_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 3, 2, 1, 11),
    _ScfMonitorValue_Type()
)
scfMonitorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMonitorValue.setStatus("current")
_ScfMonitorValueStatus_Type = ScfErrorStatus
_ScfMonitorValueStatus_Object = MibTableColumn
scfMonitorValueStatus = _ScfMonitorValueStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 3, 2, 1, 12),
    _ScfMonitorValueStatus_Type()
)
scfMonitorValueStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMonitorValueStatus.setStatus("current")
_ScfSystemInfo_ObjectIdentity = ObjectIdentity
scfSystemInfo = _ScfSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4)
)
_ScfSystemName_Type = DisplayString
_ScfSystemName_Object = MibScalar
scfSystemName = _ScfSystemName_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 1),
    _ScfSystemName_Type()
)
scfSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfSystemName.setStatus("current")
_ScfSystemType_Type = DisplayString
_ScfSystemType_Object = MibScalar
scfSystemType = _ScfSystemType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 2),
    _ScfSystemType_Type()
)
scfSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfSystemType.setStatus("current")
_ScfSystemSerialNumber_Type = DisplayString
_ScfSystemSerialNumber_Object = MibScalar
scfSystemSerialNumber = _ScfSystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 3),
    _ScfSystemSerialNumber_Type()
)
scfSystemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfSystemSerialNumber.setStatus("current")
_ScfSystemAdditionalInfo_Type = DisplayString
_ScfSystemAdditionalInfo_Object = MibScalar
scfSystemAdditionalInfo = _ScfSystemAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 4),
    _ScfSystemAdditionalInfo_Type()
)
scfSystemAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfSystemAdditionalInfo.setStatus("current")
_ScfSystemCpuNumber_Type = Integer32
_ScfSystemCpuNumber_Object = MibScalar
scfSystemCpuNumber = _ScfSystemCpuNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 5),
    _ScfSystemCpuNumber_Type()
)
scfSystemCpuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfSystemCpuNumber.setStatus("current")
_ScfSystemMemoryCapacity_Type = Integer32
_ScfSystemMemoryCapacity_Object = MibScalar
scfSystemMemoryCapacity = _ScfSystemMemoryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 6),
    _ScfSystemMemoryCapacity_Type()
)
scfSystemMemoryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfSystemMemoryCapacity.setStatus("current")
if mibBuilder.loadTexts:
    scfSystemMemoryCapacity.setUnits("GB")
_ScfSystemReadyLED_Type = ScfLEDState
_ScfSystemReadyLED_Object = MibScalar
scfSystemReadyLED = _ScfSystemReadyLED_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 7),
    _ScfSystemReadyLED_Type()
)
scfSystemReadyLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfSystemReadyLED.setStatus("current")
_ScfSystemPowerLED_Type = ScfLEDState
_ScfSystemPowerLED_Object = MibScalar
scfSystemPowerLED = _ScfSystemPowerLED_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 8),
    _ScfSystemPowerLED_Type()
)
scfSystemPowerLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfSystemPowerLED.setStatus("current")
_ScfSystemCheckLED_Type = ScfLEDState
_ScfSystemCheckLED_Object = MibScalar
scfSystemCheckLED = _ScfSystemCheckLED_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 9),
    _ScfSystemCheckLED_Type()
)
scfSystemCheckLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfSystemCheckLED.setStatus("current")
_ScfSystemActualPowerConsumption_ObjectIdentity = ObjectIdentity
scfSystemActualPowerConsumption = _ScfSystemActualPowerConsumption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 10)
)
_ScfSystemActualPowerConsumptionValue_Type = Integer32
_ScfSystemActualPowerConsumptionValue_Object = MibScalar
scfSystemActualPowerConsumptionValue = _ScfSystemActualPowerConsumptionValue_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 10, 1),
    _ScfSystemActualPowerConsumptionValue_Type()
)
scfSystemActualPowerConsumptionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfSystemActualPowerConsumptionValue.setStatus("current")
_ScfSystemActualPowerConsumptionUnit_Type = DisplayString
_ScfSystemActualPowerConsumptionUnit_Object = MibScalar
scfSystemActualPowerConsumptionUnit = _ScfSystemActualPowerConsumptionUnit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 10, 2),
    _ScfSystemActualPowerConsumptionUnit_Type()
)
scfSystemActualPowerConsumptionUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfSystemActualPowerConsumptionUnit.setStatus("current")
_ScfSystemActualPowerMinPollingInterval_Type = Integer32
_ScfSystemActualPowerMinPollingInterval_Object = MibScalar
scfSystemActualPowerMinPollingInterval = _ScfSystemActualPowerMinPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 10, 3),
    _ScfSystemActualPowerMinPollingInterval_Type()
)
scfSystemActualPowerMinPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfSystemActualPowerMinPollingInterval.setStatus("current")
_ScfSystemAirFlow_ObjectIdentity = ObjectIdentity
scfSystemAirFlow = _ScfSystemAirFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 11)
)
_ScfSystemExhaustAirFlowValue_Type = Integer32
_ScfSystemExhaustAirFlowValue_Object = MibScalar
scfSystemExhaustAirFlowValue = _ScfSystemExhaustAirFlowValue_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 11, 1),
    _ScfSystemExhaustAirFlowValue_Type()
)
scfSystemExhaustAirFlowValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfSystemExhaustAirFlowValue.setStatus("current")
_ScfSystemExhaustAirFlowUnit_Type = DisplayString
_ScfSystemExhaustAirFlowUnit_Object = MibScalar
scfSystemExhaustAirFlowUnit = _ScfSystemExhaustAirFlowUnit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 11, 2),
    _ScfSystemExhaustAirFlowUnit_Type()
)
scfSystemExhaustAirFlowUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfSystemExhaustAirFlowUnit.setStatus("current")
_ScfSystemExhaustAirFlowMinPollingInterval_Type = Integer32
_ScfSystemExhaustAirFlowMinPollingInterval_Object = MibScalar
scfSystemExhaustAirFlowMinPollingInterval = _ScfSystemExhaustAirFlowMinPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 11, 3),
    _ScfSystemExhaustAirFlowMinPollingInterval_Type()
)
scfSystemExhaustAirFlowMinPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfSystemExhaustAirFlowMinPollingInterval.setStatus("current")
_ScfSystemAmbientTemperature_ObjectIdentity = ObjectIdentity
scfSystemAmbientTemperature = _ScfSystemAmbientTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 12)
)
_ScfSystemAmbientTemperatureValue_Type = DisplayString
_ScfSystemAmbientTemperatureValue_Object = MibScalar
scfSystemAmbientTemperatureValue = _ScfSystemAmbientTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 12, 1),
    _ScfSystemAmbientTemperatureValue_Type()
)
scfSystemAmbientTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfSystemAmbientTemperatureValue.setStatus("current")
_ScfSystemAmbientTemperatureUnit_Type = DisplayString
_ScfSystemAmbientTemperatureUnit_Object = MibScalar
scfSystemAmbientTemperatureUnit = _ScfSystemAmbientTemperatureUnit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 12, 2),
    _ScfSystemAmbientTemperatureUnit_Type()
)
scfSystemAmbientTemperatureUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfSystemAmbientTemperatureUnit.setStatus("current")
_ScfSystemAmbientTemperatureMinPollingInterval_Type = Integer32
_ScfSystemAmbientTemperatureMinPollingInterval_Object = MibScalar
scfSystemAmbientTemperatureMinPollingInterval = _ScfSystemAmbientTemperatureMinPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 12, 3),
    _ScfSystemAmbientTemperatureMinPollingInterval_Type()
)
scfSystemAmbientTemperatureMinPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfSystemAmbientTemperatureMinPollingInterval.setStatus("current")
_ScfSystemPowerSource_ObjectIdentity = ObjectIdentity
scfSystemPowerSource = _ScfSystemPowerSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 13)
)
_ScfSystemPermittedPowerConsumption_ObjectIdentity = ObjectIdentity
scfSystemPermittedPowerConsumption = _ScfSystemPermittedPowerConsumption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 14)
)
_ScfSystemPermittedPowerConsumptionValue_Type = Integer32
_ScfSystemPermittedPowerConsumptionValue_Object = MibScalar
scfSystemPermittedPowerConsumptionValue = _ScfSystemPermittedPowerConsumptionValue_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 14, 1),
    _ScfSystemPermittedPowerConsumptionValue_Type()
)
scfSystemPermittedPowerConsumptionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfSystemPermittedPowerConsumptionValue.setStatus("current")
_ScfSystemPermittedPowerConsumptionUnit_Type = DisplayString
_ScfSystemPermittedPowerConsumptionUnit_Object = MibScalar
scfSystemPermittedPowerConsumptionUnit = _ScfSystemPermittedPowerConsumptionUnit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 14, 2),
    _ScfSystemPermittedPowerConsumptionUnit_Type()
)
scfSystemPermittedPowerConsumptionUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfSystemPermittedPowerConsumptionUnit.setStatus("current")
_ScfSystemAvailablePowerConsumption_ObjectIdentity = ObjectIdentity
scfSystemAvailablePowerConsumption = _ScfSystemAvailablePowerConsumption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 4, 15)
)
_ScfDomainInfo_ObjectIdentity = ObjectIdentity
scfDomainInfo = _ScfDomainInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 5)
)
_ScfDomainNumber_Type = Integer32
_ScfDomainNumber_Object = MibScalar
scfDomainNumber = _ScfDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 5, 1),
    _ScfDomainNumber_Type()
)
scfDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfDomainNumber.setStatus("current")
_ScfDomainTable_Object = MibTable
scfDomainTable = _ScfDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    scfDomainTable.setStatus("current")
_ScfDomainEntry_Object = MibTableRow
scfDomainEntry = _ScfDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 5, 2, 1)
)
scfDomainEntry.setIndexNames(
    (0, "OPL-SP-MIB", "scfDomainId"),
)
if mibBuilder.loadTexts:
    scfDomainEntry.setStatus("current")
_ScfDomainId_Type = ScfIndex
_ScfDomainId_Object = MibTableColumn
scfDomainId = _ScfDomainId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 5, 2, 1, 1),
    _ScfDomainId_Type()
)
scfDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfDomainId.setStatus("current")
_ScfDomainCpuNumber_Type = Integer32
_ScfDomainCpuNumber_Object = MibTableColumn
scfDomainCpuNumber = _ScfDomainCpuNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 5, 2, 1, 2),
    _ScfDomainCpuNumber_Type()
)
scfDomainCpuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfDomainCpuNumber.setStatus("current")
_ScfDomainMemoryCapacity_Type = Integer32
_ScfDomainMemoryCapacity_Object = MibTableColumn
scfDomainMemoryCapacity = _ScfDomainMemoryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 5, 2, 1, 3),
    _ScfDomainMemoryCapacity_Type()
)
scfDomainMemoryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfDomainMemoryCapacity.setStatus("current")
if mibBuilder.loadTexts:
    scfDomainMemoryCapacity.setUnits("GB")
_ScfDomainObpVersion_Type = DisplayString
_ScfDomainObpVersion_Object = MibTableColumn
scfDomainObpVersion = _ScfDomainObpVersion_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 5, 2, 1, 4),
    _ScfDomainObpVersion_Type()
)
scfDomainObpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfDomainObpVersion.setStatus("current")
_ScfDomainObpAdditionalInfo_Type = DisplayString
_ScfDomainObpAdditionalInfo_Object = MibTableColumn
scfDomainObpAdditionalInfo = _ScfDomainObpAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 5, 2, 1, 5),
    _ScfDomainObpAdditionalInfo_Type()
)
scfDomainObpAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfDomainObpAdditionalInfo.setStatus("current")
_ScfDomainOsMachine_Type = DisplayString
_ScfDomainOsMachine_Object = MibTableColumn
scfDomainOsMachine = _ScfDomainOsMachine_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 5, 2, 1, 6),
    _ScfDomainOsMachine_Type()
)
scfDomainOsMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfDomainOsMachine.setStatus("current")
_ScfDomainOsRelease_Type = DisplayString
_ScfDomainOsRelease_Object = MibTableColumn
scfDomainOsRelease = _ScfDomainOsRelease_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 5, 2, 1, 7),
    _ScfDomainOsRelease_Type()
)
scfDomainOsRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfDomainOsRelease.setStatus("current")
_ScfDomainOsSysName_Type = DisplayString
_ScfDomainOsSysName_Object = MibTableColumn
scfDomainOsSysName = _ScfDomainOsSysName_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 5, 2, 1, 8),
    _ScfDomainOsSysName_Type()
)
scfDomainOsSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfDomainOsSysName.setStatus("current")
_ScfDomainOsNodeName_Type = DisplayString
_ScfDomainOsNodeName_Object = MibTableColumn
scfDomainOsNodeName = _ScfDomainOsNodeName_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 5, 2, 1, 9),
    _ScfDomainOsNodeName_Type()
)
scfDomainOsNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfDomainOsNodeName.setStatus("current")
_ScfDomainOsVersion_Type = DisplayString
_ScfDomainOsVersion_Object = MibTableColumn
scfDomainOsVersion = _ScfDomainOsVersion_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 5, 2, 1, 10),
    _ScfDomainOsVersion_Type()
)
scfDomainOsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfDomainOsVersion.setStatus("current")
_ScfDomainOsAdditionalInfo_Type = DisplayString
_ScfDomainOsAdditionalInfo_Object = MibTableColumn
scfDomainOsAdditionalInfo = _ScfDomainOsAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 5, 2, 1, 11),
    _ScfDomainOsAdditionalInfo_Type()
)
scfDomainOsAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfDomainOsAdditionalInfo.setStatus("current")
_ScfDomainValid_Type = ScfValidStatus
_ScfDomainValid_Object = MibTableColumn
scfDomainValid = _ScfDomainValid_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 5, 2, 1, 12),
    _ScfDomainValid_Type()
)
scfDomainValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfDomainValid.setStatus("current")
_ScfDomainXsbs_Type = DisplayString
_ScfDomainXsbs_Object = MibTableColumn
scfDomainXsbs = _ScfDomainXsbs_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 5, 2, 1, 13),
    _ScfDomainXsbs_Type()
)
scfDomainXsbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfDomainXsbs.setStatus("current")
_ScfDomainStatus_Type = ScfDomainStatusTC
_ScfDomainStatus_Object = MibTableColumn
scfDomainStatus = _ScfDomainStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 5, 2, 1, 14),
    _ScfDomainStatus_Type()
)
scfDomainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfDomainStatus.setStatus("current")
_ScfDomainErrorStatus_Type = ScfErrorStatus
_ScfDomainErrorStatus_Object = MibTableColumn
scfDomainErrorStatus = _ScfDomainErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 5, 2, 1, 15),
    _ScfDomainErrorStatus_Type()
)
scfDomainErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfDomainErrorStatus.setStatus("current")
_ScfDomainConfigurationPolicy_Type = ScfDomainConfigPolicy
_ScfDomainConfigurationPolicy_Object = MibTableColumn
scfDomainConfigurationPolicy = _ScfDomainConfigurationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 5, 2, 1, 16),
    _ScfDomainConfigurationPolicy_Type()
)
scfDomainConfigurationPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfDomainConfigurationPolicy.setStatus("current")
_ScfXsbInfo_ObjectIdentity = ObjectIdentity
scfXsbInfo = _ScfXsbInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 6)
)
_ScfXsbType_Type = Integer32
_ScfXsbType_Object = MibScalar
scfXsbType = _ScfXsbType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 6, 1),
    _ScfXsbType_Type()
)
scfXsbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfXsbType.setStatus("current")
_ScfXsbNumber_Type = Integer32
_ScfXsbNumber_Object = MibScalar
scfXsbNumber = _ScfXsbNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 6, 2),
    _ScfXsbNumber_Type()
)
scfXsbNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfXsbNumber.setStatus("current")
_ScfXsbTable_Object = MibTable
scfXsbTable = _ScfXsbTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    scfXsbTable.setStatus("current")
_ScfXsbEntry_Object = MibTableRow
scfXsbEntry = _ScfXsbEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 6, 3, 1)
)
scfXsbEntry.setIndexNames(
    (0, "OPL-SP-MIB", "scfXsbId"),
)
if mibBuilder.loadTexts:
    scfXsbEntry.setStatus("current")
_ScfXsbId_Type = ScfXsbIndex
_ScfXsbId_Object = MibTableColumn
scfXsbId = _ScfXsbId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 6, 3, 1, 1),
    _ScfXsbId_Type()
)
scfXsbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfXsbId.setStatus("current")
_ScfXsbStatus_Type = ScfStateTC
_ScfXsbStatus_Object = MibTableColumn
scfXsbStatus = _ScfXsbStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 6, 3, 1, 2),
    _ScfXsbStatus_Type()
)
scfXsbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfXsbStatus.setStatus("current")
_ScfXsbErrorStatus_Type = ScfErrorStatus
_ScfXsbErrorStatus_Object = MibTableColumn
scfXsbErrorStatus = _ScfXsbErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 6, 3, 1, 3),
    _ScfXsbErrorStatus_Type()
)
scfXsbErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfXsbErrorStatus.setStatus("current")
_ScfXsbDomainId_Type = Integer32
_ScfXsbDomainId_Object = MibTableColumn
scfXsbDomainId = _ScfXsbDomainId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 6, 3, 1, 4),
    _ScfXsbDomainId_Type()
)
scfXsbDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfXsbDomainId.setStatus("current")
_ScfXsbDrStatus_Type = ScfDRState
_ScfXsbDrStatus_Object = MibTableColumn
scfXsbDrStatus = _ScfXsbDrStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 6, 3, 1, 5),
    _ScfXsbDrStatus_Type()
)
scfXsbDrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfXsbDrStatus.setStatus("current")
_ScfXsbSubStatusPower_Type = ScfUsageState
_ScfXsbSubStatusPower_Object = MibTableColumn
scfXsbSubStatusPower = _ScfXsbSubStatusPower_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 6, 3, 1, 6),
    _ScfXsbSubStatusPower_Type()
)
scfXsbSubStatusPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfXsbSubStatusPower.setStatus("current")
_ScfXsbSubStatusTest_Type = ScfTestState
_ScfXsbSubStatusTest_Object = MibTableColumn
scfXsbSubStatusTest = _ScfXsbSubStatusTest_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 6, 3, 1, 7),
    _ScfXsbSubStatusTest_Type()
)
scfXsbSubStatusTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfXsbSubStatusTest.setStatus("current")
_ScfXsbSubStatusAssignment_Type = ScfAssignmentState
_ScfXsbSubStatusAssignment_Object = MibTableColumn
scfXsbSubStatusAssignment = _ScfXsbSubStatusAssignment_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 6, 3, 1, 8),
    _ScfXsbSubStatusAssignment_Type()
)
scfXsbSubStatusAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfXsbSubStatusAssignment.setStatus("current")
_ScfXsbSubStatusConnectivity_Type = ScfConnectivityState
_ScfXsbSubStatusConnectivity_Object = MibTableColumn
scfXsbSubStatusConnectivity = _ScfXsbSubStatusConnectivity_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 6, 3, 1, 9),
    _ScfXsbSubStatusConnectivity_Type()
)
scfXsbSubStatusConnectivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfXsbSubStatusConnectivity.setStatus("current")
_ScfXsbSubStatusConfiguration_Type = ScfConfigurationState
_ScfXsbSubStatusConfiguration_Object = MibTableColumn
scfXsbSubStatusConfiguration = _ScfXsbSubStatusConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 6, 3, 1, 10),
    _ScfXsbSubStatusConfiguration_Type()
)
scfXsbSubStatusConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfXsbSubStatusConfiguration.setStatus("current")
_ScfXsbSetupDID_Type = Integer32
_ScfXsbSetupDID_Object = MibTableColumn
scfXsbSetupDID = _ScfXsbSetupDID_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 6, 3, 1, 11),
    _ScfXsbSetupDID_Type()
)
scfXsbSetupDID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfXsbSetupDID.setStatus("current")
_ScfXsbNextDID_Type = Integer32
_ScfXsbNextDID_Object = MibTableColumn
scfXsbNextDID = _ScfXsbNextDID_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 6, 3, 1, 12),
    _ScfXsbNextDID_Type()
)
scfXsbNextDID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfXsbNextDID.setStatus("current")
_ScfLsbInfo_ObjectIdentity = ObjectIdentity
scfLsbInfo = _ScfLsbInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 7)
)
_ScfLsbType_Type = Integer32
_ScfLsbType_Object = MibScalar
scfLsbType = _ScfLsbType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 7, 1),
    _ScfLsbType_Type()
)
scfLsbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfLsbType.setStatus("current")
_ScfLsbNumber_Type = Integer32
_ScfLsbNumber_Object = MibScalar
scfLsbNumber = _ScfLsbNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 7, 2),
    _ScfLsbNumber_Type()
)
scfLsbNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfLsbNumber.setStatus("current")
_ScfLsbTable_Object = MibTable
scfLsbTable = _ScfLsbTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 7, 3)
)
if mibBuilder.loadTexts:
    scfLsbTable.setStatus("current")
_ScfLsbEntry_Object = MibTableRow
scfLsbEntry = _ScfLsbEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 7, 3, 1)
)
scfLsbEntry.setIndexNames(
    (0, "OPL-SP-MIB", "scfLsbDomainId"),
    (0, "OPL-SP-MIB", "scfLsbId"),
)
if mibBuilder.loadTexts:
    scfLsbEntry.setStatus("current")
_ScfLsbDomainId_Type = ScfIndex
_ScfLsbDomainId_Object = MibTableColumn
scfLsbDomainId = _ScfLsbDomainId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 7, 3, 1, 1),
    _ScfLsbDomainId_Type()
)
scfLsbDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfLsbDomainId.setStatus("current")
_ScfLsbId_Type = ScfIndex
_ScfLsbId_Object = MibTableColumn
scfLsbId = _ScfLsbId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 7, 3, 1, 2),
    _ScfLsbId_Type()
)
scfLsbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfLsbId.setStatus("current")
_ScfLsbXsbId_Type = DisplayString
_ScfLsbXsbId_Object = MibTableColumn
scfLsbXsbId = _ScfLsbXsbId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 7, 3, 1, 3),
    _ScfLsbXsbId_Type()
)
scfLsbXsbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfLsbXsbId.setStatus("current")
_ScfLsbNoMem_Type = ScfUsageState
_ScfLsbNoMem_Object = MibTableColumn
scfLsbNoMem = _ScfLsbNoMem_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 7, 3, 1, 4),
    _ScfLsbNoMem_Type()
)
scfLsbNoMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfLsbNoMem.setStatus("current")
_ScfLsbNoIo_Type = ScfUsageState
_ScfLsbNoIo_Object = MibTableColumn
scfLsbNoIo = _ScfLsbNoIo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 7, 3, 1, 5),
    _ScfLsbNoIo_Type()
)
scfLsbNoIo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfLsbNoIo.setStatus("current")
_ScfLsbFloatingBoard_Type = ScfUsageState
_ScfLsbFloatingBoard_Object = MibTableColumn
scfLsbFloatingBoard = _ScfLsbFloatingBoard_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 7, 3, 1, 6),
    _ScfLsbFloatingBoard_Type()
)
scfLsbFloatingBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfLsbFloatingBoard.setStatus("current")
_ScfBoardInfo_ObjectIdentity = ObjectIdentity
scfBoardInfo = _ScfBoardInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 8)
)
_ScfBoardNumber_Type = Integer32
_ScfBoardNumber_Object = MibScalar
scfBoardNumber = _ScfBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 8, 1),
    _ScfBoardNumber_Type()
)
scfBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfBoardNumber.setStatus("current")
_ScfBoardTable_Object = MibTable
scfBoardTable = _ScfBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    scfBoardTable.setStatus("current")
_ScfBoardEntry_Object = MibTableRow
scfBoardEntry = _ScfBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 8, 2, 1)
)
scfBoardEntry.setIndexNames(
    (0, "OPL-SP-MIB", "scfBoardType"),
    (0, "OPL-SP-MIB", "scfBoardId"),
)
if mibBuilder.loadTexts:
    scfBoardEntry.setStatus("current")
_ScfBoardType_Type = ScfComponentType
_ScfBoardType_Object = MibTableColumn
scfBoardType = _ScfBoardType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 8, 2, 1, 1),
    _ScfBoardType_Type()
)
scfBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfBoardType.setStatus("current")
_ScfBoardId_Type = ScfIndex
_ScfBoardId_Object = MibTableColumn
scfBoardId = _ScfBoardId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 8, 2, 1, 2),
    _ScfBoardId_Type()
)
scfBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfBoardId.setStatus("current")
_ScfBoardName_Type = DisplayString
_ScfBoardName_Object = MibTableColumn
scfBoardName = _ScfBoardName_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 8, 2, 1, 3),
    _ScfBoardName_Type()
)
scfBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfBoardName.setStatus("current")
_ScfBoardAdditionalInfo_Type = DisplayString
_ScfBoardAdditionalInfo_Object = MibTableColumn
scfBoardAdditionalInfo = _ScfBoardAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 8, 2, 1, 4),
    _ScfBoardAdditionalInfo_Type()
)
scfBoardAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfBoardAdditionalInfo.setStatus("current")
_ScfBoardXsbs_Type = Integer32
_ScfBoardXsbs_Object = MibTableColumn
scfBoardXsbs = _ScfBoardXsbs_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 8, 2, 1, 5),
    _ScfBoardXsbs_Type()
)
scfBoardXsbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfBoardXsbs.setStatus("current")
_ScfBoardState_Type = ScfStateTC
_ScfBoardState_Object = MibTableColumn
scfBoardState = _ScfBoardState_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 8, 2, 1, 6),
    _ScfBoardState_Type()
)
scfBoardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfBoardState.setStatus("current")
_ScfBoardCODEnabled_Type = ScfCodState
_ScfBoardCODEnabled_Object = MibTableColumn
scfBoardCODEnabled = _ScfBoardCODEnabled_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 8, 2, 1, 7),
    _ScfBoardCODEnabled_Type()
)
scfBoardCODEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfBoardCODEnabled.setStatus("current")
_ScfBoardSubType_Type = ScfBoardSubTypeTC
_ScfBoardSubType_Object = MibTableColumn
scfBoardSubType = _ScfBoardSubType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 8, 2, 1, 8),
    _ScfBoardSubType_Type()
)
scfBoardSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfBoardSubType.setStatus("current")
_ScfCpuInfo_ObjectIdentity = ObjectIdentity
scfCpuInfo = _ScfCpuInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 9)
)
_ScfCpuNumber_Type = Integer32
_ScfCpuNumber_Object = MibScalar
scfCpuNumber = _ScfCpuNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 9, 1),
    _ScfCpuNumber_Type()
)
scfCpuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfCpuNumber.setStatus("current")
_ScfCpuTable_Object = MibTable
scfCpuTable = _ScfCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 9, 2)
)
if mibBuilder.loadTexts:
    scfCpuTable.setStatus("current")
_ScfCpuEntry_Object = MibTableRow
scfCpuEntry = _ScfCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 9, 2, 1)
)
scfCpuEntry.setIndexNames(
    (0, "OPL-SP-MIB", "scfCpuBoardType"),
    (0, "OPL-SP-MIB", "scfCpuBoardId"),
    (0, "OPL-SP-MIB", "scfCpuModuleType"),
    (0, "OPL-SP-MIB", "scfCpuModuleId"),
    (0, "OPL-SP-MIB", "scfCpuSubType"),
    (0, "OPL-SP-MIB", "scfCpuSubId"),
)
if mibBuilder.loadTexts:
    scfCpuEntry.setStatus("current")
_ScfCpuBoardType_Type = ScfComponentType
_ScfCpuBoardType_Object = MibTableColumn
scfCpuBoardType = _ScfCpuBoardType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 9, 2, 1, 1),
    _ScfCpuBoardType_Type()
)
scfCpuBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfCpuBoardType.setStatus("current")
_ScfCpuBoardId_Type = ScfIndex
_ScfCpuBoardId_Object = MibTableColumn
scfCpuBoardId = _ScfCpuBoardId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 9, 2, 1, 2),
    _ScfCpuBoardId_Type()
)
scfCpuBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfCpuBoardId.setStatus("current")
_ScfCpuModuleType_Type = ScfComponentType
_ScfCpuModuleType_Object = MibTableColumn
scfCpuModuleType = _ScfCpuModuleType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 9, 2, 1, 3),
    _ScfCpuModuleType_Type()
)
scfCpuModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfCpuModuleType.setStatus("current")
_ScfCpuModuleId_Type = ScfIndex
_ScfCpuModuleId_Object = MibTableColumn
scfCpuModuleId = _ScfCpuModuleId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 9, 2, 1, 4),
    _ScfCpuModuleId_Type()
)
scfCpuModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfCpuModuleId.setStatus("current")
_ScfCpuSubType_Type = ScfComponentType
_ScfCpuSubType_Object = MibTableColumn
scfCpuSubType = _ScfCpuSubType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 9, 2, 1, 5),
    _ScfCpuSubType_Type()
)
scfCpuSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfCpuSubType.setStatus("current")
_ScfCpuSubId_Type = ScfIndex
_ScfCpuSubId_Object = MibTableColumn
scfCpuSubId = _ScfCpuSubId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 9, 2, 1, 6),
    _ScfCpuSubId_Type()
)
scfCpuSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfCpuSubId.setStatus("current")
_ScfCpuType_Type = DisplayString
_ScfCpuType_Object = MibTableColumn
scfCpuType = _ScfCpuType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 9, 2, 1, 7),
    _ScfCpuType_Type()
)
scfCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfCpuType.setStatus("current")
_ScfCpuFrequency_Type = Integer32
_ScfCpuFrequency_Object = MibTableColumn
scfCpuFrequency = _ScfCpuFrequency_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 9, 2, 1, 8),
    _ScfCpuFrequency_Type()
)
scfCpuFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfCpuFrequency.setStatus("current")
if mibBuilder.loadTexts:
    scfCpuFrequency.setUnits("MHz")
_ScfCpuAdditionalInfo_Type = DisplayString
_ScfCpuAdditionalInfo_Object = MibTableColumn
scfCpuAdditionalInfo = _ScfCpuAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 9, 2, 1, 9),
    _ScfCpuAdditionalInfo_Type()
)
scfCpuAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfCpuAdditionalInfo.setStatus("current")
_ScfCpuState_Type = ScfStateTC
_ScfCpuState_Object = MibTableColumn
scfCpuState = _ScfCpuState_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 9, 2, 1, 10),
    _ScfCpuState_Type()
)
scfCpuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfCpuState.setStatus("current")
_ScfMemoryInfo_ObjectIdentity = ObjectIdentity
scfMemoryInfo = _ScfMemoryInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 10)
)
_ScfMemoryNumber_Type = Integer32
_ScfMemoryNumber_Object = MibScalar
scfMemoryNumber = _ScfMemoryNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 10, 1),
    _ScfMemoryNumber_Type()
)
scfMemoryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMemoryNumber.setStatus("current")
_ScfMemoryTable_Object = MibTable
scfMemoryTable = _ScfMemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 10, 2)
)
if mibBuilder.loadTexts:
    scfMemoryTable.setStatus("current")
_ScfMemoryEntry_Object = MibTableRow
scfMemoryEntry = _ScfMemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 10, 2, 1)
)
scfMemoryEntry.setIndexNames(
    (0, "OPL-SP-MIB", "scfMemoryBoardType"),
    (0, "OPL-SP-MIB", "scfMemoryBoardId"),
    (0, "OPL-SP-MIB", "scfMemoryModuleType"),
    (0, "OPL-SP-MIB", "scfMemoryModuleId"),
    (0, "OPL-SP-MIB", "scfMemorySubType"),
    (0, "OPL-SP-MIB", "scfMemorySubId"),
)
if mibBuilder.loadTexts:
    scfMemoryEntry.setStatus("current")
_ScfMemoryBoardType_Type = ScfComponentType
_ScfMemoryBoardType_Object = MibTableColumn
scfMemoryBoardType = _ScfMemoryBoardType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 10, 2, 1, 1),
    _ScfMemoryBoardType_Type()
)
scfMemoryBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMemoryBoardType.setStatus("current")
_ScfMemoryBoardId_Type = ScfIndex
_ScfMemoryBoardId_Object = MibTableColumn
scfMemoryBoardId = _ScfMemoryBoardId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 10, 2, 1, 2),
    _ScfMemoryBoardId_Type()
)
scfMemoryBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMemoryBoardId.setStatus("current")
_ScfMemoryModuleType_Type = ScfComponentType
_ScfMemoryModuleType_Object = MibTableColumn
scfMemoryModuleType = _ScfMemoryModuleType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 10, 2, 1, 3),
    _ScfMemoryModuleType_Type()
)
scfMemoryModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMemoryModuleType.setStatus("current")
_ScfMemoryModuleId_Type = ScfIndex
_ScfMemoryModuleId_Object = MibTableColumn
scfMemoryModuleId = _ScfMemoryModuleId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 10, 2, 1, 4),
    _ScfMemoryModuleId_Type()
)
scfMemoryModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMemoryModuleId.setStatus("current")
_ScfMemorySubType_Type = ScfComponentType
_ScfMemorySubType_Object = MibTableColumn
scfMemorySubType = _ScfMemorySubType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 10, 2, 1, 5),
    _ScfMemorySubType_Type()
)
scfMemorySubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMemorySubType.setStatus("current")
_ScfMemorySubId_Type = ScfIndex
_ScfMemorySubId_Object = MibTableColumn
scfMemorySubId = _ScfMemorySubId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 10, 2, 1, 6),
    _ScfMemorySubId_Type()
)
scfMemorySubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMemorySubId.setStatus("current")
_ScfMemoryName_Type = DisplayString
_ScfMemoryName_Object = MibTableColumn
scfMemoryName = _ScfMemoryName_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 10, 2, 1, 7),
    _ScfMemoryName_Type()
)
scfMemoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMemoryName.setStatus("current")
_ScfMemoryCapacity_Type = Integer32
_ScfMemoryCapacity_Object = MibTableColumn
scfMemoryCapacity = _ScfMemoryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 10, 2, 1, 8),
    _ScfMemoryCapacity_Type()
)
scfMemoryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMemoryCapacity.setStatus("current")
if mibBuilder.loadTexts:
    scfMemoryCapacity.setUnits("GB")
_ScfMemoryAdditionalInfo_Type = DisplayString
_ScfMemoryAdditionalInfo_Object = MibTableColumn
scfMemoryAdditionalInfo = _ScfMemoryAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 10, 2, 1, 9),
    _ScfMemoryAdditionalInfo_Type()
)
scfMemoryAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMemoryAdditionalInfo.setStatus("current")
_ScfMemoryState_Type = ScfStateTC
_ScfMemoryState_Object = MibTableColumn
scfMemoryState = _ScfMemoryState_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 10, 2, 1, 10),
    _ScfMemoryState_Type()
)
scfMemoryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfMemoryState.setStatus("current")
_ScfIoBoxInfo_ObjectIdentity = ObjectIdentity
scfIoBoxInfo = _ScfIoBoxInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11)
)
_ScfIoBoxNumber_Type = Integer32
_ScfIoBoxNumber_Object = MibScalar
scfIoBoxNumber = _ScfIoBoxNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 1),
    _ScfIoBoxNumber_Type()
)
scfIoBoxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoxNumber.setStatus("current")
_ScfIoBoxTable_Object = MibTable
scfIoBoxTable = _ScfIoBoxTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 2)
)
if mibBuilder.loadTexts:
    scfIoBoxTable.setStatus("current")
_ScfIoBoxEntry_Object = MibTableRow
scfIoBoxEntry = _ScfIoBoxEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 2, 1)
)
scfIoBoxEntry.setIndexNames(
    (0, "OPL-SP-MIB", "scfIoBoxId"),
)
if mibBuilder.loadTexts:
    scfIoBoxEntry.setStatus("current")
_ScfIoBoxId_Type = ScfIoBoxIndex
_ScfIoBoxId_Object = MibTableColumn
scfIoBoxId = _ScfIoBoxId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 2, 1, 1),
    _ScfIoBoxId_Type()
)
scfIoBoxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoxId.setStatus("current")
_ScfIoBoxLocationLED_Type = ScfIoBoxLEDState
_ScfIoBoxLocationLED_Object = MibTableColumn
scfIoBoxLocationLED = _ScfIoBoxLocationLED_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 2, 1, 2),
    _ScfIoBoxLocationLED_Type()
)
scfIoBoxLocationLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoxLocationLED.setStatus("current")
_ScfIoBoxOverTempLED_Type = ScfIoBoxLEDState
_ScfIoBoxOverTempLED_Object = MibTableColumn
scfIoBoxOverTempLED = _ScfIoBoxOverTempLED_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 2, 1, 3),
    _ScfIoBoxOverTempLED_Type()
)
scfIoBoxOverTempLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoxOverTempLED.setStatus("current")
_ScfIoBoxServiceReqLED_Type = ScfIoBoxLEDState
_ScfIoBoxServiceReqLED_Object = MibTableColumn
scfIoBoxServiceReqLED = _ScfIoBoxServiceReqLED_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 2, 1, 4),
    _ScfIoBoxServiceReqLED_Type()
)
scfIoBoxServiceReqLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoxServiceReqLED.setStatus("current")
_ScfIoBoxActiveLED_Type = ScfIoBoxLEDState
_ScfIoBoxActiveLED_Object = MibTableColumn
scfIoBoxActiveLED = _ScfIoBoxActiveLED_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 2, 1, 5),
    _ScfIoBoxActiveLED_Type()
)
scfIoBoxActiveLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoxActiveLED.setStatus("current")
_ScfIoBoxPartNumber_Type = DisplayString
_ScfIoBoxPartNumber_Object = MibTableColumn
scfIoBoxPartNumber = _ScfIoBoxPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 2, 1, 6),
    _ScfIoBoxPartNumber_Type()
)
scfIoBoxPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoxPartNumber.setStatus("current")
_ScfIoBoxSerialNumber_Type = DisplayString
_ScfIoBoxSerialNumber_Object = MibTableColumn
scfIoBoxSerialNumber = _ScfIoBoxSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 2, 1, 7),
    _ScfIoBoxSerialNumber_Type()
)
scfIoBoxSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoxSerialNumber.setStatus("current")
_ScfIoBoxDashLevel_Type = DisplayString
_ScfIoBoxDashLevel_Object = MibTableColumn
scfIoBoxDashLevel = _ScfIoBoxDashLevel_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 2, 1, 8),
    _ScfIoBoxDashLevel_Type()
)
scfIoBoxDashLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoxDashLevel.setStatus("current")
_ScfIoBoatNumber_Type = Integer32
_ScfIoBoatNumber_Object = MibScalar
scfIoBoatNumber = _ScfIoBoatNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 3),
    _ScfIoBoatNumber_Type()
)
scfIoBoatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoatNumber.setStatus("current")
_ScfIoBoatTable_Object = MibTable
scfIoBoatTable = _ScfIoBoatTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 4)
)
if mibBuilder.loadTexts:
    scfIoBoatTable.setStatus("current")
_ScfIoBoatEntry_Object = MibTableRow
scfIoBoatEntry = _ScfIoBoatEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 4, 1)
)
scfIoBoatEntry.setIndexNames(
    (0, "OPL-SP-MIB", "scfIoBoatIoBoxId"),
    (0, "OPL-SP-MIB", "scfIoBoatId"),
)
if mibBuilder.loadTexts:
    scfIoBoatEntry.setStatus("current")
_ScfIoBoatIoBoxId_Type = ScfIoBoxIndex
_ScfIoBoatIoBoxId_Object = MibTableColumn
scfIoBoatIoBoxId = _ScfIoBoatIoBoxId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 4, 1, 1),
    _ScfIoBoatIoBoxId_Type()
)
scfIoBoatIoBoxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoatIoBoxId.setStatus("current")
_ScfIoBoatId_Type = ScfIndex
_ScfIoBoatId_Object = MibTableColumn
scfIoBoatId = _ScfIoBoatId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 4, 1, 2),
    _ScfIoBoatId_Type()
)
scfIoBoatId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoatId.setStatus("current")
_ScfIoBoatLocation_Type = ScfIoBoxComponentLocation
_ScfIoBoatLocation_Object = MibTableColumn
scfIoBoatLocation = _ScfIoBoatLocation_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 4, 1, 3),
    _ScfIoBoatLocation_Type()
)
scfIoBoatLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoatLocation.setStatus("current")
_ScfIoBoatType_Type = ScfIoBoatTypeTC
_ScfIoBoatType_Object = MibTableColumn
scfIoBoatType = _ScfIoBoatType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 4, 1, 4),
    _ScfIoBoatType_Type()
)
scfIoBoatType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoatType.setStatus("current")
_ScfIoBoatOKtoRemoveLED_Type = ScfIoBoxLEDState
_ScfIoBoatOKtoRemoveLED_Object = MibTableColumn
scfIoBoatOKtoRemoveLED = _ScfIoBoatOKtoRemoveLED_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 4, 1, 5),
    _ScfIoBoatOKtoRemoveLED_Type()
)
scfIoBoatOKtoRemoveLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoatOKtoRemoveLED.setStatus("current")
_ScfIoBoatServiceReqLED_Type = ScfIoBoxLEDState
_ScfIoBoatServiceReqLED_Object = MibTableColumn
scfIoBoatServiceReqLED = _ScfIoBoatServiceReqLED_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 4, 1, 6),
    _ScfIoBoatServiceReqLED_Type()
)
scfIoBoatServiceReqLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoatServiceReqLED.setStatus("current")
_ScfIoBoatActiveLED_Type = ScfIoBoxLEDState
_ScfIoBoatActiveLED_Object = MibTableColumn
scfIoBoatActiveLED = _ScfIoBoatActiveLED_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 4, 1, 7),
    _ScfIoBoatActiveLED_Type()
)
scfIoBoatActiveLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoatActiveLED.setStatus("current")
_ScfIoBoatPartNumber_Type = DisplayString
_ScfIoBoatPartNumber_Object = MibTableColumn
scfIoBoatPartNumber = _ScfIoBoatPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 4, 1, 8),
    _ScfIoBoatPartNumber_Type()
)
scfIoBoatPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoatPartNumber.setStatus("current")
_ScfIoBoatSerialNumber_Type = DisplayString
_ScfIoBoatSerialNumber_Object = MibTableColumn
scfIoBoatSerialNumber = _ScfIoBoatSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 4, 1, 9),
    _ScfIoBoatSerialNumber_Type()
)
scfIoBoatSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoatSerialNumber.setStatus("current")
_ScfIoBoatDashLevel_Type = DisplayString
_ScfIoBoatDashLevel_Object = MibTableColumn
scfIoBoatDashLevel = _ScfIoBoatDashLevel_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 4, 1, 10),
    _ScfIoBoatDashLevel_Type()
)
scfIoBoatDashLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoatDashLevel.setStatus("current")
_ScfLinkCardNumber_Type = Integer32
_ScfLinkCardNumber_Object = MibScalar
scfLinkCardNumber = _ScfLinkCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 5),
    _ScfLinkCardNumber_Type()
)
scfLinkCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfLinkCardNumber.setStatus("current")
_ScfLinkCardTable_Object = MibTable
scfLinkCardTable = _ScfLinkCardTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 6)
)
if mibBuilder.loadTexts:
    scfLinkCardTable.setStatus("current")
_ScfLinkCardEntry_Object = MibTableRow
scfLinkCardEntry = _ScfLinkCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 6, 1)
)
scfLinkCardEntry.setIndexNames(
    (0, "OPL-SP-MIB", "scfLinkCardIoBoxId"),
    (0, "OPL-SP-MIB", "scfLinkCardIoBoatId"),
    (0, "OPL-SP-MIB", "scfLinkCardId"),
)
if mibBuilder.loadTexts:
    scfLinkCardEntry.setStatus("current")
_ScfLinkCardIoBoxId_Type = ScfIoBoxIndex
_ScfLinkCardIoBoxId_Object = MibTableColumn
scfLinkCardIoBoxId = _ScfLinkCardIoBoxId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 6, 1, 1),
    _ScfLinkCardIoBoxId_Type()
)
scfLinkCardIoBoxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfLinkCardIoBoxId.setStatus("current")
_ScfLinkCardIoBoatId_Type = ScfIndex
_ScfLinkCardIoBoatId_Object = MibTableColumn
scfLinkCardIoBoatId = _ScfLinkCardIoBoatId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 6, 1, 2),
    _ScfLinkCardIoBoatId_Type()
)
scfLinkCardIoBoatId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfLinkCardIoBoatId.setStatus("current")
_ScfLinkCardId_Type = ScfIndex
_ScfLinkCardId_Object = MibTableColumn
scfLinkCardId = _ScfLinkCardId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 6, 1, 3),
    _ScfLinkCardId_Type()
)
scfLinkCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfLinkCardId.setStatus("current")
_ScfLinkCardDataLED_Type = ScfIoBoxLEDState
_ScfLinkCardDataLED_Object = MibTableColumn
scfLinkCardDataLED = _ScfLinkCardDataLED_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 6, 1, 4),
    _ScfLinkCardDataLED_Type()
)
scfLinkCardDataLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfLinkCardDataLED.setStatus("current")
_ScfLinkCardMgmtLED_Type = ScfIoBoxLEDState
_ScfLinkCardMgmtLED_Object = MibTableColumn
scfLinkCardMgmtLED = _ScfLinkCardMgmtLED_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 6, 1, 5),
    _ScfLinkCardMgmtLED_Type()
)
scfLinkCardMgmtLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfLinkCardMgmtLED.setStatus("current")
_ScfLinkCardDownlinkCardLocation_Type = DisplayString
_ScfLinkCardDownlinkCardLocation_Object = MibTableColumn
scfLinkCardDownlinkCardLocation = _ScfLinkCardDownlinkCardLocation_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 6, 1, 6),
    _ScfLinkCardDownlinkCardLocation_Type()
)
scfLinkCardDownlinkCardLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfLinkCardDownlinkCardLocation.setStatus("current")
_ScfLinkCardDownlinkCardId_Type = Integer32
_ScfLinkCardDownlinkCardId_Object = MibTableColumn
scfLinkCardDownlinkCardId = _ScfLinkCardDownlinkCardId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 6, 1, 7),
    _ScfLinkCardDownlinkCardId_Type()
)
scfLinkCardDownlinkCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfLinkCardDownlinkCardId.setStatus("current")
_ScfLinkCardPartNumber_Type = DisplayString
_ScfLinkCardPartNumber_Object = MibTableColumn
scfLinkCardPartNumber = _ScfLinkCardPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 6, 1, 8),
    _ScfLinkCardPartNumber_Type()
)
scfLinkCardPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfLinkCardPartNumber.setStatus("current")
_ScfLinkCardSerialNumber_Type = DisplayString
_ScfLinkCardSerialNumber_Object = MibTableColumn
scfLinkCardSerialNumber = _ScfLinkCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 6, 1, 9),
    _ScfLinkCardSerialNumber_Type()
)
scfLinkCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfLinkCardSerialNumber.setStatus("current")
_ScfLinkCardDashLevel_Type = DisplayString
_ScfLinkCardDashLevel_Object = MibTableColumn
scfLinkCardDashLevel = _ScfLinkCardDashLevel_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 6, 1, 10),
    _ScfLinkCardDashLevel_Type()
)
scfLinkCardDashLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfLinkCardDashLevel.setStatus("current")
_ScfPowerSupplyFanNumber_Type = Integer32
_ScfPowerSupplyFanNumber_Object = MibScalar
scfPowerSupplyFanNumber = _ScfPowerSupplyFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 7),
    _ScfPowerSupplyFanNumber_Type()
)
scfPowerSupplyFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfPowerSupplyFanNumber.setStatus("current")
_ScfPowerSupplyFanTable_Object = MibTable
scfPowerSupplyFanTable = _ScfPowerSupplyFanTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 8)
)
if mibBuilder.loadTexts:
    scfPowerSupplyFanTable.setStatus("current")
_ScfPowerSupplyFanEntry_Object = MibTableRow
scfPowerSupplyFanEntry = _ScfPowerSupplyFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 8, 1)
)
scfPowerSupplyFanEntry.setIndexNames(
    (0, "OPL-SP-MIB", "scfPowerSupplyFanIoBoxId"),
    (0, "OPL-SP-MIB", "scfPowerSupplyFanId"),
)
if mibBuilder.loadTexts:
    scfPowerSupplyFanEntry.setStatus("current")
_ScfPowerSupplyFanIoBoxId_Type = ScfIoBoxIndex
_ScfPowerSupplyFanIoBoxId_Object = MibTableColumn
scfPowerSupplyFanIoBoxId = _ScfPowerSupplyFanIoBoxId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 8, 1, 1),
    _ScfPowerSupplyFanIoBoxId_Type()
)
scfPowerSupplyFanIoBoxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfPowerSupplyFanIoBoxId.setStatus("current")
_ScfPowerSupplyFanId_Type = ScfIndex
_ScfPowerSupplyFanId_Object = MibTableColumn
scfPowerSupplyFanId = _ScfPowerSupplyFanId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 8, 1, 2),
    _ScfPowerSupplyFanId_Type()
)
scfPowerSupplyFanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfPowerSupplyFanId.setStatus("current")
_ScfPowerSupplyFanLocation_Type = ScfIoBoxComponentLocation
_ScfPowerSupplyFanLocation_Object = MibTableColumn
scfPowerSupplyFanLocation = _ScfPowerSupplyFanLocation_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 8, 1, 3),
    _ScfPowerSupplyFanLocation_Type()
)
scfPowerSupplyFanLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfPowerSupplyFanLocation.setStatus("current")
_ScfPowerSupplyFanOKtoRemoveLED_Type = ScfIoBoxLEDState
_ScfPowerSupplyFanOKtoRemoveLED_Object = MibTableColumn
scfPowerSupplyFanOKtoRemoveLED = _ScfPowerSupplyFanOKtoRemoveLED_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 8, 1, 4),
    _ScfPowerSupplyFanOKtoRemoveLED_Type()
)
scfPowerSupplyFanOKtoRemoveLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfPowerSupplyFanOKtoRemoveLED.setStatus("current")
_ScfPowerSupplyFanServiceReqLED_Type = ScfIoBoxLEDState
_ScfPowerSupplyFanServiceReqLED_Object = MibTableColumn
scfPowerSupplyFanServiceReqLED = _ScfPowerSupplyFanServiceReqLED_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 8, 1, 5),
    _ScfPowerSupplyFanServiceReqLED_Type()
)
scfPowerSupplyFanServiceReqLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfPowerSupplyFanServiceReqLED.setStatus("current")
_ScfPowerSupplyFanACPowerLED_Type = ScfIoBoxLEDState
_ScfPowerSupplyFanACPowerLED_Object = MibTableColumn
scfPowerSupplyFanACPowerLED = _ScfPowerSupplyFanACPowerLED_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 8, 1, 6),
    _ScfPowerSupplyFanACPowerLED_Type()
)
scfPowerSupplyFanACPowerLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfPowerSupplyFanACPowerLED.setStatus("current")
_ScfPowerSupplyFanDCPowerLED_Type = ScfIoBoxLEDState
_ScfPowerSupplyFanDCPowerLED_Object = MibTableColumn
scfPowerSupplyFanDCPowerLED = _ScfPowerSupplyFanDCPowerLED_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 8, 1, 7),
    _ScfPowerSupplyFanDCPowerLED_Type()
)
scfPowerSupplyFanDCPowerLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfPowerSupplyFanDCPowerLED.setStatus("current")
_ScfPowerSupplyFanPartNumber_Type = DisplayString
_ScfPowerSupplyFanPartNumber_Object = MibTableColumn
scfPowerSupplyFanPartNumber = _ScfPowerSupplyFanPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 8, 1, 8),
    _ScfPowerSupplyFanPartNumber_Type()
)
scfPowerSupplyFanPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfPowerSupplyFanPartNumber.setStatus("current")
_ScfPowerSupplyFanSerialNumber_Type = DisplayString
_ScfPowerSupplyFanSerialNumber_Object = MibTableColumn
scfPowerSupplyFanSerialNumber = _ScfPowerSupplyFanSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 8, 1, 9),
    _ScfPowerSupplyFanSerialNumber_Type()
)
scfPowerSupplyFanSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfPowerSupplyFanSerialNumber.setStatus("current")
_ScfPowerSupplyFanDashLevel_Type = DisplayString
_ScfPowerSupplyFanDashLevel_Object = MibTableColumn
scfPowerSupplyFanDashLevel = _ScfPowerSupplyFanDashLevel_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 8, 1, 10),
    _ScfPowerSupplyFanDashLevel_Type()
)
scfPowerSupplyFanDashLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfPowerSupplyFanDashLevel.setStatus("current")
_ScfIoBoxSensorNumber_Type = Integer32
_ScfIoBoxSensorNumber_Object = MibScalar
scfIoBoxSensorNumber = _ScfIoBoxSensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 9),
    _ScfIoBoxSensorNumber_Type()
)
scfIoBoxSensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoxSensorNumber.setStatus("current")
_ScfIoBoxSensorTable_Object = MibTable
scfIoBoxSensorTable = _ScfIoBoxSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 10)
)
if mibBuilder.loadTexts:
    scfIoBoxSensorTable.setStatus("current")
_ScfIoBoxSensorEntry_Object = MibTableRow
scfIoBoxSensorEntry = _ScfIoBoxSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 10, 1)
)
scfIoBoxSensorEntry.setIndexNames(
    (0, "OPL-SP-MIB", "scfIoBoxSensorIoBoxId"),
    (0, "OPL-SP-MIB", "scfIoBoxSensorIoBoxSubType"),
    (0, "OPL-SP-MIB", "scfIoBoxSensorIoBoxSubId"),
    (0, "OPL-SP-MIB", "scfIoBoxSensorId"),
)
if mibBuilder.loadTexts:
    scfIoBoxSensorEntry.setStatus("current")
_ScfIoBoxSensorIoBoxId_Type = ScfIoBoxIndex
_ScfIoBoxSensorIoBoxId_Object = MibTableColumn
scfIoBoxSensorIoBoxId = _ScfIoBoxSensorIoBoxId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 10, 1, 1),
    _ScfIoBoxSensorIoBoxId_Type()
)
scfIoBoxSensorIoBoxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoxSensorIoBoxId.setStatus("current")
_ScfIoBoxSensorIoBoxSubType_Type = ScfIoBoxComponentType
_ScfIoBoxSensorIoBoxSubType_Object = MibTableColumn
scfIoBoxSensorIoBoxSubType = _ScfIoBoxSensorIoBoxSubType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 10, 1, 2),
    _ScfIoBoxSensorIoBoxSubType_Type()
)
scfIoBoxSensorIoBoxSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoxSensorIoBoxSubType.setStatus("current")
_ScfIoBoxSensorIoBoxSubId_Type = ScfIndex
_ScfIoBoxSensorIoBoxSubId_Object = MibTableColumn
scfIoBoxSensorIoBoxSubId = _ScfIoBoxSensorIoBoxSubId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 10, 1, 3),
    _ScfIoBoxSensorIoBoxSubId_Type()
)
scfIoBoxSensorIoBoxSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoxSensorIoBoxSubId.setStatus("current")
_ScfIoBoxSensorId_Type = ScfIndex
_ScfIoBoxSensorId_Object = MibTableColumn
scfIoBoxSensorId = _ScfIoBoxSensorId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 10, 1, 4),
    _ScfIoBoxSensorId_Type()
)
scfIoBoxSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoxSensorId.setStatus("current")
_ScfIoBoxSensorDescription_Type = DisplayString
_ScfIoBoxSensorDescription_Object = MibTableColumn
scfIoBoxSensorDescription = _ScfIoBoxSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 10, 1, 5),
    _ScfIoBoxSensorDescription_Type()
)
scfIoBoxSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoxSensorDescription.setStatus("current")
_ScfIoBoxSensorUnits_Type = DisplayString
_ScfIoBoxSensorUnits_Object = MibTableColumn
scfIoBoxSensorUnits = _ScfIoBoxSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 10, 1, 6),
    _ScfIoBoxSensorUnits_Type()
)
scfIoBoxSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoxSensorUnits.setStatus("current")
_ScfIoBoxSensorValue_Type = Integer32
_ScfIoBoxSensorValue_Object = MibTableColumn
scfIoBoxSensorValue = _ScfIoBoxSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 10, 1, 7),
    _ScfIoBoxSensorValue_Type()
)
scfIoBoxSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoxSensorValue.setStatus("current")
_ScfIoBoxSensorEnabledAlarms_Type = ScfIoBoxEnabledAlarms
_ScfIoBoxSensorEnabledAlarms_Object = MibTableColumn
scfIoBoxSensorEnabledAlarms = _ScfIoBoxSensorEnabledAlarms_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 10, 1, 8),
    _ScfIoBoxSensorEnabledAlarms_Type()
)
scfIoBoxSensorEnabledAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoxSensorEnabledAlarms.setStatus("current")
_ScfIoBoxSensorMinAlarm_Type = Integer32
_ScfIoBoxSensorMinAlarm_Object = MibTableColumn
scfIoBoxSensorMinAlarm = _ScfIoBoxSensorMinAlarm_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 10, 1, 9),
    _ScfIoBoxSensorMinAlarm_Type()
)
scfIoBoxSensorMinAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoxSensorMinAlarm.setStatus("current")
_ScfIoBoxSensorMaxAlarm_Type = Integer32
_ScfIoBoxSensorMaxAlarm_Object = MibTableColumn
scfIoBoxSensorMaxAlarm = _ScfIoBoxSensorMaxAlarm_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 11, 10, 1, 10),
    _ScfIoBoxSensorMaxAlarm_Type()
)
scfIoBoxSensorMaxAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfIoBoxSensorMaxAlarm.setStatus("current")
_ScfComponentInfo_ObjectIdentity = ObjectIdentity
scfComponentInfo = _ScfComponentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 12)
)
_ScfComponentNumber_Type = Integer32
_ScfComponentNumber_Object = MibScalar
scfComponentNumber = _ScfComponentNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 12, 1),
    _ScfComponentNumber_Type()
)
scfComponentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfComponentNumber.setStatus("current")
_ScfComponentTable_Object = MibTable
scfComponentTable = _ScfComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 12, 2)
)
if mibBuilder.loadTexts:
    scfComponentTable.setStatus("current")
_ScfComponentEntry_Object = MibTableRow
scfComponentEntry = _ScfComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 12, 2, 1)
)
scfComponentEntry.setIndexNames(
    (0, "OPL-SP-MIB", "scfComponentBoardType"),
    (0, "OPL-SP-MIB", "scfComponentBoardId"),
    (0, "OPL-SP-MIB", "scfComponentModuleType"),
    (0, "OPL-SP-MIB", "scfComponentModuleId"),
    (0, "OPL-SP-MIB", "scfComponentSubType"),
    (0, "OPL-SP-MIB", "scfComponentSubId"),
)
if mibBuilder.loadTexts:
    scfComponentEntry.setStatus("current")
_ScfComponentBoardType_Type = ScfComponentType
_ScfComponentBoardType_Object = MibTableColumn
scfComponentBoardType = _ScfComponentBoardType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 12, 2, 1, 1),
    _ScfComponentBoardType_Type()
)
scfComponentBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfComponentBoardType.setStatus("current")
_ScfComponentBoardId_Type = ScfIndex
_ScfComponentBoardId_Object = MibTableColumn
scfComponentBoardId = _ScfComponentBoardId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 12, 2, 1, 2),
    _ScfComponentBoardId_Type()
)
scfComponentBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfComponentBoardId.setStatus("current")
_ScfComponentModuleType_Type = ScfComponentType
_ScfComponentModuleType_Object = MibTableColumn
scfComponentModuleType = _ScfComponentModuleType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 12, 2, 1, 3),
    _ScfComponentModuleType_Type()
)
scfComponentModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfComponentModuleType.setStatus("current")
_ScfComponentModuleId_Type = ScfIndex
_ScfComponentModuleId_Object = MibTableColumn
scfComponentModuleId = _ScfComponentModuleId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 12, 2, 1, 4),
    _ScfComponentModuleId_Type()
)
scfComponentModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfComponentModuleId.setStatus("current")
_ScfComponentSubType_Type = ScfComponentType
_ScfComponentSubType_Object = MibTableColumn
scfComponentSubType = _ScfComponentSubType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 12, 2, 1, 5),
    _ScfComponentSubType_Type()
)
scfComponentSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfComponentSubType.setStatus("current")
_ScfComponentSubId_Type = ScfIndex
_ScfComponentSubId_Object = MibTableColumn
scfComponentSubId = _ScfComponentSubId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 12, 2, 1, 6),
    _ScfComponentSubId_Type()
)
scfComponentSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfComponentSubId.setStatus("current")
_ScfComponentAdditionalInfo_Type = DisplayString
_ScfComponentAdditionalInfo_Object = MibTableColumn
scfComponentAdditionalInfo = _ScfComponentAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 12, 2, 1, 7),
    _ScfComponentAdditionalInfo_Type()
)
scfComponentAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfComponentAdditionalInfo.setStatus("current")
_ScfComponentPartNumber_Type = DisplayString
_ScfComponentPartNumber_Object = MibTableColumn
scfComponentPartNumber = _ScfComponentPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 12, 2, 1, 8),
    _ScfComponentPartNumber_Type()
)
scfComponentPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfComponentPartNumber.setStatus("current")
_ScfComponentSerialNumber_Type = DisplayString
_ScfComponentSerialNumber_Object = MibTableColumn
scfComponentSerialNumber = _ScfComponentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 12, 2, 1, 9),
    _ScfComponentSerialNumber_Type()
)
scfComponentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfComponentSerialNumber.setStatus("current")
_ScfComponentProductName_Type = DisplayString
_ScfComponentProductName_Object = MibTableColumn
scfComponentProductName = _ScfComponentProductName_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 12, 2, 1, 10),
    _ScfComponentProductName_Type()
)
scfComponentProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfComponentProductName.setStatus("current")
_ScfComponentManufacturer_Type = DisplayString
_ScfComponentManufacturer_Object = MibTableColumn
scfComponentManufacturer = _ScfComponentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 12, 2, 1, 11),
    _ScfComponentManufacturer_Type()
)
scfComponentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfComponentManufacturer.setStatus("current")
_ScfComponentManufactureDate_Type = DisplayString
_ScfComponentManufactureDate_Object = MibTableColumn
scfComponentManufactureDate = _ScfComponentManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 12, 2, 1, 12),
    _ScfComponentManufactureDate_Type()
)
scfComponentManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfComponentManufactureDate.setStatus("current")
_ScfComponentStatus_Type = ScfStateTC
_ScfComponentStatus_Object = MibTableColumn
scfComponentStatus = _ScfComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 12, 2, 1, 13),
    _ScfComponentStatus_Type()
)
scfComponentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfComponentStatus.setStatus("current")
_ScfComponentErrorStatus_Type = ScfErrorStatus
_ScfComponentErrorStatus_Object = MibTableColumn
scfComponentErrorStatus = _ScfComponentErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 1, 12, 2, 1, 14),
    _ScfComponentErrorStatus_Type()
)
scfComponentErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scfComponentErrorStatus.setStatus("current")
_ScfMIBTraps_ObjectIdentity = ObjectIdentity
scfMIBTraps = _ScfMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2)
)
_ScfMIBTrapPrefix_ObjectIdentity = ObjectIdentity
scfMIBTrapPrefix = _ScfMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2, 0)
)
_ScfMIBTrapData_ObjectIdentity = ObjectIdentity
scfMIBTrapData = _ScfMIBTrapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2, 1)
)
_ScfTrapEventType_Type = ScfTrapEventTypeTC
_ScfTrapEventType_Object = MibScalar
scfTrapEventType = _ScfTrapEventType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2, 1, 1),
    _ScfTrapEventType_Type()
)
scfTrapEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    scfTrapEventType.setStatus("current")
_ScfTrapStatusEventType_Type = ScfTrapStatusEventTypeTC
_ScfTrapStatusEventType_Object = MibScalar
scfTrapStatusEventType = _ScfTrapStatusEventType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2, 1, 2),
    _ScfTrapStatusEventType_Type()
)
scfTrapStatusEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    scfTrapStatusEventType.setStatus("current")
_ScfTrapDomainStatusAlarmType_Type = ScfDomainStatusAlarmType
_ScfTrapDomainStatusAlarmType_Object = MibScalar
scfTrapDomainStatusAlarmType = _ScfTrapDomainStatusAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2, 1, 3),
    _ScfTrapDomainStatusAlarmType_Type()
)
scfTrapDomainStatusAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    scfTrapDomainStatusAlarmType.setStatus("current")
_ScfTrapIoBoxId_Type = ScfIoBoxIndex
_ScfTrapIoBoxId_Object = MibScalar
scfTrapIoBoxId = _ScfTrapIoBoxId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2, 1, 4),
    _ScfTrapIoBoxId_Type()
)
scfTrapIoBoxId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    scfTrapIoBoxId.setStatus("current")
_ScfTrapIoBoxSubType_Type = ScfIoBoxComponentType
_ScfTrapIoBoxSubType_Object = MibScalar
scfTrapIoBoxSubType = _ScfTrapIoBoxSubType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2, 1, 5),
    _ScfTrapIoBoxSubType_Type()
)
scfTrapIoBoxSubType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    scfTrapIoBoxSubType.setStatus("current")
_ScfTrapIoBoxSubId_Type = ScfIndex
_ScfTrapIoBoxSubId_Object = MibScalar
scfTrapIoBoxSubId = _ScfTrapIoBoxSubId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2, 1, 6),
    _ScfTrapIoBoxSubId_Type()
)
scfTrapIoBoxSubId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    scfTrapIoBoxSubId.setStatus("current")
_ScfTrapIoBoxTempEventType_Type = ScfTrapIoBoxTempEventTypeTC
_ScfTrapIoBoxTempEventType_Object = MibScalar
scfTrapIoBoxTempEventType = _ScfTrapIoBoxTempEventType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2, 1, 7),
    _ScfTrapIoBoxTempEventType_Type()
)
scfTrapIoBoxTempEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    scfTrapIoBoxTempEventType.setStatus("current")
_ScfTrapIoBoxLedType_Type = ScfIoBoxLEDType
_ScfTrapIoBoxLedType_Object = MibScalar
scfTrapIoBoxLedType = _ScfTrapIoBoxLedType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2, 1, 8),
    _ScfTrapIoBoxLedType_Type()
)
scfTrapIoBoxLedType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    scfTrapIoBoxLedType.setStatus("current")
_ScfTrapIoBoxLedValue_Type = ScfIoBoxLEDState
_ScfTrapIoBoxLedValue_Object = MibScalar
scfTrapIoBoxLedValue = _ScfTrapIoBoxLedValue_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2, 1, 9),
    _ScfTrapIoBoxLedValue_Type()
)
scfTrapIoBoxLedValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    scfTrapIoBoxLedValue.setStatus("current")
_ScfTrapModeSwitchEventType_Type = ScfTrapModeSwitchEventTypeTC
_ScfTrapModeSwitchEventType_Object = MibScalar
scfTrapModeSwitchEventType = _ScfTrapModeSwitchEventType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2, 1, 10),
    _ScfTrapModeSwitchEventType_Type()
)
scfTrapModeSwitchEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    scfTrapModeSwitchEventType.setStatus("current")
_ScfMIBConformances_ObjectIdentity = ObjectIdentity
scfMIBConformances = _ScfMIBConformances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3)
)
_ScfMIBCompliances_ObjectIdentity = ObjectIdentity
scfMIBCompliances = _ScfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 1)
)
_ScfMIBGroups_ObjectIdentity = ObjectIdentity
scfMIBGroups = _ScfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 2)
)
_ScfMIBObjectGroups_ObjectIdentity = ObjectIdentity
scfMIBObjectGroups = _ScfMIBObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 2, 1)
)
_ScfMIBNotifGroups_ObjectIdentity = ObjectIdentity
scfMIBNotifGroups = _ScfMIBNotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 2, 2)
)

# Managed Objects groups

scfInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 2, 1, 1)
)
scfInfoGroup.setObjects(
      *(("OPL-SP-MIB", "scfAgentId"),
        ("OPL-SP-MIB", "scfAgentNumber"),
        ("OPL-SP-MIB", "scfAgentIndex"),
        ("OPL-SP-MIB", "scfXcpVersion"),
        ("OPL-SP-MIB", "scfIpAddressPortNumber"),
        ("OPL-SP-MIB", "scfIpAddressNumber"),
        ("OPL-SP-MIB", "scfIpAddressIndex"),
        ("OPL-SP-MIB", "scfIpAddress"))
)
if mibBuilder.loadTexts:
    scfInfoGroup.setStatus("current")

scfStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 2, 1, 2)
)
scfStateGroup.setObjects(
      *(("OPL-SP-MIB", "scfSystemState"),
        ("OPL-SP-MIB", "scfFirmwareState"),
        ("OPL-SP-MIB", "scfHardwareState"),
        ("OPL-SP-MIB", "scfModeSwitch"))
)
if mibBuilder.loadTexts:
    scfStateGroup.setStatus("current")

scfMonitorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 2, 1, 3)
)
scfMonitorInfoGroup.setObjects(
      *(("OPL-SP-MIB", "scfMonitorNumber"),
        ("OPL-SP-MIB", "scfMonitorType"),
        ("OPL-SP-MIB", "scfMonitorBoardType"),
        ("OPL-SP-MIB", "scfMonitorBoardId"),
        ("OPL-SP-MIB", "scfMonitorModuleType"),
        ("OPL-SP-MIB", "scfMonitorModuleId"),
        ("OPL-SP-MIB", "scfMonitorId"),
        ("OPL-SP-MIB", "scfMonitorDescription"),
        ("OPL-SP-MIB", "scfMonitorAdditionalInfo"),
        ("OPL-SP-MIB", "scfMonitorUnits"),
        ("OPL-SP-MIB", "scfMonitorStatus"),
        ("OPL-SP-MIB", "scfMonitorValue"),
        ("OPL-SP-MIB", "scfMonitorValueStatus"))
)
if mibBuilder.loadTexts:
    scfMonitorInfoGroup.setStatus("current")

scfSystemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 2, 1, 4)
)
scfSystemInfoGroup.setObjects(
      *(("OPL-SP-MIB", "scfSystemName"),
        ("OPL-SP-MIB", "scfSystemType"),
        ("OPL-SP-MIB", "scfSystemSerialNumber"),
        ("OPL-SP-MIB", "scfSystemAdditionalInfo"),
        ("OPL-SP-MIB", "scfSystemCpuNumber"),
        ("OPL-SP-MIB", "scfSystemMemoryCapacity"),
        ("OPL-SP-MIB", "scfSystemReadyLED"),
        ("OPL-SP-MIB", "scfSystemPowerLED"),
        ("OPL-SP-MIB", "scfSystemCheckLED"))
)
if mibBuilder.loadTexts:
    scfSystemInfoGroup.setStatus("current")

scfDomainInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 2, 1, 5)
)
scfDomainInfoGroup.setObjects(
      *(("OPL-SP-MIB", "scfDomainNumber"),
        ("OPL-SP-MIB", "scfDomainId"),
        ("OPL-SP-MIB", "scfDomainCpuNumber"),
        ("OPL-SP-MIB", "scfDomainMemoryCapacity"),
        ("OPL-SP-MIB", "scfDomainObpVersion"),
        ("OPL-SP-MIB", "scfDomainObpAdditionalInfo"),
        ("OPL-SP-MIB", "scfDomainOsMachine"),
        ("OPL-SP-MIB", "scfDomainOsRelease"),
        ("OPL-SP-MIB", "scfDomainOsSysName"),
        ("OPL-SP-MIB", "scfDomainOsNodeName"),
        ("OPL-SP-MIB", "scfDomainOsVersion"),
        ("OPL-SP-MIB", "scfDomainOsAdditionalInfo"),
        ("OPL-SP-MIB", "scfDomainValid"),
        ("OPL-SP-MIB", "scfDomainXsbs"),
        ("OPL-SP-MIB", "scfDomainStatus"),
        ("OPL-SP-MIB", "scfDomainErrorStatus"),
        ("OPL-SP-MIB", "scfDomainConfigurationPolicy"))
)
if mibBuilder.loadTexts:
    scfDomainInfoGroup.setStatus("current")

scfXsbInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 2, 1, 6)
)
scfXsbInfoGroup.setObjects(
      *(("OPL-SP-MIB", "scfXsbType"),
        ("OPL-SP-MIB", "scfXsbNumber"),
        ("OPL-SP-MIB", "scfXsbId"),
        ("OPL-SP-MIB", "scfXsbStatus"),
        ("OPL-SP-MIB", "scfXsbErrorStatus"),
        ("OPL-SP-MIB", "scfXsbDomainId"),
        ("OPL-SP-MIB", "scfXsbDrStatus"),
        ("OPL-SP-MIB", "scfXsbSubStatusPower"),
        ("OPL-SP-MIB", "scfXsbSubStatusTest"),
        ("OPL-SP-MIB", "scfXsbSubStatusAssignment"),
        ("OPL-SP-MIB", "scfXsbSubStatusConnectivity"),
        ("OPL-SP-MIB", "scfXsbSubStatusConfiguration"),
        ("OPL-SP-MIB", "scfXsbSetupDID"),
        ("OPL-SP-MIB", "scfXsbNextDID"))
)
if mibBuilder.loadTexts:
    scfXsbInfoGroup.setStatus("current")

scfLsbInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 2, 1, 7)
)
scfLsbInfoGroup.setObjects(
      *(("OPL-SP-MIB", "scfLsbType"),
        ("OPL-SP-MIB", "scfLsbNumber"),
        ("OPL-SP-MIB", "scfLsbDomainId"),
        ("OPL-SP-MIB", "scfLsbId"),
        ("OPL-SP-MIB", "scfLsbXsbId"),
        ("OPL-SP-MIB", "scfLsbNoMem"),
        ("OPL-SP-MIB", "scfLsbNoIo"),
        ("OPL-SP-MIB", "scfLsbFloatingBoard"))
)
if mibBuilder.loadTexts:
    scfLsbInfoGroup.setStatus("current")

scfBoardInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 2, 1, 8)
)
scfBoardInfoGroup.setObjects(
      *(("OPL-SP-MIB", "scfBoardNumber"),
        ("OPL-SP-MIB", "scfBoardType"),
        ("OPL-SP-MIB", "scfBoardId"),
        ("OPL-SP-MIB", "scfBoardName"),
        ("OPL-SP-MIB", "scfBoardAdditionalInfo"),
        ("OPL-SP-MIB", "scfBoardXsbs"),
        ("OPL-SP-MIB", "scfBoardState"),
        ("OPL-SP-MIB", "scfBoardCODEnabled"),
        ("OPL-SP-MIB", "scfBoardSubType"))
)
if mibBuilder.loadTexts:
    scfBoardInfoGroup.setStatus("current")

scfCpuInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 2, 1, 9)
)
scfCpuInfoGroup.setObjects(
      *(("OPL-SP-MIB", "scfCpuNumber"),
        ("OPL-SP-MIB", "scfCpuBoardType"),
        ("OPL-SP-MIB", "scfCpuBoardId"),
        ("OPL-SP-MIB", "scfCpuModuleType"),
        ("OPL-SP-MIB", "scfCpuModuleId"),
        ("OPL-SP-MIB", "scfCpuSubType"),
        ("OPL-SP-MIB", "scfCpuSubId"),
        ("OPL-SP-MIB", "scfCpuType"),
        ("OPL-SP-MIB", "scfCpuFrequency"),
        ("OPL-SP-MIB", "scfCpuAdditionalInfo"),
        ("OPL-SP-MIB", "scfCpuState"))
)
if mibBuilder.loadTexts:
    scfCpuInfoGroup.setStatus("current")

scfMemoryInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 2, 1, 10)
)
scfMemoryInfoGroup.setObjects(
      *(("OPL-SP-MIB", "scfMemoryNumber"),
        ("OPL-SP-MIB", "scfMemoryBoardType"),
        ("OPL-SP-MIB", "scfMemoryBoardId"),
        ("OPL-SP-MIB", "scfMemoryModuleType"),
        ("OPL-SP-MIB", "scfMemoryModuleId"),
        ("OPL-SP-MIB", "scfMemorySubType"),
        ("OPL-SP-MIB", "scfMemorySubId"),
        ("OPL-SP-MIB", "scfMemoryName"),
        ("OPL-SP-MIB", "scfMemoryCapacity"),
        ("OPL-SP-MIB", "scfMemoryAdditionalInfo"),
        ("OPL-SP-MIB", "scfMemoryState"))
)
if mibBuilder.loadTexts:
    scfMemoryInfoGroup.setStatus("current")

scfIoBoxInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 2, 1, 11)
)
scfIoBoxInfoGroup.setObjects(
      *(("OPL-SP-MIB", "scfIoBoxNumber"),
        ("OPL-SP-MIB", "scfIoBoxId"),
        ("OPL-SP-MIB", "scfIoBoxLocationLED"),
        ("OPL-SP-MIB", "scfIoBoxOverTempLED"),
        ("OPL-SP-MIB", "scfIoBoxServiceReqLED"),
        ("OPL-SP-MIB", "scfIoBoxActiveLED"),
        ("OPL-SP-MIB", "scfIoBoxPartNumber"),
        ("OPL-SP-MIB", "scfIoBoxSerialNumber"),
        ("OPL-SP-MIB", "scfIoBoxDashLevel"),
        ("OPL-SP-MIB", "scfIoBoatNumber"),
        ("OPL-SP-MIB", "scfIoBoatIoBoxId"),
        ("OPL-SP-MIB", "scfIoBoatId"),
        ("OPL-SP-MIB", "scfIoBoatLocation"),
        ("OPL-SP-MIB", "scfIoBoatType"),
        ("OPL-SP-MIB", "scfIoBoatOKtoRemoveLED"),
        ("OPL-SP-MIB", "scfIoBoatServiceReqLED"),
        ("OPL-SP-MIB", "scfIoBoatActiveLED"),
        ("OPL-SP-MIB", "scfIoBoatPartNumber"),
        ("OPL-SP-MIB", "scfIoBoatSerialNumber"),
        ("OPL-SP-MIB", "scfIoBoatDashLevel"),
        ("OPL-SP-MIB", "scfLinkCardNumber"),
        ("OPL-SP-MIB", "scfLinkCardIoBoxId"),
        ("OPL-SP-MIB", "scfLinkCardIoBoatId"),
        ("OPL-SP-MIB", "scfLinkCardId"),
        ("OPL-SP-MIB", "scfLinkCardDataLED"),
        ("OPL-SP-MIB", "scfLinkCardMgmtLED"),
        ("OPL-SP-MIB", "scfLinkCardDownlinkCardLocation"),
        ("OPL-SP-MIB", "scfLinkCardDownlinkCardId"),
        ("OPL-SP-MIB", "scfLinkCardPartNumber"),
        ("OPL-SP-MIB", "scfLinkCardSerialNumber"),
        ("OPL-SP-MIB", "scfLinkCardDashLevel"),
        ("OPL-SP-MIB", "scfPowerSupplyFanNumber"),
        ("OPL-SP-MIB", "scfPowerSupplyFanIoBoxId"),
        ("OPL-SP-MIB", "scfPowerSupplyFanId"),
        ("OPL-SP-MIB", "scfPowerSupplyFanLocation"),
        ("OPL-SP-MIB", "scfPowerSupplyFanOKtoRemoveLED"),
        ("OPL-SP-MIB", "scfPowerSupplyFanServiceReqLED"),
        ("OPL-SP-MIB", "scfPowerSupplyFanACPowerLED"),
        ("OPL-SP-MIB", "scfPowerSupplyFanDCPowerLED"),
        ("OPL-SP-MIB", "scfPowerSupplyFanPartNumber"),
        ("OPL-SP-MIB", "scfPowerSupplyFanSerialNumber"),
        ("OPL-SP-MIB", "scfPowerSupplyFanDashLevel"),
        ("OPL-SP-MIB", "scfIoBoxSensorNumber"),
        ("OPL-SP-MIB", "scfIoBoxSensorIoBoxId"),
        ("OPL-SP-MIB", "scfIoBoxSensorIoBoxSubType"),
        ("OPL-SP-MIB", "scfIoBoxSensorIoBoxSubId"),
        ("OPL-SP-MIB", "scfIoBoxSensorId"),
        ("OPL-SP-MIB", "scfIoBoxSensorDescription"),
        ("OPL-SP-MIB", "scfIoBoxSensorUnits"),
        ("OPL-SP-MIB", "scfIoBoxSensorValue"),
        ("OPL-SP-MIB", "scfIoBoxSensorEnabledAlarms"),
        ("OPL-SP-MIB", "scfIoBoxSensorMinAlarm"),
        ("OPL-SP-MIB", "scfIoBoxSensorMaxAlarm"))
)
if mibBuilder.loadTexts:
    scfIoBoxInfoGroup.setStatus("current")

scfComponentInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 2, 1, 12)
)
scfComponentInfoGroup.setObjects(
      *(("OPL-SP-MIB", "scfComponentNumber"),
        ("OPL-SP-MIB", "scfComponentBoardType"),
        ("OPL-SP-MIB", "scfComponentBoardId"),
        ("OPL-SP-MIB", "scfComponentModuleType"),
        ("OPL-SP-MIB", "scfComponentModuleId"),
        ("OPL-SP-MIB", "scfComponentSubType"),
        ("OPL-SP-MIB", "scfComponentSubId"),
        ("OPL-SP-MIB", "scfComponentAdditionalInfo"),
        ("OPL-SP-MIB", "scfComponentPartNumber"),
        ("OPL-SP-MIB", "scfComponentSerialNumber"),
        ("OPL-SP-MIB", "scfComponentProductName"),
        ("OPL-SP-MIB", "scfComponentManufacturer"),
        ("OPL-SP-MIB", "scfComponentManufactureDate"),
        ("OPL-SP-MIB", "scfComponentStatus"),
        ("OPL-SP-MIB", "scfComponentErrorStatus"))
)
if mibBuilder.loadTexts:
    scfComponentInfoGroup.setStatus("current")

scfNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 2, 1, 13)
)
scfNotificationObjectGroup.setObjects(
      *(("OPL-SP-MIB", "scfTrapEventType"),
        ("OPL-SP-MIB", "scfTrapStatusEventType"),
        ("OPL-SP-MIB", "scfTrapDomainStatusAlarmType"),
        ("OPL-SP-MIB", "scfTrapIoBoxId"),
        ("OPL-SP-MIB", "scfTrapIoBoxSubType"),
        ("OPL-SP-MIB", "scfTrapIoBoxSubId"),
        ("OPL-SP-MIB", "scfTrapIoBoxTempEventType"),
        ("OPL-SP-MIB", "scfTrapIoBoxLedType"),
        ("OPL-SP-MIB", "scfTrapIoBoxLedValue"),
        ("OPL-SP-MIB", "scfTrapModeSwitchEventType"))
)
if mibBuilder.loadTexts:
    scfNotificationObjectGroup.setStatus("current")

scfSystemActualPowerConsumptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 2, 1, 14)
)
scfSystemActualPowerConsumptionGroup.setObjects(
      *(("OPL-SP-MIB", "scfSystemActualPowerConsumptionValue"),
        ("OPL-SP-MIB", "scfSystemActualPowerConsumptionUnit"),
        ("OPL-SP-MIB", "scfSystemActualPowerMinPollingInterval"))
)
if mibBuilder.loadTexts:
    scfSystemActualPowerConsumptionGroup.setStatus("current")

scfSystemAmbientTemperatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 2, 1, 15)
)
scfSystemAmbientTemperatureGroup.setObjects(
      *(("OPL-SP-MIB", "scfSystemAmbientTemperatureValue"),
        ("OPL-SP-MIB", "scfSystemAmbientTemperatureUnit"),
        ("OPL-SP-MIB", "scfSystemAmbientTemperatureMinPollingInterval"))
)
if mibBuilder.loadTexts:
    scfSystemAmbientTemperatureGroup.setStatus("current")

scfSystemPermittedPowerConsumptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 2, 1, 16)
)
scfSystemPermittedPowerConsumptionGroup.setObjects(
      *(("OPL-SP-MIB", "scfSystemPermittedPowerConsumptionValue"),
        ("OPL-SP-MIB", "scfSystemPermittedPowerConsumptionUnit"))
)
if mibBuilder.loadTexts:
    scfSystemPermittedPowerConsumptionGroup.setStatus("current")

scfSystemAirFlowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 2, 1, 17)
)
scfSystemAirFlowGroup.setObjects(
      *(("OPL-SP-MIB", "scfSystemExhaustAirFlowValue"),
        ("OPL-SP-MIB", "scfSystemExhaustAirFlowUnit"),
        ("OPL-SP-MIB", "scfSystemExhaustAirFlowMinPollingInterval"))
)
if mibBuilder.loadTexts:
    scfSystemAirFlowGroup.setStatus("current")


# Notification objects

scfSPFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2, 0, 1)
)
scfSPFailover.setObjects(
    ("OPL-SP-MIB", "scfAgentIndex")
)
if mibBuilder.loadTexts:
    scfSPFailover.setStatus(
        "current"
    )

scfComponentEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2, 0, 2)
)
scfComponentEvent.setObjects(
      *(("OPL-SP-MIB", "scfComponentSerialNumber"),
        ("OPL-SP-MIB", "scfTrapEventType"))
)
if mibBuilder.loadTexts:
    scfComponentEvent.setStatus(
        "current"
    )

scfComponentStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2, 0, 3)
)
scfComponentStatusEvent.setObjects(
      *(("OPL-SP-MIB", "scfComponentStatus"),
        ("OPL-SP-MIB", "scfTrapStatusEventType"))
)
if mibBuilder.loadTexts:
    scfComponentStatusEvent.setStatus(
        "current"
    )

scfXsbModeChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2, 0, 4)
)
scfXsbModeChangeEvent.setObjects(
    ("OPL-SP-MIB", "scfBoardXsbs")
)
if mibBuilder.loadTexts:
    scfXsbModeChangeEvent.setStatus(
        "current"
    )

scfDomainStatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2, 0, 5)
)
scfDomainStatusAlarm.setObjects(
      *(("OPL-SP-MIB", "scfDomainStatus"),
        ("OPL-SP-MIB", "scfTrapDomainStatusAlarmType"))
)
if mibBuilder.loadTexts:
    scfDomainStatusAlarm.setStatus(
        "current"
    )

scfDomainXsbEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2, 0, 6)
)
scfDomainXsbEvent.setObjects(
      *(("OPL-SP-MIB", "scfXsbDomainId"),
        ("OPL-SP-MIB", "scfTrapEventType"))
)
if mibBuilder.loadTexts:
    scfDomainXsbEvent.setStatus(
        "current"
    )

scfIoBoxEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2, 0, 7)
)
scfIoBoxEvent.setObjects(
      *(("OPL-SP-MIB", "scfTrapIoBoxId"),
        ("OPL-SP-MIB", "scfTrapIoBoxSubType"),
        ("OPL-SP-MIB", "scfTrapIoBoxSubId"),
        ("OPL-SP-MIB", "scfTrapEventType"))
)
if mibBuilder.loadTexts:
    scfIoBoxEvent.setStatus(
        "current"
    )

scfIoBoxLedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2, 0, 8)
)
scfIoBoxLedEvent.setObjects(
      *(("OPL-SP-MIB", "scfTrapIoBoxId"),
        ("OPL-SP-MIB", "scfTrapIoBoxSubType"),
        ("OPL-SP-MIB", "scfTrapIoBoxSubId"),
        ("OPL-SP-MIB", "scfTrapIoBoxLedType"),
        ("OPL-SP-MIB", "scfTrapIoBoxLedValue"))
)
if mibBuilder.loadTexts:
    scfIoBoxLedEvent.setStatus(
        "current"
    )

scfIoBoxTemperatureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2, 0, 9)
)
scfIoBoxTemperatureEvent.setObjects(
      *(("OPL-SP-MIB", "scfTrapIoBoxId"),
        ("OPL-SP-MIB", "scfTrapIoBoxSubType"),
        ("OPL-SP-MIB", "scfTrapIoBoxSubId"),
        ("OPL-SP-MIB", "scfTrapIoBoxTempEventType"))
)
if mibBuilder.loadTexts:
    scfIoBoxTemperatureEvent.setStatus(
        "current"
    )

scfModeSwitchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 2, 0, 10)
)
scfModeSwitchEvent.setObjects(
      *(("OPL-SP-MIB", "scfTrapModeSwitchEventType"),
        ("OPL-SP-MIB", "scfModeSwitch"))
)
if mibBuilder.loadTexts:
    scfModeSwitchEvent.setStatus(
        "current"
    )


# Notifications groups

scfNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 2, 2, 1)
)
scfNotificationsGroup.setObjects(
      *(("OPL-SP-MIB", "scfSPFailover"),
        ("OPL-SP-MIB", "scfComponentEvent"),
        ("OPL-SP-MIB", "scfComponentStatusEvent"),
        ("OPL-SP-MIB", "scfXsbModeChangeEvent"),
        ("OPL-SP-MIB", "scfDomainStatusAlarm"),
        ("OPL-SP-MIB", "scfDomainXsbEvent"),
        ("OPL-SP-MIB", "scfIoBoxEvent"),
        ("OPL-SP-MIB", "scfIoBoxLedEvent"),
        ("OPL-SP-MIB", "scfIoBoxTemperatureEvent"),
        ("OPL-SP-MIB", "scfModeSwitchEvent"))
)
if mibBuilder.loadTexts:
    scfNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

scfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 211, 1, 15, 3, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    scfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPL-SP-MIB",
    **{"ScfMonitorTypeTC": ScfMonitorTypeTC,
       "ScfComponentType": ScfComponentType,
       "ScfValidStatus": ScfValidStatus,
       "ScfLEDState": ScfLEDState,
       "ScfModeSwitchState": ScfModeSwitchState,
       "ScfStateTC": ScfStateTC,
       "ScfErrorStatus": ScfErrorStatus,
       "ScfDomainStatusTC": ScfDomainStatusTC,
       "ScfDomainConfigPolicy": ScfDomainConfigPolicy,
       "ScfIoBoxLEDState": ScfIoBoxLEDState,
       "ScfIoBoxComponentLocation": ScfIoBoxComponentLocation,
       "ScfIoBoxComponentType": ScfIoBoxComponentType,
       "ScfIoBoatTypeTC": ScfIoBoatTypeTC,
       "ScfIoBoxEnabledAlarms": ScfIoBoxEnabledAlarms,
       "ScfCodState": ScfCodState,
       "ScfBoardSubTypeTC": ScfBoardSubTypeTC,
       "ScfTrapEventTypeTC": ScfTrapEventTypeTC,
       "ScfTrapStatusEventTypeTC": ScfTrapStatusEventTypeTC,
       "ScfDomainStatusAlarmType": ScfDomainStatusAlarmType,
       "ScfTrapIoBoxTempEventTypeTC": ScfTrapIoBoxTempEventTypeTC,
       "ScfIoBoxLEDType": ScfIoBoxLEDType,
       "ScfTrapModeSwitchEventTypeTC": ScfTrapModeSwitchEventTypeTC,
       "ScfIndex": ScfIndex,
       "ScfIoBoxIndex": ScfIoBoxIndex,
       "ScfXsbIndex": ScfXsbIndex,
       "ScfDRState": ScfDRState,
       "ScfUsageState": ScfUsageState,
       "ScfTestState": ScfTestState,
       "ScfAssignmentState": ScfAssignmentState,
       "ScfConnectivityState": ScfConnectivityState,
       "ScfConfigurationState": ScfConfigurationState,
       "fujitsu": fujitsu,
       "product": product,
       "solaris": solaris,
       "sparcEnterprise": sparcEnterprise,
       "oplSpMIB": oplSpMIB,
       "scfObjects": scfObjects,
       "scfInfo": scfInfo,
       "scfAgentId": scfAgentId,
       "scfAgentNumber": scfAgentNumber,
       "scfAgentTable": scfAgentTable,
       "scfAgentEntry": scfAgentEntry,
       "scfAgentIndex": scfAgentIndex,
       "scfXcpVersion": scfXcpVersion,
       "scfIpAddressPortNumber": scfIpAddressPortNumber,
       "scfIpAddressNumber": scfIpAddressNumber,
       "scfIpAddressTable": scfIpAddressTable,
       "scfIpAddressEntry": scfIpAddressEntry,
       "scfIpAddressIndex": scfIpAddressIndex,
       "scfIpAddress": scfIpAddress,
       "scfState": scfState,
       "scfSystemState": scfSystemState,
       "scfFirmwareState": scfFirmwareState,
       "scfHardwareState": scfHardwareState,
       "scfModeSwitch": scfModeSwitch,
       "scfMonitorInfo": scfMonitorInfo,
       "scfMonitorNumber": scfMonitorNumber,
       "scfMonitorTable": scfMonitorTable,
       "scfMonitorEntry": scfMonitorEntry,
       "scfMonitorBoardType": scfMonitorBoardType,
       "scfMonitorBoardId": scfMonitorBoardId,
       "scfMonitorModuleType": scfMonitorModuleType,
       "scfMonitorModuleId": scfMonitorModuleId,
       "scfMonitorType": scfMonitorType,
       "scfMonitorId": scfMonitorId,
       "scfMonitorDescription": scfMonitorDescription,
       "scfMonitorAdditionalInfo": scfMonitorAdditionalInfo,
       "scfMonitorUnits": scfMonitorUnits,
       "scfMonitorStatus": scfMonitorStatus,
       "scfMonitorValue": scfMonitorValue,
       "scfMonitorValueStatus": scfMonitorValueStatus,
       "scfSystemInfo": scfSystemInfo,
       "scfSystemName": scfSystemName,
       "scfSystemType": scfSystemType,
       "scfSystemSerialNumber": scfSystemSerialNumber,
       "scfSystemAdditionalInfo": scfSystemAdditionalInfo,
       "scfSystemCpuNumber": scfSystemCpuNumber,
       "scfSystemMemoryCapacity": scfSystemMemoryCapacity,
       "scfSystemReadyLED": scfSystemReadyLED,
       "scfSystemPowerLED": scfSystemPowerLED,
       "scfSystemCheckLED": scfSystemCheckLED,
       "scfSystemActualPowerConsumption": scfSystemActualPowerConsumption,
       "scfSystemActualPowerConsumptionValue": scfSystemActualPowerConsumptionValue,
       "scfSystemActualPowerConsumptionUnit": scfSystemActualPowerConsumptionUnit,
       "scfSystemActualPowerMinPollingInterval": scfSystemActualPowerMinPollingInterval,
       "scfSystemAirFlow": scfSystemAirFlow,
       "scfSystemExhaustAirFlowValue": scfSystemExhaustAirFlowValue,
       "scfSystemExhaustAirFlowUnit": scfSystemExhaustAirFlowUnit,
       "scfSystemExhaustAirFlowMinPollingInterval": scfSystemExhaustAirFlowMinPollingInterval,
       "scfSystemAmbientTemperature": scfSystemAmbientTemperature,
       "scfSystemAmbientTemperatureValue": scfSystemAmbientTemperatureValue,
       "scfSystemAmbientTemperatureUnit": scfSystemAmbientTemperatureUnit,
       "scfSystemAmbientTemperatureMinPollingInterval": scfSystemAmbientTemperatureMinPollingInterval,
       "scfSystemPowerSource": scfSystemPowerSource,
       "scfSystemPermittedPowerConsumption": scfSystemPermittedPowerConsumption,
       "scfSystemPermittedPowerConsumptionValue": scfSystemPermittedPowerConsumptionValue,
       "scfSystemPermittedPowerConsumptionUnit": scfSystemPermittedPowerConsumptionUnit,
       "scfSystemAvailablePowerConsumption": scfSystemAvailablePowerConsumption,
       "scfDomainInfo": scfDomainInfo,
       "scfDomainNumber": scfDomainNumber,
       "scfDomainTable": scfDomainTable,
       "scfDomainEntry": scfDomainEntry,
       "scfDomainId": scfDomainId,
       "scfDomainCpuNumber": scfDomainCpuNumber,
       "scfDomainMemoryCapacity": scfDomainMemoryCapacity,
       "scfDomainObpVersion": scfDomainObpVersion,
       "scfDomainObpAdditionalInfo": scfDomainObpAdditionalInfo,
       "scfDomainOsMachine": scfDomainOsMachine,
       "scfDomainOsRelease": scfDomainOsRelease,
       "scfDomainOsSysName": scfDomainOsSysName,
       "scfDomainOsNodeName": scfDomainOsNodeName,
       "scfDomainOsVersion": scfDomainOsVersion,
       "scfDomainOsAdditionalInfo": scfDomainOsAdditionalInfo,
       "scfDomainValid": scfDomainValid,
       "scfDomainXsbs": scfDomainXsbs,
       "scfDomainStatus": scfDomainStatus,
       "scfDomainErrorStatus": scfDomainErrorStatus,
       "scfDomainConfigurationPolicy": scfDomainConfigurationPolicy,
       "scfXsbInfo": scfXsbInfo,
       "scfXsbType": scfXsbType,
       "scfXsbNumber": scfXsbNumber,
       "scfXsbTable": scfXsbTable,
       "scfXsbEntry": scfXsbEntry,
       "scfXsbId": scfXsbId,
       "scfXsbStatus": scfXsbStatus,
       "scfXsbErrorStatus": scfXsbErrorStatus,
       "scfXsbDomainId": scfXsbDomainId,
       "scfXsbDrStatus": scfXsbDrStatus,
       "scfXsbSubStatusPower": scfXsbSubStatusPower,
       "scfXsbSubStatusTest": scfXsbSubStatusTest,
       "scfXsbSubStatusAssignment": scfXsbSubStatusAssignment,
       "scfXsbSubStatusConnectivity": scfXsbSubStatusConnectivity,
       "scfXsbSubStatusConfiguration": scfXsbSubStatusConfiguration,
       "scfXsbSetupDID": scfXsbSetupDID,
       "scfXsbNextDID": scfXsbNextDID,
       "scfLsbInfo": scfLsbInfo,
       "scfLsbType": scfLsbType,
       "scfLsbNumber": scfLsbNumber,
       "scfLsbTable": scfLsbTable,
       "scfLsbEntry": scfLsbEntry,
       "scfLsbDomainId": scfLsbDomainId,
       "scfLsbId": scfLsbId,
       "scfLsbXsbId": scfLsbXsbId,
       "scfLsbNoMem": scfLsbNoMem,
       "scfLsbNoIo": scfLsbNoIo,
       "scfLsbFloatingBoard": scfLsbFloatingBoard,
       "scfBoardInfo": scfBoardInfo,
       "scfBoardNumber": scfBoardNumber,
       "scfBoardTable": scfBoardTable,
       "scfBoardEntry": scfBoardEntry,
       "scfBoardType": scfBoardType,
       "scfBoardId": scfBoardId,
       "scfBoardName": scfBoardName,
       "scfBoardAdditionalInfo": scfBoardAdditionalInfo,
       "scfBoardXsbs": scfBoardXsbs,
       "scfBoardState": scfBoardState,
       "scfBoardCODEnabled": scfBoardCODEnabled,
       "scfBoardSubType": scfBoardSubType,
       "scfCpuInfo": scfCpuInfo,
       "scfCpuNumber": scfCpuNumber,
       "scfCpuTable": scfCpuTable,
       "scfCpuEntry": scfCpuEntry,
       "scfCpuBoardType": scfCpuBoardType,
       "scfCpuBoardId": scfCpuBoardId,
       "scfCpuModuleType": scfCpuModuleType,
       "scfCpuModuleId": scfCpuModuleId,
       "scfCpuSubType": scfCpuSubType,
       "scfCpuSubId": scfCpuSubId,
       "scfCpuType": scfCpuType,
       "scfCpuFrequency": scfCpuFrequency,
       "scfCpuAdditionalInfo": scfCpuAdditionalInfo,
       "scfCpuState": scfCpuState,
       "scfMemoryInfo": scfMemoryInfo,
       "scfMemoryNumber": scfMemoryNumber,
       "scfMemoryTable": scfMemoryTable,
       "scfMemoryEntry": scfMemoryEntry,
       "scfMemoryBoardType": scfMemoryBoardType,
       "scfMemoryBoardId": scfMemoryBoardId,
       "scfMemoryModuleType": scfMemoryModuleType,
       "scfMemoryModuleId": scfMemoryModuleId,
       "scfMemorySubType": scfMemorySubType,
       "scfMemorySubId": scfMemorySubId,
       "scfMemoryName": scfMemoryName,
       "scfMemoryCapacity": scfMemoryCapacity,
       "scfMemoryAdditionalInfo": scfMemoryAdditionalInfo,
       "scfMemoryState": scfMemoryState,
       "scfIoBoxInfo": scfIoBoxInfo,
       "scfIoBoxNumber": scfIoBoxNumber,
       "scfIoBoxTable": scfIoBoxTable,
       "scfIoBoxEntry": scfIoBoxEntry,
       "scfIoBoxId": scfIoBoxId,
       "scfIoBoxLocationLED": scfIoBoxLocationLED,
       "scfIoBoxOverTempLED": scfIoBoxOverTempLED,
       "scfIoBoxServiceReqLED": scfIoBoxServiceReqLED,
       "scfIoBoxActiveLED": scfIoBoxActiveLED,
       "scfIoBoxPartNumber": scfIoBoxPartNumber,
       "scfIoBoxSerialNumber": scfIoBoxSerialNumber,
       "scfIoBoxDashLevel": scfIoBoxDashLevel,
       "scfIoBoatNumber": scfIoBoatNumber,
       "scfIoBoatTable": scfIoBoatTable,
       "scfIoBoatEntry": scfIoBoatEntry,
       "scfIoBoatIoBoxId": scfIoBoatIoBoxId,
       "scfIoBoatId": scfIoBoatId,
       "scfIoBoatLocation": scfIoBoatLocation,
       "scfIoBoatType": scfIoBoatType,
       "scfIoBoatOKtoRemoveLED": scfIoBoatOKtoRemoveLED,
       "scfIoBoatServiceReqLED": scfIoBoatServiceReqLED,
       "scfIoBoatActiveLED": scfIoBoatActiveLED,
       "scfIoBoatPartNumber": scfIoBoatPartNumber,
       "scfIoBoatSerialNumber": scfIoBoatSerialNumber,
       "scfIoBoatDashLevel": scfIoBoatDashLevel,
       "scfLinkCardNumber": scfLinkCardNumber,
       "scfLinkCardTable": scfLinkCardTable,
       "scfLinkCardEntry": scfLinkCardEntry,
       "scfLinkCardIoBoxId": scfLinkCardIoBoxId,
       "scfLinkCardIoBoatId": scfLinkCardIoBoatId,
       "scfLinkCardId": scfLinkCardId,
       "scfLinkCardDataLED": scfLinkCardDataLED,
       "scfLinkCardMgmtLED": scfLinkCardMgmtLED,
       "scfLinkCardDownlinkCardLocation": scfLinkCardDownlinkCardLocation,
       "scfLinkCardDownlinkCardId": scfLinkCardDownlinkCardId,
       "scfLinkCardPartNumber": scfLinkCardPartNumber,
       "scfLinkCardSerialNumber": scfLinkCardSerialNumber,
       "scfLinkCardDashLevel": scfLinkCardDashLevel,
       "scfPowerSupplyFanNumber": scfPowerSupplyFanNumber,
       "scfPowerSupplyFanTable": scfPowerSupplyFanTable,
       "scfPowerSupplyFanEntry": scfPowerSupplyFanEntry,
       "scfPowerSupplyFanIoBoxId": scfPowerSupplyFanIoBoxId,
       "scfPowerSupplyFanId": scfPowerSupplyFanId,
       "scfPowerSupplyFanLocation": scfPowerSupplyFanLocation,
       "scfPowerSupplyFanOKtoRemoveLED": scfPowerSupplyFanOKtoRemoveLED,
       "scfPowerSupplyFanServiceReqLED": scfPowerSupplyFanServiceReqLED,
       "scfPowerSupplyFanACPowerLED": scfPowerSupplyFanACPowerLED,
       "scfPowerSupplyFanDCPowerLED": scfPowerSupplyFanDCPowerLED,
       "scfPowerSupplyFanPartNumber": scfPowerSupplyFanPartNumber,
       "scfPowerSupplyFanSerialNumber": scfPowerSupplyFanSerialNumber,
       "scfPowerSupplyFanDashLevel": scfPowerSupplyFanDashLevel,
       "scfIoBoxSensorNumber": scfIoBoxSensorNumber,
       "scfIoBoxSensorTable": scfIoBoxSensorTable,
       "scfIoBoxSensorEntry": scfIoBoxSensorEntry,
       "scfIoBoxSensorIoBoxId": scfIoBoxSensorIoBoxId,
       "scfIoBoxSensorIoBoxSubType": scfIoBoxSensorIoBoxSubType,
       "scfIoBoxSensorIoBoxSubId": scfIoBoxSensorIoBoxSubId,
       "scfIoBoxSensorId": scfIoBoxSensorId,
       "scfIoBoxSensorDescription": scfIoBoxSensorDescription,
       "scfIoBoxSensorUnits": scfIoBoxSensorUnits,
       "scfIoBoxSensorValue": scfIoBoxSensorValue,
       "scfIoBoxSensorEnabledAlarms": scfIoBoxSensorEnabledAlarms,
       "scfIoBoxSensorMinAlarm": scfIoBoxSensorMinAlarm,
       "scfIoBoxSensorMaxAlarm": scfIoBoxSensorMaxAlarm,
       "scfComponentInfo": scfComponentInfo,
       "scfComponentNumber": scfComponentNumber,
       "scfComponentTable": scfComponentTable,
       "scfComponentEntry": scfComponentEntry,
       "scfComponentBoardType": scfComponentBoardType,
       "scfComponentBoardId": scfComponentBoardId,
       "scfComponentModuleType": scfComponentModuleType,
       "scfComponentModuleId": scfComponentModuleId,
       "scfComponentSubType": scfComponentSubType,
       "scfComponentSubId": scfComponentSubId,
       "scfComponentAdditionalInfo": scfComponentAdditionalInfo,
       "scfComponentPartNumber": scfComponentPartNumber,
       "scfComponentSerialNumber": scfComponentSerialNumber,
       "scfComponentProductName": scfComponentProductName,
       "scfComponentManufacturer": scfComponentManufacturer,
       "scfComponentManufactureDate": scfComponentManufactureDate,
       "scfComponentStatus": scfComponentStatus,
       "scfComponentErrorStatus": scfComponentErrorStatus,
       "scfMIBTraps": scfMIBTraps,
       "scfMIBTrapPrefix": scfMIBTrapPrefix,
       "scfSPFailover": scfSPFailover,
       "scfComponentEvent": scfComponentEvent,
       "scfComponentStatusEvent": scfComponentStatusEvent,
       "scfXsbModeChangeEvent": scfXsbModeChangeEvent,
       "scfDomainStatusAlarm": scfDomainStatusAlarm,
       "scfDomainXsbEvent": scfDomainXsbEvent,
       "scfIoBoxEvent": scfIoBoxEvent,
       "scfIoBoxLedEvent": scfIoBoxLedEvent,
       "scfIoBoxTemperatureEvent": scfIoBoxTemperatureEvent,
       "scfModeSwitchEvent": scfModeSwitchEvent,
       "scfMIBTrapData": scfMIBTrapData,
       "scfTrapEventType": scfTrapEventType,
       "scfTrapStatusEventType": scfTrapStatusEventType,
       "scfTrapDomainStatusAlarmType": scfTrapDomainStatusAlarmType,
       "scfTrapIoBoxId": scfTrapIoBoxId,
       "scfTrapIoBoxSubType": scfTrapIoBoxSubType,
       "scfTrapIoBoxSubId": scfTrapIoBoxSubId,
       "scfTrapIoBoxTempEventType": scfTrapIoBoxTempEventType,
       "scfTrapIoBoxLedType": scfTrapIoBoxLedType,
       "scfTrapIoBoxLedValue": scfTrapIoBoxLedValue,
       "scfTrapModeSwitchEventType": scfTrapModeSwitchEventType,
       "scfMIBConformances": scfMIBConformances,
       "scfMIBCompliances": scfMIBCompliances,
       "scfCompliance": scfCompliance,
       "scfMIBGroups": scfMIBGroups,
       "scfMIBObjectGroups": scfMIBObjectGroups,
       "scfInfoGroup": scfInfoGroup,
       "scfStateGroup": scfStateGroup,
       "scfMonitorInfoGroup": scfMonitorInfoGroup,
       "scfSystemInfoGroup": scfSystemInfoGroup,
       "scfDomainInfoGroup": scfDomainInfoGroup,
       "scfXsbInfoGroup": scfXsbInfoGroup,
       "scfLsbInfoGroup": scfLsbInfoGroup,
       "scfBoardInfoGroup": scfBoardInfoGroup,
       "scfCpuInfoGroup": scfCpuInfoGroup,
       "scfMemoryInfoGroup": scfMemoryInfoGroup,
       "scfIoBoxInfoGroup": scfIoBoxInfoGroup,
       "scfComponentInfoGroup": scfComponentInfoGroup,
       "scfNotificationObjectGroup": scfNotificationObjectGroup,
       "scfSystemActualPowerConsumptionGroup": scfSystemActualPowerConsumptionGroup,
       "scfSystemAmbientTemperatureGroup": scfSystemAmbientTemperatureGroup,
       "scfSystemPermittedPowerConsumptionGroup": scfSystemPermittedPowerConsumptionGroup,
       "scfSystemAirFlowGroup": scfSystemAirFlowGroup,
       "scfMIBNotifGroups": scfMIBNotifGroups,
       "scfNotificationsGroup": scfNotificationsGroup}
)
