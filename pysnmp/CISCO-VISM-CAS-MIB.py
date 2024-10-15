# SNMP MIB module (CISCO-VISM-CAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VISM-CAS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:47 2024
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

(voice,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "voice")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoVismCasMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 88)
)
ciscoVismCasMIB.setRevisions(
        ("2003-07-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VismCasGrp_ObjectIdentity = ObjectIdentity
vismCasGrp = _VismCasGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8)
)
_VismCasVariantTable_Object = MibTable
vismCasVariantTable = _VismCasVariantTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1)
)
if mibBuilder.loadTexts:
    vismCasVariantTable.setStatus("current")
_VismCasVariantEntry_Object = MibTableRow
vismCasVariantEntry = _VismCasVariantEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1)
)
vismCasVariantEntry.setIndexNames(
    (0, "CISCO-VISM-CAS-MIB", "vismCasVariantName"),
)
if mibBuilder.loadTexts:
    vismCasVariantEntry.setStatus("current")
_VismCasVariantName_Type = DisplayString
_VismCasVariantName_Object = MibTableColumn
vismCasVariantName = _VismCasVariantName_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1, 1),
    _VismCasVariantName_Type()
)
vismCasVariantName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismCasVariantName.setStatus("current")


class _VismCasFileName_Type(DisplayString):
    """Custom type vismCasFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_VismCasFileName_Type.__name__ = "DisplayString"
_VismCasFileName_Object = MibTableColumn
vismCasFileName = _VismCasFileName_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1, 2),
    _VismCasFileName_Type()
)
vismCasFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCasFileName.setStatus("current")


class _VismCasTRinging_Type(Integer32):
    """Custom type vismCasTRinging based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_VismCasTRinging_Type.__name__ = "Integer32"
_VismCasTRinging_Object = MibTableColumn
vismCasTRinging = _VismCasTRinging_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1, 3),
    _VismCasTRinging_Type()
)
vismCasTRinging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCasTRinging.setStatus("deprecated")


class _VismCasDigitMethod_Type(Integer32):
    """Custom type vismCasDigitMethod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 2),
          ("mf", 1))
    )


_VismCasDigitMethod_Type.__name__ = "Integer32"
_VismCasDigitMethod_Object = MibTableColumn
vismCasDigitMethod = _VismCasDigitMethod_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1, 4),
    _VismCasDigitMethod_Type()
)
vismCasDigitMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCasDigitMethod.setStatus("current")


class _VismCasInterdigitTpart_Type(Integer32):
    """Custom type vismCasInterdigitTpart based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_VismCasInterdigitTpart_Type.__name__ = "Integer32"
_VismCasInterdigitTpart_Object = MibTableColumn
vismCasInterdigitTpart = _VismCasInterdigitTpart_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1, 5),
    _VismCasInterdigitTpart_Type()
)
vismCasInterdigitTpart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCasInterdigitTpart.setStatus("current")


class _VismCasInterdigitTcrit_Type(Integer32):
    """Custom type vismCasInterdigitTcrit based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VismCasInterdigitTcrit_Type.__name__ = "Integer32"
_VismCasInterdigitTcrit_Object = MibTableColumn
vismCasInterdigitTcrit = _VismCasInterdigitTcrit_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1, 6),
    _VismCasInterdigitTcrit_Type()
)
vismCasInterdigitTcrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCasInterdigitTcrit.setStatus("current")


class _VismCasInterdigitTMF_Type(Integer32):
    """Custom type vismCasInterdigitTMF based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_VismCasInterdigitTMF_Type.__name__ = "Integer32"
_VismCasInterdigitTMF_Object = MibTableColumn
vismCasInterdigitTMF = _VismCasInterdigitTMF_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1, 7),
    _VismCasInterdigitTMF_Type()
)
vismCasInterdigitTMF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCasInterdigitTMF.setStatus("current")


class _VismCasVariantState_Type(Integer32):
    """Custom type vismCasVariantState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configInProgress", 2),
          ("configured", 3),
          ("notConfigured", 1))
    )


_VismCasVariantState_Type.__name__ = "Integer32"
_VismCasVariantState_Object = MibTableColumn
vismCasVariantState = _VismCasVariantState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1, 8),
    _VismCasVariantState_Type()
)
vismCasVariantState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismCasVariantState.setStatus("current")


class _VismCasRowStatus_Type(Integer32):
    """Custom type vismCasRowStatus based on Integer32"""
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


_VismCasRowStatus_Type.__name__ = "Integer32"
_VismCasRowStatus_Object = MibTableColumn
vismCasRowStatus = _VismCasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1, 9),
    _VismCasRowStatus_Type()
)
vismCasRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCasRowStatus.setStatus("current")


class _VismCasCountryCode_Type(DisplayString):
    """Custom type vismCasCountryCode based on DisplayString"""
    defaultValue = OctetString("US")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_VismCasCountryCode_Type.__name__ = "DisplayString"
_VismCasCountryCode_Object = MibTableColumn
vismCasCountryCode = _VismCasCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1, 10),
    _VismCasCountryCode_Type()
)
vismCasCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCasCountryCode.setStatus("deprecated")


class _VismCasVariantSource_Type(Integer32):
    """Custom type vismCasVariantSource based on Integer32"""
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
        *(("external", 3),
          ("internal", 2),
          ("unspecified", 1))
    )


_VismCasVariantSource_Type.__name__ = "Integer32"
_VismCasVariantSource_Object = MibTableColumn
vismCasVariantSource = _VismCasVariantSource_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 1, 1, 11),
    _VismCasVariantSource_Type()
)
vismCasVariantSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCasVariantSource.setStatus("current")
_VismCasXgcpVariantTable_Object = MibTable
vismCasXgcpVariantTable = _VismCasXgcpVariantTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 2)
)
if mibBuilder.loadTexts:
    vismCasXgcpVariantTable.setStatus("current")
_VismCasXgcpVariantEntry_Object = MibTableRow
vismCasXgcpVariantEntry = _VismCasXgcpVariantEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 2, 1)
)
vismCasXgcpVariantEntry.setIndexNames(
    (0, "CISCO-VISM-CAS-MIB", "vismCasXgcpVariantName"),
)
if mibBuilder.loadTexts:
    vismCasXgcpVariantEntry.setStatus("current")
_VismCasXgcpVariantName_Type = DisplayString
_VismCasXgcpVariantName_Object = MibTableColumn
vismCasXgcpVariantName = _VismCasXgcpVariantName_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 2, 1, 1),
    _VismCasXgcpVariantName_Type()
)
vismCasXgcpVariantName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismCasXgcpVariantName.setStatus("current")
_VismCasXgcpFileName_Type = DisplayString
_VismCasXgcpFileName_Object = MibTableColumn
vismCasXgcpFileName = _VismCasXgcpFileName_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 2, 1, 2),
    _VismCasXgcpFileName_Type()
)
vismCasXgcpFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismCasXgcpFileName.setStatus("current")


class _VismCasXgcpMaxReXmitTime_Type(Integer32):
    """Custom type vismCasXgcpMaxReXmitTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_VismCasXgcpMaxReXmitTime_Type.__name__ = "Integer32"
_VismCasXgcpMaxReXmitTime_Object = MibTableColumn
vismCasXgcpMaxReXmitTime = _VismCasXgcpMaxReXmitTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 2, 1, 3),
    _VismCasXgcpMaxReXmitTime_Type()
)
vismCasXgcpMaxReXmitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCasXgcpMaxReXmitTime.setStatus("current")


class _VismCasXgcpInitialReXmitTime_Type(Integer32):
    """Custom type vismCasXgcpInitialReXmitTime based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_VismCasXgcpInitialReXmitTime_Type.__name__ = "Integer32"
_VismCasXgcpInitialReXmitTime_Object = MibTableColumn
vismCasXgcpInitialReXmitTime = _VismCasXgcpInitialReXmitTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 2, 1, 4),
    _VismCasXgcpInitialReXmitTime_Type()
)
vismCasXgcpInitialReXmitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCasXgcpInitialReXmitTime.setStatus("current")


class _VismCasXgcpMaxRetries_Type(Integer32):
    """Custom type vismCasXgcpMaxRetries based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_VismCasXgcpMaxRetries_Type.__name__ = "Integer32"
_VismCasXgcpMaxRetries_Object = MibTableColumn
vismCasXgcpMaxRetries = _VismCasXgcpMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 8, 2, 1, 5),
    _VismCasXgcpMaxRetries_Type()
)
vismCasXgcpMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCasXgcpMaxRetries.setStatus("current")
_CiscoVismCasMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVismCasMIBConformance = _CiscoVismCasMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 88, 2)
)
_CiscoVismCasMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVismCasMIBGroups = _CiscoVismCasMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 88, 2, 1)
)
_CiscoVismCasMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVismCasMIBCompliances = _CiscoVismCasMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 88, 2, 2)
)

# Managed Objects groups

ciscoVismCasVariantGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 88, 2, 1, 1)
)
ciscoVismCasVariantGroup.setObjects(
      *(("CISCO-VISM-CAS-MIB", "vismCasVariantName"),
        ("CISCO-VISM-CAS-MIB", "vismCasFileName"),
        ("CISCO-VISM-CAS-MIB", "vismCasDigitMethod"),
        ("CISCO-VISM-CAS-MIB", "vismCasInterdigitTpart"),
        ("CISCO-VISM-CAS-MIB", "vismCasInterdigitTcrit"),
        ("CISCO-VISM-CAS-MIB", "vismCasInterdigitTMF"),
        ("CISCO-VISM-CAS-MIB", "vismCasVariantState"),
        ("CISCO-VISM-CAS-MIB", "vismCasRowStatus"),
        ("CISCO-VISM-CAS-MIB", "vismCasVariantSource"))
)
if mibBuilder.loadTexts:
    ciscoVismCasVariantGroup.setStatus("current")

ciscoVismCasXgcpVariantGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 88, 2, 1, 2)
)
ciscoVismCasXgcpVariantGroup.setObjects(
      *(("CISCO-VISM-CAS-MIB", "vismCasXgcpVariantName"),
        ("CISCO-VISM-CAS-MIB", "vismCasXgcpFileName"),
        ("CISCO-VISM-CAS-MIB", "vismCasXgcpMaxReXmitTime"),
        ("CISCO-VISM-CAS-MIB", "vismCasXgcpInitialReXmitTime"),
        ("CISCO-VISM-CAS-MIB", "vismCasXgcpMaxRetries"))
)
if mibBuilder.loadTexts:
    ciscoVismCasXgcpVariantGroup.setStatus("current")

cvcVariantDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 88, 2, 1, 3)
)
cvcVariantDeprecatedGroup.setObjects(
      *(("CISCO-VISM-CAS-MIB", "vismCasTRinging"),
        ("CISCO-VISM-CAS-MIB", "vismCasCountryCode"))
)
if mibBuilder.loadTexts:
    cvcVariantDeprecatedGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVismCasCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 88, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoVismCasCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VISM-CAS-MIB",
    **{"vismCasGrp": vismCasGrp,
       "vismCasVariantTable": vismCasVariantTable,
       "vismCasVariantEntry": vismCasVariantEntry,
       "vismCasVariantName": vismCasVariantName,
       "vismCasFileName": vismCasFileName,
       "vismCasTRinging": vismCasTRinging,
       "vismCasDigitMethod": vismCasDigitMethod,
       "vismCasInterdigitTpart": vismCasInterdigitTpart,
       "vismCasInterdigitTcrit": vismCasInterdigitTcrit,
       "vismCasInterdigitTMF": vismCasInterdigitTMF,
       "vismCasVariantState": vismCasVariantState,
       "vismCasRowStatus": vismCasRowStatus,
       "vismCasCountryCode": vismCasCountryCode,
       "vismCasVariantSource": vismCasVariantSource,
       "vismCasXgcpVariantTable": vismCasXgcpVariantTable,
       "vismCasXgcpVariantEntry": vismCasXgcpVariantEntry,
       "vismCasXgcpVariantName": vismCasXgcpVariantName,
       "vismCasXgcpFileName": vismCasXgcpFileName,
       "vismCasXgcpMaxReXmitTime": vismCasXgcpMaxReXmitTime,
       "vismCasXgcpInitialReXmitTime": vismCasXgcpInitialReXmitTime,
       "vismCasXgcpMaxRetries": vismCasXgcpMaxRetries,
       "ciscoVismCasMIB": ciscoVismCasMIB,
       "ciscoVismCasMIBConformance": ciscoVismCasMIBConformance,
       "ciscoVismCasMIBGroups": ciscoVismCasMIBGroups,
       "ciscoVismCasVariantGroup": ciscoVismCasVariantGroup,
       "ciscoVismCasXgcpVariantGroup": ciscoVismCasXgcpVariantGroup,
       "cvcVariantDeprecatedGroup": cvcVariantDeprecatedGroup,
       "ciscoVismCasMIBCompliances": ciscoVismCasMIBCompliances,
       "ciscoVismCasCompliance": ciscoVismCasCompliance}
)
