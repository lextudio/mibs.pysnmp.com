# SNMP MIB module (CADANT-CMTS-PCMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-CMTS-PCMM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:46 2024
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

(cadPCMibObjects,) = mibBuilder.importSymbols(
    "CADANT-CMTS-PACKETCABLE-MIB",
    "cadPCMibObjects")

(AdminState,) = mibBuilder.importSymbols(
    "CADANT-TC",
    "AdminState")

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

cadPCMMMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 3)
)
cadPCMMMib.setRevisions(
        ("2010-06-01 00:00",
         "2009-10-19 00:00",
         "2009-09-21 00:00",
         "2005-03-11 00:00",
         "2004-05-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CopsVersion(Integer32, TextualConvention):
    status = "current"
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
        *(("i02", 1),
          ("i03", 2),
          ("i04", 3),
          ("i05", 4))
    )



# MIB Managed Objects in the order of their OIDs

_CadPCMMMibObjects_ObjectIdentity = ObjectIdentity
cadPCMMMibObjects = _CadPCMMMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 3, 1)
)
_CadPCMMConfigBase_ObjectIdentity = ObjectIdentity
cadPCMMConfigBase = _CadPCMMConfigBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 3, 1, 1)
)


class _CadPCMMAdminState_Type(AdminState):
    """Custom type cadPCMMAdminState based on AdminState"""


_CadPCMMAdminState_Object = MibScalar
cadPCMMAdminState = _CadPCMMAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 3, 1, 1, 1),
    _CadPCMMAdminState_Type()
)
cadPCMMAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCMMAdminState.setStatus("current")


class _CadPCMMTimerT1_Type(Unsigned32):
    """Custom type cadPCMMTimerT1 based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3000),
    )


_CadPCMMTimerT1_Type.__name__ = "Unsigned32"
_CadPCMMTimerT1_Object = MibScalar
cadPCMMTimerT1 = _CadPCMMTimerT1_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 3, 1, 1, 2),
    _CadPCMMTimerT1_Type()
)
cadPCMMTimerT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCMMTimerT1.setStatus("current")
if mibBuilder.loadTexts:
    cadPCMMTimerT1.setUnits("deciseconds")


class _CadPCMMCopsVersion_Type(CopsVersion):
    """Custom type cadPCMMCopsVersion based on CopsVersion"""


_CadPCMMCopsVersion_Object = MibScalar
cadPCMMCopsVersion = _CadPCMMCopsVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 3, 1, 1, 3),
    _CadPCMMCopsVersion_Type()
)
cadPCMMCopsVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCMMCopsVersion.setStatus("current")


class _CadPCMMSubscriberIdVrfName_Type(DisplayString):
    """Custom type cadPCMMSubscriberIdVrfName based on DisplayString"""
    defaultValue = OctetString("default")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CadPCMMSubscriberIdVrfName_Type.__name__ = "DisplayString"
_CadPCMMSubscriberIdVrfName_Object = MibScalar
cadPCMMSubscriberIdVrfName = _CadPCMMSubscriberIdVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 115, 1, 3, 1, 1, 4),
    _CadPCMMSubscriberIdVrfName_Type()
)
cadPCMMSubscriberIdVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadPCMMSubscriberIdVrfName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-CMTS-PCMM-MIB",
    **{"CopsVersion": CopsVersion,
       "cadPCMMMib": cadPCMMMib,
       "cadPCMMMibObjects": cadPCMMMibObjects,
       "cadPCMMConfigBase": cadPCMMConfigBase,
       "cadPCMMAdminState": cadPCMMAdminState,
       "cadPCMMTimerT1": cadPCMMTimerT1,
       "cadPCMMCopsVersion": cadPCMMCopsVersion,
       "cadPCMMSubscriberIdVrfName": cadPCMMSubscriberIdVrfName}
)
