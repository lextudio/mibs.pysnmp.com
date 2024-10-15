# SNMP MIB module (MIKROTIK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MIKROTIK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:01 2024
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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

mikrotikExperimentalModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1)
)
mikrotikExperimentalModule.setRevisions(
        ("2017-03-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ObjectIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class HexInt(Integer32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )



class Voltage(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )



class Temperature(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )



class Power(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )



class GDiv100(Gauge32, TextualConvention):
    status = "current"
    displayHint = "d-2"


class GDiv1000(Gauge32, TextualConvention):
    status = "current"
    displayHint = "d-3"


class IDiv1000(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-3"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )



class BoolValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Mikrotik_ObjectIdentity = ObjectIdentity
mikrotik = _Mikrotik_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988)
)
_MtXRouterOs_ObjectIdentity = ObjectIdentity
mtXRouterOs = _MtXRouterOs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1)
)
_MtxrWireless_ObjectIdentity = ObjectIdentity
mtxrWireless = _MtxrWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1)
)
_MtxrWlStatTable_Object = MibTable
mtxrWlStatTable = _MtxrWlStatTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mtxrWlStatTable.setStatus("current")
_MtxrWlStatEntry_Object = MibTableRow
mtxrWlStatEntry = _MtxrWlStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 1, 1)
)
mtxrWlStatEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrWlStatIndex"),
)
if mibBuilder.loadTexts:
    mtxrWlStatEntry.setStatus("current")
_MtxrWlStatIndex_Type = ObjectIndex
_MtxrWlStatIndex_Object = MibTableColumn
mtxrWlStatIndex = _MtxrWlStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 1, 1, 1),
    _MtxrWlStatIndex_Type()
)
mtxrWlStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrWlStatIndex.setStatus("current")
_MtxrWlStatTxRate_Type = Gauge32
_MtxrWlStatTxRate_Object = MibTableColumn
mtxrWlStatTxRate = _MtxrWlStatTxRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 1, 1, 2),
    _MtxrWlStatTxRate_Type()
)
mtxrWlStatTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlStatTxRate.setStatus("current")
_MtxrWlStatRxRate_Type = Gauge32
_MtxrWlStatRxRate_Object = MibTableColumn
mtxrWlStatRxRate = _MtxrWlStatRxRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 1, 1, 3),
    _MtxrWlStatRxRate_Type()
)
mtxrWlStatRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlStatRxRate.setStatus("current")
_MtxrWlStatStrength_Type = Integer32
_MtxrWlStatStrength_Object = MibTableColumn
mtxrWlStatStrength = _MtxrWlStatStrength_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 1, 1, 4),
    _MtxrWlStatStrength_Type()
)
mtxrWlStatStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlStatStrength.setStatus("current")
_MtxrWlStatSsid_Type = DisplayString
_MtxrWlStatSsid_Object = MibTableColumn
mtxrWlStatSsid = _MtxrWlStatSsid_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 1, 1, 5),
    _MtxrWlStatSsid_Type()
)
mtxrWlStatSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlStatSsid.setStatus("current")
_MtxrWlStatBssid_Type = MacAddress
_MtxrWlStatBssid_Object = MibTableColumn
mtxrWlStatBssid = _MtxrWlStatBssid_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 1, 1, 6),
    _MtxrWlStatBssid_Type()
)
mtxrWlStatBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlStatBssid.setStatus("current")
_MtxrWlStatFreq_Type = Integer32
_MtxrWlStatFreq_Object = MibTableColumn
mtxrWlStatFreq = _MtxrWlStatFreq_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 1, 1, 7),
    _MtxrWlStatFreq_Type()
)
mtxrWlStatFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlStatFreq.setStatus("current")
_MtxrWlStatBand_Type = DisplayString
_MtxrWlStatBand_Object = MibTableColumn
mtxrWlStatBand = _MtxrWlStatBand_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 1, 1, 8),
    _MtxrWlStatBand_Type()
)
mtxrWlStatBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlStatBand.setStatus("current")
_MtxrWlRtabTable_Object = MibTable
mtxrWlRtabTable = _MtxrWlRtabTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mtxrWlRtabTable.setStatus("current")
_MtxrWlRtabEntry_Object = MibTableRow
mtxrWlRtabEntry = _MtxrWlRtabEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1)
)
mtxrWlRtabEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrWlRtabAddr"),
    (0, "MIKROTIK-MIB", "mtxrWlRtabIface"),
)
if mibBuilder.loadTexts:
    mtxrWlRtabEntry.setStatus("current")
_MtxrWlRtabAddr_Type = MacAddress
_MtxrWlRtabAddr_Object = MibTableColumn
mtxrWlRtabAddr = _MtxrWlRtabAddr_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 1),
    _MtxrWlRtabAddr_Type()
)
mtxrWlRtabAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrWlRtabAddr.setStatus("current")
_MtxrWlRtabIface_Type = ObjectIndex
_MtxrWlRtabIface_Object = MibTableColumn
mtxrWlRtabIface = _MtxrWlRtabIface_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 2),
    _MtxrWlRtabIface_Type()
)
mtxrWlRtabIface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrWlRtabIface.setStatus("current")
_MtxrWlRtabStrength_Type = Integer32
_MtxrWlRtabStrength_Object = MibTableColumn
mtxrWlRtabStrength = _MtxrWlRtabStrength_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 3),
    _MtxrWlRtabStrength_Type()
)
mtxrWlRtabStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabStrength.setStatus("current")
_MtxrWlRtabTxBytes_Type = Counter32
_MtxrWlRtabTxBytes_Object = MibTableColumn
mtxrWlRtabTxBytes = _MtxrWlRtabTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 4),
    _MtxrWlRtabTxBytes_Type()
)
mtxrWlRtabTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabTxBytes.setStatus("current")
_MtxrWlRtabRxBytes_Type = Counter32
_MtxrWlRtabRxBytes_Object = MibTableColumn
mtxrWlRtabRxBytes = _MtxrWlRtabRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 5),
    _MtxrWlRtabRxBytes_Type()
)
mtxrWlRtabRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabRxBytes.setStatus("current")
_MtxrWlRtabTxPackets_Type = Counter32
_MtxrWlRtabTxPackets_Object = MibTableColumn
mtxrWlRtabTxPackets = _MtxrWlRtabTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 6),
    _MtxrWlRtabTxPackets_Type()
)
mtxrWlRtabTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabTxPackets.setStatus("current")
_MtxrWlRtabRxPackets_Type = Counter32
_MtxrWlRtabRxPackets_Object = MibTableColumn
mtxrWlRtabRxPackets = _MtxrWlRtabRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 7),
    _MtxrWlRtabRxPackets_Type()
)
mtxrWlRtabRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabRxPackets.setStatus("current")
_MtxrWlRtabTxRate_Type = Gauge32
_MtxrWlRtabTxRate_Object = MibTableColumn
mtxrWlRtabTxRate = _MtxrWlRtabTxRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 8),
    _MtxrWlRtabTxRate_Type()
)
mtxrWlRtabTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabTxRate.setStatus("current")
_MtxrWlRtabRxRate_Type = Gauge32
_MtxrWlRtabRxRate_Object = MibTableColumn
mtxrWlRtabRxRate = _MtxrWlRtabRxRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 9),
    _MtxrWlRtabRxRate_Type()
)
mtxrWlRtabRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabRxRate.setStatus("current")
_MtxrWlRtabRouterOSVersion_Type = DisplayString
_MtxrWlRtabRouterOSVersion_Object = MibTableColumn
mtxrWlRtabRouterOSVersion = _MtxrWlRtabRouterOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 10),
    _MtxrWlRtabRouterOSVersion_Type()
)
mtxrWlRtabRouterOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabRouterOSVersion.setStatus("current")
_MtxrWlRtabUptime_Type = TimeTicks
_MtxrWlRtabUptime_Object = MibTableColumn
mtxrWlRtabUptime = _MtxrWlRtabUptime_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 11),
    _MtxrWlRtabUptime_Type()
)
mtxrWlRtabUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabUptime.setStatus("current")
_MtxrWlRtabSignalToNoise_Type = Integer32
_MtxrWlRtabSignalToNoise_Object = MibTableColumn
mtxrWlRtabSignalToNoise = _MtxrWlRtabSignalToNoise_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 12),
    _MtxrWlRtabSignalToNoise_Type()
)
mtxrWlRtabSignalToNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabSignalToNoise.setStatus("current")
_MtxrWlRtabTxStrengthCh0_Type = Integer32
_MtxrWlRtabTxStrengthCh0_Object = MibTableColumn
mtxrWlRtabTxStrengthCh0 = _MtxrWlRtabTxStrengthCh0_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 13),
    _MtxrWlRtabTxStrengthCh0_Type()
)
mtxrWlRtabTxStrengthCh0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabTxStrengthCh0.setStatus("current")
_MtxrWlRtabRxStrengthCh0_Type = Integer32
_MtxrWlRtabRxStrengthCh0_Object = MibTableColumn
mtxrWlRtabRxStrengthCh0 = _MtxrWlRtabRxStrengthCh0_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 14),
    _MtxrWlRtabRxStrengthCh0_Type()
)
mtxrWlRtabRxStrengthCh0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabRxStrengthCh0.setStatus("current")
_MtxrWlRtabTxStrengthCh1_Type = Integer32
_MtxrWlRtabTxStrengthCh1_Object = MibTableColumn
mtxrWlRtabTxStrengthCh1 = _MtxrWlRtabTxStrengthCh1_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 15),
    _MtxrWlRtabTxStrengthCh1_Type()
)
mtxrWlRtabTxStrengthCh1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabTxStrengthCh1.setStatus("current")
_MtxrWlRtabRxStrengthCh1_Type = Integer32
_MtxrWlRtabRxStrengthCh1_Object = MibTableColumn
mtxrWlRtabRxStrengthCh1 = _MtxrWlRtabRxStrengthCh1_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 16),
    _MtxrWlRtabRxStrengthCh1_Type()
)
mtxrWlRtabRxStrengthCh1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabRxStrengthCh1.setStatus("current")
_MtxrWlRtabTxStrengthCh2_Type = Integer32
_MtxrWlRtabTxStrengthCh2_Object = MibTableColumn
mtxrWlRtabTxStrengthCh2 = _MtxrWlRtabTxStrengthCh2_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 17),
    _MtxrWlRtabTxStrengthCh2_Type()
)
mtxrWlRtabTxStrengthCh2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabTxStrengthCh2.setStatus("current")
_MtxrWlRtabRxStrengthCh2_Type = Integer32
_MtxrWlRtabRxStrengthCh2_Object = MibTableColumn
mtxrWlRtabRxStrengthCh2 = _MtxrWlRtabRxStrengthCh2_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 18),
    _MtxrWlRtabRxStrengthCh2_Type()
)
mtxrWlRtabRxStrengthCh2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabRxStrengthCh2.setStatus("current")
_MtxrWlRtabTxStrength_Type = Integer32
_MtxrWlRtabTxStrength_Object = MibTableColumn
mtxrWlRtabTxStrength = _MtxrWlRtabTxStrength_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 2, 1, 19),
    _MtxrWlRtabTxStrength_Type()
)
mtxrWlRtabTxStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabTxStrength.setStatus("current")
_MtxrWlApTable_Object = MibTable
mtxrWlApTable = _MtxrWlApTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mtxrWlApTable.setStatus("current")
_MtxrWlApEntry_Object = MibTableRow
mtxrWlApEntry = _MtxrWlApEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1)
)
mtxrWlApEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrWlApIndex"),
)
if mibBuilder.loadTexts:
    mtxrWlApEntry.setStatus("current")
_MtxrWlApIndex_Type = ObjectIndex
_MtxrWlApIndex_Object = MibTableColumn
mtxrWlApIndex = _MtxrWlApIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1, 1),
    _MtxrWlApIndex_Type()
)
mtxrWlApIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrWlApIndex.setStatus("current")
_MtxrWlApTxRate_Type = Gauge32
_MtxrWlApTxRate_Object = MibTableColumn
mtxrWlApTxRate = _MtxrWlApTxRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1, 2),
    _MtxrWlApTxRate_Type()
)
mtxrWlApTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlApTxRate.setStatus("current")
_MtxrWlApRxRate_Type = Gauge32
_MtxrWlApRxRate_Object = MibTableColumn
mtxrWlApRxRate = _MtxrWlApRxRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1, 3),
    _MtxrWlApRxRate_Type()
)
mtxrWlApRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlApRxRate.setStatus("current")
_MtxrWlApSsid_Type = DisplayString
_MtxrWlApSsid_Object = MibTableColumn
mtxrWlApSsid = _MtxrWlApSsid_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1, 4),
    _MtxrWlApSsid_Type()
)
mtxrWlApSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlApSsid.setStatus("current")
_MtxrWlApBssid_Type = MacAddress
_MtxrWlApBssid_Object = MibTableColumn
mtxrWlApBssid = _MtxrWlApBssid_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1, 5),
    _MtxrWlApBssid_Type()
)
mtxrWlApBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlApBssid.setStatus("current")
_MtxrWlApClientCount_Type = Counter32
_MtxrWlApClientCount_Object = MibTableColumn
mtxrWlApClientCount = _MtxrWlApClientCount_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1, 6),
    _MtxrWlApClientCount_Type()
)
mtxrWlApClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlApClientCount.setStatus("current")
_MtxrWlApFreq_Type = Integer32
_MtxrWlApFreq_Object = MibTableColumn
mtxrWlApFreq = _MtxrWlApFreq_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1, 7),
    _MtxrWlApFreq_Type()
)
mtxrWlApFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlApFreq.setStatus("current")
_MtxrWlApBand_Type = DisplayString
_MtxrWlApBand_Object = MibTableColumn
mtxrWlApBand = _MtxrWlApBand_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1, 8),
    _MtxrWlApBand_Type()
)
mtxrWlApBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlApBand.setStatus("current")
_MtxrWlApNoiseFloor_Type = Integer32
_MtxrWlApNoiseFloor_Object = MibTableColumn
mtxrWlApNoiseFloor = _MtxrWlApNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1, 9),
    _MtxrWlApNoiseFloor_Type()
)
mtxrWlApNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlApNoiseFloor.setStatus("current")
_MtxrWlApOverallTxCCQ_Type = Counter32
_MtxrWlApOverallTxCCQ_Object = MibTableColumn
mtxrWlApOverallTxCCQ = _MtxrWlApOverallTxCCQ_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1, 10),
    _MtxrWlApOverallTxCCQ_Type()
)
mtxrWlApOverallTxCCQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlApOverallTxCCQ.setStatus("current")
_MtxrWlApAuthClientCount_Type = Counter32
_MtxrWlApAuthClientCount_Object = MibTableColumn
mtxrWlApAuthClientCount = _MtxrWlApAuthClientCount_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 3, 1, 11),
    _MtxrWlApAuthClientCount_Type()
)
mtxrWlApAuthClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlApAuthClientCount.setStatus("current")
_MtxrWlRtabEntryCount_Type = Gauge32
_MtxrWlRtabEntryCount_Object = MibScalar
mtxrWlRtabEntryCount = _MtxrWlRtabEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 4),
    _MtxrWlRtabEntryCount_Type()
)
mtxrWlRtabEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlRtabEntryCount.setStatus("current")
_MtxrWlCMRtabTable_Object = MibTable
mtxrWlCMRtabTable = _MtxrWlCMRtabTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    mtxrWlCMRtabTable.setStatus("current")
_MtxrWlCMRtabEntry_Object = MibTableRow
mtxrWlCMRtabEntry = _MtxrWlCMRtabEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1)
)
mtxrWlCMRtabEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrWlCMRtabAddr"),
    (0, "MIKROTIK-MIB", "mtxrWlCMRtabIface"),
)
if mibBuilder.loadTexts:
    mtxrWlCMRtabEntry.setStatus("current")
_MtxrWlCMRtabAddr_Type = MacAddress
_MtxrWlCMRtabAddr_Object = MibTableColumn
mtxrWlCMRtabAddr = _MtxrWlCMRtabAddr_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 1),
    _MtxrWlCMRtabAddr_Type()
)
mtxrWlCMRtabAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabAddr.setStatus("current")
_MtxrWlCMRtabIface_Type = ObjectIndex
_MtxrWlCMRtabIface_Object = MibTableColumn
mtxrWlCMRtabIface = _MtxrWlCMRtabIface_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 2),
    _MtxrWlCMRtabIface_Type()
)
mtxrWlCMRtabIface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrWlCMRtabIface.setStatus("current")
_MtxrWlCMRtabUptime_Type = TimeTicks
_MtxrWlCMRtabUptime_Object = MibTableColumn
mtxrWlCMRtabUptime = _MtxrWlCMRtabUptime_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 3),
    _MtxrWlCMRtabUptime_Type()
)
mtxrWlCMRtabUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabUptime.setStatus("current")
_MtxrWlCMRtabTxBytes_Type = Counter32
_MtxrWlCMRtabTxBytes_Object = MibTableColumn
mtxrWlCMRtabTxBytes = _MtxrWlCMRtabTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 4),
    _MtxrWlCMRtabTxBytes_Type()
)
mtxrWlCMRtabTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabTxBytes.setStatus("current")
_MtxrWlCMRtabRxBytes_Type = Counter32
_MtxrWlCMRtabRxBytes_Object = MibTableColumn
mtxrWlCMRtabRxBytes = _MtxrWlCMRtabRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 5),
    _MtxrWlCMRtabRxBytes_Type()
)
mtxrWlCMRtabRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabRxBytes.setStatus("current")
_MtxrWlCMRtabTxPackets_Type = Counter32
_MtxrWlCMRtabTxPackets_Object = MibTableColumn
mtxrWlCMRtabTxPackets = _MtxrWlCMRtabTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 6),
    _MtxrWlCMRtabTxPackets_Type()
)
mtxrWlCMRtabTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabTxPackets.setStatus("current")
_MtxrWlCMRtabRxPackets_Type = Counter32
_MtxrWlCMRtabRxPackets_Object = MibTableColumn
mtxrWlCMRtabRxPackets = _MtxrWlCMRtabRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 7),
    _MtxrWlCMRtabRxPackets_Type()
)
mtxrWlCMRtabRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabRxPackets.setStatus("current")
_MtxrWlCMRtabTxRate_Type = Gauge32
_MtxrWlCMRtabTxRate_Object = MibTableColumn
mtxrWlCMRtabTxRate = _MtxrWlCMRtabTxRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 8),
    _MtxrWlCMRtabTxRate_Type()
)
mtxrWlCMRtabTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabTxRate.setStatus("current")
_MtxrWlCMRtabRxRate_Type = Gauge32
_MtxrWlCMRtabRxRate_Object = MibTableColumn
mtxrWlCMRtabRxRate = _MtxrWlCMRtabRxRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 9),
    _MtxrWlCMRtabRxRate_Type()
)
mtxrWlCMRtabRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabRxRate.setStatus("current")
_MtxrWlCMRtabTxStrength_Type = Integer32
_MtxrWlCMRtabTxStrength_Object = MibTableColumn
mtxrWlCMRtabTxStrength = _MtxrWlCMRtabTxStrength_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 10),
    _MtxrWlCMRtabTxStrength_Type()
)
mtxrWlCMRtabTxStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabTxStrength.setStatus("current")
_MtxrWlCMRtabRxStrength_Type = Integer32
_MtxrWlCMRtabRxStrength_Object = MibTableColumn
mtxrWlCMRtabRxStrength = _MtxrWlCMRtabRxStrength_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 11),
    _MtxrWlCMRtabRxStrength_Type()
)
mtxrWlCMRtabRxStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabRxStrength.setStatus("current")
_MtxrWlCMRtabSsid_Type = DisplayString
_MtxrWlCMRtabSsid_Object = MibTableColumn
mtxrWlCMRtabSsid = _MtxrWlCMRtabSsid_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 5, 1, 12),
    _MtxrWlCMRtabSsid_Type()
)
mtxrWlCMRtabSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabSsid.setStatus("current")
_MtxrWlCMRtabEntryCount_Type = Gauge32
_MtxrWlCMRtabEntryCount_Object = MibScalar
mtxrWlCMRtabEntryCount = _MtxrWlCMRtabEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 1, 6),
    _MtxrWlCMRtabEntryCount_Type()
)
mtxrWlCMRtabEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWlCMRtabEntryCount.setStatus("current")
_MtxrQueues_ObjectIdentity = ObjectIdentity
mtxrQueues = _MtxrQueues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2)
)
_MtxrQueueSimpleTable_Object = MibTable
mtxrQueueSimpleTable = _MtxrQueueSimpleTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mtxrQueueSimpleTable.setStatus("current")
_MtxrQueueSimpleEntry_Object = MibTableRow
mtxrQueueSimpleEntry = _MtxrQueueSimpleEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1)
)
mtxrQueueSimpleEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrQueueSimpleIndex"),
)
if mibBuilder.loadTexts:
    mtxrQueueSimpleEntry.setStatus("current")
_MtxrQueueSimpleIndex_Type = ObjectIndex
_MtxrQueueSimpleIndex_Object = MibTableColumn
mtxrQueueSimpleIndex = _MtxrQueueSimpleIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 1),
    _MtxrQueueSimpleIndex_Type()
)
mtxrQueueSimpleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrQueueSimpleIndex.setStatus("current")
_MtxrQueueSimpleName_Type = DisplayString
_MtxrQueueSimpleName_Object = MibTableColumn
mtxrQueueSimpleName = _MtxrQueueSimpleName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 2),
    _MtxrQueueSimpleName_Type()
)
mtxrQueueSimpleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimpleName.setStatus("current")
_MtxrQueueSimpleSrcAddr_Type = IpAddress
_MtxrQueueSimpleSrcAddr_Object = MibTableColumn
mtxrQueueSimpleSrcAddr = _MtxrQueueSimpleSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 3),
    _MtxrQueueSimpleSrcAddr_Type()
)
mtxrQueueSimpleSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimpleSrcAddr.setStatus("current")
_MtxrQueueSimpleSrcMask_Type = IpAddress
_MtxrQueueSimpleSrcMask_Object = MibTableColumn
mtxrQueueSimpleSrcMask = _MtxrQueueSimpleSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 4),
    _MtxrQueueSimpleSrcMask_Type()
)
mtxrQueueSimpleSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimpleSrcMask.setStatus("current")
_MtxrQueueSimpleDstAddr_Type = IpAddress
_MtxrQueueSimpleDstAddr_Object = MibTableColumn
mtxrQueueSimpleDstAddr = _MtxrQueueSimpleDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 5),
    _MtxrQueueSimpleDstAddr_Type()
)
mtxrQueueSimpleDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimpleDstAddr.setStatus("current")
_MtxrQueueSimpleDstMask_Type = IpAddress
_MtxrQueueSimpleDstMask_Object = MibTableColumn
mtxrQueueSimpleDstMask = _MtxrQueueSimpleDstMask_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 6),
    _MtxrQueueSimpleDstMask_Type()
)
mtxrQueueSimpleDstMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimpleDstMask.setStatus("current")
_MtxrQueueSimpleIface_Type = ObjectIndex
_MtxrQueueSimpleIface_Object = MibTableColumn
mtxrQueueSimpleIface = _MtxrQueueSimpleIface_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 7),
    _MtxrQueueSimpleIface_Type()
)
mtxrQueueSimpleIface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimpleIface.setStatus("current")
_MtxrQueueSimpleBytesIn_Type = Counter64
_MtxrQueueSimpleBytesIn_Object = MibTableColumn
mtxrQueueSimpleBytesIn = _MtxrQueueSimpleBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 8),
    _MtxrQueueSimpleBytesIn_Type()
)
mtxrQueueSimpleBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimpleBytesIn.setStatus("current")
_MtxrQueueSimpleBytesOut_Type = Counter64
_MtxrQueueSimpleBytesOut_Object = MibTableColumn
mtxrQueueSimpleBytesOut = _MtxrQueueSimpleBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 9),
    _MtxrQueueSimpleBytesOut_Type()
)
mtxrQueueSimpleBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimpleBytesOut.setStatus("current")
_MtxrQueueSimplePacketsIn_Type = Counter32
_MtxrQueueSimplePacketsIn_Object = MibTableColumn
mtxrQueueSimplePacketsIn = _MtxrQueueSimplePacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 10),
    _MtxrQueueSimplePacketsIn_Type()
)
mtxrQueueSimplePacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimplePacketsIn.setStatus("current")
_MtxrQueueSimplePacketsOut_Type = Counter32
_MtxrQueueSimplePacketsOut_Object = MibTableColumn
mtxrQueueSimplePacketsOut = _MtxrQueueSimplePacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 11),
    _MtxrQueueSimplePacketsOut_Type()
)
mtxrQueueSimplePacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimplePacketsOut.setStatus("current")
_MtxrQueueSimplePCQQueuesIn_Type = Counter32
_MtxrQueueSimplePCQQueuesIn_Object = MibTableColumn
mtxrQueueSimplePCQQueuesIn = _MtxrQueueSimplePCQQueuesIn_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 12),
    _MtxrQueueSimplePCQQueuesIn_Type()
)
mtxrQueueSimplePCQQueuesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimplePCQQueuesIn.setStatus("current")
_MtxrQueueSimplePCQQueuesOut_Type = Counter32
_MtxrQueueSimplePCQQueuesOut_Object = MibTableColumn
mtxrQueueSimplePCQQueuesOut = _MtxrQueueSimplePCQQueuesOut_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 13),
    _MtxrQueueSimplePCQQueuesOut_Type()
)
mtxrQueueSimplePCQQueuesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimplePCQQueuesOut.setStatus("current")
_MtxrQueueSimpleDroppedIn_Type = Counter32
_MtxrQueueSimpleDroppedIn_Object = MibTableColumn
mtxrQueueSimpleDroppedIn = _MtxrQueueSimpleDroppedIn_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 14),
    _MtxrQueueSimpleDroppedIn_Type()
)
mtxrQueueSimpleDroppedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimpleDroppedIn.setStatus("current")
_MtxrQueueSimpleDroppedOut_Type = Counter32
_MtxrQueueSimpleDroppedOut_Object = MibTableColumn
mtxrQueueSimpleDroppedOut = _MtxrQueueSimpleDroppedOut_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 1, 1, 15),
    _MtxrQueueSimpleDroppedOut_Type()
)
mtxrQueueSimpleDroppedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueSimpleDroppedOut.setStatus("current")
_MtxrQueueTreeTable_Object = MibTable
mtxrQueueTreeTable = _MtxrQueueTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mtxrQueueTreeTable.setStatus("current")
_MtxrQueueTreeEntry_Object = MibTableRow
mtxrQueueTreeEntry = _MtxrQueueTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 2, 1)
)
mtxrQueueTreeEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrQueueTreeIndex"),
)
if mibBuilder.loadTexts:
    mtxrQueueTreeEntry.setStatus("current")
_MtxrQueueTreeIndex_Type = ObjectIndex
_MtxrQueueTreeIndex_Object = MibTableColumn
mtxrQueueTreeIndex = _MtxrQueueTreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 2, 1, 1),
    _MtxrQueueTreeIndex_Type()
)
mtxrQueueTreeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrQueueTreeIndex.setStatus("current")
_MtxrQueueTreeName_Type = DisplayString
_MtxrQueueTreeName_Object = MibTableColumn
mtxrQueueTreeName = _MtxrQueueTreeName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 2, 1, 2),
    _MtxrQueueTreeName_Type()
)
mtxrQueueTreeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueTreeName.setStatus("current")
_MtxrQueueTreeFlow_Type = DisplayString
_MtxrQueueTreeFlow_Object = MibTableColumn
mtxrQueueTreeFlow = _MtxrQueueTreeFlow_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 2, 1, 3),
    _MtxrQueueTreeFlow_Type()
)
mtxrQueueTreeFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueTreeFlow.setStatus("current")
_MtxrQueueTreeParentIndex_Type = ObjectIndex
_MtxrQueueTreeParentIndex_Object = MibTableColumn
mtxrQueueTreeParentIndex = _MtxrQueueTreeParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 2, 1, 4),
    _MtxrQueueTreeParentIndex_Type()
)
mtxrQueueTreeParentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueTreeParentIndex.setStatus("current")
_MtxrQueueTreeBytes_Type = Counter32
_MtxrQueueTreeBytes_Object = MibTableColumn
mtxrQueueTreeBytes = _MtxrQueueTreeBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 2, 1, 5),
    _MtxrQueueTreeBytes_Type()
)
mtxrQueueTreeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueTreeBytes.setStatus("current")
_MtxrQueueTreePackets_Type = Counter32
_MtxrQueueTreePackets_Object = MibTableColumn
mtxrQueueTreePackets = _MtxrQueueTreePackets_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 2, 1, 6),
    _MtxrQueueTreePackets_Type()
)
mtxrQueueTreePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueTreePackets.setStatus("current")
_MtxrQueueTreeHCBytes_Type = Counter64
_MtxrQueueTreeHCBytes_Object = MibTableColumn
mtxrQueueTreeHCBytes = _MtxrQueueTreeHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 2, 1, 7),
    _MtxrQueueTreeHCBytes_Type()
)
mtxrQueueTreeHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueTreeHCBytes.setStatus("current")
_MtxrQueueTreePCQQueues_Type = Counter32
_MtxrQueueTreePCQQueues_Object = MibTableColumn
mtxrQueueTreePCQQueues = _MtxrQueueTreePCQQueues_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 2, 1, 8),
    _MtxrQueueTreePCQQueues_Type()
)
mtxrQueueTreePCQQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueTreePCQQueues.setStatus("current")
_MtxrQueueTreeDropped_Type = Counter32
_MtxrQueueTreeDropped_Object = MibTableColumn
mtxrQueueTreeDropped = _MtxrQueueTreeDropped_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 2, 2, 1, 9),
    _MtxrQueueTreeDropped_Type()
)
mtxrQueueTreeDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrQueueTreeDropped.setStatus("current")
_MtxrHealth_ObjectIdentity = ObjectIdentity
mtxrHealth = _MtxrHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3)
)
_MtxrHlCoreVoltage_Type = Voltage
_MtxrHlCoreVoltage_Object = MibScalar
mtxrHlCoreVoltage = _MtxrHlCoreVoltage_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 1),
    _MtxrHlCoreVoltage_Type()
)
mtxrHlCoreVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlCoreVoltage.setStatus("current")
_MtxrHlThreeDotThreeVoltage_Type = Voltage
_MtxrHlThreeDotThreeVoltage_Object = MibScalar
mtxrHlThreeDotThreeVoltage = _MtxrHlThreeDotThreeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 2),
    _MtxrHlThreeDotThreeVoltage_Type()
)
mtxrHlThreeDotThreeVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlThreeDotThreeVoltage.setStatus("current")
_MtxrHlFiveVoltage_Type = Voltage
_MtxrHlFiveVoltage_Object = MibScalar
mtxrHlFiveVoltage = _MtxrHlFiveVoltage_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 3),
    _MtxrHlFiveVoltage_Type()
)
mtxrHlFiveVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlFiveVoltage.setStatus("current")
_MtxrHlTwelveVoltage_Type = Voltage
_MtxrHlTwelveVoltage_Object = MibScalar
mtxrHlTwelveVoltage = _MtxrHlTwelveVoltage_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 4),
    _MtxrHlTwelveVoltage_Type()
)
mtxrHlTwelveVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlTwelveVoltage.setStatus("current")
_MtxrHlSensorTemperature_Type = Temperature
_MtxrHlSensorTemperature_Object = MibScalar
mtxrHlSensorTemperature = _MtxrHlSensorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 5),
    _MtxrHlSensorTemperature_Type()
)
mtxrHlSensorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlSensorTemperature.setStatus("current")
_MtxrHlCpuTemperature_Type = Temperature
_MtxrHlCpuTemperature_Object = MibScalar
mtxrHlCpuTemperature = _MtxrHlCpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 6),
    _MtxrHlCpuTemperature_Type()
)
mtxrHlCpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlCpuTemperature.setStatus("current")
_MtxrHlBoardTemperature_Type = Temperature
_MtxrHlBoardTemperature_Object = MibScalar
mtxrHlBoardTemperature = _MtxrHlBoardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 7),
    _MtxrHlBoardTemperature_Type()
)
mtxrHlBoardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlBoardTemperature.setStatus("current")
_MtxrHlVoltage_Type = Voltage
_MtxrHlVoltage_Object = MibScalar
mtxrHlVoltage = _MtxrHlVoltage_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 8),
    _MtxrHlVoltage_Type()
)
mtxrHlVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlVoltage.setStatus("current")
_MtxrHlActiveFan_Type = DisplayString
_MtxrHlActiveFan_Object = MibScalar
mtxrHlActiveFan = _MtxrHlActiveFan_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 9),
    _MtxrHlActiveFan_Type()
)
mtxrHlActiveFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlActiveFan.setStatus("current")
_MtxrHlTemperature_Type = Temperature
_MtxrHlTemperature_Object = MibScalar
mtxrHlTemperature = _MtxrHlTemperature_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 10),
    _MtxrHlTemperature_Type()
)
mtxrHlTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlTemperature.setStatus("current")
_MtxrHlProcessorTemperature_Type = Temperature
_MtxrHlProcessorTemperature_Object = MibScalar
mtxrHlProcessorTemperature = _MtxrHlProcessorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 11),
    _MtxrHlProcessorTemperature_Type()
)
mtxrHlProcessorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlProcessorTemperature.setStatus("current")
_MtxrHlPower_Type = Power
_MtxrHlPower_Object = MibScalar
mtxrHlPower = _MtxrHlPower_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 12),
    _MtxrHlPower_Type()
)
mtxrHlPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlPower.setStatus("current")
_MtxrHlCurrent_Type = Integer32
_MtxrHlCurrent_Object = MibScalar
mtxrHlCurrent = _MtxrHlCurrent_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 13),
    _MtxrHlCurrent_Type()
)
mtxrHlCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlCurrent.setStatus("current")
_MtxrHlProcessorFrequency_Type = Integer32
_MtxrHlProcessorFrequency_Object = MibScalar
mtxrHlProcessorFrequency = _MtxrHlProcessorFrequency_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 14),
    _MtxrHlProcessorFrequency_Type()
)
mtxrHlProcessorFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlProcessorFrequency.setStatus("current")
_MtxrHlPowerSupplyState_Type = BoolValue
_MtxrHlPowerSupplyState_Object = MibScalar
mtxrHlPowerSupplyState = _MtxrHlPowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 15),
    _MtxrHlPowerSupplyState_Type()
)
mtxrHlPowerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlPowerSupplyState.setStatus("current")
_MtxrHlBackupPowerSupplyState_Type = BoolValue
_MtxrHlBackupPowerSupplyState_Object = MibScalar
mtxrHlBackupPowerSupplyState = _MtxrHlBackupPowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 16),
    _MtxrHlBackupPowerSupplyState_Type()
)
mtxrHlBackupPowerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlBackupPowerSupplyState.setStatus("current")
_MtxrHlFanSpeed1_Type = DisplayString
_MtxrHlFanSpeed1_Object = MibScalar
mtxrHlFanSpeed1 = _MtxrHlFanSpeed1_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 17),
    _MtxrHlFanSpeed1_Type()
)
mtxrHlFanSpeed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlFanSpeed1.setStatus("current")
_MtxrHlFanSpeed2_Type = DisplayString
_MtxrHlFanSpeed2_Object = MibScalar
mtxrHlFanSpeed2 = _MtxrHlFanSpeed2_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 3, 18),
    _MtxrHlFanSpeed2_Type()
)
mtxrHlFanSpeed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHlFanSpeed2.setStatus("current")
_MtxrLicense_ObjectIdentity = ObjectIdentity
mtxrLicense = _MtxrLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 4)
)
_MtxrLicSoftwareId_Type = DisplayString
_MtxrLicSoftwareId_Object = MibScalar
mtxrLicSoftwareId = _MtxrLicSoftwareId_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 4, 1),
    _MtxrLicSoftwareId_Type()
)
mtxrLicSoftwareId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLicSoftwareId.setStatus("current")
_MtxrLicUpgrUntil_Type = DateAndTime
_MtxrLicUpgrUntil_Object = MibScalar
mtxrLicUpgrUntil = _MtxrLicUpgrUntil_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 4, 2),
    _MtxrLicUpgrUntil_Type()
)
mtxrLicUpgrUntil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLicUpgrUntil.setStatus("current")
_MtxrLicLevel_Type = Integer32
_MtxrLicLevel_Object = MibScalar
mtxrLicLevel = _MtxrLicLevel_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 4, 3),
    _MtxrLicLevel_Type()
)
mtxrLicLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLicLevel.setStatus("current")
_MtxrLicVersion_Type = DisplayString
_MtxrLicVersion_Object = MibScalar
mtxrLicVersion = _MtxrLicVersion_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 4, 4),
    _MtxrLicVersion_Type()
)
mtxrLicVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLicVersion.setStatus("current")
_MtxrLicUpgradableTo_Type = Integer32
_MtxrLicUpgradableTo_Object = MibScalar
mtxrLicUpgradableTo = _MtxrLicUpgradableTo_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 4, 5),
    _MtxrLicUpgradableTo_Type()
)
mtxrLicUpgradableTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLicUpgradableTo.setStatus("current")
_MtxrHotspot_ObjectIdentity = ObjectIdentity
mtxrHotspot = _MtxrHotspot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5)
)
_MtxrHotspotActiveUsersTable_Object = MibTable
mtxrHotspotActiveUsersTable = _MtxrHotspotActiveUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    mtxrHotspotActiveUsersTable.setStatus("current")
_MtxrHotspotActiveUsersTableEntry_Object = MibTableRow
mtxrHotspotActiveUsersTableEntry = _MtxrHotspotActiveUsersTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1)
)
mtxrHotspotActiveUsersTableEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrHotspotActiveUserIndex"),
)
if mibBuilder.loadTexts:
    mtxrHotspotActiveUsersTableEntry.setStatus("current")
_MtxrHotspotActiveUserIndex_Type = ObjectIndex
_MtxrHotspotActiveUserIndex_Object = MibTableColumn
mtxrHotspotActiveUserIndex = _MtxrHotspotActiveUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 1),
    _MtxrHotspotActiveUserIndex_Type()
)
mtxrHotspotActiveUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserIndex.setStatus("current")
_MtxrHotspotActiveUserServerID_Type = Integer32
_MtxrHotspotActiveUserServerID_Object = MibTableColumn
mtxrHotspotActiveUserServerID = _MtxrHotspotActiveUserServerID_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 2),
    _MtxrHotspotActiveUserServerID_Type()
)
mtxrHotspotActiveUserServerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserServerID.setStatus("current")
_MtxrHotspotActiveUserName_Type = DisplayString
_MtxrHotspotActiveUserName_Object = MibTableColumn
mtxrHotspotActiveUserName = _MtxrHotspotActiveUserName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 3),
    _MtxrHotspotActiveUserName_Type()
)
mtxrHotspotActiveUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserName.setStatus("current")
_MtxrHotspotActiveUserDomain_Type = DisplayString
_MtxrHotspotActiveUserDomain_Object = MibTableColumn
mtxrHotspotActiveUserDomain = _MtxrHotspotActiveUserDomain_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 4),
    _MtxrHotspotActiveUserDomain_Type()
)
mtxrHotspotActiveUserDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserDomain.setStatus("current")
_MtxrHotspotActiveUserIP_Type = IpAddress
_MtxrHotspotActiveUserIP_Object = MibTableColumn
mtxrHotspotActiveUserIP = _MtxrHotspotActiveUserIP_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 5),
    _MtxrHotspotActiveUserIP_Type()
)
mtxrHotspotActiveUserIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserIP.setStatus("current")
_MtxrHotspotActiveUserMAC_Type = MacAddress
_MtxrHotspotActiveUserMAC_Object = MibTableColumn
mtxrHotspotActiveUserMAC = _MtxrHotspotActiveUserMAC_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 6),
    _MtxrHotspotActiveUserMAC_Type()
)
mtxrHotspotActiveUserMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserMAC.setStatus("current")
_MtxrHotspotActiveUserConnectTime_Type = Integer32
_MtxrHotspotActiveUserConnectTime_Object = MibTableColumn
mtxrHotspotActiveUserConnectTime = _MtxrHotspotActiveUserConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 7),
    _MtxrHotspotActiveUserConnectTime_Type()
)
mtxrHotspotActiveUserConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserConnectTime.setStatus("current")
_MtxrHotspotActiveUserValidTillTime_Type = Integer32
_MtxrHotspotActiveUserValidTillTime_Object = MibTableColumn
mtxrHotspotActiveUserValidTillTime = _MtxrHotspotActiveUserValidTillTime_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 8),
    _MtxrHotspotActiveUserValidTillTime_Type()
)
mtxrHotspotActiveUserValidTillTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserValidTillTime.setStatus("current")
_MtxrHotspotActiveUserIdleStartTime_Type = Integer32
_MtxrHotspotActiveUserIdleStartTime_Object = MibTableColumn
mtxrHotspotActiveUserIdleStartTime = _MtxrHotspotActiveUserIdleStartTime_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 9),
    _MtxrHotspotActiveUserIdleStartTime_Type()
)
mtxrHotspotActiveUserIdleStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserIdleStartTime.setStatus("current")
_MtxrHotspotActiveUserIdleTimeout_Type = Integer32
_MtxrHotspotActiveUserIdleTimeout_Object = MibTableColumn
mtxrHotspotActiveUserIdleTimeout = _MtxrHotspotActiveUserIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 10),
    _MtxrHotspotActiveUserIdleTimeout_Type()
)
mtxrHotspotActiveUserIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserIdleTimeout.setStatus("current")
_MtxrHotspotActiveUserPingTimeout_Type = Integer32
_MtxrHotspotActiveUserPingTimeout_Object = MibTableColumn
mtxrHotspotActiveUserPingTimeout = _MtxrHotspotActiveUserPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 11),
    _MtxrHotspotActiveUserPingTimeout_Type()
)
mtxrHotspotActiveUserPingTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserPingTimeout.setStatus("current")
_MtxrHotspotActiveUserBytesIn_Type = Counter64
_MtxrHotspotActiveUserBytesIn_Object = MibTableColumn
mtxrHotspotActiveUserBytesIn = _MtxrHotspotActiveUserBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 12),
    _MtxrHotspotActiveUserBytesIn_Type()
)
mtxrHotspotActiveUserBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserBytesIn.setStatus("current")
_MtxrHotspotActiveUserBytesOut_Type = Counter64
_MtxrHotspotActiveUserBytesOut_Object = MibTableColumn
mtxrHotspotActiveUserBytesOut = _MtxrHotspotActiveUserBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 13),
    _MtxrHotspotActiveUserBytesOut_Type()
)
mtxrHotspotActiveUserBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserBytesOut.setStatus("current")
_MtxrHotspotActiveUserPacketsIn_Type = Counter64
_MtxrHotspotActiveUserPacketsIn_Object = MibTableColumn
mtxrHotspotActiveUserPacketsIn = _MtxrHotspotActiveUserPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 14),
    _MtxrHotspotActiveUserPacketsIn_Type()
)
mtxrHotspotActiveUserPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserPacketsIn.setStatus("current")
_MtxrHotspotActiveUserPacketsOut_Type = Counter64
_MtxrHotspotActiveUserPacketsOut_Object = MibTableColumn
mtxrHotspotActiveUserPacketsOut = _MtxrHotspotActiveUserPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 15),
    _MtxrHotspotActiveUserPacketsOut_Type()
)
mtxrHotspotActiveUserPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserPacketsOut.setStatus("current")
_MtxrHotspotActiveUserLimitBytesIn_Type = Counter64
_MtxrHotspotActiveUserLimitBytesIn_Object = MibTableColumn
mtxrHotspotActiveUserLimitBytesIn = _MtxrHotspotActiveUserLimitBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 16),
    _MtxrHotspotActiveUserLimitBytesIn_Type()
)
mtxrHotspotActiveUserLimitBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserLimitBytesIn.setStatus("current")
_MtxrHotspotActiveUserLimitBytesOut_Type = Counter64
_MtxrHotspotActiveUserLimitBytesOut_Object = MibTableColumn
mtxrHotspotActiveUserLimitBytesOut = _MtxrHotspotActiveUserLimitBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 17),
    _MtxrHotspotActiveUserLimitBytesOut_Type()
)
mtxrHotspotActiveUserLimitBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserLimitBytesOut.setStatus("current")
_MtxrHotspotActiveUserAdvertStatus_Type = Integer32
_MtxrHotspotActiveUserAdvertStatus_Object = MibTableColumn
mtxrHotspotActiveUserAdvertStatus = _MtxrHotspotActiveUserAdvertStatus_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 18),
    _MtxrHotspotActiveUserAdvertStatus_Type()
)
mtxrHotspotActiveUserAdvertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserAdvertStatus.setStatus("current")
_MtxrHotspotActiveUserRadius_Type = Integer32
_MtxrHotspotActiveUserRadius_Object = MibTableColumn
mtxrHotspotActiveUserRadius = _MtxrHotspotActiveUserRadius_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 19),
    _MtxrHotspotActiveUserRadius_Type()
)
mtxrHotspotActiveUserRadius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserRadius.setStatus("current")
_MtxrHotspotActiveUserBlockedByAdvert_Type = Integer32
_MtxrHotspotActiveUserBlockedByAdvert_Object = MibTableColumn
mtxrHotspotActiveUserBlockedByAdvert = _MtxrHotspotActiveUserBlockedByAdvert_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 5, 1, 1, 20),
    _MtxrHotspotActiveUserBlockedByAdvert_Type()
)
mtxrHotspotActiveUserBlockedByAdvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserBlockedByAdvert.setStatus("current")
_MtxrDHCP_ObjectIdentity = ObjectIdentity
mtxrDHCP = _MtxrDHCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 6)
)
_MtxrDHCPLeaseCount_Type = Gauge32
_MtxrDHCPLeaseCount_Object = MibScalar
mtxrDHCPLeaseCount = _MtxrDHCPLeaseCount_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 6, 1),
    _MtxrDHCPLeaseCount_Type()
)
mtxrDHCPLeaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrDHCPLeaseCount.setStatus("current")
_MtxrSystem_ObjectIdentity = ObjectIdentity
mtxrSystem = _MtxrSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 7)
)
_MtxrSystemReboot_Type = Integer32
_MtxrSystemReboot_Object = MibScalar
mtxrSystemReboot = _MtxrSystemReboot_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 7, 1),
    _MtxrSystemReboot_Type()
)
mtxrSystemReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtxrSystemReboot.setStatus("current")
_MtxrUSBPowerReset_Type = Integer32
_MtxrUSBPowerReset_Object = MibScalar
mtxrUSBPowerReset = _MtxrUSBPowerReset_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 7, 2),
    _MtxrUSBPowerReset_Type()
)
mtxrUSBPowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtxrUSBPowerReset.setStatus("current")
_MtxrSerialNumber_Type = DisplayString
_MtxrSerialNumber_Object = MibScalar
mtxrSerialNumber = _MtxrSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 7, 3),
    _MtxrSerialNumber_Type()
)
mtxrSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrSerialNumber.setStatus("current")
_MtxrFirmwareVersion_Type = DisplayString
_MtxrFirmwareVersion_Object = MibScalar
mtxrFirmwareVersion = _MtxrFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 7, 4),
    _MtxrFirmwareVersion_Type()
)
mtxrFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrFirmwareVersion.setStatus("current")
_MtxrNote_Type = DisplayString
_MtxrNote_Object = MibScalar
mtxrNote = _MtxrNote_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 7, 5),
    _MtxrNote_Type()
)
mtxrNote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrNote.setStatus("current")
_MtxrBuildTime_Type = DisplayString
_MtxrBuildTime_Object = MibScalar
mtxrBuildTime = _MtxrBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 7, 6),
    _MtxrBuildTime_Type()
)
mtxrBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrBuildTime.setStatus("current")
_MtxrFirmwareUpgradeVersion_Type = DisplayString
_MtxrFirmwareUpgradeVersion_Object = MibScalar
mtxrFirmwareUpgradeVersion = _MtxrFirmwareUpgradeVersion_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 7, 7),
    _MtxrFirmwareUpgradeVersion_Type()
)
mtxrFirmwareUpgradeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrFirmwareUpgradeVersion.setStatus("current")
_MtxrScripts_ObjectIdentity = ObjectIdentity
mtxrScripts = _MtxrScripts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 8)
)
_MtxrScriptTable_Object = MibTable
mtxrScriptTable = _MtxrScriptTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    mtxrScriptTable.setStatus("current")
_MtxrScriptTableEntry_Object = MibTableRow
mtxrScriptTableEntry = _MtxrScriptTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 8, 1, 1)
)
mtxrScriptTableEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrScriptIndex"),
)
if mibBuilder.loadTexts:
    mtxrScriptTableEntry.setStatus("current")
_MtxrScriptIndex_Type = ObjectIndex
_MtxrScriptIndex_Object = MibTableColumn
mtxrScriptIndex = _MtxrScriptIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 8, 1, 1, 1),
    _MtxrScriptIndex_Type()
)
mtxrScriptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrScriptIndex.setStatus("current")
_MtxrScriptName_Type = DisplayString
_MtxrScriptName_Object = MibTableColumn
mtxrScriptName = _MtxrScriptName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 8, 1, 1, 2),
    _MtxrScriptName_Type()
)
mtxrScriptName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrScriptName.setStatus("current")
_MtxrScriptRunCmd_Type = Integer32
_MtxrScriptRunCmd_Object = MibTableColumn
mtxrScriptRunCmd = _MtxrScriptRunCmd_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 8, 1, 1, 3),
    _MtxrScriptRunCmd_Type()
)
mtxrScriptRunCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtxrScriptRunCmd.setStatus("current")
_MtxrTraps_ObjectIdentity = ObjectIdentity
mtxrTraps = _MtxrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 9)
)
_MtxrNotifications_ObjectIdentity = ObjectIdentity
mtxrNotifications = _MtxrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 9, 0)
)
_MtxrNstremeDual_ObjectIdentity = ObjectIdentity
mtxrNstremeDual = _MtxrNstremeDual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 10)
)
_MtxrDnStatTable_Object = MibTable
mtxrDnStatTable = _MtxrDnStatTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    mtxrDnStatTable.setStatus("current")
_MtxrDnStatEntry_Object = MibTableRow
mtxrDnStatEntry = _MtxrDnStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 10, 1, 1)
)
mtxrDnStatEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrDnStatIndex"),
)
if mibBuilder.loadTexts:
    mtxrDnStatEntry.setStatus("current")
_MtxrDnStatIndex_Type = ObjectIndex
_MtxrDnStatIndex_Object = MibTableColumn
mtxrDnStatIndex = _MtxrDnStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 10, 1, 1, 1),
    _MtxrDnStatIndex_Type()
)
mtxrDnStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrDnStatIndex.setStatus("current")
_MtxrDnStatTxRate_Type = Gauge32
_MtxrDnStatTxRate_Object = MibTableColumn
mtxrDnStatTxRate = _MtxrDnStatTxRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 10, 1, 1, 2),
    _MtxrDnStatTxRate_Type()
)
mtxrDnStatTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrDnStatTxRate.setStatus("current")
_MtxrDnStatRxRate_Type = Gauge32
_MtxrDnStatRxRate_Object = MibTableColumn
mtxrDnStatRxRate = _MtxrDnStatRxRate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 10, 1, 1, 3),
    _MtxrDnStatRxRate_Type()
)
mtxrDnStatRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrDnStatRxRate.setStatus("current")
_MtxrDnStatTxStrength_Type = Integer32
_MtxrDnStatTxStrength_Object = MibTableColumn
mtxrDnStatTxStrength = _MtxrDnStatTxStrength_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 10, 1, 1, 4),
    _MtxrDnStatTxStrength_Type()
)
mtxrDnStatTxStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrDnStatTxStrength.setStatus("current")
_MtxrDnStatRxStrength_Type = Integer32
_MtxrDnStatRxStrength_Object = MibTableColumn
mtxrDnStatRxStrength = _MtxrDnStatRxStrength_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 10, 1, 1, 5),
    _MtxrDnStatRxStrength_Type()
)
mtxrDnStatRxStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrDnStatRxStrength.setStatus("current")
_MtxrDnConnected_Type = Integer32
_MtxrDnConnected_Object = MibTableColumn
mtxrDnConnected = _MtxrDnConnected_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 10, 1, 1, 6),
    _MtxrDnConnected_Type()
)
mtxrDnConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrDnConnected.setStatus("current")
_MtxrNeighbor_ObjectIdentity = ObjectIdentity
mtxrNeighbor = _MtxrNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 11)
)
_MtxrNeighborTable_Object = MibTable
mtxrNeighborTable = _MtxrNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    mtxrNeighborTable.setStatus("current")
_MtxrNeighborTableEntry_Object = MibTableRow
mtxrNeighborTableEntry = _MtxrNeighborTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 11, 1, 1)
)
mtxrNeighborTableEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrNeighborIndex"),
)
if mibBuilder.loadTexts:
    mtxrNeighborTableEntry.setStatus("current")
_MtxrNeighborIndex_Type = ObjectIndex
_MtxrNeighborIndex_Object = MibTableColumn
mtxrNeighborIndex = _MtxrNeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 11, 1, 1, 1),
    _MtxrNeighborIndex_Type()
)
mtxrNeighborIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrNeighborIndex.setStatus("current")
_MtxrNeighborIpAddress_Type = IpAddress
_MtxrNeighborIpAddress_Object = MibTableColumn
mtxrNeighborIpAddress = _MtxrNeighborIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 11, 1, 1, 2),
    _MtxrNeighborIpAddress_Type()
)
mtxrNeighborIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrNeighborIpAddress.setStatus("current")
_MtxrNeighborMacAddress_Type = MacAddress
_MtxrNeighborMacAddress_Object = MibTableColumn
mtxrNeighborMacAddress = _MtxrNeighborMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 11, 1, 1, 3),
    _MtxrNeighborMacAddress_Type()
)
mtxrNeighborMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrNeighborMacAddress.setStatus("current")
_MtxrNeighborVersion_Type = DisplayString
_MtxrNeighborVersion_Object = MibTableColumn
mtxrNeighborVersion = _MtxrNeighborVersion_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 11, 1, 1, 4),
    _MtxrNeighborVersion_Type()
)
mtxrNeighborVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrNeighborVersion.setStatus("current")
_MtxrNeighborPlatform_Type = DisplayString
_MtxrNeighborPlatform_Object = MibTableColumn
mtxrNeighborPlatform = _MtxrNeighborPlatform_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 11, 1, 1, 5),
    _MtxrNeighborPlatform_Type()
)
mtxrNeighborPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrNeighborPlatform.setStatus("current")
_MtxrNeighborIdentity_Type = DisplayString
_MtxrNeighborIdentity_Object = MibTableColumn
mtxrNeighborIdentity = _MtxrNeighborIdentity_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 11, 1, 1, 6),
    _MtxrNeighborIdentity_Type()
)
mtxrNeighborIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrNeighborIdentity.setStatus("current")
_MtxrNeighborSoftwareID_Type = DisplayString
_MtxrNeighborSoftwareID_Object = MibTableColumn
mtxrNeighborSoftwareID = _MtxrNeighborSoftwareID_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 11, 1, 1, 7),
    _MtxrNeighborSoftwareID_Type()
)
mtxrNeighborSoftwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrNeighborSoftwareID.setStatus("current")
_MtxrNeighborInterfaceID_Type = ObjectIndex
_MtxrNeighborInterfaceID_Object = MibTableColumn
mtxrNeighborInterfaceID = _MtxrNeighborInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 11, 1, 1, 8),
    _MtxrNeighborInterfaceID_Type()
)
mtxrNeighborInterfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrNeighborInterfaceID.setStatus("current")
_MtxrGps_ObjectIdentity = ObjectIdentity
mtxrGps = _MtxrGps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 12)
)
_MtxrDate_Type = Integer32
_MtxrDate_Object = MibScalar
mtxrDate = _MtxrDate_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 12, 1),
    _MtxrDate_Type()
)
mtxrDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrDate.setStatus("current")
_MtxrLongtitude_Type = DisplayString
_MtxrLongtitude_Object = MibScalar
mtxrLongtitude = _MtxrLongtitude_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 12, 2),
    _MtxrLongtitude_Type()
)
mtxrLongtitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLongtitude.setStatus("current")
_MtxrLatitude_Type = DisplayString
_MtxrLatitude_Object = MibScalar
mtxrLatitude = _MtxrLatitude_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 12, 3),
    _MtxrLatitude_Type()
)
mtxrLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLatitude.setStatus("current")
_MtxrAltitude_Type = DisplayString
_MtxrAltitude_Object = MibScalar
mtxrAltitude = _MtxrAltitude_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 12, 4),
    _MtxrAltitude_Type()
)
mtxrAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrAltitude.setStatus("current")
_MtxrSpeed_Type = DisplayString
_MtxrSpeed_Object = MibScalar
mtxrSpeed = _MtxrSpeed_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 12, 5),
    _MtxrSpeed_Type()
)
mtxrSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrSpeed.setStatus("current")
_MtxrSattelites_Type = Integer32
_MtxrSattelites_Object = MibScalar
mtxrSattelites = _MtxrSattelites_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 12, 6),
    _MtxrSattelites_Type()
)
mtxrSattelites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrSattelites.setStatus("current")
_MtxrValid_Type = Integer32
_MtxrValid_Object = MibScalar
mtxrValid = _MtxrValid_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 12, 7),
    _MtxrValid_Type()
)
mtxrValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrValid.setStatus("current")
_MtxrWirelessModem_ObjectIdentity = ObjectIdentity
mtxrWirelessModem = _MtxrWirelessModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 13)
)
_MtxrWirelessModemSignalStrength_Type = Integer32
_MtxrWirelessModemSignalStrength_Object = MibScalar
mtxrWirelessModemSignalStrength = _MtxrWirelessModemSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 13, 1),
    _MtxrWirelessModemSignalStrength_Type()
)
mtxrWirelessModemSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWirelessModemSignalStrength.setStatus("current")
_MtxrWirelessModemSignalECIO_Type = Integer32
_MtxrWirelessModemSignalECIO_Object = MibScalar
mtxrWirelessModemSignalECIO = _MtxrWirelessModemSignalECIO_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 13, 2),
    _MtxrWirelessModemSignalECIO_Type()
)
mtxrWirelessModemSignalECIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrWirelessModemSignalECIO.setStatus("current")
_MtxrInterfaceStats_ObjectIdentity = ObjectIdentity
mtxrInterfaceStats = _MtxrInterfaceStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14)
)
_MtxrInterfaceStatsTable_Object = MibTable
mtxrInterfaceStatsTable = _MtxrInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1)
)
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTable.setStatus("current")
_MtxrInterfaceStatsEntry_Object = MibTableRow
mtxrInterfaceStatsEntry = _MtxrInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1)
)
mtxrInterfaceStatsEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrInterfaceStatsIndex"),
)
if mibBuilder.loadTexts:
    mtxrInterfaceStatsEntry.setStatus("current")
_MtxrInterfaceStatsIndex_Type = ObjectIndex
_MtxrInterfaceStatsIndex_Object = MibTableColumn
mtxrInterfaceStatsIndex = _MtxrInterfaceStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 1),
    _MtxrInterfaceStatsIndex_Type()
)
mtxrInterfaceStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsIndex.setStatus("current")
_MtxrInterfaceStatsName_Type = DisplayString
_MtxrInterfaceStatsName_Object = MibTableColumn
mtxrInterfaceStatsName = _MtxrInterfaceStatsName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 2),
    _MtxrInterfaceStatsName_Type()
)
mtxrInterfaceStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsName.setStatus("current")
_MtxrInterfaceStatsDriverRxBytes_Type = Counter64
_MtxrInterfaceStatsDriverRxBytes_Object = MibTableColumn
mtxrInterfaceStatsDriverRxBytes = _MtxrInterfaceStatsDriverRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 11),
    _MtxrInterfaceStatsDriverRxBytes_Type()
)
mtxrInterfaceStatsDriverRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsDriverRxBytes.setStatus("current")
_MtxrInterfaceStatsDriverRxPackets_Type = Counter64
_MtxrInterfaceStatsDriverRxPackets_Object = MibTableColumn
mtxrInterfaceStatsDriverRxPackets = _MtxrInterfaceStatsDriverRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 12),
    _MtxrInterfaceStatsDriverRxPackets_Type()
)
mtxrInterfaceStatsDriverRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsDriverRxPackets.setStatus("current")
_MtxrInterfaceStatsDriverTxBytes_Type = Counter64
_MtxrInterfaceStatsDriverTxBytes_Object = MibTableColumn
mtxrInterfaceStatsDriverTxBytes = _MtxrInterfaceStatsDriverTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 13),
    _MtxrInterfaceStatsDriverTxBytes_Type()
)
mtxrInterfaceStatsDriverTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsDriverTxBytes.setStatus("current")
_MtxrInterfaceStatsDriverTxPackets_Type = Counter64
_MtxrInterfaceStatsDriverTxPackets_Object = MibTableColumn
mtxrInterfaceStatsDriverTxPackets = _MtxrInterfaceStatsDriverTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 14),
    _MtxrInterfaceStatsDriverTxPackets_Type()
)
mtxrInterfaceStatsDriverTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsDriverTxPackets.setStatus("current")
_MtxrInterfaceStatsTxRx64_Type = Counter64
_MtxrInterfaceStatsTxRx64_Object = MibTableColumn
mtxrInterfaceStatsTxRx64 = _MtxrInterfaceStatsTxRx64_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 15),
    _MtxrInterfaceStatsTxRx64_Type()
)
mtxrInterfaceStatsTxRx64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxRx64.setStatus("current")
_MtxrInterfaceStatsTxRx65To127_Type = Counter64
_MtxrInterfaceStatsTxRx65To127_Object = MibTableColumn
mtxrInterfaceStatsTxRx65To127 = _MtxrInterfaceStatsTxRx65To127_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 16),
    _MtxrInterfaceStatsTxRx65To127_Type()
)
mtxrInterfaceStatsTxRx65To127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxRx65To127.setStatus("current")
_MtxrInterfaceStatsTxRx128To255_Type = Counter64
_MtxrInterfaceStatsTxRx128To255_Object = MibTableColumn
mtxrInterfaceStatsTxRx128To255 = _MtxrInterfaceStatsTxRx128To255_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 17),
    _MtxrInterfaceStatsTxRx128To255_Type()
)
mtxrInterfaceStatsTxRx128To255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxRx128To255.setStatus("current")
_MtxrInterfaceStatsTxRx256To511_Type = Counter64
_MtxrInterfaceStatsTxRx256To511_Object = MibTableColumn
mtxrInterfaceStatsTxRx256To511 = _MtxrInterfaceStatsTxRx256To511_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 18),
    _MtxrInterfaceStatsTxRx256To511_Type()
)
mtxrInterfaceStatsTxRx256To511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxRx256To511.setStatus("current")
_MtxrInterfaceStatsTxRx512To1023_Type = Counter64
_MtxrInterfaceStatsTxRx512To1023_Object = MibTableColumn
mtxrInterfaceStatsTxRx512To1023 = _MtxrInterfaceStatsTxRx512To1023_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 19),
    _MtxrInterfaceStatsTxRx512To1023_Type()
)
mtxrInterfaceStatsTxRx512To1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxRx512To1023.setStatus("current")
_MtxrInterfaceStatsTxRx1024To1518_Type = Counter64
_MtxrInterfaceStatsTxRx1024To1518_Object = MibTableColumn
mtxrInterfaceStatsTxRx1024To1518 = _MtxrInterfaceStatsTxRx1024To1518_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 20),
    _MtxrInterfaceStatsTxRx1024To1518_Type()
)
mtxrInterfaceStatsTxRx1024To1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxRx1024To1518.setStatus("current")
_MtxrInterfaceStatsTxRx1519ToMax_Type = Counter64
_MtxrInterfaceStatsTxRx1519ToMax_Object = MibTableColumn
mtxrInterfaceStatsTxRx1519ToMax = _MtxrInterfaceStatsTxRx1519ToMax_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 21),
    _MtxrInterfaceStatsTxRx1519ToMax_Type()
)
mtxrInterfaceStatsTxRx1519ToMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxRx1519ToMax.setStatus("current")
_MtxrInterfaceStatsRxBytes_Type = Counter64
_MtxrInterfaceStatsRxBytes_Object = MibTableColumn
mtxrInterfaceStatsRxBytes = _MtxrInterfaceStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 31),
    _MtxrInterfaceStatsRxBytes_Type()
)
mtxrInterfaceStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxBytes.setStatus("current")
_MtxrInterfaceStatsRxPackets_Type = Counter64
_MtxrInterfaceStatsRxPackets_Object = MibTableColumn
mtxrInterfaceStatsRxPackets = _MtxrInterfaceStatsRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 32),
    _MtxrInterfaceStatsRxPackets_Type()
)
mtxrInterfaceStatsRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxPackets.setStatus("current")
_MtxrInterfaceStatsRxTooShort_Type = Counter64
_MtxrInterfaceStatsRxTooShort_Object = MibTableColumn
mtxrInterfaceStatsRxTooShort = _MtxrInterfaceStatsRxTooShort_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 33),
    _MtxrInterfaceStatsRxTooShort_Type()
)
mtxrInterfaceStatsRxTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxTooShort.setStatus("current")
_MtxrInterfaceStatsRx64_Type = Counter64
_MtxrInterfaceStatsRx64_Object = MibTableColumn
mtxrInterfaceStatsRx64 = _MtxrInterfaceStatsRx64_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 34),
    _MtxrInterfaceStatsRx64_Type()
)
mtxrInterfaceStatsRx64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRx64.setStatus("current")
_MtxrInterfaceStatsRx65To127_Type = Counter64
_MtxrInterfaceStatsRx65To127_Object = MibTableColumn
mtxrInterfaceStatsRx65To127 = _MtxrInterfaceStatsRx65To127_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 35),
    _MtxrInterfaceStatsRx65To127_Type()
)
mtxrInterfaceStatsRx65To127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRx65To127.setStatus("current")
_MtxrInterfaceStatsRx128To255_Type = Counter64
_MtxrInterfaceStatsRx128To255_Object = MibTableColumn
mtxrInterfaceStatsRx128To255 = _MtxrInterfaceStatsRx128To255_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 36),
    _MtxrInterfaceStatsRx128To255_Type()
)
mtxrInterfaceStatsRx128To255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRx128To255.setStatus("current")
_MtxrInterfaceStatsRx256To511_Type = Counter64
_MtxrInterfaceStatsRx256To511_Object = MibTableColumn
mtxrInterfaceStatsRx256To511 = _MtxrInterfaceStatsRx256To511_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 37),
    _MtxrInterfaceStatsRx256To511_Type()
)
mtxrInterfaceStatsRx256To511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRx256To511.setStatus("current")
_MtxrInterfaceStatsRx512To1023_Type = Counter64
_MtxrInterfaceStatsRx512To1023_Object = MibTableColumn
mtxrInterfaceStatsRx512To1023 = _MtxrInterfaceStatsRx512To1023_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 38),
    _MtxrInterfaceStatsRx512To1023_Type()
)
mtxrInterfaceStatsRx512To1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRx512To1023.setStatus("current")
_MtxrInterfaceStatsRx1024To1518_Type = Counter64
_MtxrInterfaceStatsRx1024To1518_Object = MibTableColumn
mtxrInterfaceStatsRx1024To1518 = _MtxrInterfaceStatsRx1024To1518_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 39),
    _MtxrInterfaceStatsRx1024To1518_Type()
)
mtxrInterfaceStatsRx1024To1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRx1024To1518.setStatus("current")
_MtxrInterfaceStatsRx1519ToMax_Type = Counter64
_MtxrInterfaceStatsRx1519ToMax_Object = MibTableColumn
mtxrInterfaceStatsRx1519ToMax = _MtxrInterfaceStatsRx1519ToMax_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 40),
    _MtxrInterfaceStatsRx1519ToMax_Type()
)
mtxrInterfaceStatsRx1519ToMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRx1519ToMax.setStatus("current")
_MtxrInterfaceStatsRxTooLong_Type = Counter64
_MtxrInterfaceStatsRxTooLong_Object = MibTableColumn
mtxrInterfaceStatsRxTooLong = _MtxrInterfaceStatsRxTooLong_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 41),
    _MtxrInterfaceStatsRxTooLong_Type()
)
mtxrInterfaceStatsRxTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxTooLong.setStatus("current")
_MtxrInterfaceStatsRxBroadcast_Type = Counter64
_MtxrInterfaceStatsRxBroadcast_Object = MibTableColumn
mtxrInterfaceStatsRxBroadcast = _MtxrInterfaceStatsRxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 42),
    _MtxrInterfaceStatsRxBroadcast_Type()
)
mtxrInterfaceStatsRxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxBroadcast.setStatus("current")
_MtxrInterfaceStatsRxPause_Type = Counter64
_MtxrInterfaceStatsRxPause_Object = MibTableColumn
mtxrInterfaceStatsRxPause = _MtxrInterfaceStatsRxPause_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 43),
    _MtxrInterfaceStatsRxPause_Type()
)
mtxrInterfaceStatsRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxPause.setStatus("current")
_MtxrInterfaceStatsRxMulticast_Type = Counter64
_MtxrInterfaceStatsRxMulticast_Object = MibTableColumn
mtxrInterfaceStatsRxMulticast = _MtxrInterfaceStatsRxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 44),
    _MtxrInterfaceStatsRxMulticast_Type()
)
mtxrInterfaceStatsRxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxMulticast.setStatus("current")
_MtxrInterfaceStatsRxFCSError_Type = Counter64
_MtxrInterfaceStatsRxFCSError_Object = MibTableColumn
mtxrInterfaceStatsRxFCSError = _MtxrInterfaceStatsRxFCSError_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 45),
    _MtxrInterfaceStatsRxFCSError_Type()
)
mtxrInterfaceStatsRxFCSError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxFCSError.setStatus("current")
_MtxrInterfaceStatsRxAlignError_Type = Counter64
_MtxrInterfaceStatsRxAlignError_Object = MibTableColumn
mtxrInterfaceStatsRxAlignError = _MtxrInterfaceStatsRxAlignError_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 46),
    _MtxrInterfaceStatsRxAlignError_Type()
)
mtxrInterfaceStatsRxAlignError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxAlignError.setStatus("current")
_MtxrInterfaceStatsRxFragment_Type = Counter64
_MtxrInterfaceStatsRxFragment_Object = MibTableColumn
mtxrInterfaceStatsRxFragment = _MtxrInterfaceStatsRxFragment_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 47),
    _MtxrInterfaceStatsRxFragment_Type()
)
mtxrInterfaceStatsRxFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxFragment.setStatus("current")
_MtxrInterfaceStatsRxOverflow_Type = Counter64
_MtxrInterfaceStatsRxOverflow_Object = MibTableColumn
mtxrInterfaceStatsRxOverflow = _MtxrInterfaceStatsRxOverflow_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 48),
    _MtxrInterfaceStatsRxOverflow_Type()
)
mtxrInterfaceStatsRxOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxOverflow.setStatus("current")
_MtxrInterfaceStatsRxControl_Type = Counter64
_MtxrInterfaceStatsRxControl_Object = MibTableColumn
mtxrInterfaceStatsRxControl = _MtxrInterfaceStatsRxControl_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 49),
    _MtxrInterfaceStatsRxControl_Type()
)
mtxrInterfaceStatsRxControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxControl.setStatus("current")
_MtxrInterfaceStatsRxUnknownOp_Type = Counter64
_MtxrInterfaceStatsRxUnknownOp_Object = MibTableColumn
mtxrInterfaceStatsRxUnknownOp = _MtxrInterfaceStatsRxUnknownOp_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 50),
    _MtxrInterfaceStatsRxUnknownOp_Type()
)
mtxrInterfaceStatsRxUnknownOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxUnknownOp.setStatus("current")
_MtxrInterfaceStatsRxLengthError_Type = Counter64
_MtxrInterfaceStatsRxLengthError_Object = MibTableColumn
mtxrInterfaceStatsRxLengthError = _MtxrInterfaceStatsRxLengthError_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 51),
    _MtxrInterfaceStatsRxLengthError_Type()
)
mtxrInterfaceStatsRxLengthError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxLengthError.setStatus("current")
_MtxrInterfaceStatsRxCodeError_Type = Counter64
_MtxrInterfaceStatsRxCodeError_Object = MibTableColumn
mtxrInterfaceStatsRxCodeError = _MtxrInterfaceStatsRxCodeError_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 52),
    _MtxrInterfaceStatsRxCodeError_Type()
)
mtxrInterfaceStatsRxCodeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxCodeError.setStatus("current")
_MtxrInterfaceStatsRxCarrierError_Type = Counter64
_MtxrInterfaceStatsRxCarrierError_Object = MibTableColumn
mtxrInterfaceStatsRxCarrierError = _MtxrInterfaceStatsRxCarrierError_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 53),
    _MtxrInterfaceStatsRxCarrierError_Type()
)
mtxrInterfaceStatsRxCarrierError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxCarrierError.setStatus("current")
_MtxrInterfaceStatsRxJabber_Type = Counter64
_MtxrInterfaceStatsRxJabber_Object = MibTableColumn
mtxrInterfaceStatsRxJabber = _MtxrInterfaceStatsRxJabber_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 54),
    _MtxrInterfaceStatsRxJabber_Type()
)
mtxrInterfaceStatsRxJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxJabber.setStatus("current")
_MtxrInterfaceStatsRxDrop_Type = Counter64
_MtxrInterfaceStatsRxDrop_Object = MibTableColumn
mtxrInterfaceStatsRxDrop = _MtxrInterfaceStatsRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 55),
    _MtxrInterfaceStatsRxDrop_Type()
)
mtxrInterfaceStatsRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsRxDrop.setStatus("current")
_MtxrInterfaceStatsTxBytes_Type = Counter64
_MtxrInterfaceStatsTxBytes_Object = MibTableColumn
mtxrInterfaceStatsTxBytes = _MtxrInterfaceStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 61),
    _MtxrInterfaceStatsTxBytes_Type()
)
mtxrInterfaceStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxBytes.setStatus("current")
_MtxrInterfaceStatsTxPackets_Type = Counter64
_MtxrInterfaceStatsTxPackets_Object = MibTableColumn
mtxrInterfaceStatsTxPackets = _MtxrInterfaceStatsTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 62),
    _MtxrInterfaceStatsTxPackets_Type()
)
mtxrInterfaceStatsTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxPackets.setStatus("current")
_MtxrInterfaceStatsTxTooShort_Type = Counter64
_MtxrInterfaceStatsTxTooShort_Object = MibTableColumn
mtxrInterfaceStatsTxTooShort = _MtxrInterfaceStatsTxTooShort_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 63),
    _MtxrInterfaceStatsTxTooShort_Type()
)
mtxrInterfaceStatsTxTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxTooShort.setStatus("current")
_MtxrInterfaceStatsTx64_Type = Counter64
_MtxrInterfaceStatsTx64_Object = MibTableColumn
mtxrInterfaceStatsTx64 = _MtxrInterfaceStatsTx64_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 64),
    _MtxrInterfaceStatsTx64_Type()
)
mtxrInterfaceStatsTx64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTx64.setStatus("current")
_MtxrInterfaceStatsTx65To127_Type = Counter64
_MtxrInterfaceStatsTx65To127_Object = MibTableColumn
mtxrInterfaceStatsTx65To127 = _MtxrInterfaceStatsTx65To127_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 65),
    _MtxrInterfaceStatsTx65To127_Type()
)
mtxrInterfaceStatsTx65To127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTx65To127.setStatus("current")
_MtxrInterfaceStatsTx128To255_Type = Counter64
_MtxrInterfaceStatsTx128To255_Object = MibTableColumn
mtxrInterfaceStatsTx128To255 = _MtxrInterfaceStatsTx128To255_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 66),
    _MtxrInterfaceStatsTx128To255_Type()
)
mtxrInterfaceStatsTx128To255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTx128To255.setStatus("current")
_MtxrInterfaceStatsTx256To511_Type = Counter64
_MtxrInterfaceStatsTx256To511_Object = MibTableColumn
mtxrInterfaceStatsTx256To511 = _MtxrInterfaceStatsTx256To511_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 67),
    _MtxrInterfaceStatsTx256To511_Type()
)
mtxrInterfaceStatsTx256To511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTx256To511.setStatus("current")
_MtxrInterfaceStatsTx512To1023_Type = Counter64
_MtxrInterfaceStatsTx512To1023_Object = MibTableColumn
mtxrInterfaceStatsTx512To1023 = _MtxrInterfaceStatsTx512To1023_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 68),
    _MtxrInterfaceStatsTx512To1023_Type()
)
mtxrInterfaceStatsTx512To1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTx512To1023.setStatus("current")
_MtxrInterfaceStatsTx1024To1518_Type = Counter64
_MtxrInterfaceStatsTx1024To1518_Object = MibTableColumn
mtxrInterfaceStatsTx1024To1518 = _MtxrInterfaceStatsTx1024To1518_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 69),
    _MtxrInterfaceStatsTx1024To1518_Type()
)
mtxrInterfaceStatsTx1024To1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTx1024To1518.setStatus("current")
_MtxrInterfaceStatsTx1519ToMax_Type = Counter64
_MtxrInterfaceStatsTx1519ToMax_Object = MibTableColumn
mtxrInterfaceStatsTx1519ToMax = _MtxrInterfaceStatsTx1519ToMax_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 70),
    _MtxrInterfaceStatsTx1519ToMax_Type()
)
mtxrInterfaceStatsTx1519ToMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTx1519ToMax.setStatus("current")
_MtxrInterfaceStatsTxTooLong_Type = Counter64
_MtxrInterfaceStatsTxTooLong_Object = MibTableColumn
mtxrInterfaceStatsTxTooLong = _MtxrInterfaceStatsTxTooLong_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 71),
    _MtxrInterfaceStatsTxTooLong_Type()
)
mtxrInterfaceStatsTxTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxTooLong.setStatus("current")
_MtxrInterfaceStatsTxBroadcast_Type = Counter64
_MtxrInterfaceStatsTxBroadcast_Object = MibTableColumn
mtxrInterfaceStatsTxBroadcast = _MtxrInterfaceStatsTxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 72),
    _MtxrInterfaceStatsTxBroadcast_Type()
)
mtxrInterfaceStatsTxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxBroadcast.setStatus("current")
_MtxrInterfaceStatsTxPause_Type = Counter64
_MtxrInterfaceStatsTxPause_Object = MibTableColumn
mtxrInterfaceStatsTxPause = _MtxrInterfaceStatsTxPause_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 73),
    _MtxrInterfaceStatsTxPause_Type()
)
mtxrInterfaceStatsTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxPause.setStatus("current")
_MtxrInterfaceStatsTxMulticast_Type = Counter64
_MtxrInterfaceStatsTxMulticast_Object = MibTableColumn
mtxrInterfaceStatsTxMulticast = _MtxrInterfaceStatsTxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 74),
    _MtxrInterfaceStatsTxMulticast_Type()
)
mtxrInterfaceStatsTxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxMulticast.setStatus("current")
_MtxrInterfaceStatsTxUnderrun_Type = Counter64
_MtxrInterfaceStatsTxUnderrun_Object = MibTableColumn
mtxrInterfaceStatsTxUnderrun = _MtxrInterfaceStatsTxUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 75),
    _MtxrInterfaceStatsTxUnderrun_Type()
)
mtxrInterfaceStatsTxUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxUnderrun.setStatus("current")
_MtxrInterfaceStatsTxCollision_Type = Counter64
_MtxrInterfaceStatsTxCollision_Object = MibTableColumn
mtxrInterfaceStatsTxCollision = _MtxrInterfaceStatsTxCollision_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 76),
    _MtxrInterfaceStatsTxCollision_Type()
)
mtxrInterfaceStatsTxCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxCollision.setStatus("current")
_MtxrInterfaceStatsTxExcessiveCollision_Type = Counter64
_MtxrInterfaceStatsTxExcessiveCollision_Object = MibTableColumn
mtxrInterfaceStatsTxExcessiveCollision = _MtxrInterfaceStatsTxExcessiveCollision_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 77),
    _MtxrInterfaceStatsTxExcessiveCollision_Type()
)
mtxrInterfaceStatsTxExcessiveCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxExcessiveCollision.setStatus("current")
_MtxrInterfaceStatsTxMultipleCollision_Type = Counter64
_MtxrInterfaceStatsTxMultipleCollision_Object = MibTableColumn
mtxrInterfaceStatsTxMultipleCollision = _MtxrInterfaceStatsTxMultipleCollision_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 78),
    _MtxrInterfaceStatsTxMultipleCollision_Type()
)
mtxrInterfaceStatsTxMultipleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxMultipleCollision.setStatus("current")
_MtxrInterfaceStatsTxSingleCollision_Type = Counter64
_MtxrInterfaceStatsTxSingleCollision_Object = MibTableColumn
mtxrInterfaceStatsTxSingleCollision = _MtxrInterfaceStatsTxSingleCollision_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 79),
    _MtxrInterfaceStatsTxSingleCollision_Type()
)
mtxrInterfaceStatsTxSingleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxSingleCollision.setStatus("current")
_MtxrInterfaceStatsTxExcessiveDeferred_Type = Counter64
_MtxrInterfaceStatsTxExcessiveDeferred_Object = MibTableColumn
mtxrInterfaceStatsTxExcessiveDeferred = _MtxrInterfaceStatsTxExcessiveDeferred_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 80),
    _MtxrInterfaceStatsTxExcessiveDeferred_Type()
)
mtxrInterfaceStatsTxExcessiveDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxExcessiveDeferred.setStatus("current")
_MtxrInterfaceStatsTxDeferred_Type = Counter64
_MtxrInterfaceStatsTxDeferred_Object = MibTableColumn
mtxrInterfaceStatsTxDeferred = _MtxrInterfaceStatsTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 81),
    _MtxrInterfaceStatsTxDeferred_Type()
)
mtxrInterfaceStatsTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxDeferred.setStatus("current")
_MtxrInterfaceStatsTxLateCollision_Type = Counter64
_MtxrInterfaceStatsTxLateCollision_Object = MibTableColumn
mtxrInterfaceStatsTxLateCollision = _MtxrInterfaceStatsTxLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 82),
    _MtxrInterfaceStatsTxLateCollision_Type()
)
mtxrInterfaceStatsTxLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxLateCollision.setStatus("current")
_MtxrInterfaceStatsTxTotalCollision_Type = Counter64
_MtxrInterfaceStatsTxTotalCollision_Object = MibTableColumn
mtxrInterfaceStatsTxTotalCollision = _MtxrInterfaceStatsTxTotalCollision_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 83),
    _MtxrInterfaceStatsTxTotalCollision_Type()
)
mtxrInterfaceStatsTxTotalCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxTotalCollision.setStatus("current")
_MtxrInterfaceStatsTxPauseHonored_Type = Counter64
_MtxrInterfaceStatsTxPauseHonored_Object = MibTableColumn
mtxrInterfaceStatsTxPauseHonored = _MtxrInterfaceStatsTxPauseHonored_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 84),
    _MtxrInterfaceStatsTxPauseHonored_Type()
)
mtxrInterfaceStatsTxPauseHonored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxPauseHonored.setStatus("current")
_MtxrInterfaceStatsTxDrop_Type = Counter64
_MtxrInterfaceStatsTxDrop_Object = MibTableColumn
mtxrInterfaceStatsTxDrop = _MtxrInterfaceStatsTxDrop_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 85),
    _MtxrInterfaceStatsTxDrop_Type()
)
mtxrInterfaceStatsTxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxDrop.setStatus("current")
_MtxrInterfaceStatsTxJabber_Type = Counter64
_MtxrInterfaceStatsTxJabber_Object = MibTableColumn
mtxrInterfaceStatsTxJabber = _MtxrInterfaceStatsTxJabber_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 86),
    _MtxrInterfaceStatsTxJabber_Type()
)
mtxrInterfaceStatsTxJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxJabber.setStatus("current")
_MtxrInterfaceStatsTxFCSError_Type = Counter64
_MtxrInterfaceStatsTxFCSError_Object = MibTableColumn
mtxrInterfaceStatsTxFCSError = _MtxrInterfaceStatsTxFCSError_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 87),
    _MtxrInterfaceStatsTxFCSError_Type()
)
mtxrInterfaceStatsTxFCSError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxFCSError.setStatus("current")
_MtxrInterfaceStatsTxControl_Type = Counter64
_MtxrInterfaceStatsTxControl_Object = MibTableColumn
mtxrInterfaceStatsTxControl = _MtxrInterfaceStatsTxControl_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 88),
    _MtxrInterfaceStatsTxControl_Type()
)
mtxrInterfaceStatsTxControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxControl.setStatus("current")
_MtxrInterfaceStatsTxFragment_Type = Counter64
_MtxrInterfaceStatsTxFragment_Object = MibTableColumn
mtxrInterfaceStatsTxFragment = _MtxrInterfaceStatsTxFragment_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 14, 1, 1, 89),
    _MtxrInterfaceStatsTxFragment_Type()
)
mtxrInterfaceStatsTxFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrInterfaceStatsTxFragment.setStatus("current")
_MtxrPOE_ObjectIdentity = ObjectIdentity
mtxrPOE = _MtxrPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 15)
)
_MtxrPOETable_Object = MibTable
mtxrPOETable = _MtxrPOETable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 15, 1)
)
if mibBuilder.loadTexts:
    mtxrPOETable.setStatus("current")
_MtxrPOEEntry_Object = MibTableRow
mtxrPOEEntry = _MtxrPOEEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 15, 1, 1)
)
mtxrPOEEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrPOEInterfaceIndex"),
)
if mibBuilder.loadTexts:
    mtxrPOEEntry.setStatus("current")
_MtxrPOEInterfaceIndex_Type = ObjectIndex
_MtxrPOEInterfaceIndex_Object = MibTableColumn
mtxrPOEInterfaceIndex = _MtxrPOEInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 15, 1, 1, 1),
    _MtxrPOEInterfaceIndex_Type()
)
mtxrPOEInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrPOEInterfaceIndex.setStatus("current")
_MtxrPOEName_Type = DisplayString
_MtxrPOEName_Object = MibTableColumn
mtxrPOEName = _MtxrPOEName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 15, 1, 1, 2),
    _MtxrPOEName_Type()
)
mtxrPOEName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrPOEName.setStatus("current")


class _MtxrPOEStatus_Type(Integer32):
    """Custom type mtxrPOEStatus based on Integer32"""
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
        *(("disabled", 1),
          ("overload", 4),
          ("poweredOn", 3),
          ("waitingForLoad", 2))
    )


_MtxrPOEStatus_Type.__name__ = "Integer32"
_MtxrPOEStatus_Object = MibTableColumn
mtxrPOEStatus = _MtxrPOEStatus_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 15, 1, 1, 3),
    _MtxrPOEStatus_Type()
)
mtxrPOEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrPOEStatus.setStatus("current")
_MtxrPOEVoltage_Type = Voltage
_MtxrPOEVoltage_Object = MibTableColumn
mtxrPOEVoltage = _MtxrPOEVoltage_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 15, 1, 1, 4),
    _MtxrPOEVoltage_Type()
)
mtxrPOEVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrPOEVoltage.setStatus("current")
_MtxrPOECurrent_Type = Integer32
_MtxrPOECurrent_Object = MibTableColumn
mtxrPOECurrent = _MtxrPOECurrent_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 15, 1, 1, 5),
    _MtxrPOECurrent_Type()
)
mtxrPOECurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrPOECurrent.setStatus("current")
_MtxrPOEPower_Type = Power
_MtxrPOEPower_Object = MibTableColumn
mtxrPOEPower = _MtxrPOEPower_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 15, 1, 1, 6),
    _MtxrPOEPower_Type()
)
mtxrPOEPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrPOEPower.setStatus("current")
_MtxrLTEModem_ObjectIdentity = ObjectIdentity
mtxrLTEModem = _MtxrLTEModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16)
)
_MtxrLTEModemTable_Object = MibTable
mtxrLTEModemTable = _MtxrLTEModemTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1)
)
if mibBuilder.loadTexts:
    mtxrLTEModemTable.setStatus("current")
_MtxrLTEModemEntry_Object = MibTableRow
mtxrLTEModemEntry = _MtxrLTEModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1)
)
mtxrLTEModemEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrLTEModemInterfaceIndex"),
)
if mibBuilder.loadTexts:
    mtxrLTEModemEntry.setStatus("current")
_MtxrLTEModemInterfaceIndex_Type = ObjectIndex
_MtxrLTEModemInterfaceIndex_Object = MibTableColumn
mtxrLTEModemInterfaceIndex = _MtxrLTEModemInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1, 1),
    _MtxrLTEModemInterfaceIndex_Type()
)
mtxrLTEModemInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrLTEModemInterfaceIndex.setStatus("current")
_MtxrLTEModemSignalRSSI_Type = Integer32
_MtxrLTEModemSignalRSSI_Object = MibTableColumn
mtxrLTEModemSignalRSSI = _MtxrLTEModemSignalRSSI_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1, 2),
    _MtxrLTEModemSignalRSSI_Type()
)
mtxrLTEModemSignalRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLTEModemSignalRSSI.setStatus("current")
_MtxrLTEModemSignalRSRQ_Type = Integer32
_MtxrLTEModemSignalRSRQ_Object = MibTableColumn
mtxrLTEModemSignalRSRQ = _MtxrLTEModemSignalRSRQ_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1, 3),
    _MtxrLTEModemSignalRSRQ_Type()
)
mtxrLTEModemSignalRSRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLTEModemSignalRSRQ.setStatus("current")
_MtxrLTEModemSignalRSRP_Type = Integer32
_MtxrLTEModemSignalRSRP_Object = MibTableColumn
mtxrLTEModemSignalRSRP = _MtxrLTEModemSignalRSRP_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1, 4),
    _MtxrLTEModemSignalRSRP_Type()
)
mtxrLTEModemSignalRSRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLTEModemSignalRSRP.setStatus("current")
_MtxrLTEModemCellId_Type = HexInt
_MtxrLTEModemCellId_Object = MibTableColumn
mtxrLTEModemCellId = _MtxrLTEModemCellId_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1, 5),
    _MtxrLTEModemCellId_Type()
)
mtxrLTEModemCellId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLTEModemCellId.setStatus("current")


class _MtxrLTEModemAccessTechnology_Type(Integer32):
    """Custom type mtxrLTEModemAccessTechnology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
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
        *(("egprs", 3),
          ("eutran", 7),
          ("gsm", 1),
          ("gsmcompact", 0),
          ("hsdpa", 4),
          ("hsdpahsupa", 6),
          ("hsupa", 5),
          ("unknown", -1),
          ("utran", 2))
    )


_MtxrLTEModemAccessTechnology_Type.__name__ = "Integer32"
_MtxrLTEModemAccessTechnology_Object = MibTableColumn
mtxrLTEModemAccessTechnology = _MtxrLTEModemAccessTechnology_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1, 6),
    _MtxrLTEModemAccessTechnology_Type()
)
mtxrLTEModemAccessTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLTEModemAccessTechnology.setStatus("current")
_MtxrLTEModemSignalSINR_Type = Integer32
_MtxrLTEModemSignalSINR_Object = MibTableColumn
mtxrLTEModemSignalSINR = _MtxrLTEModemSignalSINR_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 16, 1, 1, 7),
    _MtxrLTEModemSignalSINR_Type()
)
mtxrLTEModemSignalSINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrLTEModemSignalSINR.setStatus("current")
_MtxrPartition_ObjectIdentity = ObjectIdentity
mtxrPartition = _MtxrPartition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 17)
)
_MtxrPartitionTable_Object = MibTable
mtxrPartitionTable = _MtxrPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 17, 1)
)
if mibBuilder.loadTexts:
    mtxrPartitionTable.setStatus("current")
_MtxrPartitionEntry_Object = MibTableRow
mtxrPartitionEntry = _MtxrPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 17, 1, 1)
)
mtxrPartitionEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrPartitionIndex"),
)
if mibBuilder.loadTexts:
    mtxrPartitionEntry.setStatus("current")
_MtxrPartitionIndex_Type = ObjectIndex
_MtxrPartitionIndex_Object = MibTableColumn
mtxrPartitionIndex = _MtxrPartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 17, 1, 1, 1),
    _MtxrPartitionIndex_Type()
)
mtxrPartitionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrPartitionIndex.setStatus("current")
_MtxrPartitionName_Type = DisplayString
_MtxrPartitionName_Object = MibTableColumn
mtxrPartitionName = _MtxrPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 17, 1, 1, 2),
    _MtxrPartitionName_Type()
)
mtxrPartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrPartitionName.setStatus("current")
_MtxrPartitionSize_Type = Integer32
_MtxrPartitionSize_Object = MibTableColumn
mtxrPartitionSize = _MtxrPartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 17, 1, 1, 3),
    _MtxrPartitionSize_Type()
)
mtxrPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrPartitionSize.setStatus("current")
_MtxrPartitionVersion_Type = DisplayString
_MtxrPartitionVersion_Object = MibTableColumn
mtxrPartitionVersion = _MtxrPartitionVersion_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 17, 1, 1, 4),
    _MtxrPartitionVersion_Type()
)
mtxrPartitionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrPartitionVersion.setStatus("current")
_MtxrPartitionActive_Type = BoolValue
_MtxrPartitionActive_Object = MibTableColumn
mtxrPartitionActive = _MtxrPartitionActive_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 17, 1, 1, 5),
    _MtxrPartitionActive_Type()
)
mtxrPartitionActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrPartitionActive.setStatus("current")
_MtxrPartitionRunning_Type = BoolValue
_MtxrPartitionRunning_Object = MibTableColumn
mtxrPartitionRunning = _MtxrPartitionRunning_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 17, 1, 1, 6),
    _MtxrPartitionRunning_Type()
)
mtxrPartitionRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrPartitionRunning.setStatus("current")
_MtxrScriptRun_ObjectIdentity = ObjectIdentity
mtxrScriptRun = _MtxrScriptRun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 18)
)
_MtxrScriptRunTable_Object = MibTable
mtxrScriptRunTable = _MtxrScriptRunTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 18, 1)
)
if mibBuilder.loadTexts:
    mtxrScriptRunTable.setStatus("current")
_MtxrScriptRunTableEntry_Object = MibTableRow
mtxrScriptRunTableEntry = _MtxrScriptRunTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 18, 1, 1)
)
mtxrScriptRunTableEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrScriptRunIndex"),
)
if mibBuilder.loadTexts:
    mtxrScriptRunTableEntry.setStatus("current")
_MtxrScriptRunIndex_Type = ObjectIndex
_MtxrScriptRunIndex_Object = MibTableColumn
mtxrScriptRunIndex = _MtxrScriptRunIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 18, 1, 1, 1),
    _MtxrScriptRunIndex_Type()
)
mtxrScriptRunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrScriptRunIndex.setStatus("current")
_MtxrScriptRunOutput_Type = DisplayString
_MtxrScriptRunOutput_Object = MibTableColumn
mtxrScriptRunOutput = _MtxrScriptRunOutput_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 18, 1, 1, 2),
    _MtxrScriptRunOutput_Type()
)
mtxrScriptRunOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrScriptRunOutput.setStatus("current")
_MtxrOptical_ObjectIdentity = ObjectIdentity
mtxrOptical = _MtxrOptical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19)
)
_MtxrOpticalTable_Object = MibTable
mtxrOpticalTable = _MtxrOpticalTable_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1)
)
if mibBuilder.loadTexts:
    mtxrOpticalTable.setStatus("current")
_MtxrOpticalTableEntry_Object = MibTableRow
mtxrOpticalTableEntry = _MtxrOpticalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1)
)
mtxrOpticalTableEntry.setIndexNames(
    (0, "MIKROTIK-MIB", "mtxrOpticalIndex"),
)
if mibBuilder.loadTexts:
    mtxrOpticalTableEntry.setStatus("current")
_MtxrOpticalIndex_Type = ObjectIndex
_MtxrOpticalIndex_Object = MibTableColumn
mtxrOpticalIndex = _MtxrOpticalIndex_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1, 1),
    _MtxrOpticalIndex_Type()
)
mtxrOpticalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtxrOpticalIndex.setStatus("current")
_MtxrOpticalName_Type = DisplayString
_MtxrOpticalName_Object = MibTableColumn
mtxrOpticalName = _MtxrOpticalName_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1, 2),
    _MtxrOpticalName_Type()
)
mtxrOpticalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrOpticalName.setStatus("current")
_MtxrOpticalRxLoss_Type = BoolValue
_MtxrOpticalRxLoss_Object = MibTableColumn
mtxrOpticalRxLoss = _MtxrOpticalRxLoss_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1, 3),
    _MtxrOpticalRxLoss_Type()
)
mtxrOpticalRxLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrOpticalRxLoss.setStatus("current")
_MtxrOpticalTxFault_Type = BoolValue
_MtxrOpticalTxFault_Object = MibTableColumn
mtxrOpticalTxFault = _MtxrOpticalTxFault_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1, 4),
    _MtxrOpticalTxFault_Type()
)
mtxrOpticalTxFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrOpticalTxFault.setStatus("current")
_MtxrOpticalWavelength_Type = GDiv100
_MtxrOpticalWavelength_Object = MibTableColumn
mtxrOpticalWavelength = _MtxrOpticalWavelength_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1, 5),
    _MtxrOpticalWavelength_Type()
)
mtxrOpticalWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrOpticalWavelength.setStatus("current")
if mibBuilder.loadTexts:
    mtxrOpticalWavelength.setUnits("nm")
_MtxrOpticalTemperature_Type = Gauge32
_MtxrOpticalTemperature_Object = MibTableColumn
mtxrOpticalTemperature = _MtxrOpticalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1, 6),
    _MtxrOpticalTemperature_Type()
)
mtxrOpticalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrOpticalTemperature.setStatus("current")
if mibBuilder.loadTexts:
    mtxrOpticalTemperature.setUnits("C")
_MtxrOpticalSupplyVoltage_Type = GDiv1000
_MtxrOpticalSupplyVoltage_Object = MibTableColumn
mtxrOpticalSupplyVoltage = _MtxrOpticalSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1, 7),
    _MtxrOpticalSupplyVoltage_Type()
)
mtxrOpticalSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrOpticalSupplyVoltage.setStatus("current")
if mibBuilder.loadTexts:
    mtxrOpticalSupplyVoltage.setUnits("V")
_MtxrOpticalTxBiasCurrent_Type = Gauge32
_MtxrOpticalTxBiasCurrent_Object = MibTableColumn
mtxrOpticalTxBiasCurrent = _MtxrOpticalTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1, 8),
    _MtxrOpticalTxBiasCurrent_Type()
)
mtxrOpticalTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrOpticalTxBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    mtxrOpticalTxBiasCurrent.setUnits("mA")
_MtxrOpticalTxPower_Type = IDiv1000
_MtxrOpticalTxPower_Object = MibTableColumn
mtxrOpticalTxPower = _MtxrOpticalTxPower_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1, 9),
    _MtxrOpticalTxPower_Type()
)
mtxrOpticalTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrOpticalTxPower.setStatus("current")
if mibBuilder.loadTexts:
    mtxrOpticalTxPower.setUnits("dBm")
_MtxrOpticalRxPower_Type = IDiv1000
_MtxrOpticalRxPower_Object = MibTableColumn
mtxrOpticalRxPower = _MtxrOpticalRxPower_Object(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 19, 1, 1, 10),
    _MtxrOpticalRxPower_Type()
)
mtxrOpticalRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtxrOpticalRxPower.setStatus("current")
if mibBuilder.loadTexts:
    mtxrOpticalRxPower.setUnits("dBm")
_MtXMetaInfo_ObjectIdentity = ObjectIdentity
mtXMetaInfo = _MtXMetaInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2)
)
_MtXRouterOsGroups_ObjectIdentity = ObjectIdentity
mtXRouterOsGroups = _MtXRouterOsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1)
)

# Managed Objects groups

mtxrWirelessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 1)
)
mtxrWirelessGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrWlStatTxRate"),
        ("MIKROTIK-MIB", "mtxrWlStatRxRate"),
        ("MIKROTIK-MIB", "mtxrWlStatStrength"),
        ("MIKROTIK-MIB", "mtxrWlStatSsid"),
        ("MIKROTIK-MIB", "mtxrWlStatBssid"),
        ("MIKROTIK-MIB", "mtxrWlStatFreq"),
        ("MIKROTIK-MIB", "mtxrWlStatBand"),
        ("MIKROTIK-MIB", "mtxrWlRtabStrength"),
        ("MIKROTIK-MIB", "mtxrWlRtabTxBytes"),
        ("MIKROTIK-MIB", "mtxrWlRtabRxBytes"),
        ("MIKROTIK-MIB", "mtxrWlRtabTxPackets"),
        ("MIKROTIK-MIB", "mtxrWlRtabRxPackets"),
        ("MIKROTIK-MIB", "mtxrWlRtabTxRate"),
        ("MIKROTIK-MIB", "mtxrWlRtabRxRate"),
        ("MIKROTIK-MIB", "mtxrWlRtabEntryCount"),
        ("MIKROTIK-MIB", "mtxrWlRtabRouterOSVersion"),
        ("MIKROTIK-MIB", "mtxrWlRtabUptime"),
        ("MIKROTIK-MIB", "mtxrWlRtabSignalToNoise"),
        ("MIKROTIK-MIB", "mtxrWlRtabTxStrengthCh0"),
        ("MIKROTIK-MIB", "mtxrWlRtabRxStrengthCh0"),
        ("MIKROTIK-MIB", "mtxrWlRtabTxStrengthCh1"),
        ("MIKROTIK-MIB", "mtxrWlRtabRxStrengthCh1"),
        ("MIKROTIK-MIB", "mtxrWlRtabTxStrengthCh2"),
        ("MIKROTIK-MIB", "mtxrWlRtabRxStrengthCh2"),
        ("MIKROTIK-MIB", "mtxrWlRtabTxStrength"),
        ("MIKROTIK-MIB", "mtxrWlApTxRate"),
        ("MIKROTIK-MIB", "mtxrWlApRxRate"),
        ("MIKROTIK-MIB", "mtxrWlApSsid"),
        ("MIKROTIK-MIB", "mtxrWlApBssid"),
        ("MIKROTIK-MIB", "mtxrWlApClientCount"),
        ("MIKROTIK-MIB", "mtxrWlApBand"),
        ("MIKROTIK-MIB", "mtxrWlApFreq"),
        ("MIKROTIK-MIB", "mtxrWlApNoiseFloor"),
        ("MIKROTIK-MIB", "mtxrWlApOverallTxCCQ"),
        ("MIKROTIK-MIB", "mtxrWlApAuthClientCount"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabAddr"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabTxBytes"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabRxBytes"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabTxPackets"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabRxPackets"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabTxRate"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabRxRate"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabUptime"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabTxStrength"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabRxStrength"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabSsid"),
        ("MIKROTIK-MIB", "mtxrWlCMRtabEntryCount"))
)
if mibBuilder.loadTexts:
    mtxrWirelessGroup.setStatus("current")

mtxrQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 2)
)
mtxrQueueGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrQueueSimpleName"),
        ("MIKROTIK-MIB", "mtxrQueueSimpleSrcAddr"),
        ("MIKROTIK-MIB", "mtxrQueueSimpleSrcMask"),
        ("MIKROTIK-MIB", "mtxrQueueSimpleDstAddr"),
        ("MIKROTIK-MIB", "mtxrQueueSimpleDstMask"),
        ("MIKROTIK-MIB", "mtxrQueueSimpleIface"),
        ("MIKROTIK-MIB", "mtxrQueueSimpleBytesIn"),
        ("MIKROTIK-MIB", "mtxrQueueSimpleBytesOut"),
        ("MIKROTIK-MIB", "mtxrQueueSimplePacketsIn"),
        ("MIKROTIK-MIB", "mtxrQueueSimplePacketsOut"),
        ("MIKROTIK-MIB", "mtxrQueueTreeName"),
        ("MIKROTIK-MIB", "mtxrQueueSimplePCQQueuesIn"),
        ("MIKROTIK-MIB", "mtxrQueueSimplePCQQueuesOut"),
        ("MIKROTIK-MIB", "mtxrQueueSimpleDroppedIn"),
        ("MIKROTIK-MIB", "mtxrQueueSimpleDroppedOut"),
        ("MIKROTIK-MIB", "mtxrQueueTreeFlow"),
        ("MIKROTIK-MIB", "mtxrQueueTreeParentIndex"),
        ("MIKROTIK-MIB", "mtxrQueueTreeBytes"),
        ("MIKROTIK-MIB", "mtxrQueueTreePackets"),
        ("MIKROTIK-MIB", "mtxrQueueTreeHCBytes"),
        ("MIKROTIK-MIB", "mtxrQueueTreePCQQueues"),
        ("MIKROTIK-MIB", "mtxrQueueTreeDropped"))
)
if mibBuilder.loadTexts:
    mtxrQueueGroup.setStatus("current")

mtxrHealthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 3)
)
mtxrHealthGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrHlCoreVoltage"),
        ("MIKROTIK-MIB", "mtxrHlThreeDotThreeVoltage"),
        ("MIKROTIK-MIB", "mtxrHlFiveVoltage"),
        ("MIKROTIK-MIB", "mtxrHlTwelveVoltage"),
        ("MIKROTIK-MIB", "mtxrHlSensorTemperature"),
        ("MIKROTIK-MIB", "mtxrHlCpuTemperature"),
        ("MIKROTIK-MIB", "mtxrHlBoardTemperature"),
        ("MIKROTIK-MIB", "mtxrHlVoltage"),
        ("MIKROTIK-MIB", "mtxrHlActiveFan"),
        ("MIKROTIK-MIB", "mtxrHlTemperature"),
        ("MIKROTIK-MIB", "mtxrHlProcessorTemperature"),
        ("MIKROTIK-MIB", "mtxrHlCurrent"),
        ("MIKROTIK-MIB", "mtxrHlPower"),
        ("MIKROTIK-MIB", "mtxrHlProcessorFrequency"),
        ("MIKROTIK-MIB", "mtxrHlPowerSupplyState"),
        ("MIKROTIK-MIB", "mtxrHlBackupPowerSupplyState"),
        ("MIKROTIK-MIB", "mtxrHlFanSpeed1"),
        ("MIKROTIK-MIB", "mtxrHlFanSpeed2"))
)
if mibBuilder.loadTexts:
    mtxrHealthGroup.setStatus("current")

mtxrLincenseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 4)
)
mtxrLincenseGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrLicSoftwareId"),
        ("MIKROTIK-MIB", "mtxrLicUpgrUntil"),
        ("MIKROTIK-MIB", "mtxrLicLevel"),
        ("MIKROTIK-MIB", "mtxrLicVersion"),
        ("MIKROTIK-MIB", "mtxrLicUpgradableTo"))
)
if mibBuilder.loadTexts:
    mtxrLincenseGroup.setStatus("current")

mtxrHotspotActiveUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 5)
)
mtxrHotspotActiveUserGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrHotspotActiveUserServerID"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserName"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserDomain"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserIP"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserMAC"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserConnectTime"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserValidTillTime"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserIdleStartTime"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserIdleTimeout"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserPingTimeout"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserBytesIn"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserBytesOut"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserPacketsIn"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserPacketsOut"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserLimitBytesIn"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserLimitBytesOut"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserAdvertStatus"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserRadius"),
        ("MIKROTIK-MIB", "mtxrHotspotActiveUserBlockedByAdvert"))
)
if mibBuilder.loadTexts:
    mtxrHotspotActiveUserGroup.setStatus("current")

mtxrOpticalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 6)
)
mtxrOpticalGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrOpticalName"),
        ("MIKROTIK-MIB", "mtxrOpticalRxLoss"),
        ("MIKROTIK-MIB", "mtxrOpticalTxFault"),
        ("MIKROTIK-MIB", "mtxrOpticalWavelength"),
        ("MIKROTIK-MIB", "mtxrOpticalTemperature"),
        ("MIKROTIK-MIB", "mtxrOpticalSupplyVoltage"),
        ("MIKROTIK-MIB", "mtxrOpticalTxBiasCurrent"),
        ("MIKROTIK-MIB", "mtxrOpticalTxPower"),
        ("MIKROTIK-MIB", "mtxrOpticalRxPower"))
)
if mibBuilder.loadTexts:
    mtxrOpticalGroup.setStatus("current")

mtxrScriptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 8)
)
mtxrScriptGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrScriptName"),
        ("MIKROTIK-MIB", "mtxrScriptRunCmd"))
)
if mibBuilder.loadTexts:
    mtxrScriptGroup.setStatus("current")

mtxrNstremeDualGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 10)
)
mtxrNstremeDualGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrDnStatTxRate"),
        ("MIKROTIK-MIB", "mtxrDnStatRxRate"),
        ("MIKROTIK-MIB", "mtxrDnStatTxStrength"),
        ("MIKROTIK-MIB", "mtxrDnStatRxStrength"),
        ("MIKROTIK-MIB", "mtxrDnConnected"))
)
if mibBuilder.loadTexts:
    mtxrNstremeDualGroup.setStatus("current")

mtxrNeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 11)
)
mtxrNeighborGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrNeighborIpAddress"),
        ("MIKROTIK-MIB", "mtxrNeighborMacAddress"),
        ("MIKROTIK-MIB", "mtxrNeighborVersion"),
        ("MIKROTIK-MIB", "mtxrNeighborPlatform"),
        ("MIKROTIK-MIB", "mtxrNeighborIdentity"),
        ("MIKROTIK-MIB", "mtxrNeighborSoftwareID"),
        ("MIKROTIK-MIB", "mtxrNeighborInterfaceID"))
)
if mibBuilder.loadTexts:
    mtxrNeighborGroup.setStatus("current")

mtxrDHCPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 12)
)
mtxrDHCPGroup.setObjects(
    ("MIKROTIK-MIB", "mtxrDHCPLeaseCount")
)
if mibBuilder.loadTexts:
    mtxrDHCPGroup.setStatus("current")

mtxrSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 13)
)
mtxrSystemGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrSystemReboot"),
        ("MIKROTIK-MIB", "mtxrUSBPowerReset"),
        ("MIKROTIK-MIB", "mtxrSerialNumber"),
        ("MIKROTIK-MIB", "mtxrFirmwareVersion"),
        ("MIKROTIK-MIB", "mtxrNote"),
        ("MIKROTIK-MIB", "mtxrBuildTime"),
        ("MIKROTIK-MIB", "mtxrFirmwareUpgradeVersion"))
)
if mibBuilder.loadTexts:
    mtxrSystemGroup.setStatus("current")

mtxrGPSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 15)
)
mtxrGPSGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrDate"),
        ("MIKROTIK-MIB", "mtxrLongtitude"),
        ("MIKROTIK-MIB", "mtxrLatitude"),
        ("MIKROTIK-MIB", "mtxrAltitude"),
        ("MIKROTIK-MIB", "mtxrSpeed"),
        ("MIKROTIK-MIB", "mtxrSattelites"),
        ("MIKROTIK-MIB", "mtxrValid"))
)
if mibBuilder.loadTexts:
    mtxrGPSGroup.setStatus("current")

mtxrWirelessModemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 16)
)
mtxrWirelessModemGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrWirelessModemSignalStrength"),
        ("MIKROTIK-MIB", "mtxrWirelessModemSignalECIO"))
)
if mibBuilder.loadTexts:
    mtxrWirelessModemGroup.setStatus("current")

mtxrInterfaceStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 17)
)
mtxrInterfaceStatsGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrInterfaceStatsName"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsDriverRxBytes"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsDriverRxPackets"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsDriverTxBytes"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsDriverTxPackets"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxRx64"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxRx65To127"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxRx128To255"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxRx256To511"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxRx512To1023"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxRx1024To1518"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxRx1519ToMax"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxBytes"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxPackets"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxTooShort"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRx64"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRx65To127"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRx128To255"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRx256To511"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRx512To1023"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRx1024To1518"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRx1519ToMax"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxTooLong"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxBroadcast"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxPause"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxMulticast"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxFCSError"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxAlignError"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxFragment"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxOverflow"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxControl"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxUnknownOp"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxLengthError"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxCodeError"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxCarrierError"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxJabber"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsRxDrop"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxBytes"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxPackets"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxTooShort"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTx64"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTx65To127"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTx128To255"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTx256To511"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTx512To1023"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTx1024To1518"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTx1519ToMax"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxTooLong"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxBroadcast"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxPause"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxMulticast"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxUnderrun"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxCollision"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxExcessiveCollision"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxMultipleCollision"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxSingleCollision"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxExcessiveDeferred"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxDeferred"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxLateCollision"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxTotalCollision"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxPauseHonored"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxDrop"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxJabber"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxFCSError"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxControl"),
        ("MIKROTIK-MIB", "mtxrInterfaceStatsTxFragment"))
)
if mibBuilder.loadTexts:
    mtxrInterfaceStatsGroup.setStatus("current")

mtxrPOEGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 18)
)
mtxrPOEGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrPOEName"),
        ("MIKROTIK-MIB", "mtxrPOEStatus"),
        ("MIKROTIK-MIB", "mtxrPOEVoltage"),
        ("MIKROTIK-MIB", "mtxrPOECurrent"),
        ("MIKROTIK-MIB", "mtxrPOEPower"))
)
if mibBuilder.loadTexts:
    mtxrPOEGroup.setStatus("current")

mtxrLTEModemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 19)
)
mtxrLTEModemGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrLTEModemSignalRSSI"),
        ("MIKROTIK-MIB", "mtxrLTEModemSignalRSRQ"),
        ("MIKROTIK-MIB", "mtxrLTEModemSignalRSRP"),
        ("MIKROTIK-MIB", "mtxrLTEModemCellId"),
        ("MIKROTIK-MIB", "mtxrLTEModemAccessTechnology"),
        ("MIKROTIK-MIB", "mtxrLTEModemSignalSINR"))
)
if mibBuilder.loadTexts:
    mtxrLTEModemGroup.setStatus("current")

mtxrPartitionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 20)
)
mtxrPartitionGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrPartitionName"),
        ("MIKROTIK-MIB", "mtxrPartitionSize"),
        ("MIKROTIK-MIB", "mtxrPartitionVersion"),
        ("MIKROTIK-MIB", "mtxrPartitionActive"),
        ("MIKROTIK-MIB", "mtxrPartitionRunning"))
)
if mibBuilder.loadTexts:
    mtxrPartitionGroup.setStatus("current")

mtxrScriptRunGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 21)
)
mtxrScriptRunGroup.setObjects(
    ("MIKROTIK-MIB", "mtxrScriptRunOutput")
)
if mibBuilder.loadTexts:
    mtxrScriptRunGroup.setStatus("current")


# Notification objects

mtxrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 9, 0, 1)
)
if mibBuilder.loadTexts:
    mtxrTrap.setStatus(
        "current"
    )

mtxrTemperatureException = NotificationType(
    (1, 3, 6, 1, 4, 1, 14988, 1, 1, 9, 0, 2)
)
if mibBuilder.loadTexts:
    mtxrTemperatureException.setStatus(
        "current"
    )


# Notifications groups

mtxrTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 14988, 1, 2, 1, 14)
)
mtxrTrapGroup.setObjects(
      *(("MIKROTIK-MIB", "mtxrTrap"),
        ("MIKROTIK-MIB", "mtxrTemperatureException"))
)
if mibBuilder.loadTexts:
    mtxrTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIKROTIK-MIB",
    **{"ObjectIndex": ObjectIndex,
       "HexInt": HexInt,
       "Voltage": Voltage,
       "Temperature": Temperature,
       "Power": Power,
       "GDiv100": GDiv100,
       "GDiv1000": GDiv1000,
       "IDiv1000": IDiv1000,
       "BoolValue": BoolValue,
       "mikrotik": mikrotik,
       "mikrotikExperimentalModule": mikrotikExperimentalModule,
       "mtXRouterOs": mtXRouterOs,
       "mtxrWireless": mtxrWireless,
       "mtxrWlStatTable": mtxrWlStatTable,
       "mtxrWlStatEntry": mtxrWlStatEntry,
       "mtxrWlStatIndex": mtxrWlStatIndex,
       "mtxrWlStatTxRate": mtxrWlStatTxRate,
       "mtxrWlStatRxRate": mtxrWlStatRxRate,
       "mtxrWlStatStrength": mtxrWlStatStrength,
       "mtxrWlStatSsid": mtxrWlStatSsid,
       "mtxrWlStatBssid": mtxrWlStatBssid,
       "mtxrWlStatFreq": mtxrWlStatFreq,
       "mtxrWlStatBand": mtxrWlStatBand,
       "mtxrWlRtabTable": mtxrWlRtabTable,
       "mtxrWlRtabEntry": mtxrWlRtabEntry,
       "mtxrWlRtabAddr": mtxrWlRtabAddr,
       "mtxrWlRtabIface": mtxrWlRtabIface,
       "mtxrWlRtabStrength": mtxrWlRtabStrength,
       "mtxrWlRtabTxBytes": mtxrWlRtabTxBytes,
       "mtxrWlRtabRxBytes": mtxrWlRtabRxBytes,
       "mtxrWlRtabTxPackets": mtxrWlRtabTxPackets,
       "mtxrWlRtabRxPackets": mtxrWlRtabRxPackets,
       "mtxrWlRtabTxRate": mtxrWlRtabTxRate,
       "mtxrWlRtabRxRate": mtxrWlRtabRxRate,
       "mtxrWlRtabRouterOSVersion": mtxrWlRtabRouterOSVersion,
       "mtxrWlRtabUptime": mtxrWlRtabUptime,
       "mtxrWlRtabSignalToNoise": mtxrWlRtabSignalToNoise,
       "mtxrWlRtabTxStrengthCh0": mtxrWlRtabTxStrengthCh0,
       "mtxrWlRtabRxStrengthCh0": mtxrWlRtabRxStrengthCh0,
       "mtxrWlRtabTxStrengthCh1": mtxrWlRtabTxStrengthCh1,
       "mtxrWlRtabRxStrengthCh1": mtxrWlRtabRxStrengthCh1,
       "mtxrWlRtabTxStrengthCh2": mtxrWlRtabTxStrengthCh2,
       "mtxrWlRtabRxStrengthCh2": mtxrWlRtabRxStrengthCh2,
       "mtxrWlRtabTxStrength": mtxrWlRtabTxStrength,
       "mtxrWlApTable": mtxrWlApTable,
       "mtxrWlApEntry": mtxrWlApEntry,
       "mtxrWlApIndex": mtxrWlApIndex,
       "mtxrWlApTxRate": mtxrWlApTxRate,
       "mtxrWlApRxRate": mtxrWlApRxRate,
       "mtxrWlApSsid": mtxrWlApSsid,
       "mtxrWlApBssid": mtxrWlApBssid,
       "mtxrWlApClientCount": mtxrWlApClientCount,
       "mtxrWlApFreq": mtxrWlApFreq,
       "mtxrWlApBand": mtxrWlApBand,
       "mtxrWlApNoiseFloor": mtxrWlApNoiseFloor,
       "mtxrWlApOverallTxCCQ": mtxrWlApOverallTxCCQ,
       "mtxrWlApAuthClientCount": mtxrWlApAuthClientCount,
       "mtxrWlRtabEntryCount": mtxrWlRtabEntryCount,
       "mtxrWlCMRtabTable": mtxrWlCMRtabTable,
       "mtxrWlCMRtabEntry": mtxrWlCMRtabEntry,
       "mtxrWlCMRtabAddr": mtxrWlCMRtabAddr,
       "mtxrWlCMRtabIface": mtxrWlCMRtabIface,
       "mtxrWlCMRtabUptime": mtxrWlCMRtabUptime,
       "mtxrWlCMRtabTxBytes": mtxrWlCMRtabTxBytes,
       "mtxrWlCMRtabRxBytes": mtxrWlCMRtabRxBytes,
       "mtxrWlCMRtabTxPackets": mtxrWlCMRtabTxPackets,
       "mtxrWlCMRtabRxPackets": mtxrWlCMRtabRxPackets,
       "mtxrWlCMRtabTxRate": mtxrWlCMRtabTxRate,
       "mtxrWlCMRtabRxRate": mtxrWlCMRtabRxRate,
       "mtxrWlCMRtabTxStrength": mtxrWlCMRtabTxStrength,
       "mtxrWlCMRtabRxStrength": mtxrWlCMRtabRxStrength,
       "mtxrWlCMRtabSsid": mtxrWlCMRtabSsid,
       "mtxrWlCMRtabEntryCount": mtxrWlCMRtabEntryCount,
       "mtxrQueues": mtxrQueues,
       "mtxrQueueSimpleTable": mtxrQueueSimpleTable,
       "mtxrQueueSimpleEntry": mtxrQueueSimpleEntry,
       "mtxrQueueSimpleIndex": mtxrQueueSimpleIndex,
       "mtxrQueueSimpleName": mtxrQueueSimpleName,
       "mtxrQueueSimpleSrcAddr": mtxrQueueSimpleSrcAddr,
       "mtxrQueueSimpleSrcMask": mtxrQueueSimpleSrcMask,
       "mtxrQueueSimpleDstAddr": mtxrQueueSimpleDstAddr,
       "mtxrQueueSimpleDstMask": mtxrQueueSimpleDstMask,
       "mtxrQueueSimpleIface": mtxrQueueSimpleIface,
       "mtxrQueueSimpleBytesIn": mtxrQueueSimpleBytesIn,
       "mtxrQueueSimpleBytesOut": mtxrQueueSimpleBytesOut,
       "mtxrQueueSimplePacketsIn": mtxrQueueSimplePacketsIn,
       "mtxrQueueSimplePacketsOut": mtxrQueueSimplePacketsOut,
       "mtxrQueueSimplePCQQueuesIn": mtxrQueueSimplePCQQueuesIn,
       "mtxrQueueSimplePCQQueuesOut": mtxrQueueSimplePCQQueuesOut,
       "mtxrQueueSimpleDroppedIn": mtxrQueueSimpleDroppedIn,
       "mtxrQueueSimpleDroppedOut": mtxrQueueSimpleDroppedOut,
       "mtxrQueueTreeTable": mtxrQueueTreeTable,
       "mtxrQueueTreeEntry": mtxrQueueTreeEntry,
       "mtxrQueueTreeIndex": mtxrQueueTreeIndex,
       "mtxrQueueTreeName": mtxrQueueTreeName,
       "mtxrQueueTreeFlow": mtxrQueueTreeFlow,
       "mtxrQueueTreeParentIndex": mtxrQueueTreeParentIndex,
       "mtxrQueueTreeBytes": mtxrQueueTreeBytes,
       "mtxrQueueTreePackets": mtxrQueueTreePackets,
       "mtxrQueueTreeHCBytes": mtxrQueueTreeHCBytes,
       "mtxrQueueTreePCQQueues": mtxrQueueTreePCQQueues,
       "mtxrQueueTreeDropped": mtxrQueueTreeDropped,
       "mtxrHealth": mtxrHealth,
       "mtxrHlCoreVoltage": mtxrHlCoreVoltage,
       "mtxrHlThreeDotThreeVoltage": mtxrHlThreeDotThreeVoltage,
       "mtxrHlFiveVoltage": mtxrHlFiveVoltage,
       "mtxrHlTwelveVoltage": mtxrHlTwelveVoltage,
       "mtxrHlSensorTemperature": mtxrHlSensorTemperature,
       "mtxrHlCpuTemperature": mtxrHlCpuTemperature,
       "mtxrHlBoardTemperature": mtxrHlBoardTemperature,
       "mtxrHlVoltage": mtxrHlVoltage,
       "mtxrHlActiveFan": mtxrHlActiveFan,
       "mtxrHlTemperature": mtxrHlTemperature,
       "mtxrHlProcessorTemperature": mtxrHlProcessorTemperature,
       "mtxrHlPower": mtxrHlPower,
       "mtxrHlCurrent": mtxrHlCurrent,
       "mtxrHlProcessorFrequency": mtxrHlProcessorFrequency,
       "mtxrHlPowerSupplyState": mtxrHlPowerSupplyState,
       "mtxrHlBackupPowerSupplyState": mtxrHlBackupPowerSupplyState,
       "mtxrHlFanSpeed1": mtxrHlFanSpeed1,
       "mtxrHlFanSpeed2": mtxrHlFanSpeed2,
       "mtxrLicense": mtxrLicense,
       "mtxrLicSoftwareId": mtxrLicSoftwareId,
       "mtxrLicUpgrUntil": mtxrLicUpgrUntil,
       "mtxrLicLevel": mtxrLicLevel,
       "mtxrLicVersion": mtxrLicVersion,
       "mtxrLicUpgradableTo": mtxrLicUpgradableTo,
       "mtxrHotspot": mtxrHotspot,
       "mtxrHotspotActiveUsersTable": mtxrHotspotActiveUsersTable,
       "mtxrHotspotActiveUsersTableEntry": mtxrHotspotActiveUsersTableEntry,
       "mtxrHotspotActiveUserIndex": mtxrHotspotActiveUserIndex,
       "mtxrHotspotActiveUserServerID": mtxrHotspotActiveUserServerID,
       "mtxrHotspotActiveUserName": mtxrHotspotActiveUserName,
       "mtxrHotspotActiveUserDomain": mtxrHotspotActiveUserDomain,
       "mtxrHotspotActiveUserIP": mtxrHotspotActiveUserIP,
       "mtxrHotspotActiveUserMAC": mtxrHotspotActiveUserMAC,
       "mtxrHotspotActiveUserConnectTime": mtxrHotspotActiveUserConnectTime,
       "mtxrHotspotActiveUserValidTillTime": mtxrHotspotActiveUserValidTillTime,
       "mtxrHotspotActiveUserIdleStartTime": mtxrHotspotActiveUserIdleStartTime,
       "mtxrHotspotActiveUserIdleTimeout": mtxrHotspotActiveUserIdleTimeout,
       "mtxrHotspotActiveUserPingTimeout": mtxrHotspotActiveUserPingTimeout,
       "mtxrHotspotActiveUserBytesIn": mtxrHotspotActiveUserBytesIn,
       "mtxrHotspotActiveUserBytesOut": mtxrHotspotActiveUserBytesOut,
       "mtxrHotspotActiveUserPacketsIn": mtxrHotspotActiveUserPacketsIn,
       "mtxrHotspotActiveUserPacketsOut": mtxrHotspotActiveUserPacketsOut,
       "mtxrHotspotActiveUserLimitBytesIn": mtxrHotspotActiveUserLimitBytesIn,
       "mtxrHotspotActiveUserLimitBytesOut": mtxrHotspotActiveUserLimitBytesOut,
       "mtxrHotspotActiveUserAdvertStatus": mtxrHotspotActiveUserAdvertStatus,
       "mtxrHotspotActiveUserRadius": mtxrHotspotActiveUserRadius,
       "mtxrHotspotActiveUserBlockedByAdvert": mtxrHotspotActiveUserBlockedByAdvert,
       "mtxrDHCP": mtxrDHCP,
       "mtxrDHCPLeaseCount": mtxrDHCPLeaseCount,
       "mtxrSystem": mtxrSystem,
       "mtxrSystemReboot": mtxrSystemReboot,
       "mtxrUSBPowerReset": mtxrUSBPowerReset,
       "mtxrSerialNumber": mtxrSerialNumber,
       "mtxrFirmwareVersion": mtxrFirmwareVersion,
       "mtxrNote": mtxrNote,
       "mtxrBuildTime": mtxrBuildTime,
       "mtxrFirmwareUpgradeVersion": mtxrFirmwareUpgradeVersion,
       "mtxrScripts": mtxrScripts,
       "mtxrScriptTable": mtxrScriptTable,
       "mtxrScriptTableEntry": mtxrScriptTableEntry,
       "mtxrScriptIndex": mtxrScriptIndex,
       "mtxrScriptName": mtxrScriptName,
       "mtxrScriptRunCmd": mtxrScriptRunCmd,
       "mtxrTraps": mtxrTraps,
       "mtxrNotifications": mtxrNotifications,
       "mtxrTrap": mtxrTrap,
       "mtxrTemperatureException": mtxrTemperatureException,
       "mtxrNstremeDual": mtxrNstremeDual,
       "mtxrDnStatTable": mtxrDnStatTable,
       "mtxrDnStatEntry": mtxrDnStatEntry,
       "mtxrDnStatIndex": mtxrDnStatIndex,
       "mtxrDnStatTxRate": mtxrDnStatTxRate,
       "mtxrDnStatRxRate": mtxrDnStatRxRate,
       "mtxrDnStatTxStrength": mtxrDnStatTxStrength,
       "mtxrDnStatRxStrength": mtxrDnStatRxStrength,
       "mtxrDnConnected": mtxrDnConnected,
       "mtxrNeighbor": mtxrNeighbor,
       "mtxrNeighborTable": mtxrNeighborTable,
       "mtxrNeighborTableEntry": mtxrNeighborTableEntry,
       "mtxrNeighborIndex": mtxrNeighborIndex,
       "mtxrNeighborIpAddress": mtxrNeighborIpAddress,
       "mtxrNeighborMacAddress": mtxrNeighborMacAddress,
       "mtxrNeighborVersion": mtxrNeighborVersion,
       "mtxrNeighborPlatform": mtxrNeighborPlatform,
       "mtxrNeighborIdentity": mtxrNeighborIdentity,
       "mtxrNeighborSoftwareID": mtxrNeighborSoftwareID,
       "mtxrNeighborInterfaceID": mtxrNeighborInterfaceID,
       "mtxrGps": mtxrGps,
       "mtxrDate": mtxrDate,
       "mtxrLongtitude": mtxrLongtitude,
       "mtxrLatitude": mtxrLatitude,
       "mtxrAltitude": mtxrAltitude,
       "mtxrSpeed": mtxrSpeed,
       "mtxrSattelites": mtxrSattelites,
       "mtxrValid": mtxrValid,
       "mtxrWirelessModem": mtxrWirelessModem,
       "mtxrWirelessModemSignalStrength": mtxrWirelessModemSignalStrength,
       "mtxrWirelessModemSignalECIO": mtxrWirelessModemSignalECIO,
       "mtxrInterfaceStats": mtxrInterfaceStats,
       "mtxrInterfaceStatsTable": mtxrInterfaceStatsTable,
       "mtxrInterfaceStatsEntry": mtxrInterfaceStatsEntry,
       "mtxrInterfaceStatsIndex": mtxrInterfaceStatsIndex,
       "mtxrInterfaceStatsName": mtxrInterfaceStatsName,
       "mtxrInterfaceStatsDriverRxBytes": mtxrInterfaceStatsDriverRxBytes,
       "mtxrInterfaceStatsDriverRxPackets": mtxrInterfaceStatsDriverRxPackets,
       "mtxrInterfaceStatsDriverTxBytes": mtxrInterfaceStatsDriverTxBytes,
       "mtxrInterfaceStatsDriverTxPackets": mtxrInterfaceStatsDriverTxPackets,
       "mtxrInterfaceStatsTxRx64": mtxrInterfaceStatsTxRx64,
       "mtxrInterfaceStatsTxRx65To127": mtxrInterfaceStatsTxRx65To127,
       "mtxrInterfaceStatsTxRx128To255": mtxrInterfaceStatsTxRx128To255,
       "mtxrInterfaceStatsTxRx256To511": mtxrInterfaceStatsTxRx256To511,
       "mtxrInterfaceStatsTxRx512To1023": mtxrInterfaceStatsTxRx512To1023,
       "mtxrInterfaceStatsTxRx1024To1518": mtxrInterfaceStatsTxRx1024To1518,
       "mtxrInterfaceStatsTxRx1519ToMax": mtxrInterfaceStatsTxRx1519ToMax,
       "mtxrInterfaceStatsRxBytes": mtxrInterfaceStatsRxBytes,
       "mtxrInterfaceStatsRxPackets": mtxrInterfaceStatsRxPackets,
       "mtxrInterfaceStatsRxTooShort": mtxrInterfaceStatsRxTooShort,
       "mtxrInterfaceStatsRx64": mtxrInterfaceStatsRx64,
       "mtxrInterfaceStatsRx65To127": mtxrInterfaceStatsRx65To127,
       "mtxrInterfaceStatsRx128To255": mtxrInterfaceStatsRx128To255,
       "mtxrInterfaceStatsRx256To511": mtxrInterfaceStatsRx256To511,
       "mtxrInterfaceStatsRx512To1023": mtxrInterfaceStatsRx512To1023,
       "mtxrInterfaceStatsRx1024To1518": mtxrInterfaceStatsRx1024To1518,
       "mtxrInterfaceStatsRx1519ToMax": mtxrInterfaceStatsRx1519ToMax,
       "mtxrInterfaceStatsRxTooLong": mtxrInterfaceStatsRxTooLong,
       "mtxrInterfaceStatsRxBroadcast": mtxrInterfaceStatsRxBroadcast,
       "mtxrInterfaceStatsRxPause": mtxrInterfaceStatsRxPause,
       "mtxrInterfaceStatsRxMulticast": mtxrInterfaceStatsRxMulticast,
       "mtxrInterfaceStatsRxFCSError": mtxrInterfaceStatsRxFCSError,
       "mtxrInterfaceStatsRxAlignError": mtxrInterfaceStatsRxAlignError,
       "mtxrInterfaceStatsRxFragment": mtxrInterfaceStatsRxFragment,
       "mtxrInterfaceStatsRxOverflow": mtxrInterfaceStatsRxOverflow,
       "mtxrInterfaceStatsRxControl": mtxrInterfaceStatsRxControl,
       "mtxrInterfaceStatsRxUnknownOp": mtxrInterfaceStatsRxUnknownOp,
       "mtxrInterfaceStatsRxLengthError": mtxrInterfaceStatsRxLengthError,
       "mtxrInterfaceStatsRxCodeError": mtxrInterfaceStatsRxCodeError,
       "mtxrInterfaceStatsRxCarrierError": mtxrInterfaceStatsRxCarrierError,
       "mtxrInterfaceStatsRxJabber": mtxrInterfaceStatsRxJabber,
       "mtxrInterfaceStatsRxDrop": mtxrInterfaceStatsRxDrop,
       "mtxrInterfaceStatsTxBytes": mtxrInterfaceStatsTxBytes,
       "mtxrInterfaceStatsTxPackets": mtxrInterfaceStatsTxPackets,
       "mtxrInterfaceStatsTxTooShort": mtxrInterfaceStatsTxTooShort,
       "mtxrInterfaceStatsTx64": mtxrInterfaceStatsTx64,
       "mtxrInterfaceStatsTx65To127": mtxrInterfaceStatsTx65To127,
       "mtxrInterfaceStatsTx128To255": mtxrInterfaceStatsTx128To255,
       "mtxrInterfaceStatsTx256To511": mtxrInterfaceStatsTx256To511,
       "mtxrInterfaceStatsTx512To1023": mtxrInterfaceStatsTx512To1023,
       "mtxrInterfaceStatsTx1024To1518": mtxrInterfaceStatsTx1024To1518,
       "mtxrInterfaceStatsTx1519ToMax": mtxrInterfaceStatsTx1519ToMax,
       "mtxrInterfaceStatsTxTooLong": mtxrInterfaceStatsTxTooLong,
       "mtxrInterfaceStatsTxBroadcast": mtxrInterfaceStatsTxBroadcast,
       "mtxrInterfaceStatsTxPause": mtxrInterfaceStatsTxPause,
       "mtxrInterfaceStatsTxMulticast": mtxrInterfaceStatsTxMulticast,
       "mtxrInterfaceStatsTxUnderrun": mtxrInterfaceStatsTxUnderrun,
       "mtxrInterfaceStatsTxCollision": mtxrInterfaceStatsTxCollision,
       "mtxrInterfaceStatsTxExcessiveCollision": mtxrInterfaceStatsTxExcessiveCollision,
       "mtxrInterfaceStatsTxMultipleCollision": mtxrInterfaceStatsTxMultipleCollision,
       "mtxrInterfaceStatsTxSingleCollision": mtxrInterfaceStatsTxSingleCollision,
       "mtxrInterfaceStatsTxExcessiveDeferred": mtxrInterfaceStatsTxExcessiveDeferred,
       "mtxrInterfaceStatsTxDeferred": mtxrInterfaceStatsTxDeferred,
       "mtxrInterfaceStatsTxLateCollision": mtxrInterfaceStatsTxLateCollision,
       "mtxrInterfaceStatsTxTotalCollision": mtxrInterfaceStatsTxTotalCollision,
       "mtxrInterfaceStatsTxPauseHonored": mtxrInterfaceStatsTxPauseHonored,
       "mtxrInterfaceStatsTxDrop": mtxrInterfaceStatsTxDrop,
       "mtxrInterfaceStatsTxJabber": mtxrInterfaceStatsTxJabber,
       "mtxrInterfaceStatsTxFCSError": mtxrInterfaceStatsTxFCSError,
       "mtxrInterfaceStatsTxControl": mtxrInterfaceStatsTxControl,
       "mtxrInterfaceStatsTxFragment": mtxrInterfaceStatsTxFragment,
       "mtxrPOE": mtxrPOE,
       "mtxrPOETable": mtxrPOETable,
       "mtxrPOEEntry": mtxrPOEEntry,
       "mtxrPOEInterfaceIndex": mtxrPOEInterfaceIndex,
       "mtxrPOEName": mtxrPOEName,
       "mtxrPOEStatus": mtxrPOEStatus,
       "mtxrPOEVoltage": mtxrPOEVoltage,
       "mtxrPOECurrent": mtxrPOECurrent,
       "mtxrPOEPower": mtxrPOEPower,
       "mtxrLTEModem": mtxrLTEModem,
       "mtxrLTEModemTable": mtxrLTEModemTable,
       "mtxrLTEModemEntry": mtxrLTEModemEntry,
       "mtxrLTEModemInterfaceIndex": mtxrLTEModemInterfaceIndex,
       "mtxrLTEModemSignalRSSI": mtxrLTEModemSignalRSSI,
       "mtxrLTEModemSignalRSRQ": mtxrLTEModemSignalRSRQ,
       "mtxrLTEModemSignalRSRP": mtxrLTEModemSignalRSRP,
       "mtxrLTEModemCellId": mtxrLTEModemCellId,
       "mtxrLTEModemAccessTechnology": mtxrLTEModemAccessTechnology,
       "mtxrLTEModemSignalSINR": mtxrLTEModemSignalSINR,
       "mtxrPartition": mtxrPartition,
       "mtxrPartitionTable": mtxrPartitionTable,
       "mtxrPartitionEntry": mtxrPartitionEntry,
       "mtxrPartitionIndex": mtxrPartitionIndex,
       "mtxrPartitionName": mtxrPartitionName,
       "mtxrPartitionSize": mtxrPartitionSize,
       "mtxrPartitionVersion": mtxrPartitionVersion,
       "mtxrPartitionActive": mtxrPartitionActive,
       "mtxrPartitionRunning": mtxrPartitionRunning,
       "mtxrScriptRun": mtxrScriptRun,
       "mtxrScriptRunTable": mtxrScriptRunTable,
       "mtxrScriptRunTableEntry": mtxrScriptRunTableEntry,
       "mtxrScriptRunIndex": mtxrScriptRunIndex,
       "mtxrScriptRunOutput": mtxrScriptRunOutput,
       "mtxrOptical": mtxrOptical,
       "mtxrOpticalTable": mtxrOpticalTable,
       "mtxrOpticalTableEntry": mtxrOpticalTableEntry,
       "mtxrOpticalIndex": mtxrOpticalIndex,
       "mtxrOpticalName": mtxrOpticalName,
       "mtxrOpticalRxLoss": mtxrOpticalRxLoss,
       "mtxrOpticalTxFault": mtxrOpticalTxFault,
       "mtxrOpticalWavelength": mtxrOpticalWavelength,
       "mtxrOpticalTemperature": mtxrOpticalTemperature,
       "mtxrOpticalSupplyVoltage": mtxrOpticalSupplyVoltage,
       "mtxrOpticalTxBiasCurrent": mtxrOpticalTxBiasCurrent,
       "mtxrOpticalTxPower": mtxrOpticalTxPower,
       "mtxrOpticalRxPower": mtxrOpticalRxPower,
       "mtXMetaInfo": mtXMetaInfo,
       "mtXRouterOsGroups": mtXRouterOsGroups,
       "mtxrWirelessGroup": mtxrWirelessGroup,
       "mtxrQueueGroup": mtxrQueueGroup,
       "mtxrHealthGroup": mtxrHealthGroup,
       "mtxrLincenseGroup": mtxrLincenseGroup,
       "mtxrHotspotActiveUserGroup": mtxrHotspotActiveUserGroup,
       "mtxrOpticalGroup": mtxrOpticalGroup,
       "mtxrScriptGroup": mtxrScriptGroup,
       "mtxrNstremeDualGroup": mtxrNstremeDualGroup,
       "mtxrNeighborGroup": mtxrNeighborGroup,
       "mtxrDHCPGroup": mtxrDHCPGroup,
       "mtxrSystemGroup": mtxrSystemGroup,
       "mtxrTrapGroup": mtxrTrapGroup,
       "mtxrGPSGroup": mtxrGPSGroup,
       "mtxrWirelessModemGroup": mtxrWirelessModemGroup,
       "mtxrInterfaceStatsGroup": mtxrInterfaceStatsGroup,
       "mtxrPOEGroup": mtxrPOEGroup,
       "mtxrLTEModemGroup": mtxrLTEModemGroup,
       "mtxrPartitionGroup": mtxrPartitionGroup,
       "mtxrScriptRunGroup": mtxrScriptRunGroup}
)
