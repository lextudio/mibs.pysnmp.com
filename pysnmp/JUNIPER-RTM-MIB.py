# SNMP MIB module (JUNIPER-RTM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-RTM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:09 2024
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

(jnxVoip,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxVoip")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

jnxRtmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxRtmMIBObjects_ObjectIdentity = ObjectIdentity
jnxRtmMIBObjects = _JnxRtmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1)
)
_JnxSipTemplateTable_Object = MibTable
jnxSipTemplateTable = _JnxSipTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxSipTemplateTable.setStatus("current")
_JnxSipTemplateEntry_Object = MibTableRow
jnxSipTemplateEntry = _JnxSipTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 1, 1)
)
jnxSipTemplateEntry.setIndexNames(
    (0, "JUNIPER-RTM-MIB", "jnxSipTemplateName"),
)
if mibBuilder.loadTexts:
    jnxSipTemplateEntry.setStatus("current")
_JnxSipTemplateName_Type = DisplayString
_JnxSipTemplateName_Object = MibTableColumn
jnxSipTemplateName = _JnxSipTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 1, 1, 1),
    _JnxSipTemplateName_Type()
)
jnxSipTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSipTemplateName.setStatus("current")


class _JnxDtmfMethod_Type(Integer32):
    """Custom type jnxDtmfMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inband", 3),
          ("rfc-2833", 1),
          ("sip-info", 2))
    )


_JnxDtmfMethod_Type.__name__ = "Integer32"
_JnxDtmfMethod_Object = MibTableColumn
jnxDtmfMethod = _JnxDtmfMethod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 1, 1, 2),
    _JnxDtmfMethod_Type()
)
jnxDtmfMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDtmfMethod.setStatus("current")


class _JnxCallerIdTransmit_Type(Integer32):
    """Custom type jnxCallerIdTransmit based on Integer32"""
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


_JnxCallerIdTransmit_Type.__name__ = "Integer32"
_JnxCallerIdTransmit_Object = MibTableColumn
jnxCallerIdTransmit = _JnxCallerIdTransmit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 1, 1, 3),
    _JnxCallerIdTransmit_Type()
)
jnxCallerIdTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCallerIdTransmit.setStatus("current")
_JnxInheritExtensionsFrom_Type = DisplayString
_JnxInheritExtensionsFrom_Object = MibTableColumn
jnxInheritExtensionsFrom = _JnxInheritExtensionsFrom_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 1, 1, 4),
    _JnxInheritExtensionsFrom_Type()
)
jnxInheritExtensionsFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxInheritExtensionsFrom.setStatus("current")
_JnxInheritExtensionsTo_Type = DisplayString
_JnxInheritExtensionsTo_Object = MibTableColumn
jnxInheritExtensionsTo = _JnxInheritExtensionsTo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 1, 1, 5),
    _JnxInheritExtensionsTo_Type()
)
jnxInheritExtensionsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxInheritExtensionsTo.setStatus("current")
_JnxClassOfRestriction_Type = DisplayString
_JnxClassOfRestriction_Object = MibTableColumn
jnxClassOfRestriction = _JnxClassOfRestriction_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 1, 1, 6),
    _JnxClassOfRestriction_Type()
)
jnxClassOfRestriction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxClassOfRestriction.setStatus("current")


class _JnxCodecG711MU_Type(Integer32):
    """Custom type jnxCodecG711MU based on Integer32"""
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


_JnxCodecG711MU_Type.__name__ = "Integer32"
_JnxCodecG711MU_Object = MibTableColumn
jnxCodecG711MU = _JnxCodecG711MU_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 1, 1, 7),
    _JnxCodecG711MU_Type()
)
jnxCodecG711MU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCodecG711MU.setStatus("current")


class _JnxCodecG711A_Type(Integer32):
    """Custom type jnxCodecG711A based on Integer32"""
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


_JnxCodecG711A_Type.__name__ = "Integer32"
_JnxCodecG711A_Object = MibTableColumn
jnxCodecG711A = _JnxCodecG711A_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 1, 1, 8),
    _JnxCodecG711A_Type()
)
jnxCodecG711A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCodecG711A.setStatus("current")


class _JnxCodecG729AB_Type(Integer32):
    """Custom type jnxCodecG729AB based on Integer32"""
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


_JnxCodecG729AB_Type.__name__ = "Integer32"
_JnxCodecG729AB_Object = MibTableColumn
jnxCodecG729AB = _JnxCodecG729AB_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 1, 1, 9),
    _JnxCodecG729AB_Type()
)
jnxCodecG729AB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCodecG729AB.setStatus("current")
_JnxAnalogTemplateTable_Object = MibTable
jnxAnalogTemplateTable = _JnxAnalogTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxAnalogTemplateTable.setStatus("current")
_JnxAnalogTemplateEntry_Object = MibTableRow
jnxAnalogTemplateEntry = _JnxAnalogTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 2, 1)
)
jnxAnalogTemplateEntry.setIndexNames(
    (0, "JUNIPER-RTM-MIB", "jnxAnalogTemplateName"),
)
if mibBuilder.loadTexts:
    jnxAnalogTemplateEntry.setStatus("current")
_JnxAnalogTemplateName_Type = DisplayString
_JnxAnalogTemplateName_Object = MibTableColumn
jnxAnalogTemplateName = _JnxAnalogTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 2, 1, 1),
    _JnxAnalogTemplateName_Type()
)
jnxAnalogTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxAnalogTemplateName.setStatus("current")


class _JnxAanalogCallerIdTransmit_Type(Integer32):
    """Custom type jnxAanalogCallerIdTransmit based on Integer32"""
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


_JnxAanalogCallerIdTransmit_Type.__name__ = "Integer32"
_JnxAanalogCallerIdTransmit_Object = MibTableColumn
jnxAanalogCallerIdTransmit = _JnxAanalogCallerIdTransmit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 2, 1, 2),
    _JnxAanalogCallerIdTransmit_Type()
)
jnxAanalogCallerIdTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAanalogCallerIdTransmit.setStatus("current")


class _JnxAnalogVoiceActivityDetection_Type(Integer32):
    """Custom type jnxAnalogVoiceActivityDetection based on Integer32"""
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


_JnxAnalogVoiceActivityDetection_Type.__name__ = "Integer32"
_JnxAnalogVoiceActivityDetection_Object = MibTableColumn
jnxAnalogVoiceActivityDetection = _JnxAnalogVoiceActivityDetection_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 2, 1, 3),
    _JnxAnalogVoiceActivityDetection_Type()
)
jnxAnalogVoiceActivityDetection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAnalogVoiceActivityDetection.setStatus("current")


class _JnxAnalogComfortNoiseGeneration_Type(Integer32):
    """Custom type jnxAnalogComfortNoiseGeneration based on Integer32"""
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


_JnxAnalogComfortNoiseGeneration_Type.__name__ = "Integer32"
_JnxAnalogComfortNoiseGeneration_Object = MibTableColumn
jnxAnalogComfortNoiseGeneration = _JnxAnalogComfortNoiseGeneration_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 2, 1, 4),
    _JnxAnalogComfortNoiseGeneration_Type()
)
jnxAnalogComfortNoiseGeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAnalogComfortNoiseGeneration.setStatus("current")
_JnxAnalogClassOfRestriction_Type = DisplayString
_JnxAnalogClassOfRestriction_Object = MibTableColumn
jnxAnalogClassOfRestriction = _JnxAnalogClassOfRestriction_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 2, 1, 5),
    _JnxAnalogClassOfRestriction_Type()
)
jnxAnalogClassOfRestriction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAnalogClassOfRestriction.setStatus("current")
_JnxStationTable_Object = MibTable
jnxStationTable = _JnxStationTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxStationTable.setStatus("current")
_JnxStationEntry_Object = MibTableRow
jnxStationEntry = _JnxStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1)
)
jnxStationEntry.setIndexNames(
    (0, "JUNIPER-RTM-MIB", "jnxStationName"),
)
if mibBuilder.loadTexts:
    jnxStationEntry.setStatus("current")
_JnxStationName_Type = DisplayString
_JnxStationName_Object = MibTableColumn
jnxStationName = _JnxStationName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 1),
    _JnxStationName_Type()
)
jnxStationName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxStationName.setStatus("current")
_JnxStationExtension_Type = DisplayString
_JnxStationExtension_Object = MibTableColumn
jnxStationExtension = _JnxStationExtension_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 2),
    _JnxStationExtension_Type()
)
jnxStationExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxStationExtension.setStatus("current")
_JnxStationRestriction_Type = DisplayString
_JnxStationRestriction_Object = MibTableColumn
jnxStationRestriction = _JnxStationRestriction_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 3),
    _JnxStationRestriction_Type()
)
jnxStationRestriction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxStationRestriction.setStatus("current")
_JnxStationCallerId_Type = DisplayString
_JnxStationCallerId_Object = MibTableColumn
jnxStationCallerId = _JnxStationCallerId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 5),
    _JnxStationCallerId_Type()
)
jnxStationCallerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxStationCallerId.setStatus("current")
_JnxStationDID_Type = DisplayString
_JnxStationDID_Object = MibTableColumn
jnxStationDID = _JnxStationDID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 6),
    _JnxStationDID_Type()
)
jnxStationDID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxStationDID.setStatus("current")
_JnxStationDILTdmInterface_Type = DisplayString
_JnxStationDILTdmInterface_Object = MibTableColumn
jnxStationDILTdmInterface = _JnxStationDILTdmInterface_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 7),
    _JnxStationDILTdmInterface_Type()
)
jnxStationDILTdmInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxStationDILTdmInterface.setStatus("current")
_JnxStationDILTimeSlotNumber_Type = Unsigned32
_JnxStationDILTimeSlotNumber_Object = MibTableColumn
jnxStationDILTimeSlotNumber = _JnxStationDILTimeSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 8),
    _JnxStationDILTimeSlotNumber_Type()
)
jnxStationDILTimeSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxStationDILTimeSlotNumber.setStatus("current")
_JnxStationAuthId_Type = DisplayString
_JnxStationAuthId_Object = MibTableColumn
jnxStationAuthId = _JnxStationAuthId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 9),
    _JnxStationAuthId_Type()
)
jnxStationAuthId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxStationAuthId.setStatus("current")


class _JnxStationType_Type(Integer32):
    """Custom type jnxStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("analog", 2),
          ("sip", 1))
    )


_JnxStationType_Type.__name__ = "Integer32"
_JnxStationType_Object = MibTableColumn
jnxStationType = _JnxStationType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 10),
    _JnxStationType_Type()
)
jnxStationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxStationType.setStatus("current")
_JnxStationTemplate_Type = DisplayString
_JnxStationTemplate_Object = MibTableColumn
jnxStationTemplate = _JnxStationTemplate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 11),
    _JnxStationTemplate_Type()
)
jnxStationTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxStationTemplate.setStatus("current")
_JnxStationTdmInterface_Type = DisplayString
_JnxStationTdmInterface_Object = MibTableColumn
jnxStationTdmInterface = _JnxStationTdmInterface_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 12),
    _JnxStationTdmInterface_Type()
)
jnxStationTdmInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxStationTdmInterface.setStatus("current")
_JnxStationTimeSlotNumber_Type = Unsigned32
_JnxStationTimeSlotNumber_Object = MibTableColumn
jnxStationTimeSlotNumber = _JnxStationTimeSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 3, 1, 13),
    _JnxStationTimeSlotNumber_Type()
)
jnxStationTimeSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxStationTimeSlotNumber.setStatus("current")
_JnxSurvivableCallServiceTable_Object = MibTable
jnxSurvivableCallServiceTable = _JnxSurvivableCallServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4)
)
if mibBuilder.loadTexts:
    jnxSurvivableCallServiceTable.setStatus("current")
_JnxSurvivableCallServiceEntry_Object = MibTableRow
jnxSurvivableCallServiceEntry = _JnxSurvivableCallServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1)
)
jnxSurvivableCallServiceEntry.setIndexNames(
    (0, "JUNIPER-RTM-MIB", "jnxSurvivableCallServiceName"),
)
if mibBuilder.loadTexts:
    jnxSurvivableCallServiceEntry.setStatus("current")
_JnxSurvivableCallServiceName_Type = DisplayString
_JnxSurvivableCallServiceName_Object = MibTableColumn
jnxSurvivableCallServiceName = _JnxSurvivableCallServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 1),
    _JnxSurvivableCallServiceName_Type()
)
jnxSurvivableCallServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSurvivableCallServiceName.setStatus("current")
_JnxSurvivableCallServicePeerCallServer_Type = DisplayString
_JnxSurvivableCallServicePeerCallServer_Object = MibTableColumn
jnxSurvivableCallServicePeerCallServer = _JnxSurvivableCallServicePeerCallServer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 2),
    _JnxSurvivableCallServicePeerCallServer_Type()
)
jnxSurvivableCallServicePeerCallServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSurvivableCallServicePeerCallServer.setStatus("current")


class _JnxSurvivableCallServiceSipProtocolPort_Type(Integer32):
    """Custom type jnxSurvivableCallServiceSipProtocolPort based on Integer32"""
    defaultValue = 5060

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxSurvivableCallServiceSipProtocolPort_Type.__name__ = "Integer32"
_JnxSurvivableCallServiceSipProtocolPort_Object = MibTableColumn
jnxSurvivableCallServiceSipProtocolPort = _JnxSurvivableCallServiceSipProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 3),
    _JnxSurvivableCallServiceSipProtocolPort_Type()
)
jnxSurvivableCallServiceSipProtocolPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSurvivableCallServiceSipProtocolPort.setStatus("current")


class _JnxSurvivableCallServiceSipProtocolTransport_Type(Integer32):
    """Custom type jnxSurvivableCallServiceSipProtocolTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("tls", 3),
          ("udp", 2))
    )


_JnxSurvivableCallServiceSipProtocolTransport_Type.__name__ = "Integer32"
_JnxSurvivableCallServiceSipProtocolTransport_Object = MibTableColumn
jnxSurvivableCallServiceSipProtocolTransport = _JnxSurvivableCallServiceSipProtocolTransport_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 4),
    _JnxSurvivableCallServiceSipProtocolTransport_Type()
)
jnxSurvivableCallServiceSipProtocolTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSurvivableCallServiceSipProtocolTransport.setStatus("current")


class _JnxSurvivableCallServiceHeartbeatNormalInterval_Type(Integer32):
    """Custom type jnxSurvivableCallServiceHeartbeatNormalInterval based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8),
    )


_JnxSurvivableCallServiceHeartbeatNormalInterval_Type.__name__ = "Integer32"
_JnxSurvivableCallServiceHeartbeatNormalInterval_Object = MibTableColumn
jnxSurvivableCallServiceHeartbeatNormalInterval = _JnxSurvivableCallServiceHeartbeatNormalInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 5),
    _JnxSurvivableCallServiceHeartbeatNormalInterval_Type()
)
jnxSurvivableCallServiceHeartbeatNormalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSurvivableCallServiceHeartbeatNormalInterval.setStatus("current")


class _JnxSurvivableCallServiceRegistrationExpiryTimeout_Type(Integer32):
    """Custom type jnxSurvivableCallServiceRegistrationExpiryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxSurvivableCallServiceRegistrationExpiryTimeout_Type.__name__ = "Integer32"
_JnxSurvivableCallServiceRegistrationExpiryTimeout_Object = MibTableColumn
jnxSurvivableCallServiceRegistrationExpiryTimeout = _JnxSurvivableCallServiceRegistrationExpiryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 6),
    _JnxSurvivableCallServiceRegistrationExpiryTimeout_Type()
)
jnxSurvivableCallServiceRegistrationExpiryTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSurvivableCallServiceRegistrationExpiryTimeout.setStatus("current")


class _JnxSurvivableCallServiceSipTimeout_Type(Integer32):
    """Custom type jnxSurvivableCallServiceSipTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 120),
    )


_JnxSurvivableCallServiceSipTimeout_Type.__name__ = "Integer32"
_JnxSurvivableCallServiceSipTimeout_Object = MibTableColumn
jnxSurvivableCallServiceSipTimeout = _JnxSurvivableCallServiceSipTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 7),
    _JnxSurvivableCallServiceSipTimeout_Type()
)
jnxSurvivableCallServiceSipTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSurvivableCallServiceSipTimeout.setStatus("current")


class _JnxSurvivableCallServiceMonitorTimeout_Type(Integer32):
    """Custom type jnxSurvivableCallServiceMonitorTimeout based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_JnxSurvivableCallServiceMonitorTimeout_Type.__name__ = "Integer32"
_JnxSurvivableCallServiceMonitorTimeout_Object = MibTableColumn
jnxSurvivableCallServiceMonitorTimeout = _JnxSurvivableCallServiceMonitorTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 8),
    _JnxSurvivableCallServiceMonitorTimeout_Type()
)
jnxSurvivableCallServiceMonitorTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSurvivableCallServiceMonitorTimeout.setStatus("current")


class _JnxSurvivableCallServiceHeartbeatSurvivableInterval_Type(Integer32):
    """Custom type jnxSurvivableCallServiceHeartbeatSurvivableInterval based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_JnxSurvivableCallServiceHeartbeatSurvivableInterval_Type.__name__ = "Integer32"
_JnxSurvivableCallServiceHeartbeatSurvivableInterval_Object = MibTableColumn
jnxSurvivableCallServiceHeartbeatSurvivableInterval = _JnxSurvivableCallServiceHeartbeatSurvivableInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 9),
    _JnxSurvivableCallServiceHeartbeatSurvivableInterval_Type()
)
jnxSurvivableCallServiceHeartbeatSurvivableInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSurvivableCallServiceHeartbeatSurvivableInterval.setStatus("current")


class _JnxSurvivableCallServiceResponseThresholdMinimum_Type(Integer32):
    """Custom type jnxSurvivableCallServiceResponseThresholdMinimum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JnxSurvivableCallServiceResponseThresholdMinimum_Type.__name__ = "Integer32"
_JnxSurvivableCallServiceResponseThresholdMinimum_Object = MibTableColumn
jnxSurvivableCallServiceResponseThresholdMinimum = _JnxSurvivableCallServiceResponseThresholdMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 10),
    _JnxSurvivableCallServiceResponseThresholdMinimum_Type()
)
jnxSurvivableCallServiceResponseThresholdMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSurvivableCallServiceResponseThresholdMinimum.setStatus("current")
_JnxSurvivableCallServiceServicePointZone_Type = DisplayString
_JnxSurvivableCallServiceServicePointZone_Object = MibTableColumn
jnxSurvivableCallServiceServicePointZone = _JnxSurvivableCallServiceServicePointZone_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 11),
    _JnxSurvivableCallServiceServicePointZone_Type()
)
jnxSurvivableCallServiceServicePointZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSurvivableCallServiceServicePointZone.setStatus("current")
_JnxSurvivableCallServiceDialPlan_Type = DisplayString
_JnxSurvivableCallServiceDialPlan_Object = MibTableColumn
jnxSurvivableCallServiceDialPlan = _JnxSurvivableCallServiceDialPlan_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 4, 1, 12),
    _JnxSurvivableCallServiceDialPlan_Type()
)
jnxSurvivableCallServiceDialPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSurvivableCallServiceDialPlan.setStatus("current")
_JnxTrunkConfigTable_Object = MibTable
jnxTrunkConfigTable = _JnxTrunkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 5)
)
if mibBuilder.loadTexts:
    jnxTrunkConfigTable.setStatus("current")
_JnxTrunkConfigEntry_Object = MibTableRow
jnxTrunkConfigEntry = _JnxTrunkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 5, 1)
)
jnxTrunkConfigEntry.setIndexNames(
    (0, "JUNIPER-RTM-MIB", "jnxTrunkConfigName"),
)
if mibBuilder.loadTexts:
    jnxTrunkConfigEntry.setStatus("current")
_JnxTrunkConfigName_Type = DisplayString
_JnxTrunkConfigName_Object = MibTableColumn
jnxTrunkConfigName = _JnxTrunkConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 5, 1, 1),
    _JnxTrunkConfigName_Type()
)
jnxTrunkConfigName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxTrunkConfigName.setStatus("current")


class _JnxTrunkConfigType_Type(Integer32):
    """Custom type jnxTrunkConfigType based on Integer32"""
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
        *(("e1", 4),
          ("fxo", 2),
          ("fxs", 1),
          ("t1", 3))
    )


_JnxTrunkConfigType_Type.__name__ = "Integer32"
_JnxTrunkConfigType_Object = MibTableColumn
jnxTrunkConfigType = _JnxTrunkConfigType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 5, 1, 2),
    _JnxTrunkConfigType_Type()
)
jnxTrunkConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTrunkConfigType.setStatus("current")
_JnxTrunkConfigTdmInterface_Type = DisplayString
_JnxTrunkConfigTdmInterface_Object = MibTableColumn
jnxTrunkConfigTdmInterface = _JnxTrunkConfigTdmInterface_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 5, 1, 3),
    _JnxTrunkConfigTdmInterface_Type()
)
jnxTrunkConfigTdmInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTrunkConfigTdmInterface.setStatus("current")
_JnxTrunkConfigT1CasGroupTimeSlots_Type = DisplayString
_JnxTrunkConfigT1CasGroupTimeSlots_Object = MibTableColumn
jnxTrunkConfigT1CasGroupTimeSlots = _JnxTrunkConfigT1CasGroupTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 5, 1, 4),
    _JnxTrunkConfigT1CasGroupTimeSlots_Type()
)
jnxTrunkConfigT1CasGroupTimeSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTrunkConfigT1CasGroupTimeSlots.setStatus("current")


class _JnxTrunkConfigT1CasGroupSignaling_Type(Integer32):
    """Custom type jnxTrunkConfigT1CasGroupSignaling based on Integer32"""
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
        *(("em-wink-start", 5),
          ("fxo-ground-start", 2),
          ("fxo-loop-start", 1),
          ("fxs-ground-start", 4),
          ("fxs-loop-start", 3))
    )


_JnxTrunkConfigT1CasGroupSignaling_Type.__name__ = "Integer32"
_JnxTrunkConfigT1CasGroupSignaling_Object = MibTableColumn
jnxTrunkConfigT1CasGroupSignaling = _JnxTrunkConfigT1CasGroupSignaling_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 5, 1, 5),
    _JnxTrunkConfigT1CasGroupSignaling_Type()
)
jnxTrunkConfigT1CasGroupSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTrunkConfigT1CasGroupSignaling.setStatus("current")
_JnxDigitManipulationTable_Object = MibTable
jnxDigitManipulationTable = _JnxDigitManipulationTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 6)
)
if mibBuilder.loadTexts:
    jnxDigitManipulationTable.setStatus("current")
_JnxDigitManipulationEntry_Object = MibTableRow
jnxDigitManipulationEntry = _JnxDigitManipulationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 6, 1)
)
jnxDigitManipulationEntry.setIndexNames(
    (0, "JUNIPER-RTM-MIB", "jnxDigitTransformName"),
)
if mibBuilder.loadTexts:
    jnxDigitManipulationEntry.setStatus("current")
_JnxDigitTransformName_Type = DisplayString
_JnxDigitTransformName_Object = MibTableColumn
jnxDigitTransformName = _JnxDigitTransformName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 6, 1, 1),
    _JnxDigitTransformName_Type()
)
jnxDigitTransformName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxDigitTransformName.setStatus("current")
_JnxDigitTransformRegularExpression_Type = DisplayString
_JnxDigitTransformRegularExpression_Object = MibTableColumn
jnxDigitTransformRegularExpression = _JnxDigitTransformRegularExpression_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 6, 1, 2),
    _JnxDigitTransformRegularExpression_Type()
)
jnxDigitTransformRegularExpression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDigitTransformRegularExpression.setStatus("current")
_JnxPeerCallServerTable_Object = MibTable
jnxPeerCallServerTable = _JnxPeerCallServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7)
)
if mibBuilder.loadTexts:
    jnxPeerCallServerTable.setStatus("current")
_JnxPeerCallServerEntry_Object = MibTableRow
jnxPeerCallServerEntry = _JnxPeerCallServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1)
)
jnxPeerCallServerEntry.setIndexNames(
    (0, "JUNIPER-RTM-MIB", "jnxPeerCallServerName"),
)
if mibBuilder.loadTexts:
    jnxPeerCallServerEntry.setStatus("current")
_JnxPeerCallServerName_Type = DisplayString
_JnxPeerCallServerName_Object = MibTableColumn
jnxPeerCallServerName = _JnxPeerCallServerName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1, 1),
    _JnxPeerCallServerName_Type()
)
jnxPeerCallServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPeerCallServerName.setStatus("current")
_JnxPeerCallServerDescription_Type = DisplayString
_JnxPeerCallServerDescription_Object = MibTableColumn
jnxPeerCallServerDescription = _JnxPeerCallServerDescription_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1, 2),
    _JnxPeerCallServerDescription_Type()
)
jnxPeerCallServerDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPeerCallServerDescription.setStatus("current")
_JnxPeerCallServerAddress_Type = DisplayString
_JnxPeerCallServerAddress_Object = MibTableColumn
jnxPeerCallServerAddress = _JnxPeerCallServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1, 3),
    _JnxPeerCallServerAddress_Type()
)
jnxPeerCallServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPeerCallServerAddress.setStatus("current")


class _JnxPeerCallServerSipProtocolPort_Type(Integer32):
    """Custom type jnxPeerCallServerSipProtocolPort based on Integer32"""
    defaultValue = 5060

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxPeerCallServerSipProtocolPort_Type.__name__ = "Integer32"
_JnxPeerCallServerSipProtocolPort_Object = MibTableColumn
jnxPeerCallServerSipProtocolPort = _JnxPeerCallServerSipProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1, 4),
    _JnxPeerCallServerSipProtocolPort_Type()
)
jnxPeerCallServerSipProtocolPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPeerCallServerSipProtocolPort.setStatus("current")


class _JnxPeerCallServerSipProtocolTransport_Type(Integer32):
    """Custom type jnxPeerCallServerSipProtocolTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("tls", 3),
          ("udp", 2))
    )


_JnxPeerCallServerSipProtocolTransport_Type.__name__ = "Integer32"
_JnxPeerCallServerSipProtocolTransport_Object = MibTableColumn
jnxPeerCallServerSipProtocolTransport = _JnxPeerCallServerSipProtocolTransport_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1, 5),
    _JnxPeerCallServerSipProtocolTransport_Type()
)
jnxPeerCallServerSipProtocolTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPeerCallServerSipProtocolTransport.setStatus("current")


class _JnxPeerCallServerCodecG711MU_Type(Integer32):
    """Custom type jnxPeerCallServerCodecG711MU based on Integer32"""
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


_JnxPeerCallServerCodecG711MU_Type.__name__ = "Integer32"
_JnxPeerCallServerCodecG711MU_Object = MibTableColumn
jnxPeerCallServerCodecG711MU = _JnxPeerCallServerCodecG711MU_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1, 6),
    _JnxPeerCallServerCodecG711MU_Type()
)
jnxPeerCallServerCodecG711MU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPeerCallServerCodecG711MU.setStatus("current")


class _JnxPeerCallServerCodecG711A_Type(Integer32):
    """Custom type jnxPeerCallServerCodecG711A based on Integer32"""
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


_JnxPeerCallServerCodecG711A_Type.__name__ = "Integer32"
_JnxPeerCallServerCodecG711A_Object = MibTableColumn
jnxPeerCallServerCodecG711A = _JnxPeerCallServerCodecG711A_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1, 7),
    _JnxPeerCallServerCodecG711A_Type()
)
jnxPeerCallServerCodecG711A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPeerCallServerCodecG711A.setStatus("current")


class _JnxPeerCallServerCodecG729AB_Type(Integer32):
    """Custom type jnxPeerCallServerCodecG729AB based on Integer32"""
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


_JnxPeerCallServerCodecG729AB_Type.__name__ = "Integer32"
_JnxPeerCallServerCodecG729AB_Object = MibTableColumn
jnxPeerCallServerCodecG729AB = _JnxPeerCallServerCodecG729AB_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1, 8),
    _JnxPeerCallServerCodecG729AB_Type()
)
jnxPeerCallServerCodecG729AB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPeerCallServerCodecG729AB.setStatus("current")


class _JnxPeerCallServerDtmfMethod_Type(Integer32):
    """Custom type jnxPeerCallServerDtmfMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inband", 3),
          ("rfc-2833", 1),
          ("sip-info", 2))
    )


_JnxPeerCallServerDtmfMethod_Type.__name__ = "Integer32"
_JnxPeerCallServerDtmfMethod_Object = MibTableColumn
jnxPeerCallServerDtmfMethod = _JnxPeerCallServerDtmfMethod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1, 9),
    _JnxPeerCallServerDtmfMethod_Type()
)
jnxPeerCallServerDtmfMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPeerCallServerDtmfMethod.setStatus("current")
_JnxPeerCallServerPstnAccessNumber_Type = DisplayString
_JnxPeerCallServerPstnAccessNumber_Object = MibTableColumn
jnxPeerCallServerPstnAccessNumber = _JnxPeerCallServerPstnAccessNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1, 10),
    _JnxPeerCallServerPstnAccessNumber_Type()
)
jnxPeerCallServerPstnAccessNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPeerCallServerPstnAccessNumber.setStatus("current")
_JnxPeerCallServerAuthId_Type = DisplayString
_JnxPeerCallServerAuthId_Object = MibTableColumn
jnxPeerCallServerAuthId = _JnxPeerCallServerAuthId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 7, 1, 11),
    _JnxPeerCallServerAuthId_Type()
)
jnxPeerCallServerAuthId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPeerCallServerAuthId.setStatus("current")
_JnxFeatures_ObjectIdentity = ObjectIdentity
jnxFeatures = _JnxFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 8)
)
_JnxFeaturesLiveAttendantExtension_Type = DisplayString
_JnxFeaturesLiveAttendantExtension_Object = MibScalar
jnxFeaturesLiveAttendantExtension = _JnxFeaturesLiveAttendantExtension_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 8, 1),
    _JnxFeaturesLiveAttendantExtension_Type()
)
jnxFeaturesLiveAttendantExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFeaturesLiveAttendantExtension.setStatus("current")
_JnxFeaturesLiveAttendantStartTime_Type = DisplayString
_JnxFeaturesLiveAttendantStartTime_Object = MibScalar
jnxFeaturesLiveAttendantStartTime = _JnxFeaturesLiveAttendantStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 8, 2),
    _JnxFeaturesLiveAttendantStartTime_Type()
)
jnxFeaturesLiveAttendantStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFeaturesLiveAttendantStartTime.setStatus("current")
_JnxFeaturesLiveAttendantEndTime_Type = DisplayString
_JnxFeaturesLiveAttendantEndTime_Object = MibScalar
jnxFeaturesLiveAttendantEndTime = _JnxFeaturesLiveAttendantEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 8, 3),
    _JnxFeaturesLiveAttendantEndTime_Type()
)
jnxFeaturesLiveAttendantEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFeaturesLiveAttendantEndTime.setStatus("current")


class _JnxFeaturesAttendantRingCount_Type(Integer32):
    """Custom type jnxFeaturesAttendantRingCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxFeaturesAttendantRingCount_Type.__name__ = "Integer32"
_JnxFeaturesAttendantRingCount_Object = MibScalar
jnxFeaturesAttendantRingCount = _JnxFeaturesAttendantRingCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 8, 4),
    _JnxFeaturesAttendantRingCount_Type()
)
jnxFeaturesAttendantRingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFeaturesAttendantRingCount.setStatus("current")
_JnxFeaturesVoicemailExtension_Type = DisplayString
_JnxFeaturesVoicemailExtension_Object = MibScalar
jnxFeaturesVoicemailExtension = _JnxFeaturesVoicemailExtension_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 8, 5),
    _JnxFeaturesVoicemailExtension_Type()
)
jnxFeaturesVoicemailExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFeaturesVoicemailExtension.setStatus("current")
_JnxFeaturesVoicemailRemoteAccessNumber_Type = DisplayString
_JnxFeaturesVoicemailRemoteAccessNumber_Object = MibScalar
jnxFeaturesVoicemailRemoteAccessNumber = _JnxFeaturesVoicemailRemoteAccessNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 8, 6),
    _JnxFeaturesVoicemailRemoteAccessNumber_Type()
)
jnxFeaturesVoicemailRemoteAccessNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFeaturesVoicemailRemoteAccessNumber.setStatus("current")
_JnxDialPlanTable_Object = MibTable
jnxDialPlanTable = _JnxDialPlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 9)
)
if mibBuilder.loadTexts:
    jnxDialPlanTable.setStatus("current")
_JnxDialPlanEntry_Object = MibTableRow
jnxDialPlanEntry = _JnxDialPlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 9, 1)
)
jnxDialPlanEntry.setIndexNames(
    (0, "JUNIPER-RTM-MIB", "jnxDialPlanName"),
    (0, "JUNIPER-RTM-MIB", "jnxDialPlanDigitPattern"),
)
if mibBuilder.loadTexts:
    jnxDialPlanEntry.setStatus("current")
_JnxDialPlanName_Type = DisplayString
_JnxDialPlanName_Object = MibTableColumn
jnxDialPlanName = _JnxDialPlanName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 9, 1, 1),
    _JnxDialPlanName_Type()
)
jnxDialPlanName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxDialPlanName.setStatus("current")
_JnxDialPlanDigitPattern_Type = DisplayString
_JnxDialPlanDigitPattern_Object = MibTableColumn
jnxDialPlanDigitPattern = _JnxDialPlanDigitPattern_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 9, 1, 2),
    _JnxDialPlanDigitPattern_Type()
)
jnxDialPlanDigitPattern.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxDialPlanDigitPattern.setStatus("current")
_JnxDialPlanCallType_Type = DisplayString
_JnxDialPlanCallType_Object = MibTableColumn
jnxDialPlanCallType = _JnxDialPlanCallType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 9, 1, 3),
    _JnxDialPlanCallType_Type()
)
jnxDialPlanCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDialPlanCallType.setStatus("current")
_JnxDialPlanTrunkGroupList_Type = DisplayString
_JnxDialPlanTrunkGroupList_Object = MibTableColumn
jnxDialPlanTrunkGroupList = _JnxDialPlanTrunkGroupList_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 9, 1, 4),
    _JnxDialPlanTrunkGroupList_Type()
)
jnxDialPlanTrunkGroupList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxDialPlanTrunkGroupList.setStatus("current")
_JnxClassOfRestrictionTable_Object = MibTable
jnxClassOfRestrictionTable = _JnxClassOfRestrictionTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 11)
)
if mibBuilder.loadTexts:
    jnxClassOfRestrictionTable.setStatus("current")
_JnxClassOfRestrictionEntry_Object = MibTableRow
jnxClassOfRestrictionEntry = _JnxClassOfRestrictionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 11, 1)
)
jnxClassOfRestrictionEntry.setIndexNames(
    (0, "JUNIPER-RTM-MIB", "jnxClassOfRestrictionName"),
    (0, "JUNIPER-RTM-MIB", "jnxRestrictionPolicyName"),
)
if mibBuilder.loadTexts:
    jnxClassOfRestrictionEntry.setStatus("current")
_JnxClassOfRestrictionName_Type = DisplayString
_JnxClassOfRestrictionName_Object = MibTableColumn
jnxClassOfRestrictionName = _JnxClassOfRestrictionName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 11, 1, 1),
    _JnxClassOfRestrictionName_Type()
)
jnxClassOfRestrictionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxClassOfRestrictionName.setStatus("current")
_JnxRestrictionPolicyName_Type = DisplayString
_JnxRestrictionPolicyName_Object = MibTableColumn
jnxRestrictionPolicyName = _JnxRestrictionPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 11, 1, 2),
    _JnxRestrictionPolicyName_Type()
)
jnxRestrictionPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxRestrictionPolicyName.setStatus("current")
_JnxRestrictionCallType_Type = DisplayString
_JnxRestrictionCallType_Object = MibTableColumn
jnxRestrictionCallType = _JnxRestrictionCallType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 11, 1, 3),
    _JnxRestrictionCallType_Type()
)
jnxRestrictionCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRestrictionCallType.setStatus("current")


class _JnxRestrictionCallPermission_Type(Integer32):
    """Custom type jnxRestrictionCallPermission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_JnxRestrictionCallPermission_Type.__name__ = "Integer32"
_JnxRestrictionCallPermission_Object = MibTableColumn
jnxRestrictionCallPermission = _JnxRestrictionCallPermission_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 11, 1, 4),
    _JnxRestrictionCallPermission_Type()
)
jnxRestrictionCallPermission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRestrictionCallPermission.setStatus("current")
_JnxMediaGatewayTable_Object = MibTable
jnxMediaGatewayTable = _JnxMediaGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 12)
)
if mibBuilder.loadTexts:
    jnxMediaGatewayTable.setStatus("current")
_JnxMediaGatewayEntry_Object = MibTableRow
jnxMediaGatewayEntry = _JnxMediaGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 12, 1)
)
jnxMediaGatewayEntry.setIndexNames(
    (0, "JUNIPER-RTM-MIB", "jnxMediaGatewayName"),
)
if mibBuilder.loadTexts:
    jnxMediaGatewayEntry.setStatus("current")
_JnxMediaGatewayName_Type = DisplayString
_JnxMediaGatewayName_Object = MibTableColumn
jnxMediaGatewayName = _JnxMediaGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 12, 1, 1),
    _JnxMediaGatewayName_Type()
)
jnxMediaGatewayName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMediaGatewayName.setStatus("current")
_JnxMediaGatewayPeerCallServer_Type = DisplayString
_JnxMediaGatewayPeerCallServer_Object = MibTableColumn
jnxMediaGatewayPeerCallServer = _JnxMediaGatewayPeerCallServer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 12, 1, 2),
    _JnxMediaGatewayPeerCallServer_Type()
)
jnxMediaGatewayPeerCallServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMediaGatewayPeerCallServer.setStatus("current")


class _JnxMediaGatewaySipProtocolPort_Type(Integer32):
    """Custom type jnxMediaGatewaySipProtocolPort based on Integer32"""
    defaultValue = 5060

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxMediaGatewaySipProtocolPort_Type.__name__ = "Integer32"
_JnxMediaGatewaySipProtocolPort_Object = MibTableColumn
jnxMediaGatewaySipProtocolPort = _JnxMediaGatewaySipProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 12, 1, 3),
    _JnxMediaGatewaySipProtocolPort_Type()
)
jnxMediaGatewaySipProtocolPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMediaGatewaySipProtocolPort.setStatus("current")


class _JnxMediaGatewaySipProtocolTransport_Type(Integer32):
    """Custom type jnxMediaGatewaySipProtocolTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("tls", 3),
          ("udp", 2))
    )


_JnxMediaGatewaySipProtocolTransport_Type.__name__ = "Integer32"
_JnxMediaGatewaySipProtocolTransport_Object = MibTableColumn
jnxMediaGatewaySipProtocolTransport = _JnxMediaGatewaySipProtocolTransport_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 12, 1, 4),
    _JnxMediaGatewaySipProtocolTransport_Type()
)
jnxMediaGatewaySipProtocolTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMediaGatewaySipProtocolTransport.setStatus("current")
_JnxMediaGatewayDialPlan_Type = DisplayString
_JnxMediaGatewayDialPlan_Object = MibTableColumn
jnxMediaGatewayDialPlan = _JnxMediaGatewayDialPlan_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 12, 1, 5),
    _JnxMediaGatewayDialPlan_Type()
)
jnxMediaGatewayDialPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMediaGatewayDialPlan.setStatus("current")
_JnxTrunkGroupTable_Object = MibTable
jnxTrunkGroupTable = _JnxTrunkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 13)
)
if mibBuilder.loadTexts:
    jnxTrunkGroupTable.setStatus("current")
_JnxTrunkGroupEntry_Object = MibTableRow
jnxTrunkGroupEntry = _JnxTrunkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 13, 1)
)
jnxTrunkGroupEntry.setIndexNames(
    (0, "JUNIPER-RTM-MIB", "jnxTrunkGroupName"),
)
if mibBuilder.loadTexts:
    jnxTrunkGroupEntry.setStatus("current")
_JnxTrunkGroupName_Type = DisplayString
_JnxTrunkGroupName_Object = MibTableColumn
jnxTrunkGroupName = _JnxTrunkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 13, 1, 1),
    _JnxTrunkGroupName_Type()
)
jnxTrunkGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxTrunkGroupName.setStatus("current")
_JnxTrunkGroupDescription_Type = DisplayString
_JnxTrunkGroupDescription_Object = MibTableColumn
jnxTrunkGroupDescription = _JnxTrunkGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 13, 1, 2),
    _JnxTrunkGroupDescription_Type()
)
jnxTrunkGroupDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTrunkGroupDescription.setStatus("current")
_JnxTrunkGroupTrunkList_Type = DisplayString
_JnxTrunkGroupTrunkList_Object = MibTableColumn
jnxTrunkGroupTrunkList = _JnxTrunkGroupTrunkList_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 13, 1, 3),
    _JnxTrunkGroupTrunkList_Type()
)
jnxTrunkGroupTrunkList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTrunkGroupTrunkList.setStatus("current")
_JnxSurvivableStatsTable_Object = MibTable
jnxSurvivableStatsTable = _JnxSurvivableStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14)
)
if mibBuilder.loadTexts:
    jnxSurvivableStatsTable.setStatus("current")
_JnxSurvivableStatsEntry_Object = MibTableRow
jnxSurvivableStatsEntry = _JnxSurvivableStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1)
)
jnxSurvivableStatsEntry.setIndexNames(
    (0, "JUNIPER-RTM-MIB", "jnxSurvivableStatsAddress"),
    (0, "JUNIPER-RTM-MIB", "jnxSurvivableStatsPort"),
    (0, "JUNIPER-RTM-MIB", "jnxSurvivableStatsTransport"),
)
if mibBuilder.loadTexts:
    jnxSurvivableStatsEntry.setStatus("current")
_JnxSurvivableStatsAddress_Type = IpAddress
_JnxSurvivableStatsAddress_Object = MibTableColumn
jnxSurvivableStatsAddress = _JnxSurvivableStatsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 1),
    _JnxSurvivableStatsAddress_Type()
)
jnxSurvivableStatsAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSurvivableStatsAddress.setStatus("current")
_JnxSurvivableStatsPort_Type = Unsigned32
_JnxSurvivableStatsPort_Object = MibTableColumn
jnxSurvivableStatsPort = _JnxSurvivableStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 2),
    _JnxSurvivableStatsPort_Type()
)
jnxSurvivableStatsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSurvivableStatsPort.setStatus("current")


class _JnxSurvivableStatsTransport_Type(Integer32):
    """Custom type jnxSurvivableStatsTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_JnxSurvivableStatsTransport_Type.__name__ = "Integer32"
_JnxSurvivableStatsTransport_Object = MibTableColumn
jnxSurvivableStatsTransport = _JnxSurvivableStatsTransport_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 3),
    _JnxSurvivableStatsTransport_Type()
)
jnxSurvivableStatsTransport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSurvivableStatsTransport.setStatus("current")
_JnxSurvivableStatsSCSName_Type = DisplayString
_JnxSurvivableStatsSCSName_Object = MibTableColumn
jnxSurvivableStatsSCSName = _JnxSurvivableStatsSCSName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 4),
    _JnxSurvivableStatsSCSName_Type()
)
jnxSurvivableStatsSCSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSurvivableStatsSCSName.setStatus("current")
_JnxSurvivableStatsPeerCallServer_Type = DisplayString
_JnxSurvivableStatsPeerCallServer_Object = MibTableColumn
jnxSurvivableStatsPeerCallServer = _JnxSurvivableStatsPeerCallServer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 5),
    _JnxSurvivableStatsPeerCallServer_Type()
)
jnxSurvivableStatsPeerCallServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSurvivableStatsPeerCallServer.setStatus("current")


class _JnxSurvivableStatsCurrentState_Type(Integer32):
    """Custom type jnxSurvivableStatsCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("monitor", 3),
          ("normal", 1),
          ("survivable", 2))
    )


_JnxSurvivableStatsCurrentState_Type.__name__ = "Integer32"
_JnxSurvivableStatsCurrentState_Object = MibTableColumn
jnxSurvivableStatsCurrentState = _JnxSurvivableStatsCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 6),
    _JnxSurvivableStatsCurrentState_Type()
)
jnxSurvivableStatsCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSurvivableStatsCurrentState.setStatus("current")
_JnxSurvivableStatsPriority_Type = Integer32
_JnxSurvivableStatsPriority_Object = MibTableColumn
jnxSurvivableStatsPriority = _JnxSurvivableStatsPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 7),
    _JnxSurvivableStatsPriority_Type()
)
jnxSurvivableStatsPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSurvivableStatsPriority.setStatus("current")
_JnxSurvivableStatsLastDownTime_Type = DisplayString
_JnxSurvivableStatsLastDownTime_Object = MibTableColumn
jnxSurvivableStatsLastDownTime = _JnxSurvivableStatsLastDownTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 8),
    _JnxSurvivableStatsLastDownTime_Type()
)
jnxSurvivableStatsLastDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSurvivableStatsLastDownTime.setStatus("current")
_JnxSurvivableStatsLastDownLen_Type = Unsigned32
_JnxSurvivableStatsLastDownLen_Object = MibTableColumn
jnxSurvivableStatsLastDownLen = _JnxSurvivableStatsLastDownLen_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 9),
    _JnxSurvivableStatsLastDownLen_Type()
)
jnxSurvivableStatsLastDownLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSurvivableStatsLastDownLen.setStatus("current")
_JnxSurvivableStatsTotalDownTime_Type = Unsigned32
_JnxSurvivableStatsTotalDownTime_Object = MibTableColumn
jnxSurvivableStatsTotalDownTime = _JnxSurvivableStatsTotalDownTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 10),
    _JnxSurvivableStatsTotalDownTime_Type()
)
jnxSurvivableStatsTotalDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSurvivableStatsTotalDownTime.setStatus("current")
_JnxSurvivableStatsTimesDown_Type = Unsigned32
_JnxSurvivableStatsTimesDown_Object = MibTableColumn
jnxSurvivableStatsTimesDown = _JnxSurvivableStatsTimesDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 11),
    _JnxSurvivableStatsTimesDown_Type()
)
jnxSurvivableStatsTimesDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSurvivableStatsTimesDown.setStatus("current")
_JnxSurvivableStatsMinResponse_Type = Unsigned32
_JnxSurvivableStatsMinResponse_Object = MibTableColumn
jnxSurvivableStatsMinResponse = _JnxSurvivableStatsMinResponse_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 12),
    _JnxSurvivableStatsMinResponse_Type()
)
jnxSurvivableStatsMinResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSurvivableStatsMinResponse.setStatus("current")
_JnxSurvivableStatsMaxResponse_Type = Unsigned32
_JnxSurvivableStatsMaxResponse_Object = MibTableColumn
jnxSurvivableStatsMaxResponse = _JnxSurvivableStatsMaxResponse_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 13),
    _JnxSurvivableStatsMaxResponse_Type()
)
jnxSurvivableStatsMaxResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSurvivableStatsMaxResponse.setStatus("current")
_JnxSurvivableStatsAvgResponse_Type = Unsigned32
_JnxSurvivableStatsAvgResponse_Object = MibTableColumn
jnxSurvivableStatsAvgResponse = _JnxSurvivableStatsAvgResponse_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 1, 1, 14, 1, 14),
    _JnxSurvivableStatsAvgResponse_Type()
)
jnxSurvivableStatsAvgResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSurvivableStatsAvgResponse.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-RTM-MIB",
    **{"jnxRtmMIB": jnxRtmMIB,
       "jnxRtmMIBObjects": jnxRtmMIBObjects,
       "jnxSipTemplateTable": jnxSipTemplateTable,
       "jnxSipTemplateEntry": jnxSipTemplateEntry,
       "jnxSipTemplateName": jnxSipTemplateName,
       "jnxDtmfMethod": jnxDtmfMethod,
       "jnxCallerIdTransmit": jnxCallerIdTransmit,
       "jnxInheritExtensionsFrom": jnxInheritExtensionsFrom,
       "jnxInheritExtensionsTo": jnxInheritExtensionsTo,
       "jnxClassOfRestriction": jnxClassOfRestriction,
       "jnxCodecG711MU": jnxCodecG711MU,
       "jnxCodecG711A": jnxCodecG711A,
       "jnxCodecG729AB": jnxCodecG729AB,
       "jnxAnalogTemplateTable": jnxAnalogTemplateTable,
       "jnxAnalogTemplateEntry": jnxAnalogTemplateEntry,
       "jnxAnalogTemplateName": jnxAnalogTemplateName,
       "jnxAanalogCallerIdTransmit": jnxAanalogCallerIdTransmit,
       "jnxAnalogVoiceActivityDetection": jnxAnalogVoiceActivityDetection,
       "jnxAnalogComfortNoiseGeneration": jnxAnalogComfortNoiseGeneration,
       "jnxAnalogClassOfRestriction": jnxAnalogClassOfRestriction,
       "jnxStationTable": jnxStationTable,
       "jnxStationEntry": jnxStationEntry,
       "jnxStationName": jnxStationName,
       "jnxStationExtension": jnxStationExtension,
       "jnxStationRestriction": jnxStationRestriction,
       "jnxStationCallerId": jnxStationCallerId,
       "jnxStationDID": jnxStationDID,
       "jnxStationDILTdmInterface": jnxStationDILTdmInterface,
       "jnxStationDILTimeSlotNumber": jnxStationDILTimeSlotNumber,
       "jnxStationAuthId": jnxStationAuthId,
       "jnxStationType": jnxStationType,
       "jnxStationTemplate": jnxStationTemplate,
       "jnxStationTdmInterface": jnxStationTdmInterface,
       "jnxStationTimeSlotNumber": jnxStationTimeSlotNumber,
       "jnxSurvivableCallServiceTable": jnxSurvivableCallServiceTable,
       "jnxSurvivableCallServiceEntry": jnxSurvivableCallServiceEntry,
       "jnxSurvivableCallServiceName": jnxSurvivableCallServiceName,
       "jnxSurvivableCallServicePeerCallServer": jnxSurvivableCallServicePeerCallServer,
       "jnxSurvivableCallServiceSipProtocolPort": jnxSurvivableCallServiceSipProtocolPort,
       "jnxSurvivableCallServiceSipProtocolTransport": jnxSurvivableCallServiceSipProtocolTransport,
       "jnxSurvivableCallServiceHeartbeatNormalInterval": jnxSurvivableCallServiceHeartbeatNormalInterval,
       "jnxSurvivableCallServiceRegistrationExpiryTimeout": jnxSurvivableCallServiceRegistrationExpiryTimeout,
       "jnxSurvivableCallServiceSipTimeout": jnxSurvivableCallServiceSipTimeout,
       "jnxSurvivableCallServiceMonitorTimeout": jnxSurvivableCallServiceMonitorTimeout,
       "jnxSurvivableCallServiceHeartbeatSurvivableInterval": jnxSurvivableCallServiceHeartbeatSurvivableInterval,
       "jnxSurvivableCallServiceResponseThresholdMinimum": jnxSurvivableCallServiceResponseThresholdMinimum,
       "jnxSurvivableCallServiceServicePointZone": jnxSurvivableCallServiceServicePointZone,
       "jnxSurvivableCallServiceDialPlan": jnxSurvivableCallServiceDialPlan,
       "jnxTrunkConfigTable": jnxTrunkConfigTable,
       "jnxTrunkConfigEntry": jnxTrunkConfigEntry,
       "jnxTrunkConfigName": jnxTrunkConfigName,
       "jnxTrunkConfigType": jnxTrunkConfigType,
       "jnxTrunkConfigTdmInterface": jnxTrunkConfigTdmInterface,
       "jnxTrunkConfigT1CasGroupTimeSlots": jnxTrunkConfigT1CasGroupTimeSlots,
       "jnxTrunkConfigT1CasGroupSignaling": jnxTrunkConfigT1CasGroupSignaling,
       "jnxDigitManipulationTable": jnxDigitManipulationTable,
       "jnxDigitManipulationEntry": jnxDigitManipulationEntry,
       "jnxDigitTransformName": jnxDigitTransformName,
       "jnxDigitTransformRegularExpression": jnxDigitTransformRegularExpression,
       "jnxPeerCallServerTable": jnxPeerCallServerTable,
       "jnxPeerCallServerEntry": jnxPeerCallServerEntry,
       "jnxPeerCallServerName": jnxPeerCallServerName,
       "jnxPeerCallServerDescription": jnxPeerCallServerDescription,
       "jnxPeerCallServerAddress": jnxPeerCallServerAddress,
       "jnxPeerCallServerSipProtocolPort": jnxPeerCallServerSipProtocolPort,
       "jnxPeerCallServerSipProtocolTransport": jnxPeerCallServerSipProtocolTransport,
       "jnxPeerCallServerCodecG711MU": jnxPeerCallServerCodecG711MU,
       "jnxPeerCallServerCodecG711A": jnxPeerCallServerCodecG711A,
       "jnxPeerCallServerCodecG729AB": jnxPeerCallServerCodecG729AB,
       "jnxPeerCallServerDtmfMethod": jnxPeerCallServerDtmfMethod,
       "jnxPeerCallServerPstnAccessNumber": jnxPeerCallServerPstnAccessNumber,
       "jnxPeerCallServerAuthId": jnxPeerCallServerAuthId,
       "jnxFeatures": jnxFeatures,
       "jnxFeaturesLiveAttendantExtension": jnxFeaturesLiveAttendantExtension,
       "jnxFeaturesLiveAttendantStartTime": jnxFeaturesLiveAttendantStartTime,
       "jnxFeaturesLiveAttendantEndTime": jnxFeaturesLiveAttendantEndTime,
       "jnxFeaturesAttendantRingCount": jnxFeaturesAttendantRingCount,
       "jnxFeaturesVoicemailExtension": jnxFeaturesVoicemailExtension,
       "jnxFeaturesVoicemailRemoteAccessNumber": jnxFeaturesVoicemailRemoteAccessNumber,
       "jnxDialPlanTable": jnxDialPlanTable,
       "jnxDialPlanEntry": jnxDialPlanEntry,
       "jnxDialPlanName": jnxDialPlanName,
       "jnxDialPlanDigitPattern": jnxDialPlanDigitPattern,
       "jnxDialPlanCallType": jnxDialPlanCallType,
       "jnxDialPlanTrunkGroupList": jnxDialPlanTrunkGroupList,
       "jnxClassOfRestrictionTable": jnxClassOfRestrictionTable,
       "jnxClassOfRestrictionEntry": jnxClassOfRestrictionEntry,
       "jnxClassOfRestrictionName": jnxClassOfRestrictionName,
       "jnxRestrictionPolicyName": jnxRestrictionPolicyName,
       "jnxRestrictionCallType": jnxRestrictionCallType,
       "jnxRestrictionCallPermission": jnxRestrictionCallPermission,
       "jnxMediaGatewayTable": jnxMediaGatewayTable,
       "jnxMediaGatewayEntry": jnxMediaGatewayEntry,
       "jnxMediaGatewayName": jnxMediaGatewayName,
       "jnxMediaGatewayPeerCallServer": jnxMediaGatewayPeerCallServer,
       "jnxMediaGatewaySipProtocolPort": jnxMediaGatewaySipProtocolPort,
       "jnxMediaGatewaySipProtocolTransport": jnxMediaGatewaySipProtocolTransport,
       "jnxMediaGatewayDialPlan": jnxMediaGatewayDialPlan,
       "jnxTrunkGroupTable": jnxTrunkGroupTable,
       "jnxTrunkGroupEntry": jnxTrunkGroupEntry,
       "jnxTrunkGroupName": jnxTrunkGroupName,
       "jnxTrunkGroupDescription": jnxTrunkGroupDescription,
       "jnxTrunkGroupTrunkList": jnxTrunkGroupTrunkList,
       "jnxSurvivableStatsTable": jnxSurvivableStatsTable,
       "jnxSurvivableStatsEntry": jnxSurvivableStatsEntry,
       "jnxSurvivableStatsAddress": jnxSurvivableStatsAddress,
       "jnxSurvivableStatsPort": jnxSurvivableStatsPort,
       "jnxSurvivableStatsTransport": jnxSurvivableStatsTransport,
       "jnxSurvivableStatsSCSName": jnxSurvivableStatsSCSName,
       "jnxSurvivableStatsPeerCallServer": jnxSurvivableStatsPeerCallServer,
       "jnxSurvivableStatsCurrentState": jnxSurvivableStatsCurrentState,
       "jnxSurvivableStatsPriority": jnxSurvivableStatsPriority,
       "jnxSurvivableStatsLastDownTime": jnxSurvivableStatsLastDownTime,
       "jnxSurvivableStatsLastDownLen": jnxSurvivableStatsLastDownLen,
       "jnxSurvivableStatsTotalDownTime": jnxSurvivableStatsTotalDownTime,
       "jnxSurvivableStatsTimesDown": jnxSurvivableStatsTimesDown,
       "jnxSurvivableStatsMinResponse": jnxSurvivableStatsMinResponse,
       "jnxSurvivableStatsMaxResponse": jnxSurvivableStatsMaxResponse,
       "jnxSurvivableStatsAvgResponse": jnxSurvivableStatsAvgResponse}
)
