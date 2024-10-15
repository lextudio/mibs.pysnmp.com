# SNMP MIB module (DELLLOCALRESPONSEAGENTMIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DELLLOCALRESPONSEAGENTMIF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:24:08 2024
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


# Types definitions



class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




class DmiDisplaystring(DisplayString):
    """Custom type DmiDisplaystring based on DisplayString"""




class DmiDate(OctetString):
    """Custom type DmiDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(28, 28),
    )





class DmiComponentIndex(Integer32):
    """Custom type DmiComponentIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_Server_ObjectIdentity = ObjectIdentity
server = _Server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10890)
)
_Localresponseagent_ObjectIdentity = ObjectIdentity
localresponseagent = _Localresponseagent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3)
)
_DmtfGroups_ObjectIdentity = ObjectIdentity
dmtfGroups = _DmtfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1)
)
_TComponentid_Object = MibTable
tComponentid = _TComponentid_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tComponentid.setStatus("mandatory")
_EComponentid_Object = MibTableRow
eComponentid = _EComponentid_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1, 1)
)
eComponentid.setIndexNames(
    (0, "DELLLOCALRESPONSEAGENTMIF-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eComponentid.setStatus("mandatory")
_A1Manufacturer_Type = DmiDisplaystring
_A1Manufacturer_Object = MibTableColumn
a1Manufacturer = _A1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1, 1, 1),
    _A1Manufacturer_Type()
)
a1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Manufacturer.setStatus("mandatory")
_A1Product_Type = DmiDisplaystring
_A1Product_Object = MibTableColumn
a1Product = _A1Product_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1, 1, 2),
    _A1Product_Type()
)
a1Product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Product.setStatus("mandatory")
_A1Version_Type = DmiDisplaystring
_A1Version_Object = MibTableColumn
a1Version = _A1Version_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1, 1, 3),
    _A1Version_Type()
)
a1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Version.setStatus("mandatory")
_A1SerialNumber_Type = DmiDisplaystring
_A1SerialNumber_Object = MibTableColumn
a1SerialNumber = _A1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1, 1, 4),
    _A1SerialNumber_Type()
)
a1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1SerialNumber.setStatus("mandatory")
_A1Installation_Type = DmiDate
_A1Installation_Object = MibTableColumn
a1Installation = _A1Installation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1, 1, 5),
    _A1Installation_Type()
)
a1Installation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Installation.setStatus("mandatory")


class _A1Verify_Type(Integer32):
    """Custom type a1Verify based on Integer32"""
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
        *(("vAnErrorOccurredCheckStatusCode", 0),
          ("vReserved", 3),
          ("vTheVerifyIsNotSupported", 2),
          ("vThisComponentDoesNotExist", 1),
          ("vThisComponentExistsAndIsFunctioningCorr", 7),
          ("vThisComponentExistsAndIsNotFunctioningC", 6),
          ("vThisComponentExistsButTheFunctionality1", 5),
          ("vThisComponentExistsButTheFunctionalityI", 4))
    )


_A1Verify_Type.__name__ = "Integer32"
_A1Verify_Object = MibTableColumn
a1Verify = _A1Verify_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1, 1, 6),
    _A1Verify_Type()
)
a1Verify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Verify.setStatus("mandatory")
_TActionResponseTable_Object = MibTable
tActionResponseTable = _TActionResponseTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 2)
)
if mibBuilder.loadTexts:
    tActionResponseTable.setStatus("mandatory")
_EActionResponseTable_Object = MibTableRow
eActionResponseTable = _EActionResponseTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 2, 1)
)
eActionResponseTable.setIndexNames(
    (0, "DELLLOCALRESPONSEAGENTMIF-MIB", "DmiComponentIndex"),
    (0, "DELLLOCALRESPONSEAGENTMIF-MIB", "a2Actionname"),
)
if mibBuilder.loadTexts:
    eActionResponseTable.setStatus("mandatory")


class _A2Actionname_Type(Integer32):
    """Custom type a2Actionname based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              7,
              13,
              14,
              160,
              168,
              172,
              200,
              202,
              204,
              206,
              208,
              210,
              212,
              214,
              220,
              225)
        )
    )
    namedValues = NamedValues(
        *(("vAdaptec-HostAdapterFailed", 3),
          ("vAdaptec-LogicalUnitFailed", 7),
          ("vApc-SystemOnLowBatteryPower", 14),
          ("vApc-SystemOnLowUtilityPower", 13),
          ("vChassisIntrusionDetected", 220),
          ("vCurrentSensorDetectedAFailure", 206),
          ("vCurrentSensorWarningDetected", 208),
          ("vFanSensorDetectedAFailure", 168),
          ("vFanSensorWarningDetected", 204),
          ("vLostConnectionToDiskPod", 225),
          ("vPowerSupplyDegradedRedundancyDetected", 212),
          ("vPowerSupplyDetectedAFailure", 214),
          ("vPowerSupplyLostRedundancyDetected", 210),
          ("vTemperatureSensorDetectedAFailure", 160),
          ("vTemperatureSensorWarningDetected", 200),
          ("vUnknown", 0),
          ("vVoltageSensorDetectedAFailure", 172),
          ("vVoltageSensorWarningDetected", 202))
    )


_A2Actionname_Type.__name__ = "Integer32"
_A2Actionname_Object = MibTableColumn
a2Actionname = _A2Actionname_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 2, 1, 1),
    _A2Actionname_Type()
)
a2Actionname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Actionname.setStatus("mandatory")
_A2Actionresponse_Type = DmiDisplaystring
_A2Actionresponse_Object = MibTableColumn
a2Actionresponse = _A2Actionresponse_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 2, 1, 2),
    _A2Actionresponse_Type()
)
a2Actionresponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2Actionresponse.setStatus("mandatory")
_A2Actionexecute_Type = DmiDisplaystring
_A2Actionexecute_Object = MibTableColumn
a2Actionexecute = _A2Actionexecute_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 2, 1, 3),
    _A2Actionexecute_Type()
)
a2Actionexecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2Actionexecute.setStatus("mandatory")
_A2Actionsource_Type = DmiDisplaystring
_A2Actionsource_Object = MibTableColumn
a2Actionsource = _A2Actionsource_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 2, 1, 4),
    _A2Actionsource_Type()
)
a2Actionsource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Actionsource.setStatus("mandatory")
_TActionCapabilities_Object = MibTable
tActionCapabilities = _TActionCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 3)
)
if mibBuilder.loadTexts:
    tActionCapabilities.setStatus("mandatory")
_EActionCapabilities_Object = MibTableRow
eActionCapabilities = _EActionCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 3, 1)
)
eActionCapabilities.setIndexNames(
    (0, "DELLLOCALRESPONSEAGENTMIF-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eActionCapabilities.setStatus("mandatory")
_A3LraCapabilities_Type = DmiInteger
_A3LraCapabilities_Object = MibTableColumn
a3LraCapabilities = _A3LraCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 3, 1, 1),
    _A3LraCapabilities_Type()
)
a3LraCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3LraCapabilities.setStatus("mandatory")
_TMiftomib_Object = MibTable
tMiftomib = _TMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 99)
)
if mibBuilder.loadTexts:
    tMiftomib.setStatus("mandatory")
_EMiftomib_Object = MibTableRow
eMiftomib = _EMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 99, 1)
)
eMiftomib.setIndexNames(
    (0, "DELLLOCALRESPONSEAGENTMIF-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eMiftomib.setStatus("mandatory")
_A99DellLocalResponseAgentMib_Type = DmiDisplaystring
_A99DellLocalResponseAgentMib_Object = MibTableColumn
a99DellLocalResponseAgentMib = _A99DellLocalResponseAgentMib_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 99, 1, 1),
    _A99DellLocalResponseAgentMib_Type()
)
a99DellLocalResponseAgentMib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99DellLocalResponseAgentMib.setStatus("mandatory")
_A99MibOid_Type = DmiDisplaystring
_A99MibOid_Object = MibTableColumn
a99MibOid = _A99MibOid_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 99, 1, 2),
    _A99MibOid_Type()
)
a99MibOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99MibOid.setStatus("mandatory")
_A99DisableTraps_Type = DmiInteger
_A99DisableTraps_Object = MibTableColumn
a99DisableTraps = _A99DisableTraps_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 99, 1, 3),
    _A99DisableTraps_Type()
)
a99DisableTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99DisableTraps.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELLLOCALRESPONSEAGENTMIF-MIB",
    **{"DmiInteger": DmiInteger,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiDate": DmiDate,
       "DmiComponentIndex": DmiComponentIndex,
       "dell": dell,
       "server": server,
       "localresponseagent": localresponseagent,
       "dmtfGroups": dmtfGroups,
       "tComponentid": tComponentid,
       "eComponentid": eComponentid,
       "a1Manufacturer": a1Manufacturer,
       "a1Product": a1Product,
       "a1Version": a1Version,
       "a1SerialNumber": a1SerialNumber,
       "a1Installation": a1Installation,
       "a1Verify": a1Verify,
       "tActionResponseTable": tActionResponseTable,
       "eActionResponseTable": eActionResponseTable,
       "a2Actionname": a2Actionname,
       "a2Actionresponse": a2Actionresponse,
       "a2Actionexecute": a2Actionexecute,
       "a2Actionsource": a2Actionsource,
       "tActionCapabilities": tActionCapabilities,
       "eActionCapabilities": eActionCapabilities,
       "a3LraCapabilities": a3LraCapabilities,
       "tMiftomib": tMiftomib,
       "eMiftomib": eMiftomib,
       "a99DellLocalResponseAgentMib": a99DellLocalResponseAgentMib,
       "a99MibOid": a99MibOid,
       "a99DisableTraps": a99DisableTraps}
)
