# SNMP MIB module (ALCATEL-IND1-SSH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-SSH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:06 2024
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

(softentIND1Ssh,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Ssh")

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

alcatelIND1SshMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1)
)
alcatelIND1SshMIB.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1SshMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1SshMIBObjects = _AlcatelIND1SshMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SshMIBObjects.setStatus("current")


class _AlaSshAdminStatus_Type(Integer32):
    """Custom type alaSshAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AlaSshAdminStatus_Type.__name__ = "Integer32"
_AlaSshAdminStatus_Object = MibScalar
alaSshAdminStatus = _AlaSshAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 1, 1),
    _AlaSshAdminStatus_Type()
)
alaSshAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaSshAdminStatus.setStatus("current")


class _AlaScpSftpAdminStatus_Type(Integer32):
    """Custom type alaScpSftpAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AlaScpSftpAdminStatus_Type.__name__ = "Integer32"
_AlaScpSftpAdminStatus_Object = MibScalar
alaScpSftpAdminStatus = _AlaScpSftpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 1, 2),
    _AlaScpSftpAdminStatus_Type()
)
alaScpSftpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaScpSftpAdminStatus.setStatus("current")


class _AlaSshPubKeyEnforceAdminStatus_Type(Integer32):
    """Custom type alaSshPubKeyEnforceAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AlaSshPubKeyEnforceAdminStatus_Type.__name__ = "Integer32"
_AlaSshPubKeyEnforceAdminStatus_Object = MibScalar
alaSshPubKeyEnforceAdminStatus = _AlaSshPubKeyEnforceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 1, 3),
    _AlaSshPubKeyEnforceAdminStatus_Type()
)
alaSshPubKeyEnforceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaSshPubKeyEnforceAdminStatus.setStatus("current")
_AlcatelIND1SshMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1SshMIBConformance = _AlcatelIND1SshMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1SshMIBConformance.setStatus("current")
_AlcatelIND1SshMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1SshMIBGroups = _AlcatelIND1SshMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SshMIBGroups.setStatus("current")
_AlcatelIND1SshMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1SshMIBCompliances = _AlcatelIND1SshMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1SshMIBCompliances.setStatus("current")

# Managed Objects groups

alaSshConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 2, 1, 1)
)
alaSshConfigGroup.setObjects(
      *(("ALCATEL-IND1-SSH-MIB", "alaSshAdminStatus"),
        ("ALCATEL-IND1-SSH-MIB", "alaScpSftpAdminStatus"),
        ("ALCATEL-IND1-SSH-MIB", "alaSshPubKeyEnforceAdminStatus"))
)
if mibBuilder.loadTexts:
    alaSshConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1SshMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SshMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-SSH-MIB",
    **{"alcatelIND1SshMIB": alcatelIND1SshMIB,
       "alcatelIND1SshMIBObjects": alcatelIND1SshMIBObjects,
       "alaSshAdminStatus": alaSshAdminStatus,
       "alaScpSftpAdminStatus": alaScpSftpAdminStatus,
       "alaSshPubKeyEnforceAdminStatus": alaSshPubKeyEnforceAdminStatus,
       "alcatelIND1SshMIBConformance": alcatelIND1SshMIBConformance,
       "alcatelIND1SshMIBGroups": alcatelIND1SshMIBGroups,
       "alaSshConfigGroup": alaSshConfigGroup,
       "alcatelIND1SshMIBCompliances": alcatelIND1SshMIBCompliances,
       "alcatelIND1SshMIBCompliance": alcatelIND1SshMIBCompliance}
)
