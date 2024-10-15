# SNMP MIB module (AISYSCFGTEMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AISYSCFGTEMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:25 2024
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

aiSysCfgTemp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32, 5)
)
aiSysCfgTemp.setRevisions(
        ("2001-04-30 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiSysCfg_ObjectIdentity = ObjectIdentity
aiSysCfg = _AiSysCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32)
)
_AiSCTempTrapInfo_ObjectIdentity = ObjectIdentity
aiSCTempTrapInfo = _AiSCTempTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32, 5, 0)
)


class _AiSCTempAgregateStatus_Type(Integer32):
    """Custom type aiSCTempAgregateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("okay", 1),
          ("trouble", 2))
    )


_AiSCTempAgregateStatus_Type.__name__ = "Integer32"
_AiSCTempAgregateStatus_Object = MibScalar
aiSCTempAgregateStatus = _AiSCTempAgregateStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 5, 1),
    _AiSCTempAgregateStatus_Type()
)
aiSCTempAgregateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCTempAgregateStatus.setStatus("current")
_AiSCTempProbeTable_Object = MibTable
aiSCTempProbeTable = _AiSCTempProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 5, 2)
)
if mibBuilder.loadTexts:
    aiSCTempProbeTable.setStatus("current")
_AiSCTempProbeEntry_Object = MibTableRow
aiSCTempProbeEntry = _AiSCTempProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 5, 2, 1)
)
aiSCTempProbeEntry.setIndexNames(
    (0, "AISYSCFGTEMP-MIB", "aiSCTempProbeIndex"),
)
if mibBuilder.loadTexts:
    aiSCTempProbeEntry.setStatus("current")


class _AiSCTempProbeIndex_Type(Integer32):
    """Custom type aiSCTempProbeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AiSCTempProbeIndex_Type.__name__ = "Integer32"
_AiSCTempProbeIndex_Object = MibTableColumn
aiSCTempProbeIndex = _AiSCTempProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 5, 2, 1, 1),
    _AiSCTempProbeIndex_Type()
)
aiSCTempProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCTempProbeIndex.setStatus("current")


class _AiSCTempProbeDescription_Type(DisplayString):
    """Custom type aiSCTempProbeDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AiSCTempProbeDescription_Type.__name__ = "DisplayString"
_AiSCTempProbeDescription_Object = MibTableColumn
aiSCTempProbeDescription = _AiSCTempProbeDescription_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 5, 2, 1, 2),
    _AiSCTempProbeDescription_Type()
)
aiSCTempProbeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCTempProbeDescription.setStatus("current")


class _AiSCTempProbeStatus_Type(Integer32):
    """Custom type aiSCTempProbeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2))
    )


_AiSCTempProbeStatus_Type.__name__ = "Integer32"
_AiSCTempProbeStatus_Object = MibTableColumn
aiSCTempProbeStatus = _AiSCTempProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 5, 2, 1, 3),
    _AiSCTempProbeStatus_Type()
)
aiSCTempProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCTempProbeStatus.setStatus("current")


class _AiSCTempProbeLocation_Type(Integer32):
    """Custom type aiSCTempProbeLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_AiSCTempProbeLocation_Type.__name__ = "Integer32"
_AiSCTempProbeLocation_Object = MibTableColumn
aiSCTempProbeLocation = _AiSCTempProbeLocation_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 5, 2, 1, 4),
    _AiSCTempProbeLocation_Type()
)
aiSCTempProbeLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCTempProbeLocation.setStatus("current")
_AiSCTempProbeLowThreshCelsius_Type = Integer32
_AiSCTempProbeLowThreshCelsius_Object = MibTableColumn
aiSCTempProbeLowThreshCelsius = _AiSCTempProbeLowThreshCelsius_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 5, 2, 1, 5),
    _AiSCTempProbeLowThreshCelsius_Type()
)
aiSCTempProbeLowThreshCelsius.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSCTempProbeLowThreshCelsius.setStatus("current")
if mibBuilder.loadTexts:
    aiSCTempProbeLowThreshCelsius.setUnits("degrees Celsius")
_AiSCTempProbeHighThreshCelsius_Type = Integer32
_AiSCTempProbeHighThreshCelsius_Object = MibTableColumn
aiSCTempProbeHighThreshCelsius = _AiSCTempProbeHighThreshCelsius_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 5, 2, 1, 6),
    _AiSCTempProbeHighThreshCelsius_Type()
)
aiSCTempProbeHighThreshCelsius.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiSCTempProbeHighThreshCelsius.setStatus("current")
if mibBuilder.loadTexts:
    aiSCTempProbeHighThreshCelsius.setUnits("degrees Celsius")
_AiSCTempProbeTempCelsius_Type = Integer32
_AiSCTempProbeTempCelsius_Object = MibTableColumn
aiSCTempProbeTempCelsius = _AiSCTempProbeTempCelsius_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 5, 2, 1, 7),
    _AiSCTempProbeTempCelsius_Type()
)
aiSCTempProbeTempCelsius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCTempProbeTempCelsius.setStatus("current")
if mibBuilder.loadTexts:
    aiSCTempProbeTempCelsius.setUnits("degrees Celsius")

# Managed Objects groups


# Notification objects

aiSCTempTrapFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 539, 32, 5, 0, 1)
)
aiSCTempTrapFail.setObjects(
      *(("AISYSCFGTEMP-MIB", "aiSCTempProbeIndex"),
        ("AISYSCFGTEMP-MIB", "aiSCTempProbeTempCelsius"))
)
if mibBuilder.loadTexts:
    aiSCTempTrapFail.setStatus(
        "current"
    )

aiSCTempTrapOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 539, 32, 5, 0, 2)
)
aiSCTempTrapOk.setObjects(
      *(("AISYSCFGTEMP-MIB", "aiSCTempProbeIndex"),
        ("AISYSCFGTEMP-MIB", "aiSCTempProbeTempCelsius"))
)
if mibBuilder.loadTexts:
    aiSCTempTrapOk.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AISYSCFGTEMP-MIB",
    **{"aii": aii,
       "aiSysCfg": aiSysCfg,
       "aiSysCfgTemp": aiSysCfgTemp,
       "aiSCTempTrapInfo": aiSCTempTrapInfo,
       "aiSCTempTrapFail": aiSCTempTrapFail,
       "aiSCTempTrapOk": aiSCTempTrapOk,
       "aiSCTempAgregateStatus": aiSCTempAgregateStatus,
       "aiSCTempProbeTable": aiSCTempProbeTable,
       "aiSCTempProbeEntry": aiSCTempProbeEntry,
       "aiSCTempProbeIndex": aiSCTempProbeIndex,
       "aiSCTempProbeDescription": aiSCTempProbeDescription,
       "aiSCTempProbeStatus": aiSCTempProbeStatus,
       "aiSCTempProbeLocation": aiSCTempProbeLocation,
       "aiSCTempProbeLowThreshCelsius": aiSCTempProbeLowThreshCelsius,
       "aiSCTempProbeHighThreshCelsius": aiSCTempProbeHighThreshCelsius,
       "aiSCTempProbeTempCelsius": aiSCTempProbeTempCelsius}
)
