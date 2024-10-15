# SNMP MIB module (NAI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NAI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:01 2024
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

_Nai_ObjectIdentity = ObjectIdentity
nai = _Nai_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3401)
)
_NaiStandardTrap_ObjectIdentity = ObjectIdentity
naiStandardTrap = _NaiStandardTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3401, 1)
)


class _NaiTrapAgent_Type(DisplayString):
    """Custom type naiTrapAgent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_NaiTrapAgent_Type.__name__ = "DisplayString"
_NaiTrapAgent_Object = MibScalar
naiTrapAgent = _NaiTrapAgent_Object(
    (1, 3, 6, 1, 4, 1, 3401, 1, 1),
    _NaiTrapAgent_Type()
)
naiTrapAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naiTrapAgent.setStatus("mandatory")


class _NaiTrapAgentVersion_Type(DisplayString):
    """Custom type naiTrapAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_NaiTrapAgentVersion_Type.__name__ = "DisplayString"
_NaiTrapAgentVersion_Object = MibScalar
naiTrapAgentVersion = _NaiTrapAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 3401, 1, 2),
    _NaiTrapAgentVersion_Type()
)
naiTrapAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naiTrapAgentVersion.setStatus("mandatory")


class _NaiTrapSeverity_Type(Integer32):
    """Custom type naiTrapSeverity based on Integer32"""
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
        *(("critical", 5),
          ("inform", 1),
          ("major", 4),
          ("minor", 3),
          ("warning", 2))
    )


_NaiTrapSeverity_Type.__name__ = "Integer32"
_NaiTrapSeverity_Object = MibScalar
naiTrapSeverity = _NaiTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3401, 1, 3),
    _NaiTrapSeverity_Type()
)
naiTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naiTrapSeverity.setStatus("mandatory")


class _NaiTrapDescription_Type(DisplayString):
    """Custom type naiTrapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 300),
    )


_NaiTrapDescription_Type.__name__ = "DisplayString"
_NaiTrapDescription_Object = MibScalar
naiTrapDescription = _NaiTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 3401, 1, 4),
    _NaiTrapDescription_Type()
)
naiTrapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naiTrapDescription.setStatus("mandatory")
_NaiTrapAlarmSourceAddress_Type = OctetString
_NaiTrapAlarmSourceAddress_Object = MibScalar
naiTrapAlarmSourceAddress = _NaiTrapAlarmSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 3401, 1, 5),
    _NaiTrapAlarmSourceAddress_Type()
)
naiTrapAlarmSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naiTrapAlarmSourceAddress.setStatus("mandatory")
_NaiTrapAlarmSourceDNSName_Type = OctetString
_NaiTrapAlarmSourceDNSName_Object = MibScalar
naiTrapAlarmSourceDNSName = _NaiTrapAlarmSourceDNSName_Object(
    (1, 3, 6, 1, 4, 1, 3401, 1, 6),
    _NaiTrapAlarmSourceDNSName_Type()
)
naiTrapAlarmSourceDNSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naiTrapAlarmSourceDNSName.setStatus("mandatory")
_NaiTrapGMTTime_Type = TimeTicks
_NaiTrapGMTTime_Object = MibScalar
naiTrapGMTTime = _NaiTrapGMTTime_Object(
    (1, 3, 6, 1, 4, 1, 3401, 1, 7),
    _NaiTrapGMTTime_Type()
)
naiTrapGMTTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naiTrapGMTTime.setStatus("mandatory")
_NaiTrapLocalTime_Type = TimeTicks
_NaiTrapLocalTime_Object = MibScalar
naiTrapLocalTime = _NaiTrapLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 3401, 1, 8),
    _NaiTrapLocalTime_Type()
)
naiTrapLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naiTrapLocalTime.setStatus("mandatory")
_NaiTrapURL_Type = OctetString
_NaiTrapURL_Object = MibScalar
naiTrapURL = _NaiTrapURL_Object(
    (1, 3, 6, 1, 4, 1, 3401, 1, 9),
    _NaiTrapURL_Type()
)
naiTrapURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naiTrapURL.setStatus("mandatory")
_NaiTrapPseudoID_Type = Integer32
_NaiTrapPseudoID_Object = MibScalar
naiTrapPseudoID = _NaiTrapPseudoID_Object(
    (1, 3, 6, 1, 4, 1, 3401, 1, 10),
    _NaiTrapPseudoID_Type()
)
naiTrapPseudoID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    naiTrapPseudoID.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NAI-MIB",
    **{"nai": nai,
       "naiStandardTrap": naiStandardTrap,
       "naiTrapAgent": naiTrapAgent,
       "naiTrapAgentVersion": naiTrapAgentVersion,
       "naiTrapSeverity": naiTrapSeverity,
       "naiTrapDescription": naiTrapDescription,
       "naiTrapAlarmSourceAddress": naiTrapAlarmSourceAddress,
       "naiTrapAlarmSourceDNSName": naiTrapAlarmSourceDNSName,
       "naiTrapGMTTime": naiTrapGMTTime,
       "naiTrapLocalTime": naiTrapLocalTime,
       "naiTrapURL": naiTrapURL,
       "naiTrapPseudoID": naiTrapPseudoID}
)
