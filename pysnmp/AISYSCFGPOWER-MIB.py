# SNMP MIB module (AISYSCFGPOWER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AISYSCFGPOWER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:24 2024
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

aiSysCfgPower = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32, 3)
)
aiSysCfgPower.setRevisions(
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
_AiSCPowerTrapInfo_ObjectIdentity = ObjectIdentity
aiSCPowerTrapInfo = _AiSCPowerTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32, 3, 0)
)


class _AiSCPowerAgregateStatus_Type(Integer32):
    """Custom type aiSCPowerAgregateStatus based on Integer32"""
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


_AiSCPowerAgregateStatus_Type.__name__ = "Integer32"
_AiSCPowerAgregateStatus_Object = MibScalar
aiSCPowerAgregateStatus = _AiSCPowerAgregateStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 3, 1),
    _AiSCPowerAgregateStatus_Type()
)
aiSCPowerAgregateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCPowerAgregateStatus.setStatus("current")
_AiSCPowerFeedTable_Object = MibTable
aiSCPowerFeedTable = _AiSCPowerFeedTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 3, 2)
)
if mibBuilder.loadTexts:
    aiSCPowerFeedTable.setStatus("current")
_AiSCPowerFeedEntry_Object = MibTableRow
aiSCPowerFeedEntry = _AiSCPowerFeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 3, 2, 1)
)
aiSCPowerFeedEntry.setIndexNames(
    (0, "AISYSCFGPOWER-MIB", "aiSCPowerFeedIndex"),
)
if mibBuilder.loadTexts:
    aiSCPowerFeedEntry.setStatus("current")


class _AiSCPowerFeedIndex_Type(Integer32):
    """Custom type aiSCPowerFeedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AiSCPowerFeedIndex_Type.__name__ = "Integer32"
_AiSCPowerFeedIndex_Object = MibTableColumn
aiSCPowerFeedIndex = _AiSCPowerFeedIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 3, 2, 1, 1),
    _AiSCPowerFeedIndex_Type()
)
aiSCPowerFeedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCPowerFeedIndex.setStatus("current")


class _AiSCPowerFeedDescription_Type(DisplayString):
    """Custom type aiSCPowerFeedDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AiSCPowerFeedDescription_Type.__name__ = "DisplayString"
_AiSCPowerFeedDescription_Object = MibTableColumn
aiSCPowerFeedDescription = _AiSCPowerFeedDescription_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 3, 2, 1, 2),
    _AiSCPowerFeedDescription_Type()
)
aiSCPowerFeedDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCPowerFeedDescription.setStatus("current")


class _AiSCPowerFeedStatus_Type(Integer32):
    """Custom type aiSCPowerFeedStatus based on Integer32"""
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
        *(("fail", 2),
          ("okay", 1),
          ("overVoltage", 4),
          ("underVoltage", 3))
    )


_AiSCPowerFeedStatus_Type.__name__ = "Integer32"
_AiSCPowerFeedStatus_Object = MibTableColumn
aiSCPowerFeedStatus = _AiSCPowerFeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 3, 2, 1, 3),
    _AiSCPowerFeedStatus_Type()
)
aiSCPowerFeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCPowerFeedStatus.setStatus("current")
_AiSCPowerConverterTable_Object = MibTable
aiSCPowerConverterTable = _AiSCPowerConverterTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 3, 3)
)
if mibBuilder.loadTexts:
    aiSCPowerConverterTable.setStatus("current")
_AiSCPowerConverterEntry_Object = MibTableRow
aiSCPowerConverterEntry = _AiSCPowerConverterEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 3, 3, 1)
)
aiSCPowerConverterEntry.setIndexNames(
    (0, "AISYSCFGPOWER-MIB", "aiSCPowerConverterIndex"),
)
if mibBuilder.loadTexts:
    aiSCPowerConverterEntry.setStatus("current")


class _AiSCPowerConverterIndex_Type(Integer32):
    """Custom type aiSCPowerConverterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AiSCPowerConverterIndex_Type.__name__ = "Integer32"
_AiSCPowerConverterIndex_Object = MibTableColumn
aiSCPowerConverterIndex = _AiSCPowerConverterIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 3, 3, 1, 1),
    _AiSCPowerConverterIndex_Type()
)
aiSCPowerConverterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCPowerConverterIndex.setStatus("current")


class _AiSCPowerConverterDescription_Type(DisplayString):
    """Custom type aiSCPowerConverterDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AiSCPowerConverterDescription_Type.__name__ = "DisplayString"
_AiSCPowerConverterDescription_Object = MibTableColumn
aiSCPowerConverterDescription = _AiSCPowerConverterDescription_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 3, 3, 1, 2),
    _AiSCPowerConverterDescription_Type()
)
aiSCPowerConverterDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCPowerConverterDescription.setStatus("current")


class _AiSCPowerConverterStatus_Type(Integer32):
    """Custom type aiSCPowerConverterStatus based on Integer32"""
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
        *(("fail", 2),
          ("okay", 1),
          ("overVoltage", 4),
          ("underVoltage", 3))
    )


_AiSCPowerConverterStatus_Type.__name__ = "Integer32"
_AiSCPowerConverterStatus_Object = MibTableColumn
aiSCPowerConverterStatus = _AiSCPowerConverterStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 32, 3, 3, 1, 3),
    _AiSCPowerConverterStatus_Type()
)
aiSCPowerConverterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSCPowerConverterStatus.setStatus("current")

# Managed Objects groups


# Notification objects

aiSCPowerTrapFeedFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 539, 32, 3, 0, 1)
)
aiSCPowerTrapFeedFail.setObjects(
      *(("AISYSCFGPOWER-MIB", "aiSCPowerFeedIndex"),
        ("AISYSCFGPOWER-MIB", "aiSCPowerFeedStatus"))
)
if mibBuilder.loadTexts:
    aiSCPowerTrapFeedFail.setStatus(
        "current"
    )

aiSCPowerTrapFeedOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 539, 32, 3, 0, 2)
)
aiSCPowerTrapFeedOk.setObjects(
      *(("AISYSCFGPOWER-MIB", "aiSCPowerFeedIndex"),
        ("AISYSCFGPOWER-MIB", "aiSCPowerFeedStatus"))
)
if mibBuilder.loadTexts:
    aiSCPowerTrapFeedOk.setStatus(
        "current"
    )

aiSCPowerTrapConverterFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 539, 32, 3, 0, 3)
)
aiSCPowerTrapConverterFail.setObjects(
      *(("AISYSCFGPOWER-MIB", "aiSCPowerConverterIndex"),
        ("AISYSCFGPOWER-MIB", "aiSCPowerConverterStatus"))
)
if mibBuilder.loadTexts:
    aiSCPowerTrapConverterFail.setStatus(
        "current"
    )

aiSCPowerTrapConverterOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 539, 32, 3, 0, 4)
)
aiSCPowerTrapConverterOk.setObjects(
      *(("AISYSCFGPOWER-MIB", "aiSCPowerConverterIndex"),
        ("AISYSCFGPOWER-MIB", "aiSCPowerConverterStatus"))
)
if mibBuilder.loadTexts:
    aiSCPowerTrapConverterOk.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AISYSCFGPOWER-MIB",
    **{"aii": aii,
       "aiSysCfg": aiSysCfg,
       "aiSysCfgPower": aiSysCfgPower,
       "aiSCPowerTrapInfo": aiSCPowerTrapInfo,
       "aiSCPowerTrapFeedFail": aiSCPowerTrapFeedFail,
       "aiSCPowerTrapFeedOk": aiSCPowerTrapFeedOk,
       "aiSCPowerTrapConverterFail": aiSCPowerTrapConverterFail,
       "aiSCPowerTrapConverterOk": aiSCPowerTrapConverterOk,
       "aiSCPowerAgregateStatus": aiSCPowerAgregateStatus,
       "aiSCPowerFeedTable": aiSCPowerFeedTable,
       "aiSCPowerFeedEntry": aiSCPowerFeedEntry,
       "aiSCPowerFeedIndex": aiSCPowerFeedIndex,
       "aiSCPowerFeedDescription": aiSCPowerFeedDescription,
       "aiSCPowerFeedStatus": aiSCPowerFeedStatus,
       "aiSCPowerConverterTable": aiSCPowerConverterTable,
       "aiSCPowerConverterEntry": aiSCPowerConverterEntry,
       "aiSCPowerConverterIndex": aiSCPowerConverterIndex,
       "aiSCPowerConverterDescription": aiSCPowerConverterDescription,
       "aiSCPowerConverterStatus": aiSCPowerConverterStatus}
)
