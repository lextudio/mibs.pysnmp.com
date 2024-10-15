# SNMP MIB module (ASCEND-MIBTRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBTRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:29 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibtrapProfile_ObjectIdentity = ObjectIdentity
mibtrapProfile = _MibtrapProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 132)
)
_MibtrapProfileTable_Object = MibTable
mibtrapProfileTable = _MibtrapProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1)
)
if mibBuilder.loadTexts:
    mibtrapProfileTable.setStatus("mandatory")
_MibtrapProfileEntry_Object = MibTableRow
mibtrapProfileEntry = _MibtrapProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1)
)
mibtrapProfileEntry.setIndexNames(
    (0, "ASCEND-MIBTRAP-MIB", "trapProfile-HostName"),
)
if mibBuilder.loadTexts:
    mibtrapProfileEntry.setStatus("mandatory")
_TrapProfile_HostName_Type = DisplayString
_TrapProfile_HostName_Object = MibScalar
trapProfile_HostName = _TrapProfile_HostName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 1),
    _TrapProfile_HostName_Type()
)
trapProfile_HostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapProfile_HostName.setStatus("mandatory")


class _TrapProfile_ActiveEnabled_Type(Integer32):
    """Custom type trapProfile_ActiveEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_ActiveEnabled_Type.__name__ = "Integer32"
_TrapProfile_ActiveEnabled_Object = MibScalar
trapProfile_ActiveEnabled = _TrapProfile_ActiveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 2),
    _TrapProfile_ActiveEnabled_Type()
)
trapProfile_ActiveEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_ActiveEnabled.setStatus("mandatory")
_TrapProfile_CommunityName_Type = DisplayString
_TrapProfile_CommunityName_Object = MibScalar
trapProfile_CommunityName = _TrapProfile_CommunityName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 3),
    _TrapProfile_CommunityName_Type()
)
trapProfile_CommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_CommunityName.setStatus("mandatory")
_TrapProfile_HostAddress_Type = IpAddress
_TrapProfile_HostAddress_Object = MibScalar
trapProfile_HostAddress = _TrapProfile_HostAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 4),
    _TrapProfile_HostAddress_Type()
)
trapProfile_HostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_HostAddress.setStatus("mandatory")
_TrapProfile_HostPort_Type = Integer32
_TrapProfile_HostPort_Object = MibScalar
trapProfile_HostPort = _TrapProfile_HostPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 5),
    _TrapProfile_HostPort_Type()
)
trapProfile_HostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_HostPort.setStatus("mandatory")
_TrapProfile_InformTimeOut_Type = Integer32
_TrapProfile_InformTimeOut_Object = MibScalar
trapProfile_InformTimeOut = _TrapProfile_InformTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 6),
    _TrapProfile_InformTimeOut_Type()
)
trapProfile_InformTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapProfile_InformTimeOut.setStatus("mandatory")
_TrapProfile_InformRetryCount_Type = Integer32
_TrapProfile_InformRetryCount_Object = MibScalar
trapProfile_InformRetryCount = _TrapProfile_InformRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 7),
    _TrapProfile_InformRetryCount_Type()
)
trapProfile_InformRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapProfile_InformRetryCount.setStatus("mandatory")
_TrapProfile_NotifyTagList_Type = OctetString
_TrapProfile_NotifyTagList_Object = MibScalar
trapProfile_NotifyTagList = _TrapProfile_NotifyTagList_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 8),
    _TrapProfile_NotifyTagList_Type()
)
trapProfile_NotifyTagList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_NotifyTagList.setStatus("mandatory")
_TrapProfile_TargetParamsName_Type = OctetString
_TrapProfile_TargetParamsName_Object = MibScalar
trapProfile_TargetParamsName = _TrapProfile_TargetParamsName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 9),
    _TrapProfile_TargetParamsName_Type()
)
trapProfile_TargetParamsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_TargetParamsName.setStatus("mandatory")
_TrapProfile_AgentAddress_Type = IpAddress
_TrapProfile_AgentAddress_Object = MibScalar
trapProfile_AgentAddress = _TrapProfile_AgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 10),
    _TrapProfile_AgentAddress_Type()
)
trapProfile_AgentAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_AgentAddress.setStatus("mandatory")


class _TrapProfile_AlarmEnabled_Type(Integer32):
    """Custom type trapProfile_AlarmEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_AlarmEnabled_Type.__name__ = "Integer32"
_TrapProfile_AlarmEnabled_Object = MibScalar
trapProfile_AlarmEnabled = _TrapProfile_AlarmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 11),
    _TrapProfile_AlarmEnabled_Type()
)
trapProfile_AlarmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_AlarmEnabled.setStatus("mandatory")


class _TrapProfile_SecurityEnabled_Type(Integer32):
    """Custom type trapProfile_SecurityEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_SecurityEnabled_Type.__name__ = "Integer32"
_TrapProfile_SecurityEnabled_Object = MibScalar
trapProfile_SecurityEnabled = _TrapProfile_SecurityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 12),
    _TrapProfile_SecurityEnabled_Type()
)
trapProfile_SecurityEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_SecurityEnabled.setStatus("mandatory")


class _TrapProfile_PortEnabled_Type(Integer32):
    """Custom type trapProfile_PortEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_PortEnabled_Type.__name__ = "Integer32"
_TrapProfile_PortEnabled_Object = MibScalar
trapProfile_PortEnabled = _TrapProfile_PortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 13),
    _TrapProfile_PortEnabled_Type()
)
trapProfile_PortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_PortEnabled.setStatus("mandatory")


class _TrapProfile_SlotEnabled_Type(Integer32):
    """Custom type trapProfile_SlotEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_SlotEnabled_Type.__name__ = "Integer32"
_TrapProfile_SlotEnabled_Object = MibScalar
trapProfile_SlotEnabled = _TrapProfile_SlotEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 14),
    _TrapProfile_SlotEnabled_Type()
)
trapProfile_SlotEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_SlotEnabled.setStatus("mandatory")


class _TrapProfile_ColdstartEnabled_Type(Integer32):
    """Custom type trapProfile_ColdstartEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_ColdstartEnabled_Type.__name__ = "Integer32"
_TrapProfile_ColdstartEnabled_Object = MibScalar
trapProfile_ColdstartEnabled = _TrapProfile_ColdstartEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 15),
    _TrapProfile_ColdstartEnabled_Type()
)
trapProfile_ColdstartEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_ColdstartEnabled.setStatus("mandatory")


class _TrapProfile_WarmstartEnabled_Type(Integer32):
    """Custom type trapProfile_WarmstartEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_WarmstartEnabled_Type.__name__ = "Integer32"
_TrapProfile_WarmstartEnabled_Object = MibScalar
trapProfile_WarmstartEnabled = _TrapProfile_WarmstartEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 16),
    _TrapProfile_WarmstartEnabled_Type()
)
trapProfile_WarmstartEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_WarmstartEnabled.setStatus("mandatory")


class _TrapProfile_LinkdownEnabled_Type(Integer32):
    """Custom type trapProfile_LinkdownEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_LinkdownEnabled_Type.__name__ = "Integer32"
_TrapProfile_LinkdownEnabled_Object = MibScalar
trapProfile_LinkdownEnabled = _TrapProfile_LinkdownEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 17),
    _TrapProfile_LinkdownEnabled_Type()
)
trapProfile_LinkdownEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_LinkdownEnabled.setStatus("mandatory")


class _TrapProfile_LinkupEnabled_Type(Integer32):
    """Custom type trapProfile_LinkupEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_LinkupEnabled_Type.__name__ = "Integer32"
_TrapProfile_LinkupEnabled_Object = MibScalar
trapProfile_LinkupEnabled = _TrapProfile_LinkupEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 18),
    _TrapProfile_LinkupEnabled_Type()
)
trapProfile_LinkupEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_LinkupEnabled.setStatus("mandatory")


class _TrapProfile_AscendEnabled_Type(Integer32):
    """Custom type trapProfile_AscendEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_AscendEnabled_Type.__name__ = "Integer32"
_TrapProfile_AscendEnabled_Object = MibScalar
trapProfile_AscendEnabled = _TrapProfile_AscendEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 19),
    _TrapProfile_AscendEnabled_Type()
)
trapProfile_AscendEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_AscendEnabled.setStatus("mandatory")


class _TrapProfile_ConsoleEnabled_Type(Integer32):
    """Custom type trapProfile_ConsoleEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_ConsoleEnabled_Type.__name__ = "Integer32"
_TrapProfile_ConsoleEnabled_Object = MibScalar
trapProfile_ConsoleEnabled = _TrapProfile_ConsoleEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 20),
    _TrapProfile_ConsoleEnabled_Type()
)
trapProfile_ConsoleEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_ConsoleEnabled.setStatus("mandatory")


class _TrapProfile_UseExceededEnabled_Type(Integer32):
    """Custom type trapProfile_UseExceededEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_UseExceededEnabled_Type.__name__ = "Integer32"
_TrapProfile_UseExceededEnabled_Object = MibScalar
trapProfile_UseExceededEnabled = _TrapProfile_UseExceededEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 21),
    _TrapProfile_UseExceededEnabled_Type()
)
trapProfile_UseExceededEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_UseExceededEnabled.setStatus("mandatory")


class _TrapProfile_PasswordEnabled_Type(Integer32):
    """Custom type trapProfile_PasswordEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_PasswordEnabled_Type.__name__ = "Integer32"
_TrapProfile_PasswordEnabled_Object = MibScalar
trapProfile_PasswordEnabled = _TrapProfile_PasswordEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 22),
    _TrapProfile_PasswordEnabled_Type()
)
trapProfile_PasswordEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_PasswordEnabled.setStatus("mandatory")


class _TrapProfile_FrLinkupEnabled_Type(Integer32):
    """Custom type trapProfile_FrLinkupEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_FrLinkupEnabled_Type.__name__ = "Integer32"
_TrapProfile_FrLinkupEnabled_Object = MibScalar
trapProfile_FrLinkupEnabled = _TrapProfile_FrLinkupEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 23),
    _TrapProfile_FrLinkupEnabled_Type()
)
trapProfile_FrLinkupEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_FrLinkupEnabled.setStatus("mandatory")


class _TrapProfile_FrLinkdownEnabled_Type(Integer32):
    """Custom type trapProfile_FrLinkdownEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_FrLinkdownEnabled_Type.__name__ = "Integer32"
_TrapProfile_FrLinkdownEnabled_Object = MibScalar
trapProfile_FrLinkdownEnabled = _TrapProfile_FrLinkdownEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 24),
    _TrapProfile_FrLinkdownEnabled_Type()
)
trapProfile_FrLinkdownEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_FrLinkdownEnabled.setStatus("mandatory")


class _TrapProfile_EventOverwriteEnabled_Type(Integer32):
    """Custom type trapProfile_EventOverwriteEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_EventOverwriteEnabled_Type.__name__ = "Integer32"
_TrapProfile_EventOverwriteEnabled_Object = MibScalar
trapProfile_EventOverwriteEnabled = _TrapProfile_EventOverwriteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 25),
    _TrapProfile_EventOverwriteEnabled_Type()
)
trapProfile_EventOverwriteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_EventOverwriteEnabled.setStatus("mandatory")


class _TrapProfile_RadiusChangeEnabled_Type(Integer32):
    """Custom type trapProfile_RadiusChangeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_RadiusChangeEnabled_Type.__name__ = "Integer32"
_TrapProfile_RadiusChangeEnabled_Object = MibScalar
trapProfile_RadiusChangeEnabled = _TrapProfile_RadiusChangeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 26),
    _TrapProfile_RadiusChangeEnabled_Type()
)
trapProfile_RadiusChangeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_RadiusChangeEnabled.setStatus("mandatory")


class _TrapProfile_McastMonitorEnabled_Type(Integer32):
    """Custom type trapProfile_McastMonitorEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_McastMonitorEnabled_Type.__name__ = "Integer32"
_TrapProfile_McastMonitorEnabled_Object = MibScalar
trapProfile_McastMonitorEnabled = _TrapProfile_McastMonitorEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 27),
    _TrapProfile_McastMonitorEnabled_Type()
)
trapProfile_McastMonitorEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_McastMonitorEnabled.setStatus("mandatory")


class _TrapProfile_LanModemEnabled_Type(Integer32):
    """Custom type trapProfile_LanModemEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_LanModemEnabled_Type.__name__ = "Integer32"
_TrapProfile_LanModemEnabled_Object = MibScalar
trapProfile_LanModemEnabled = _TrapProfile_LanModemEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 28),
    _TrapProfile_LanModemEnabled_Type()
)
trapProfile_LanModemEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_LanModemEnabled.setStatus("mandatory")


class _TrapProfile_DirdoEnabled_Type(Integer32):
    """Custom type trapProfile_DirdoEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_DirdoEnabled_Type.__name__ = "Integer32"
_TrapProfile_DirdoEnabled_Object = MibScalar
trapProfile_DirdoEnabled = _TrapProfile_DirdoEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 29),
    _TrapProfile_DirdoEnabled_Type()
)
trapProfile_DirdoEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_DirdoEnabled.setStatus("mandatory")


class _TrapProfile_SlotProfileChangeEnabled_Type(Integer32):
    """Custom type trapProfile_SlotProfileChangeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_SlotProfileChangeEnabled_Type.__name__ = "Integer32"
_TrapProfile_SlotProfileChangeEnabled_Object = MibScalar
trapProfile_SlotProfileChangeEnabled = _TrapProfile_SlotProfileChangeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 30),
    _TrapProfile_SlotProfileChangeEnabled_Type()
)
trapProfile_SlotProfileChangeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_SlotProfileChangeEnabled.setStatus("mandatory")


class _TrapProfile_PowerSupplyEnabled_Type(Integer32):
    """Custom type trapProfile_PowerSupplyEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_PowerSupplyEnabled_Type.__name__ = "Integer32"
_TrapProfile_PowerSupplyEnabled_Object = MibScalar
trapProfile_PowerSupplyEnabled = _TrapProfile_PowerSupplyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 31),
    _TrapProfile_PowerSupplyEnabled_Type()
)
trapProfile_PowerSupplyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_PowerSupplyEnabled.setStatus("mandatory")


class _TrapProfile_MultishelfEnabled_Type(Integer32):
    """Custom type trapProfile_MultishelfEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_MultishelfEnabled_Type.__name__ = "Integer32"
_TrapProfile_MultishelfEnabled_Object = MibScalar
trapProfile_MultishelfEnabled = _TrapProfile_MultishelfEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 32),
    _TrapProfile_MultishelfEnabled_Type()
)
trapProfile_MultishelfEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_MultishelfEnabled.setStatus("mandatory")


class _TrapProfile_AuthenticationEnabled_Type(Integer32):
    """Custom type trapProfile_AuthenticationEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_AuthenticationEnabled_Type.__name__ = "Integer32"
_TrapProfile_AuthenticationEnabled_Object = MibScalar
trapProfile_AuthenticationEnabled = _TrapProfile_AuthenticationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 33),
    _TrapProfile_AuthenticationEnabled_Type()
)
trapProfile_AuthenticationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_AuthenticationEnabled.setStatus("mandatory")


class _TrapProfile_ConfigChangeEnabled_Type(Integer32):
    """Custom type trapProfile_ConfigChangeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_ConfigChangeEnabled_Type.__name__ = "Integer32"
_TrapProfile_ConfigChangeEnabled_Object = MibScalar
trapProfile_ConfigChangeEnabled = _TrapProfile_ConfigChangeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 34),
    _TrapProfile_ConfigChangeEnabled_Type()
)
trapProfile_ConfigChangeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_ConfigChangeEnabled.setStatus("mandatory")


class _TrapProfile_SysClockDriftEnabled_Type(Integer32):
    """Custom type trapProfile_SysClockDriftEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_SysClockDriftEnabled_Type.__name__ = "Integer32"
_TrapProfile_SysClockDriftEnabled_Object = MibScalar
trapProfile_SysClockDriftEnabled = _TrapProfile_SysClockDriftEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 35),
    _TrapProfile_SysClockDriftEnabled_Type()
)
trapProfile_SysClockDriftEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_SysClockDriftEnabled.setStatus("mandatory")


class _TrapProfile_PrimarySdtnEmptyEnabled_Type(Integer32):
    """Custom type trapProfile_PrimarySdtnEmptyEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_PrimarySdtnEmptyEnabled_Type.__name__ = "Integer32"
_TrapProfile_PrimarySdtnEmptyEnabled_Object = MibScalar
trapProfile_PrimarySdtnEmptyEnabled = _TrapProfile_PrimarySdtnEmptyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 36),
    _TrapProfile_PrimarySdtnEmptyEnabled_Type()
)
trapProfile_PrimarySdtnEmptyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_PrimarySdtnEmptyEnabled.setStatus("mandatory")


class _TrapProfile_SecondarySdtnEmptyEnabled_Type(Integer32):
    """Custom type trapProfile_SecondarySdtnEmptyEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_SecondarySdtnEmptyEnabled_Type.__name__ = "Integer32"
_TrapProfile_SecondarySdtnEmptyEnabled_Object = MibScalar
trapProfile_SecondarySdtnEmptyEnabled = _TrapProfile_SecondarySdtnEmptyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 37),
    _TrapProfile_SecondarySdtnEmptyEnabled_Type()
)
trapProfile_SecondarySdtnEmptyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_SecondarySdtnEmptyEnabled.setStatus("mandatory")


class _TrapProfile_SuspectAccessResourceEnabled_Type(Integer32):
    """Custom type trapProfile_SuspectAccessResourceEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_SuspectAccessResourceEnabled_Type.__name__ = "Integer32"
_TrapProfile_SuspectAccessResourceEnabled_Object = MibScalar
trapProfile_SuspectAccessResourceEnabled = _TrapProfile_SuspectAccessResourceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 38),
    _TrapProfile_SuspectAccessResourceEnabled_Type()
)
trapProfile_SuspectAccessResourceEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_SuspectAccessResourceEnabled.setStatus("mandatory")


class _TrapProfile_OspfEnabled_Type(Integer32):
    """Custom type trapProfile_OspfEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_OspfEnabled_Type.__name__ = "Integer32"
_TrapProfile_OspfEnabled_Object = MibScalar
trapProfile_OspfEnabled = _TrapProfile_OspfEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 39),
    _TrapProfile_OspfEnabled_Type()
)
trapProfile_OspfEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_OspfEnabled.setStatus("mandatory")


class _TrapProfile_OspfIfConfigErrorEnabled_Type(Integer32):
    """Custom type trapProfile_OspfIfConfigErrorEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_OspfIfConfigErrorEnabled_Type.__name__ = "Integer32"
_TrapProfile_OspfIfConfigErrorEnabled_Object = MibScalar
trapProfile_OspfIfConfigErrorEnabled = _TrapProfile_OspfIfConfigErrorEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 40),
    _TrapProfile_OspfIfConfigErrorEnabled_Type()
)
trapProfile_OspfIfConfigErrorEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_OspfIfConfigErrorEnabled.setStatus("mandatory")


class _TrapProfile_OspfIfAuthFailureEnabled_Type(Integer32):
    """Custom type trapProfile_OspfIfAuthFailureEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_OspfIfAuthFailureEnabled_Type.__name__ = "Integer32"
_TrapProfile_OspfIfAuthFailureEnabled_Object = MibScalar
trapProfile_OspfIfAuthFailureEnabled = _TrapProfile_OspfIfAuthFailureEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 41),
    _TrapProfile_OspfIfAuthFailureEnabled_Type()
)
trapProfile_OspfIfAuthFailureEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_OspfIfAuthFailureEnabled.setStatus("mandatory")


class _TrapProfile_OspfIfStateChangeEnabled_Type(Integer32):
    """Custom type trapProfile_OspfIfStateChangeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_OspfIfStateChangeEnabled_Type.__name__ = "Integer32"
_TrapProfile_OspfIfStateChangeEnabled_Object = MibScalar
trapProfile_OspfIfStateChangeEnabled = _TrapProfile_OspfIfStateChangeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 42),
    _TrapProfile_OspfIfStateChangeEnabled_Type()
)
trapProfile_OspfIfStateChangeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_OspfIfStateChangeEnabled.setStatus("mandatory")


class _TrapProfile_OspfIfRxBadPacket_Type(Integer32):
    """Custom type trapProfile_OspfIfRxBadPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_OspfIfRxBadPacket_Type.__name__ = "Integer32"
_TrapProfile_OspfIfRxBadPacket_Object = MibScalar
trapProfile_OspfIfRxBadPacket = _TrapProfile_OspfIfRxBadPacket_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 43),
    _TrapProfile_OspfIfRxBadPacket_Type()
)
trapProfile_OspfIfRxBadPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_OspfIfRxBadPacket.setStatus("mandatory")


class _TrapProfile_OspfTxRetransmitEnabled_Type(Integer32):
    """Custom type trapProfile_OspfTxRetransmitEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_OspfTxRetransmitEnabled_Type.__name__ = "Integer32"
_TrapProfile_OspfTxRetransmitEnabled_Object = MibScalar
trapProfile_OspfTxRetransmitEnabled = _TrapProfile_OspfTxRetransmitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 44),
    _TrapProfile_OspfTxRetransmitEnabled_Type()
)
trapProfile_OspfTxRetransmitEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_OspfTxRetransmitEnabled.setStatus("mandatory")


class _TrapProfile_OspfNbrStateChangeEnabled_Type(Integer32):
    """Custom type trapProfile_OspfNbrStateChangeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_OspfNbrStateChangeEnabled_Type.__name__ = "Integer32"
_TrapProfile_OspfNbrStateChangeEnabled_Object = MibScalar
trapProfile_OspfNbrStateChangeEnabled = _TrapProfile_OspfNbrStateChangeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 45),
    _TrapProfile_OspfNbrStateChangeEnabled_Type()
)
trapProfile_OspfNbrStateChangeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_OspfNbrStateChangeEnabled.setStatus("mandatory")


class _TrapProfile_OspfVirtIfConfigErrorEnabled_Type(Integer32):
    """Custom type trapProfile_OspfVirtIfConfigErrorEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_OspfVirtIfConfigErrorEnabled_Type.__name__ = "Integer32"
_TrapProfile_OspfVirtIfConfigErrorEnabled_Object = MibScalar
trapProfile_OspfVirtIfConfigErrorEnabled = _TrapProfile_OspfVirtIfConfigErrorEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 46),
    _TrapProfile_OspfVirtIfConfigErrorEnabled_Type()
)
trapProfile_OspfVirtIfConfigErrorEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_OspfVirtIfConfigErrorEnabled.setStatus("mandatory")


class _TrapProfile_OspfVirtIfAuthFailureEnabled_Type(Integer32):
    """Custom type trapProfile_OspfVirtIfAuthFailureEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_OspfVirtIfAuthFailureEnabled_Type.__name__ = "Integer32"
_TrapProfile_OspfVirtIfAuthFailureEnabled_Object = MibScalar
trapProfile_OspfVirtIfAuthFailureEnabled = _TrapProfile_OspfVirtIfAuthFailureEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 47),
    _TrapProfile_OspfVirtIfAuthFailureEnabled_Type()
)
trapProfile_OspfVirtIfAuthFailureEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_OspfVirtIfAuthFailureEnabled.setStatus("mandatory")


class _TrapProfile_OspfVirtIfStateChangeEnabled_Type(Integer32):
    """Custom type trapProfile_OspfVirtIfStateChangeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_OspfVirtIfStateChangeEnabled_Type.__name__ = "Integer32"
_TrapProfile_OspfVirtIfStateChangeEnabled_Object = MibScalar
trapProfile_OspfVirtIfStateChangeEnabled = _TrapProfile_OspfVirtIfStateChangeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 48),
    _TrapProfile_OspfVirtIfStateChangeEnabled_Type()
)
trapProfile_OspfVirtIfStateChangeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_OspfVirtIfStateChangeEnabled.setStatus("mandatory")


class _TrapProfile_OspfVirtIfRxBadPacket_Type(Integer32):
    """Custom type trapProfile_OspfVirtIfRxBadPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_OspfVirtIfRxBadPacket_Type.__name__ = "Integer32"
_TrapProfile_OspfVirtIfRxBadPacket_Object = MibScalar
trapProfile_OspfVirtIfRxBadPacket = _TrapProfile_OspfVirtIfRxBadPacket_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 49),
    _TrapProfile_OspfVirtIfRxBadPacket_Type()
)
trapProfile_OspfVirtIfRxBadPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_OspfVirtIfRxBadPacket.setStatus("mandatory")


class _TrapProfile_OspfVirtIfTxRetransmitEnabled_Type(Integer32):
    """Custom type trapProfile_OspfVirtIfTxRetransmitEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_OspfVirtIfTxRetransmitEnabled_Type.__name__ = "Integer32"
_TrapProfile_OspfVirtIfTxRetransmitEnabled_Object = MibScalar
trapProfile_OspfVirtIfTxRetransmitEnabled = _TrapProfile_OspfVirtIfTxRetransmitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 50),
    _TrapProfile_OspfVirtIfTxRetransmitEnabled_Type()
)
trapProfile_OspfVirtIfTxRetransmitEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_OspfVirtIfTxRetransmitEnabled.setStatus("mandatory")


class _TrapProfile_OspfVirtNbrStateChangeEnabled_Type(Integer32):
    """Custom type trapProfile_OspfVirtNbrStateChangeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_OspfVirtNbrStateChangeEnabled_Type.__name__ = "Integer32"
_TrapProfile_OspfVirtNbrStateChangeEnabled_Object = MibScalar
trapProfile_OspfVirtNbrStateChangeEnabled = _TrapProfile_OspfVirtNbrStateChangeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 51),
    _TrapProfile_OspfVirtNbrStateChangeEnabled_Type()
)
trapProfile_OspfVirtNbrStateChangeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_OspfVirtNbrStateChangeEnabled.setStatus("mandatory")


class _TrapProfile_OspfOriginateLsaEnabled_Type(Integer32):
    """Custom type trapProfile_OspfOriginateLsaEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_OspfOriginateLsaEnabled_Type.__name__ = "Integer32"
_TrapProfile_OspfOriginateLsaEnabled_Object = MibScalar
trapProfile_OspfOriginateLsaEnabled = _TrapProfile_OspfOriginateLsaEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 52),
    _TrapProfile_OspfOriginateLsaEnabled_Type()
)
trapProfile_OspfOriginateLsaEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_OspfOriginateLsaEnabled.setStatus("mandatory")


class _TrapProfile_OspfMaxAgeLsaEnabled_Type(Integer32):
    """Custom type trapProfile_OspfMaxAgeLsaEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_OspfMaxAgeLsaEnabled_Type.__name__ = "Integer32"
_TrapProfile_OspfMaxAgeLsaEnabled_Object = MibScalar
trapProfile_OspfMaxAgeLsaEnabled = _TrapProfile_OspfMaxAgeLsaEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 53),
    _TrapProfile_OspfMaxAgeLsaEnabled_Type()
)
trapProfile_OspfMaxAgeLsaEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_OspfMaxAgeLsaEnabled.setStatus("mandatory")


class _TrapProfile_OspfLsdbOverflowEnabled_Type(Integer32):
    """Custom type trapProfile_OspfLsdbOverflowEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_OspfLsdbOverflowEnabled_Type.__name__ = "Integer32"
_TrapProfile_OspfLsdbOverflowEnabled_Object = MibScalar
trapProfile_OspfLsdbOverflowEnabled = _TrapProfile_OspfLsdbOverflowEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 54),
    _TrapProfile_OspfLsdbOverflowEnabled_Type()
)
trapProfile_OspfLsdbOverflowEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_OspfLsdbOverflowEnabled.setStatus("mandatory")


class _TrapProfile_OspfApproachingOverflowEnabled_Type(Integer32):
    """Custom type trapProfile_OspfApproachingOverflowEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_OspfApproachingOverflowEnabled_Type.__name__ = "Integer32"
_TrapProfile_OspfApproachingOverflowEnabled_Object = MibScalar
trapProfile_OspfApproachingOverflowEnabled = _TrapProfile_OspfApproachingOverflowEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 55),
    _TrapProfile_OspfApproachingOverflowEnabled_Type()
)
trapProfile_OspfApproachingOverflowEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_OspfApproachingOverflowEnabled.setStatus("mandatory")


class _TrapProfile_WatchdogWarningEnabled_Type(Integer32):
    """Custom type trapProfile_WatchdogWarningEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_WatchdogWarningEnabled_Type.__name__ = "Integer32"
_TrapProfile_WatchdogWarningEnabled_Object = MibScalar
trapProfile_WatchdogWarningEnabled = _TrapProfile_WatchdogWarningEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 56),
    _TrapProfile_WatchdogWarningEnabled_Type()
)
trapProfile_WatchdogWarningEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_WatchdogWarningEnabled.setStatus("mandatory")


class _TrapProfile_ControllerSwitchoverEnabled_Type(Integer32):
    """Custom type trapProfile_ControllerSwitchoverEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_ControllerSwitchoverEnabled_Type.__name__ = "Integer32"
_TrapProfile_ControllerSwitchoverEnabled_Object = MibScalar
trapProfile_ControllerSwitchoverEnabled = _TrapProfile_ControllerSwitchoverEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 57),
    _TrapProfile_ControllerSwitchoverEnabled_Type()
)
trapProfile_ControllerSwitchoverEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_ControllerSwitchoverEnabled.setStatus("mandatory")


class _TrapProfile_CallLogServChangeEnabled_Type(Integer32):
    """Custom type trapProfile_CallLogServChangeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_CallLogServChangeEnabled_Type.__name__ = "Integer32"
_TrapProfile_CallLogServChangeEnabled_Object = MibScalar
trapProfile_CallLogServChangeEnabled = _TrapProfile_CallLogServChangeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 58),
    _TrapProfile_CallLogServChangeEnabled_Type()
)
trapProfile_CallLogServChangeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_CallLogServChangeEnabled.setStatus("mandatory")


class _TrapProfile_VoipGkChangeEnabled_Type(Integer32):
    """Custom type trapProfile_VoipGkChangeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_VoipGkChangeEnabled_Type.__name__ = "Integer32"
_TrapProfile_VoipGkChangeEnabled_Object = MibScalar
trapProfile_VoipGkChangeEnabled = _TrapProfile_VoipGkChangeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 59),
    _TrapProfile_VoipGkChangeEnabled_Type()
)
trapProfile_VoipGkChangeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_VoipGkChangeEnabled.setStatus("mandatory")


class _TrapProfile_WanLineStateChangeEnabled_Type(Integer32):
    """Custom type trapProfile_WanLineStateChangeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_WanLineStateChangeEnabled_Type.__name__ = "Integer32"
_TrapProfile_WanLineStateChangeEnabled_Object = MibScalar
trapProfile_WanLineStateChangeEnabled = _TrapProfile_WanLineStateChangeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 60),
    _TrapProfile_WanLineStateChangeEnabled_Type()
)
trapProfile_WanLineStateChangeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_WanLineStateChangeEnabled.setStatus("mandatory")


class _TrapProfile_CallLogDroppedPktEnabled_Type(Integer32):
    """Custom type trapProfile_CallLogDroppedPktEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_CallLogDroppedPktEnabled_Type.__name__ = "Integer32"
_TrapProfile_CallLogDroppedPktEnabled_Object = MibScalar
trapProfile_CallLogDroppedPktEnabled = _TrapProfile_CallLogDroppedPktEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 61),
    _TrapProfile_CallLogDroppedPktEnabled_Type()
)
trapProfile_CallLogDroppedPktEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_CallLogDroppedPktEnabled.setStatus("mandatory")


class _TrapProfile_LimSparingEnabled_Type(Integer32):
    """Custom type trapProfile_LimSparingEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_LimSparingEnabled_Type.__name__ = "Integer32"
_TrapProfile_LimSparingEnabled_Object = MibScalar
trapProfile_LimSparingEnabled = _TrapProfile_LimSparingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 62),
    _TrapProfile_LimSparingEnabled_Type()
)
trapProfile_LimSparingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_LimSparingEnabled.setStatus("mandatory")


class _TrapProfile_InterfaceSparingEnabled_Type(Integer32):
    """Custom type trapProfile_InterfaceSparingEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_InterfaceSparingEnabled_Type.__name__ = "Integer32"
_TrapProfile_InterfaceSparingEnabled_Object = MibScalar
trapProfile_InterfaceSparingEnabled = _TrapProfile_InterfaceSparingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 63),
    _TrapProfile_InterfaceSparingEnabled_Type()
)
trapProfile_InterfaceSparingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_InterfaceSparingEnabled.setStatus("mandatory")


class _TrapProfile_MegacoLinkStatusEnabled_Type(Integer32):
    """Custom type trapProfile_MegacoLinkStatusEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_MegacoLinkStatusEnabled_Type.__name__ = "Integer32"
_TrapProfile_MegacoLinkStatusEnabled_Object = MibScalar
trapProfile_MegacoLinkStatusEnabled = _TrapProfile_MegacoLinkStatusEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 64),
    _TrapProfile_MegacoLinkStatusEnabled_Type()
)
trapProfile_MegacoLinkStatusEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_MegacoLinkStatusEnabled.setStatus("mandatory")


class _TrapProfile_SecondaryControllerStateChangeEnabled_Type(Integer32):
    """Custom type trapProfile_SecondaryControllerStateChangeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_SecondaryControllerStateChangeEnabled_Type.__name__ = "Integer32"
_TrapProfile_SecondaryControllerStateChangeEnabled_Object = MibScalar
trapProfile_SecondaryControllerStateChangeEnabled = _TrapProfile_SecondaryControllerStateChangeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 65),
    _TrapProfile_SecondaryControllerStateChangeEnabled_Type()
)
trapProfile_SecondaryControllerStateChangeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_SecondaryControllerStateChangeEnabled.setStatus("mandatory")


class _TrapProfile_PctfiTrunkStatusChangeEnabled_Type(Integer32):
    """Custom type trapProfile_PctfiTrunkStatusChangeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_PctfiTrunkStatusChangeEnabled_Type.__name__ = "Integer32"
_TrapProfile_PctfiTrunkStatusChangeEnabled_Object = MibScalar
trapProfile_PctfiTrunkStatusChangeEnabled = _TrapProfile_PctfiTrunkStatusChangeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 66),
    _TrapProfile_PctfiTrunkStatusChangeEnabled_Type()
)
trapProfile_PctfiTrunkStatusChangeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_PctfiTrunkStatusChangeEnabled.setStatus("mandatory")


class _TrapProfile_NoResourceAvailableEnabled_Type(Integer32):
    """Custom type trapProfile_NoResourceAvailableEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_NoResourceAvailableEnabled_Type.__name__ = "Integer32"
_TrapProfile_NoResourceAvailableEnabled_Object = MibScalar
trapProfile_NoResourceAvailableEnabled = _TrapProfile_NoResourceAvailableEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 67),
    _TrapProfile_NoResourceAvailableEnabled_Type()
)
trapProfile_NoResourceAvailableEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_NoResourceAvailableEnabled.setStatus("mandatory")


class _TrapProfile_DslThreshTrapEnabled_Type(Integer32):
    """Custom type trapProfile_DslThreshTrapEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_DslThreshTrapEnabled_Type.__name__ = "Integer32"
_TrapProfile_DslThreshTrapEnabled_Object = MibScalar
trapProfile_DslThreshTrapEnabled = _TrapProfile_DslThreshTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 68),
    _TrapProfile_DslThreshTrapEnabled_Type()
)
trapProfile_DslThreshTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_DslThreshTrapEnabled.setStatus("mandatory")


class _TrapProfile_AtmPvcFailureTrapEnabled_Type(Integer32):
    """Custom type trapProfile_AtmPvcFailureTrapEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_AtmPvcFailureTrapEnabled_Type.__name__ = "Integer32"
_TrapProfile_AtmPvcFailureTrapEnabled_Object = MibScalar
trapProfile_AtmPvcFailureTrapEnabled = _TrapProfile_AtmPvcFailureTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 69),
    _TrapProfile_AtmPvcFailureTrapEnabled_Type()
)
trapProfile_AtmPvcFailureTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_AtmPvcFailureTrapEnabled.setStatus("mandatory")


class _TrapProfile_AtmImaAlarmTrapEnabled_Type(Integer32):
    """Custom type trapProfile_AtmImaAlarmTrapEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_AtmImaAlarmTrapEnabled_Type.__name__ = "Integer32"
_TrapProfile_AtmImaAlarmTrapEnabled_Object = MibScalar
trapProfile_AtmImaAlarmTrapEnabled = _TrapProfile_AtmImaAlarmTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 70),
    _TrapProfile_AtmImaAlarmTrapEnabled_Type()
)
trapProfile_AtmImaAlarmTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_AtmImaAlarmTrapEnabled.setStatus("mandatory")


class _TrapProfile_AscendLinkDownTrapEnabled_Type(Integer32):
    """Custom type trapProfile_AscendLinkDownTrapEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_AscendLinkDownTrapEnabled_Type.__name__ = "Integer32"
_TrapProfile_AscendLinkDownTrapEnabled_Object = MibScalar
trapProfile_AscendLinkDownTrapEnabled = _TrapProfile_AscendLinkDownTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 71),
    _TrapProfile_AscendLinkDownTrapEnabled_Type()
)
trapProfile_AscendLinkDownTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_AscendLinkDownTrapEnabled.setStatus("mandatory")


class _TrapProfile_AscendLinkUpTrapEnabled_Type(Integer32):
    """Custom type trapProfile_AscendLinkUpTrapEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_AscendLinkUpTrapEnabled_Type.__name__ = "Integer32"
_TrapProfile_AscendLinkUpTrapEnabled_Object = MibScalar
trapProfile_AscendLinkUpTrapEnabled = _TrapProfile_AscendLinkUpTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 72),
    _TrapProfile_AscendLinkUpTrapEnabled_Type()
)
trapProfile_AscendLinkUpTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_AscendLinkUpTrapEnabled.setStatus("mandatory")


class _TrapProfile_SnmpIllegalAccessAttempt_Type(Integer32):
    """Custom type trapProfile_SnmpIllegalAccessAttempt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_SnmpIllegalAccessAttempt_Type.__name__ = "Integer32"
_TrapProfile_SnmpIllegalAccessAttempt_Object = MibScalar
trapProfile_SnmpIllegalAccessAttempt = _TrapProfile_SnmpIllegalAccessAttempt_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 73),
    _TrapProfile_SnmpIllegalAccessAttempt_Type()
)
trapProfile_SnmpIllegalAccessAttempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_SnmpIllegalAccessAttempt.setStatus("mandatory")


class _TrapProfile_Action_o_Type(Integer32):
    """Custom type trapProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_TrapProfile_Action_o_Type.__name__ = "Integer32"
_TrapProfile_Action_o_Object = MibScalar
trapProfile_Action_o = _TrapProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 74),
    _TrapProfile_Action_o_Type()
)
trapProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_Action_o.setStatus("mandatory")


class _TrapProfile_NotificationLogEnable_Type(Integer32):
    """Custom type trapProfile_NotificationLogEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_NotificationLogEnable_Type.__name__ = "Integer32"
_TrapProfile_NotificationLogEnable_Object = MibScalar
trapProfile_NotificationLogEnable = _TrapProfile_NotificationLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 75),
    _TrapProfile_NotificationLogEnable_Type()
)
trapProfile_NotificationLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_NotificationLogEnable.setStatus("mandatory")
_TrapProfile_NotificationLogLimit_Type = Integer32
_TrapProfile_NotificationLogLimit_Object = MibScalar
trapProfile_NotificationLogLimit = _TrapProfile_NotificationLogLimit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 76),
    _TrapProfile_NotificationLogLimit_Type()
)
trapProfile_NotificationLogLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_NotificationLogLimit.setStatus("mandatory")


class _TrapProfile_Hdsl2ShdslThresholdTrapsEnabled_Type(Integer32):
    """Custom type trapProfile_Hdsl2ShdslThresholdTrapsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_Hdsl2ShdslThresholdTrapsEnabled_Type.__name__ = "Integer32"
_TrapProfile_Hdsl2ShdslThresholdTrapsEnabled_Object = MibScalar
trapProfile_Hdsl2ShdslThresholdTrapsEnabled = _TrapProfile_Hdsl2ShdslThresholdTrapsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 77),
    _TrapProfile_Hdsl2ShdslThresholdTrapsEnabled_Type()
)
trapProfile_Hdsl2ShdslThresholdTrapsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_Hdsl2ShdslThresholdTrapsEnabled.setStatus("mandatory")


class _TrapProfile_ClockChangeTrapEnabled_Type(Integer32):
    """Custom type trapProfile_ClockChangeTrapEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_ClockChangeTrapEnabled_Type.__name__ = "Integer32"
_TrapProfile_ClockChangeTrapEnabled_Object = MibScalar
trapProfile_ClockChangeTrapEnabled = _TrapProfile_ClockChangeTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 78),
    _TrapProfile_ClockChangeTrapEnabled_Type()
)
trapProfile_ClockChangeTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_ClockChangeTrapEnabled.setStatus("mandatory")


class _TrapProfile_L2tpTunnelTrapEnabled_Type(Integer32):
    """Custom type trapProfile_L2tpTunnelTrapEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrapProfile_L2tpTunnelTrapEnabled_Type.__name__ = "Integer32"
_TrapProfile_L2tpTunnelTrapEnabled_Object = MibScalar
trapProfile_L2tpTunnelTrapEnabled = _TrapProfile_L2tpTunnelTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 132, 1, 1, 79),
    _TrapProfile_L2tpTunnelTrapEnabled_Type()
)
trapProfile_L2tpTunnelTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapProfile_L2tpTunnelTrapEnabled.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBTRAP-MIB",
    **{"DisplayString": DisplayString,
       "mibtrapProfile": mibtrapProfile,
       "mibtrapProfileTable": mibtrapProfileTable,
       "mibtrapProfileEntry": mibtrapProfileEntry,
       "trapProfile-HostName": trapProfile_HostName,
       "trapProfile-ActiveEnabled": trapProfile_ActiveEnabled,
       "trapProfile-CommunityName": trapProfile_CommunityName,
       "trapProfile-HostAddress": trapProfile_HostAddress,
       "trapProfile-HostPort": trapProfile_HostPort,
       "trapProfile-InformTimeOut": trapProfile_InformTimeOut,
       "trapProfile-InformRetryCount": trapProfile_InformRetryCount,
       "trapProfile-NotifyTagList": trapProfile_NotifyTagList,
       "trapProfile-TargetParamsName": trapProfile_TargetParamsName,
       "trapProfile-AgentAddress": trapProfile_AgentAddress,
       "trapProfile-AlarmEnabled": trapProfile_AlarmEnabled,
       "trapProfile-SecurityEnabled": trapProfile_SecurityEnabled,
       "trapProfile-PortEnabled": trapProfile_PortEnabled,
       "trapProfile-SlotEnabled": trapProfile_SlotEnabled,
       "trapProfile-ColdstartEnabled": trapProfile_ColdstartEnabled,
       "trapProfile-WarmstartEnabled": trapProfile_WarmstartEnabled,
       "trapProfile-LinkdownEnabled": trapProfile_LinkdownEnabled,
       "trapProfile-LinkupEnabled": trapProfile_LinkupEnabled,
       "trapProfile-AscendEnabled": trapProfile_AscendEnabled,
       "trapProfile-ConsoleEnabled": trapProfile_ConsoleEnabled,
       "trapProfile-UseExceededEnabled": trapProfile_UseExceededEnabled,
       "trapProfile-PasswordEnabled": trapProfile_PasswordEnabled,
       "trapProfile-FrLinkupEnabled": trapProfile_FrLinkupEnabled,
       "trapProfile-FrLinkdownEnabled": trapProfile_FrLinkdownEnabled,
       "trapProfile-EventOverwriteEnabled": trapProfile_EventOverwriteEnabled,
       "trapProfile-RadiusChangeEnabled": trapProfile_RadiusChangeEnabled,
       "trapProfile-McastMonitorEnabled": trapProfile_McastMonitorEnabled,
       "trapProfile-LanModemEnabled": trapProfile_LanModemEnabled,
       "trapProfile-DirdoEnabled": trapProfile_DirdoEnabled,
       "trapProfile-SlotProfileChangeEnabled": trapProfile_SlotProfileChangeEnabled,
       "trapProfile-PowerSupplyEnabled": trapProfile_PowerSupplyEnabled,
       "trapProfile-MultishelfEnabled": trapProfile_MultishelfEnabled,
       "trapProfile-AuthenticationEnabled": trapProfile_AuthenticationEnabled,
       "trapProfile-ConfigChangeEnabled": trapProfile_ConfigChangeEnabled,
       "trapProfile-SysClockDriftEnabled": trapProfile_SysClockDriftEnabled,
       "trapProfile-PrimarySdtnEmptyEnabled": trapProfile_PrimarySdtnEmptyEnabled,
       "trapProfile-SecondarySdtnEmptyEnabled": trapProfile_SecondarySdtnEmptyEnabled,
       "trapProfile-SuspectAccessResourceEnabled": trapProfile_SuspectAccessResourceEnabled,
       "trapProfile-OspfEnabled": trapProfile_OspfEnabled,
       "trapProfile-OspfIfConfigErrorEnabled": trapProfile_OspfIfConfigErrorEnabled,
       "trapProfile-OspfIfAuthFailureEnabled": trapProfile_OspfIfAuthFailureEnabled,
       "trapProfile-OspfIfStateChangeEnabled": trapProfile_OspfIfStateChangeEnabled,
       "trapProfile-OspfIfRxBadPacket": trapProfile_OspfIfRxBadPacket,
       "trapProfile-OspfTxRetransmitEnabled": trapProfile_OspfTxRetransmitEnabled,
       "trapProfile-OspfNbrStateChangeEnabled": trapProfile_OspfNbrStateChangeEnabled,
       "trapProfile-OspfVirtIfConfigErrorEnabled": trapProfile_OspfVirtIfConfigErrorEnabled,
       "trapProfile-OspfVirtIfAuthFailureEnabled": trapProfile_OspfVirtIfAuthFailureEnabled,
       "trapProfile-OspfVirtIfStateChangeEnabled": trapProfile_OspfVirtIfStateChangeEnabled,
       "trapProfile-OspfVirtIfRxBadPacket": trapProfile_OspfVirtIfRxBadPacket,
       "trapProfile-OspfVirtIfTxRetransmitEnabled": trapProfile_OspfVirtIfTxRetransmitEnabled,
       "trapProfile-OspfVirtNbrStateChangeEnabled": trapProfile_OspfVirtNbrStateChangeEnabled,
       "trapProfile-OspfOriginateLsaEnabled": trapProfile_OspfOriginateLsaEnabled,
       "trapProfile-OspfMaxAgeLsaEnabled": trapProfile_OspfMaxAgeLsaEnabled,
       "trapProfile-OspfLsdbOverflowEnabled": trapProfile_OspfLsdbOverflowEnabled,
       "trapProfile-OspfApproachingOverflowEnabled": trapProfile_OspfApproachingOverflowEnabled,
       "trapProfile-WatchdogWarningEnabled": trapProfile_WatchdogWarningEnabled,
       "trapProfile-ControllerSwitchoverEnabled": trapProfile_ControllerSwitchoverEnabled,
       "trapProfile-CallLogServChangeEnabled": trapProfile_CallLogServChangeEnabled,
       "trapProfile-VoipGkChangeEnabled": trapProfile_VoipGkChangeEnabled,
       "trapProfile-WanLineStateChangeEnabled": trapProfile_WanLineStateChangeEnabled,
       "trapProfile-CallLogDroppedPktEnabled": trapProfile_CallLogDroppedPktEnabled,
       "trapProfile-LimSparingEnabled": trapProfile_LimSparingEnabled,
       "trapProfile-InterfaceSparingEnabled": trapProfile_InterfaceSparingEnabled,
       "trapProfile-MegacoLinkStatusEnabled": trapProfile_MegacoLinkStatusEnabled,
       "trapProfile-SecondaryControllerStateChangeEnabled": trapProfile_SecondaryControllerStateChangeEnabled,
       "trapProfile-PctfiTrunkStatusChangeEnabled": trapProfile_PctfiTrunkStatusChangeEnabled,
       "trapProfile-NoResourceAvailableEnabled": trapProfile_NoResourceAvailableEnabled,
       "trapProfile-DslThreshTrapEnabled": trapProfile_DslThreshTrapEnabled,
       "trapProfile-AtmPvcFailureTrapEnabled": trapProfile_AtmPvcFailureTrapEnabled,
       "trapProfile-AtmImaAlarmTrapEnabled": trapProfile_AtmImaAlarmTrapEnabled,
       "trapProfile-AscendLinkDownTrapEnabled": trapProfile_AscendLinkDownTrapEnabled,
       "trapProfile-AscendLinkUpTrapEnabled": trapProfile_AscendLinkUpTrapEnabled,
       "trapProfile-SnmpIllegalAccessAttempt": trapProfile_SnmpIllegalAccessAttempt,
       "trapProfile-Action-o": trapProfile_Action_o,
       "trapProfile-NotificationLogEnable": trapProfile_NotificationLogEnable,
       "trapProfile-NotificationLogLimit": trapProfile_NotificationLogLimit,
       "trapProfile-Hdsl2ShdslThresholdTrapsEnabled": trapProfile_Hdsl2ShdslThresholdTrapsEnabled,
       "trapProfile-ClockChangeTrapEnabled": trapProfile_ClockChangeTrapEnabled,
       "trapProfile-L2tpTunnelTrapEnabled": trapProfile_L2tpTunnelTrapEnabled}
)
