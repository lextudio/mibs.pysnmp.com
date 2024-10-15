# SNMP MIB module (ACE20-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACE20-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:29 2024
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

(AtmTrafficDescrParamIndex,) = mibBuilder.importSymbols(
    "ATM-MIB",
    "AtmTrafficDescrParamIndex")

(ifAlias,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAlias")

(TimeSlots,
 agnIndication,
 agnLed,
 alarmSeverity,
 alarmState,
 radAtm) = mibBuilder.importSymbols(
    "RAD-MIB",
    "TimeSlots",
    "agnIndication",
    "agnLed",
    "alarmSeverity",
    "alarmState",
    "radAtm")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RadAtmEvents_ObjectIdentity = ObjectIdentity
radAtmEvents = _RadAtmEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 0)
)
if mibBuilder.loadTexts:
    radAtmEvents.setStatus("current")
_AtmSu_ObjectIdentity = ObjectIdentity
atmSu = _AtmSu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 4)
)
_AtmSuSystem_ObjectIdentity = ObjectIdentity
atmSuSystem = _AtmSuSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1)
)


class _AtmSuSystemSwOperStatus_Type(Integer32):
    """Custom type atmSuSystemSwOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AtmSuSystemSwOperStatus_Type.__name__ = "Integer32"
_AtmSuSystemSwOperStatus_Object = MibScalar
atmSuSystemSwOperStatus = _AtmSuSystemSwOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 1),
    _AtmSuSystemSwOperStatus_Type()
)
atmSuSystemSwOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuSystemSwOperStatus.setStatus("current")


class _AtmSuSystemSwSwitchVersionsCmd_Type(Integer32):
    """Custom type atmSuSystemSwSwitchVersionsCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1))
    )


_AtmSuSystemSwSwitchVersionsCmd_Type.__name__ = "Integer32"
_AtmSuSystemSwSwitchVersionsCmd_Object = MibScalar
atmSuSystemSwSwitchVersionsCmd = _AtmSuSystemSwSwitchVersionsCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 2),
    _AtmSuSystemSwSwitchVersionsCmd_Type()
)
atmSuSystemSwSwitchVersionsCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuSystemSwSwitchVersionsCmd.setStatus("current")
_AtmSuSystemHistoryAlrTable_Object = MibTable
atmSuSystemHistoryAlrTable = _AtmSuSystemHistoryAlrTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 3)
)
if mibBuilder.loadTexts:
    atmSuSystemHistoryAlrTable.setStatus("current")
_AtmSuSystemHistoryAlrEntry_Object = MibTableRow
atmSuSystemHistoryAlrEntry = _AtmSuSystemHistoryAlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 3, 1)
)
atmSuSystemHistoryAlrEntry.setIndexNames(
    (0, "ACE20-MIB", "atmSuSystemHistoryAlrIndex"),
)
if mibBuilder.loadTexts:
    atmSuSystemHistoryAlrEntry.setStatus("current")
_AtmSuSystemHistoryAlrIndex_Type = Integer32
_AtmSuSystemHistoryAlrIndex_Object = MibTableColumn
atmSuSystemHistoryAlrIndex = _AtmSuSystemHistoryAlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 3, 1, 1),
    _AtmSuSystemHistoryAlrIndex_Type()
)
atmSuSystemHistoryAlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuSystemHistoryAlrIndex.setStatus("current")
_AtmSuSystemHistoryAlrIfIndex_Type = Integer32
_AtmSuSystemHistoryAlrIfIndex_Object = MibTableColumn
atmSuSystemHistoryAlrIfIndex = _AtmSuSystemHistoryAlrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 3, 1, 2),
    _AtmSuSystemHistoryAlrIfIndex_Type()
)
atmSuSystemHistoryAlrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuSystemHistoryAlrIfIndex.setStatus("current")


class _AtmSuSystemHistoryAlrDescription_Type(DisplayString):
    """Custom type atmSuSystemHistoryAlrDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtmSuSystemHistoryAlrDescription_Type.__name__ = "DisplayString"
_AtmSuSystemHistoryAlrDescription_Object = MibTableColumn
atmSuSystemHistoryAlrDescription = _AtmSuSystemHistoryAlrDescription_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 3, 1, 3),
    _AtmSuSystemHistoryAlrDescription_Type()
)
atmSuSystemHistoryAlrDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuSystemHistoryAlrDescription.setStatus("current")


class _AtmSuSystemHistoryAlrStatus_Type(Integer32):
    """Custom type atmSuSystemHistoryAlrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("event", 3),
          ("off", 2),
          ("on", 1))
    )


_AtmSuSystemHistoryAlrStatus_Type.__name__ = "Integer32"
_AtmSuSystemHistoryAlrStatus_Object = MibTableColumn
atmSuSystemHistoryAlrStatus = _AtmSuSystemHistoryAlrStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 3, 1, 4),
    _AtmSuSystemHistoryAlrStatus_Type()
)
atmSuSystemHistoryAlrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuSystemHistoryAlrStatus.setStatus("current")
_AtmSuSystemHistoryAlrOccurrenceTime_Type = DisplayString
_AtmSuSystemHistoryAlrOccurrenceTime_Object = MibTableColumn
atmSuSystemHistoryAlrOccurrenceTime = _AtmSuSystemHistoryAlrOccurrenceTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 3, 1, 5),
    _AtmSuSystemHistoryAlrOccurrenceTime_Type()
)
atmSuSystemHistoryAlrOccurrenceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuSystemHistoryAlrOccurrenceTime.setStatus("current")
_AtmSuSystemHistoryAlrVpi_Type = Integer32
_AtmSuSystemHistoryAlrVpi_Object = MibTableColumn
atmSuSystemHistoryAlrVpi = _AtmSuSystemHistoryAlrVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 3, 1, 6),
    _AtmSuSystemHistoryAlrVpi_Type()
)
atmSuSystemHistoryAlrVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuSystemHistoryAlrVpi.setStatus("current")
_AtmSuSystemHistoryAlrVci_Type = Integer32
_AtmSuSystemHistoryAlrVci_Object = MibTableColumn
atmSuSystemHistoryAlrVci = _AtmSuSystemHistoryAlrVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 3, 1, 7),
    _AtmSuSystemHistoryAlrVci_Type()
)
atmSuSystemHistoryAlrVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuSystemHistoryAlrVci.setStatus("current")


class _AtmSuSystemClearHistoryAlrListCmd_Type(Integer32):
    """Custom type atmSuSystemClearHistoryAlrListCmd based on Integer32"""
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


_AtmSuSystemClearHistoryAlrListCmd_Type.__name__ = "Integer32"
_AtmSuSystemClearHistoryAlrListCmd_Object = MibScalar
atmSuSystemClearHistoryAlrListCmd = _AtmSuSystemClearHistoryAlrListCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 4),
    _AtmSuSystemClearHistoryAlrListCmd_Type()
)
atmSuSystemClearHistoryAlrListCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuSystemClearHistoryAlrListCmd.setStatus("current")
_AtmSuSystemCurrentAlrTable_Object = MibTable
atmSuSystemCurrentAlrTable = _AtmSuSystemCurrentAlrTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 5)
)
if mibBuilder.loadTexts:
    atmSuSystemCurrentAlrTable.setStatus("current")
_AtmSuSystemCurrentAlrEntry_Object = MibTableRow
atmSuSystemCurrentAlrEntry = _AtmSuSystemCurrentAlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 5, 1)
)
atmSuSystemCurrentAlrEntry.setIndexNames(
    (0, "ACE20-MIB", "atmSuSystemCurrentAlrIndex"),
)
if mibBuilder.loadTexts:
    atmSuSystemCurrentAlrEntry.setStatus("current")
_AtmSuSystemCurrentAlrIndex_Type = Integer32
_AtmSuSystemCurrentAlrIndex_Object = MibTableColumn
atmSuSystemCurrentAlrIndex = _AtmSuSystemCurrentAlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 5, 1, 1),
    _AtmSuSystemCurrentAlrIndex_Type()
)
atmSuSystemCurrentAlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuSystemCurrentAlrIndex.setStatus("current")
_AtmSuSystemCurrentAlrIfIndex_Type = Integer32
_AtmSuSystemCurrentAlrIfIndex_Object = MibTableColumn
atmSuSystemCurrentAlrIfIndex = _AtmSuSystemCurrentAlrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 5, 1, 2),
    _AtmSuSystemCurrentAlrIfIndex_Type()
)
atmSuSystemCurrentAlrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuSystemCurrentAlrIfIndex.setStatus("current")


class _AtmSuSystemCurrentAlrDescription_Type(DisplayString):
    """Custom type atmSuSystemCurrentAlrDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtmSuSystemCurrentAlrDescription_Type.__name__ = "DisplayString"
_AtmSuSystemCurrentAlrDescription_Object = MibTableColumn
atmSuSystemCurrentAlrDescription = _AtmSuSystemCurrentAlrDescription_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 5, 1, 3),
    _AtmSuSystemCurrentAlrDescription_Type()
)
atmSuSystemCurrentAlrDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuSystemCurrentAlrDescription.setStatus("current")
_AtmSuSystemILMICommunity_Type = DisplayString
_AtmSuSystemILMICommunity_Object = MibScalar
atmSuSystemILMICommunity = _AtmSuSystemILMICommunity_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 6),
    _AtmSuSystemILMICommunity_Type()
)
atmSuSystemILMICommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuSystemILMICommunity.setStatus("current")


class _AtmSuSystemTrapMaxManagers_Type(Integer32):
    """Custom type atmSuSystemTrapMaxManagers based on Integer32"""
    defaultValue = 10


_AtmSuSystemTrapMaxManagers_Object = MibScalar
atmSuSystemTrapMaxManagers = _AtmSuSystemTrapMaxManagers_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 7),
    _AtmSuSystemTrapMaxManagers_Type()
)
atmSuSystemTrapMaxManagers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuSystemTrapMaxManagers.setStatus("current")


class _AtmSuSystemAalSelection_Type(Integer32):
    """Custom type atmSuSystemAalSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aal1", 3),
          ("aal2", 2),
          ("notApplicable", 1))
    )


_AtmSuSystemAalSelection_Type.__name__ = "Integer32"
_AtmSuSystemAalSelection_Object = MibScalar
atmSuSystemAalSelection = _AtmSuSystemAalSelection_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 8),
    _AtmSuSystemAalSelection_Type()
)
atmSuSystemAalSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuSystemAalSelection.setStatus("current")


class _AtmSuSystemCodingLaw_Type(Integer32):
    """Custom type atmSuSystemCodingLaw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aLaw", 2),
          ("notApplicable", 1),
          ("uLaw", 3))
    )


_AtmSuSystemCodingLaw_Type.__name__ = "Integer32"
_AtmSuSystemCodingLaw_Object = MibScalar
atmSuSystemCodingLaw = _AtmSuSystemCodingLaw_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 9),
    _AtmSuSystemCodingLaw_Type()
)
atmSuSystemCodingLaw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuSystemCodingLaw.setStatus("current")


class _AtmSuSystemISDNDataLinkActivation_Type(Integer32):
    """Custom type atmSuSystemISDNDataLinkActivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonPermanent", 2),
          ("notApplicable", 1),
          ("permanent", 3))
    )


_AtmSuSystemISDNDataLinkActivation_Type.__name__ = "Integer32"
_AtmSuSystemISDNDataLinkActivation_Object = MibScalar
atmSuSystemISDNDataLinkActivation = _AtmSuSystemISDNDataLinkActivation_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 10),
    _AtmSuSystemISDNDataLinkActivation_Type()
)
atmSuSystemISDNDataLinkActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuSystemISDNDataLinkActivation.setStatus("current")
_AtmSuSystemJitterBuffer_Type = Integer32
_AtmSuSystemJitterBuffer_Object = MibScalar
atmSuSystemJitterBuffer = _AtmSuSystemJitterBuffer_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 11),
    _AtmSuSystemJitterBuffer_Type()
)
atmSuSystemJitterBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuSystemJitterBuffer.setStatus("current")


class _AtmSuSystemOperMode_Type(Integer32):
    """Custom type atmSuSystemOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ima", 2),
          ("miniDslam", 3),
          ("notApplicable", 1))
    )


_AtmSuSystemOperMode_Type.__name__ = "Integer32"
_AtmSuSystemOperMode_Object = MibScalar
atmSuSystemOperMode = _AtmSuSystemOperMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 12),
    _AtmSuSystemOperMode_Type()
)
atmSuSystemOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuSystemOperMode.setStatus("current")
_AtmSuSystemDSPGain_Type = Integer32
_AtmSuSystemDSPGain_Object = MibScalar
atmSuSystemDSPGain = _AtmSuSystemDSPGain_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 1, 13),
    _AtmSuSystemDSPGain_Type()
)
atmSuSystemDSPGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuSystemDSPGain.setStatus("current")
_AtmSuPort_ObjectIdentity = ObjectIdentity
atmSuPort = _AtmSuPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2)
)
_AtmSuPortDataCnfgTable_Object = MibTable
atmSuPortDataCnfgTable = _AtmSuPortDataCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 1)
)
if mibBuilder.loadTexts:
    atmSuPortDataCnfgTable.setStatus("current")
_AtmSuPortDataCnfgEntry_Object = MibTableRow
atmSuPortDataCnfgEntry = _AtmSuPortDataCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 1, 1)
)
atmSuPortDataCnfgEntry.setIndexNames(
    (0, "ACE20-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmSuPortDataCnfgEntry.setStatus("current")


class _AtmSuPortDataApplication_Type(Integer32):
    """Custom type atmSuPortDataApplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("aal1Stream", 5),
          ("atmDxi", 2),
          ("bridgedEthernet", 3),
          ("frameRelay", 1),
          ("notApplicable", 255),
          ("routedEthernet", 6),
          ("smdsDxi", 4))
    )


_AtmSuPortDataApplication_Type.__name__ = "Integer32"
_AtmSuPortDataApplication_Object = MibTableColumn
atmSuPortDataApplication = _AtmSuPortDataApplication_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 1, 1, 1),
    _AtmSuPortDataApplication_Type()
)
atmSuPortDataApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortDataApplication.setStatus("current")


class _AtmSuPortDataRate_Type(Integer32):
    """Custom type atmSuPortDataRate based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
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
              35,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 255),
          ("r1024KBps", 16),
          ("r1088KBps", 17),
          ("r1152KBps", 18),
          ("r1216KBps", 19),
          ("r1280KBps", 20),
          ("r128KBps", 2),
          ("r1344KBps", 21),
          ("r1408KBps", 22),
          ("r1472KBps", 23),
          ("r1536KBps", 24),
          ("r1544network", 25),
          ("r1600KBps", 26),
          ("r1664KBps", 27),
          ("r1728KBps", 28),
          ("r1792KBps", 29),
          ("r1856KBps", 30),
          ("r1920KBps", 31),
          ("r192KBps", 3),
          ("r1984KBps", 32),
          ("r2048KBps", 33),
          ("r2048network", 34),
          ("r256KBps", 4),
          ("r320KBps", 5),
          ("r384KBps", 6),
          ("r448KBps", 7),
          ("r512KBps", 8),
          ("r576KBps", 9),
          ("r640KBps", 10),
          ("r64KBps", 1),
          ("r704KBps", 11),
          ("r768KBps", 12),
          ("r8192KBps", 35),
          ("r832KBps", 13),
          ("r896KBps", 14),
          ("r960KBps", 15))
    )


_AtmSuPortDataRate_Type.__name__ = "Integer32"
_AtmSuPortDataRate_Object = MibTableColumn
atmSuPortDataRate = _AtmSuPortDataRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 1, 1, 2),
    _AtmSuPortDataRate_Type()
)
atmSuPortDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortDataRate.setStatus("current")


class _AtmSuPortDataDCD_Type(Integer32):
    """Custom type atmSuPortDataDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ignoreRtsDcdOff", 6),
          ("ignoreRtsDcdOn", 5),
          ("notApplicable", 255),
          ("obeyRtsDcdOff", 4),
          ("obeyRtsDcdOn", 3),
          ("off", 1),
          ("on", 2))
    )


_AtmSuPortDataDCD_Type.__name__ = "Integer32"
_AtmSuPortDataDCD_Object = MibTableColumn
atmSuPortDataDCD = _AtmSuPortDataDCD_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 1, 1, 3),
    _AtmSuPortDataDCD_Type()
)
atmSuPortDataDCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortDataDCD.setStatus("current")


class _AtmSuPortDataMode_Type(Integer32):
    """Custom type atmSuPortDataMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 255),
          ("nrz", 2),
          ("nrzi", 1))
    )


_AtmSuPortDataMode_Type.__name__ = "Integer32"
_AtmSuPortDataMode_Object = MibTableColumn
atmSuPortDataMode = _AtmSuPortDataMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 1, 1, 4),
    _AtmSuPortDataMode_Type()
)
atmSuPortDataMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortDataMode.setStatus("deprecated")


class _AtmSuPortDataCRC_Type(Integer32):
    """Custom type atmSuPortDataCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cRC16", 1),
          ("cRC32", 2),
          ("noCRC", 3),
          ("notApplicable", 255))
    )


_AtmSuPortDataCRC_Type.__name__ = "Integer32"
_AtmSuPortDataCRC_Object = MibTableColumn
atmSuPortDataCRC = _AtmSuPortDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 1, 1, 5),
    _AtmSuPortDataCRC_Type()
)
atmSuPortDataCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortDataCRC.setStatus("current")


class _AtmSuPortDataClock_Type(Integer32):
    """Custom type atmSuPortDataClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 3),
          ("edce", 2),
          ("notApplicable", 255))
    )


_AtmSuPortDataClock_Type.__name__ = "Integer32"
_AtmSuPortDataClock_Object = MibTableColumn
atmSuPortDataClock = _AtmSuPortDataClock_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 1, 1, 6),
    _AtmSuPortDataClock_Type()
)
atmSuPortDataClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortDataClock.setStatus("current")
_AtmSuPortDataMaxNoOfConns_Type = Integer32
_AtmSuPortDataMaxNoOfConns_Object = MibTableColumn
atmSuPortDataMaxNoOfConns = _AtmSuPortDataMaxNoOfConns_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 1, 1, 7),
    _AtmSuPortDataMaxNoOfConns_Type()
)
atmSuPortDataMaxNoOfConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortDataMaxNoOfConns.setStatus("current")
_AtmSuPortDataConfNoOfConns_Type = Integer32
_AtmSuPortDataConfNoOfConns_Object = MibTableColumn
atmSuPortDataConfNoOfConns = _AtmSuPortDataConfNoOfConns_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 1, 1, 8),
    _AtmSuPortDataConfNoOfConns_Type()
)
atmSuPortDataConfNoOfConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortDataConfNoOfConns.setStatus("current")


class _AtmSuPortDataIdleCode_Type(Integer32):
    """Custom type atmSuPortDataIdleCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmSuPortDataIdleCode_Type.__name__ = "Integer32"
_AtmSuPortDataIdleCode_Object = MibTableColumn
atmSuPortDataIdleCode = _AtmSuPortDataIdleCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 1, 1, 9),
    _AtmSuPortDataIdleCode_Type()
)
atmSuPortDataIdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortDataIdleCode.setStatus("current")


class _AtmSuPortDataInterfaceType_Type(Integer32):
    """Custom type atmSuPortDataInterfaceType based on Integer32"""
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
        *(("notApplicable", 1),
          ("rs530", 5),
          ("v35", 3),
          ("v36", 4),
          ("x21", 2))
    )


_AtmSuPortDataInterfaceType_Type.__name__ = "Integer32"
_AtmSuPortDataInterfaceType_Object = MibTableColumn
atmSuPortDataInterfaceType = _AtmSuPortDataInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 1, 1, 10),
    _AtmSuPortDataInterfaceType_Type()
)
atmSuPortDataInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortDataInterfaceType.setStatus("current")


class _AtmSuPortDataClkPolarity_Type(Integer32):
    """Custom type atmSuPortDataClkPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inverted", 3),
          ("normal", 2),
          ("notApplicable", 1))
    )


_AtmSuPortDataClkPolarity_Type.__name__ = "Integer32"
_AtmSuPortDataClkPolarity_Object = MibTableColumn
atmSuPortDataClkPolarity = _AtmSuPortDataClkPolarity_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 1, 1, 11),
    _AtmSuPortDataClkPolarity_Type()
)
atmSuPortDataClkPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortDataClkPolarity.setStatus("current")


class _AtmSuPortDataCtsStatus_Type(Integer32):
    """Custom type atmSuPortDataCtsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("off", 2),
          ("on", 3))
    )


_AtmSuPortDataCtsStatus_Type.__name__ = "Integer32"
_AtmSuPortDataCtsStatus_Object = MibTableColumn
atmSuPortDataCtsStatus = _AtmSuPortDataCtsStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 1, 1, 12),
    _AtmSuPortDataCtsStatus_Type()
)
atmSuPortDataCtsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortDataCtsStatus.setStatus("current")


class _AtmSuPortDataRtsStatus_Type(Integer32):
    """Custom type atmSuPortDataRtsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("off", 2),
          ("on", 3))
    )


_AtmSuPortDataRtsStatus_Type.__name__ = "Integer32"
_AtmSuPortDataRtsStatus_Object = MibTableColumn
atmSuPortDataRtsStatus = _AtmSuPortDataRtsStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 1, 1, 13),
    _AtmSuPortDataRtsStatus_Type()
)
atmSuPortDataRtsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortDataRtsStatus.setStatus("current")
_AtmSuPortDs1_ObjectIdentity = ObjectIdentity
atmSuPortDs1 = _AtmSuPortDs1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 2)
)
_AtmSuPortDs1CnfgTable_Object = MibTable
atmSuPortDs1CnfgTable = _AtmSuPortDs1CnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    atmSuPortDs1CnfgTable.setStatus("current")
_AtmSuPortDs1CnfgEntry_Object = MibTableRow
atmSuPortDs1CnfgEntry = _AtmSuPortDs1CnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 2, 1, 1)
)
atmSuPortDs1CnfgEntry.setIndexNames(
    (0, "ACE20-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmSuPortDs1CnfgEntry.setStatus("current")


class _AtmSuPortDs1CnfgRxSensitivity_Type(Integer32):
    """Custom type atmSuPortDs1CnfgRxSensitivity based on Integer32"""
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
        *(("s12dB", 1),
          ("s15dB", 4),
          ("s30dB", 2),
          ("s36dB", 3),
          ("s43dB", 5))
    )


_AtmSuPortDs1CnfgRxSensitivity_Type.__name__ = "Integer32"
_AtmSuPortDs1CnfgRxSensitivity_Object = MibTableColumn
atmSuPortDs1CnfgRxSensitivity = _AtmSuPortDs1CnfgRxSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 2, 1, 1, 1),
    _AtmSuPortDs1CnfgRxSensitivity_Type()
)
atmSuPortDs1CnfgRxSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortDs1CnfgRxSensitivity.setStatus("current")


class _AtmSuPortDs1CnfgLBO_Type(Integer32):
    """Custom type atmSuPortDs1CnfgLBO based on Integer32"""
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
        *(("balanceE1", 11),
          ("len0p133ft", 5),
          ("len133p266ft", 6),
          ("len266p399ft", 7),
          ("len399p533ft", 8),
          ("len533p655ft", 9),
          ("txGain0db", 1),
          ("txGain15db", 3),
          ("txGain22dot5db", 4),
          ("txGain7dot5db", 2),
          ("unbalanceE1", 10))
    )


_AtmSuPortDs1CnfgLBO_Type.__name__ = "Integer32"
_AtmSuPortDs1CnfgLBO_Object = MibTableColumn
atmSuPortDs1CnfgLBO = _AtmSuPortDs1CnfgLBO_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 2, 1, 1, 2),
    _AtmSuPortDs1CnfgLBO_Type()
)
atmSuPortDs1CnfgLBO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortDs1CnfgLBO.setStatus("current")


class _AtmSuPortDs1CnfgRestoreTime_Type(Integer32):
    """Custom type atmSuPortDs1CnfgRestoreTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ccittE1", 1),
          ("restoreT10sec62411", 3),
          ("restoreT1secFast", 2))
    )


_AtmSuPortDs1CnfgRestoreTime_Type.__name__ = "Integer32"
_AtmSuPortDs1CnfgRestoreTime_Object = MibTableColumn
atmSuPortDs1CnfgRestoreTime = _AtmSuPortDs1CnfgRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 2, 1, 1, 3),
    _AtmSuPortDs1CnfgRestoreTime_Type()
)
atmSuPortDs1CnfgRestoreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortDs1CnfgRestoreTime.setStatus("current")


class _AtmSuPortDs1CnfgInbandMng_Type(Integer32):
    """Custom type atmSuPortDs1CnfgInbandMng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dedicatedFr", 6),
          ("dedicatedTs", 4),
          ("off", 2))
    )


_AtmSuPortDs1CnfgInbandMng_Type.__name__ = "Integer32"
_AtmSuPortDs1CnfgInbandMng_Object = MibTableColumn
atmSuPortDs1CnfgInbandMng = _AtmSuPortDs1CnfgInbandMng_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 2, 1, 1, 4),
    _AtmSuPortDs1CnfgInbandMng_Type()
)
atmSuPortDs1CnfgInbandMng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortDs1CnfgInbandMng.setStatus("current")
_AtmSuPortDs1CnfgDedicatedTs_Type = Integer32
_AtmSuPortDs1CnfgDedicatedTs_Object = MibTableColumn
atmSuPortDs1CnfgDedicatedTs = _AtmSuPortDs1CnfgDedicatedTs_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 2, 1, 1, 5),
    _AtmSuPortDs1CnfgDedicatedTs_Type()
)
atmSuPortDs1CnfgDedicatedTs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortDs1CnfgDedicatedTs.setStatus("current")
_AtmSuPortDs1CbrCnfgTable_Object = MibTable
atmSuPortDs1CbrCnfgTable = _AtmSuPortDs1CbrCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 2, 2)
)
if mibBuilder.loadTexts:
    atmSuPortDs1CbrCnfgTable.setStatus("current")
_AtmSuPortDs1CbrCnfgEntry_Object = MibTableRow
atmSuPortDs1CbrCnfgEntry = _AtmSuPortDs1CbrCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 2, 2, 1)
)
atmSuPortDs1CbrCnfgEntry.setIndexNames(
    (0, "ACE20-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmSuPortDs1CbrCnfgEntry.setStatus("current")
_AtmSuPortDs1CbrIdleCode_Type = Integer32
_AtmSuPortDs1CbrIdleCode_Object = MibTableColumn
atmSuPortDs1CbrIdleCode = _AtmSuPortDs1CbrIdleCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 2, 2, 1, 1),
    _AtmSuPortDs1CbrIdleCode_Type()
)
atmSuPortDs1CbrIdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortDs1CbrIdleCode.setStatus("current")
_AtmSuPortDs1CbrRxTimeSlots_Type = TimeSlots
_AtmSuPortDs1CbrRxTimeSlots_Object = MibTableColumn
atmSuPortDs1CbrRxTimeSlots = _AtmSuPortDs1CbrRxTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 2, 2, 1, 2),
    _AtmSuPortDs1CbrRxTimeSlots_Type()
)
atmSuPortDs1CbrRxTimeSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortDs1CbrRxTimeSlots.setStatus("current")
_AtmSuPortDs1CbrTxTimeSlots_Type = TimeSlots
_AtmSuPortDs1CbrTxTimeSlots_Object = MibTableColumn
atmSuPortDs1CbrTxTimeSlots = _AtmSuPortDs1CbrTxTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 2, 2, 1, 3),
    _AtmSuPortDs1CbrTxTimeSlots_Type()
)
atmSuPortDs1CbrTxTimeSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortDs1CbrTxTimeSlots.setStatus("current")
_AtmSuPortDs1CbrMaxNoOfConns_Type = Integer32
_AtmSuPortDs1CbrMaxNoOfConns_Object = MibTableColumn
atmSuPortDs1CbrMaxNoOfConns = _AtmSuPortDs1CbrMaxNoOfConns_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 2, 2, 1, 4),
    _AtmSuPortDs1CbrMaxNoOfConns_Type()
)
atmSuPortDs1CbrMaxNoOfConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortDs1CbrMaxNoOfConns.setStatus("current")
_AtmSuPortDs1CbrConfNoOfConns_Type = Integer32
_AtmSuPortDs1CbrConfNoOfConns_Object = MibTableColumn
atmSuPortDs1CbrConfNoOfConns = _AtmSuPortDs1CbrConfNoOfConns_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 2, 2, 1, 5),
    _AtmSuPortDs1CbrConfNoOfConns_Type()
)
atmSuPortDs1CbrConfNoOfConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortDs1CbrConfNoOfConns.setStatus("current")


class _AtmSuPortDs1CbrSignallingSampleTime_Type(Integer32):
    """Custom type atmSuPortDs1CbrSignallingSampleTime based on Integer32"""
    defaultValue = 3

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
        *(("msec100", 1),
          ("msec1000", 4),
          ("msec1500", 5),
          ("msec200", 2),
          ("msec2000", 6),
          ("msec500", 3))
    )


_AtmSuPortDs1CbrSignallingSampleTime_Type.__name__ = "Integer32"
_AtmSuPortDs1CbrSignallingSampleTime_Object = MibTableColumn
atmSuPortDs1CbrSignallingSampleTime = _AtmSuPortDs1CbrSignallingSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 2, 2, 1, 6),
    _AtmSuPortDs1CbrSignallingSampleTime_Type()
)
atmSuPortDs1CbrSignallingSampleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortDs1CbrSignallingSampleTime.setStatus("current")
_AtmSuPortAtm_ObjectIdentity = ObjectIdentity
atmSuPortAtm = _AtmSuPortAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3)
)
_AtmSuPortAtmCnfgTable_Object = MibTable
atmSuPortAtmCnfgTable = _AtmSuPortAtmCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    atmSuPortAtmCnfgTable.setStatus("current")
_AtmSuPortAtmCnfgEntry_Object = MibTableRow
atmSuPortAtmCnfgEntry = _AtmSuPortAtmCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 1, 1)
)
atmSuPortAtmCnfgEntry.setIndexNames(
    (0, "ACE20-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmSuPortAtmCnfgEntry.setStatus("current")


class _AtmSuPortAtmCnfgIdleCellCLP_Type(Integer32):
    """Custom type atmSuPortAtmCnfgIdleCellCLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clp0", 1),
          ("clp1", 2))
    )


_AtmSuPortAtmCnfgIdleCellCLP_Type.__name__ = "Integer32"
_AtmSuPortAtmCnfgIdleCellCLP_Object = MibTableColumn
atmSuPortAtmCnfgIdleCellCLP = _AtmSuPortAtmCnfgIdleCellCLP_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 1, 1, 1),
    _AtmSuPortAtmCnfgIdleCellCLP_Type()
)
atmSuPortAtmCnfgIdleCellCLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortAtmCnfgIdleCellCLP.setStatus("current")


class _AtmSuPortAtmCnfgScramble_Type(Integer32):
    """Custom type atmSuPortAtmCnfgScramble based on Integer32"""
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


_AtmSuPortAtmCnfgScramble_Type.__name__ = "Integer32"
_AtmSuPortAtmCnfgScramble_Object = MibTableColumn
atmSuPortAtmCnfgScramble = _AtmSuPortAtmCnfgScramble_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 1, 1, 2),
    _AtmSuPortAtmCnfgScramble_Type()
)
atmSuPortAtmCnfgScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortAtmCnfgScramble.setStatus("current")
_AtmSuPortAtmSNMPVpi_Type = Integer32
_AtmSuPortAtmSNMPVpi_Object = MibTableColumn
atmSuPortAtmSNMPVpi = _AtmSuPortAtmSNMPVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 1, 1, 3),
    _AtmSuPortAtmSNMPVpi_Type()
)
atmSuPortAtmSNMPVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortAtmSNMPVpi.setStatus("current")
_AtmSuPortAtmSNMPVci_Type = Integer32
_AtmSuPortAtmSNMPVci_Object = MibTableColumn
atmSuPortAtmSNMPVci = _AtmSuPortAtmSNMPVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 1, 1, 4),
    _AtmSuPortAtmSNMPVci_Type()
)
atmSuPortAtmSNMPVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortAtmSNMPVci.setStatus("current")


class _AtmSuPortAtmSNMPStatus_Type(Integer32):
    """Custom type atmSuPortAtmSNMPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_AtmSuPortAtmSNMPStatus_Type.__name__ = "Integer32"
_AtmSuPortAtmSNMPStatus_Object = MibTableColumn
atmSuPortAtmSNMPStatus = _AtmSuPortAtmSNMPStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 1, 1, 5),
    _AtmSuPortAtmSNMPStatus_Type()
)
atmSuPortAtmSNMPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortAtmSNMPStatus.setStatus("current")


class _AtmSuPortAtmILMIStatus_Type(Integer32):
    """Custom type atmSuPortAtmILMIStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_AtmSuPortAtmILMIStatus_Type.__name__ = "Integer32"
_AtmSuPortAtmILMIStatus_Object = MibTableColumn
atmSuPortAtmILMIStatus = _AtmSuPortAtmILMIStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 1, 1, 6),
    _AtmSuPortAtmILMIStatus_Type()
)
atmSuPortAtmILMIStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortAtmILMIStatus.setStatus("current")
_AtmSuPortAtmSNMPIp_Type = IpAddress
_AtmSuPortAtmSNMPIp_Object = MibTableColumn
atmSuPortAtmSNMPIp = _AtmSuPortAtmSNMPIp_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 1, 1, 7),
    _AtmSuPortAtmSNMPIp_Type()
)
atmSuPortAtmSNMPIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortAtmSNMPIp.setStatus("current")


class _AtmSuPortAtmCnfgCDVOptimization_Type(Integer32):
    """Custom type atmSuPortAtmCnfgCDVOptimization based on Integer32"""
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
          ("enable", 3),
          ("notApplicable", 1))
    )


_AtmSuPortAtmCnfgCDVOptimization_Type.__name__ = "Integer32"
_AtmSuPortAtmCnfgCDVOptimization_Object = MibTableColumn
atmSuPortAtmCnfgCDVOptimization = _AtmSuPortAtmCnfgCDVOptimization_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 1, 1, 8),
    _AtmSuPortAtmCnfgCDVOptimization_Type()
)
atmSuPortAtmCnfgCDVOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortAtmCnfgCDVOptimization.setStatus("current")


class _AtmSuPortAtmCnfgShapingMode_Type(Integer32):
    """Custom type atmSuPortAtmCnfgShapingMode based on Integer32"""
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
        *(("hwNcits1", 3),
          ("hwNcits2", 4),
          ("notApplicable", 1),
          ("sw", 2))
    )


_AtmSuPortAtmCnfgShapingMode_Type.__name__ = "Integer32"
_AtmSuPortAtmCnfgShapingMode_Object = MibTableColumn
atmSuPortAtmCnfgShapingMode = _AtmSuPortAtmCnfgShapingMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 1, 1, 9),
    _AtmSuPortAtmCnfgShapingMode_Type()
)
atmSuPortAtmCnfgShapingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortAtmCnfgShapingMode.setStatus("current")
_AtmSuPortAtmSNMPTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_AtmSuPortAtmSNMPTrafficDescrIndex_Object = MibTableColumn
atmSuPortAtmSNMPTrafficDescrIndex = _AtmSuPortAtmSNMPTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 1, 1, 10),
    _AtmSuPortAtmSNMPTrafficDescrIndex_Type()
)
atmSuPortAtmSNMPTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortAtmSNMPTrafficDescrIndex.setStatus("current")
_AtmSuPortAtmIfStatsTable_Object = MibTable
atmSuPortAtmIfStatsTable = _AtmSuPortAtmIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 2)
)
if mibBuilder.loadTexts:
    atmSuPortAtmIfStatsTable.setStatus("current")
_AtmSuPortAtmIfStatsEntry_Object = MibTableRow
atmSuPortAtmIfStatsEntry = _AtmSuPortAtmIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 2, 1)
)
atmSuPortAtmIfStatsEntry.setIndexNames(
    (0, "ACE20-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmSuPortAtmIfStatsEntry.setStatus("current")
_AtmSuPortAtmRxClp0Cells_Type = Counter32
_AtmSuPortAtmRxClp0Cells_Object = MibTableColumn
atmSuPortAtmRxClp0Cells = _AtmSuPortAtmRxClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 2, 1, 1),
    _AtmSuPortAtmRxClp0Cells_Type()
)
atmSuPortAtmRxClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmRxClp0Cells.setStatus("current")
_AtmSuPortAtmRxClp1Cells_Type = Counter32
_AtmSuPortAtmRxClp1Cells_Object = MibTableColumn
atmSuPortAtmRxClp1Cells = _AtmSuPortAtmRxClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 2, 1, 2),
    _AtmSuPortAtmRxClp1Cells_Type()
)
atmSuPortAtmRxClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmRxClp1Cells.setStatus("current")
_AtmSuPortAtmRxEfciSetCells_Type = Counter32
_AtmSuPortAtmRxEfciSetCells_Object = MibTableColumn
atmSuPortAtmRxEfciSetCells = _AtmSuPortAtmRxEfciSetCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 2, 1, 3),
    _AtmSuPortAtmRxEfciSetCells_Type()
)
atmSuPortAtmRxEfciSetCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmRxEfciSetCells.setStatus("current")
_AtmSuPortAtmRxOamCells_Type = Counter32
_AtmSuPortAtmRxOamCells_Object = MibTableColumn
atmSuPortAtmRxOamCells = _AtmSuPortAtmRxOamCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 2, 1, 4),
    _AtmSuPortAtmRxOamCells_Type()
)
atmSuPortAtmRxOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmRxOamCells.setStatus("current")
_AtmSuPortAtmTxClp0Cells_Type = Counter32
_AtmSuPortAtmTxClp0Cells_Object = MibTableColumn
atmSuPortAtmTxClp0Cells = _AtmSuPortAtmTxClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 2, 1, 5),
    _AtmSuPortAtmTxClp0Cells_Type()
)
atmSuPortAtmTxClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmTxClp0Cells.setStatus("current")
_AtmSuPortAtmTxClp1Cells_Type = Counter32
_AtmSuPortAtmTxClp1Cells_Object = MibTableColumn
atmSuPortAtmTxClp1Cells = _AtmSuPortAtmTxClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 2, 1, 6),
    _AtmSuPortAtmTxClp1Cells_Type()
)
atmSuPortAtmTxClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmTxClp1Cells.setStatus("current")
_AtmSuPortAtmTxEfciSetCells_Type = Counter32
_AtmSuPortAtmTxEfciSetCells_Object = MibTableColumn
atmSuPortAtmTxEfciSetCells = _AtmSuPortAtmTxEfciSetCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 2, 1, 7),
    _AtmSuPortAtmTxEfciSetCells_Type()
)
atmSuPortAtmTxEfciSetCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmTxEfciSetCells.setStatus("current")
_AtmSuPortAtmTxOamCells_Type = Counter32
_AtmSuPortAtmTxOamCells_Object = MibTableColumn
atmSuPortAtmTxOamCells = _AtmSuPortAtmTxOamCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 2, 1, 8),
    _AtmSuPortAtmTxOamCells_Type()
)
atmSuPortAtmTxOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmTxOamCells.setStatus("current")
_AtmSuPortAtmVclStatsTable_Object = MibTable
atmSuPortAtmVclStatsTable = _AtmSuPortAtmVclStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 3)
)
if mibBuilder.loadTexts:
    atmSuPortAtmVclStatsTable.setStatus("current")
_AtmSuPortAtmVclStatsEntry_Object = MibTableRow
atmSuPortAtmVclStatsEntry = _AtmSuPortAtmVclStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 3, 1)
)
atmSuPortAtmVclStatsEntry.setIndexNames(
    (0, "ACE20-MIB", "ifIndex"),
    (0, "ACE20-MIB", "atmVclVpi"),
    (0, "ACE20-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    atmSuPortAtmVclStatsEntry.setStatus("current")
_AtmSuPortAtmVclStatsRxCells_Type = Counter32
_AtmSuPortAtmVclStatsRxCells_Object = MibTableColumn
atmSuPortAtmVclStatsRxCells = _AtmSuPortAtmVclStatsRxCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 3, 1, 1),
    _AtmSuPortAtmVclStatsRxCells_Type()
)
atmSuPortAtmVclStatsRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmVclStatsRxCells.setStatus("current")
_AtmSuPortAtmVclStatsRxClp0Cells_Type = Counter32
_AtmSuPortAtmVclStatsRxClp0Cells_Object = MibTableColumn
atmSuPortAtmVclStatsRxClp0Cells = _AtmSuPortAtmVclStatsRxClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 3, 1, 2),
    _AtmSuPortAtmVclStatsRxClp0Cells_Type()
)
atmSuPortAtmVclStatsRxClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmVclStatsRxClp0Cells.setStatus("current")
_AtmSuPortAtmVclStatsRxClp1Cells_Type = Counter32
_AtmSuPortAtmVclStatsRxClp1Cells_Object = MibTableColumn
atmSuPortAtmVclStatsRxClp1Cells = _AtmSuPortAtmVclStatsRxClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 3, 1, 3),
    _AtmSuPortAtmVclStatsRxClp1Cells_Type()
)
atmSuPortAtmVclStatsRxClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmVclStatsRxClp1Cells.setStatus("current")
_AtmSuPortAtmVclStatsRxDiscardsCells_Type = Counter32
_AtmSuPortAtmVclStatsRxDiscardsCells_Object = MibTableColumn
atmSuPortAtmVclStatsRxDiscardsCells = _AtmSuPortAtmVclStatsRxDiscardsCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 3, 1, 4),
    _AtmSuPortAtmVclStatsRxDiscardsCells_Type()
)
atmSuPortAtmVclStatsRxDiscardsCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmVclStatsRxDiscardsCells.setStatus("current")
_AtmSuPortAtmVclStatsTxCells_Type = Counter32
_AtmSuPortAtmVclStatsTxCells_Object = MibTableColumn
atmSuPortAtmVclStatsTxCells = _AtmSuPortAtmVclStatsTxCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 3, 1, 5),
    _AtmSuPortAtmVclStatsTxCells_Type()
)
atmSuPortAtmVclStatsTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmVclStatsTxCells.setStatus("current")
_AtmSuPortAtmVclStatsTxClp0Cells_Type = Counter32
_AtmSuPortAtmVclStatsTxClp0Cells_Object = MibTableColumn
atmSuPortAtmVclStatsTxClp0Cells = _AtmSuPortAtmVclStatsTxClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 3, 1, 6),
    _AtmSuPortAtmVclStatsTxClp0Cells_Type()
)
atmSuPortAtmVclStatsTxClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmVclStatsTxClp0Cells.setStatus("current")
_AtmSuPortAtmVclStatsTxClp1Cells_Type = Counter32
_AtmSuPortAtmVclStatsTxClp1Cells_Object = MibTableColumn
atmSuPortAtmVclStatsTxClp1Cells = _AtmSuPortAtmVclStatsTxClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 3, 1, 7),
    _AtmSuPortAtmVclStatsTxClp1Cells_Type()
)
atmSuPortAtmVclStatsTxClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmVclStatsTxClp1Cells.setStatus("current")
_AtmSuPortAtmVclStatsRxTotalAISCells_Type = Counter32
_AtmSuPortAtmVclStatsRxTotalAISCells_Object = MibTableColumn
atmSuPortAtmVclStatsRxTotalAISCells = _AtmSuPortAtmVclStatsRxTotalAISCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 3, 1, 8),
    _AtmSuPortAtmVclStatsRxTotalAISCells_Type()
)
atmSuPortAtmVclStatsRxTotalAISCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmVclStatsRxTotalAISCells.setStatus("current")
_AtmSuPortAtmVclStatsRxTotalCCCells_Type = Counter32
_AtmSuPortAtmVclStatsRxTotalCCCells_Object = MibTableColumn
atmSuPortAtmVclStatsRxTotalCCCells = _AtmSuPortAtmVclStatsRxTotalCCCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 3, 1, 9),
    _AtmSuPortAtmVclStatsRxTotalCCCells_Type()
)
atmSuPortAtmVclStatsRxTotalCCCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmVclStatsRxTotalCCCells.setStatus("current")
_AtmSuPortAtmVclStatsTotalSuccLoopbacks_Type = Counter32
_AtmSuPortAtmVclStatsTotalSuccLoopbacks_Object = MibTableColumn
atmSuPortAtmVclStatsTotalSuccLoopbacks = _AtmSuPortAtmVclStatsTotalSuccLoopbacks_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 3, 1, 10),
    _AtmSuPortAtmVclStatsTotalSuccLoopbacks_Type()
)
atmSuPortAtmVclStatsTotalSuccLoopbacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmVclStatsTotalSuccLoopbacks.setStatus("current")
_AtmSuPortAtmVclStatsTotalFailLoopbacks_Type = Counter32
_AtmSuPortAtmVclStatsTotalFailLoopbacks_Object = MibTableColumn
atmSuPortAtmVclStatsTotalFailLoopbacks = _AtmSuPortAtmVclStatsTotalFailLoopbacks_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 3, 1, 11),
    _AtmSuPortAtmVclStatsTotalFailLoopbacks_Type()
)
atmSuPortAtmVclStatsTotalFailLoopbacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmVclStatsTotalFailLoopbacks.setStatus("current")
_AtmSuPortAtmVclStatsRxTotalRDICells_Type = Counter32
_AtmSuPortAtmVclStatsRxTotalRDICells_Object = MibTableColumn
atmSuPortAtmVclStatsRxTotalRDICells = _AtmSuPortAtmVclStatsRxTotalRDICells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 3, 1, 12),
    _AtmSuPortAtmVclStatsRxTotalRDICells_Type()
)
atmSuPortAtmVclStatsRxTotalRDICells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmVclStatsRxTotalRDICells.setStatus("current")
_AtmSuPortAtmVclStatsTotalLOCSeconds_Type = Counter32
_AtmSuPortAtmVclStatsTotalLOCSeconds_Object = MibTableColumn
atmSuPortAtmVclStatsTotalLOCSeconds = _AtmSuPortAtmVclStatsTotalLOCSeconds_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 3, 1, 13),
    _AtmSuPortAtmVclStatsTotalLOCSeconds_Type()
)
atmSuPortAtmVclStatsTotalLOCSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmVclStatsTotalLOCSeconds.setStatus("current")
_AtmSuPortAtmVclStatsRxTotalLoopbackRequests_Type = Counter32
_AtmSuPortAtmVclStatsRxTotalLoopbackRequests_Object = MibTableColumn
atmSuPortAtmVclStatsRxTotalLoopbackRequests = _AtmSuPortAtmVclStatsRxTotalLoopbackRequests_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 3, 1, 14),
    _AtmSuPortAtmVclStatsRxTotalLoopbackRequests_Type()
)
atmSuPortAtmVclStatsRxTotalLoopbackRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmVclStatsRxTotalLoopbackRequests.setStatus("current")
_AtmSuPortAtmVclStatsTxTotalAISCells_Type = Counter32
_AtmSuPortAtmVclStatsTxTotalAISCells_Object = MibTableColumn
atmSuPortAtmVclStatsTxTotalAISCells = _AtmSuPortAtmVclStatsTxTotalAISCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 3, 1, 15),
    _AtmSuPortAtmVclStatsTxTotalAISCells_Type()
)
atmSuPortAtmVclStatsTxTotalAISCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmVclStatsTxTotalAISCells.setStatus("current")
_AtmSuPortAtmVclStatsTxTotalCCCells_Type = Counter32
_AtmSuPortAtmVclStatsTxTotalCCCells_Object = MibTableColumn
atmSuPortAtmVclStatsTxTotalCCCells = _AtmSuPortAtmVclStatsTxTotalCCCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 3, 1, 16),
    _AtmSuPortAtmVclStatsTxTotalCCCells_Type()
)
atmSuPortAtmVclStatsTxTotalCCCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmVclStatsTxTotalCCCells.setStatus("current")
_AtmSuPortAtmVclStatsTxTotalRDICells_Type = Counter32
_AtmSuPortAtmVclStatsTxTotalRDICells_Object = MibTableColumn
atmSuPortAtmVclStatsTxTotalRDICells = _AtmSuPortAtmVclStatsTxTotalRDICells_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 3, 1, 17),
    _AtmSuPortAtmVclStatsTxTotalRDICells_Type()
)
atmSuPortAtmVclStatsTxTotalRDICells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmVclStatsTxTotalRDICells.setStatus("current")
_AtmSuPortAtmVclStatsTxTotalLoopbackResponses_Type = Counter32
_AtmSuPortAtmVclStatsTxTotalLoopbackResponses_Object = MibTableColumn
atmSuPortAtmVclStatsTxTotalLoopbackResponses = _AtmSuPortAtmVclStatsTxTotalLoopbackResponses_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 3, 1, 18),
    _AtmSuPortAtmVclStatsTxTotalLoopbackResponses_Type()
)
atmSuPortAtmVclStatsTxTotalLoopbackResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmVclStatsTxTotalLoopbackResponses.setStatus("current")
_AtmSuPortAtmVclStatsTxTotalLoopbackRequests_Type = Counter32
_AtmSuPortAtmVclStatsTxTotalLoopbackRequests_Object = MibTableColumn
atmSuPortAtmVclStatsTxTotalLoopbackRequests = _AtmSuPortAtmVclStatsTxTotalLoopbackRequests_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 3, 1, 19),
    _AtmSuPortAtmVclStatsTxTotalLoopbackRequests_Type()
)
atmSuPortAtmVclStatsTxTotalLoopbackRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmVclStatsTxTotalLoopbackRequests.setStatus("current")
_AtmSuPortAtmVclStatsRxTotalLoopbackResponses_Type = Counter32
_AtmSuPortAtmVclStatsRxTotalLoopbackResponses_Object = MibTableColumn
atmSuPortAtmVclStatsRxTotalLoopbackResponses = _AtmSuPortAtmVclStatsRxTotalLoopbackResponses_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 3, 3, 1, 20),
    _AtmSuPortAtmVclStatsRxTotalLoopbackResponses_Type()
)
atmSuPortAtmVclStatsRxTotalLoopbackResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortAtmVclStatsRxTotalLoopbackResponses.setStatus("current")
_AtmSuPortFr_ObjectIdentity = ObjectIdentity
atmSuPortFr = _AtmSuPortFr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 4)
)
_AtmSuPortFrLportTable_Object = MibTable
atmSuPortFrLportTable = _AtmSuPortFrLportTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 4, 1)
)
if mibBuilder.loadTexts:
    atmSuPortFrLportTable.setStatus("current")
_AtmSuPortFrLportEntry_Object = MibTableRow
atmSuPortFrLportEntry = _AtmSuPortFrLportEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 4, 1, 1)
)
atmSuPortFrLportEntry.setIndexNames(
    (0, "ACE20-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmSuPortFrLportEntry.setStatus("current")
_AtmSuPortFrLportSNMPDlci_Type = Integer32
_AtmSuPortFrLportSNMPDlci_Object = MibTableColumn
atmSuPortFrLportSNMPDlci = _AtmSuPortFrLportSNMPDlci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 4, 1, 1, 1),
    _AtmSuPortFrLportSNMPDlci_Type()
)
atmSuPortFrLportSNMPDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortFrLportSNMPDlci.setStatus("current")


class _AtmSuPortFrLportSNMPStatus_Type(Integer32):
    """Custom type atmSuPortFrLportSNMPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_AtmSuPortFrLportSNMPStatus_Type.__name__ = "Integer32"
_AtmSuPortFrLportSNMPStatus_Object = MibTableColumn
atmSuPortFrLportSNMPStatus = _AtmSuPortFrLportSNMPStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 4, 1, 1, 2),
    _AtmSuPortFrLportSNMPStatus_Type()
)
atmSuPortFrLportSNMPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortFrLportSNMPStatus.setStatus("current")


class _AtmSuPortFrLportVCSigProtocol_Type(Integer32):
    """Custom type atmSuPortFrLportVCSigProtocol based on Integer32"""
    defaultValue = 1

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
        *(("ansiT1617D", 3),
          ("ccittQ933A", 2),
          ("lmi", 4),
          ("none", 1))
    )


_AtmSuPortFrLportVCSigProtocol_Type.__name__ = "Integer32"
_AtmSuPortFrLportVCSigProtocol_Object = MibTableColumn
atmSuPortFrLportVCSigProtocol = _AtmSuPortFrLportVCSigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 4, 1, 1, 3),
    _AtmSuPortFrLportVCSigProtocol_Type()
)
atmSuPortFrLportVCSigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortFrLportVCSigProtocol.setStatus("current")


class _AtmSuPortFrLportVCSigProcedure_Type(Integer32):
    """Custom type atmSuPortFrLportVCSigProcedure based on Integer32"""
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
        *(("bidirect", 4),
          ("notApplicable", 1),
          ("u2nnet", 2),
          ("u2nuser", 3))
    )


_AtmSuPortFrLportVCSigProcedure_Type.__name__ = "Integer32"
_AtmSuPortFrLportVCSigProcedure_Object = MibTableColumn
atmSuPortFrLportVCSigProcedure = _AtmSuPortFrLportVCSigProcedure_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 4, 1, 1, 4),
    _AtmSuPortFrLportVCSigProcedure_Type()
)
atmSuPortFrLportVCSigProcedure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortFrLportVCSigProcedure.setStatus("current")


class _AtmSuPortFrLportCLLM_Type(Integer32):
    """Custom type atmSuPortFrLportCLLM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_AtmSuPortFrLportCLLM_Type.__name__ = "Integer32"
_AtmSuPortFrLportCLLM_Object = MibTableColumn
atmSuPortFrLportCLLM = _AtmSuPortFrLportCLLM_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 4, 1, 1, 5),
    _AtmSuPortFrLportCLLM_Type()
)
atmSuPortFrLportCLLM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortFrLportCLLM.setStatus("current")
_AtmSuPortFrLportSNMPIp_Type = IpAddress
_AtmSuPortFrLportSNMPIp_Object = MibTableColumn
atmSuPortFrLportSNMPIp = _AtmSuPortFrLportSNMPIp_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 4, 1, 1, 6),
    _AtmSuPortFrLportSNMPIp_Type()
)
atmSuPortFrLportSNMPIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortFrLportSNMPIp.setStatus("current")
_AtmSuPortFrPvcEndptTable_Object = MibTable
atmSuPortFrPvcEndptTable = _AtmSuPortFrPvcEndptTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 4, 2)
)
if mibBuilder.loadTexts:
    atmSuPortFrPvcEndptTable.setStatus("current")
_AtmSuPortFrPvcEndptEntry_Object = MibTableRow
atmSuPortFrPvcEndptEntry = _AtmSuPortFrPvcEndptEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 4, 2, 1)
)
atmSuPortFrPvcEndptEntry.setIndexNames(
    (0, "ACE20-MIB", "ifIndex"),
    (0, "ACE20-MIB", "frPVCEndptDLCIIndex"),
)
if mibBuilder.loadTexts:
    atmSuPortFrPvcEndptEntry.setStatus("current")
_AtmSuPortFrPvcEndptTxFECNs_Type = Counter32
_AtmSuPortFrPvcEndptTxFECNs_Object = MibTableColumn
atmSuPortFrPvcEndptTxFECNs = _AtmSuPortFrPvcEndptTxFECNs_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 4, 2, 1, 1),
    _AtmSuPortFrPvcEndptTxFECNs_Type()
)
atmSuPortFrPvcEndptTxFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortFrPvcEndptTxFECNs.setStatus("current")
_AtmSuPortFrPvcEndptTxBECNs_Type = Counter32
_AtmSuPortFrPvcEndptTxBECNs_Object = MibTableColumn
atmSuPortFrPvcEndptTxBECNs = _AtmSuPortFrPvcEndptTxBECNs_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 4, 2, 1, 2),
    _AtmSuPortFrPvcEndptTxBECNs_Type()
)
atmSuPortFrPvcEndptTxBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortFrPvcEndptTxBECNs.setStatus("current")
_AtmSuPortFrPvcEndptTxDEs_Type = Counter32
_AtmSuPortFrPvcEndptTxDEs_Object = MibTableColumn
atmSuPortFrPvcEndptTxDEs = _AtmSuPortFrPvcEndptTxDEs_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 4, 2, 1, 3),
    _AtmSuPortFrPvcEndptTxDEs_Type()
)
atmSuPortFrPvcEndptTxDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortFrPvcEndptTxDEs.setStatus("current")
_AtmSuPortFrPvcEndptRxFECNs_Type = Counter32
_AtmSuPortFrPvcEndptRxFECNs_Object = MibTableColumn
atmSuPortFrPvcEndptRxFECNs = _AtmSuPortFrPvcEndptRxFECNs_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 4, 2, 1, 4),
    _AtmSuPortFrPvcEndptRxFECNs_Type()
)
atmSuPortFrPvcEndptRxFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortFrPvcEndptRxFECNs.setStatus("current")
_AtmSuPortFrPvcEndptRxBECNs_Type = Counter32
_AtmSuPortFrPvcEndptRxBECNs_Object = MibTableColumn
atmSuPortFrPvcEndptRxBECNs = _AtmSuPortFrPvcEndptRxBECNs_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 4, 2, 1, 5),
    _AtmSuPortFrPvcEndptRxBECNs_Type()
)
atmSuPortFrPvcEndptRxBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuPortFrPvcEndptRxBECNs.setStatus("current")
_AtmSuPortDxi_ObjectIdentity = ObjectIdentity
atmSuPortDxi = _AtmSuPortDxi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 5)
)
_AtmSuPortDxiConfTable_Object = MibTable
atmSuPortDxiConfTable = _AtmSuPortDxiConfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 5, 1)
)
if mibBuilder.loadTexts:
    atmSuPortDxiConfTable.setStatus("current")
_AtmSuPortDxiConfEntry_Object = MibTableRow
atmSuPortDxiConfEntry = _AtmSuPortDxiConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 5, 1, 1)
)
atmSuPortDxiConfEntry.setIndexNames(
    (0, "ACE20-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmSuPortDxiConfEntry.setStatus("current")


class _AtmSuPortDxiPortMode_Type(Integer32):
    """Custom type atmSuPortDxiPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mode1a", 1),
          ("mode1b", 2),
          ("mode2", 3))
    )


_AtmSuPortDxiPortMode_Type.__name__ = "Integer32"
_AtmSuPortDxiPortMode_Object = MibTableColumn
atmSuPortDxiPortMode = _AtmSuPortDxiPortMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 5, 1, 1, 1),
    _AtmSuPortDxiPortMode_Type()
)
atmSuPortDxiPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortDxiPortMode.setStatus("current")


class _AtmSuPortDxiSigProtocol_Type(Integer32):
    """Custom type atmSuPortDxiSigProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lmi", 2),
          ("none", 1))
    )


_AtmSuPortDxiSigProtocol_Type.__name__ = "Integer32"
_AtmSuPortDxiSigProtocol_Object = MibTableColumn
atmSuPortDxiSigProtocol = _AtmSuPortDxiSigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 5, 1, 1, 2),
    _AtmSuPortDxiSigProtocol_Type()
)
atmSuPortDxiSigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortDxiSigProtocol.setStatus("current")


class _AtmSuPortDxiSigDfa_Type(Integer32):
    """Custom type atmSuPortDxiSigDfa based on Integer32"""
    defaultValue = 0


_AtmSuPortDxiSigDfa_Object = MibTableColumn
atmSuPortDxiSigDfa = _AtmSuPortDxiSigDfa_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 5, 1, 1, 3),
    _AtmSuPortDxiSigDfa_Type()
)
atmSuPortDxiSigDfa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortDxiSigDfa.setStatus("current")
_AtmSuPortCmdTable_Object = MibTable
atmSuPortCmdTable = _AtmSuPortCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 6)
)
if mibBuilder.loadTexts:
    atmSuPortCmdTable.setStatus("current")
_AtmSuPortCmdEntry_Object = MibTableRow
atmSuPortCmdEntry = _AtmSuPortCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 6, 1)
)
atmSuPortCmdEntry.setIndexNames(
    (0, "ACE20-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmSuPortCmdEntry.setStatus("current")


class _AtmSuResetPortStatsCmd_Type(Integer32):
    """Custom type atmSuResetPortStatsCmd based on Integer32"""
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


_AtmSuResetPortStatsCmd_Type.__name__ = "Integer32"
_AtmSuResetPortStatsCmd_Object = MibTableColumn
atmSuResetPortStatsCmd = _AtmSuResetPortStatsCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 6, 1, 1),
    _AtmSuResetPortStatsCmd_Type()
)
atmSuResetPortStatsCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuResetPortStatsCmd.setStatus("current")


class _AtmSuResetConnsStatsCmd_Type(Integer32):
    """Custom type atmSuResetConnsStatsCmd based on Integer32"""
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


_AtmSuResetConnsStatsCmd_Type.__name__ = "Integer32"
_AtmSuResetConnsStatsCmd_Object = MibTableColumn
atmSuResetConnsStatsCmd = _AtmSuResetConnsStatsCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 6, 1, 2),
    _AtmSuResetConnsStatsCmd_Type()
)
atmSuResetConnsStatsCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuResetConnsStatsCmd.setStatus("current")
_AtmSuPortEther_ObjectIdentity = ObjectIdentity
atmSuPortEther = _AtmSuPortEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 7)
)
_AtmSuPortEtherTable_Object = MibTable
atmSuPortEtherTable = _AtmSuPortEtherTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 7, 1)
)
if mibBuilder.loadTexts:
    atmSuPortEtherTable.setStatus("current")
_AtmSuPortEtherEntry_Object = MibTableRow
atmSuPortEtherEntry = _AtmSuPortEtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 7, 1, 1)
)
atmSuPortEtherEntry.setIndexNames(
    (0, "ACE20-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmSuPortEtherEntry.setStatus("current")
_AtmSuPortEtherIP_Type = IpAddress
_AtmSuPortEtherIP_Object = MibTableColumn
atmSuPortEtherIP = _AtmSuPortEtherIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 7, 1, 1, 1),
    _AtmSuPortEtherIP_Type()
)
atmSuPortEtherIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortEtherIP.setStatus("current")
_AtmSuPortEtherMask_Type = IpAddress
_AtmSuPortEtherMask_Object = MibTableColumn
atmSuPortEtherMask = _AtmSuPortEtherMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 7, 1, 1, 2),
    _AtmSuPortEtherMask_Type()
)
atmSuPortEtherMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortEtherMask.setStatus("current")
_AtmSuPortEtherDefaultGateWayIp_Type = IpAddress
_AtmSuPortEtherDefaultGateWayIp_Object = MibTableColumn
atmSuPortEtherDefaultGateWayIp = _AtmSuPortEtherDefaultGateWayIp_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 7, 1, 1, 3),
    _AtmSuPortEtherDefaultGateWayIp_Type()
)
atmSuPortEtherDefaultGateWayIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortEtherDefaultGateWayIp.setStatus("current")
_AtmSuPortEtherDefaultCrossConnectId_Type = Integer32
_AtmSuPortEtherDefaultCrossConnectId_Object = MibTableColumn
atmSuPortEtherDefaultCrossConnectId = _AtmSuPortEtherDefaultCrossConnectId_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 7, 1, 1, 4),
    _AtmSuPortEtherDefaultCrossConnectId_Type()
)
atmSuPortEtherDefaultCrossConnectId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortEtherDefaultCrossConnectId.setStatus("current")


class _AtmSuPortEtherDefaultGatewayStatus_Type(Integer32):
    """Custom type atmSuPortEtherDefaultGatewayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2),
          ("notApplicable", 255))
    )


_AtmSuPortEtherDefaultGatewayStatus_Type.__name__ = "Integer32"
_AtmSuPortEtherDefaultGatewayStatus_Object = MibTableColumn
atmSuPortEtherDefaultGatewayStatus = _AtmSuPortEtherDefaultGatewayStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 7, 1, 1, 5),
    _AtmSuPortEtherDefaultGatewayStatus_Type()
)
atmSuPortEtherDefaultGatewayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortEtherDefaultGatewayStatus.setStatus("current")


class _AtmSuPortEtherSNMPStatus_Type(Integer32):
    """Custom type atmSuPortEtherSNMPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2),
          ("notApplicable", 255))
    )


_AtmSuPortEtherSNMPStatus_Type.__name__ = "Integer32"
_AtmSuPortEtherSNMPStatus_Object = MibTableColumn
atmSuPortEtherSNMPStatus = _AtmSuPortEtherSNMPStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 7, 1, 1, 6),
    _AtmSuPortEtherSNMPStatus_Type()
)
atmSuPortEtherSNMPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortEtherSNMPStatus.setStatus("current")


class _AtmSuPortEtherFragmentation_Type(Integer32):
    """Custom type atmSuPortEtherFragmentation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("notApplicable", 255),
          ("yes", 3))
    )


_AtmSuPortEtherFragmentation_Type.__name__ = "Integer32"
_AtmSuPortEtherFragmentation_Object = MibTableColumn
atmSuPortEtherFragmentation = _AtmSuPortEtherFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 7, 1, 1, 7),
    _AtmSuPortEtherFragmentation_Type()
)
atmSuPortEtherFragmentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortEtherFragmentation.setStatus("current")


class _AtmSuPortEtherRIPMode_Type(Integer32):
    """Custom type atmSuPortEtherRIPMode based on Integer32"""
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
        *(("none", 4),
          ("notApplicable", 255),
          ("rip1", 1),
          ("rip1And2", 3),
          ("rip2", 2))
    )


_AtmSuPortEtherRIPMode_Type.__name__ = "Integer32"
_AtmSuPortEtherRIPMode_Object = MibTableColumn
atmSuPortEtherRIPMode = _AtmSuPortEtherRIPMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 7, 1, 1, 8),
    _AtmSuPortEtherRIPMode_Type()
)
atmSuPortEtherRIPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortEtherRIPMode.setStatus("current")


class _AtmSuPortEtherBridgingMode_Type(Integer32):
    """Custom type atmSuPortEtherBridgingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("accessAndSwitching", 2),
          ("accessOnly", 1),
          ("notApplicable", 255))
    )


_AtmSuPortEtherBridgingMode_Type.__name__ = "Integer32"
_AtmSuPortEtherBridgingMode_Object = MibTableColumn
atmSuPortEtherBridgingMode = _AtmSuPortEtherBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 7, 1, 1, 9),
    _AtmSuPortEtherBridgingMode_Type()
)
atmSuPortEtherBridgingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortEtherBridgingMode.setStatus("current")


class _AtmSuPortEtherARPTimeout_Type(Integer32):
    """Custom type atmSuPortEtherARPTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AtmSuPortEtherARPTimeout_Type.__name__ = "Integer32"
_AtmSuPortEtherARPTimeout_Object = MibTableColumn
atmSuPortEtherARPTimeout = _AtmSuPortEtherARPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 7, 1, 1, 10),
    _AtmSuPortEtherARPTimeout_Type()
)
atmSuPortEtherARPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortEtherARPTimeout.setStatus("current")


class _AtmSuPortEtherAgingTime_Type(Integer32):
    """Custom type atmSuPortEtherAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_AtmSuPortEtherAgingTime_Type.__name__ = "Integer32"
_AtmSuPortEtherAgingTime_Object = MibTableColumn
atmSuPortEtherAgingTime = _AtmSuPortEtherAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 7, 1, 1, 11),
    _AtmSuPortEtherAgingTime_Type()
)
atmSuPortEtherAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortEtherAgingTime.setStatus("current")


class _AtmSuPortEtherPppOEEnable_Type(Integer32):
    """Custom type atmSuPortEtherPppOEEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("off", 2),
          ("on", 3))
    )


_AtmSuPortEtherPppOEEnable_Type.__name__ = "Integer32"
_AtmSuPortEtherPppOEEnable_Object = MibTableColumn
atmSuPortEtherPppOEEnable = _AtmSuPortEtherPppOEEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 7, 1, 1, 12),
    _AtmSuPortEtherPppOEEnable_Type()
)
atmSuPortEtherPppOEEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortEtherPppOEEnable.setStatus("current")


class _AtmSuPortEtherStatus_Type(Integer32):
    """Custom type atmSuPortEtherStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_AtmSuPortEtherStatus_Type.__name__ = "Integer32"
_AtmSuPortEtherStatus_Object = MibTableColumn
atmSuPortEtherStatus = _AtmSuPortEtherStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 2, 7, 1, 1, 13),
    _AtmSuPortEtherStatus_Type()
)
atmSuPortEtherStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSuPortEtherStatus.setStatus("current")
_AtmSuCrossConnect_ObjectIdentity = ObjectIdentity
atmSuCrossConnect = _AtmSuCrossConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3)
)
_AtmSuCrossConnectAtmFr_ObjectIdentity = ObjectIdentity
atmSuCrossConnectAtmFr = _AtmSuCrossConnectAtmFr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1)
)
_AtmSuCrossConnectAtmFrDescriptor_ObjectIdentity = ObjectIdentity
atmSuCrossConnectAtmFrDescriptor = _AtmSuCrossConnectAtmFrDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 1)
)
_AtmFrCrossConnectNetwork_ObjectIdentity = ObjectIdentity
atmFrCrossConnectNetwork = _AtmFrCrossConnectNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 1, 1)
)
_AtmFrCrossConnectService_ObjectIdentity = ObjectIdentity
atmFrCrossConnectService = _AtmFrCrossConnectService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 1, 2)
)
_AtmFrDescrTable_Object = MibTable
atmFrDescrTable = _AtmFrDescrTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 2)
)
if mibBuilder.loadTexts:
    atmFrDescrTable.setStatus("current")
_AtmFrDescrEntry_Object = MibTableRow
atmFrDescrEntry = _AtmFrDescrEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 2, 1)
)
atmFrDescrEntry.setIndexNames(
    (0, "ACE20-MIB", "atmFrDescrIndex"),
)
if mibBuilder.loadTexts:
    atmFrDescrEntry.setStatus("current")
_AtmFrDescrIndex_Type = Integer32
_AtmFrDescrIndex_Object = MibTableColumn
atmFrDescrIndex = _AtmFrDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 2, 1, 1),
    _AtmFrDescrIndex_Type()
)
atmFrDescrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmFrDescrIndex.setStatus("current")
_AtmFrDescrType_Type = ObjectIdentifier
_AtmFrDescrType_Object = MibTableColumn
atmFrDescrType = _AtmFrDescrType_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 2, 1, 2),
    _AtmFrDescrType_Type()
)
atmFrDescrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmFrDescrType.setStatus("current")


class _AtmFrDescrClp2De_Type(Integer32):
    """Custom type atmFrDescrClp2De based on Integer32"""
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
        *(("always0", 3),
          ("always1", 4),
          ("conv", 2),
          ("convSscs", 1))
    )


_AtmFrDescrClp2De_Type.__name__ = "Integer32"
_AtmFrDescrClp2De_Object = MibTableColumn
atmFrDescrClp2De = _AtmFrDescrClp2De_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 2, 1, 3),
    _AtmFrDescrClp2De_Type()
)
atmFrDescrClp2De.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmFrDescrClp2De.setStatus("current")


class _AtmFrDescrDe2Clp_Type(Integer32):
    """Custom type atmFrDescrDe2Clp based on Integer32"""
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
        *(("always0", 2),
          ("always1", 3),
          ("conv", 1))
    )


_AtmFrDescrDe2Clp_Type.__name__ = "Integer32"
_AtmFrDescrDe2Clp_Object = MibTableColumn
atmFrDescrDe2Clp = _AtmFrDescrDe2Clp_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 2, 1, 4),
    _AtmFrDescrDe2Clp_Type()
)
atmFrDescrDe2Clp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmFrDescrDe2Clp.setStatus("current")


class _AtmFrDescrFecn2Efci_Type(Integer32):
    """Custom type atmFrDescrFecn2Efci based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always0", 2),
          ("conv", 1))
    )


_AtmFrDescrFecn2Efci_Type.__name__ = "Integer32"
_AtmFrDescrFecn2Efci_Object = MibTableColumn
atmFrDescrFecn2Efci = _AtmFrDescrFecn2Efci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 2, 1, 5),
    _AtmFrDescrFecn2Efci_Type()
)
atmFrDescrFecn2Efci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmFrDescrFecn2Efci.setStatus("current")


class _AtmFrDescrMappingMode_Type(Integer32):
    """Custom type atmFrDescrMappingMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("translation", 2),
          ("transparent", 1))
    )


_AtmFrDescrMappingMode_Type.__name__ = "Integer32"
_AtmFrDescrMappingMode_Object = MibTableColumn
atmFrDescrMappingMode = _AtmFrDescrMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 2, 1, 6),
    _AtmFrDescrMappingMode_Type()
)
atmFrDescrMappingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmFrDescrMappingMode.setStatus("current")


class _AtmFrDescrRowStatus_Type(RowStatus):
    """Custom type atmFrDescrRowStatus based on RowStatus"""


_AtmFrDescrRowStatus_Object = MibTableColumn
atmFrDescrRowStatus = _AtmFrDescrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 2, 1, 7),
    _AtmFrDescrRowStatus_Type()
)
atmFrDescrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmFrDescrRowStatus.setStatus("current")
_AtmSuCrossConnectAtmFrIndexNext_Type = Integer32
_AtmSuCrossConnectAtmFrIndexNext_Object = MibScalar
atmSuCrossConnectAtmFrIndexNext = _AtmSuCrossConnectAtmFrIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 3),
    _AtmSuCrossConnectAtmFrIndexNext_Type()
)
atmSuCrossConnectAtmFrIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuCrossConnectAtmFrIndexNext.setStatus("current")
_AtmFrCnfgTable_Object = MibTable
atmFrCnfgTable = _AtmFrCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 4)
)
if mibBuilder.loadTexts:
    atmFrCnfgTable.setStatus("current")
_AtmFrCnfgEntry_Object = MibTableRow
atmFrCnfgEntry = _AtmFrCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 4, 1)
)
atmFrCnfgEntry.setIndexNames(
    (0, "ACE20-MIB", "atmFrCnfgCrossConnectIndex"),
    (0, "ACE20-MIB", "atmFrCnfgAtmIfIndex"),
    (0, "ACE20-MIB", "atmFrCnfgAtmVpi"),
    (0, "ACE20-MIB", "atmFrCnfgAtmVci"),
    (0, "ACE20-MIB", "atmFrCnfgFrIfIndex"),
    (0, "ACE20-MIB", "atmFrCnfgDlci"),
)
if mibBuilder.loadTexts:
    atmFrCnfgEntry.setStatus("current")
_AtmFrCnfgCrossConnectIndex_Type = Integer32
_AtmFrCnfgCrossConnectIndex_Object = MibTableColumn
atmFrCnfgCrossConnectIndex = _AtmFrCnfgCrossConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 4, 1, 1),
    _AtmFrCnfgCrossConnectIndex_Type()
)
atmFrCnfgCrossConnectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmFrCnfgCrossConnectIndex.setStatus("current")
_AtmFrCnfgAtmIfIndex_Type = Integer32
_AtmFrCnfgAtmIfIndex_Object = MibTableColumn
atmFrCnfgAtmIfIndex = _AtmFrCnfgAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 4, 1, 2),
    _AtmFrCnfgAtmIfIndex_Type()
)
atmFrCnfgAtmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmFrCnfgAtmIfIndex.setStatus("current")


class _AtmFrCnfgAtmVpi_Type(Integer32):
    """Custom type atmFrCnfgAtmVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AtmFrCnfgAtmVpi_Type.__name__ = "Integer32"
_AtmFrCnfgAtmVpi_Object = MibTableColumn
atmFrCnfgAtmVpi = _AtmFrCnfgAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 4, 1, 3),
    _AtmFrCnfgAtmVpi_Type()
)
atmFrCnfgAtmVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmFrCnfgAtmVpi.setStatus("current")


class _AtmFrCnfgAtmVci_Type(Integer32):
    """Custom type atmFrCnfgAtmVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmFrCnfgAtmVci_Type.__name__ = "Integer32"
_AtmFrCnfgAtmVci_Object = MibTableColumn
atmFrCnfgAtmVci = _AtmFrCnfgAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 4, 1, 4),
    _AtmFrCnfgAtmVci_Type()
)
atmFrCnfgAtmVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmFrCnfgAtmVci.setStatus("current")
_AtmFrCnfgFrIfIndex_Type = Integer32
_AtmFrCnfgFrIfIndex_Object = MibTableColumn
atmFrCnfgFrIfIndex = _AtmFrCnfgFrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 4, 1, 5),
    _AtmFrCnfgFrIfIndex_Type()
)
atmFrCnfgFrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmFrCnfgFrIfIndex.setStatus("current")
_AtmFrCnfgDlci_Type = Integer32
_AtmFrCnfgDlci_Object = MibTableColumn
atmFrCnfgDlci = _AtmFrCnfgDlci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 4, 1, 6),
    _AtmFrCnfgDlci_Type()
)
atmFrCnfgDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmFrCnfgDlci.setStatus("current")


class _AtmFrCnfgAdminStatus_Type(Integer32):
    """Custom type atmFrCnfgAdminStatus based on Integer32"""
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


_AtmFrCnfgAdminStatus_Type.__name__ = "Integer32"
_AtmFrCnfgAdminStatus_Object = MibTableColumn
atmFrCnfgAdminStatus = _AtmFrCnfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 4, 1, 7),
    _AtmFrCnfgAdminStatus_Type()
)
atmFrCnfgAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmFrCnfgAdminStatus.setStatus("current")


class _AtmFrCnfgOperStatus_Type(Integer32):
    """Custom type atmFrCnfgOperStatus based on Integer32"""
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


_AtmFrCnfgOperStatus_Type.__name__ = "Integer32"
_AtmFrCnfgOperStatus_Object = MibTableColumn
atmFrCnfgOperStatus = _AtmFrCnfgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 4, 1, 8),
    _AtmFrCnfgOperStatus_Type()
)
atmFrCnfgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmFrCnfgOperStatus.setStatus("current")
_AtmFrCnfgLastChange_Type = TimeStamp
_AtmFrCnfgLastChange_Object = MibTableColumn
atmFrCnfgLastChange = _AtmFrCnfgLastChange_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 4, 1, 9),
    _AtmFrCnfgLastChange_Type()
)
atmFrCnfgLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmFrCnfgLastChange.setStatus("current")
_AtmFrCnfgMappingDescrIndex_Type = Integer32
_AtmFrCnfgMappingDescrIndex_Object = MibTableColumn
atmFrCnfgMappingDescrIndex = _AtmFrCnfgMappingDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 4, 1, 10),
    _AtmFrCnfgMappingDescrIndex_Type()
)
atmFrCnfgMappingDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmFrCnfgMappingDescrIndex.setStatus("current")
_AtmFrCnfgSscsDlci_Type = Integer32
_AtmFrCnfgSscsDlci_Object = MibTableColumn
atmFrCnfgSscsDlci = _AtmFrCnfgSscsDlci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 4, 1, 11),
    _AtmFrCnfgSscsDlci_Type()
)
atmFrCnfgSscsDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmFrCnfgSscsDlci.setStatus("current")
_AtmFrCnfgTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_AtmFrCnfgTrafficDescrIndex_Object = MibTableColumn
atmFrCnfgTrafficDescrIndex = _AtmFrCnfgTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 4, 1, 12),
    _AtmFrCnfgTrafficDescrIndex_Type()
)
atmFrCnfgTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmFrCnfgTrafficDescrIndex.setStatus("current")


class _AtmFrCnfgPriority_Type(Integer32):
    """Custom type atmFrCnfgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("highPriority", 1),
          ("lowPriority", 3),
          ("mediumPriority", 2))
    )


_AtmFrCnfgPriority_Type.__name__ = "Integer32"
_AtmFrCnfgPriority_Object = MibTableColumn
atmFrCnfgPriority = _AtmFrCnfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 4, 1, 13),
    _AtmFrCnfgPriority_Type()
)
atmFrCnfgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmFrCnfgPriority.setStatus("current")
_AtmFrCnfgRowStatus_Type = RowStatus
_AtmFrCnfgRowStatus_Object = MibTableColumn
atmFrCnfgRowStatus = _AtmFrCnfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 4, 1, 14),
    _AtmFrCnfgRowStatus_Type()
)
atmFrCnfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmFrCnfgRowStatus.setStatus("current")


class _AtmFrCnfgAllocatedBuffers_Type(Integer32):
    """Custom type atmFrCnfgAllocatedBuffers based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 217),
    )


_AtmFrCnfgAllocatedBuffers_Type.__name__ = "Integer32"
_AtmFrCnfgAllocatedBuffers_Object = MibTableColumn
atmFrCnfgAllocatedBuffers = _AtmFrCnfgAllocatedBuffers_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 4, 1, 15),
    _AtmFrCnfgAllocatedBuffers_Type()
)
atmFrCnfgAllocatedBuffers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmFrCnfgAllocatedBuffers.setStatus("current")
_AtmFrMaxMany2OneConnsPerVcc_Type = Integer32
_AtmFrMaxMany2OneConnsPerVcc_Object = MibScalar
atmFrMaxMany2OneConnsPerVcc = _AtmFrMaxMany2OneConnsPerVcc_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 1, 5),
    _AtmFrMaxMany2OneConnsPerVcc_Type()
)
atmFrMaxMany2OneConnsPerVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmFrMaxMany2OneConnsPerVcc.setStatus("current")
_AtmSuCrossConnectAtmDxi_ObjectIdentity = ObjectIdentity
atmSuCrossConnectAtmDxi = _AtmSuCrossConnectAtmDxi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 2)
)
_AtmSuCrossConnectAtmDxiIndexNext_Type = Integer32
_AtmSuCrossConnectAtmDxiIndexNext_Object = MibScalar
atmSuCrossConnectAtmDxiIndexNext = _AtmSuCrossConnectAtmDxiIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 2, 1),
    _AtmSuCrossConnectAtmDxiIndexNext_Type()
)
atmSuCrossConnectAtmDxiIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuCrossConnectAtmDxiIndexNext.setStatus("current")
_AtmDxiCnfgTable_Object = MibTable
atmDxiCnfgTable = _AtmDxiCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 2, 2)
)
if mibBuilder.loadTexts:
    atmDxiCnfgTable.setStatus("current")
_AtmDxiCnfgEntry_Object = MibTableRow
atmDxiCnfgEntry = _AtmDxiCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 2, 2, 1)
)
atmDxiCnfgEntry.setIndexNames(
    (0, "ACE20-MIB", "atmDxiCnfgCrossConnectIndex"),
    (0, "ACE20-MIB", "atmDxiCnfgAtmIfIndex"),
    (0, "ACE20-MIB", "atmDxiCnfgAtmVpi"),
    (0, "ACE20-MIB", "atmDxiCnfgAtmVci"),
    (0, "ACE20-MIB", "atmDxiCnfgDxiIfIndex"),
    (0, "ACE20-MIB", "atmDxiCnfgDfa"),
)
if mibBuilder.loadTexts:
    atmDxiCnfgEntry.setStatus("current")
_AtmDxiCnfgCrossConnectIndex_Type = Integer32
_AtmDxiCnfgCrossConnectIndex_Object = MibTableColumn
atmDxiCnfgCrossConnectIndex = _AtmDxiCnfgCrossConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 2, 2, 1, 1),
    _AtmDxiCnfgCrossConnectIndex_Type()
)
atmDxiCnfgCrossConnectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiCnfgCrossConnectIndex.setStatus("current")
_AtmDxiCnfgAtmIfIndex_Type = Integer32
_AtmDxiCnfgAtmIfIndex_Object = MibTableColumn
atmDxiCnfgAtmIfIndex = _AtmDxiCnfgAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 2, 2, 1, 2),
    _AtmDxiCnfgAtmIfIndex_Type()
)
atmDxiCnfgAtmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiCnfgAtmIfIndex.setStatus("current")


class _AtmDxiCnfgAtmVpi_Type(Integer32):
    """Custom type atmDxiCnfgAtmVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AtmDxiCnfgAtmVpi_Type.__name__ = "Integer32"
_AtmDxiCnfgAtmVpi_Object = MibTableColumn
atmDxiCnfgAtmVpi = _AtmDxiCnfgAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 2, 2, 1, 3),
    _AtmDxiCnfgAtmVpi_Type()
)
atmDxiCnfgAtmVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiCnfgAtmVpi.setStatus("current")


class _AtmDxiCnfgAtmVci_Type(Integer32):
    """Custom type atmDxiCnfgAtmVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmDxiCnfgAtmVci_Type.__name__ = "Integer32"
_AtmDxiCnfgAtmVci_Object = MibTableColumn
atmDxiCnfgAtmVci = _AtmDxiCnfgAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 2, 2, 1, 4),
    _AtmDxiCnfgAtmVci_Type()
)
atmDxiCnfgAtmVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiCnfgAtmVci.setStatus("current")
_AtmDxiCnfgDxiIfIndex_Type = Integer32
_AtmDxiCnfgDxiIfIndex_Object = MibTableColumn
atmDxiCnfgDxiIfIndex = _AtmDxiCnfgDxiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 2, 2, 1, 5),
    _AtmDxiCnfgDxiIfIndex_Type()
)
atmDxiCnfgDxiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiCnfgDxiIfIndex.setStatus("current")
_AtmDxiCnfgDfa_Type = Integer32
_AtmDxiCnfgDfa_Object = MibTableColumn
atmDxiCnfgDfa = _AtmDxiCnfgDfa_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 2, 2, 1, 6),
    _AtmDxiCnfgDfa_Type()
)
atmDxiCnfgDfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiCnfgDfa.setStatus("current")


class _AtmDxiCnfgAdminStatus_Type(Integer32):
    """Custom type atmDxiCnfgAdminStatus based on Integer32"""
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


_AtmDxiCnfgAdminStatus_Type.__name__ = "Integer32"
_AtmDxiCnfgAdminStatus_Object = MibTableColumn
atmDxiCnfgAdminStatus = _AtmDxiCnfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 2, 2, 1, 7),
    _AtmDxiCnfgAdminStatus_Type()
)
atmDxiCnfgAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmDxiCnfgAdminStatus.setStatus("current")


class _AtmDxiCnfgOperStatus_Type(Integer32):
    """Custom type atmDxiCnfgOperStatus based on Integer32"""
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


_AtmDxiCnfgOperStatus_Type.__name__ = "Integer32"
_AtmDxiCnfgOperStatus_Object = MibTableColumn
atmDxiCnfgOperStatus = _AtmDxiCnfgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 2, 2, 1, 8),
    _AtmDxiCnfgOperStatus_Type()
)
atmDxiCnfgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiCnfgOperStatus.setStatus("current")
_AtmDxiCnfgLastChange_Type = TimeStamp
_AtmDxiCnfgLastChange_Object = MibTableColumn
atmDxiCnfgLastChange = _AtmDxiCnfgLastChange_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 2, 2, 1, 9),
    _AtmDxiCnfgLastChange_Type()
)
atmDxiCnfgLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiCnfgLastChange.setStatus("current")
_AtmDxiCnfgTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_AtmDxiCnfgTrafficDescrIndex_Object = MibTableColumn
atmDxiCnfgTrafficDescrIndex = _AtmDxiCnfgTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 2, 2, 1, 10),
    _AtmDxiCnfgTrafficDescrIndex_Type()
)
atmDxiCnfgTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmDxiCnfgTrafficDescrIndex.setStatus("current")


class _AtmDxiCnfgPriority_Type(Integer32):
    """Custom type atmDxiCnfgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("highPriority", 1),
          ("lowPriority", 3),
          ("mediumPriority", 2))
    )


_AtmDxiCnfgPriority_Type.__name__ = "Integer32"
_AtmDxiCnfgPriority_Object = MibTableColumn
atmDxiCnfgPriority = _AtmDxiCnfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 2, 2, 1, 11),
    _AtmDxiCnfgPriority_Type()
)
atmDxiCnfgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmDxiCnfgPriority.setStatus("current")
_AtmDxiCnfgRowStatus_Type = RowStatus
_AtmDxiCnfgRowStatus_Object = MibTableColumn
atmDxiCnfgRowStatus = _AtmDxiCnfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 2, 2, 1, 12),
    _AtmDxiCnfgRowStatus_Type()
)
atmDxiCnfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmDxiCnfgRowStatus.setStatus("current")
_AtmSuAtmCbr_ObjectIdentity = ObjectIdentity
atmSuAtmCbr = _AtmSuAtmCbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3)
)
_AtmCbrCnfgTable_Object = MibTable
atmCbrCnfgTable = _AtmCbrCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 1)
)
if mibBuilder.loadTexts:
    atmCbrCnfgTable.setStatus("current")
_AtmCbrCnfgEntry_Object = MibTableRow
atmCbrCnfgEntry = _AtmCbrCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 1, 1)
)
atmCbrCnfgEntry.setIndexNames(
    (0, "ACE20-MIB", "atmCbrCnfgAtmIfIndex"),
    (0, "ACE20-MIB", "atmCbrCnfgAtmVpi"),
    (0, "ACE20-MIB", "atmCbrCnfgAtmVci"),
    (0, "ACE20-MIB", "atmCbrCnfgCbrIfIndex"),
)
if mibBuilder.loadTexts:
    atmCbrCnfgEntry.setStatus("current")
_AtmCbrCnfgAtmIfIndex_Type = Integer32
_AtmCbrCnfgAtmIfIndex_Object = MibTableColumn
atmCbrCnfgAtmIfIndex = _AtmCbrCnfgAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 1, 1, 1),
    _AtmCbrCnfgAtmIfIndex_Type()
)
atmCbrCnfgAtmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCbrCnfgAtmIfIndex.setStatus("current")


class _AtmCbrCnfgAtmVpi_Type(Integer32):
    """Custom type atmCbrCnfgAtmVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AtmCbrCnfgAtmVpi_Type.__name__ = "Integer32"
_AtmCbrCnfgAtmVpi_Object = MibTableColumn
atmCbrCnfgAtmVpi = _AtmCbrCnfgAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 1, 1, 2),
    _AtmCbrCnfgAtmVpi_Type()
)
atmCbrCnfgAtmVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCbrCnfgAtmVpi.setStatus("current")


class _AtmCbrCnfgAtmVci_Type(Integer32):
    """Custom type atmCbrCnfgAtmVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmCbrCnfgAtmVci_Type.__name__ = "Integer32"
_AtmCbrCnfgAtmVci_Object = MibTableColumn
atmCbrCnfgAtmVci = _AtmCbrCnfgAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 1, 1, 3),
    _AtmCbrCnfgAtmVci_Type()
)
atmCbrCnfgAtmVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCbrCnfgAtmVci.setStatus("current")
_AtmCbrCnfgCbrIfIndex_Type = Integer32
_AtmCbrCnfgCbrIfIndex_Object = MibTableColumn
atmCbrCnfgCbrIfIndex = _AtmCbrCnfgCbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 1, 1, 4),
    _AtmCbrCnfgCbrIfIndex_Type()
)
atmCbrCnfgCbrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCbrCnfgCbrIfIndex.setStatus("current")


class _AtmCbrCnfgAdminStatus_Type(Integer32):
    """Custom type atmCbrCnfgAdminStatus based on Integer32"""
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


_AtmCbrCnfgAdminStatus_Type.__name__ = "Integer32"
_AtmCbrCnfgAdminStatus_Object = MibTableColumn
atmCbrCnfgAdminStatus = _AtmCbrCnfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 1, 1, 5),
    _AtmCbrCnfgAdminStatus_Type()
)
atmCbrCnfgAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmCbrCnfgAdminStatus.setStatus("current")


class _AtmCbrCnfgOperStatus_Type(Integer32):
    """Custom type atmCbrCnfgOperStatus based on Integer32"""
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


_AtmCbrCnfgOperStatus_Type.__name__ = "Integer32"
_AtmCbrCnfgOperStatus_Object = MibTableColumn
atmCbrCnfgOperStatus = _AtmCbrCnfgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 1, 1, 6),
    _AtmCbrCnfgOperStatus_Type()
)
atmCbrCnfgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCbrCnfgOperStatus.setStatus("current")
_AtmCbrCnfgLastChange_Type = TimeStamp
_AtmCbrCnfgLastChange_Object = MibTableColumn
atmCbrCnfgLastChange = _AtmCbrCnfgLastChange_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 1, 1, 7),
    _AtmCbrCnfgLastChange_Type()
)
atmCbrCnfgLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCbrCnfgLastChange.setStatus("current")


class _AtmCbrCnfgAAL1Signalling_Type(Integer32):
    """Custom type atmCbrCnfgAAL1Signalling based on Integer32"""
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


_AtmCbrCnfgAAL1Signalling_Type.__name__ = "Integer32"
_AtmCbrCnfgAAL1Signalling_Object = MibTableColumn
atmCbrCnfgAAL1Signalling = _AtmCbrCnfgAAL1Signalling_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 1, 1, 8),
    _AtmCbrCnfgAAL1Signalling_Type()
)
atmCbrCnfgAAL1Signalling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmCbrCnfgAAL1Signalling.setStatus("current")
_AtmCbrCnfgRxTimeSlots_Type = TimeSlots
_AtmCbrCnfgRxTimeSlots_Object = MibTableColumn
atmCbrCnfgRxTimeSlots = _AtmCbrCnfgRxTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 1, 1, 9),
    _AtmCbrCnfgRxTimeSlots_Type()
)
atmCbrCnfgRxTimeSlots.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmCbrCnfgRxTimeSlots.setStatus("current")


class _AtmCbrCnfgRxBytesPerCell_Type(Integer32):
    """Custom type atmCbrCnfgRxBytesPerCell based on Integer32"""
    defaultValue = 47


_AtmCbrCnfgRxBytesPerCell_Object = MibTableColumn
atmCbrCnfgRxBytesPerCell = _AtmCbrCnfgRxBytesPerCell_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 1, 1, 10),
    _AtmCbrCnfgRxBytesPerCell_Type()
)
atmCbrCnfgRxBytesPerCell.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmCbrCnfgRxBytesPerCell.setStatus("current")
_AtmCbrCnfgTxTimeSlots_Type = TimeSlots
_AtmCbrCnfgTxTimeSlots_Object = MibTableColumn
atmCbrCnfgTxTimeSlots = _AtmCbrCnfgTxTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 1, 1, 11),
    _AtmCbrCnfgTxTimeSlots_Type()
)
atmCbrCnfgTxTimeSlots.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmCbrCnfgTxTimeSlots.setStatus("current")


class _AtmCbrCnfgTxBytesPerCell_Type(Integer32):
    """Custom type atmCbrCnfgTxBytesPerCell based on Integer32"""
    defaultValue = 47


_AtmCbrCnfgTxBytesPerCell_Object = MibTableColumn
atmCbrCnfgTxBytesPerCell = _AtmCbrCnfgTxBytesPerCell_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 1, 1, 12),
    _AtmCbrCnfgTxBytesPerCell_Type()
)
atmCbrCnfgTxBytesPerCell.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmCbrCnfgTxBytesPerCell.setStatus("current")


class _AtmCbrCnfgParity_Type(Integer32):
    """Custom type atmCbrCnfgParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 3),
          ("off", 1),
          ("on", 2))
    )


_AtmCbrCnfgParity_Type.__name__ = "Integer32"
_AtmCbrCnfgParity_Object = MibTableColumn
atmCbrCnfgParity = _AtmCbrCnfgParity_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 1, 1, 13),
    _AtmCbrCnfgParity_Type()
)
atmCbrCnfgParity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmCbrCnfgParity.setStatus("current")
_AtmCbrCnfgRowStatus_Type = RowStatus
_AtmCbrCnfgRowStatus_Object = MibTableColumn
atmCbrCnfgRowStatus = _AtmCbrCnfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 1, 1, 14),
    _AtmCbrCnfgRowStatus_Type()
)
atmCbrCnfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmCbrCnfgRowStatus.setStatus("current")


class _AtmCbrCnfgService_Type(Integer32):
    """Custom type atmCbrCnfgService based on Integer32"""
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
        *(("notApplicable", 1),
          ("structured", 3),
          ("structuredControlSignalsTransport", 6),
          ("structuredWithPointer", 4),
          ("structuredWithoutPointer", 5),
          ("unstructured", 2))
    )


_AtmCbrCnfgService_Type.__name__ = "Integer32"
_AtmCbrCnfgService_Object = MibTableColumn
atmCbrCnfgService = _AtmCbrCnfgService_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 1, 1, 15),
    _AtmCbrCnfgService_Type()
)
atmCbrCnfgService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmCbrCnfgService.setStatus("current")
_AtmCESConfExtnsTable_Object = MibTable
atmCESConfExtnsTable = _AtmCESConfExtnsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 2)
)
if mibBuilder.loadTexts:
    atmCESConfExtnsTable.setStatus("current")
_AtmCESConfExtnsEntry_Object = MibTableRow
atmCESConfExtnsEntry = _AtmCESConfExtnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 2, 1)
)
atmCESConfExtnsEntry.setIndexNames(
    (0, "ACE20-MIB", "atmfCESCbrIndex"),
)
if mibBuilder.loadTexts:
    atmCESConfExtnsEntry.setStatus("current")
_AtmCESLastChange_Type = TimeStamp
_AtmCESLastChange_Object = MibTableColumn
atmCESLastChange = _AtmCESLastChange_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 2, 1, 1),
    _AtmCESLastChange_Type()
)
atmCESLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCESLastChange.setStatus("current")


class _AtmCESRxBytesPerCell_Type(Integer32):
    """Custom type atmCESRxBytesPerCell based on Integer32"""
    defaultValue = 47

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 47),
    )


_AtmCESRxBytesPerCell_Type.__name__ = "Integer32"
_AtmCESRxBytesPerCell_Object = MibTableColumn
atmCESRxBytesPerCell = _AtmCESRxBytesPerCell_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 2, 1, 2),
    _AtmCESRxBytesPerCell_Type()
)
atmCESRxBytesPerCell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCESRxBytesPerCell.setStatus("current")


class _AtmCESTxBytesPerCell_Type(Integer32):
    """Custom type atmCESTxBytesPerCell based on Integer32"""
    defaultValue = 47

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 47),
    )


_AtmCESTxBytesPerCell_Type.__name__ = "Integer32"
_AtmCESTxBytesPerCell_Object = MibTableColumn
atmCESTxBytesPerCell = _AtmCESTxBytesPerCell_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 2, 1, 3),
    _AtmCESTxBytesPerCell_Type()
)
atmCESTxBytesPerCell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCESTxBytesPerCell.setStatus("current")


class _AtmCESAal1Type_Type(Integer32):
    """Custom type atmCESAal1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ces", 1),
          ("dbces", 2),
          ("transparent", 3))
    )


_AtmCESAal1Type_Type.__name__ = "Integer32"
_AtmCESAal1Type_Object = MibTableColumn
atmCESAal1Type = _AtmCESAal1Type_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 2, 1, 4),
    _AtmCESAal1Type_Type()
)
atmCESAal1Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCESAal1Type.setStatus("current")


class _AtmCESParity_Type(Integer32):
    """Custom type atmCESParity based on Integer32"""
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


_AtmCESParity_Type.__name__ = "Integer32"
_AtmCESParity_Object = MibTableColumn
atmCESParity = _AtmCESParity_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 2, 1, 5),
    _AtmCESParity_Type()
)
atmCESParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCESParity.setStatus("current")


class _AtmCESSigType_Type(Integer32):
    """Custom type atmCESSigType based on Integer32"""
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
        *(("eAndmOrPlar", 1),
          ("fxoGroundStart", 4),
          ("fxoLoopStart", 2),
          ("fxsGroundStart", 5),
          ("fxsLoopStart", 3),
          ("other", 7),
          ("r2", 6))
    )


_AtmCESSigType_Type.__name__ = "Integer32"
_AtmCESSigType_Object = MibTableColumn
atmCESSigType = _AtmCESSigType_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 2, 1, 6),
    _AtmCESSigType_Type()
)
atmCESSigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCESSigType.setStatus("current")


class _AtmCESSigABBits_Type(OctetString):
    """Custom type atmCESSigABBits based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AtmCESSigABBits_Type.__name__ = "OctetString"
_AtmCESSigABBits_Object = MibTableColumn
atmCESSigABBits = _AtmCESSigABBits_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 3, 2, 1, 7),
    _AtmCESSigABBits_Type()
)
atmCESSigABBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmCESSigABBits.setStatus("current")
_AtmSuCrossConnectAtmEther_ObjectIdentity = ObjectIdentity
atmSuCrossConnectAtmEther = _AtmSuCrossConnectAtmEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4)
)
_AtmSuCrossConnectAtmEtherIndexNext_Type = Integer32
_AtmSuCrossConnectAtmEtherIndexNext_Object = MibScalar
atmSuCrossConnectAtmEtherIndexNext = _AtmSuCrossConnectAtmEtherIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 1),
    _AtmSuCrossConnectAtmEtherIndexNext_Type()
)
atmSuCrossConnectAtmEtherIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSuCrossConnectAtmEtherIndexNext.setStatus("current")
_AtmEtherCnfgTable_Object = MibTable
atmEtherCnfgTable = _AtmEtherCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 2)
)
if mibBuilder.loadTexts:
    atmEtherCnfgTable.setStatus("current")
_AtmEtherCnfgEntry_Object = MibTableRow
atmEtherCnfgEntry = _AtmEtherCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 2, 1)
)
atmEtherCnfgEntry.setIndexNames(
    (0, "ACE20-MIB", "atmEtherCnfgCrossConnectIndex"),
    (0, "ACE20-MIB", "atmEtherCnfgAtmIfIndex"),
    (0, "ACE20-MIB", "atmEtherCnfgAtmVpi"),
    (0, "ACE20-MIB", "atmEtherCnfgAtmVci"),
    (0, "ACE20-MIB", "atmEtherCnfgEtherIfIndex"),
)
if mibBuilder.loadTexts:
    atmEtherCnfgEntry.setStatus("current")
_AtmEtherCnfgCrossConnectIndex_Type = Integer32
_AtmEtherCnfgCrossConnectIndex_Object = MibTableColumn
atmEtherCnfgCrossConnectIndex = _AtmEtherCnfgCrossConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 2, 1, 1),
    _AtmEtherCnfgCrossConnectIndex_Type()
)
atmEtherCnfgCrossConnectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEtherCnfgCrossConnectIndex.setStatus("current")
_AtmEtherCnfgAtmIfIndex_Type = Integer32
_AtmEtherCnfgAtmIfIndex_Object = MibTableColumn
atmEtherCnfgAtmIfIndex = _AtmEtherCnfgAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 2, 1, 2),
    _AtmEtherCnfgAtmIfIndex_Type()
)
atmEtherCnfgAtmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEtherCnfgAtmIfIndex.setStatus("current")


class _AtmEtherCnfgAtmVpi_Type(Integer32):
    """Custom type atmEtherCnfgAtmVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AtmEtherCnfgAtmVpi_Type.__name__ = "Integer32"
_AtmEtherCnfgAtmVpi_Object = MibTableColumn
atmEtherCnfgAtmVpi = _AtmEtherCnfgAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 2, 1, 3),
    _AtmEtherCnfgAtmVpi_Type()
)
atmEtherCnfgAtmVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEtherCnfgAtmVpi.setStatus("current")


class _AtmEtherCnfgAtmVci_Type(Integer32):
    """Custom type atmEtherCnfgAtmVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmEtherCnfgAtmVci_Type.__name__ = "Integer32"
_AtmEtherCnfgAtmVci_Object = MibTableColumn
atmEtherCnfgAtmVci = _AtmEtherCnfgAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 2, 1, 4),
    _AtmEtherCnfgAtmVci_Type()
)
atmEtherCnfgAtmVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEtherCnfgAtmVci.setStatus("current")
_AtmEtherCnfgEtherIfIndex_Type = Integer32
_AtmEtherCnfgEtherIfIndex_Object = MibTableColumn
atmEtherCnfgEtherIfIndex = _AtmEtherCnfgEtherIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 2, 1, 5),
    _AtmEtherCnfgEtherIfIndex_Type()
)
atmEtherCnfgEtherIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEtherCnfgEtherIfIndex.setStatus("current")
_AtmEtherCnfgMacAddr_Type = MacAddress
_AtmEtherCnfgMacAddr_Object = MibTableColumn
atmEtherCnfgMacAddr = _AtmEtherCnfgMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 2, 1, 6),
    _AtmEtherCnfgMacAddr_Type()
)
atmEtherCnfgMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEtherCnfgMacAddr.setStatus("deprecated")


class _AtmEtherCnfgAdminStatus_Type(Integer32):
    """Custom type atmEtherCnfgAdminStatus based on Integer32"""
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


_AtmEtherCnfgAdminStatus_Type.__name__ = "Integer32"
_AtmEtherCnfgAdminStatus_Object = MibTableColumn
atmEtherCnfgAdminStatus = _AtmEtherCnfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 2, 1, 7),
    _AtmEtherCnfgAdminStatus_Type()
)
atmEtherCnfgAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmEtherCnfgAdminStatus.setStatus("current")


class _AtmEtherCnfgOperStatus_Type(Integer32):
    """Custom type atmEtherCnfgOperStatus based on Integer32"""
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


_AtmEtherCnfgOperStatus_Type.__name__ = "Integer32"
_AtmEtherCnfgOperStatus_Object = MibTableColumn
atmEtherCnfgOperStatus = _AtmEtherCnfgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 2, 1, 8),
    _AtmEtherCnfgOperStatus_Type()
)
atmEtherCnfgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEtherCnfgOperStatus.setStatus("current")
_AtmEtherCnfgLastChange_Type = TimeStamp
_AtmEtherCnfgLastChange_Object = MibTableColumn
atmEtherCnfgLastChange = _AtmEtherCnfgLastChange_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 2, 1, 9),
    _AtmEtherCnfgLastChange_Type()
)
atmEtherCnfgLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmEtherCnfgLastChange.setStatus("current")
_AtmEtherCnfgTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_AtmEtherCnfgTrafficDescrIndex_Object = MibTableColumn
atmEtherCnfgTrafficDescrIndex = _AtmEtherCnfgTrafficDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 2, 1, 10),
    _AtmEtherCnfgTrafficDescrIndex_Type()
)
atmEtherCnfgTrafficDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmEtherCnfgTrafficDescrIndex.setStatus("current")


class _AtmEtherCnfgEncapsulationMode_Type(Integer32):
    """Custom type atmEtherCnfgEncapsulationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atmBridgedEther", 1),
          ("atmBridgedEtherCRC", 2))
    )


_AtmEtherCnfgEncapsulationMode_Type.__name__ = "Integer32"
_AtmEtherCnfgEncapsulationMode_Object = MibTableColumn
atmEtherCnfgEncapsulationMode = _AtmEtherCnfgEncapsulationMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 2, 1, 11),
    _AtmEtherCnfgEncapsulationMode_Type()
)
atmEtherCnfgEncapsulationMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmEtherCnfgEncapsulationMode.setStatus("deprecated")


class _AtmEtherCnfgPriority_Type(Integer32):
    """Custom type atmEtherCnfgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("highPriority", 1),
          ("lowPriority", 3),
          ("mediumPriority", 2))
    )


_AtmEtherCnfgPriority_Type.__name__ = "Integer32"
_AtmEtherCnfgPriority_Object = MibTableColumn
atmEtherCnfgPriority = _AtmEtherCnfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 2, 1, 12),
    _AtmEtherCnfgPriority_Type()
)
atmEtherCnfgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmEtherCnfgPriority.setStatus("current")
_AtmEtherCnfgRowStatus_Type = RowStatus
_AtmEtherCnfgRowStatus_Object = MibTableColumn
atmEtherCnfgRowStatus = _AtmEtherCnfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 2, 1, 13),
    _AtmEtherCnfgRowStatus_Type()
)
atmEtherCnfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmEtherCnfgRowStatus.setStatus("current")
_AtmEtherCnfgRouterIP_Type = IpAddress
_AtmEtherCnfgRouterIP_Object = MibTableColumn
atmEtherCnfgRouterIP = _AtmEtherCnfgRouterIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 2, 1, 14),
    _AtmEtherCnfgRouterIP_Type()
)
atmEtherCnfgRouterIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmEtherCnfgRouterIP.setStatus("current")
_AtmEtherCnfgRouterMask_Type = IpAddress
_AtmEtherCnfgRouterMask_Object = MibTableColumn
atmEtherCnfgRouterMask = _AtmEtherCnfgRouterMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 2, 1, 15),
    _AtmEtherCnfgRouterMask_Type()
)
atmEtherCnfgRouterMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmEtherCnfgRouterMask.setStatus("current")


class _AtmEtherCnfgRouterFragmentation_Type(Integer32):
    """Custom type atmEtherCnfgRouterFragmentation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("notApplicable", 255),
          ("yes", 3))
    )


_AtmEtherCnfgRouterFragmentation_Type.__name__ = "Integer32"
_AtmEtherCnfgRouterFragmentation_Object = MibTableColumn
atmEtherCnfgRouterFragmentation = _AtmEtherCnfgRouterFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 2, 1, 16),
    _AtmEtherCnfgRouterFragmentation_Type()
)
atmEtherCnfgRouterFragmentation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmEtherCnfgRouterFragmentation.setStatus("current")


class _AtmEtherCnfgRouterRIPMode_Type(Integer32):
    """Custom type atmEtherCnfgRouterRIPMode based on Integer32"""
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
        *(("none", 4),
          ("notApplicable", 255),
          ("rip1", 1),
          ("rip1And2", 3),
          ("rip2", 2))
    )


_AtmEtherCnfgRouterRIPMode_Type.__name__ = "Integer32"
_AtmEtherCnfgRouterRIPMode_Object = MibTableColumn
atmEtherCnfgRouterRIPMode = _AtmEtherCnfgRouterRIPMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 2, 1, 17),
    _AtmEtherCnfgRouterRIPMode_Type()
)
atmEtherCnfgRouterRIPMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmEtherCnfgRouterRIPMode.setStatus("current")
_AtmEtherCnfgRouterMTU_Type = Integer32
_AtmEtherCnfgRouterMTU_Object = MibTableColumn
atmEtherCnfgRouterMTU = _AtmEtherCnfgRouterMTU_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 2, 1, 18),
    _AtmEtherCnfgRouterMTU_Type()
)
atmEtherCnfgRouterMTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmEtherCnfgRouterMTU.setStatus("deprecated")


class _AtmEtherCnfgPPPEncapsulation_Type(Integer32):
    """Custom type atmEtherCnfgPPPEncapsulation based on Integer32"""
    defaultValue = 3

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
        *(("none", 2),
          ("notApplicable", 1),
          ("pppLlcMuxed", 5),
          ("pppVcMuxed", 4),
          ("rfc1483", 3))
    )


_AtmEtherCnfgPPPEncapsulation_Type.__name__ = "Integer32"
_AtmEtherCnfgPPPEncapsulation_Object = MibTableColumn
atmEtherCnfgPPPEncapsulation = _AtmEtherCnfgPPPEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 2, 1, 19),
    _AtmEtherCnfgPPPEncapsulation_Type()
)
atmEtherCnfgPPPEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmEtherCnfgPPPEncapsulation.setStatus("current")


class _AtmEtherCnfgAllocatedBuffers_Type(Integer32):
    """Custom type atmEtherCnfgAllocatedBuffers based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 217),
    )


_AtmEtherCnfgAllocatedBuffers_Type.__name__ = "Integer32"
_AtmEtherCnfgAllocatedBuffers_Object = MibTableColumn
atmEtherCnfgAllocatedBuffers = _AtmEtherCnfgAllocatedBuffers_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 4, 2, 1, 20),
    _AtmEtherCnfgAllocatedBuffers_Type()
)
atmEtherCnfgAllocatedBuffers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmEtherCnfgAllocatedBuffers.setStatus("current")
_AtmSuCrossConnectTranslate_ObjectIdentity = ObjectIdentity
atmSuCrossConnectTranslate = _AtmSuCrossConnectTranslate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 5)
)
_AtmTranslateTable_Object = MibTable
atmTranslateTable = _AtmTranslateTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 5, 1)
)
if mibBuilder.loadTexts:
    atmTranslateTable.setStatus("current")
_AtmTranslateEntry_Object = MibTableRow
atmTranslateEntry = _AtmTranslateEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 5, 1, 1)
)
atmTranslateEntry.setIndexNames(
    (0, "ACE20-MIB", "atmTranslateAtmIfIndex"),
    (0, "ACE20-MIB", "atmTranslateAtmVpi"),
    (0, "ACE20-MIB", "atmTranslateAtmVci"),
)
if mibBuilder.loadTexts:
    atmTranslateEntry.setStatus("current")
_AtmTranslateAtmIfIndex_Type = Integer32
_AtmTranslateAtmIfIndex_Object = MibTableColumn
atmTranslateAtmIfIndex = _AtmTranslateAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 5, 1, 1, 1),
    _AtmTranslateAtmIfIndex_Type()
)
atmTranslateAtmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTranslateAtmIfIndex.setStatus("current")


class _AtmTranslateAtmVpi_Type(Integer32):
    """Custom type atmTranslateAtmVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AtmTranslateAtmVpi_Type.__name__ = "Integer32"
_AtmTranslateAtmVpi_Object = MibTableColumn
atmTranslateAtmVpi = _AtmTranslateAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 5, 1, 1, 2),
    _AtmTranslateAtmVpi_Type()
)
atmTranslateAtmVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTranslateAtmVpi.setStatus("current")


class _AtmTranslateAtmVci_Type(Integer32):
    """Custom type atmTranslateAtmVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmTranslateAtmVci_Type.__name__ = "Integer32"
_AtmTranslateAtmVci_Object = MibTableColumn
atmTranslateAtmVci = _AtmTranslateAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 5, 1, 1, 3),
    _AtmTranslateAtmVci_Type()
)
atmTranslateAtmVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTranslateAtmVci.setStatus("current")
_AtmTranslateUserIfIndex_Type = Integer32
_AtmTranslateUserIfIndex_Object = MibTableColumn
atmTranslateUserIfIndex = _AtmTranslateUserIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 12, 4, 3, 5, 1, 1, 4),
    _AtmTranslateUserIfIndex_Type()
)
atmTranslateUserIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmTranslateUserIfIndex.setStatus("current")

# Managed Objects groups


# Notification objects

alarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 12, 0, 1)
)
if mibBuilder.loadTexts:
    alarmTrap.setStatus(
        "current"
    )

statusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 12, 0, 2)
)
statusChangeTrap.setObjects(
      *(("RAD-MIB", "agnLed"),
        ("RAD-MIB", "agnIndication"))
)
if mibBuilder.loadTexts:
    statusChangeTrap.setStatus(
        "current"
    )

atmSuAgnNoBufferToNetwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 12, 0, 3)
)
atmSuAgnNoBufferToNetwork.setObjects(
    ("RAD-MIB", "alarmSeverity")
)
if mibBuilder.loadTexts:
    atmSuAgnNoBufferToNetwork.setStatus(
        "current"
    )

atmSuJitterBufferOverrun = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 12, 0, 4)
)
atmSuJitterBufferOverrun.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmSuJitterBufferOverrun.setStatus(
        "current"
    )

atmSuJitterBufferUnderrun = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 12, 0, 5)
)
atmSuJitterBufferUnderrun.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmSuJitterBufferUnderrun.setStatus(
        "current"
    )

atmSuDataLocalLoopbackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 12, 0, 6)
)
atmSuDataLocalLoopbackTrap.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("RAD-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmSuDataLocalLoopbackTrap.setStatus(
        "current"
    )

atmSuDataRemoteLoopbackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 12, 0, 7)
)
atmSuDataRemoteLoopbackTrap.setObjects(
      *(("RAD-MIB", "alarmSeverity"),
        ("RAD-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    atmSuDataRemoteLoopbackTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACE20-MIB",
    **{"radAtmEvents": radAtmEvents,
       "alarmTrap": alarmTrap,
       "statusChangeTrap": statusChangeTrap,
       "atmSuAgnNoBufferToNetwork": atmSuAgnNoBufferToNetwork,
       "atmSuJitterBufferOverrun": atmSuJitterBufferOverrun,
       "atmSuJitterBufferUnderrun": atmSuJitterBufferUnderrun,
       "atmSuDataLocalLoopbackTrap": atmSuDataLocalLoopbackTrap,
       "atmSuDataRemoteLoopbackTrap": atmSuDataRemoteLoopbackTrap,
       "atmSu": atmSu,
       "atmSuSystem": atmSuSystem,
       "atmSuSystemSwOperStatus": atmSuSystemSwOperStatus,
       "atmSuSystemSwSwitchVersionsCmd": atmSuSystemSwSwitchVersionsCmd,
       "atmSuSystemHistoryAlrTable": atmSuSystemHistoryAlrTable,
       "atmSuSystemHistoryAlrEntry": atmSuSystemHistoryAlrEntry,
       "atmSuSystemHistoryAlrIndex": atmSuSystemHistoryAlrIndex,
       "atmSuSystemHistoryAlrIfIndex": atmSuSystemHistoryAlrIfIndex,
       "atmSuSystemHistoryAlrDescription": atmSuSystemHistoryAlrDescription,
       "atmSuSystemHistoryAlrStatus": atmSuSystemHistoryAlrStatus,
       "atmSuSystemHistoryAlrOccurrenceTime": atmSuSystemHistoryAlrOccurrenceTime,
       "atmSuSystemHistoryAlrVpi": atmSuSystemHistoryAlrVpi,
       "atmSuSystemHistoryAlrVci": atmSuSystemHistoryAlrVci,
       "atmSuSystemClearHistoryAlrListCmd": atmSuSystemClearHistoryAlrListCmd,
       "atmSuSystemCurrentAlrTable": atmSuSystemCurrentAlrTable,
       "atmSuSystemCurrentAlrEntry": atmSuSystemCurrentAlrEntry,
       "atmSuSystemCurrentAlrIndex": atmSuSystemCurrentAlrIndex,
       "atmSuSystemCurrentAlrIfIndex": atmSuSystemCurrentAlrIfIndex,
       "atmSuSystemCurrentAlrDescription": atmSuSystemCurrentAlrDescription,
       "atmSuSystemILMICommunity": atmSuSystemILMICommunity,
       "atmSuSystemTrapMaxManagers": atmSuSystemTrapMaxManagers,
       "atmSuSystemAalSelection": atmSuSystemAalSelection,
       "atmSuSystemCodingLaw": atmSuSystemCodingLaw,
       "atmSuSystemISDNDataLinkActivation": atmSuSystemISDNDataLinkActivation,
       "atmSuSystemJitterBuffer": atmSuSystemJitterBuffer,
       "atmSuSystemOperMode": atmSuSystemOperMode,
       "atmSuSystemDSPGain": atmSuSystemDSPGain,
       "atmSuPort": atmSuPort,
       "atmSuPortDataCnfgTable": atmSuPortDataCnfgTable,
       "atmSuPortDataCnfgEntry": atmSuPortDataCnfgEntry,
       "atmSuPortDataApplication": atmSuPortDataApplication,
       "atmSuPortDataRate": atmSuPortDataRate,
       "atmSuPortDataDCD": atmSuPortDataDCD,
       "atmSuPortDataMode": atmSuPortDataMode,
       "atmSuPortDataCRC": atmSuPortDataCRC,
       "atmSuPortDataClock": atmSuPortDataClock,
       "atmSuPortDataMaxNoOfConns": atmSuPortDataMaxNoOfConns,
       "atmSuPortDataConfNoOfConns": atmSuPortDataConfNoOfConns,
       "atmSuPortDataIdleCode": atmSuPortDataIdleCode,
       "atmSuPortDataInterfaceType": atmSuPortDataInterfaceType,
       "atmSuPortDataClkPolarity": atmSuPortDataClkPolarity,
       "atmSuPortDataCtsStatus": atmSuPortDataCtsStatus,
       "atmSuPortDataRtsStatus": atmSuPortDataRtsStatus,
       "atmSuPortDs1": atmSuPortDs1,
       "atmSuPortDs1CnfgTable": atmSuPortDs1CnfgTable,
       "atmSuPortDs1CnfgEntry": atmSuPortDs1CnfgEntry,
       "atmSuPortDs1CnfgRxSensitivity": atmSuPortDs1CnfgRxSensitivity,
       "atmSuPortDs1CnfgLBO": atmSuPortDs1CnfgLBO,
       "atmSuPortDs1CnfgRestoreTime": atmSuPortDs1CnfgRestoreTime,
       "atmSuPortDs1CnfgInbandMng": atmSuPortDs1CnfgInbandMng,
       "atmSuPortDs1CnfgDedicatedTs": atmSuPortDs1CnfgDedicatedTs,
       "atmSuPortDs1CbrCnfgTable": atmSuPortDs1CbrCnfgTable,
       "atmSuPortDs1CbrCnfgEntry": atmSuPortDs1CbrCnfgEntry,
       "atmSuPortDs1CbrIdleCode": atmSuPortDs1CbrIdleCode,
       "atmSuPortDs1CbrRxTimeSlots": atmSuPortDs1CbrRxTimeSlots,
       "atmSuPortDs1CbrTxTimeSlots": atmSuPortDs1CbrTxTimeSlots,
       "atmSuPortDs1CbrMaxNoOfConns": atmSuPortDs1CbrMaxNoOfConns,
       "atmSuPortDs1CbrConfNoOfConns": atmSuPortDs1CbrConfNoOfConns,
       "atmSuPortDs1CbrSignallingSampleTime": atmSuPortDs1CbrSignallingSampleTime,
       "atmSuPortAtm": atmSuPortAtm,
       "atmSuPortAtmCnfgTable": atmSuPortAtmCnfgTable,
       "atmSuPortAtmCnfgEntry": atmSuPortAtmCnfgEntry,
       "atmSuPortAtmCnfgIdleCellCLP": atmSuPortAtmCnfgIdleCellCLP,
       "atmSuPortAtmCnfgScramble": atmSuPortAtmCnfgScramble,
       "atmSuPortAtmSNMPVpi": atmSuPortAtmSNMPVpi,
       "atmSuPortAtmSNMPVci": atmSuPortAtmSNMPVci,
       "atmSuPortAtmSNMPStatus": atmSuPortAtmSNMPStatus,
       "atmSuPortAtmILMIStatus": atmSuPortAtmILMIStatus,
       "atmSuPortAtmSNMPIp": atmSuPortAtmSNMPIp,
       "atmSuPortAtmCnfgCDVOptimization": atmSuPortAtmCnfgCDVOptimization,
       "atmSuPortAtmCnfgShapingMode": atmSuPortAtmCnfgShapingMode,
       "atmSuPortAtmSNMPTrafficDescrIndex": atmSuPortAtmSNMPTrafficDescrIndex,
       "atmSuPortAtmIfStatsTable": atmSuPortAtmIfStatsTable,
       "atmSuPortAtmIfStatsEntry": atmSuPortAtmIfStatsEntry,
       "atmSuPortAtmRxClp0Cells": atmSuPortAtmRxClp0Cells,
       "atmSuPortAtmRxClp1Cells": atmSuPortAtmRxClp1Cells,
       "atmSuPortAtmRxEfciSetCells": atmSuPortAtmRxEfciSetCells,
       "atmSuPortAtmRxOamCells": atmSuPortAtmRxOamCells,
       "atmSuPortAtmTxClp0Cells": atmSuPortAtmTxClp0Cells,
       "atmSuPortAtmTxClp1Cells": atmSuPortAtmTxClp1Cells,
       "atmSuPortAtmTxEfciSetCells": atmSuPortAtmTxEfciSetCells,
       "atmSuPortAtmTxOamCells": atmSuPortAtmTxOamCells,
       "atmSuPortAtmVclStatsTable": atmSuPortAtmVclStatsTable,
       "atmSuPortAtmVclStatsEntry": atmSuPortAtmVclStatsEntry,
       "atmSuPortAtmVclStatsRxCells": atmSuPortAtmVclStatsRxCells,
       "atmSuPortAtmVclStatsRxClp0Cells": atmSuPortAtmVclStatsRxClp0Cells,
       "atmSuPortAtmVclStatsRxClp1Cells": atmSuPortAtmVclStatsRxClp1Cells,
       "atmSuPortAtmVclStatsRxDiscardsCells": atmSuPortAtmVclStatsRxDiscardsCells,
       "atmSuPortAtmVclStatsTxCells": atmSuPortAtmVclStatsTxCells,
       "atmSuPortAtmVclStatsTxClp0Cells": atmSuPortAtmVclStatsTxClp0Cells,
       "atmSuPortAtmVclStatsTxClp1Cells": atmSuPortAtmVclStatsTxClp1Cells,
       "atmSuPortAtmVclStatsRxTotalAISCells": atmSuPortAtmVclStatsRxTotalAISCells,
       "atmSuPortAtmVclStatsRxTotalCCCells": atmSuPortAtmVclStatsRxTotalCCCells,
       "atmSuPortAtmVclStatsTotalSuccLoopbacks": atmSuPortAtmVclStatsTotalSuccLoopbacks,
       "atmSuPortAtmVclStatsTotalFailLoopbacks": atmSuPortAtmVclStatsTotalFailLoopbacks,
       "atmSuPortAtmVclStatsRxTotalRDICells": atmSuPortAtmVclStatsRxTotalRDICells,
       "atmSuPortAtmVclStatsTotalLOCSeconds": atmSuPortAtmVclStatsTotalLOCSeconds,
       "atmSuPortAtmVclStatsRxTotalLoopbackRequests": atmSuPortAtmVclStatsRxTotalLoopbackRequests,
       "atmSuPortAtmVclStatsTxTotalAISCells": atmSuPortAtmVclStatsTxTotalAISCells,
       "atmSuPortAtmVclStatsTxTotalCCCells": atmSuPortAtmVclStatsTxTotalCCCells,
       "atmSuPortAtmVclStatsTxTotalRDICells": atmSuPortAtmVclStatsTxTotalRDICells,
       "atmSuPortAtmVclStatsTxTotalLoopbackResponses": atmSuPortAtmVclStatsTxTotalLoopbackResponses,
       "atmSuPortAtmVclStatsTxTotalLoopbackRequests": atmSuPortAtmVclStatsTxTotalLoopbackRequests,
       "atmSuPortAtmVclStatsRxTotalLoopbackResponses": atmSuPortAtmVclStatsRxTotalLoopbackResponses,
       "atmSuPortFr": atmSuPortFr,
       "atmSuPortFrLportTable": atmSuPortFrLportTable,
       "atmSuPortFrLportEntry": atmSuPortFrLportEntry,
       "atmSuPortFrLportSNMPDlci": atmSuPortFrLportSNMPDlci,
       "atmSuPortFrLportSNMPStatus": atmSuPortFrLportSNMPStatus,
       "atmSuPortFrLportVCSigProtocol": atmSuPortFrLportVCSigProtocol,
       "atmSuPortFrLportVCSigProcedure": atmSuPortFrLportVCSigProcedure,
       "atmSuPortFrLportCLLM": atmSuPortFrLportCLLM,
       "atmSuPortFrLportSNMPIp": atmSuPortFrLportSNMPIp,
       "atmSuPortFrPvcEndptTable": atmSuPortFrPvcEndptTable,
       "atmSuPortFrPvcEndptEntry": atmSuPortFrPvcEndptEntry,
       "atmSuPortFrPvcEndptTxFECNs": atmSuPortFrPvcEndptTxFECNs,
       "atmSuPortFrPvcEndptTxBECNs": atmSuPortFrPvcEndptTxBECNs,
       "atmSuPortFrPvcEndptTxDEs": atmSuPortFrPvcEndptTxDEs,
       "atmSuPortFrPvcEndptRxFECNs": atmSuPortFrPvcEndptRxFECNs,
       "atmSuPortFrPvcEndptRxBECNs": atmSuPortFrPvcEndptRxBECNs,
       "atmSuPortDxi": atmSuPortDxi,
       "atmSuPortDxiConfTable": atmSuPortDxiConfTable,
       "atmSuPortDxiConfEntry": atmSuPortDxiConfEntry,
       "atmSuPortDxiPortMode": atmSuPortDxiPortMode,
       "atmSuPortDxiSigProtocol": atmSuPortDxiSigProtocol,
       "atmSuPortDxiSigDfa": atmSuPortDxiSigDfa,
       "atmSuPortCmdTable": atmSuPortCmdTable,
       "atmSuPortCmdEntry": atmSuPortCmdEntry,
       "atmSuResetPortStatsCmd": atmSuResetPortStatsCmd,
       "atmSuResetConnsStatsCmd": atmSuResetConnsStatsCmd,
       "atmSuPortEther": atmSuPortEther,
       "atmSuPortEtherTable": atmSuPortEtherTable,
       "atmSuPortEtherEntry": atmSuPortEtherEntry,
       "atmSuPortEtherIP": atmSuPortEtherIP,
       "atmSuPortEtherMask": atmSuPortEtherMask,
       "atmSuPortEtherDefaultGateWayIp": atmSuPortEtherDefaultGateWayIp,
       "atmSuPortEtherDefaultCrossConnectId": atmSuPortEtherDefaultCrossConnectId,
       "atmSuPortEtherDefaultGatewayStatus": atmSuPortEtherDefaultGatewayStatus,
       "atmSuPortEtherSNMPStatus": atmSuPortEtherSNMPStatus,
       "atmSuPortEtherFragmentation": atmSuPortEtherFragmentation,
       "atmSuPortEtherRIPMode": atmSuPortEtherRIPMode,
       "atmSuPortEtherBridgingMode": atmSuPortEtherBridgingMode,
       "atmSuPortEtherARPTimeout": atmSuPortEtherARPTimeout,
       "atmSuPortEtherAgingTime": atmSuPortEtherAgingTime,
       "atmSuPortEtherPppOEEnable": atmSuPortEtherPppOEEnable,
       "atmSuPortEtherStatus": atmSuPortEtherStatus,
       "atmSuCrossConnect": atmSuCrossConnect,
       "atmSuCrossConnectAtmFr": atmSuCrossConnectAtmFr,
       "atmSuCrossConnectAtmFrDescriptor": atmSuCrossConnectAtmFrDescriptor,
       "atmFrCrossConnectNetwork": atmFrCrossConnectNetwork,
       "atmFrCrossConnectService": atmFrCrossConnectService,
       "atmFrDescrTable": atmFrDescrTable,
       "atmFrDescrEntry": atmFrDescrEntry,
       "atmFrDescrIndex": atmFrDescrIndex,
       "atmFrDescrType": atmFrDescrType,
       "atmFrDescrClp2De": atmFrDescrClp2De,
       "atmFrDescrDe2Clp": atmFrDescrDe2Clp,
       "atmFrDescrFecn2Efci": atmFrDescrFecn2Efci,
       "atmFrDescrMappingMode": atmFrDescrMappingMode,
       "atmFrDescrRowStatus": atmFrDescrRowStatus,
       "atmSuCrossConnectAtmFrIndexNext": atmSuCrossConnectAtmFrIndexNext,
       "atmFrCnfgTable": atmFrCnfgTable,
       "atmFrCnfgEntry": atmFrCnfgEntry,
       "atmFrCnfgCrossConnectIndex": atmFrCnfgCrossConnectIndex,
       "atmFrCnfgAtmIfIndex": atmFrCnfgAtmIfIndex,
       "atmFrCnfgAtmVpi": atmFrCnfgAtmVpi,
       "atmFrCnfgAtmVci": atmFrCnfgAtmVci,
       "atmFrCnfgFrIfIndex": atmFrCnfgFrIfIndex,
       "atmFrCnfgDlci": atmFrCnfgDlci,
       "atmFrCnfgAdminStatus": atmFrCnfgAdminStatus,
       "atmFrCnfgOperStatus": atmFrCnfgOperStatus,
       "atmFrCnfgLastChange": atmFrCnfgLastChange,
       "atmFrCnfgMappingDescrIndex": atmFrCnfgMappingDescrIndex,
       "atmFrCnfgSscsDlci": atmFrCnfgSscsDlci,
       "atmFrCnfgTrafficDescrIndex": atmFrCnfgTrafficDescrIndex,
       "atmFrCnfgPriority": atmFrCnfgPriority,
       "atmFrCnfgRowStatus": atmFrCnfgRowStatus,
       "atmFrCnfgAllocatedBuffers": atmFrCnfgAllocatedBuffers,
       "atmFrMaxMany2OneConnsPerVcc": atmFrMaxMany2OneConnsPerVcc,
       "atmSuCrossConnectAtmDxi": atmSuCrossConnectAtmDxi,
       "atmSuCrossConnectAtmDxiIndexNext": atmSuCrossConnectAtmDxiIndexNext,
       "atmDxiCnfgTable": atmDxiCnfgTable,
       "atmDxiCnfgEntry": atmDxiCnfgEntry,
       "atmDxiCnfgCrossConnectIndex": atmDxiCnfgCrossConnectIndex,
       "atmDxiCnfgAtmIfIndex": atmDxiCnfgAtmIfIndex,
       "atmDxiCnfgAtmVpi": atmDxiCnfgAtmVpi,
       "atmDxiCnfgAtmVci": atmDxiCnfgAtmVci,
       "atmDxiCnfgDxiIfIndex": atmDxiCnfgDxiIfIndex,
       "atmDxiCnfgDfa": atmDxiCnfgDfa,
       "atmDxiCnfgAdminStatus": atmDxiCnfgAdminStatus,
       "atmDxiCnfgOperStatus": atmDxiCnfgOperStatus,
       "atmDxiCnfgLastChange": atmDxiCnfgLastChange,
       "atmDxiCnfgTrafficDescrIndex": atmDxiCnfgTrafficDescrIndex,
       "atmDxiCnfgPriority": atmDxiCnfgPriority,
       "atmDxiCnfgRowStatus": atmDxiCnfgRowStatus,
       "atmSuAtmCbr": atmSuAtmCbr,
       "atmCbrCnfgTable": atmCbrCnfgTable,
       "atmCbrCnfgEntry": atmCbrCnfgEntry,
       "atmCbrCnfgAtmIfIndex": atmCbrCnfgAtmIfIndex,
       "atmCbrCnfgAtmVpi": atmCbrCnfgAtmVpi,
       "atmCbrCnfgAtmVci": atmCbrCnfgAtmVci,
       "atmCbrCnfgCbrIfIndex": atmCbrCnfgCbrIfIndex,
       "atmCbrCnfgAdminStatus": atmCbrCnfgAdminStatus,
       "atmCbrCnfgOperStatus": atmCbrCnfgOperStatus,
       "atmCbrCnfgLastChange": atmCbrCnfgLastChange,
       "atmCbrCnfgAAL1Signalling": atmCbrCnfgAAL1Signalling,
       "atmCbrCnfgRxTimeSlots": atmCbrCnfgRxTimeSlots,
       "atmCbrCnfgRxBytesPerCell": atmCbrCnfgRxBytesPerCell,
       "atmCbrCnfgTxTimeSlots": atmCbrCnfgTxTimeSlots,
       "atmCbrCnfgTxBytesPerCell": atmCbrCnfgTxBytesPerCell,
       "atmCbrCnfgParity": atmCbrCnfgParity,
       "atmCbrCnfgRowStatus": atmCbrCnfgRowStatus,
       "atmCbrCnfgService": atmCbrCnfgService,
       "atmCESConfExtnsTable": atmCESConfExtnsTable,
       "atmCESConfExtnsEntry": atmCESConfExtnsEntry,
       "atmCESLastChange": atmCESLastChange,
       "atmCESRxBytesPerCell": atmCESRxBytesPerCell,
       "atmCESTxBytesPerCell": atmCESTxBytesPerCell,
       "atmCESAal1Type": atmCESAal1Type,
       "atmCESParity": atmCESParity,
       "atmCESSigType": atmCESSigType,
       "atmCESSigABBits": atmCESSigABBits,
       "atmSuCrossConnectAtmEther": atmSuCrossConnectAtmEther,
       "atmSuCrossConnectAtmEtherIndexNext": atmSuCrossConnectAtmEtherIndexNext,
       "atmEtherCnfgTable": atmEtherCnfgTable,
       "atmEtherCnfgEntry": atmEtherCnfgEntry,
       "atmEtherCnfgCrossConnectIndex": atmEtherCnfgCrossConnectIndex,
       "atmEtherCnfgAtmIfIndex": atmEtherCnfgAtmIfIndex,
       "atmEtherCnfgAtmVpi": atmEtherCnfgAtmVpi,
       "atmEtherCnfgAtmVci": atmEtherCnfgAtmVci,
       "atmEtherCnfgEtherIfIndex": atmEtherCnfgEtherIfIndex,
       "atmEtherCnfgMacAddr": atmEtherCnfgMacAddr,
       "atmEtherCnfgAdminStatus": atmEtherCnfgAdminStatus,
       "atmEtherCnfgOperStatus": atmEtherCnfgOperStatus,
       "atmEtherCnfgLastChange": atmEtherCnfgLastChange,
       "atmEtherCnfgTrafficDescrIndex": atmEtherCnfgTrafficDescrIndex,
       "atmEtherCnfgEncapsulationMode": atmEtherCnfgEncapsulationMode,
       "atmEtherCnfgPriority": atmEtherCnfgPriority,
       "atmEtherCnfgRowStatus": atmEtherCnfgRowStatus,
       "atmEtherCnfgRouterIP": atmEtherCnfgRouterIP,
       "atmEtherCnfgRouterMask": atmEtherCnfgRouterMask,
       "atmEtherCnfgRouterFragmentation": atmEtherCnfgRouterFragmentation,
       "atmEtherCnfgRouterRIPMode": atmEtherCnfgRouterRIPMode,
       "atmEtherCnfgRouterMTU": atmEtherCnfgRouterMTU,
       "atmEtherCnfgPPPEncapsulation": atmEtherCnfgPPPEncapsulation,
       "atmEtherCnfgAllocatedBuffers": atmEtherCnfgAllocatedBuffers,
       "atmSuCrossConnectTranslate": atmSuCrossConnectTranslate,
       "atmTranslateTable": atmTranslateTable,
       "atmTranslateEntry": atmTranslateEntry,
       "atmTranslateAtmIfIndex": atmTranslateAtmIfIndex,
       "atmTranslateAtmVpi": atmTranslateAtmVpi,
       "atmTranslateAtmVci": atmTranslateAtmVci,
       "atmTranslateUserIfIndex": atmTranslateUserIfIndex}
)
