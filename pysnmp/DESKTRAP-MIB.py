# SNMP MIB module (DESKTRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DESKTRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:03 2024
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sni_ObjectIdentity = ObjectIdentity
sni = _Sni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231)
)
_SniProductMibs_ObjectIdentity = ObjectIdentity
sniProductMibs = _SniProductMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2)
)
_SniExtensions_ObjectIdentity = ObjectIdentity
sniExtensions = _SniExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10)
)
_SniDesktopMgmt_ObjectIdentity = ObjectIdentity
sniDesktopMgmt = _SniDesktopMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3)
)
_SniDeskTrap_ObjectIdentity = ObjectIdentity
sniDeskTrap = _SniDeskTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 2)
)
_SniTrapAgentVersionInformation_ObjectIdentity = ObjectIdentity
sniTrapAgentVersionInformation = _SniTrapAgentVersionInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 2, 1)
)
_SniTrapAgentPurpose_Type = DisplayString
_SniTrapAgentPurpose_Object = MibScalar
sniTrapAgentPurpose = _SniTrapAgentPurpose_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 2, 1, 1),
    _SniTrapAgentPurpose_Type()
)
sniTrapAgentPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniTrapAgentPurpose.setStatus("mandatory")
_SniTrapAgentVersion_Type = DisplayString
_SniTrapAgentVersion_Object = MibScalar
sniTrapAgentVersion = _SniTrapAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 2, 1, 2),
    _SniTrapAgentVersion_Type()
)
sniTrapAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniTrapAgentVersion.setStatus("mandatory")
_SniTrapAgentDeskInfoVersion_Type = DisplayString
_SniTrapAgentDeskInfoVersion_Object = MibScalar
sniTrapAgentDeskInfoVersion = _SniTrapAgentDeskInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 2, 1, 3),
    _SniTrapAgentDeskInfoVersion_Type()
)
sniTrapAgentDeskInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniTrapAgentDeskInfoVersion.setStatus("mandatory")
_SniTrapAgentTrapParameter_ObjectIdentity = ObjectIdentity
sniTrapAgentTrapParameter = _SniTrapAgentTrapParameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 2, 2)
)
_SniTrapDesktop_Type = DisplayString
_SniTrapDesktop_Object = MibScalar
sniTrapDesktop = _SniTrapDesktop_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 2, 2, 1),
    _SniTrapDesktop_Type()
)
sniTrapDesktop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniTrapDesktop.setStatus("mandatory")
_SniTrapTimeInt_Type = Integer32
_SniTrapTimeInt_Object = MibScalar
sniTrapTimeInt = _SniTrapTimeInt_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 2, 2, 2),
    _SniTrapTimeInt_Type()
)
sniTrapTimeInt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniTrapTimeInt.setStatus("mandatory")
_SniTrapTimeStr_Type = DisplayString
_SniTrapTimeStr_Object = MibScalar
sniTrapTimeStr = _SniTrapTimeStr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 2, 2, 3),
    _SniTrapTimeStr_Type()
)
sniTrapTimeStr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniTrapTimeStr.setStatus("mandatory")


class _SniTrapAgentStatus_Type(Integer32):
    """Custom type sniTrapAgentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("st-critical", 3),
          ("st-ok", 1),
          ("st-unknown", 0),
          ("st-warning", 2))
    )


_SniTrapAgentStatus_Type.__name__ = "Integer32"
_SniTrapAgentStatus_Object = MibScalar
sniTrapAgentStatus = _SniTrapAgentStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 2, 2, 4),
    _SniTrapAgentStatus_Type()
)
sniTrapAgentStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniTrapAgentStatus.setStatus("mandatory")


class _SniTrapAgentType_Type(Integer32):
    """Custom type sniTrapAgentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("t-alert", 1),
          ("t-event", 2),
          ("t-info", 3))
    )


_SniTrapAgentType_Type.__name__ = "Integer32"
_SniTrapAgentType_Object = MibScalar
sniTrapAgentType = _SniTrapAgentType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 2, 2, 5),
    _SniTrapAgentType_Type()
)
sniTrapAgentType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniTrapAgentType.setStatus("mandatory")
_SniTrapAgentEventName_Type = DisplayString
_SniTrapAgentEventName_Object = MibScalar
sniTrapAgentEventName = _SniTrapAgentEventName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 2, 2, 6),
    _SniTrapAgentEventName_Type()
)
sniTrapAgentEventName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniTrapAgentEventName.setStatus("mandatory")
_SniTrapAgentEventText_Type = DisplayString
_SniTrapAgentEventText_Object = MibScalar
sniTrapAgentEventText = _SniTrapAgentEventText_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 2, 2, 7),
    _SniTrapAgentEventText_Type()
)
sniTrapAgentEventText.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniTrapAgentEventText.setStatus("mandatory")
_SniTrapAgentTimeBIAS_Type = Integer32
_SniTrapAgentTimeBIAS_Object = MibScalar
sniTrapAgentTimeBIAS = _SniTrapAgentTimeBIAS_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 2, 2, 8),
    _SniTrapAgentTimeBIAS_Type()
)
sniTrapAgentTimeBIAS.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniTrapAgentTimeBIAS.setStatus("mandatory")


class _SniTrapAgentSystemStatus_Type(Integer32):
    """Custom type sniTrapAgentSystemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("st-critical", 3),
          ("st-ok", 1),
          ("st-unknown", 0),
          ("st-warning", 2))
    )


_SniTrapAgentSystemStatus_Type.__name__ = "Integer32"
_SniTrapAgentSystemStatus_Object = MibScalar
sniTrapAgentSystemStatus = _SniTrapAgentSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 2, 2, 9),
    _SniTrapAgentSystemStatus_Type()
)
sniTrapAgentSystemStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniTrapAgentSystemStatus.setStatus("mandatory")


class _SniTrapAgentClassStatus_Type(Integer32):
    """Custom type sniTrapAgentClassStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("st-critical", 3),
          ("st-ok", 1),
          ("st-unknown", 0),
          ("st-warning", 2))
    )


_SniTrapAgentClassStatus_Type.__name__ = "Integer32"
_SniTrapAgentClassStatus_Object = MibScalar
sniTrapAgentClassStatus = _SniTrapAgentClassStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 2, 2, 10),
    _SniTrapAgentClassStatus_Type()
)
sniTrapAgentClassStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniTrapAgentClassStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

sniTrapError = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 1)
)
sniTrapError.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniTrapError.setStatus(
        ""
    )

sniSmartOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 1001)
)
sniSmartOK.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniSmartOK.setStatus(
        ""
    )

sniSmartWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 1002)
)
sniSmartWarning.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniSmartWarning.setStatus(
        ""
    )

sniSmartError = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 1003)
)
sniSmartError.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniSmartError.setStatus(
        ""
    )

sniCoverClosed = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 2001)
)
sniCoverClosed.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniCoverClosed.setStatus(
        ""
    )

sniCoverOpened = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 2003)
)
sniCoverOpened.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniCoverOpened.setStatus(
        ""
    )

sniCoverSensorincorporated = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 3001)
)
sniCoverSensorincorporated.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniCoverSensorincorporated.setStatus(
        ""
    )

sniCoverSensorMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 3003)
)
sniCoverSensorMissing.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniCoverSensorMissing.setStatus(
        ""
    )

sniCoverRecognition = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 4001)
)
sniCoverRecognition.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniCoverRecognition.setStatus(
        ""
    )

sniCoverRecognitionMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 4003)
)
sniCoverRecognitionMissing.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniCoverRecognitionMissing.setStatus(
        ""
    )

sniNoShortCurcuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 5001)
)
sniNoShortCurcuit.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniNoShortCurcuit.setStatus(
        ""
    )

sniShortCurcuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 5003)
)
sniShortCurcuit.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniShortCurcuit.setStatus(
        ""
    )

sniTemperatureOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 7001)
)
sniTemperatureOK.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniTemperatureOK.setStatus(
        ""
    )

sniTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 7002)
)
sniTemperatureWarning.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniTemperatureWarning.setStatus(
        ""
    )

sniTemperatureCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 7003)
)
sniTemperatureCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniTemperatureCritical.setStatus(
        ""
    )

sniFanRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 8001)
)
sniFanRunning.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniFanRunning.setStatus(
        ""
    )

sniFanNotRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 8003)
)
sniFanNotRunning.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniFanNotRunning.setStatus(
        ""
    )

sniFanWornOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 9001)
)
sniFanWornOK.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniFanWornOK.setStatus(
        ""
    )

sniFanWornWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 9002)
)
sniFanWornWarning.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniFanWornWarning.setStatus(
        ""
    )

sniFanWornCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 9003)
)
sniFanWornCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniFanWornCritical.setStatus(
        ""
    )

sniVoltageOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 11001)
)
sniVoltageOk.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniVoltageOk.setStatus(
        ""
    )

sniVoltageWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 11002)
)
sniVoltageWarning.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniVoltageWarning.setStatus(
        ""
    )

sniVoltageCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 11003)
)
sniVoltageCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniVoltageCritical.setStatus(
        ""
    )

sniWatchdogOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 12001)
)
sniWatchdogOk.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniWatchdogOk.setStatus(
        ""
    )

sniWatchdogCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 12003)
)
sniWatchdogCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniWatchdogCritical.setStatus(
        ""
    )

sniInternalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 13001)
)
sniInternalError.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniInternalError.setStatus(
        ""
    )

sniBIOSErrorLogOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 14001)
)
sniBIOSErrorLogOK.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniBIOSErrorLogOK.setStatus(
        ""
    )

sniBIOSErrorLogWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 14002)
)
sniBIOSErrorLogWarning.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniBIOSErrorLogWarning.setStatus(
        ""
    )

sniBIOSErrorLogCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 14003)
)
sniBIOSErrorLogCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniBIOSErrorLogCritical.setStatus(
        ""
    )

sniAOLPOSTCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 15003)
)
sniAOLPOSTCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLPOSTCritical.setStatus(
        ""
    )

sniAOLWatchdogCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 16003)
)
sniAOLWatchdogCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLWatchdogCritical.setStatus(
        ""
    )

sniAOLCoverOpened = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 17003)
)
sniAOLCoverOpened.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLCoverOpened.setStatus(
        ""
    )

sniAOLCPUMissingCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 18003)
)
sniAOLCPUMissingCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLCPUMissingCritical.setStatus(
        ""
    )

sniAOLHeartbeatCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 20003)
)
sniAOLHeartbeatCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLHeartbeatCritical.setStatus(
        ""
    )

sniFreeDiskSpaceOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 21001)
)
sniFreeDiskSpaceOK.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniFreeDiskSpaceOK.setStatus(
        ""
    )

sniFreeDiskSpaceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 21002)
)
sniFreeDiskSpaceWarning.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniFreeDiskSpaceWarning.setStatus(
        ""
    )

sniFreeDiskSpaceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 21003)
)
sniFreeDiskSpaceError.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniFreeDiskSpaceError.setStatus(
        ""
    )

sniMemoryChangesOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 22001)
)
sniMemoryChangesOK.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniMemoryChangesOK.setStatus(
        ""
    )

sniMemoryChangesWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 22002)
)
sniMemoryChangesWarning.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniMemoryChangesWarning.setStatus(
        ""
    )

sniMemoryChangesError = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 22003)
)
sniMemoryChangesError.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniMemoryChangesError.setStatus(
        ""
    )

sniDeviceChangesOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 23001)
)
sniDeviceChangesOK.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniDeviceChangesOK.setStatus(
        ""
    )

sniDeviceChangesWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 23002)
)
sniDeviceChangesWarning.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniDeviceChangesWarning.setStatus(
        ""
    )

sniDeviceChangesError = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 23003)
)
sniDeviceChangesError.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniDeviceChangesError.setStatus(
        ""
    )

sniAOLVoltage_Fan_TemperatureCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 24003)
)
sniAOLVoltage_Fan_TemperatureCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLVoltage_Fan_TemperatureCritical.setStatus(
        ""
    )

sniAOLLANLeashCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 25003)
)
sniAOLLANLeashCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLLANLeashCritical.setStatus(
        ""
    )

sniAOLProcessorTemperatureCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 26003)
)
sniAOLProcessorTemperatureCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLProcessorTemperatureCritical.setStatus(
        ""
    )

sniAOLProcessor0MissingCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 28003)
)
sniAOLProcessor0MissingCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLProcessor0MissingCritical.setStatus(
        ""
    )

sniAOLProcessor1MissingCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 29003)
)
sniAOLProcessor1MissingCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLProcessor1MissingCritical.setStatus(
        ""
    )

sniAOLVoltage_FanCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 30003)
)
sniAOLVoltage_FanCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLVoltage_FanCritical.setStatus(
        ""
    )

sniAOLVoltageCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 31003)
)
sniAOLVoltageCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLVoltageCritical.setStatus(
        ""
    )

sniAOLFanCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 32003)
)
sniAOLFanCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLFanCritical.setStatus(
        ""
    )

sniAOLFan_TemperatureCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 33003)
)
sniAOLFan_TemperatureCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLFan_TemperatureCritical.setStatus(
        ""
    )

sniAOLVoltage_TemperatureCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 34003)
)
sniAOLVoltage_TemperatureCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLVoltage_TemperatureCritical.setStatus(
        ""
    )

sniAOLNICSMBusSlotCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 35003)
)
sniAOLNICSMBusSlotCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLNICSMBusSlotCritical.setStatus(
        ""
    )

sniAOLPresencePongCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 36003)
)
sniAOLPresencePongCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLPresencePongCritical.setStatus(
        ""
    )

sniAOLHardwareMonitorCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 37003)
)
sniAOLHardwareMonitorCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLHardwareMonitorCritical.setStatus(
        ""
    )

sniAOL1_5VGTLVoltageCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 38003)
)
sniAOL1_5VGTLVoltageCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOL1_5VGTLVoltageCritical.setStatus(
        ""
    )

sniAOLCPUCoreVoltageCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 39003)
)
sniAOLCPUCoreVoltageCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLCPUCoreVoltageCritical.setStatus(
        ""
    )

sniAOL3_3VStandbyCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 40003)
)
sniAOL3_3VStandbyCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOL3_3VStandbyCritical.setStatus(
        ""
    )

sniAOL5VoltageCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 41003)
)
sniAOL5VoltageCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOL5VoltageCritical.setStatus(
        ""
    )

sniAOLHardwareMonitorInternalTemperatureCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 42003)
)
sniAOLHardwareMonitorInternalTemperatureCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLHardwareMonitorInternalTemperatureCritical.setStatus(
        ""
    )

sniAOLCPUDiodeSensorCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 43003)
)
sniAOLCPUDiodeSensorCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLCPUDiodeSensorCritical.setStatus(
        ""
    )

sniAOLCPUFanCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 44003)
)
sniAOLCPUFanCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLCPUFanCritical.setStatus(
        ""
    )

sniAOLChassisFanCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 45003)
)
sniAOLChassisFanCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLChassisFanCritical.setStatus(
        ""
    )

sniAOL12VoltageCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 46003)
)
sniAOL12VoltageCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOL12VoltageCritical.setStatus(
        ""
    )

sniAOL3_3VoltageCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 47003)
)
sniAOL3_3VoltageCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOL3_3VoltageCritical.setStatus(
        ""
    )

sniAOLCPUDiodeCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 48003)
)
sniAOLCPUDiodeCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLCPUDiodeCritical.setStatus(
        ""
    )

sniAOL2_5VoltageCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 49003)
)
sniAOL2_5VoltageCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOL2_5VoltageCritical.setStatus(
        ""
    )

sniAOLAmbientTemperatureCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 50003)
)
sniAOLAmbientTemperatureCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLAmbientTemperatureCritical.setStatus(
        ""
    )

sniAOLRemoteTemperatureCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 51003)
)
sniAOLRemoteTemperatureCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLRemoteTemperatureCritical.setStatus(
        ""
    )

sniAOLUndockEventCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 52003)
)
sniAOLUndockEventCritical.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniAOLUndockEventCritical.setStatus(
        ""
    )

sniFreeSystemDiskSpaceOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 56001)
)
sniFreeSystemDiskSpaceOK.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniFreeSystemDiskSpaceOK.setStatus(
        ""
    )

sniFreeSystemDiskSpaceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 56002)
)
sniFreeSystemDiskSpaceWarning.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniFreeSystemDiskSpaceWarning.setStatus(
        ""
    )

sniFreeSystemDiskSpaceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 56003)
)
sniFreeSystemDiskSpaceError.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniFreeSystemDiskSpaceError.setStatus(
        ""
    )

sniLeaseExpirationOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 57001)
)
sniLeaseExpirationOK.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniLeaseExpirationOK.setStatus(
        ""
    )

sniLeaseExpirationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 57002)
)
sniLeaseExpirationWarning.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniLeaseExpirationWarning.setStatus(
        ""
    )

sniLeaseExpirationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 57003)
)
sniLeaseExpirationError.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniLeaseExpirationError.setStatus(
        ""
    )

sniProcessorChangeOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 58001)
)
sniProcessorChangeOK.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniProcessorChangeOK.setStatus(
        ""
    )

sniProcessorChangeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 58002)
)
sniProcessorChangeWarning.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniProcessorChangeWarning.setStatus(
        ""
    )

sniProcessorChangeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 3, 0, 58003)
)
sniProcessorChangeError.setObjects(
      *(("DESKTRAP-MIB", "sniTrapDesktop"),
        ("DESKTRAP-MIB", "sniTrapTimeInt"),
        ("DESKTRAP-MIB", "sniTrapTimeStr"),
        ("DESKTRAP-MIB", "sniTrapAgentStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentType"),
        ("DESKTRAP-MIB", "sniTrapAgentEventName"),
        ("DESKTRAP-MIB", "sniTrapAgentEventText"),
        ("DESKTRAP-MIB", "sniTrapAgentTimeBIAS"),
        ("DESKTRAP-MIB", "sniTrapAgentSystemStatus"),
        ("DESKTRAP-MIB", "sniTrapAgentClassStatus"))
)
if mibBuilder.loadTexts:
    sniProcessorChangeError.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DESKTRAP-MIB",
    **{"sni": sni,
       "sniProductMibs": sniProductMibs,
       "sniExtensions": sniExtensions,
       "sniDesktopMgmt": sniDesktopMgmt,
       "sniTrapError": sniTrapError,
       "sniSmartOK": sniSmartOK,
       "sniSmartWarning": sniSmartWarning,
       "sniSmartError": sniSmartError,
       "sniCoverClosed": sniCoverClosed,
       "sniCoverOpened": sniCoverOpened,
       "sniCoverSensorincorporated": sniCoverSensorincorporated,
       "sniCoverSensorMissing": sniCoverSensorMissing,
       "sniCoverRecognition": sniCoverRecognition,
       "sniCoverRecognitionMissing": sniCoverRecognitionMissing,
       "sniNoShortCurcuit": sniNoShortCurcuit,
       "sniShortCurcuit": sniShortCurcuit,
       "sniTemperatureOK": sniTemperatureOK,
       "sniTemperatureWarning": sniTemperatureWarning,
       "sniTemperatureCritical": sniTemperatureCritical,
       "sniFanRunning": sniFanRunning,
       "sniFanNotRunning": sniFanNotRunning,
       "sniFanWornOK": sniFanWornOK,
       "sniFanWornWarning": sniFanWornWarning,
       "sniFanWornCritical": sniFanWornCritical,
       "sniVoltageOk": sniVoltageOk,
       "sniVoltageWarning": sniVoltageWarning,
       "sniVoltageCritical": sniVoltageCritical,
       "sniWatchdogOk": sniWatchdogOk,
       "sniWatchdogCritical": sniWatchdogCritical,
       "sniInternalError": sniInternalError,
       "sniBIOSErrorLogOK": sniBIOSErrorLogOK,
       "sniBIOSErrorLogWarning": sniBIOSErrorLogWarning,
       "sniBIOSErrorLogCritical": sniBIOSErrorLogCritical,
       "sniAOLPOSTCritical": sniAOLPOSTCritical,
       "sniAOLWatchdogCritical": sniAOLWatchdogCritical,
       "sniAOLCoverOpened": sniAOLCoverOpened,
       "sniAOLCPUMissingCritical": sniAOLCPUMissingCritical,
       "sniAOLHeartbeatCritical": sniAOLHeartbeatCritical,
       "sniFreeDiskSpaceOK": sniFreeDiskSpaceOK,
       "sniFreeDiskSpaceWarning": sniFreeDiskSpaceWarning,
       "sniFreeDiskSpaceError": sniFreeDiskSpaceError,
       "sniMemoryChangesOK": sniMemoryChangesOK,
       "sniMemoryChangesWarning": sniMemoryChangesWarning,
       "sniMemoryChangesError": sniMemoryChangesError,
       "sniDeviceChangesOK": sniDeviceChangesOK,
       "sniDeviceChangesWarning": sniDeviceChangesWarning,
       "sniDeviceChangesError": sniDeviceChangesError,
       "sniAOLVoltage-Fan-TemperatureCritical": sniAOLVoltage_Fan_TemperatureCritical,
       "sniAOLLANLeashCritical": sniAOLLANLeashCritical,
       "sniAOLProcessorTemperatureCritical": sniAOLProcessorTemperatureCritical,
       "sniAOLProcessor0MissingCritical": sniAOLProcessor0MissingCritical,
       "sniAOLProcessor1MissingCritical": sniAOLProcessor1MissingCritical,
       "sniAOLVoltage-FanCritical": sniAOLVoltage_FanCritical,
       "sniAOLVoltageCritical": sniAOLVoltageCritical,
       "sniAOLFanCritical": sniAOLFanCritical,
       "sniAOLFan-TemperatureCritical": sniAOLFan_TemperatureCritical,
       "sniAOLVoltage-TemperatureCritical": sniAOLVoltage_TemperatureCritical,
       "sniAOLNICSMBusSlotCritical": sniAOLNICSMBusSlotCritical,
       "sniAOLPresencePongCritical": sniAOLPresencePongCritical,
       "sniAOLHardwareMonitorCritical": sniAOLHardwareMonitorCritical,
       "sniAOL1-5VGTLVoltageCritical": sniAOL1_5VGTLVoltageCritical,
       "sniAOLCPUCoreVoltageCritical": sniAOLCPUCoreVoltageCritical,
       "sniAOL3-3VStandbyCritical": sniAOL3_3VStandbyCritical,
       "sniAOL5VoltageCritical": sniAOL5VoltageCritical,
       "sniAOLHardwareMonitorInternalTemperatureCritical": sniAOLHardwareMonitorInternalTemperatureCritical,
       "sniAOLCPUDiodeSensorCritical": sniAOLCPUDiodeSensorCritical,
       "sniAOLCPUFanCritical": sniAOLCPUFanCritical,
       "sniAOLChassisFanCritical": sniAOLChassisFanCritical,
       "sniAOL12VoltageCritical": sniAOL12VoltageCritical,
       "sniAOL3-3VoltageCritical": sniAOL3_3VoltageCritical,
       "sniAOLCPUDiodeCritical": sniAOLCPUDiodeCritical,
       "sniAOL2-5VoltageCritical": sniAOL2_5VoltageCritical,
       "sniAOLAmbientTemperatureCritical": sniAOLAmbientTemperatureCritical,
       "sniAOLRemoteTemperatureCritical": sniAOLRemoteTemperatureCritical,
       "sniAOLUndockEventCritical": sniAOLUndockEventCritical,
       "sniFreeSystemDiskSpaceOK": sniFreeSystemDiskSpaceOK,
       "sniFreeSystemDiskSpaceWarning": sniFreeSystemDiskSpaceWarning,
       "sniFreeSystemDiskSpaceError": sniFreeSystemDiskSpaceError,
       "sniLeaseExpirationOK": sniLeaseExpirationOK,
       "sniLeaseExpirationWarning": sniLeaseExpirationWarning,
       "sniLeaseExpirationError": sniLeaseExpirationError,
       "sniProcessorChangeOK": sniProcessorChangeOK,
       "sniProcessorChangeWarning": sniProcessorChangeWarning,
       "sniProcessorChangeError": sniProcessorChangeError,
       "sniDeskTrap": sniDeskTrap,
       "sniTrapAgentVersionInformation": sniTrapAgentVersionInformation,
       "sniTrapAgentPurpose": sniTrapAgentPurpose,
       "sniTrapAgentVersion": sniTrapAgentVersion,
       "sniTrapAgentDeskInfoVersion": sniTrapAgentDeskInfoVersion,
       "sniTrapAgentTrapParameter": sniTrapAgentTrapParameter,
       "sniTrapDesktop": sniTrapDesktop,
       "sniTrapTimeInt": sniTrapTimeInt,
       "sniTrapTimeStr": sniTrapTimeStr,
       "sniTrapAgentStatus": sniTrapAgentStatus,
       "sniTrapAgentType": sniTrapAgentType,
       "sniTrapAgentEventName": sniTrapAgentEventName,
       "sniTrapAgentEventText": sniTrapAgentEventText,
       "sniTrapAgentTimeBIAS": sniTrapAgentTimeBIAS,
       "sniTrapAgentSystemStatus": sniTrapAgentSystemStatus,
       "sniTrapAgentClassStatus": sniTrapAgentClassStatus}
)
