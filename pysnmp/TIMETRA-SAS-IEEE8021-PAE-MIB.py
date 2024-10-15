# SNMP MIB module (TIMETRA-SAS-IEEE8021-PAE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-SAS-IEEE8021-PAE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:04:23 2024
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

(dot1xAuthConfigEntry,) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xAuthConfigEntry")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(timetraSASConfs,
 timetraSASModules,
 timetraSASNotifyPrefix,
 timetraSASObjs) = mibBuilder.importSymbols(
    "TIMETRA-SAS-GLOBAL-MIB",
    "timetraSASConfs",
    "timetraSASModules",
    "timetraSASNotifyPrefix",
    "timetraSASObjs")

(ServiceAdminStatus,
 TNamedItem,
 TPolicyStatementNameOrEmpty) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "ServiceAdminStatus",
    "TNamedItem",
    "TPolicyStatementNameOrEmpty")


# MODULE-IDENTITY

timeraSASIEEE8021PaeMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 17)
)
timeraSASIEEE8021PaeMIBModule.setRevisions(
        ("1912-07-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxSASDot1xConformance_ObjectIdentity = ObjectIdentity
tmnxSASDot1xConformance = _TmnxSASDot1xConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 12)
)
_TmnxDot1xSASCompliancs_ObjectIdentity = ObjectIdentity
tmnxDot1xSASCompliancs = _TmnxDot1xSASCompliancs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 12, 1)
)
_TmnxDot1xSASGroups_ObjectIdentity = ObjectIdentity
tmnxDot1xSASGroups = _TmnxDot1xSASGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 12, 2)
)
_TmnxSASDot1xObjs_ObjectIdentity = ObjectIdentity
tmnxSASDot1xObjs = _TmnxSASDot1xObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 16)
)
_TmnxSASDot1xAuthenticatorObjs_ObjectIdentity = ObjectIdentity
tmnxSASDot1xAuthenticatorObjs = _TmnxSASDot1xAuthenticatorObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 16, 1)
)
_Dot1xAuthConfigExtnTable_Object = MibTable
dot1xAuthConfigExtnTable = _Dot1xAuthConfigExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 16, 1, 1)
)
if mibBuilder.loadTexts:
    dot1xAuthConfigExtnTable.setStatus("current")
_Dot1xAuthConfigExtnEntry_Object = MibTableRow
dot1xAuthConfigExtnEntry = _Dot1xAuthConfigExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 16, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dot1xAuthConfigExtnEntry.setStatus("current")


class _Dot1xPortEtherTunnel_Type(TruthValue):
    """Custom type dot1xPortEtherTunnel based on TruthValue"""


_Dot1xPortEtherTunnel_Object = MibTableColumn
dot1xPortEtherTunnel = _Dot1xPortEtherTunnel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 16, 1, 1, 1, 150),
    _Dot1xPortEtherTunnel_Type()
)
dot1xPortEtherTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xPortEtherTunnel.setStatus("current")
dot1xAuthConfigEntry.registerAugmentions(
    ("TIMETRA-SAS-IEEE8021-PAE-MIB",
     "dot1xAuthConfigExtnEntry")
)
dot1xAuthConfigExtnEntry.setIndexNames(*dot1xAuthConfigEntry.getIndexNames())

# Managed Objects groups

dot1xAuthConfigExtnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 12, 2, 1)
)
dot1xAuthConfigExtnGroup.setObjects(
    ("TIMETRA-SAS-IEEE8021-PAE-MIB", "dot1xPortEtherTunnel")
)
if mibBuilder.loadTexts:
    dot1xAuthConfigExtnGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dot1xAuthConfigExtnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 12, 1, 1)
)
if mibBuilder.loadTexts:
    dot1xAuthConfigExtnCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SAS-IEEE8021-PAE-MIB",
    **{"timeraSASIEEE8021PaeMIBModule": timeraSASIEEE8021PaeMIBModule,
       "tmnxSASDot1xConformance": tmnxSASDot1xConformance,
       "tmnxDot1xSASCompliancs": tmnxDot1xSASCompliancs,
       "dot1xAuthConfigExtnCompliance": dot1xAuthConfigExtnCompliance,
       "tmnxDot1xSASGroups": tmnxDot1xSASGroups,
       "dot1xAuthConfigExtnGroup": dot1xAuthConfigExtnGroup,
       "tmnxSASDot1xObjs": tmnxSASDot1xObjs,
       "tmnxSASDot1xAuthenticatorObjs": tmnxSASDot1xAuthenticatorObjs,
       "dot1xAuthConfigExtnTable": dot1xAuthConfigExtnTable,
       "dot1xAuthConfigExtnEntry": dot1xAuthConfigExtnEntry,
       "dot1xPortEtherTunnel": dot1xPortEtherTunnel}
)
