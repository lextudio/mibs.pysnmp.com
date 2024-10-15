# SNMP MIB module (HHMSAGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HHMSAGENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:25 2024
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

_Akcp_ObjectIdentity = ObjectIdentity
akcp = _Akcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3854)
)
_Hhmsagent_ObjectIdentity = ObjectIdentity
hhmsagent = _Hhmsagent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3854, 1)
)
_HhmsAgentSummary_ObjectIdentity = ObjectIdentity
hhmsAgentSummary = _HhmsAgentSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3854, 1, 1)
)
_HhmsAgentLocation_Type = DisplayString
_HhmsAgentLocation_Object = MibScalar
hhmsAgentLocation = _HhmsAgentLocation_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 1, 1),
    _HhmsAgentLocation_Type()
)
hhmsAgentLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsAgentLocation.setStatus("mandatory")


class _HhmsAgentStatus_Type(Integer32):
    """Custom type hhmsAgentStatus based on Integer32"""
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
        *(("critical", 4),
          ("noStatus", 1),
          ("normal", 2),
          ("sensorError", 5),
          ("warning", 3))
    )


_HhmsAgentStatus_Type.__name__ = "Integer32"
_HhmsAgentStatus_Object = MibScalar
hhmsAgentStatus = _HhmsAgentStatus_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 1, 2),
    _HhmsAgentStatus_Type()
)
hhmsAgentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsAgentStatus.setStatus("mandatory")
_HhmsNumberBadSensors_Type = Integer32
_HhmsNumberBadSensors_Object = MibScalar
hhmsNumberBadSensors = _HhmsNumberBadSensors_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 1, 4),
    _HhmsNumberBadSensors_Type()
)
hhmsNumberBadSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsNumberBadSensors.setStatus("mandatory")
_HhmsLocationBadSensor_Type = DisplayString
_HhmsLocationBadSensor_Object = MibScalar
hhmsLocationBadSensor = _HhmsLocationBadSensor_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 1, 5),
    _HhmsLocationBadSensor_Type()
)
hhmsLocationBadSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsLocationBadSensor.setStatus("mandatory")
_HhmsAgentManufName_Type = DisplayString
_HhmsAgentManufName_Object = MibScalar
hhmsAgentManufName = _HhmsAgentManufName_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 1, 6),
    _HhmsAgentManufName_Type()
)
hhmsAgentManufName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsAgentManufName.setStatus("mandatory")
_HhmsAgentHelpUrl_Type = DisplayString
_HhmsAgentHelpUrl_Object = MibScalar
hhmsAgentHelpUrl = _HhmsAgentHelpUrl_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 1, 7),
    _HhmsAgentHelpUrl_Type()
)
hhmsAgentHelpUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsAgentHelpUrl.setStatus("mandatory")


class _HhmsAgentHtmlView_Type(Integer32):
    """Custom type hhmsAgentHtmlView based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("advanced", 3),
          ("sensorArray", 1),
          ("sensorArrayPro", 2))
    )


_HhmsAgentHtmlView_Type.__name__ = "Integer32"
_HhmsAgentHtmlView_Object = MibScalar
hhmsAgentHtmlView = _HhmsAgentHtmlView_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 1, 8),
    _HhmsAgentHtmlView_Type()
)
hhmsAgentHtmlView.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsAgentHtmlView.setStatus("mandatory")
_HhmsAgentHtmlStandardTitle_Type = DisplayString
_HhmsAgentHtmlStandardTitle_Object = MibScalar
hhmsAgentHtmlStandardTitle = _HhmsAgentHtmlStandardTitle_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 1, 9),
    _HhmsAgentHtmlStandardTitle_Type()
)
hhmsAgentHtmlStandardTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsAgentHtmlStandardTitle.setStatus("mandatory")
_HhmsAgentHtmlStandardButton_Type = DisplayString
_HhmsAgentHtmlStandardButton_Object = MibScalar
hhmsAgentHtmlStandardButton = _HhmsAgentHtmlStandardButton_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 1, 10),
    _HhmsAgentHtmlStandardButton_Type()
)
hhmsAgentHtmlStandardButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsAgentHtmlStandardButton.setStatus("mandatory")
_HhmsSensor_ObjectIdentity = ObjectIdentity
hhmsSensor = _HhmsSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2)
)
_HhmsSensorArrayTable_ObjectIdentity = ObjectIdentity
hhmsSensorArrayTable = _HhmsSensorArrayTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2)
)
_HhmsSensorArrayEntry_ObjectIdentity = ObjectIdentity
hhmsSensorArrayEntry = _HhmsSensorArrayEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1)
)
_HhmsSensorArrayHost_Type = IpAddress
_HhmsSensorArrayHost_Object = MibScalar
hhmsSensorArrayHost = _HhmsSensorArrayHost_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 1),
    _HhmsSensorArrayHost_Type()
)
hhmsSensorArrayHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayHost.setStatus("mandatory")


class _HhmsSensorArrayUseDHCP_Type(Integer32):
    """Custom type hhmsSensorArrayUseDHCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_HhmsSensorArrayUseDHCP_Type.__name__ = "Integer32"
_HhmsSensorArrayUseDHCP_Object = MibScalar
hhmsSensorArrayUseDHCP = _HhmsSensorArrayUseDHCP_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 2),
    _HhmsSensorArrayUseDHCP_Type()
)
hhmsSensorArrayUseDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayUseDHCP.setStatus("mandatory")
_HhmsSensorArrayMAC_Type = DisplayString
_HhmsSensorArrayMAC_Object = MibScalar
hhmsSensorArrayMAC = _HhmsSensorArrayMAC_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 3),
    _HhmsSensorArrayMAC_Type()
)
hhmsSensorArrayMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayMAC.setStatus("mandatory")
_HhmsSensorArraySetCommunity_Type = DisplayString
_HhmsSensorArraySetCommunity_Object = MibScalar
hhmsSensorArraySetCommunity = _HhmsSensorArraySetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 4),
    _HhmsSensorArraySetCommunity_Type()
)
hhmsSensorArraySetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArraySetCommunity.setStatus("mandatory")
_HhmsSensorArrayGetCommunity_Type = DisplayString
_HhmsSensorArrayGetCommunity_Object = MibScalar
hhmsSensorArrayGetCommunity = _HhmsSensorArrayGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 5),
    _HhmsSensorArrayGetCommunity_Type()
)
hhmsSensorArrayGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayGetCommunity.setStatus("mandatory")
_HhmsSensorArrayDescription_Type = DisplayString
_HhmsSensorArrayDescription_Object = MibScalar
hhmsSensorArrayDescription = _HhmsSensorArrayDescription_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 6),
    _HhmsSensorArrayDescription_Type()
)
hhmsSensorArrayDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayDescription.setStatus("mandatory")
_HhmsSensorArrayLocation_Type = DisplayString
_HhmsSensorArrayLocation_Object = MibScalar
hhmsSensorArrayLocation = _HhmsSensorArrayLocation_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 7),
    _HhmsSensorArrayLocation_Type()
)
hhmsSensorArrayLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayLocation.setStatus("mandatory")
_HhmsSensorArrayLastUpdate_Type = DisplayString
_HhmsSensorArrayLastUpdate_Object = MibScalar
hhmsSensorArrayLastUpdate = _HhmsSensorArrayLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 8),
    _HhmsSensorArrayLastUpdate_Type()
)
hhmsSensorArrayLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayLastUpdate.setStatus("mandatory")


class _HhmsSensorArrayStatus_Type(Integer32):
    """Custom type hhmsSensorArrayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              7)
        )
    )
    namedValues = NamedValues(
        *(("noStatus", 1),
          ("normal", 2),
          ("sensorError", 7))
    )


_HhmsSensorArrayStatus_Type.__name__ = "Integer32"
_HhmsSensorArrayStatus_Object = MibScalar
hhmsSensorArrayStatus = _HhmsSensorArrayStatus_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 9),
    _HhmsSensorArrayStatus_Type()
)
hhmsSensorArrayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayStatus.setStatus("mandatory")


class _HhmsSensorArrayOnline_Type(Integer32):
    """Custom type hhmsSensorArrayOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_HhmsSensorArrayOnline_Type.__name__ = "Integer32"
_HhmsSensorArrayOnline_Object = MibScalar
hhmsSensorArrayOnline = _HhmsSensorArrayOnline_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 10),
    _HhmsSensorArrayOnline_Type()
)
hhmsSensorArrayOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayOnline.setStatus("mandatory")


class _HhmsSensorArrayGoOnline_Type(Integer32):
    """Custom type hhmsSensorArrayGoOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("goOffline", 2),
          ("goOnline", 1))
    )


_HhmsSensorArrayGoOnline_Type.__name__ = "Integer32"
_HhmsSensorArrayGoOnline_Object = MibScalar
hhmsSensorArrayGoOnline = _HhmsSensorArrayGoOnline_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 11),
    _HhmsSensorArrayGoOnline_Type()
)
hhmsSensorArrayGoOnline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayGoOnline.setStatus("mandatory")
_HhmsSensorArrayReadInterval_Type = Integer32
_HhmsSensorArrayReadInterval_Object = MibScalar
hhmsSensorArrayReadInterval = _HhmsSensorArrayReadInterval_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 12),
    _HhmsSensorArrayReadInterval_Type()
)
hhmsSensorArrayReadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayReadInterval.setStatus("mandatory")
_HhmsSensorArrayReceiveTimeout_Type = Integer32
_HhmsSensorArrayReceiveTimeout_Object = MibScalar
hhmsSensorArrayReceiveTimeout = _HhmsSensorArrayReceiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 13),
    _HhmsSensorArrayReceiveTimeout_Type()
)
hhmsSensorArrayReceiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayReceiveTimeout.setStatus("mandatory")
_HhmsSensorArrayReceiveRetries_Type = Integer32
_HhmsSensorArrayReceiveRetries_Object = MibScalar
hhmsSensorArrayReceiveRetries = _HhmsSensorArrayReceiveRetries_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 14),
    _HhmsSensorArrayReceiveRetries_Type()
)
hhmsSensorArrayReceiveRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayReceiveRetries.setStatus("mandatory")
_HhmsSensorArrayVersion_Type = Integer32
_HhmsSensorArrayVersion_Object = MibScalar
hhmsSensorArrayVersion = _HhmsSensorArrayVersion_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 15),
    _HhmsSensorArrayVersion_Type()
)
hhmsSensorArrayVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayVersion.setStatus("mandatory")
_HhmsSensorArrayTempTable_Object = MibTable
hhmsSensorArrayTempTable = _HhmsSensorArrayTempTable_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 16)
)
if mibBuilder.loadTexts:
    hhmsSensorArrayTempTable.setStatus("mandatory")
_HhmsSensorArrayTempEntry_Object = MibTableRow
hhmsSensorArrayTempEntry = _HhmsSensorArrayTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 16, 1)
)
hhmsSensorArrayTempEntry.setIndexNames(
    (0, "HHMSAGENT-MIB", "hhmsSensorArrayTempIndex"),
)
if mibBuilder.loadTexts:
    hhmsSensorArrayTempEntry.setStatus("mandatory")
_HhmsSensorArrayTempDescription_Type = DisplayString
_HhmsSensorArrayTempDescription_Object = MibTableColumn
hhmsSensorArrayTempDescription = _HhmsSensorArrayTempDescription_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 16, 1, 1),
    _HhmsSensorArrayTempDescription_Type()
)
hhmsSensorArrayTempDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayTempDescription.setStatus("mandatory")
_HhmsSensorArrayTempLocation_Type = DisplayString
_HhmsSensorArrayTempLocation_Object = MibTableColumn
hhmsSensorArrayTempLocation = _HhmsSensorArrayTempLocation_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 16, 1, 2),
    _HhmsSensorArrayTempLocation_Type()
)
hhmsSensorArrayTempLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayTempLocation.setStatus("mandatory")
_HhmsSensorArrayTempDegree_Type = Integer32
_HhmsSensorArrayTempDegree_Object = MibTableColumn
hhmsSensorArrayTempDegree = _HhmsSensorArrayTempDegree_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 16, 1, 3),
    _HhmsSensorArrayTempDegree_Type()
)
hhmsSensorArrayTempDegree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayTempDegree.setStatus("mandatory")


class _HhmsSensorArrayTempStatus_Type(Integer32):
    """Custom type hhmsSensorArrayTempStatus based on Integer32"""
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
        *(("highCritical", 4),
          ("highWarning", 3),
          ("lowCritical", 6),
          ("lowWarning", 5),
          ("noStatus", 1),
          ("normal", 2),
          ("sensorError", 7))
    )


_HhmsSensorArrayTempStatus_Type.__name__ = "Integer32"
_HhmsSensorArrayTempStatus_Object = MibTableColumn
hhmsSensorArrayTempStatus = _HhmsSensorArrayTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 16, 1, 4),
    _HhmsSensorArrayTempStatus_Type()
)
hhmsSensorArrayTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayTempStatus.setStatus("mandatory")


class _HhmsSensorArrayTempOnline_Type(Integer32):
    """Custom type hhmsSensorArrayTempOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_HhmsSensorArrayTempOnline_Type.__name__ = "Integer32"
_HhmsSensorArrayTempOnline_Object = MibTableColumn
hhmsSensorArrayTempOnline = _HhmsSensorArrayTempOnline_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 16, 1, 5),
    _HhmsSensorArrayTempOnline_Type()
)
hhmsSensorArrayTempOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayTempOnline.setStatus("mandatory")


class _HhmsSensorArrayTempGoOnline_Type(Integer32):
    """Custom type hhmsSensorArrayTempGoOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("goOffline", 2),
          ("goOnline", 1))
    )


_HhmsSensorArrayTempGoOnline_Type.__name__ = "Integer32"
_HhmsSensorArrayTempGoOnline_Object = MibTableColumn
hhmsSensorArrayTempGoOnline = _HhmsSensorArrayTempGoOnline_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 16, 1, 6),
    _HhmsSensorArrayTempGoOnline_Type()
)
hhmsSensorArrayTempGoOnline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayTempGoOnline.setStatus("mandatory")
_HhmsSensorArrayTempHighWarning_Type = Integer32
_HhmsSensorArrayTempHighWarning_Object = MibTableColumn
hhmsSensorArrayTempHighWarning = _HhmsSensorArrayTempHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 16, 1, 7),
    _HhmsSensorArrayTempHighWarning_Type()
)
hhmsSensorArrayTempHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayTempHighWarning.setStatus("mandatory")
_HhmsSensorArrayTempHighCritical_Type = Integer32
_HhmsSensorArrayTempHighCritical_Object = MibTableColumn
hhmsSensorArrayTempHighCritical = _HhmsSensorArrayTempHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 16, 1, 8),
    _HhmsSensorArrayTempHighCritical_Type()
)
hhmsSensorArrayTempHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayTempHighCritical.setStatus("mandatory")
_HhmsSensorArrayTempLowWarning_Type = Integer32
_HhmsSensorArrayTempLowWarning_Object = MibTableColumn
hhmsSensorArrayTempLowWarning = _HhmsSensorArrayTempLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 16, 1, 9),
    _HhmsSensorArrayTempLowWarning_Type()
)
hhmsSensorArrayTempLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayTempLowWarning.setStatus("mandatory")
_HhmsSensorArrayTempLowCritical_Type = Integer32
_HhmsSensorArrayTempLowCritical_Object = MibTableColumn
hhmsSensorArrayTempLowCritical = _HhmsSensorArrayTempLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 16, 1, 10),
    _HhmsSensorArrayTempLowCritical_Type()
)
hhmsSensorArrayTempLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayTempLowCritical.setStatus("mandatory")
_HhmsSensorArrayTempRearm_Type = Integer32
_HhmsSensorArrayTempRearm_Object = MibTableColumn
hhmsSensorArrayTempRearm = _HhmsSensorArrayTempRearm_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 16, 1, 11),
    _HhmsSensorArrayTempRearm_Type()
)
hhmsSensorArrayTempRearm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayTempRearm.setStatus("mandatory")


class _HhmsSensorArrayTempDegreeType_Type(Integer32):
    """Custom type hhmsSensorArrayTempDegreeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 1),
          ("fahr", 0))
    )


_HhmsSensorArrayTempDegreeType_Type.__name__ = "Integer32"
_HhmsSensorArrayTempDegreeType_Object = MibTableColumn
hhmsSensorArrayTempDegreeType = _HhmsSensorArrayTempDegreeType_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 16, 1, 12),
    _HhmsSensorArrayTempDegreeType_Type()
)
hhmsSensorArrayTempDegreeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayTempDegreeType.setStatus("mandatory")


class _HhmsSensorArrayTempSensorType_Type(Integer32):
    """Custom type hhmsSensorArrayTempSensorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("type1", 0),
          ("type2", 1))
    )


_HhmsSensorArrayTempSensorType_Type.__name__ = "Integer32"
_HhmsSensorArrayTempSensorType_Object = MibTableColumn
hhmsSensorArrayTempSensorType = _HhmsSensorArrayTempSensorType_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 16, 1, 13),
    _HhmsSensorArrayTempSensorType_Type()
)
hhmsSensorArrayTempSensorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayTempSensorType.setStatus("mandatory")


class _HhmsSensorArrayTempTestStatus_Type(Integer32):
    """Custom type hhmsSensorArrayTempTestStatus based on Integer32"""
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
        *(("sensorError", 7),
          ("testHighCritical", 4),
          ("testHighWarning", 3),
          ("testLowCritical", 6),
          ("testLowWarning", 5),
          ("testNoStatus", 1),
          ("testNormal", 2))
    )


_HhmsSensorArrayTempTestStatus_Type.__name__ = "Integer32"
_HhmsSensorArrayTempTestStatus_Object = MibTableColumn
hhmsSensorArrayTempTestStatus = _HhmsSensorArrayTempTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 16, 1, 14),
    _HhmsSensorArrayTempTestStatus_Type()
)
hhmsSensorArrayTempTestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayTempTestStatus.setStatus("mandatory")
_HhmsSensorArrayTempTestDegree_Type = Integer32
_HhmsSensorArrayTempTestDegree_Object = MibTableColumn
hhmsSensorArrayTempTestDegree = _HhmsSensorArrayTempTestDegree_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 16, 1, 15),
    _HhmsSensorArrayTempTestDegree_Type()
)
hhmsSensorArrayTempTestDegree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayTempTestDegree.setStatus("mandatory")


class _HhmsSensorArrayTempIndex_Type(Integer32):
    """Custom type hhmsSensorArrayTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_HhmsSensorArrayTempIndex_Type.__name__ = "Integer32"
_HhmsSensorArrayTempIndex_Object = MibTableColumn
hhmsSensorArrayTempIndex = _HhmsSensorArrayTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 16, 1, 16),
    _HhmsSensorArrayTempIndex_Type()
)
hhmsSensorArrayTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayTempIndex.setStatus("mandatory")
_HhmsSensorArrayHumidityTable_Object = MibTable
hhmsSensorArrayHumidityTable = _HhmsSensorArrayHumidityTable_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 17)
)
if mibBuilder.loadTexts:
    hhmsSensorArrayHumidityTable.setStatus("mandatory")
_HhmsSensorArrayHumidityEntry_Object = MibTableRow
hhmsSensorArrayHumidityEntry = _HhmsSensorArrayHumidityEntry_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 17, 1)
)
hhmsSensorArrayHumidityEntry.setIndexNames(
    (0, "HHMSAGENT-MIB", "hhmsSensorArrayHumidityIndex"),
)
if mibBuilder.loadTexts:
    hhmsSensorArrayHumidityEntry.setStatus("mandatory")
_HhmsSensorArrayHumidityDescription_Type = DisplayString
_HhmsSensorArrayHumidityDescription_Object = MibTableColumn
hhmsSensorArrayHumidityDescription = _HhmsSensorArrayHumidityDescription_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 17, 1, 1),
    _HhmsSensorArrayHumidityDescription_Type()
)
hhmsSensorArrayHumidityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayHumidityDescription.setStatus("mandatory")
_HhmsSensorArrayHumidityLocation_Type = DisplayString
_HhmsSensorArrayHumidityLocation_Object = MibTableColumn
hhmsSensorArrayHumidityLocation = _HhmsSensorArrayHumidityLocation_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 17, 1, 2),
    _HhmsSensorArrayHumidityLocation_Type()
)
hhmsSensorArrayHumidityLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayHumidityLocation.setStatus("mandatory")
_HhmsSensorArrayHumidityPercent_Type = Integer32
_HhmsSensorArrayHumidityPercent_Object = MibTableColumn
hhmsSensorArrayHumidityPercent = _HhmsSensorArrayHumidityPercent_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 17, 1, 3),
    _HhmsSensorArrayHumidityPercent_Type()
)
hhmsSensorArrayHumidityPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayHumidityPercent.setStatus("mandatory")


class _HhmsSensorArrayHumidityStatus_Type(Integer32):
    """Custom type hhmsSensorArrayHumidityStatus based on Integer32"""
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
        *(("highCritical", 4),
          ("highWarning", 3),
          ("lowCritical", 6),
          ("lowWarning", 5),
          ("noStatus", 1),
          ("normal", 2),
          ("sensorError", 7))
    )


_HhmsSensorArrayHumidityStatus_Type.__name__ = "Integer32"
_HhmsSensorArrayHumidityStatus_Object = MibTableColumn
hhmsSensorArrayHumidityStatus = _HhmsSensorArrayHumidityStatus_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 17, 1, 4),
    _HhmsSensorArrayHumidityStatus_Type()
)
hhmsSensorArrayHumidityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayHumidityStatus.setStatus("mandatory")


class _HhmsSensorArrayHumidityOnline_Type(Integer32):
    """Custom type hhmsSensorArrayHumidityOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_HhmsSensorArrayHumidityOnline_Type.__name__ = "Integer32"
_HhmsSensorArrayHumidityOnline_Object = MibTableColumn
hhmsSensorArrayHumidityOnline = _HhmsSensorArrayHumidityOnline_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 17, 1, 5),
    _HhmsSensorArrayHumidityOnline_Type()
)
hhmsSensorArrayHumidityOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayHumidityOnline.setStatus("mandatory")


class _HhmsSensorArrayHumidityGoOnline_Type(Integer32):
    """Custom type hhmsSensorArrayHumidityGoOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("goOffline", 2),
          ("goOnline", 1))
    )


_HhmsSensorArrayHumidityGoOnline_Type.__name__ = "Integer32"
_HhmsSensorArrayHumidityGoOnline_Object = MibTableColumn
hhmsSensorArrayHumidityGoOnline = _HhmsSensorArrayHumidityGoOnline_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 17, 1, 6),
    _HhmsSensorArrayHumidityGoOnline_Type()
)
hhmsSensorArrayHumidityGoOnline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayHumidityGoOnline.setStatus("mandatory")
_HhmsSensorArrayHumidityHighWarning_Type = Integer32
_HhmsSensorArrayHumidityHighWarning_Object = MibTableColumn
hhmsSensorArrayHumidityHighWarning = _HhmsSensorArrayHumidityHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 17, 1, 7),
    _HhmsSensorArrayHumidityHighWarning_Type()
)
hhmsSensorArrayHumidityHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayHumidityHighWarning.setStatus("mandatory")
_HhmsSensorArrayHumidityHighCritical_Type = Integer32
_HhmsSensorArrayHumidityHighCritical_Object = MibTableColumn
hhmsSensorArrayHumidityHighCritical = _HhmsSensorArrayHumidityHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 17, 1, 8),
    _HhmsSensorArrayHumidityHighCritical_Type()
)
hhmsSensorArrayHumidityHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayHumidityHighCritical.setStatus("mandatory")
_HhmsSensorArrayHumidityLowWarning_Type = Integer32
_HhmsSensorArrayHumidityLowWarning_Object = MibTableColumn
hhmsSensorArrayHumidityLowWarning = _HhmsSensorArrayHumidityLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 17, 1, 9),
    _HhmsSensorArrayHumidityLowWarning_Type()
)
hhmsSensorArrayHumidityLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayHumidityLowWarning.setStatus("mandatory")
_HhmsSensorArrayHumidityLowCritical_Type = Integer32
_HhmsSensorArrayHumidityLowCritical_Object = MibTableColumn
hhmsSensorArrayHumidityLowCritical = _HhmsSensorArrayHumidityLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 17, 1, 10),
    _HhmsSensorArrayHumidityLowCritical_Type()
)
hhmsSensorArrayHumidityLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayHumidityLowCritical.setStatus("mandatory")
_HhmsSensorArrayHumidityRearm_Type = Integer32
_HhmsSensorArrayHumidityRearm_Object = MibTableColumn
hhmsSensorArrayHumidityRearm = _HhmsSensorArrayHumidityRearm_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 17, 1, 11),
    _HhmsSensorArrayHumidityRearm_Type()
)
hhmsSensorArrayHumidityRearm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayHumidityRearm.setStatus("mandatory")


class _HhmsSensorArrayHumidityTestStatus_Type(Integer32):
    """Custom type hhmsSensorArrayHumidityTestStatus based on Integer32"""
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
        *(("sensorError", 7),
          ("testHighCritical", 4),
          ("testHighWarning", 3),
          ("testLowCritical", 6),
          ("testLowWarning", 5),
          ("testNoStatus", 1),
          ("testNormal", 2))
    )


_HhmsSensorArrayHumidityTestStatus_Type.__name__ = "Integer32"
_HhmsSensorArrayHumidityTestStatus_Object = MibTableColumn
hhmsSensorArrayHumidityTestStatus = _HhmsSensorArrayHumidityTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 17, 1, 12),
    _HhmsSensorArrayHumidityTestStatus_Type()
)
hhmsSensorArrayHumidityTestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayHumidityTestStatus.setStatus("mandatory")
_HhmsSensorArrayHumidityTestPercent_Type = Integer32
_HhmsSensorArrayHumidityTestPercent_Object = MibTableColumn
hhmsSensorArrayHumidityTestPercent = _HhmsSensorArrayHumidityTestPercent_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 17, 1, 13),
    _HhmsSensorArrayHumidityTestPercent_Type()
)
hhmsSensorArrayHumidityTestPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayHumidityTestPercent.setStatus("mandatory")


class _HhmsSensorArrayHumidityIndex_Type(Integer32):
    """Custom type hhmsSensorArrayHumidityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HhmsSensorArrayHumidityIndex_Type.__name__ = "Integer32"
_HhmsSensorArrayHumidityIndex_Object = MibTableColumn
hhmsSensorArrayHumidityIndex = _HhmsSensorArrayHumidityIndex_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 17, 1, 14),
    _HhmsSensorArrayHumidityIndex_Type()
)
hhmsSensorArrayHumidityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayHumidityIndex.setStatus("mandatory")
_HhmsSensorArraySwitchTable_Object = MibTable
hhmsSensorArraySwitchTable = _HhmsSensorArraySwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 18)
)
if mibBuilder.loadTexts:
    hhmsSensorArraySwitchTable.setStatus("mandatory")
_HhmsSensorArraySwitchEntry_Object = MibTableRow
hhmsSensorArraySwitchEntry = _HhmsSensorArraySwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 18, 1)
)
hhmsSensorArraySwitchEntry.setIndexNames(
    (0, "HHMSAGENT-MIB", "hhmsSensorArraySwitchIndex"),
)
if mibBuilder.loadTexts:
    hhmsSensorArraySwitchEntry.setStatus("mandatory")
_HhmsSensorArraySwitchDescription_Type = DisplayString
_HhmsSensorArraySwitchDescription_Object = MibTableColumn
hhmsSensorArraySwitchDescription = _HhmsSensorArraySwitchDescription_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 18, 1, 1),
    _HhmsSensorArraySwitchDescription_Type()
)
hhmsSensorArraySwitchDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArraySwitchDescription.setStatus("mandatory")
_HhmsSensorArraySwitchLocation_Type = DisplayString
_HhmsSensorArraySwitchLocation_Object = MibTableColumn
hhmsSensorArraySwitchLocation = _HhmsSensorArraySwitchLocation_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 18, 1, 2),
    _HhmsSensorArraySwitchLocation_Type()
)
hhmsSensorArraySwitchLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArraySwitchLocation.setStatus("mandatory")


class _HhmsSensorArraySwitchStatus_Type(Integer32):
    """Custom type hhmsSensorArraySwitchStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("noStatus", 1),
          ("normal", 2),
          ("sensorError", 7))
    )


_HhmsSensorArraySwitchStatus_Type.__name__ = "Integer32"
_HhmsSensorArraySwitchStatus_Object = MibTableColumn
hhmsSensorArraySwitchStatus = _HhmsSensorArraySwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 18, 1, 3),
    _HhmsSensorArraySwitchStatus_Type()
)
hhmsSensorArraySwitchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArraySwitchStatus.setStatus("mandatory")


class _HhmsSensorArraySwitchOnline_Type(Integer32):
    """Custom type hhmsSensorArraySwitchOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_HhmsSensorArraySwitchOnline_Type.__name__ = "Integer32"
_HhmsSensorArraySwitchOnline_Object = MibTableColumn
hhmsSensorArraySwitchOnline = _HhmsSensorArraySwitchOnline_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 18, 1, 4),
    _HhmsSensorArraySwitchOnline_Type()
)
hhmsSensorArraySwitchOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArraySwitchOnline.setStatus("mandatory")


class _HhmsSensorArraySwitchGoOnline_Type(Integer32):
    """Custom type hhmsSensorArraySwitchGoOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("goOffline", 2),
          ("goOnline", 1))
    )


_HhmsSensorArraySwitchGoOnline_Type.__name__ = "Integer32"
_HhmsSensorArraySwitchGoOnline_Object = MibTableColumn
hhmsSensorArraySwitchGoOnline = _HhmsSensorArraySwitchGoOnline_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 18, 1, 5),
    _HhmsSensorArraySwitchGoOnline_Type()
)
hhmsSensorArraySwitchGoOnline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArraySwitchGoOnline.setStatus("mandatory")


class _HhmsSensorArraySwitchDirection_Type(Integer32):
    """Custom type hhmsSensorArraySwitchDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("input", 0),
          ("output", 1))
    )


_HhmsSensorArraySwitchDirection_Type.__name__ = "Integer32"
_HhmsSensorArraySwitchDirection_Object = MibTableColumn
hhmsSensorArraySwitchDirection = _HhmsSensorArraySwitchDirection_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 18, 1, 6),
    _HhmsSensorArraySwitchDirection_Type()
)
hhmsSensorArraySwitchDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArraySwitchDirection.setStatus("mandatory")


class _HhmsSensorArraySwitchNormalState_Type(Integer32):
    """Custom type hhmsSensorArraySwitchNormalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 0),
          ("open", 1))
    )


_HhmsSensorArraySwitchNormalState_Type.__name__ = "Integer32"
_HhmsSensorArraySwitchNormalState_Object = MibTableColumn
hhmsSensorArraySwitchNormalState = _HhmsSensorArraySwitchNormalState_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 18, 1, 7),
    _HhmsSensorArraySwitchNormalState_Type()
)
hhmsSensorArraySwitchNormalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArraySwitchNormalState.setStatus("mandatory")


class _HhmsSensorArraySwitchOutputLevel_Type(Integer32):
    """Custom type hhmsSensorArraySwitchOutputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_HhmsSensorArraySwitchOutputLevel_Type.__name__ = "Integer32"
_HhmsSensorArraySwitchOutputLevel_Object = MibTableColumn
hhmsSensorArraySwitchOutputLevel = _HhmsSensorArraySwitchOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 18, 1, 8),
    _HhmsSensorArraySwitchOutputLevel_Type()
)
hhmsSensorArraySwitchOutputLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArraySwitchOutputLevel.setStatus("mandatory")


class _HhmsSensorArraySwitchTestState_Type(Integer32):
    """Custom type hhmsSensorArraySwitchTestState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("noStatus", 1),
          ("normal", 2),
          ("sensorError", 7))
    )


_HhmsSensorArraySwitchTestState_Type.__name__ = "Integer32"
_HhmsSensorArraySwitchTestState_Object = MibTableColumn
hhmsSensorArraySwitchTestState = _HhmsSensorArraySwitchTestState_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 18, 1, 9),
    _HhmsSensorArraySwitchTestState_Type()
)
hhmsSensorArraySwitchTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArraySwitchTestState.setStatus("mandatory")


class _HhmsSensorArraySwitchIndex_Type(Integer32):
    """Custom type hhmsSensorArraySwitchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_HhmsSensorArraySwitchIndex_Type.__name__ = "Integer32"
_HhmsSensorArraySwitchIndex_Object = MibTableColumn
hhmsSensorArraySwitchIndex = _HhmsSensorArraySwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 18, 1, 10),
    _HhmsSensorArraySwitchIndex_Type()
)
hhmsSensorArraySwitchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArraySwitchIndex.setStatus("mandatory")
_HhmsSensorArraySerialTable_Object = MibTable
hhmsSensorArraySerialTable = _HhmsSensorArraySerialTable_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 19)
)
if mibBuilder.loadTexts:
    hhmsSensorArraySerialTable.setStatus("mandatory")
_HhmsSensorArraySerialEntry_Object = MibTableRow
hhmsSensorArraySerialEntry = _HhmsSensorArraySerialEntry_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 19, 1)
)
hhmsSensorArraySerialEntry.setIndexNames(
    (0, "HHMSAGENT-MIB", "hhmsSensorArraySerialIndex"),
)
if mibBuilder.loadTexts:
    hhmsSensorArraySerialEntry.setStatus("mandatory")
_HhmsSensorArraySerialDescription_Type = DisplayString
_HhmsSensorArraySerialDescription_Object = MibTableColumn
hhmsSensorArraySerialDescription = _HhmsSensorArraySerialDescription_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 19, 1, 1),
    _HhmsSensorArraySerialDescription_Type()
)
hhmsSensorArraySerialDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArraySerialDescription.setStatus("mandatory")
_HhmsSensorArraySerialLocation_Type = DisplayString
_HhmsSensorArraySerialLocation_Object = MibTableColumn
hhmsSensorArraySerialLocation = _HhmsSensorArraySerialLocation_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 19, 1, 2),
    _HhmsSensorArraySerialLocation_Type()
)
hhmsSensorArraySerialLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArraySerialLocation.setStatus("mandatory")


class _HhmsSensorArraySerialStatus_Type(Integer32):
    """Custom type hhmsSensorArraySerialStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("noStatus", 1),
          ("normal", 2),
          ("sensorError", 7))
    )


_HhmsSensorArraySerialStatus_Type.__name__ = "Integer32"
_HhmsSensorArraySerialStatus_Object = MibTableColumn
hhmsSensorArraySerialStatus = _HhmsSensorArraySerialStatus_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 19, 1, 3),
    _HhmsSensorArraySerialStatus_Type()
)
hhmsSensorArraySerialStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArraySerialStatus.setStatus("mandatory")


class _HhmsSensorArraySerialOnline_Type(Integer32):
    """Custom type hhmsSensorArraySerialOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_HhmsSensorArraySerialOnline_Type.__name__ = "Integer32"
_HhmsSensorArraySerialOnline_Object = MibTableColumn
hhmsSensorArraySerialOnline = _HhmsSensorArraySerialOnline_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 19, 1, 4),
    _HhmsSensorArraySerialOnline_Type()
)
hhmsSensorArraySerialOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArraySerialOnline.setStatus("mandatory")


class _HhmsSensorArraySerialGoOnline_Type(Integer32):
    """Custom type hhmsSensorArraySerialGoOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("goOffline", 2),
          ("goOnline", 1))
    )


_HhmsSensorArraySerialGoOnline_Type.__name__ = "Integer32"
_HhmsSensorArraySerialGoOnline_Object = MibTableColumn
hhmsSensorArraySerialGoOnline = _HhmsSensorArraySerialGoOnline_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 19, 1, 5),
    _HhmsSensorArraySerialGoOnline_Type()
)
hhmsSensorArraySerialGoOnline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArraySerialGoOnline.setStatus("mandatory")
_HhmsSensorArraySerialData_Type = DisplayString
_HhmsSensorArraySerialData_Object = MibTableColumn
hhmsSensorArraySerialData = _HhmsSensorArraySerialData_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 19, 1, 6),
    _HhmsSensorArraySerialData_Type()
)
hhmsSensorArraySerialData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArraySerialData.setStatus("mandatory")


class _HhmsSensorArraySerialBaud_Type(Integer32):
    """Custom type hhmsSensorArraySerialBaud based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              7,
              10,
              15,
              32,
              64,
              129,
              255)
        )
    )
    namedValues = NamedValues(
        *(("baud115200", 2),
          ("baud1200", 255),
          ("baud19200", 15),
          ("baud2400", 129),
          ("baud28800", 10),
          ("baud38400", 7),
          ("baud4800", 64),
          ("baud57600", 4),
          ("baud9600", 32))
    )


_HhmsSensorArraySerialBaud_Type.__name__ = "Integer32"
_HhmsSensorArraySerialBaud_Object = MibTableColumn
hhmsSensorArraySerialBaud = _HhmsSensorArraySerialBaud_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 19, 1, 7),
    _HhmsSensorArraySerialBaud_Type()
)
hhmsSensorArraySerialBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArraySerialBaud.setStatus("mandatory")


class _HhmsSensorArraySerialDataBits_Type(Integer32):
    """Custom type hhmsSensorArraySerialDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            8
        )
    )
    namedValues = NamedValues(
        ("eight", 8)
    )


_HhmsSensorArraySerialDataBits_Type.__name__ = "Integer32"
_HhmsSensorArraySerialDataBits_Object = MibTableColumn
hhmsSensorArraySerialDataBits = _HhmsSensorArraySerialDataBits_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 19, 1, 8),
    _HhmsSensorArraySerialDataBits_Type()
)
hhmsSensorArraySerialDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArraySerialDataBits.setStatus("mandatory")


class _HhmsSensorArraySerialParity_Type(Integer32):
    """Custom type hhmsSensorArraySerialParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("none", 1)
    )


_HhmsSensorArraySerialParity_Type.__name__ = "Integer32"
_HhmsSensorArraySerialParity_Object = MibTableColumn
hhmsSensorArraySerialParity = _HhmsSensorArraySerialParity_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 19, 1, 9),
    _HhmsSensorArraySerialParity_Type()
)
hhmsSensorArraySerialParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArraySerialParity.setStatus("mandatory")


class _HhmsSensorArraySerialStop_Type(Integer32):
    """Custom type hhmsSensorArraySerialStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("one", 1)
    )


_HhmsSensorArraySerialStop_Type.__name__ = "Integer32"
_HhmsSensorArraySerialStop_Object = MibTableColumn
hhmsSensorArraySerialStop = _HhmsSensorArraySerialStop_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 19, 1, 10),
    _HhmsSensorArraySerialStop_Type()
)
hhmsSensorArraySerialStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArraySerialStop.setStatus("mandatory")


class _HhmsSensorArraySerialCTS_Type(Integer32):
    """Custom type hhmsSensorArraySerialCTS based on Integer32"""
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


_HhmsSensorArraySerialCTS_Type.__name__ = "Integer32"
_HhmsSensorArraySerialCTS_Object = MibTableColumn
hhmsSensorArraySerialCTS = _HhmsSensorArraySerialCTS_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 19, 1, 11),
    _HhmsSensorArraySerialCTS_Type()
)
hhmsSensorArraySerialCTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArraySerialCTS.setStatus("mandatory")


class _HhmsSensorArraySerialRTS_Type(Integer32):
    """Custom type hhmsSensorArraySerialRTS based on Integer32"""
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


_HhmsSensorArraySerialRTS_Type.__name__ = "Integer32"
_HhmsSensorArraySerialRTS_Object = MibTableColumn
hhmsSensorArraySerialRTS = _HhmsSensorArraySerialRTS_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 19, 1, 12),
    _HhmsSensorArraySerialRTS_Type()
)
hhmsSensorArraySerialRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArraySerialRTS.setStatus("mandatory")
_HhmsSensorArraySerialConfig_Type = DisplayString
_HhmsSensorArraySerialConfig_Object = MibTableColumn
hhmsSensorArraySerialConfig = _HhmsSensorArraySerialConfig_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 19, 1, 13),
    _HhmsSensorArraySerialConfig_Type()
)
hhmsSensorArraySerialConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArraySerialConfig.setStatus("mandatory")


class _HhmsSensorArraySerialIndex_Type(Integer32):
    """Custom type hhmsSensorArraySerialIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HhmsSensorArraySerialIndex_Type.__name__ = "Integer32"
_HhmsSensorArraySerialIndex_Object = MibTableColumn
hhmsSensorArraySerialIndex = _HhmsSensorArraySerialIndex_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 19, 1, 14),
    _HhmsSensorArraySerialIndex_Type()
)
hhmsSensorArraySerialIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArraySerialIndex.setStatus("mandatory")


class _HhmsSensorArrayDebug_Type(Integer32):
    """Custom type hhmsSensorArrayDebug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_HhmsSensorArrayDebug_Type.__name__ = "Integer32"
_HhmsSensorArrayDebug_Object = MibScalar
hhmsSensorArrayDebug = _HhmsSensorArrayDebug_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 20),
    _HhmsSensorArrayDebug_Type()
)
hhmsSensorArrayDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayDebug.setStatus("mandatory")
_HhmsSensorArrayDebugIP_Type = DisplayString
_HhmsSensorArrayDebugIP_Object = MibScalar
hhmsSensorArrayDebugIP = _HhmsSensorArrayDebugIP_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 21),
    _HhmsSensorArrayDebugIP_Type()
)
hhmsSensorArrayDebugIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayDebugIP.setStatus("mandatory")


class _HhmsSensorArrayTrapResend_Type(Integer32):
    """Custom type hhmsSensorArrayTrapResend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_HhmsSensorArrayTrapResend_Type.__name__ = "Integer32"
_HhmsSensorArrayTrapResend_Object = MibScalar
hhmsSensorArrayTrapResend = _HhmsSensorArrayTrapResend_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 22),
    _HhmsSensorArrayTrapResend_Type()
)
hhmsSensorArrayTrapResend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayTrapResend.setStatus("mandatory")
_HhmsSensorArrayTrapResendInterval_Type = Integer32
_HhmsSensorArrayTrapResendInterval_Object = MibScalar
hhmsSensorArrayTrapResendInterval = _HhmsSensorArrayTrapResendInterval_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 23),
    _HhmsSensorArrayTrapResendInterval_Type()
)
hhmsSensorArrayTrapResendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayTrapResendInterval.setStatus("mandatory")


class _HhmsSensorArraySendTraps_Type(Integer32):
    """Custom type hhmsSensorArraySendTraps based on Integer32"""
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


_HhmsSensorArraySendTraps_Type.__name__ = "Integer32"
_HhmsSensorArraySendTraps_Object = MibScalar
hhmsSensorArraySendTraps = _HhmsSensorArraySendTraps_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 24),
    _HhmsSensorArraySendTraps_Type()
)
hhmsSensorArraySendTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArraySendTraps.setStatus("mandatory")
_HhmsSensorArrayTrapDestination_Type = IpAddress
_HhmsSensorArrayTrapDestination_Object = MibScalar
hhmsSensorArrayTrapDestination = _HhmsSensorArrayTrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 25),
    _HhmsSensorArrayTrapDestination_Type()
)
hhmsSensorArrayTrapDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayTrapDestination.setStatus("mandatory")
_HhmsSensorArrayTrapCommunity_Type = DisplayString
_HhmsSensorArrayTrapCommunity_Object = MibScalar
hhmsSensorArrayTrapCommunity = _HhmsSensorArrayTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 26),
    _HhmsSensorArrayTrapCommunity_Type()
)
hhmsSensorArrayTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayTrapCommunity.setStatus("mandatory")
_HhmsSensorArrayTrapDefaultGateway_Type = IpAddress
_HhmsSensorArrayTrapDefaultGateway_Object = MibScalar
hhmsSensorArrayTrapDefaultGateway = _HhmsSensorArrayTrapDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 27),
    _HhmsSensorArrayTrapDefaultGateway_Type()
)
hhmsSensorArrayTrapDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayTrapDefaultGateway.setStatus("mandatory")


class _HhmsSensorArrayTrapUseDefaultGateway_Type(Integer32):
    """Custom type hhmsSensorArrayTrapUseDefaultGateway based on Integer32"""
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


_HhmsSensorArrayTrapUseDefaultGateway_Type.__name__ = "Integer32"
_HhmsSensorArrayTrapUseDefaultGateway_Object = MibScalar
hhmsSensorArrayTrapUseDefaultGateway = _HhmsSensorArrayTrapUseDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 28),
    _HhmsSensorArrayTrapUseDefaultGateway_Type()
)
hhmsSensorArrayTrapUseDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayTrapUseDefaultGateway.setStatus("mandatory")
_HhmsSensorArrayTrapDestinationMac_Type = DisplayString
_HhmsSensorArrayTrapDestinationMac_Object = MibScalar
hhmsSensorArrayTrapDestinationMac = _HhmsSensorArrayTrapDestinationMac_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 29),
    _HhmsSensorArrayTrapDestinationMac_Type()
)
hhmsSensorArrayTrapDestinationMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayTrapDestinationMac.setStatus("mandatory")


class _HhmsSensorArraySendMail_Type(Integer32):
    """Custom type hhmsSensorArraySendMail based on Integer32"""
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


_HhmsSensorArraySendMail_Type.__name__ = "Integer32"
_HhmsSensorArraySendMail_Object = MibScalar
hhmsSensorArraySendMail = _HhmsSensorArraySendMail_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 30),
    _HhmsSensorArraySendMail_Type()
)
hhmsSensorArraySendMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArraySendMail.setStatus("mandatory")
_HhmsSensorArrayMailRecpt_Type = DisplayString
_HhmsSensorArrayMailRecpt_Object = MibScalar
hhmsSensorArrayMailRecpt = _HhmsSensorArrayMailRecpt_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 31),
    _HhmsSensorArrayMailRecpt_Type()
)
hhmsSensorArrayMailRecpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayMailRecpt.setStatus("mandatory")
_HhmsSensorArrayMailFrom_Type = DisplayString
_HhmsSensorArrayMailFrom_Object = MibScalar
hhmsSensorArrayMailFrom = _HhmsSensorArrayMailFrom_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 32),
    _HhmsSensorArrayMailFrom_Type()
)
hhmsSensorArrayMailFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayMailFrom.setStatus("mandatory")
_HhmsSensorArrayMailSmpt_Type = IpAddress
_HhmsSensorArrayMailSmpt_Object = MibScalar
hhmsSensorArrayMailSmpt = _HhmsSensorArrayMailSmpt_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 33),
    _HhmsSensorArrayMailSmpt_Type()
)
hhmsSensorArrayMailSmpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayMailSmpt.setStatus("mandatory")
_HhmsSensorArrayMailGateway_Type = IpAddress
_HhmsSensorArrayMailGateway_Object = MibScalar
hhmsSensorArrayMailGateway = _HhmsSensorArrayMailGateway_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 34),
    _HhmsSensorArrayMailGateway_Type()
)
hhmsSensorArrayMailGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayMailGateway.setStatus("mandatory")


class _HhmsSensorArrayMailUseGateway_Type(Integer32):
    """Custom type hhmsSensorArrayMailUseGateway based on Integer32"""
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


_HhmsSensorArrayMailUseGateway_Type.__name__ = "Integer32"
_HhmsSensorArrayMailUseGateway_Object = MibScalar
hhmsSensorArrayMailUseGateway = _HhmsSensorArrayMailUseGateway_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 35),
    _HhmsSensorArrayMailUseGateway_Type()
)
hhmsSensorArrayMailUseGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayMailUseGateway.setStatus("mandatory")
_HhmsSensorArrayMailResendInterval_Type = Integer32
_HhmsSensorArrayMailResendInterval_Object = MibScalar
hhmsSensorArrayMailResendInterval = _HhmsSensorArrayMailResendInterval_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 36),
    _HhmsSensorArrayMailResendInterval_Type()
)
hhmsSensorArrayMailResendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayMailResendInterval.setStatus("mandatory")
_HhmsSensorArrayMailMaxResend_Type = Integer32
_HhmsSensorArrayMailMaxResend_Object = MibScalar
hhmsSensorArrayMailMaxResend = _HhmsSensorArrayMailMaxResend_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 37),
    _HhmsSensorArrayMailMaxResend_Type()
)
hhmsSensorArrayMailMaxResend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayMailMaxResend.setStatus("mandatory")
_HhmsSensorArrayMailDestinationMac_Type = DisplayString
_HhmsSensorArrayMailDestinationMac_Object = MibScalar
hhmsSensorArrayMailDestinationMac = _HhmsSensorArrayMailDestinationMac_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 38),
    _HhmsSensorArrayMailDestinationMac_Type()
)
hhmsSensorArrayMailDestinationMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayMailDestinationMac.setStatus("mandatory")
_HhmsSensorArrayMailLastStatus_Type = DisplayString
_HhmsSensorArrayMailLastStatus_Object = MibScalar
hhmsSensorArrayMailLastStatus = _HhmsSensorArrayMailLastStatus_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 39),
    _HhmsSensorArrayMailLastStatus_Type()
)
hhmsSensorArrayMailLastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayMailLastStatus.setStatus("mandatory")
_HhmsSensorArrayPowerControlTable_Object = MibTable
hhmsSensorArrayPowerControlTable = _HhmsSensorArrayPowerControlTable_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 40)
)
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerControlTable.setStatus("mandatory")
_HhmsSensorArrayPowerControlEntry_Object = MibTableRow
hhmsSensorArrayPowerControlEntry = _HhmsSensorArrayPowerControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 40, 1)
)
hhmsSensorArrayPowerControlEntry.setIndexNames(
    (0, "HHMSAGENT-MIB", "hhmsSensorArrayPowerControlIndex"),
)
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerControlEntry.setStatus("mandatory")
_HhmsSensorArrayPowerModuleDescription_Type = DisplayString
_HhmsSensorArrayPowerModuleDescription_Object = MibTableColumn
hhmsSensorArrayPowerModuleDescription = _HhmsSensorArrayPowerModuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 40, 1, 1),
    _HhmsSensorArrayPowerModuleDescription_Type()
)
hhmsSensorArrayPowerModuleDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerModuleDescription.setStatus("mandatory")


class _HhmsSensorArrayPowerModuleStatus_Type(Integer32):
    """Custom type hhmsSensorArrayPowerModuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              7)
        )
    )
    namedValues = NamedValues(
        *(("noStatus", 1),
          ("normal", 2),
          ("sensorError", 7))
    )


_HhmsSensorArrayPowerModuleStatus_Type.__name__ = "Integer32"
_HhmsSensorArrayPowerModuleStatus_Object = MibTableColumn
hhmsSensorArrayPowerModuleStatus = _HhmsSensorArrayPowerModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 40, 1, 2),
    _HhmsSensorArrayPowerModuleStatus_Type()
)
hhmsSensorArrayPowerModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerModuleStatus.setStatus("mandatory")


class _HhmsSensorArrayPowerModuleOnline_Type(Integer32):
    """Custom type hhmsSensorArrayPowerModuleOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_HhmsSensorArrayPowerModuleOnline_Type.__name__ = "Integer32"
_HhmsSensorArrayPowerModuleOnline_Object = MibTableColumn
hhmsSensorArrayPowerModuleOnline = _HhmsSensorArrayPowerModuleOnline_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 40, 1, 3),
    _HhmsSensorArrayPowerModuleOnline_Type()
)
hhmsSensorArrayPowerModuleOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerModuleOnline.setStatus("mandatory")


class _HhmsSensorArrayPowerModuleGoOnline_Type(Integer32):
    """Custom type hhmsSensorArrayPowerModuleGoOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("goOffline", 2),
          ("goOnline", 1))
    )


_HhmsSensorArrayPowerModuleGoOnline_Type.__name__ = "Integer32"
_HhmsSensorArrayPowerModuleGoOnline_Object = MibTableColumn
hhmsSensorArrayPowerModuleGoOnline = _HhmsSensorArrayPowerModuleGoOnline_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 40, 1, 4),
    _HhmsSensorArrayPowerModuleGoOnline_Type()
)
hhmsSensorArrayPowerModuleGoOnline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerModuleGoOnline.setStatus("mandatory")
_HhmsSensorArrayPowerOutletDescription_Type = DisplayString
_HhmsSensorArrayPowerOutletDescription_Object = MibTableColumn
hhmsSensorArrayPowerOutletDescription = _HhmsSensorArrayPowerOutletDescription_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 40, 1, 5),
    _HhmsSensorArrayPowerOutletDescription_Type()
)
hhmsSensorArrayPowerOutletDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerOutletDescription.setStatus("mandatory")


class _HhmsSensorArrayPowerOutletStatus_Type(Integer32):
    """Custom type hhmsSensorArrayPowerOutletStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("noStatus", 1),
          ("off", 3),
          ("on", 2),
          ("sensorError", 7))
    )


_HhmsSensorArrayPowerOutletStatus_Type.__name__ = "Integer32"
_HhmsSensorArrayPowerOutletStatus_Object = MibTableColumn
hhmsSensorArrayPowerOutletStatus = _HhmsSensorArrayPowerOutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 40, 1, 6),
    _HhmsSensorArrayPowerOutletStatus_Type()
)
hhmsSensorArrayPowerOutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerOutletStatus.setStatus("mandatory")


class _HhmsSensorArrayPowerOutletSet_Type(Integer32):
    """Custom type hhmsSensorArrayPowerOutletSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("noStatus", 1),
          ("off", 3),
          ("on", 2),
          ("reboot", 4),
          ("sensorError", 7))
    )


_HhmsSensorArrayPowerOutletSet_Type.__name__ = "Integer32"
_HhmsSensorArrayPowerOutletSet_Object = MibTableColumn
hhmsSensorArrayPowerOutletSet = _HhmsSensorArrayPowerOutletSet_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 40, 1, 7),
    _HhmsSensorArrayPowerOutletSet_Type()
)
hhmsSensorArrayPowerOutletSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerOutletSet.setStatus("mandatory")


class _HhmsSensorArrayPowerControlIndex_Type(Integer32):
    """Custom type hhmsSensorArrayPowerControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HhmsSensorArrayPowerControlIndex_Type.__name__ = "Integer32"
_HhmsSensorArrayPowerControlIndex_Object = MibTableColumn
hhmsSensorArrayPowerControlIndex = _HhmsSensorArrayPowerControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 40, 1, 8),
    _HhmsSensorArrayPowerControlIndex_Type()
)
hhmsSensorArrayPowerControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerControlIndex.setStatus("mandatory")
_HhmsSensorArrayPowerMonitorTable_Object = MibTable
hhmsSensorArrayPowerMonitorTable = _HhmsSensorArrayPowerMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 41)
)
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerMonitorTable.setStatus("mandatory")
_HhmsSensorArrayPowerMonitorEntry_Object = MibTableRow
hhmsSensorArrayPowerMonitorEntry = _HhmsSensorArrayPowerMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 41, 1)
)
hhmsSensorArrayPowerMonitorEntry.setIndexNames(
    (0, "HHMSAGENT-MIB", "hhmsSensorArrayPowerMonitorIndex"),
)
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerMonitorEntry.setStatus("mandatory")
_HhmsSensorArrayPowerMonitorDescription_Type = DisplayString
_HhmsSensorArrayPowerMonitorDescription_Object = MibTableColumn
hhmsSensorArrayPowerMonitorDescription = _HhmsSensorArrayPowerMonitorDescription_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 41, 1, 1),
    _HhmsSensorArrayPowerMonitorDescription_Type()
)
hhmsSensorArrayPowerMonitorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerMonitorDescription.setStatus("mandatory")
_HhmsSensorArrayPowerMonitorCurrent_Type = Integer32
_HhmsSensorArrayPowerMonitorCurrent_Object = MibTableColumn
hhmsSensorArrayPowerMonitorCurrent = _HhmsSensorArrayPowerMonitorCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 41, 1, 2),
    _HhmsSensorArrayPowerMonitorCurrent_Type()
)
hhmsSensorArrayPowerMonitorCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerMonitorCurrent.setStatus("mandatory")
_HhmsSensorArrayPowerMonitorVoltage_Type = Integer32
_HhmsSensorArrayPowerMonitorVoltage_Object = MibTableColumn
hhmsSensorArrayPowerMonitorVoltage = _HhmsSensorArrayPowerMonitorVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 41, 1, 3),
    _HhmsSensorArrayPowerMonitorVoltage_Type()
)
hhmsSensorArrayPowerMonitorVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerMonitorVoltage.setStatus("mandatory")
_HhmsSensorArrayPowerMonitorPower_Type = DisplayString
_HhmsSensorArrayPowerMonitorPower_Object = MibTableColumn
hhmsSensorArrayPowerMonitorPower = _HhmsSensorArrayPowerMonitorPower_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 41, 1, 4),
    _HhmsSensorArrayPowerMonitorPower_Type()
)
hhmsSensorArrayPowerMonitorPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerMonitorPower.setStatus("mandatory")


class _HhmsSensorArrayPowerMonitorStatus_Type(Integer32):
    """Custom type hhmsSensorArrayPowerMonitorStatus based on Integer32"""
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
        *(("highCritical", 4),
          ("highWarning", 3),
          ("lowCritical", 6),
          ("lowWarning", 5),
          ("noStatus", 1),
          ("normal", 2),
          ("sensorError", 7))
    )


_HhmsSensorArrayPowerMonitorStatus_Type.__name__ = "Integer32"
_HhmsSensorArrayPowerMonitorStatus_Object = MibTableColumn
hhmsSensorArrayPowerMonitorStatus = _HhmsSensorArrayPowerMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 41, 1, 5),
    _HhmsSensorArrayPowerMonitorStatus_Type()
)
hhmsSensorArrayPowerMonitorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerMonitorStatus.setStatus("mandatory")


class _HhmsSensorArrayPowerMonitorOnline_Type(Integer32):
    """Custom type hhmsSensorArrayPowerMonitorOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_HhmsSensorArrayPowerMonitorOnline_Type.__name__ = "Integer32"
_HhmsSensorArrayPowerMonitorOnline_Object = MibTableColumn
hhmsSensorArrayPowerMonitorOnline = _HhmsSensorArrayPowerMonitorOnline_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 41, 1, 6),
    _HhmsSensorArrayPowerMonitorOnline_Type()
)
hhmsSensorArrayPowerMonitorOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerMonitorOnline.setStatus("mandatory")


class _HhmsSensorArrayPowerMonitorGoOnline_Type(Integer32):
    """Custom type hhmsSensorArrayPowerMonitorGoOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("goOffline", 2),
          ("goOnline", 1))
    )


_HhmsSensorArrayPowerMonitorGoOnline_Type.__name__ = "Integer32"
_HhmsSensorArrayPowerMonitorGoOnline_Object = MibTableColumn
hhmsSensorArrayPowerMonitorGoOnline = _HhmsSensorArrayPowerMonitorGoOnline_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 41, 1, 7),
    _HhmsSensorArrayPowerMonitorGoOnline_Type()
)
hhmsSensorArrayPowerMonitorGoOnline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerMonitorGoOnline.setStatus("mandatory")
_HhmsSensorArrayPowerMonitorHighWarning_Type = Integer32
_HhmsSensorArrayPowerMonitorHighWarning_Object = MibTableColumn
hhmsSensorArrayPowerMonitorHighWarning = _HhmsSensorArrayPowerMonitorHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 41, 1, 8),
    _HhmsSensorArrayPowerMonitorHighWarning_Type()
)
hhmsSensorArrayPowerMonitorHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerMonitorHighWarning.setStatus("mandatory")
_HhmsSensorArrayPowerMonitorHighCritical_Type = Integer32
_HhmsSensorArrayPowerMonitorHighCritical_Object = MibTableColumn
hhmsSensorArrayPowerMonitorHighCritical = _HhmsSensorArrayPowerMonitorHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 41, 1, 9),
    _HhmsSensorArrayPowerMonitorHighCritical_Type()
)
hhmsSensorArrayPowerMonitorHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerMonitorHighCritical.setStatus("mandatory")
_HhmsSensorArrayPowerMonitorLowWarning_Type = Integer32
_HhmsSensorArrayPowerMonitorLowWarning_Object = MibTableColumn
hhmsSensorArrayPowerMonitorLowWarning = _HhmsSensorArrayPowerMonitorLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 41, 1, 10),
    _HhmsSensorArrayPowerMonitorLowWarning_Type()
)
hhmsSensorArrayPowerMonitorLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerMonitorLowWarning.setStatus("mandatory")
_HhmsSensorArrayPowerMonitorLowCritical_Type = Integer32
_HhmsSensorArrayPowerMonitorLowCritical_Object = MibTableColumn
hhmsSensorArrayPowerMonitorLowCritical = _HhmsSensorArrayPowerMonitorLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 41, 1, 11),
    _HhmsSensorArrayPowerMonitorLowCritical_Type()
)
hhmsSensorArrayPowerMonitorLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerMonitorLowCritical.setStatus("mandatory")
_HhmsSensorArrayPowerMonitorRearm_Type = Integer32
_HhmsSensorArrayPowerMonitorRearm_Object = MibTableColumn
hhmsSensorArrayPowerMonitorRearm = _HhmsSensorArrayPowerMonitorRearm_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 41, 1, 12),
    _HhmsSensorArrayPowerMonitorRearm_Type()
)
hhmsSensorArrayPowerMonitorRearm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerMonitorRearm.setStatus("mandatory")


class _HhmsSensorArrayPowerMonitorIndex_Type(Integer32):
    """Custom type hhmsSensorArrayPowerMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_HhmsSensorArrayPowerMonitorIndex_Type.__name__ = "Integer32"
_HhmsSensorArrayPowerMonitorIndex_Object = MibTableColumn
hhmsSensorArrayPowerMonitorIndex = _HhmsSensorArrayPowerMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 41, 1, 13),
    _HhmsSensorArrayPowerMonitorIndex_Type()
)
hhmsSensorArrayPowerMonitorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayPowerMonitorIndex.setStatus("mandatory")
_HhmsSensorArrayHighDriveTable_Object = MibTable
hhmsSensorArrayHighDriveTable = _HhmsSensorArrayHighDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 42)
)
if mibBuilder.loadTexts:
    hhmsSensorArrayHighDriveTable.setStatus("mandatory")
_HhmsSensorArrayHighDriveEntry_Object = MibTableRow
hhmsSensorArrayHighDriveEntry = _HhmsSensorArrayHighDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 42, 1)
)
hhmsSensorArrayHighDriveEntry.setIndexNames(
    (0, "HHMSAGENT-MIB", "hhmsSensorArrayHighDriveIndex"),
)
if mibBuilder.loadTexts:
    hhmsSensorArrayHighDriveEntry.setStatus("mandatory")
_HhmsSensorArrayHighDriveDescription_Type = DisplayString
_HhmsSensorArrayHighDriveDescription_Object = MibTableColumn
hhmsSensorArrayHighDriveDescription = _HhmsSensorArrayHighDriveDescription_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 42, 1, 1),
    _HhmsSensorArrayHighDriveDescription_Type()
)
hhmsSensorArrayHighDriveDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayHighDriveDescription.setStatus("mandatory")


class _HhmsSensorArrayHighDriveOutputLevel_Type(Integer32):
    """Custom type hhmsSensorArrayHighDriveOutputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 0),
          ("open", 1))
    )


_HhmsSensorArrayHighDriveOutputLevel_Type.__name__ = "Integer32"
_HhmsSensorArrayHighDriveOutputLevel_Object = MibTableColumn
hhmsSensorArrayHighDriveOutputLevel = _HhmsSensorArrayHighDriveOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 42, 1, 2),
    _HhmsSensorArrayHighDriveOutputLevel_Type()
)
hhmsSensorArrayHighDriveOutputLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayHighDriveOutputLevel.setStatus("mandatory")


class _HhmsSensorArrayHighDriveIndex_Type(Integer32):
    """Custom type hhmsSensorArrayHighDriveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_HhmsSensorArrayHighDriveIndex_Type.__name__ = "Integer32"
_HhmsSensorArrayHighDriveIndex_Object = MibTableColumn
hhmsSensorArrayHighDriveIndex = _HhmsSensorArrayHighDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 42, 1, 3),
    _HhmsSensorArrayHighDriveIndex_Type()
)
hhmsSensorArrayHighDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayHighDriveIndex.setStatus("mandatory")
_HhmsSensorArrayCameraTable_Object = MibTable
hhmsSensorArrayCameraTable = _HhmsSensorArrayCameraTable_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 43)
)
if mibBuilder.loadTexts:
    hhmsSensorArrayCameraTable.setStatus("mandatory")
_HhmsSensorArrayCameraEntry_Object = MibTableRow
hhmsSensorArrayCameraEntry = _HhmsSensorArrayCameraEntry_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 43, 1)
)
hhmsSensorArrayCameraEntry.setIndexNames(
    (0, "HHMSAGENT-MIB", "hhmsSensorArrayCameraIndex"),
)
if mibBuilder.loadTexts:
    hhmsSensorArrayCameraEntry.setStatus("mandatory")
_HhmsSensorArrayCameraDescription_Type = DisplayString
_HhmsSensorArrayCameraDescription_Object = MibTableColumn
hhmsSensorArrayCameraDescription = _HhmsSensorArrayCameraDescription_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 43, 1, 1),
    _HhmsSensorArrayCameraDescription_Type()
)
hhmsSensorArrayCameraDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayCameraDescription.setStatus("mandatory")


class _HhmsSensorArrayCameraOnline_Type(Integer32):
    """Custom type hhmsSensorArrayCameraOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_HhmsSensorArrayCameraOnline_Type.__name__ = "Integer32"
_HhmsSensorArrayCameraOnline_Object = MibTableColumn
hhmsSensorArrayCameraOnline = _HhmsSensorArrayCameraOnline_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 43, 1, 2),
    _HhmsSensorArrayCameraOnline_Type()
)
hhmsSensorArrayCameraOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayCameraOnline.setStatus("mandatory")


class _HhmsSensorArrayCameraGoOnline_Type(Integer32):
    """Custom type hhmsSensorArrayCameraGoOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("goOffline", 2),
          ("goOnline", 1))
    )


_HhmsSensorArrayCameraGoOnline_Type.__name__ = "Integer32"
_HhmsSensorArrayCameraGoOnline_Object = MibTableColumn
hhmsSensorArrayCameraGoOnline = _HhmsSensorArrayCameraGoOnline_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 43, 1, 3),
    _HhmsSensorArrayCameraGoOnline_Type()
)
hhmsSensorArrayCameraGoOnline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayCameraGoOnline.setStatus("mandatory")
_HhmsSensorArrayCameraUrlMain_Type = DisplayString
_HhmsSensorArrayCameraUrlMain_Object = MibTableColumn
hhmsSensorArrayCameraUrlMain = _HhmsSensorArrayCameraUrlMain_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 43, 1, 4),
    _HhmsSensorArrayCameraUrlMain_Type()
)
hhmsSensorArrayCameraUrlMain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayCameraUrlMain.setStatus("mandatory")
_HhmsSensorArrayCameraUrlExtension_Type = DisplayString
_HhmsSensorArrayCameraUrlExtension_Object = MibTableColumn
hhmsSensorArrayCameraUrlExtension = _HhmsSensorArrayCameraUrlExtension_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 43, 1, 5),
    _HhmsSensorArrayCameraUrlExtension_Type()
)
hhmsSensorArrayCameraUrlExtension.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayCameraUrlExtension.setStatus("mandatory")
_HhmsSensorArrayCameraRefreshRate_Type = Integer32
_HhmsSensorArrayCameraRefreshRate_Object = MibTableColumn
hhmsSensorArrayCameraRefreshRate = _HhmsSensorArrayCameraRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 43, 1, 6),
    _HhmsSensorArrayCameraRefreshRate_Type()
)
hhmsSensorArrayCameraRefreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayCameraRefreshRate.setStatus("mandatory")


class _HhmsSensorArrayCameraIndex_Type(Integer32):
    """Custom type hhmsSensorArrayCameraIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_HhmsSensorArrayCameraIndex_Type.__name__ = "Integer32"
_HhmsSensorArrayCameraIndex_Object = MibTableColumn
hhmsSensorArrayCameraIndex = _HhmsSensorArrayCameraIndex_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 43, 1, 7),
    _HhmsSensorArrayCameraIndex_Type()
)
hhmsSensorArrayCameraIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayCameraIndex.setStatus("mandatory")
_HhmsSensorArrayTrapMailPollInterval_Type = Integer32
_HhmsSensorArrayTrapMailPollInterval_Object = MibScalar
hhmsSensorArrayTrapMailPollInterval = _HhmsSensorArrayTrapMailPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 50),
    _HhmsSensorArrayTrapMailPollInterval_Type()
)
hhmsSensorArrayTrapMailPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayTrapMailPollInterval.setStatus("mandatory")
_HhmsSensorArraySendTestMail_Type = Integer32
_HhmsSensorArraySendTestMail_Object = MibScalar
hhmsSensorArraySendTestMail = _HhmsSensorArraySendTestMail_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 51),
    _HhmsSensorArraySendTestMail_Type()
)
hhmsSensorArraySendTestMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArraySendTestMail.setStatus("mandatory")
_HhmsSensorArrayLastSystemError_Type = DisplayString
_HhmsSensorArrayLastSystemError_Object = MibScalar
hhmsSensorArrayLastSystemError = _HhmsSensorArrayLastSystemError_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 52),
    _HhmsSensorArrayLastSystemError_Type()
)
hhmsSensorArrayLastSystemError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorArrayLastSystemError.setStatus("mandatory")
_HhmsSensorArrayDataCollectionPeriod_Type = Integer32
_HhmsSensorArrayDataCollectionPeriod_Object = MibScalar
hhmsSensorArrayDataCollectionPeriod = _HhmsSensorArrayDataCollectionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 53),
    _HhmsSensorArrayDataCollectionPeriod_Type()
)
hhmsSensorArrayDataCollectionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayDataCollectionPeriod.setStatus("mandatory")
_HhmsSensorArrayMailTimeout_Type = Integer32
_HhmsSensorArrayMailTimeout_Object = MibScalar
hhmsSensorArrayMailTimeout = _HhmsSensorArrayMailTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 2, 2, 1, 54),
    _HhmsSensorArrayMailTimeout_Type()
)
hhmsSensorArrayMailTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hhmsSensorArrayMailTimeout.setStatus("mandatory")
_HhmsAgentConfig_ObjectIdentity = ObjectIdentity
hhmsAgentConfig = _HhmsAgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3854, 1, 5)
)
_HhmsAgentVersion_Type = DisplayString
_HhmsAgentVersion_Object = MibScalar
hhmsAgentVersion = _HhmsAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 5, 1),
    _HhmsAgentVersion_Type()
)
hhmsAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsAgentVersion.setStatus("mandatory")
_HhmsCompressedSummaryTable_Object = MibTable
hhmsCompressedSummaryTable = _HhmsCompressedSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 5, 7)
)
if mibBuilder.loadTexts:
    hhmsCompressedSummaryTable.setStatus("mandatory")
_HhmsCompressedSummaryEntry_Object = MibTableRow
hhmsCompressedSummaryEntry = _HhmsCompressedSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 5, 7, 1)
)
hhmsCompressedSummaryEntry.setIndexNames(
    (0, "HHMSAGENT-MIB", "hhmsCompressedSummaryIndex"),
)
if mibBuilder.loadTexts:
    hhmsCompressedSummaryEntry.setStatus("mandatory")
_HhmsCompressedSummaryGet_Type = DisplayString
_HhmsCompressedSummaryGet_Object = MibTableColumn
hhmsCompressedSummaryGet = _HhmsCompressedSummaryGet_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 5, 7, 1, 1),
    _HhmsCompressedSummaryGet_Type()
)
hhmsCompressedSummaryGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsCompressedSummaryGet.setStatus("mandatory")


class _HhmsCompressedSummaryIndex_Type(Integer32):
    """Custom type hhmsCompressedSummaryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HhmsCompressedSummaryIndex_Type.__name__ = "Integer32"
_HhmsCompressedSummaryIndex_Object = MibTableColumn
hhmsCompressedSummaryIndex = _HhmsCompressedSummaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 5, 7, 1, 2),
    _HhmsCompressedSummaryIndex_Type()
)
hhmsCompressedSummaryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsCompressedSummaryIndex.setStatus("mandatory")
_HhmsAgentTraps_ObjectIdentity = ObjectIdentity
hhmsAgentTraps = _HhmsAgentTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3854, 1, 7)
)


class _HhmsSensorStatus_Type(Integer32):
    """Custom type hhmsSensorStatus based on Integer32"""
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
        *(("highCritical", 4),
          ("highWarning", 3),
          ("lowCritical", 6),
          ("lowWarning", 5),
          ("noStatus", 1),
          ("normal", 2),
          ("sensorError", 7))
    )


_HhmsSensorStatus_Type.__name__ = "Integer32"
_HhmsSensorStatus_Object = MibScalar
hhmsSensorStatus = _HhmsSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 7, 1),
    _HhmsSensorStatus_Type()
)
hhmsSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorStatus.setStatus("mandatory")
_HhmsSensorValue_Type = Integer32
_HhmsSensorValue_Object = MibScalar
hhmsSensorValue = _HhmsSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 7, 2),
    _HhmsSensorValue_Type()
)
hhmsSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorValue.setStatus("mandatory")
_HhmsSensorLevelExceeded_Type = Integer32
_HhmsSensorLevelExceeded_Object = MibScalar
hhmsSensorLevelExceeded = _HhmsSensorLevelExceeded_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 7, 3),
    _HhmsSensorLevelExceeded_Type()
)
hhmsSensorLevelExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorLevelExceeded.setStatus("mandatory")
_HhmsSensorIndex_Type = Integer32
_HhmsSensorIndex_Object = MibScalar
hhmsSensorIndex = _HhmsSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 7, 4),
    _HhmsSensorIndex_Type()
)
hhmsSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorIndex.setStatus("mandatory")
_HhmsSensorName_Type = DisplayString
_HhmsSensorName_Object = MibScalar
hhmsSensorName = _HhmsSensorName_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 7, 5),
    _HhmsSensorName_Type()
)
hhmsSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorName.setStatus("mandatory")
_HhmsSensorDescription_Type = DisplayString
_HhmsSensorDescription_Object = MibScalar
hhmsSensorDescription = _HhmsSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 3854, 1, 7, 6),
    _HhmsSensorDescription_Type()
)
hhmsSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhmsSensorDescription.setStatus("mandatory")

# Managed Objects groups


# Notification objects

hhmsUnknownStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3854, 1, 0, 0)
)
if mibBuilder.loadTexts:
    hhmsUnknownStatus.setStatus(
        ""
    )

hhmsNormalStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3854, 1, 0, 1)
)
if mibBuilder.loadTexts:
    hhmsNormalStatus.setStatus(
        ""
    )

hhmsWarningStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3854, 1, 0, 2)
)
if mibBuilder.loadTexts:
    hhmsWarningStatus.setStatus(
        ""
    )

hhmsCriticalStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3854, 1, 0, 3)
)
if mibBuilder.loadTexts:
    hhmsCriticalStatus.setStatus(
        ""
    )

hhmsDownStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3854, 1, 0, 4)
)
if mibBuilder.loadTexts:
    hhmsDownStatus.setStatus(
        ""
    )

hhmsTemperatureStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3854, 1, 0, 10)
)
hhmsTemperatureStatus.setObjects(
      *(("HHMSAGENT-MIB", "hhmsSensorStatus"),
        ("HHMSAGENT-MIB", "hhmsSensorValue"),
        ("HHMSAGENT-MIB", "hhmsSensorLevelExceeded"),
        ("HHMSAGENT-MIB", "hhmsSensorIndex"),
        ("HHMSAGENT-MIB", "hhmsSensorName"),
        ("HHMSAGENT-MIB", "hhmsSensorDescription"))
)
if mibBuilder.loadTexts:
    hhmsTemperatureStatus.setStatus(
        ""
    )

hhmsHumidityStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3854, 1, 0, 20)
)
hhmsHumidityStatus.setObjects(
      *(("HHMSAGENT-MIB", "hhmsSensorStatus"),
        ("HHMSAGENT-MIB", "hhmsSensorValue"),
        ("HHMSAGENT-MIB", "hhmsSensorLevelExceeded"),
        ("HHMSAGENT-MIB", "hhmsSensorIndex"),
        ("HHMSAGENT-MIB", "hhmsSensorName"),
        ("HHMSAGENT-MIB", "hhmsSensorDescription"))
)
if mibBuilder.loadTexts:
    hhmsHumidityStatus.setStatus(
        ""
    )

hhmsSwitchStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3854, 1, 0, 30)
)
hhmsSwitchStatus.setObjects(
      *(("HHMSAGENT-MIB", "hhmsSensorStatus"),
        ("HHMSAGENT-MIB", "hhmsSensorValue"),
        ("HHMSAGENT-MIB", "hhmsSensorLevelExceeded"),
        ("HHMSAGENT-MIB", "hhmsSensorIndex"),
        ("HHMSAGENT-MIB", "hhmsSensorName"),
        ("HHMSAGENT-MIB", "hhmsSensorDescription"))
)
if mibBuilder.loadTexts:
    hhmsSwitchStatus.setStatus(
        ""
    )

hhmsPowerMonitorStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3854, 1, 0, 40)
)
hhmsPowerMonitorStatus.setObjects(
      *(("HHMSAGENT-MIB", "hhmsSensorStatus"),
        ("HHMSAGENT-MIB", "hhmsSensorValue"),
        ("HHMSAGENT-MIB", "hhmsSensorLevelExceeded"),
        ("HHMSAGENT-MIB", "hhmsSensorIndex"),
        ("HHMSAGENT-MIB", "hhmsSensorName"),
        ("HHMSAGENT-MIB", "hhmsSensorDescription"))
)
if mibBuilder.loadTexts:
    hhmsPowerMonitorStatus.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HHMSAGENT-MIB",
    **{"akcp": akcp,
       "hhmsagent": hhmsagent,
       "hhmsUnknownStatus": hhmsUnknownStatus,
       "hhmsNormalStatus": hhmsNormalStatus,
       "hhmsWarningStatus": hhmsWarningStatus,
       "hhmsCriticalStatus": hhmsCriticalStatus,
       "hhmsDownStatus": hhmsDownStatus,
       "hhmsTemperatureStatus": hhmsTemperatureStatus,
       "hhmsHumidityStatus": hhmsHumidityStatus,
       "hhmsSwitchStatus": hhmsSwitchStatus,
       "hhmsPowerMonitorStatus": hhmsPowerMonitorStatus,
       "hhmsAgentSummary": hhmsAgentSummary,
       "hhmsAgentLocation": hhmsAgentLocation,
       "hhmsAgentStatus": hhmsAgentStatus,
       "hhmsNumberBadSensors": hhmsNumberBadSensors,
       "hhmsLocationBadSensor": hhmsLocationBadSensor,
       "hhmsAgentManufName": hhmsAgentManufName,
       "hhmsAgentHelpUrl": hhmsAgentHelpUrl,
       "hhmsAgentHtmlView": hhmsAgentHtmlView,
       "hhmsAgentHtmlStandardTitle": hhmsAgentHtmlStandardTitle,
       "hhmsAgentHtmlStandardButton": hhmsAgentHtmlStandardButton,
       "hhmsSensor": hhmsSensor,
       "hhmsSensorArrayTable": hhmsSensorArrayTable,
       "hhmsSensorArrayEntry": hhmsSensorArrayEntry,
       "hhmsSensorArrayHost": hhmsSensorArrayHost,
       "hhmsSensorArrayUseDHCP": hhmsSensorArrayUseDHCP,
       "hhmsSensorArrayMAC": hhmsSensorArrayMAC,
       "hhmsSensorArraySetCommunity": hhmsSensorArraySetCommunity,
       "hhmsSensorArrayGetCommunity": hhmsSensorArrayGetCommunity,
       "hhmsSensorArrayDescription": hhmsSensorArrayDescription,
       "hhmsSensorArrayLocation": hhmsSensorArrayLocation,
       "hhmsSensorArrayLastUpdate": hhmsSensorArrayLastUpdate,
       "hhmsSensorArrayStatus": hhmsSensorArrayStatus,
       "hhmsSensorArrayOnline": hhmsSensorArrayOnline,
       "hhmsSensorArrayGoOnline": hhmsSensorArrayGoOnline,
       "hhmsSensorArrayReadInterval": hhmsSensorArrayReadInterval,
       "hhmsSensorArrayReceiveTimeout": hhmsSensorArrayReceiveTimeout,
       "hhmsSensorArrayReceiveRetries": hhmsSensorArrayReceiveRetries,
       "hhmsSensorArrayVersion": hhmsSensorArrayVersion,
       "hhmsSensorArrayTempTable": hhmsSensorArrayTempTable,
       "hhmsSensorArrayTempEntry": hhmsSensorArrayTempEntry,
       "hhmsSensorArrayTempDescription": hhmsSensorArrayTempDescription,
       "hhmsSensorArrayTempLocation": hhmsSensorArrayTempLocation,
       "hhmsSensorArrayTempDegree": hhmsSensorArrayTempDegree,
       "hhmsSensorArrayTempStatus": hhmsSensorArrayTempStatus,
       "hhmsSensorArrayTempOnline": hhmsSensorArrayTempOnline,
       "hhmsSensorArrayTempGoOnline": hhmsSensorArrayTempGoOnline,
       "hhmsSensorArrayTempHighWarning": hhmsSensorArrayTempHighWarning,
       "hhmsSensorArrayTempHighCritical": hhmsSensorArrayTempHighCritical,
       "hhmsSensorArrayTempLowWarning": hhmsSensorArrayTempLowWarning,
       "hhmsSensorArrayTempLowCritical": hhmsSensorArrayTempLowCritical,
       "hhmsSensorArrayTempRearm": hhmsSensorArrayTempRearm,
       "hhmsSensorArrayTempDegreeType": hhmsSensorArrayTempDegreeType,
       "hhmsSensorArrayTempSensorType": hhmsSensorArrayTempSensorType,
       "hhmsSensorArrayTempTestStatus": hhmsSensorArrayTempTestStatus,
       "hhmsSensorArrayTempTestDegree": hhmsSensorArrayTempTestDegree,
       "hhmsSensorArrayTempIndex": hhmsSensorArrayTempIndex,
       "hhmsSensorArrayHumidityTable": hhmsSensorArrayHumidityTable,
       "hhmsSensorArrayHumidityEntry": hhmsSensorArrayHumidityEntry,
       "hhmsSensorArrayHumidityDescription": hhmsSensorArrayHumidityDescription,
       "hhmsSensorArrayHumidityLocation": hhmsSensorArrayHumidityLocation,
       "hhmsSensorArrayHumidityPercent": hhmsSensorArrayHumidityPercent,
       "hhmsSensorArrayHumidityStatus": hhmsSensorArrayHumidityStatus,
       "hhmsSensorArrayHumidityOnline": hhmsSensorArrayHumidityOnline,
       "hhmsSensorArrayHumidityGoOnline": hhmsSensorArrayHumidityGoOnline,
       "hhmsSensorArrayHumidityHighWarning": hhmsSensorArrayHumidityHighWarning,
       "hhmsSensorArrayHumidityHighCritical": hhmsSensorArrayHumidityHighCritical,
       "hhmsSensorArrayHumidityLowWarning": hhmsSensorArrayHumidityLowWarning,
       "hhmsSensorArrayHumidityLowCritical": hhmsSensorArrayHumidityLowCritical,
       "hhmsSensorArrayHumidityRearm": hhmsSensorArrayHumidityRearm,
       "hhmsSensorArrayHumidityTestStatus": hhmsSensorArrayHumidityTestStatus,
       "hhmsSensorArrayHumidityTestPercent": hhmsSensorArrayHumidityTestPercent,
       "hhmsSensorArrayHumidityIndex": hhmsSensorArrayHumidityIndex,
       "hhmsSensorArraySwitchTable": hhmsSensorArraySwitchTable,
       "hhmsSensorArraySwitchEntry": hhmsSensorArraySwitchEntry,
       "hhmsSensorArraySwitchDescription": hhmsSensorArraySwitchDescription,
       "hhmsSensorArraySwitchLocation": hhmsSensorArraySwitchLocation,
       "hhmsSensorArraySwitchStatus": hhmsSensorArraySwitchStatus,
       "hhmsSensorArraySwitchOnline": hhmsSensorArraySwitchOnline,
       "hhmsSensorArraySwitchGoOnline": hhmsSensorArraySwitchGoOnline,
       "hhmsSensorArraySwitchDirection": hhmsSensorArraySwitchDirection,
       "hhmsSensorArraySwitchNormalState": hhmsSensorArraySwitchNormalState,
       "hhmsSensorArraySwitchOutputLevel": hhmsSensorArraySwitchOutputLevel,
       "hhmsSensorArraySwitchTestState": hhmsSensorArraySwitchTestState,
       "hhmsSensorArraySwitchIndex": hhmsSensorArraySwitchIndex,
       "hhmsSensorArraySerialTable": hhmsSensorArraySerialTable,
       "hhmsSensorArraySerialEntry": hhmsSensorArraySerialEntry,
       "hhmsSensorArraySerialDescription": hhmsSensorArraySerialDescription,
       "hhmsSensorArraySerialLocation": hhmsSensorArraySerialLocation,
       "hhmsSensorArraySerialStatus": hhmsSensorArraySerialStatus,
       "hhmsSensorArraySerialOnline": hhmsSensorArraySerialOnline,
       "hhmsSensorArraySerialGoOnline": hhmsSensorArraySerialGoOnline,
       "hhmsSensorArraySerialData": hhmsSensorArraySerialData,
       "hhmsSensorArraySerialBaud": hhmsSensorArraySerialBaud,
       "hhmsSensorArraySerialDataBits": hhmsSensorArraySerialDataBits,
       "hhmsSensorArraySerialParity": hhmsSensorArraySerialParity,
       "hhmsSensorArraySerialStop": hhmsSensorArraySerialStop,
       "hhmsSensorArraySerialCTS": hhmsSensorArraySerialCTS,
       "hhmsSensorArraySerialRTS": hhmsSensorArraySerialRTS,
       "hhmsSensorArraySerialConfig": hhmsSensorArraySerialConfig,
       "hhmsSensorArraySerialIndex": hhmsSensorArraySerialIndex,
       "hhmsSensorArrayDebug": hhmsSensorArrayDebug,
       "hhmsSensorArrayDebugIP": hhmsSensorArrayDebugIP,
       "hhmsSensorArrayTrapResend": hhmsSensorArrayTrapResend,
       "hhmsSensorArrayTrapResendInterval": hhmsSensorArrayTrapResendInterval,
       "hhmsSensorArraySendTraps": hhmsSensorArraySendTraps,
       "hhmsSensorArrayTrapDestination": hhmsSensorArrayTrapDestination,
       "hhmsSensorArrayTrapCommunity": hhmsSensorArrayTrapCommunity,
       "hhmsSensorArrayTrapDefaultGateway": hhmsSensorArrayTrapDefaultGateway,
       "hhmsSensorArrayTrapUseDefaultGateway": hhmsSensorArrayTrapUseDefaultGateway,
       "hhmsSensorArrayTrapDestinationMac": hhmsSensorArrayTrapDestinationMac,
       "hhmsSensorArraySendMail": hhmsSensorArraySendMail,
       "hhmsSensorArrayMailRecpt": hhmsSensorArrayMailRecpt,
       "hhmsSensorArrayMailFrom": hhmsSensorArrayMailFrom,
       "hhmsSensorArrayMailSmpt": hhmsSensorArrayMailSmpt,
       "hhmsSensorArrayMailGateway": hhmsSensorArrayMailGateway,
       "hhmsSensorArrayMailUseGateway": hhmsSensorArrayMailUseGateway,
       "hhmsSensorArrayMailResendInterval": hhmsSensorArrayMailResendInterval,
       "hhmsSensorArrayMailMaxResend": hhmsSensorArrayMailMaxResend,
       "hhmsSensorArrayMailDestinationMac": hhmsSensorArrayMailDestinationMac,
       "hhmsSensorArrayMailLastStatus": hhmsSensorArrayMailLastStatus,
       "hhmsSensorArrayPowerControlTable": hhmsSensorArrayPowerControlTable,
       "hhmsSensorArrayPowerControlEntry": hhmsSensorArrayPowerControlEntry,
       "hhmsSensorArrayPowerModuleDescription": hhmsSensorArrayPowerModuleDescription,
       "hhmsSensorArrayPowerModuleStatus": hhmsSensorArrayPowerModuleStatus,
       "hhmsSensorArrayPowerModuleOnline": hhmsSensorArrayPowerModuleOnline,
       "hhmsSensorArrayPowerModuleGoOnline": hhmsSensorArrayPowerModuleGoOnline,
       "hhmsSensorArrayPowerOutletDescription": hhmsSensorArrayPowerOutletDescription,
       "hhmsSensorArrayPowerOutletStatus": hhmsSensorArrayPowerOutletStatus,
       "hhmsSensorArrayPowerOutletSet": hhmsSensorArrayPowerOutletSet,
       "hhmsSensorArrayPowerControlIndex": hhmsSensorArrayPowerControlIndex,
       "hhmsSensorArrayPowerMonitorTable": hhmsSensorArrayPowerMonitorTable,
       "hhmsSensorArrayPowerMonitorEntry": hhmsSensorArrayPowerMonitorEntry,
       "hhmsSensorArrayPowerMonitorDescription": hhmsSensorArrayPowerMonitorDescription,
       "hhmsSensorArrayPowerMonitorCurrent": hhmsSensorArrayPowerMonitorCurrent,
       "hhmsSensorArrayPowerMonitorVoltage": hhmsSensorArrayPowerMonitorVoltage,
       "hhmsSensorArrayPowerMonitorPower": hhmsSensorArrayPowerMonitorPower,
       "hhmsSensorArrayPowerMonitorStatus": hhmsSensorArrayPowerMonitorStatus,
       "hhmsSensorArrayPowerMonitorOnline": hhmsSensorArrayPowerMonitorOnline,
       "hhmsSensorArrayPowerMonitorGoOnline": hhmsSensorArrayPowerMonitorGoOnline,
       "hhmsSensorArrayPowerMonitorHighWarning": hhmsSensorArrayPowerMonitorHighWarning,
       "hhmsSensorArrayPowerMonitorHighCritical": hhmsSensorArrayPowerMonitorHighCritical,
       "hhmsSensorArrayPowerMonitorLowWarning": hhmsSensorArrayPowerMonitorLowWarning,
       "hhmsSensorArrayPowerMonitorLowCritical": hhmsSensorArrayPowerMonitorLowCritical,
       "hhmsSensorArrayPowerMonitorRearm": hhmsSensorArrayPowerMonitorRearm,
       "hhmsSensorArrayPowerMonitorIndex": hhmsSensorArrayPowerMonitorIndex,
       "hhmsSensorArrayHighDriveTable": hhmsSensorArrayHighDriveTable,
       "hhmsSensorArrayHighDriveEntry": hhmsSensorArrayHighDriveEntry,
       "hhmsSensorArrayHighDriveDescription": hhmsSensorArrayHighDriveDescription,
       "hhmsSensorArrayHighDriveOutputLevel": hhmsSensorArrayHighDriveOutputLevel,
       "hhmsSensorArrayHighDriveIndex": hhmsSensorArrayHighDriveIndex,
       "hhmsSensorArrayCameraTable": hhmsSensorArrayCameraTable,
       "hhmsSensorArrayCameraEntry": hhmsSensorArrayCameraEntry,
       "hhmsSensorArrayCameraDescription": hhmsSensorArrayCameraDescription,
       "hhmsSensorArrayCameraOnline": hhmsSensorArrayCameraOnline,
       "hhmsSensorArrayCameraGoOnline": hhmsSensorArrayCameraGoOnline,
       "hhmsSensorArrayCameraUrlMain": hhmsSensorArrayCameraUrlMain,
       "hhmsSensorArrayCameraUrlExtension": hhmsSensorArrayCameraUrlExtension,
       "hhmsSensorArrayCameraRefreshRate": hhmsSensorArrayCameraRefreshRate,
       "hhmsSensorArrayCameraIndex": hhmsSensorArrayCameraIndex,
       "hhmsSensorArrayTrapMailPollInterval": hhmsSensorArrayTrapMailPollInterval,
       "hhmsSensorArraySendTestMail": hhmsSensorArraySendTestMail,
       "hhmsSensorArrayLastSystemError": hhmsSensorArrayLastSystemError,
       "hhmsSensorArrayDataCollectionPeriod": hhmsSensorArrayDataCollectionPeriod,
       "hhmsSensorArrayMailTimeout": hhmsSensorArrayMailTimeout,
       "hhmsAgentConfig": hhmsAgentConfig,
       "hhmsAgentVersion": hhmsAgentVersion,
       "hhmsCompressedSummaryTable": hhmsCompressedSummaryTable,
       "hhmsCompressedSummaryEntry": hhmsCompressedSummaryEntry,
       "hhmsCompressedSummaryGet": hhmsCompressedSummaryGet,
       "hhmsCompressedSummaryIndex": hhmsCompressedSummaryIndex,
       "hhmsAgentTraps": hhmsAgentTraps,
       "hhmsSensorStatus": hhmsSensorStatus,
       "hhmsSensorValue": hhmsSensorValue,
       "hhmsSensorLevelExceeded": hhmsSensorLevelExceeded,
       "hhmsSensorIndex": hhmsSensorIndex,
       "hhmsSensorName": hhmsSensorName,
       "hhmsSensorDescription": hhmsSensorDescription}
)
